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
Detail: blueprints/cold-email.md. Free public sources only. Never invent or guess. Bots never send.

## Why
Fewer, verified, dated facts; the Copywriter picks the angle.

## Find
1. **Mix:** roofing first, then team/industry-mix.md. **One niche per list**; never mix trades.
2. **Sources:** Google Maps and WA directories (one by one, never bulk-scrape), company sites, GBP and reviews, public LinkedIn, local news, podcasts, trade and chamber lists, permits. No logins.
3. **Signals (dated):** new location or area, permits, hiring, new owner or role, recent post, review surge or few reviews, no ads, website status. Filter on real break points, cheapest first. Check CRM for prior contact.
4. **Lookalikes:** from best clients and positive repliers.
5. **Email:** first@, first.last@, flast@ on the domain; verify within 7 days of sending; flag catch-alls; bounces under 2%.

## Required review pull (part of each Maps lookup, never skipped)
One listing at a time, never bulk. Read the 5 most recent Google Maps reviews; put the best-sounding qualifying one first, then up to 2 more. None qualify: check up to 10 most recent. **Qualifies:** 5 stars (any age), directly about the company (price mentions fine), word for word, and a screenshot whose listing name matches the row's company. Write the live count and rating into Review Count and Rating (the source). **Reviews** holds only Google Maps ★5 lines:
`★5 | name | relative date (captured date) | "text" | Maps URL | proof: screenshot path`
Nothing in 10: `NO QUALIFYING REVIEW (checked date)`. Never blank.

## Registry and new rows (guide §11-12)
- DBs come from the **12b registry**, never hardcoded IDs. No 12b DB for the industry: hold, flag, never write into Fencing.
- Every new row gets a **Prospect Page Code**: 12 characters from `abcdefghjkmnpqrstuvwxyz23456789`, unique across all 12b DBs. Never change an existing code.
- In the same signed-out Maps lookup, fill **Address** and **Google Place ID**.
- "Focus on <industry>" (Brennan): Grok Bot creates the DB from 12a and adds it to 12b; you start Maps lookups.

## 3-layer research (5-7 minutes)
1. **Human:** role, tenure, career, talks, posts.
2. **Company:** site, press, values, projects, awards, our history.
3. **Space:** problems the niche already talks about, in their words [V7]. Never invent one.

## Account brief (one per lead)
Fit, dated signal, priority (hot, warm, cold, skip), **3-5 hooks** with source URL, date, confidence; suggested angle, what not to mention, "hook found: yes/no".
- **Allowed:** professional or clearly public business facts (area, project, review reply, award, podcast, public quote, chamber tie).
- **Never:** private-feeling or sensitive topics (health, family, religion, politics, finances, age), guesses, conflicting numbers as fact (mark [U]).
- **So what:** each hook ties to their lead flow or neighbors, or it's weak.
- **No strong hook: HOLD the lead.** Depth beats volume.

## CRM fields
As in the blueprint: verify and signal dates, hook URLs, contact source URL and date, hold reason, unsubscribe flag, problem, last campaign date, utm_campaign `<industry>_<type>`.

## Output
Account briefs, CRM rows, and a hold list with reasons. Ready for Summary rows are drafted and edited within 1 day unless they fail.

## Learning loop
Weekly with GW Analytics: hook types and signals that earned positive replies; log changes in the blueprint.

Related: `cold-email-copy`, `gw-lead-generation`.
