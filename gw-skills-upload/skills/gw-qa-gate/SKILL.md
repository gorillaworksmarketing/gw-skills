---
name: gw-qa-gate
description: Use as the final pass/fail check on any Gorilla Works post, reply, or article before it goes to Brennan for approval. It runs the two-tier QA standard, the Social Editor rulings, the content rules, link/UTM logging, and platform format checks, and outputs PASS or FAIL with fixes. Use it even if the request doesn't name the skill.
---
# Gorilla Works QA gate
Sources: knowledge-base/00-source-of-truth.md §0A/§10, the Social Editor rulings (Oct 14 2026), `gw-content-rules`, `gw-claims-guardrails`, research/utm-link-strategy.md, and the platform blueprint.

## Checks
1. **BLOCKED** (any hit = FAIL): the blocked list in `gw-claims-guardrails`.
2. **Stats:** every number is verifiable and logged with a V or S stat-log ID (or is an approved company fact). The post needs no source line. F-prefixed or missing = FAIL.
3. **Price:** only "as low as $0.78" / "under $1"; any stamp comparison = FAIL.
4. **Real Great Roofing:** the exact quote only, as one client's result, no campaign details.
5. **Content rules:** no banned or self-aware ranking lines, no hashtags, custom mail first, no "you need a list", authority voice.
6. **Links/UTM (required):** every gorillaworksmarketing.com link is built per research/utm-link-strategy.md (utm_campaign=<industry>_<type>, utm_term=<article slug>, unique utm_content never reused, lowercase; blog internal and canonical links stay clean), and **every link has a row in research/link-log.csv**. Lead-gen posts carry the /book-demo UTM link. UTMs: utm_source=<platform>, utm_campaign=<industry>_<type> (e.g. fencing_faq), utm_term=<article slug>, lowercase; the industry, type, and utm_term columns are filled in the log. Missing UTM or log row = fix before PASS.
7. **Platform format:** LinkedIn @Gorilla Works Marketing mention at the top; X replies under 240 characters, spelled-out numbers, "X" not "Twitter"; Reddit self-promo limits; no identical text across platforms; blueprint length and structure.
7b. **Long-form:** information gain, the "search over" test, 5+ (ideally 10) in-body internal links, about a 5th-grade reading level, and proof of a human edit (fully automated AI content = FAIL).
8. **Confidentiality:** no client data or internals.

## Output
- PASS or FAIL
- Each issue: rule, quote, fix
- Stat IDs and link-log rows used
- Open questions for Brennan (e.g. the ranked-list disclosure)

Log the decision for the QA Decision Log; Brennan's edits become lessons in the rules file. **Never publish.** Brennan is the only approver.

Skills to reference: `gw-skills-index`; cold email drafts also run the `cold-email-copy` editor check (CAN-SPAM line and address).

Oct 19 gate additions: fail any link whose utm_source does not match the platform; fail utm_campaign industries not listed in research/utm-link-strategy.md (HVAC and other new trades use home-services); fail any reuse of the li-p1 "51%" hook; fail replies that force a URL every time (~75% pure value). Also run the banned-line check on LIVE published copy and flag any hit to Brennan for a fix. Mix is 75% value / 25% lead-gen.
