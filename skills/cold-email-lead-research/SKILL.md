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
Detail, owners, examples: blueprints/cold-email.md. Free public sources only. Never invent, guess, or send. Fewer, verified, dated facts.

## Scope
**Focus:** new work only for the industry Brennan names (currently Roofing); other DBs are setup only. **Exception:** cleanup backfill runs pipeline steps 2-9 on every past row in every 12b DB, Fencing too; failed rows skipped. One niche per list. **Order:** WA, AZ, OR, then west to east. DBs come from **12b**, never hardcoded IDs; no 12b DB for the industry: hold, flag, never write into Fencing. "Focus on <industry>": Grok Bot creates the DB (12a, 12b); you start lookups. MISSING 12b templates hold only that industry.

## Pipeline (your steps; rest in blueprint)
1. **Find:** Maps and state directories one listing at a time (never bulk, signed out), company sites, public LinkedIn, news, trade lists, permits. No logins. Signals and lookalikes: blueprint.
2. **Dedupe, immediately (Brennan):** before any other work, check every Cold Leads DB for the company: root website domain, then normalized name, then phone or Google Place ID. Found: no new row, no repeat work. One row per company, one location.
3. **Qualify:** 31+ Maps reviews only; 30 or fewer or unknown: skip, no row.
4. **Create row** with a **Prospect Page Code**: 12 chars from `abcdefghjkmnpqrstuvwxyz23456789`, unique across 12b DBs; never change one.
5. **Research:** **Address**, **Google Place ID**, live Review Count and Rating, website. **Review pull:** read the 5 newest Maps reviews; best-sounding qualifier first, up to 2 more; none: check 10. Qualifies: 5 stars (any age), about the company (price fine), word for word, screenshot listing name matches. **Reviews** holds only:
`★5 | name | relative date (captured date) | "text" | Maps URL | proof: screenshot path`
Nothing in 10: `NO QUALIFYING REVIEW (checked date)` = failed. Never blank. Email patterns: blueprint; verify within 7 days of sending; flag catch-alls; bounces under 2%.

## Failed rows
**Failed check:** Status Failed, Bad match, Drop; Hunter invalid or no usable verified email; editor HOLD/QA FAIL; NO QUALIFYING REVIEW; listing 30 or fewer reviews (backfill/step check: Status = Failed, reason "review count 30 or fewer"). No backfill, code, Hunter re-run, handoff, or Ready; report as failed with reason, not stalled. **Existing duplicates:** keep the most complete row (else oldest); mark others Status = Drop, reason "duplicate of <kept row>"; never delete.

## Complete every step (Brennan)
On any row you touch, dedupe first, then check every pipeline field. Any missing, even if later ones are filled: run that step or hand it to its owner first. A step that finds a failure marks the row failed and stops. Gating and focus (plus backfill) apply.

## Account brief
3-layer (human, company, space: problems the niche already names; never invent one). Fit, dated signal, priority, **3-5 hooks** (source URL, date, confidence), angle, what to avoid, "hook found: yes/no". Only professional or clearly public facts; never sensitive topics (blueprint), guesses, conflicting numbers as fact (mark [U]). Hooks tie to lead flow or neighbors. **No strong hook: HOLD.**

## Output
Briefs, CRM rows (fields: blueprint), hold/failed lists with reasons. Non-failed Ready for Summary rows: drafted and edited within 1 day.

## Learning loop
Weekly with GW Analytics: hooks, signals that earned positive replies; log in blueprint. See `cold-email-copy`, `gw-lead-generation`.
