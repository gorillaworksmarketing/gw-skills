---
name: gw-qa-gate
description: >-
  Use as the final pass/fail check on any Gorilla Works post, reply, article, or
  email before it goes to Brennan for approval. It runs the brand check and
  retry loop, the two-tier QA standard, the Social Editor rulings, the content rules, link/UTM logging, and
  platform format checks, and outputs PASS or FAIL with fixes. Use it even if
  the request doesn't name the skill.
---
# Gorilla Works QA gate
Sources: knowledge-base/00-source-of-truth.md §0A/§10, Social Editor rulings (Oct 14), `gw-brand-guidelines`, `gw-content-rules`, `gw-claims-guardrails`, the UTM strategy, blueprint.

## Checks
0. **Brand check (Nov 13):** `scripts/brand_check.py --channel <ch>` passes; input guard ran on sources. Fail = retry loop.
1. **BLOCKED** (any hit = FAIL): the blocked list in `gw-claims-guardrails`.
2b. **No made-up facts (Nov 10):** `gw-fact-check` claim table attached, every row verified or cut. Invented/unverified claim, quote, example, or broken link = FAIL.
2. **Stats:** every number has a V or S stat-log ID or approved fact, and an inline citation (`gw-claims-guardrails`). F or missing = FAIL.
3. **Price:** any price or cost ($0.78, "under $1", "as low as", stamp comparison, per-piece or plan price) = FAIL. Approved offers as worded OK, not in roofing cold email. Verbatim third-party reviews/quotes exempt.
4. **Real Great Roofing:** the exact quote only, one client's result, no campaign details. "Thousands of other customers" = FAIL.
5. **Content rules:** no banned lines, hashtags, or "you need a list"; custom mail first; brand voice, persona reset, no AI tells or clichés (`gw-content-rules`; em dash = FAIL). Mix per team/industry-mix.md.
6. **Links/UTM:** every gorillaworksmarketing.com link per research/utm-link-strategy.md (utm_campaign=<industry>_<type>, utm_term=<slug>, unique utm_content, lowercase; blog internal/canonical clean) with **a row in research/link-log.csv**. Lead-gen posts carry the /book-demo UTM link. Missing = fix first. Roofing CTA URL exactly as the row gives it.
7. **Platform format** (guidelines §8): LinkedIn @Gorilla Works Marketing mention on top; X replies under 240 characters, spelled-out numbers, "X" not "Twitter"; Reddit promo limits; no cross-platform duplicates.
7b. **Long-form:** information gain, "search over" test, 5+ (ideally 10) internal links, grade 6-7, a human edit (fully automated AI = FAIL).
7c. **Email:** honest subject (no fake Re:/Fwd:), sender Brennan, one ask, sourced hooks. **Roofing cold email** (blueprints/cold-email.md): slots in order; only ask is `See my page -> ` + Prospect Page URL or `{{page_link}}`, never invented. Opt-out and address sit in Brennan's Ember footer (unconfirmed = flag him). Other emails: opt-out line plus Gorilla Works Marketing, LLC, 13120 NE 85th St Unit 123, Kirkland, WA 98033. Cold and nurture emails need a `cold-email-editing` PASS.
8. **Confidential:** no client data/internals.
9. **Coherence (Nov 6):** read as the target owner: each line follows, no self-contradiction, plain stats, no jargon, one-sentence main point. Miss = FAIL: rewrite.

## Retry loop (`gw-brand-guidelines` §9)
Check-0 or judge fail (judge = separate pass, never the writer): auto-rewrite with the exact errors fed back (`retry_prompt` plus judge notes), recheck; max 2 rewrites, then escalate to Brennan with all versions.

## Output
PASS or FAIL; each issue (rule, quote, fix); stat IDs and link-log rows used; open questions for Brennan.

Log in the QA Decision Log; Brennan's edits become lessons. **Never publish**; Brennan alone approves.

Oct 19: FAIL utm_source not matching the platform; utm_campaign industries outside the UTM strategy (new trades: home-services); the li-p1 "51%" hook; replies forcing a URL every time. Flag banned-line hits in LIVE copy to Brennan. Mix 75/25.

Learning loop: weekly, recurring FAIL reasons go to writer skills and the QA Decision Log.
