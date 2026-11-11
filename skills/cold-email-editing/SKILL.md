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
Roofing format spec and examples: blueprints/cold-email.md. Scorecard: blueprints/email-copy-frameworks.md §14 (AI tells §11). Apply `gw-claims-guardrails`, `gw-fact-check`, then `gw-qa-gate`. The editor never sends.

## How to think about it
Each email has one job: get the owner to click to their personal page. Specific, true, Brennan's voice: leave it. Generic or AI-sounding: back with notes.

## Pass 1: hard fails (any one = FAIL, list the fix)
- Labeled lines missing, out of order, misspelled, or extra: Subject, Preview, Eyebrow, Headline, Review quote, Review name, Body paragraph 1, Body paragraph 2, Proof line, CTA. Any greeting, checklist, channel strip, signature, or footer written in the copy (Ember has them).
- **Review quote:** open its source. Not word for word, not labeled as a Google review, reworded, typo-fixed, merged, or cut other than with "...". Not 5 stars, older than about 6 months, or no proof of stars and date. Mentions price, cost, or money. Reviewer name not exact.
- Eyebrow doesn't match the Review Count and Rating properties (rating 1 decimal).
- A company fact with no source or not matching it.
- Proof line not exactly `Real Great Roofing: "$90,000 in leads from just one mail drop."`, or campaign details or other stats added.
- Any other dollar amount or price word: $0.78, "under $1", stamp comparison, "$750 value", "$500 off". Guarantees, ROI promises. Write `[NEED: ...]`.
- "Thousands of other customers" or any unapproved claim.
- CTA not `See my page -> ` + the row's Prospect Page URL or `{{page_link}}`. An invented or edited URL, a google.com/url wrapper, or a second ask (call booking, "reply yes").
- Fake Re:/Fwd: subject, urgency, pitch words. Any em dash, hashtag.
- Status set to Send, or workflow fields touched. No `gw-fact-check` claim table.

## Pass 2: slot checks
Subject is short with the company name. Preview one line under 90 characters, about the page. Headline 3-8 words, this company only. Body paragraph 1 is 25-40 words: one or two verified details, then nearby homes that need the same work. Body paragraph 2 is the spec's fixed sentence with the short company name.

## Pass 3: Seven Sweeps for email
1. **Clarity:** 7th-grade level; scannable on a phone.
2. **Voice:** Brennan, peer to peer.
3. **So what:** each slot ties to their jobs.
4. **Prove it:** each claim backed or cut.
5. **Specificity:** swap in another company's name; if it still works, the headline or body is thin.
6. **Coherence:** read all slots in template order; each makes sense next to the last.
7. **One click:** the page is the only next step.

## Pass 4: panel score
1-10 as the busy roofing owner, a deliverability reviewer, a copywriter, and Brennan. PASS needs every score 7+ and an average of 8+. Note why the lowest is low.

## Final copy
Put it in **Edited Email Copy**, same labeled layout. Holding a row: keep its Status. Never set Status = Send.

## Follow-ups and replies
Roofing follow-ups and positive-reply text are PENDING Brennan (spec covers email 1). Replies stay drafts; no auto-send until he approves the reply agent. Other trades: legacy offer-arm checks in the blueprint.

## Output
Edited copy, change log, claim table, four scores, PASS or FAIL, held rows with reasons.

## Learning loop
Weekly: log repeat fixes in blueprints/cold-email.md. Compare scores to real page clicks and positive replies; if they disagree, recalibrate and note it in the changelog.
