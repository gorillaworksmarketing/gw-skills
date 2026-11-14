---
name: cold-email-editing
description: >-
  Use whenever GW Email Editor reviews, edits, scores, or approves a Gorilla
  Works cold email (including the roofing landing-page email), follow-up,
  objection reply, positive-reply draft, or nurture email before it goes to
  Brennan. Runs hard fails, the slot checklist, Seven Sweeps for email, AI-tell
  removal, claims and fact checks, a 1-10 panel score, and the landing-page
  handoff (Outreach Email, Ready) plus the daily stall report, then outputs
  PASS or FAIL with a change log. Use it even if the request just says "check these
  emails".
---
# Cold email editing (GW Email Editor)
Spec: blueprints/cold-email.md, guide §11-12. Scorecard: email-copy-frameworks.md §14. Apply `gw-brand-guidelines`, `gw-claims-guardrails`, `gw-fact-check`, `gw-qa-gate`. Never send.

Work only the industry Brennan names (currently Roofing); other DBs' systems are setup only. One job: a click to their page. Specific, true: keep. Generic: back with notes.

## Pass 1: hard fails (any = FAIL; list fixes)
- Labeled lines missing, misordered, misspelled, extra. Greeting, checklist, channel strip, signature, footer (Ember's).
- **Review quote:** not from a **Reviews** line (Maps only) or not word for word with its screenshot (cuts only "..."). Listing name not the row's company. Not 5 stars or not about the company (age, price fine). Reviewer name not exact.
- Eyebrow not matching Review Count and Rating (1 decimal). Pre-refresh row: note, not a fail.
- Unsourced or wrong company fact.
- Proof line not exactly `Real Great Roofing: "$90,000 in leads from just one mail drop."`, or details added.
- Other price words in our copy (quote exempt), incl. "$750 value", "$500 off"; guarantees, ROI. Write `[NEED: ...]`.
- "Thousands of other customers" or other unapproved claims.
- CTA not `See my page -> ` + Prospect Page URL or `{{page_link}}`; invented URL, google.com/url wrapper, second ask.
- Fake Re:/Fwd:, urgency, pitch words, any `brand_check.py --channel cold-email` fail.
- Status = Send, fields beyond the handoff list, no claim table.

## Pass 2: slots
Subject short with company name. Preview under 90 chars. Headline 3-8 words. Body 1: 25-40 words, facts then nearby homes. Body 2: fixed sentence.

## Pass 3: Seven Sweeps
Clarity, voice (Brennan, peer to peer), so what, prove it, specificity (fits others = thin), coherence, one click.

## Retry loop
Judge is a separate pass, never the writer. On a brand_check or judge fail, rewrite with the errors; max 2, then send Brennan all versions.

## Pass 4: panel
1-10 as owner, deliverability, copywriter, Brennan. PASS: all 7+, avg 8+; explain lowest.

## Final copy and handoff (guide §11)
**Edited Email Copy**, same layout. Holding: keep Status. At clear time, in order:
1. **Outreach Email:** one address from Hunter's usable list: Verified, valid, deliverable, not accept-all. Never unknown, risky, or discovered-only. None: failed; reason in Editor Notes.
2. **Lifecycle Stage** = website, then **Landing Page Input Version** +1.
3. **Landing Page Status = Ready** LAST, only when research and final edit are done, code present, no Hold, and 12b lists that industry's landing-page template approved (MISSING holds only that industry; flag Brennan once).
Only these stage fields. Ready never authorizes a send. Never set Published, Building, Needs Fix, Uncertain, Send.

## Failed rows and 1-day rule
**Failed check:** Status Failed, Bad match, Drop; Hunter invalid or no usable verified email; your HOLD/QA FAIL; NO QUALIFYING REVIEW; Review Count 30 or fewer. Never backfill, code, re-run Hunter, hand off, set Ready; report as failed with reason, not stalled. Other rows: edit within 1 day. Daily stall report, all 12b DBs (never moves Status); Grok Bot fixes stalls with owners.

## Follow-ups and replies
Roofing follow-ups, replies: PENDING Brennan; drafts only, no auto-send.

## Output
Edited copy, change log, claims, scores, PASS/FAIL, held/failed rows.

## Learning loop
Weekly: log repeat fixes, retries in the blueprint; recalibrate if scores disagree with clicks, replies.
