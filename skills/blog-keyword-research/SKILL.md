---
name: blog-keyword-research
description: >-
  Use to find, qualify, and prioritize blog topics for the Gorilla Works
  website: mining Google People Also Ask on direct mail and fence-company
  marketing keywords, checking competition and our existing pages, scoring buyer
  intent, and logging the keyword backlog with SEO/AEO answer intents. Use it
  even if the request just says "what should we blog about next?".
---
# Blog keyword research (People Also Ask, SEO/AEO)
Platform rules: blueprints/blog.md. Backlog: blog/keyword-backlog.md.

## Why intent beats volume
A fence owner searching "how to get more fence leads" may book a demo; a homeowner searching "fence cost" never will. We pick questions our buyers ask, where we have something to add, near topics we already own.

## Steps
1. **Seed by the mix:** 50% of topics are fencing (team/industry-mix.md, Oct 23): fence-company marketing questions ("how to get more fence leads", "fence company marketing ideas"), even when the answer isn't mail; the rest rotates roofing, HVAC, siding, electrical, plumbing, landscaping, windows/doors, home services, B2B. Add questions and objections from team/handoffs.md, cold-email replies, and sales notes. For seeds, ask an AI for 10 short seeds plus modifiers, then expand in Semrush.
2. **Harvest PAA** from a live SERP. Tag `PAA` (read live) or `PAA-candidate` (confirm live before writing).
3. **Tag the buyer stage by modifier:** awareness (what is, how to), consideration (best, vs, alternatives), decision (cost, pricing, reviews), implementation (template, examples). Traffic light: green (wants our solution), yellow (maybe later), red (never buys).
4. **Qualify:**
   - Skip if more than 7 of 10 results are big brands.
   - `site:gorillaworksmarketing.com "kw"`: if we already answer it, log an internal-link or refresh task instead. Cluster by SERP overlap (same results = one page).
   - Volume and KD only from Semrush; otherwise `n/a`. Never guess.
   - **Information gain:** write one sentence on what our post would add that the top results lack (an approved fact, a fence-specific example, a template). No sentence, no post.
   - **AI filter:** if AI fully answers it, the goal is a brand mention (`ai-search-visibility`). Favor action queries (local service + city, "<competitor> alternative for <industry>", cost tools).
5. **Score and rank:** customer impact 40%, fit with what we sell 30%, search potential 20%, effort 10%. Fencing greens next to topics we own go first.
6. **Refresh bucket:** flag sleeper pages (links but falling traffic) and pages ranking about 8-20 for a refresh brief; a ranking page usually needs a missing section, not a rewrite.
7. **One question = one post.** The title is the question word for word.
8. **Answer intent:** the consensus answer, scope (state or US), which PAAs become H2s or FAQs, and stats needed (request stat-log IDs from `stat-sourcing-and-verification`).
9. **Log** in the backlog: keyword, source tag, volume/KD, industry, stage, light, score, info-gain line, flag. Log Semrush backlink sightings in backlinks/semrush-sightings.md.
10. Hand the chosen question to `blog-brief-writing`.

## Learning loop
Weekly with GW Analytics (blueprints/blog.md loop): which stages and trades drive demo signups by UTM; adjust scoring weights only with evidence. Log in the blueprint changelog.

Related: `gw-lead-generation` (awareness levels, VOC), `gw-lead-magnets` (magnet problems).
