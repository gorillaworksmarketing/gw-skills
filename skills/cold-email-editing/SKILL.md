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
Spec: blueprints/cold-email.md; contract: guide v3.22 §0. Apply `gw-brand-guidelines`, `gw-claims-guardrails`, `gw-fact-check`, `gw-qa-gate`. Never send.
Work only the industry Brennan names (currently Roofing), plus backfill rows from any 12b DB. **Roles:** edit rows from both writers (Claude (Replit), Grok Bot); never change Copywriter or Email Copy.

## Pass 1: hard fails (any = FAIL; list fixes; detail: blueprint)
- Any `cold-email-copy` slot or hard rule broken (labels, order, extras, Ember-only parts, quote, eyebrow, proof, price, CTA, pitch words).
- **Review quote** not word for word with its screenshot, listing name not the company, or "…" text.
- Unsourced/wrong fact, guarantees, ROI, unapproved claims (write `[NEED: ...]`); `brand_check.py --channel cold-email` fail.
- Status = Send, fields beyond the handoff list, no claim table. Generic drafts go back with notes.

## Pass 2-4
Sweeps: clarity, voice, so what, prove it, specificity, coherence, one click. Panel 1-10 (4 judges: blueprint): all 7+, avg 8+; explain lowest. **Retry:** separate judge pass; on fail rewrite; max 2, then send Brennan all versions.

## Final copy and handoff (guide 0.9)
**Edited Email Copy**, same layout, own Subject (never pair the original subject). Re-read the row right before writing. In order:
1. **Outreach Email:** one address from the row's Hunter usable results (Verified, valid, deliverable, accept_all false, not disposable). Prefer a company-domain role inbox; one published on its own site counts, even webmail (Brennan). Never vendor, guessed, discovered-only; Verified select is not Hunter. None: failed, reason in Editor Notes; keep copy.
2. **Lifecycle Stage** = website, then **Landing Page Input Version** +1 only on first handoff, changed build inputs, or Brennan's rebuild ask (blueprint).
3. **Landing Page Status = Ready** LAST: final edit, usable email, code, no active hold, industry template approved in 12b. MISSING (e.g. Fencing): Outreach Email only; flag Brennan once per industry.
Status stays Editing; Ready never permits a send. Never bulk Ready. Never write Building, Published, Needs Fix, Uncertain, Built Version, Last Built, Prospect Page URL, Send; never reset Uncertain to Ready or rebuild a live page.

## Failed rows, steps, stalls
**Failed check:** Status Failed, Bad match, Drop (duplicates too; flag any you notice); Hunter not usable; active HOLD/FAIL (Editor Notes first line starts HOLD or FAIL, maybe after "Sweep N:"; "HOLD cleared" is not); NO QUALIFYING REVIEW; Review Count 30 or fewer (backfill/step check: Status = Failed, reason "review count 30 or fewer"). Never work it; report with reason.
**Complete every step (Brennan):** dedupe first; any missing pipeline field: run it if yours, else hand to its owner. A failure marks the row failed and stops.
**1-day rule:** edit within 1 day. Daily stall report, all 12b DBs: rows over 1 day at any stage (list: blueprint), role, reason; never move Status. Grok Bot fixes stalls.
**Retries:** reads may retry (429 Retry-After; 409/5xx up to 3); writes: log, read back, redo only if not applied.

## Follow-ups, output, loop
Roofing follow-ups, replies: PENDING Brennan; drafts only. Fencing backfill: legacy checks (blueprint). Output: copy, changes, claims, scores, PASS/FAIL, prepared, skipped, failed rows with reasons; never report Ember outputs. Weekly: log repeat fixes, retries in blueprint; recalibrate if scores miss replies.
