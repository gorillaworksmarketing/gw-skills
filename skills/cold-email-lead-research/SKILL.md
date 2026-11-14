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
Detail: blueprints/cold-email.md. Free public sources only. Never invent or guess. Never send. Fewer, verified, dated facts; the Copywriter picks the angle.

## Find
1. **Mix:** roofing first, then team/industry-mix.md. **One niche per list**; never mix trades.
2. **Sources:** Google Maps and WA directories (one by one, never bulk-scrape), company sites, public LinkedIn, news, trade lists, permits. No logins.
3. **Signals (dated):** new location, permits, hiring, new owner, recent post, review surge, no ads, website. Filter cheapest first. Check CRM for prior contact.
4. **Lookalikes:** from best clients and positive repliers.
5. **Email:** first@, first.last@, flast@; verify within 7 days of sending; flag catch-alls; bounces under 2%.

## Required review pull (part of each Maps lookup, never skipped)
**Target (Brennan):** only listings with 31+ Maps reviews; 30 or fewer or unknown: skip before creating a row. One listing at a time, never bulk. Read the 5 most recent Maps reviews; best-sounding qualifying one first, then up to 2 more. None: check up to 10. **Qualifies:** 5 stars (any age), about the company (price fine), word for word, screenshot listing name matches the company. Write live count and rating into Review Count and Rating. **Reviews** holds only Maps ★5 lines:
`★5 | name | relative date (captured date) | "text" | Maps URL | proof: screenshot path`
Nothing in 10: `NO QUALIFYING REVIEW (checked date)` = failed. Never blank.

## Registry and new rows (guide §11-12)
- DBs come from the **12b registry**, never hardcoded IDs. No 12b DB for the industry: hold, flag, never write into Fencing.
- Every new row gets a **Prospect Page Code**: 12 characters from `abcdefghjkmnpqrstuvwxyz23456789`, unique across all 12b DBs. Never change an existing code.
- Same signed-out Maps lookup: fill **Address** and **Google Place ID**.
- "Focus on <industry>": Grok Bot creates the DB from 12a, adds it to 12b; you start Maps lookups. A MISSING 12b template holds only that industry.
- **Failed check** (Status Failed, Bad match, Drop; Hunter invalid or no usable verified email; editor HOLD/QA FAIL; NO QUALIFYING REVIEW; listing 30 or fewer reviews): never backfill, code, re-run Hunter, hand off, set Ready. Report as failed with reason, not stalled.

## 3-layer research (5-7 minutes)
Human (role, tenure, talks, posts); company (site, press, projects, awards, our history); space (problems the niche already names, in their words; never invent one).

## Account brief (one per lead)
Fit, dated signal, priority (hot, warm, cold, skip), **3-5 hooks** with source URL, date, confidence; suggested angle, what not to mention, "hook found: yes/no".
- **Allowed:** professional or clearly public business facts.
- **Never:** private or sensitive topics (health, family, religion, politics, finances, age), guesses, conflicting numbers as fact (mark [U]).
- **So what:** each hook ties to their lead flow or neighbors.
- **No strong hook: HOLD the lead.** Depth beats volume.

## CRM fields
Per blueprint: verify and signal dates, hook URLs, contact source and date, hold reason, unsubscribe flag, problem, last campaign, utm_campaign `<industry>_<type>`.

## Output
Briefs, CRM rows, hold and failed lists, reasons. Non-failed Ready for Summary rows are drafted and edited within 1 day.

## Learning loop
Weekly with GW Analytics: hooks and signals that earned positive replies; log in the blueprint.

Related: `cold-email-copy`, `gw-lead-generation`.
