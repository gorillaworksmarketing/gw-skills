---
name: cold-email-editing
description: >-
  Use whenever GW Email Editor reviews, edits, scores, or approves a Gorilla
  Works cold email (including the roofing landing-page email), follow-up,
  objection reply, positive-reply draft, or nurture email before it goes to
  Brennan. Runs hard fails, the slot checklist, Seven Sweeps for email, AI-tell
  removal, claims and fact checks, and a 1-10 panel score, then outputs PASS or
  FAIL with a change log. Use it even if the request just says "check these
  emails".
---
# Cold email editing (GW Email Editor)
Spec: blueprints/cold-email.md. Scorecard: blueprints/email-copy-frameworks.md §14. Apply `gw-brand-guidelines`, `gw-claims-guardrails`, `gw-fact-check`, then `gw-qa-gate`. Never send.

## How to think about it
One job: a click to their page. Specific and true: leave it. Generic or AI-sounding: back with notes.

## Pass 1: hard fails (any one = FAIL, list the fix)
- Labeled lines missing, out of order, misspelled, or extra (spec order). Any greeting, checklist, channel strip, signature, footer (Ember has them).
- **Review quote:** not from a **Reviews** field line (Google Maps only), or not matching it and its screenshot word for word (cuts only with "..."). Screenshot listing name not the row's company. Not 5 stars or not directly about the company (age and price mentions are fine). Reviewer name not exact. NO QUALIFYING REVIEW: hold.
- Eyebrow doesn't match the Review Count and Rating fields, which the lookup refreshes (rating 1 decimal). Row scraped before the refresh: note it, not a fail.
- A company fact unsourced or not matching.
- Proof line not exactly `Real Great Roofing: "$90,000 in leads from just one mail drop."`, or details or stats added.
- Any other dollar amount or price word in our copy (review quote exempt), incl. "$750 value", "$500 off". Guarantees, ROI promises. Write `[NEED: ...]`.
- "Thousands of other customers" or any unapproved claim.
- CTA not `See my page -> ` + the row's Prospect Page URL or `{{page_link}}`. Invented or edited URL, google.com/url wrapper, or a second ask (call, "reply yes").
- Fake Re:/Fwd: subject, urgency, pitch words. Any `brand_check.py --channel cold-email` fail (em dash, hashtag, cliché, grade over 7).
- Status set to Send, or workflow fields touched. No `gw-fact-check` claim table.

## Pass 2: slot checks
Subject short with the company name. Preview under 90 characters. Headline 3-8 words. Body 1 is 25-40 words: verified details, then nearby homes needing the same work. Body 2 is the spec's fixed sentence with the short company name.

## Pass 3: Seven Sweeps
**Clarity** (phone-scannable); **voice** (Brennan, peer to peer); **so what** (each slot ties to their jobs); **prove it** (backed or cut); **specificity** (works for another company = thin); **coherence** in template order; **one click** (the page is the only next step).

## Retry loop (Nov 13)
Judge = a separate pass, never the writer. On a brand_check or judge fail (hallucination vs claim table, cliché, voice), auto-rewrite with the exact errors fed back, recheck; max 2, then escalate to Brennan with all versions.

## Pass 4: panel score
1-10 as a roofing owner, a deliverability reviewer, a copywriter, Brennan. PASS: all 7+, average 8+. Note why the lowest is low.

## Final copy
**Edited Email Copy**, same labeled layout. Holding a row: keep its Status. Never set Status = Send.

## 1-day rule (Nov 13)
Ready for Summary rows are edited within 1 day unless they fail; reports list rows past 1 day and why. Grok Bot checks daily, fixes stalls with the owner.

## Follow-ups and replies
Roofing follow-ups and positive-reply text: PENDING Brennan. Replies stay drafts; no auto-send until he approves. Other trades: legacy offer-arm checks in the blueprint.

## Output
Edited copy, change log, claim table, scores, PASS/FAIL, held rows and reasons.

## Learning loop
Weekly: log repeat fixes and retries in the blueprint; compare scores to page clicks and positive replies, recalibrate if they disagree.
