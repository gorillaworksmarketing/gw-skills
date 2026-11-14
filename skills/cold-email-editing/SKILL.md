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
Spec, handoff, registry: blueprints/cold-email.md, Notion guide §11-12. Scorecard: email-copy-frameworks.md §14. Apply `gw-brand-guidelines`, `gw-claims-guardrails`, `gw-fact-check`, `gw-qa-gate`. Never send.

## How to think
One job: a click to their page. Specific and true: keep. Generic: back with notes.

## Pass 1: hard fails (any = FAIL, list the fix)
- Labeled lines missing, misordered, misspelled, or extra. Any greeting, checklist, channel strip, signature, footer (Ember has them).
- **Review quote:** not from a **Reviews** line (Maps only) or not word for word with its screenshot (cuts only "..."). Screenshot listing name not the row's company. Not 5 stars or not about the company (age, price fine). Reviewer name not exact. NO QUALIFYING REVIEW: hold.
- Eyebrow doesn't match Review Count and Rating (1 decimal). Row scraped before the refresh: note, not a fail.
- Unsourced or wrong company fact.
- Proof line not exactly `Real Great Roofing: "$90,000 in leads from just one mail drop."`, or details added.
- Other dollar or price words in our copy (review quote exempt), incl. "$750 value", "$500 off"; guarantees, ROI. Write `[NEED: ...]`.
- "Thousands of other customers" or any unapproved claim.
- CTA not `See my page -> ` + Prospect Page URL or `{{page_link}}`. Invented URL, google.com/url wrapper, second ask.
- Fake Re:/Fwd:, urgency, pitch words. Any `brand_check.py --channel cold-email` fail.
- Status = Send, fields outside the handoff list touched, no claim table.

## Pass 2: slots
Subject short, company name. Preview under 90 characters. Headline 3-8 words. Body 1: 25-40 words, verified details, then nearby homes. Body 2: the fixed sentence.

## Pass 3: Seven Sweeps
Clarity, voice (Brennan, peer to peer), so what, prove it, specificity (fits another company = thin), coherence, one click.

## Retry loop
Judge is a separate pass, never the writer. On a brand_check or judge fail, rewrite with the errors fed back; max 2, then escalate to Brennan with all versions.

## Pass 4: panel
1-10 as owner, deliverability, copywriter, Brennan. PASS: all 7+, average 8+; explain the lowest.

## Final copy and handoff (guide §11, Nov 13)
Write **Edited Email Copy**, same layout. Holding: keep Status. At clear time, in order:
1. **Outreach Email:** one address from Hunter's usable list: Verified, valid, deliverable, accept_all false. Never accept-all, unknown, risky, or discovered-only. None: no Ready; reason in Editor Notes.
2. **Lifecycle Stage** = website, then **Landing Page Input Version** +1.
3. **Landing Page Status = Ready** LAST, only when research and final edit are complete, code present, no Hold, and 12b lists an approved landing-page template (MISSING: leave empty, flag Brennan once).
Only these stage fields. Ready never authorizes a send. Never set Published, Building, Needs Fix, Uncertain, Send.

## 1-day rule
Edit within 1 day of Ready for Summary unless the row fails. Daily stall report across every 12b DB (report only, never moves Status): rows past 1 day and why. Grok Bot fixes stalls with the owner.

## Follow-ups and replies
Roofing follow-ups, reply text: PENDING Brennan. Replies stay drafts; no auto-send until he approves. Other trades: legacy checks in the blueprint.

## Output
Edited copy, change log, claim table, scores, PASS/FAIL, held rows.

## Learning loop
Weekly: log repeat fixes and retries in the blueprint; recalibrate if scores disagree with clicks and positive replies.
