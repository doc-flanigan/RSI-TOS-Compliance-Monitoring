from __future__ import annotations

import base64
import os
from dataclasses import dataclass, field
from typing import Optional

import requests

from . import policy

API = "https://api.github.com"


@dataclass
class RepoFinding:
    rule: str
    status: str
    detail: str


@dataclass
class RepoResult:
    full_name: str
    findings: list[RepoFinding] = field(default_factory=list)


def _headers() -> dict[str, str]:
    h = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "rsi-compliance-auditor",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def _get_json(path: str):
    r = requests.get(f"{API}{path}", headers=_headers(), timeout=15)
    return r.json() if r.status_code == 200 else None


def _get_readme(full_name: str) -> Optional[str]:
    data = _get_json(f"/repos/{full_name}/readme")
    if not data or "content" not in data:
        return None
    return base64.b64decode(data["content"]).decode("utf-8", errors="replace")


def audit_repo(full_name: str) -> RepoResult:
    result = RepoResult(full_name=full_name)
    repo = _get_json(f"/repos/{full_name}")
    if not repo:
        result.findings.append(RepoFinding("fetch", "fail", "Could not fetch repository metadata"))
        return result

    name_lower = repo.get("name", "").lower()
    matched_tm = next(
        (tm for tm in policy.RSI_TRADEMARKS if tm.replace(" ", "") in name_lower.replace(" ", "")),
        None,
    )
    if matched_tm:
        result.findings.append(
            RepoFinding("ip_trademarks_in_name", "fail", f"Repo name contains RSI trademark '{matched_tm}'")
        )
    else:
        result.findings.append(RepoFinding("ip_trademarks_in_name", "pass", "No RSI trademarks in repo name"))

    license_info = repo.get("license") or {}
    spdx = license_info.get("spdx_id")
    if spdx and spdx != "NOASSERTION":
        result.findings.append(RepoFinding("license", "pass", f"License: {spdx}"))
    else:
        result.findings.append(RepoFinding("license", "warn", "No identifiable license — add one to clarify reuse terms"))

    readme = _get_readme(full_name)
    if not readme:
        result.findings.append(RepoFinding("disclaimer", "warn", "No README found — disclaimer presence cannot be verified"))
    else:
        rl = readme.lower()
        has_rsi_refs = any(tm in rl for tm in policy.RSI_TRADEMARKS)
        has_disclaimer = any(p.search(readme) for p in policy.DISCLAIMER_PATTERNS)

        if has_disclaimer:
            result.findings.append(RepoFinding("disclaimer", "pass", "Fan-site disclaimer found in README"))
        elif has_rsi_refs:
            result.findings.append(
                RepoFinding("disclaimer", "fail", "README references RSI trademarks but contains no fan-site disclaimer")
            )
        else:
            result.findings.append(RepoFinding("disclaimer", "pass", "No RSI trademarks referenced; disclaimer not required"))

        if any(ind in rl for ind in policy.SQUADRON_42_INDICATORS):
            result.findings.append(
                RepoFinding("content_squadron42", "warn", "README references Squadron 42 — verify no SQ42 assets are reproduced")
            )

    return result


def audit_all(repos: list[str]) -> list[RepoResult]:
    return [audit_repo(r) for r in repos]
