---
name: gw-qa-gate
description: >-
  Use as the final pass/fail check on any Gorilla Works post, reply, article, or
  email before it goes to Brennan for approval. It runs the two-tier QA
  standard, the Social Editor rulings, the content rules, link/UTM logging, and
  platform format checks, and outputs PASS or FAIL with fixes. Use it even if
  the request doesn't name the skill.
---
# Gorilla Works QA gate
Sources: knowledge-base/00-source-of-truth.md §0A/§10, Social Editor rulings (Oct 14 2026), `gw-content-rules`, `gw-claims-guardrails`, research/utm-link-strategy.md, platform blueprint.

## Checks
1. **BLOCKED** (any hit = FAIL): the blocked list in `gw-claims-guardrails`.
2b. **No made-up facts (Nov 10):** `gw-fact-check` claim table attached, every row verified or cut. Invented or unverified claim, quote, example, or broken link = FAIL.
2. **Stats:** every number verifiable, logged with a V or S stat-log ID (or an approved company fact); no source line needed. F-prefixed or missing = FAIL.
3. **Price:** any price or cost ($0.78, "under $1", "as low as", stamp comparison, per-piece or plan price) = FAIL. Approved offers as worded OK, not in roofing cold email. Its verbatim review quote is exempt.
4. **Real Great Roofing:** the exact quote only, one client's result, no campaign details. "Thousands of other customers" = FAIL.
5. **Content rules:** no banned or self-aware ranking lines, hashtags, or "you need a list"; custom mail first; authority voice; no AI tells (`gw-content-rules`; em dash = FAIL). Mix per team/industry-mix.md.
6. **Links/UTM:** every gorillaworksmarketing.com link built per research/utm-link-strategy.md (utm_campaign=<industry>_<type>, utm_term=<slug>, unique utm_content, lowercase; blog internal and canonical links clean), and **every link has a row in research/link-log.csv**. Lead-gen posts carry the /book-demo UTM link. Missing UTM or row = fix first. Roofing cold-email CTA URL: used exactly as the row gives it (UTM: ask Brennan).
7. **Platform format:** LinkedIn @Gorilla Works Marketing mention on top; X replies under 240 characters, spelled-out numbers, "X" not "Twitter"; Reddit self-promo limits; no cross-platform duplicates; blueprint length and structure.
7b. **Long-form:** information gain, "search over" test, 5+ (ideally 10) internal links, about 5th-grade level, proof of a human edit (fully automated AI = FAIL).
7c. **Email:** honest subject (no fake Re:/Fwd:), sender Brennan, one ask, sourced hooks. **Roofing cold email** (landing-page format, blueprints/cold-email.md): slots in order; only ask is the CTA `See my page -> ` + Prospect Page URL or `{{page_link}}`, never invented. Opt-out and Kirkland address are in Brennan's fixed Ember footer, not this copy; unconfirmed footer = flag Brennan. Other emails carry an opt-out line and Gorilla Works Marketing, LLC, 13120 NE 85th St Unit 123, Kirkland, WA 98033. Cold and nurture emails need a `cold-email-editing` PASS.
8. **Confidential:** no client data or internals.
9. **Coherence (Nov 6):** read it as the target owner. Each line follows the last; no self-contradiction; stats in plain words; no jargon; main point fits one sentence. Any miss = FAIL: rewrite, don't polish.

## Output
PASS or FAIL; each issue (rule, quote, fix); stat IDs and link-log rows used; open questions for Brennan.

Log it in the QA Decision Log; Brennan's edits become lessons. **Never publish.** Brennan is the only approver. See `gw-skills-index`, `cold-email-editing`.

Oct 19: FAIL a utm_source not matching the platform; utm_campaign industries not in the UTM strategy (new trades use home-services); reuse of the li-p1 "51%" hook; replies forcing a URL every time (~75% pure value). Flag banned-line hits in LIVE copy to Brennan. Mix 75% value / 25% lead-gen.

Learning loop: weekly, recurring FAIL reasons go to the writer skills and the QA Decision Log.
