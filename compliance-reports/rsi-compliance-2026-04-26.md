# RSI Compliance Audit — 2026-04-26

## Audit Metadata
- **Date:** 2026-04-26
- **Auditor:** Automated Compliance Agent
- **Branch:** claude/setup-compliance-auditor-UHr3g
- **Sites Audited:** 6
- **Live Content Fetch:** ❌ Blocked (403 — WAF/Cloudflare on all sites)
- **Audit Basis:** Domain-name analysis + known RSI policy baseline; manual content review required for full sign-off

> **Important:** All 6 sites returned HTTP 403 to the automated fetch agent (consistent with Cloudflare or equivalent WAF protection). Compliance findings below are based on domain-name-level signals and applicable RSI policy rules. Items marked ⚠️ require manual content verification. Items marked ❌ represent concerns identifiable from the domain/name alone and should be addressed regardless of content.

---

## Policy Reference Baseline

| Rule | RSI Requirement |
|------|----------------|
| Non-Commercial | No ads, paywalls, merchandise sales, or fees using RSI IP |
| IP & Trademarks | RSI trademarks must not appear in domain or business names; must not imply official affiliation |
| Referral Program | One code per account; honest disclosure; correct enlist URL; no false UEC claims |
| Content Rules | No Squadron 42 assets; no RSI marketing materials; no defamatory content |
| Disclaimer | Visible on every page: "Unofficial fan site not affiliated with or endorsed by RSI/CIG" |

---

## Site Audits

---

### 1. www.starcitizenhelp.com

| Check | Status | Notes |
|-------|--------|-------|
| Non-Commercial | ⚠️ Needs Review | Could not fetch live content. Verify no display ads, paywalls, or paid services are present. |
| IP & Trademarks | ⚠️ Needs Review | Domain contains "Star Citizen" — RSI policy prohibits trademark use in domain names. Assess whether RSI has previously objected; many help-oriented fan domains exist in a grey area but this is technically non-compliant. No official RSI approval on record. |
| Referral Program | ⚠️ Needs Review | Could not verify referral link presence, UEC claim accuracy, or enlist URL correctness. |
| Content Rules | ⚠️ Needs Review | Could not verify absence of Squadron 42 content or reproduced marketing materials. |
| Fansite Disclaimer | ⚠️ Needs Review | Could not verify disclaimer presence. |

**Summary:** Help/guide fansite with moderate domain-level trademark risk. Cannot confirm content compliance without live access.
**Action Items:**
- Verify disclaimer is present on every page.
- Confirm no display ads or paid features.
- Consider whether the domain name has been flagged by RSI previously.
- Manually verify referral links point to `https://robertsspaceindustries.com/enlist?referral=<CODE>`.

---

### 2. www.trystarcitizen.com

| Check | Status | Notes |
|-------|--------|-------|
| Non-Commercial | ⚠️ Needs Review | Could not fetch live content. Domain name implies new-player recruitment (referral funnel); verify no monetization beyond the RSI referral program. |
| IP & Trademarks | ⚠️ Needs Review | Domain contains "Star Citizen" — same trademark-in-domain concern as above. "Try Star Citizen" strongly implies a referral/landing page. RSI's referral program is permitted, but the domain name itself may still violate trademark policy. |
| Referral Program | ⚠️ Needs Review | Site purpose appears to be referral-focused. Could not verify: referral code accuracy, UEC bonus claims, use of correct enlist URL, or absence of deceptive language. |
| Content Rules | ⚠️ Needs Review | Could not verify absence of Squadron 42 content or RSI marketing materials. |
| Fansite Disclaimer | ⚠️ Needs Review | Could not verify disclaimer presence. Especially important on a referral-focused site. |

**Summary:** Appears to be a referral landing page. Domain-level trademark risk; cannot confirm content compliance without live access.
**Action Items:**
- Ensure disclaimer is prominent on the homepage and all referral-focused pages.
- Verify UEC bonus amounts match the current RSI program (amounts change).
- Confirm referral links use the correct official enlist URL.
- Verify no high-pressure or deceptive language is used.

---

### 3. www.buystarcitizen.com

| Check | Status | Notes |
|-------|--------|-------|
| Non-Commercial | ❌ Non-Compliant (Domain-Level) | The domain name "buystarcitizen.com" explicitly implies that visitors can purchase Star Citizen or Star Citizen goods through this site. This is a strong indicator of commercial use of RSI IP regardless of actual site content. RSI fansite rules prohibit commercial use without a signed license. |
| IP & Trademarks | ❌ Non-Compliant (Domain-Level) | Domain contains "Star Citizen" (RSI trademark) combined with "buy" — the combination directly implies a commercial storefront using RSI IP. This violates RSI's trademark policy which prohibits use of trademarks in domain names, and is compounded by the commercial framing. |
| Referral Program | ⚠️ Needs Review | If the site directs users to buy Star Citizen via a referral link, it must comply with referral program rules. Could not verify specifics. |
| Content Rules | ⚠️ Needs Review | Could not fetch live content to verify. |
| Fansite Disclaimer | ⚠️ Needs Review | Could not verify. Critical for this domain given the commercial-sounding name — users may assume it is an official RSI storefront. |

**Summary:** ❌ CRITICAL — The domain name alone constitutes a likely RSI policy violation on both commercial use and trademark grounds. This site presents the highest compliance risk in the portfolio.
**Action Items:**
- **Urgent:** Assess whether this domain should be redirected, rebranded, or taken offline pending legal review.
- If the site is purely a referral funnel (linking to RSI's official store), the domain name still creates unacceptable trademark and commercial-framing risk.
- Add a prominent disclaimer clarifying this is not an official RSI purchasing channel.
- Consult RSI's fansite policy or contact RSI directly to request written guidance on this domain.

---

### 4. www.starcitizenstore.com

| Check | Status | Notes |
|-------|--------|-------|
| Non-Commercial | ❌ Non-Compliant (Domain-Level) | The domain "starcitizenstore.com" explicitly names itself a "store" using RSI's "Star Citizen" trademark. This strongly implies a commercial operation selling goods using RSI IP, which requires a signed commercial license from CIG — not available to general fan sites. |
| IP & Trademarks | ❌ Non-Compliant (Domain-Level) | Domain contains "Star Citizen" (RSI trademark) combined with "store" — nearly identical in risk to buystarcitizen.com. RSI policy prohibits use of its trademarks in domain names. |
| Referral Program | ⚠️ Needs Review | Could not fetch live content to verify. |
| Content Rules | ⚠️ Needs Review | Could not fetch live content to verify. |
| Fansite Disclaimer | ⚠️ Needs Review | Could not verify. A "store" domain with no disclaimer risks being mistaken for an official RSI shop. |

**Summary:** ❌ CRITICAL — Equivalent risk level to buystarcitizen.com. The domain name itself constitutes a likely RSI policy violation. "Star Citizen Store" is almost certainly how RSI would characterize a commercial entity using their IP.
**Action Items:**
- **Urgent:** Same as buystarcitizen.com — assess rebrand/redirect/takedown.
- If only directing users to RSI's official store via referral link, the domain name still creates serious legal exposure.
- If any physical or digital goods are sold under this domain (merchandise, ship upgrades, accounts), this is a clear ToS and trademark violation.
- Contact RSI/CIG for written guidance before continuing to operate this domain.

---

### 5. www.millionmilehighclub.com

| Check | Status | Notes |
|-------|--------|-------|
| Non-Commercial | ⚠️ Needs Review | Could not fetch live content. Domain name does not inherently imply commercial use — verify no ads, paywalls, or merchandise. |
| IP & Trademarks | ✅ Compliant (Domain-Level) | Domain does not contain any RSI/CIG trademarks ("Star Citizen", "Roberts Space Industries", "Cloud Imperium", "Squadron 42"). Lowest domain-level trademark risk in the portfolio. Could not verify on-page IP use. |
| Referral Program | ⚠️ Needs Review | Could not fetch live content to verify referral compliance. |
| Content Rules | ⚠️ Needs Review | Could not fetch live content to verify. |
| Fansite Disclaimer | ⚠️ Needs Review | Could not verify disclaimer presence. |

**Summary:** Lowest compliance risk domain in the portfolio. Domain name is original and avoids RSI trademarks. Cannot confirm content compliance without live access.
**Action Items:**
- Verify disclaimer is present and visible on every page.
- Confirm no monetization beyond the RSI referral program.
- Manually check for any Squadron 42 content or reproduced RSI marketing materials.

---

### 6. www.greysmarket.com

| Check | Status | Notes |
|-------|--------|-------|
| Non-Commercial | ⚠️ Needs Review | "Grey's Market" / "Greys Market" — the name could imply a secondary marketplace for Star Citizen items (ships, accounts, in-game goods). Selling Star Citizen ships, accounts, or in-game items is prohibited under RSI ToS (Section on Virtual Items/Currency). Could not fetch live content to confirm intent. |
| IP & Trademarks | ✅ Compliant (Domain-Level) | Domain does not contain RSI trademarks. However, if RSI IP is used on-page (ship images, logos, etc.) without proper attribution, this changes. |
| Referral Program | ⚠️ Needs Review | Could not verify. |
| Content Rules | ⚠️ Needs Review | Could not fetch live content. If the site facilitates secondary sales of RSI game assets or accounts, this would violate RSI ToS. |
| Fansite Disclaimer | ⚠️ Needs Review | Could not verify. If site is Star Citizen-related, disclaimer is required. |

**Summary:** Domain name is trademark-safe but the "market" framing warrants scrutiny. If this site facilitates any sale or trade of Star Citizen accounts, ships, or in-game currency/items, it is in direct violation of RSI ToS.
**Action Items:**
- Clarify site purpose: if it is a secondary market for Star Citizen items, this is a ToS violation regardless of domain name safety.
- Verify no RSI IP is used without attribution.
- Confirm disclaimer is present if the site is Star Citizen-related.

---

## Portfolio Risk Summary

| Site | Domain Trademark Risk | Commercial Risk | Overall |
|------|----------------------|-----------------|---------|
| starcitizenhelp.com | ⚠️ Medium | ⚠️ Unknown | ⚠️ Needs Review |
| trystarcitizen.com | ⚠️ Medium | ⚠️ Unknown | ⚠️ Needs Review |
| buystarcitizen.com | ❌ High | ❌ High | ❌ Critical |
| starcitizenstore.com | ❌ High | ❌ High | ❌ Critical |
| millionmilehighclub.com | ✅ Low | ⚠️ Unknown | ⚠️ Needs Review |
| greysmarket.com | ✅ Low | ⚠️ Unknown | ⚠️ Needs Review |

---

## Policy Change Notes

- RSI policy pages returned 403 this cycle — no live policy changes could be detected.
- Manual review recommended at: `https://robertsspaceindustries.com/en/tos` and `https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793`

---

## Global Action Items

- [ ] **[URGENT]** Review `buystarcitizen.com` and `starcitizenstore.com` — domain names alone present high RSI trademark and commercial-use violation risk. Consider consulting a trademark attorney.
- [ ] **[URGENT]** Manually verify live content on all 6 sites — automated fetch was blocked on all domains.
- [ ] Confirm RSI-required disclaimer is visible on every page of every site.
- [ ] Verify all referral links use the correct format: `https://robertsspaceindustries.com/enlist?referral=<CODE>`
- [ ] Confirm current UEC referral bonus amounts match what is advertised on any referral-focused pages.
- [ ] Investigate `greysmarket.com` site purpose — if it facilitates secondary market trades of Star Citizen assets, this violates RSI ToS independently of IP rules.
- [ ] Enable live content fetching: configure a headless browser or session-authenticated fetch tool to bypass WAF protection on future audit cycles.

---

*This report was generated automatically. It is not legal advice. Consult RSI's official documentation and, where necessary, a qualified attorney for compliance and trademark determinations.*
