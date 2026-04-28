from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .repo_checker import RepoResult
from .site_checker import SiteResult

STATUS_LABEL = {"pass": "PASS", "warn": "WARN", "fail": "FAIL"}
SEVERITY_RANK = {"pass": 0, "warn": 1, "fail": 2}


@dataclass
class _Section:
    title: str
    body: str


def _worst(findings) -> str:
    if not findings:
        return "pass"
    return max((f.status for f in findings), key=lambda s: SEVERITY_RANK.get(s, 0))


def _findings_table(findings) -> str:
    rows = ["| Rule | Status | Detail |", "|------|--------|--------|"]
    for f in findings:
        detail = f.detail.replace("|", "\\|")
        rows.append(f"| `{f.rule}` | **{STATUS_LABEL.get(f.status, f.status)}** | {detail} |")
    return "\n".join(rows)


def _site_section(r: SiteResult) -> str:
    return (
        f"### {r.domain}\n\n"
        f"- URL: <{r.url}>\n"
        f"- Fetched via: `{r.fetched_via}` (HTTP {r.http_status})\n\n"
        f"{_findings_table(r.findings)}\n"
    )


def _repo_section(r: RepoResult) -> str:
    return f"### {r.full_name}\n\n{_findings_table(r.findings)}\n"


def _summary_table(site_results, repo_results) -> str:
    rows = ["| Target | Severity | Notes |", "|--------|----------|-------|"]
    for r in site_results:
        sev = _worst(r.findings)
        notes = f"fetched via `{r.fetched_via}`"
        rows.append(f"| {r.domain} | **{STATUS_LABEL[sev]}** | {notes} |")
    for r in repo_results:
        sev = _worst(r.findings)
        rows.append(f"| {r.full_name} (repo) | **{STATUS_LABEL[sev]}** | |")
    return "\n".join(rows)


def write_reports(site_results: list[SiteResult], repo_results: list[RepoResult], reports_dir: Path) -> Path:
    reports_dir.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    report_path = reports_dir / f"rsi-compliance-{today}.md"

    parts = [
        f"# RSI Compliance Audit — {today}",
        "",
        "## Audit Metadata",
        f"- **Date:** {today}",
        f"- **Sites Audited:** {len(site_results)}",
        f"- **Repos Audited:** {len(repo_results)}",
        "- **Auditor:** automated `compliance` tool (Playwright-backed fetch)",
        "",
        "## Policy Reference Baseline",
        "",
        "| Rule | RSI Requirement |",
        "|------|-----------------|",
        "| Non-Commercial | No ads, paywalls, merchandise sales, or fees using RSI IP |",
        "| IP & Trademarks | RSI trademarks must not appear in domain or business names |",
        "| Referral Program | One code per account; honest disclosure; correct enlist URL |",
        "| Content Rules | No Squadron 42 assets; no RSI marketing materials |",
        "| Disclaimer | Visible: 'Unofficial fan site, not affiliated with or endorsed by RSI/CIG' |",
        "",
        "## Portfolio Summary",
        "",
        _summary_table(site_results, repo_results),
        "",
        "## Site Audits",
        "",
    ]
    parts.extend(_site_section(r) for r in site_results)

    if repo_results:
        parts.append("## Repository Audits\n")
        parts.extend(_repo_section(r) for r in repo_results)

    parts.extend(["", "---", "*Generated automatically. Not legal advice.*", ""])
    report_path.write_text("\n".join(parts))

    _write_urgent(site_results, repo_results, reports_dir, today)
    return report_path


def _write_urgent(site_results, repo_results, reports_dir: Path, today: str) -> None:
    lines = [
        "# URGENT — RSI Compliance Action Required",
        f"**Generated:** {today}",
        f"**Full Report:** [rsi-compliance-{today}.md](./rsi-compliance-{today}.md)",
        "",
        "## Critical Findings (FAIL)",
        "",
    ]
    any_fail = False
    for r in site_results:
        crit = [f for f in r.findings if f.status == "fail"]
        if crit:
            any_fail = True
            lines.append(f"### {r.domain}")
            for f in crit:
                lines.append(f"- **{f.rule}**: {f.detail}")
            lines.append("")
    for r in repo_results:
        crit = [f for f in r.findings if f.status == "fail"]
        if crit:
            any_fail = True
            lines.append(f"### {r.full_name} (repo)")
            for f in crit:
                lines.append(f"- **{f.rule}**: {f.detail}")
            lines.append("")
    if not any_fail:
        lines.append("No FAIL-severity findings in this audit cycle.")
    lines.extend(["", "---", "*Not legal advice.*", ""])
    (reports_dir / "URGENT-action-needed.md").write_text("\n".join(lines))
