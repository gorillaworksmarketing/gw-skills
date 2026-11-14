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
Spec, pipeline, owners: blueprints/cold-email.md. Apply `gw-brand-guidelines` (persona reset; pass `brand_check.py --channel cold-email`), `gw-content-rules`, `gw-claims-guardrails`, `gw-fact-check`; hand drafts to `cold-email-editing`. Brennan sends.

## Goal
One job: a click to the personal landing page built for the company. No call booking, "reply yes", offer amounts. Never write the greeting, checklist, channel strip, signature, or footer/opt-out (Brennan's Ember HTML).

## Before writing
Brief from lead research. **No hook: hold, say why.** DBs come from **12b**, never hardcoded IDs. Draft only for the industry Brennan names (currently Roofing), plus backfill rows from any 12b DB; other DBs are setup. Gates are per industry: 12b email template MISSING holds only its rows at Ready for Summary; flag Brennan once. Write only your own rows.
**Complete every step (Brennan):** dedupe first, then check every pipeline field; any missing (research, Reviews, count, code, Hunter) goes to its owner before drafting. Never on failed rows; a failure found marks the row failed and stops.

## Where it goes
**Email Copy**, plain text, one labeled line per slot, in order:
Subject: / Preview: / Eyebrow: / Headline: / Review quote: / Review name: / Body paragraph 1: / Body paragraph 2: / Proof line: / CTA:

## Slot rules
1. **Subject:** short, with the company name. No fake Re:, urgency, pitch words.
2. **Preview:** under 90 characters; default in blueprint.
3. **Eyebrow:** "<Review Count> Google reviews at <Rating, 1 decimal>".
4. **Headline:** 3-8 words, verified hook.
5. **Review quote:** only from a ★5 **Reviews** line (usually the first), word for word. Cut only with "..."; never reword, fix typos, merge. Max 20 words.
6. **Review name:** exactly as the source shows it.
7. **Body paragraph 1:** 25-40 words: verified details, then nearby homes needing the same work.
8. **Body paragraph 2:** fixed sentence; only the short company name changes.
9. **Proof line:** exactly `Real Great Roofing: "$90,000 in leads from just one mail drop."` No details or other stats.
10. **CTA:** `See my page -> ` + Prospect Page URL, else `{{page_link}}`. Never invent or edit it; no google.com/url wrappers.

## Hard rules
- No price or cost wording ($0.78, "under $1", stamps, "$750 value", "$500 off"); only the proof line has a dollar figure; review quote exempt.
- Never "thousands of other customers".
- No hashtags, em dashes, AI tells, clichés; grade 6-7.
- Draft only. Never Status = Send or Ember send settings. Set Editing; no other workflow fields.
- Coherence check. Attach the `gw-fact-check` table: count, rating, quote source, company facts, proof line.

## Failed rows and 1-day rule
**Failed check:** Status Failed, Bad match, Drop (incl. duplicates); Hunter invalid or no usable verified email; editor HOLD or QA FAIL; NO QUALIFYING REVIEW; listing with 30 or fewer reviews (backfill or step check: set Status = Failed, reason "review count 30 or fewer", skip). Never draft, backfill, advance it; report as failed with the reason. Others: drafted and edited within 1 day (Claude/Replit 25 a day, Grok Bot the rest). Reports list stalled rows, why; Grok Bot fixes stalls.

## Follow-ups and replies
Roofing follow-ups, replies: PENDING Brennan; drafts, no auto-send. Fencing backfill: legacy flow (blueprint).

## Learning loop
Weekly with GW Analytics: clicks, replies by headline, hook, review; Editor fixes; log in blueprint.
