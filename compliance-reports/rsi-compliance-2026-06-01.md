# RSI Compliance Audit — 2026-06-01

## Audit Metadata
- **Date:** 2026-06-01
- **Sites Audited:** 14
- **Repos Audited:** 0
- **Auditor:** automated `compliance` tool (Playwright-backed fetch)

## Policy Reference Baseline

| Rule | RSI Requirement |
|------|-----------------|
| Non-Commercial | No ads, paywalls, merchandise sales, or fees using RSI IP |
| IP & Trademarks | RSI trademarks must not appear in domain or business names |
| Referral Program | One code per account; honest disclosure; correct enlist URL |
| Content Rules | No Squadron 42 assets; no RSI marketing materials |
| Disclaimer | Visible: 'Unofficial fan site, not affiliated with or endorsed by RSI/CIG' |

## Portfolio Summary

| Target | Severity | Notes |
|--------|----------|-------|
| heldtheline.com | **FAIL** | fetched via `blocked` |
| iheldtheline.com | **WARN** | fetched via `requests` |
| 42ndsquadron.com | **FAIL** | fetched via `blocked` |
| screferralbonus.com | **FAIL** | fetched via `blocked` |
| screferralreward.com | **PASS** | fetched via `requests` |
| o7citizen.gg | **FAIL** | fetched via `blocked` |
| bestspacesim.com | **PASS** | fetched via `requests` |
| freeflyevent.com | **PASS** | fetched via `requests` |
| pledgemeaning.com | **WARN** | fetched via `requests` |
| highestfundedgame.com | **PASS** | fetched via `requests` |
| mostfundedgame.com | **PASS** | fetched via `requests` |
| o7meaning.com | **PASS** | fetched via `requests` |
| o7citizens.com | **FAIL** | fetched via `blocked` |
| o7citizen.com | **WARN** | fetched via `requests` |

## Site Audits

### heldtheline.com

- URL: <https://heldtheline.com>
- Fetched via: `blocked` (HTTP None)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `fetch` | **FAIL** | Could not fetch live content (HTTP None) — content checks skipped |

### iheldtheline.com

- URL: <https://iheldtheline.com>
- Fetched via: `requests` (HTTP 200)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `disclaimer` | **PASS** | Fan-site disclaimer detected |
| `non_commercial_ads` | **PASS** | No ad-network references detected |
| `content_squadron42` | **WARN** | Squadron 42 references detected — verify no protected SQ42 assets are reproduced |
| `referral_program` | **PASS** | Referral link uses correct enlist URL (code STAR-GCQJ-N6NC) |

### 42ndsquadron.com

- URL: <https://42ndsquadron.com>
- Fetched via: `blocked` (HTTP None)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `fetch` | **FAIL** | Could not fetch live content (HTTP None) — content checks skipped |

### screferralbonus.com

- URL: <https://screferralbonus.com>
- Fetched via: `blocked` (HTTP None)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `fetch` | **FAIL** | Could not fetch live content (HTTP None) — content checks skipped |

### screferralreward.com

- URL: <https://screferralreward.com>
- Fetched via: `requests` (HTTP 200)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `disclaimer` | **PASS** | Fan-site disclaimer detected |
| `non_commercial_ads` | **PASS** | No ad-network references detected |
| `referral_program` | **PASS** | Referral link uses correct enlist URL (code STAR-GCQJ-N6NC) |

### o7citizen.gg

- URL: <https://o7citizen.gg>
- Fetched via: `blocked` (HTTP None)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `fetch` | **FAIL** | Could not fetch live content (HTTP None) — content checks skipped |

### bestspacesim.com

- URL: <https://bestspacesim.com>
- Fetched via: `requests` (HTTP 200)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `disclaimer` | **PASS** | Fan-site disclaimer detected |
| `non_commercial_ads` | **PASS** | No ad-network references detected |
| `referral_program` | **PASS** | Referral link uses correct enlist URL (code STAR-GCQJ-N6NC) |

### freeflyevent.com

- URL: <https://freeflyevent.com>
- Fetched via: `requests` (HTTP 200)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `disclaimer` | **PASS** | Fan-site disclaimer detected |
| `non_commercial_ads` | **PASS** | No ad-network references detected |
| `referral_program` | **PASS** | Referral link uses correct enlist URL (code STAR-GCQJ-N6NC) |

### pledgemeaning.com

- URL: <https://pledgemeaning.com>
- Fetched via: `requests` (HTTP 200)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `disclaimer` | **PASS** | Fan-site disclaimer detected |
| `non_commercial_ads` | **PASS** | No ad-network references detected |
| `content_squadron42` | **WARN** | Squadron 42 references detected — verify no protected SQ42 assets are reproduced |
| `referral_program` | **PASS** | Referral link uses correct enlist URL (code STAR-GCQJ-N6NC) |

### highestfundedgame.com

- URL: <https://highestfundedgame.com>
- Fetched via: `requests` (HTTP 200)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `disclaimer` | **PASS** | Fan-site disclaimer detected |
| `non_commercial_ads` | **PASS** | No ad-network references detected |
| `referral_program` | **PASS** | Referral link uses correct enlist URL (code STAR-GCQJ-N6NC) |

### mostfundedgame.com

- URL: <https://mostfundedgame.com>
- Fetched via: `requests` (HTTP 200)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `disclaimer` | **PASS** | Fan-site disclaimer detected |
| `non_commercial_ads` | **PASS** | No ad-network references detected |
| `referral_program` | **PASS** | Referral link uses correct enlist URL (code STAR-GCQJ-N6NC) |

### o7meaning.com

- URL: <https://o7meaning.com>
- Fetched via: `requests` (HTTP 200)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `disclaimer` | **PASS** | Fan-site disclaimer detected |
| `non_commercial_ads` | **PASS** | No ad-network references detected |
| `referral_program` | **PASS** | Referral link uses correct enlist URL (code STAR-GCQJ-N6NC) |

### o7citizens.com

- URL: <https://o7citizens.com>
- Fetched via: `blocked` (HTTP None)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `fetch` | **FAIL** | Could not fetch live content (HTTP None) — content checks skipped |

### o7citizen.com

- URL: <https://o7citizen.com>
- Fetched via: `requests` (HTTP 200)

| Rule | Status | Detail |
|------|--------|--------|
| `ip_trademarks_in_domain` | **PASS** | No RSI trademark tokens in domain |
| `disclaimer` | **PASS** | Fan-site disclaimer detected |
| `non_commercial_ads` | **PASS** | No ad-network references detected |
| `content_squadron42` | **WARN** | Squadron 42 references detected — verify no protected SQ42 assets are reproduced |
| `referral_program` | **PASS** | Referral link uses correct enlist URL (code STAR-GCQJ-N6NC) |


---
*Generated automatically. Not legal advice.*
