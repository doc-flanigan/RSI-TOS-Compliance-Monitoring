from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import Optional
from urllib.parse import urlparse

import requests

from . import policy

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


@dataclass
class Finding:
    rule: str
    status: str  # "pass" | "warn" | "fail"
    detail: str


@dataclass
class SiteResult:
    domain: str
    url: str
    fetched_via: str  # "requests" | "playwright" | "blocked" | "error"
    http_status: Optional[int]
    findings: list[Finding] = field(default_factory=list)


def _normalize(domain: str) -> str:
    return domain if domain.startswith("http") else f"https://{domain}"


def _try_requests(url: str) -> tuple[Optional[int], Optional[str]]:
    try:
        r = requests.get(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/html,application/xhtml+xml",
                "Accept-Language": "en-US,en;q=0.9",
            },
            timeout=15,
            allow_redirects=True,
        )
        return r.status_code, r.text if r.status_code == 200 else None
    except requests.RequestException:
        return None, None


async def _try_playwright(url: str) -> tuple[Optional[int], Optional[str]]:
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"],
        )
        ctx = await browser.new_context(
            user_agent=USER_AGENT,
            viewport={"width": 1280, "height": 800},
            locale="en-US",
        )
        page = await ctx.new_page()
        try:
            response = await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            # Give Cloudflare challenge pages a moment to resolve.
            await page.wait_for_timeout(4000)
            html = await page.content()
            status = response.status if response else None
            return status, html
        except Exception as exc:  # network/timeout/navigation error
            return None, f"<!-- playwright error: {exc} -->"
        finally:
            await browser.close()


def _bare_domain(netloc: str) -> str:
    return netloc.lower().removeprefix("www.")


def _domain_checks(netloc: str) -> list[Finding]:
    findings: list[Finding] = []
    bare = _bare_domain(netloc)
    label = bare.split(".")[0]

    matched_tm = next((tm for tm in policy.RSI_TRADEMARKS if tm.replace(" ", "") in label), None)
    if matched_tm:
        findings.append(
            Finding(
                "ip_trademarks_in_domain",
                "fail",
                f"Domain label contains RSI trademark token '{matched_tm}'",
            )
        )
    else:
        findings.append(Finding("ip_trademarks_in_domain", "pass", "No RSI trademark tokens in domain"))

    commercial_token = next((t for t in policy.COMMERCIAL_DOMAIN_TOKENS if t in label), None)
    if commercial_token:
        findings.append(
            Finding(
                "non_commercial_domain",
                "warn",
                f"Domain label contains commercial token '{commercial_token}' — verify the site is not selling RSI IP",
            )
        )
    return findings


def _content_checks(html: str) -> list[Finding]:
    findings: list[Finding] = []
    text = html.lower()

    if any(p.search(html) for p in policy.DISCLAIMER_PATTERNS):
        findings.append(Finding("disclaimer", "pass", "Fan-site disclaimer detected"))
    else:
        findings.append(
            Finding(
                "disclaimer",
                "fail",
                "Required RSI fan-site disclaimer not found ('unofficial fan site, not affiliated with RSI/CIG')",
            )
        )

    ad_hits = [ad for ad in policy.AD_NETWORK_INDICATORS if ad in text]
    if ad_hits:
        findings.append(
            Finding("non_commercial_ads", "fail", f"Ad-network references detected: {', '.join(ad_hits[:3])}")
        )
    else:
        findings.append(Finding("non_commercial_ads", "pass", "No ad-network references detected"))

    commercial_hits = [kw for kw in policy.COMMERCIAL_KEYWORDS if kw in text]
    if commercial_hits:
        findings.append(
            Finding(
                "non_commercial_language",
                "warn",
                f"Commercial / monetization language: {', '.join(commercial_hits)}",
            )
        )

    if any(ind in text for ind in policy.SQUADRON_42_INDICATORS):
        findings.append(
            Finding(
                "content_squadron42",
                "warn",
                "Squadron 42 references detected — verify no protected SQ42 assets are reproduced",
            )
        )

    referral_codes = set(policy.REFERRAL_URL_RE.findall(html))
    other_rsi_links = [
        m for m in policy.RSI_LINK_RE.findall(html) if "/enlist?referral=" not in m.lower()
    ]
    if len(referral_codes) > 1:
        findings.append(
            Finding(
                "referral_program",
                "fail",
                f"Multiple referral codes detected ({', '.join(sorted(referral_codes))}) — RSI permits one code per account",
            )
        )
    elif referral_codes:
        findings.append(
            Finding(
                "referral_program",
                "pass",
                f"Referral link uses correct enlist URL (code {next(iter(referral_codes))})",
            )
        )
    elif other_rsi_links:
        findings.append(
            Finding(
                "referral_program",
                "warn",
                "RSI links present but no /enlist?referral=CODE format detected",
            )
        )

    return findings


async def audit_site(domain: str) -> SiteResult:
    url = _normalize(domain)
    netloc = urlparse(url).netloc
    result = SiteResult(domain=netloc, url=url, fetched_via="blocked", http_status=None)
    result.findings.extend(_domain_checks(netloc))

    status, html = _try_requests(url)
    if status == 200 and html:
        result.fetched_via = "requests"
        result.http_status = status
    else:
        pw_status, pw_html = await _try_playwright(url)
        if pw_status == 200 and pw_html:
            result.fetched_via = "playwright"
            result.http_status = pw_status
            html = pw_html
            status = pw_status
        else:
            result.http_status = pw_status if pw_status is not None else status

    if status == 200 and html:
        result.findings.extend(_content_checks(html))
    else:
        result.findings.append(
            Finding(
                "fetch",
                "fail",
                f"Could not fetch live content (HTTP {result.http_status}) — content checks skipped",
            )
        )
    return result


async def audit_all(domains: list[str]) -> list[SiteResult]:
    results: list[SiteResult] = []
    for d in domains:
        try:
            results.append(await audit_site(d))
        except Exception as exc:  # one bad site shouldn't kill the audit
            r = SiteResult(domain=d, url=_normalize(d), fetched_via="error", http_status=None)
            r.findings.append(Finding("fetch", "fail", f"Audit error: {exc}"))
            results.append(r)
    return results
