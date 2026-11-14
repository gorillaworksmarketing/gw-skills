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
Spec: blueprints/cold-email.md, guide §11-12. Apply `gw-brand-guidelines`, `gw-claims-guardrails`, `gw-fact-check`, `gw-qa-gate`. Never send.

Work only the industry Brennan names (currently Roofing), plus backfill rows from any 12b DB; setup is not work. One job: a click to their page. Generic drafts go back with notes.

## Pass 1: hard fails (any = FAIL; list fixes)
- Labeled lines missing, misordered, misspelled, extra; greeting, checklist, strip, signature, footer.
- **Review quote:** not from a **Reviews** line or not word for word with its screenshot (cuts only "..."); listing name not the company; not 5 stars or not about the company (age, price fine); reviewer name not exact.
- Eyebrow not matching Review Count, Rating (1 decimal); pre-refresh: note only.
- Unsourced/wrong fact. Proof line not exactly `Real Great Roofing: "$90,000 in leads from just one mail drop."`, or details added.
- Other price words in our copy (quote exempt); guarantees, ROI. Write `[NEED: ...]`.
- "Thousands of other customers" or unapproved claims.
- CTA not `See my page -> ` + Prospect Page URL or `{{page_link}}`; invented URL, google.com/url wrapper, second ask.
- Fake Re:/Fwd:, urgency, pitch words; `brand_check.py --channel cold-email` fail.
- Status = Send, fields beyond the handoff list, no claim table.

## Pass 2-4
Slots per `cold-email-copy`. Sweeps: clarity, voice (Brennan), so what, prove it, specificity, coherence, one click. Panel 1-10 (owner, deliverability, copywriter, Brennan): all 7+, avg 8+; explain lowest.

**Retry:** judge is a separate pass, never the writer; on a fail, rewrite with errors; max 2, then send Brennan all versions.

## Final copy and handoff (guide §11)
**Edited Email Copy**, same layout; holding keeps Status. At clear time, in order:
1. **Outreach Email:** one Hunter usable address (Verified, valid, deliverable, not accept-all; never unknown, risky, discovered-only). None: failed, reason in Editor Notes.
2. **Lifecycle Stage** = website, then **Landing Page Input Version** +1.
3. **Landing Page Status = Ready** LAST, only when research and edit are done, code present, no Hold, and 12b shows the industry's landing-page template approved. MISSING (e.g. Fencing): Outreach Email only; flag Brennan once.
Only these stage fields. Ready never authorizes a send. Never Published, Building, Needs Fix, Uncertain, Send.

## Failed rows and 1-day rule
**Failed check:** Status Failed, Bad match, Drop (incl. duplicates; flag any duplicate you notice); Hunter invalid or no usable verified email; your HOLD/QA FAIL; NO QUALIFYING REVIEW; Review Count 30 or fewer (backfill/step check: Status = Failed, reason "review count 30 or fewer"). Never backfill, code, re-run Hunter, hand off, set Ready; report as failed with reason. Others: edit within 1 day.
**Complete every step (Brennan):** on rows you touch, dedupe first; any missing pipeline field (research, Reviews, count, code, Hunter, draft): run it if yours, else hand to its owner (blueprint) first. A step finding a failure marks the row failed and stops. Daily stall report, all 12b DBs (no Status moves); Grok Bot fixes stalls.

## Follow-ups and replies
Roofing follow-ups, replies: PENDING Brennan; drafts, no auto-send. Fencing backfill: legacy checks, blueprint.

## Output
Copy, changes, claims, scores, PASS/FAIL, held/failed rows.

## Learning loop
Weekly: log repeat fixes, retries in blueprint; recalibrate if scores disagree with clicks, replies.
