---
name: cold-email-lead-research
description: >-
  Use when GW Lead Research finds fencing, roofing, home service, or B2B
  prospects and builds account briefs and CRM rows for cold email: free public
  sources, dated signals, email permutations plus verification, lookalikes,
  3-layer research, and 3-5 verified hooks with source URLs. Holds leads with no
  hook. Use it even if the request just says "find me 20 fence companies".
---
# Cold email lead research
Detail, owners: blueprints/cold-email.md; contract: guide v3.22 §0. Lookups per `gw-google-places-budget`. Never invent, guess, pay for enrichment, or send.

## Scope
**Focus (Brennan):** new work only for the industry Brennan names (currently Roofing). **Exception:** one-time backfill of steps 2-9 on every past row in every 12b DB, Fencing too; failed rows skipped. Systems are all-industry (12b; approved template, guide 0.1); never widens focus. **Order:** WA, AZ, OR, then west to east. DBs from **12b** only; no 12b DB: hold, flag, never write into Fencing or another industry.

## Pipeline (later steps: blueprint)
1. **Find** one listing at a time (sources: blueprint). No logins.
2. **Dedupe, immediately (Brennan):** before any other work, search every Cold Leads DB (root domain, then normalized name, then phone or Place ID; ignore shared platform domains: blueprint). Found: no row, no repeat work. One row, one location per company.
2b. **Website + industry check (Brennan, Nov 20; replaces Nov 19), before any row or Hunter:** Website = the Maps listing's link; another URL only if clearly the same business. Industry from the site (homepage/services) against the 12b list, never from name, search query, or substring. Roofing: repair, replacement, install, cleaning, moss, coatings, gutters. Wrong industry: move to that 12b table and set Industry (not a fail). Moved out of an active industry (only Roofing is active): HOLD, no further work. **HOLD only** (never fail) if the Maps website is clearly a different business, or industry can't be determined.
3. **Qualify (Brennan, Nov 23):** 30+ Maps reviews; under 30 or unknown: skip, no row.
4. **Row + Prospect Page Code:** 12 chars from `abcdefghjkmnpqrstuvwxyz23456789`, unique across 12b; collision: hold, report, never re-code. Never change a code; none on failed rows (blueprint).
5. **Research:** required: Company, Website, Rating, Review Count, one complete ★5 review with proof, full site text in page body (Source: url + date). Rest per `gw-google-places-budget`; not found: "not available". Label facts website / Maps / directory / idea. Review pull: blueprint. None in 10: `NO QUALIFYING REVIEW (checked date)` = failed. Emails: verify per `cold-email-deliverability`; Hunter only via Ember.

## Failed rows
**Failed check:** Status Failed, Bad match, Drop; Hunter not usable (Verified select = your match flag, not Hunter); active HOLD/FAIL (blueprint); NO QUALIFYING REVIEW; under 30 reviews (backfill: Status = Failed, reason "review count under 30"). Never work them; report why. **Existing duplicates (bulk Drop confirmed, Brennan 5:29 PM):** keep the most complete (edited copy, then furthest stage; tie: oldest); others Status = Drop, "duplicate of <kept page id>"; never delete.

## Complete every step (Brennan)
On any touched row, dedupe first, then every pipeline field. Any missing, even if later ones are filled: run it or hand it to its owner first. A failure marks the row failed and stops. Gating, focus, backfill apply.
**Retries:** reads may retry (429 Retry-After; 409/5xx up to 3). Writes, paid calls: log, read back, redo only if not applied.

## Account brief
3 layers, fit, dated signal, priority, 3-5 sourced hooks, angle, avoid (blueprint). Public professional facts only; no guesses; conflicting numbers [U]. **No strong hook: HOLD.**

## Output and learning loop
Briefs, CRM rows, hold/failed lists. 1-day rule (blueprint). Weekly with GW Analytics (blueprint).
