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
Spec: blueprints/cold-email.md. Scorecard: blueprints/email-copy-frameworks.md §14 (AI tells §11). Apply `gw-claims-guardrails`, `gw-fact-check`, then `gw-qa-gate`. The editor never sends.

## How to think about it
One job: a click to their personal page. Specific and true: leave it. Generic or AI-sounding: back with notes.

## Pass 1: hard fails (any one = FAIL, list the fix)
- Labeled lines missing, out of order, misspelled, or extra (Subject, Preview, Eyebrow, Headline, Review quote, Review name, Body paragraph 1-2, Proof line, CTA). Any greeting, checklist, channel strip, signature, or footer in the copy (Ember has them).
- **Review quote:** not from a **Reviews** field line (Google Maps only), or not matching it and its screenshot word for word (cuts only with "..."). Screenshot listing name not the row's company. Not 5 stars or not directly about the company (age and price mentions are fine). Reviewer name not exact. NO QUALIFYING REVIEW: hold.
- Eyebrow doesn't match the Review Count and Rating fields, which the lookup refreshes (rating 1 decimal). Row scraped before the refresh: note it, not a fail.
- A company fact unsourced or not matching.
- Proof line not exactly `Real Great Roofing: "$90,000 in leads from just one mail drop."`, or details or stats added.
- Any other dollar amount or price word in our copy (review quote exempt): $0.78, "under $1", stamp comparison, "$750 value", "$500 off". Guarantees, ROI promises. Write `[NEED: ...]`.
- "Thousands of other customers" or any unapproved claim.
- CTA not `See my page -> ` + the row's Prospect Page URL or `{{page_link}}`. Invented or edited URL, google.com/url wrapper, or a second ask (call, "reply yes").
- Fake Re:/Fwd: subject, urgency, pitch words. Any em dash, hashtag.
- Status set to Send, or workflow fields touched. No `gw-fact-check` claim table.

## Pass 2: slot checks
Subject short with the company name. Preview one line under 90 characters. Headline 3-8 words. Body paragraph 1 is 25-40 words: verified details, then nearby homes needing the same work. Body paragraph 2 is the spec's fixed sentence with the short company name.

## Pass 3: Seven Sweeps for email
1. **Clarity:** 7th grade; phone-scannable.
2. **Voice:** Brennan, peer to peer.
3. **So what:** each slot ties to their jobs.
4. **Prove it:** each claim backed or cut.
5. **Specificity:** swap in another company's name; if it still works, it's thin.
6. **Coherence:** all slots make sense read in template order.
7. **One click:** the page is the only next step.

## Pass 4: panel score
1-10 as a roofing owner, a deliverability reviewer, a copywriter, and Brennan. PASS: every score 7+, average 8+. Note why the lowest is low.

## Final copy
**Edited Email Copy**, same labeled layout. Holding a row: keep its Status. Never set Status = Send.

## 1-day rule (Nov 13)
Ready for Summary rows are edited within 1 day unless they fail. Every run report lists rows past 1 day and why. Grok Bot checks daily and fixes stalls with the step's owner.

## Follow-ups and replies
Roofing follow-ups and positive-reply text: PENDING Brennan. Replies stay drafts; no auto-send until he approves it. Other trades: legacy offer-arm checks in the blueprint.

## Output
Edited copy, change log, claim table, scores, PASS/FAIL, held rows and reasons.

## Learning loop
Weekly: log repeat fixes in the blueprint. Compare scores to real page clicks and positive replies; if they disagree, recalibrate and log it.
