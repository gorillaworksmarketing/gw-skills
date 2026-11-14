---
name: cold-email-copy
description: >-
  Use whenever GW Email Copywriter writes a Gorilla Works cold email: the
  roofing landing-page email (personal page click), subject and preview,
  follow-ups, or objection replies (roofing first, then other trades). Built on
  Brennan's format spec, cold-email training and videos. Email only, no
  LinkedIn. Use it even if the request just says "write the emails for these
  leads".
---
# Cold email copy (GW Email Copywriter)
Spec, owners: blueprints/cold-email.md; guide v3.22 §0. Apply `gw-brand-guidelines` (persona reset; pass `brand_check.py --channel cold-email`), `gw-content-rules`, `gw-claims-guardrails`, `gw-fact-check`; hand drafts to `cold-email-editing`. Brennan sends.

## Goal
One job: a click to the company's personal page. No call booking, "reply yes", offer amounts. Never greeting, checklist, channel strip, signature, footer (Ember HTML).

## Before writing
Brief from lead research. **No hook: hold, say why.** DBs from **12b**, no hardcoded IDs. Draft only for the industry Brennan names (currently Roofing), plus backfill rows from any 12b DB. Gates are per industry: a MISSING 12b email template holds only its rows at Ready for Summary; flag Brennan once.
**Roles (guide 0.8):** write only rows where Copywriter = Grok Bot; never touch Claude (Replit) originals or Copywriter. Editor edits both; Ember reads both.
**Complete every step (Brennan):** dedupe first, then check every pipeline field; any missing (research, Reviews, count, code, Hunter) goes to its owner before drafting. Never on failed rows; a failure found marks the row failed and stops.

## Where it goes
**Email Copy**, plain text, one labeled line per slot, in order:
Subject: / Preview: / Eyebrow: / Headline: / Review quote: / Review name: / Body paragraph 1: / Body paragraph 2: / Proof line: / CTA:

## Slot rules
1. **Subject:** short, with the company name. No fake Re:, urgency, pitch words.
2. **Preview:** under 90 characters; default in blueprint.
3. **Eyebrow:** "<Review Count> Google reviews at <Rating, 1 decimal>".
4. **Headline:** 3-8 words, verified hook.
5. **Review quote:** only from a complete ★5 review (a `★5 |` line, or legacy `[5★]` with full text), word for word; never text ending in "…". Cut only with "..."; never reword, fix typos, merge. Max 20 words.
6. **Review name:** exactly as the source shows it.
7. **Body paragraph 1:** 25-40 words: verified details, then nearby homes needing that work.
8. **Body paragraph 2:** fixed sentence; only the short company name changes.
9. **Proof line:** exactly `Real Great Roofing: "$90,000 in leads from just one mail drop."`, nothing added.
10. **CTA:** `See my page -> {{page_link}}`; confirmed Ember URL only once written (none yet). Never invent a URL; no google.com/url wrappers. Other trades: no link in email 1.

## Hard rules
- No price or cost wording (examples: blueprint); only the proof line has a dollar figure; review quote exempt.
- Never "thousands of other customers".
- No hashtags, em dashes, AI tells, clichés; grade 6-7
- Draft only. Never Status = Send or Ember send settings. Set Editing; no other workflow fields.
- Coherence check; attach the `gw-fact-check` table (blueprint).

## Failed rows and 1-day rule
**Failed check:** Status Failed, Bad match, Drop (incl. duplicates); Hunter invalid or no usable verified email; active editor HOLD/FAIL (blueprint); NO QUALIFYING REVIEW; 30 or fewer reviews (backfill/step check: Status = Failed, reason "review count 30 or fewer"). Never work it; report as failed with reason. Others: drafted and edited within 1 day (split: blueprint). Reports list stalled rows, why; Grok Bot fixes stalls.

## Follow-ups and replies
Roofing follow-ups, replies: PENDING Brennan; drafts, no auto-send. Fencing backfill: legacy flow (blueprint).

## Learning loop
Weekly with GW Analytics: clicks, replies by headline, hook, review, Editor fixes; log in blueprint.
