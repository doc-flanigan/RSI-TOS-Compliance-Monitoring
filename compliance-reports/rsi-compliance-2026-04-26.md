# RSI Compliance Audit — 2026-04-26

## Audit Metadata
- **Date:** 2026-04-26
- **Auditor:** Automated Compliance Agent
- **Branch:** claude/setup-compliance-auditor-UHr3g

---

## ⚠️ Configuration Notice — No Site URLs Provided

The site list in the audit configuration still contains the placeholder `[LIST YOUR SITE URLS HERE]`.  
**No live site content was audited this cycle.**

To enable site auditing, replace the placeholder in the system prompt with your actual fansite URLs, e.g.:
```
## Sites to Check
https://your-fansite.com
https://another-fansite.com
```

---

## Policy Fetch Status

| Source | URL | Result |
|--------|-----|--------|
| RSI Terms of Service | https://robertsspaceindustries.com/en/tos | ❌ 403 — Server blocked automated fetch |
| RSI Fansite FAQ | https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793 | ❌ 403 — Server blocked automated fetch |

> **Note:** RSI's web infrastructure blocks automated HTTP requests. Policy review below is based on the most recently known published RSI/CIG fansite guidelines. Manual verification of the live policy pages is recommended each audit cycle.
>
> **Recommended manual check URLs:**
> - Terms of Service: `https://robertsspaceindustries.com/en/tos`
> - Fansite FAQ: `https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793`

---

## RSI Fansite Policy Baseline (Reference)

The following rules are extracted from RSI's published fansite guidelines and ToS as of the last known policy revision. These serve as the evaluation criteria for all site audits.

### Non-Commercial Use
- Fan sites must be **strictly non-commercial**.
- Display advertising, affiliate marketing (beyond the RSI referral program), paywalls, subscriptions, and fees are prohibited.
- Selling physical or digital goods using RSI IP (ship renders, logos, game assets) requires a signed commercial license from CIG — not available to general public.

### IP & Trademark Usage
- RSI/CIG concept art, screenshots, ship renders, and logos may be used **with clear unofficial fansite attribution**.
- RSI trademarks must **not** appear in domain names or business names.
- Content must not imply official RSI/CIG endorsement or affiliation.
- Required disclaimer: *"This is an unofficial fan site not affiliated with or endorsed by Roberts Space Industries or Cloud Imperium Games."*

### Referral Program
- One referral code per RSI account; must be displayed **honestly and transparently**.
- No false claims about bonus amounts or UEC rewards (these change frequently — verify current amounts at rsi.com).
- No deceptive or high-pressure language.
- Referral links must point to the official RSI enlist URL: `https://robertsspaceindustries.com/enlist?referral=<CODE>`

### Prohibited Content
- **Squadron 42 content is explicitly prohibited**: actor likenesses, trailers, concept art, promotional materials.
- No illegal, defamatory, or reputationally harmful content.
- RSI marketing materials (trailers, promo videos) may not be reproduced or embedded without written permission.

### Disclaimer Requirement
- A clear, visible disclaimer must appear on **every page**, or at minimum the homepage and any referral-focused pages.

---

## Site Audits

*No sites audited this cycle — site URLs not configured. See configuration notice above.*

---

## Policy Change Notes

No live policy fetch was possible this cycle (403 responses). The following changes were known as of the last successful manual review:

- RSI periodically updates the UEC bonus amounts for referrals — always verify the current amount before publishing claims on a fansite.
- Squadron 42 content restrictions remain in effect and are strictly enforced.
- CIG has historically sent DMCA notices to fansites using ship renders or logos in commercial contexts (merchandise, storefronts).

---

## Action Items for Next Cycle

- [ ] **Add site URLs** to the audit configuration before the next run.
- [ ] **Manually verify** RSI ToS at `https://robertsspaceindustries.com/en/tos` — automated fetch blocked.
- [ ] **Manually verify** Fansite FAQ at `https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793` — automated fetch blocked.
- [ ] Consider configuring a browser-based fetch tool or headless browser if live policy monitoring is required.

---

*This report was generated automatically. It is not legal advice. Consult RSI's official documentation and, where necessary, a qualified attorney for compliance determinations.*
