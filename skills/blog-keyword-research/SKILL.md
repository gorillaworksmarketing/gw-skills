---
name: blog-keyword-research
description: >-
  Use to find, qualify, and prioritize blog topics for the Gorilla Works
  website from Semrush (the only keyword source), checking competition and
  existing pages, scoring buyer intent, and logging the SEO/AEO keyword
  backlog. Use it even if the request just says "what should we blog about
  next?".
---
# Blog keyword research (Semrush, SEO/AEO)
Platform rules: blueprints/blog.md. Backlog: blog/keyword-backlog.md.

## Topic source (Brennan, Nov 24)
Semrush is the only keyword research source for blog posts. All or almost all posts come from Semrush keywords plus GW Video Research (`video-research`). Use only the `user-Semrush` MCP connector and the free tier (10 web searches a day); buy no units. On `no_api_units`, stop, write `n/a`, and report (`api-issue-handling`). Never guess volume or KD. PAA is not the topic source; after the Semrush keyword is chosen it may support question wording and AEO answers (H2s, FAQs). Do not mine PAA or Google Trends to pick topics. Pick questions our buyers ask, where we have something to add, near topics we already own.

## Steps (detail: blueprints/blog.md)
1. **Seed by the mix (team/industry-mix.md, Nov 10):** HVAC, roofing, and B2B direct mail lead; general direct mail as support; fencing max 3 posts/week. Add questions and objections from team/handoffs.md, cold-email replies, and sales notes. For seeds, ask an AI for 10 short seeds plus modifiers, then expand in Semrush.
2. **Expand in Semrush.** Tag source `Semrush`.
3. **Buyer stage by modifier:** awareness (what is, how to), consideration (best, vs, alternatives), decision (cost, pricing, reviews), implementation (template, examples). Light: green (wants our solution), yellow (maybe later), red (never buys).
4. **Qualify:** skip if more than 7 of 10 results are big brands. `site:gorillaworksmarketing.com "kw"`: if we already answer it, log an internal-link or refresh task instead. Cluster by SERP overlap (same results = one page). Volume and KD only from Semrush; otherwise `n/a`; never guess. **Information gain:** one sentence on what our post adds that the top results lack (approved fact, fence-specific example, template); no sentence, no post. **AI filter:** if AI fully answers it, the goal is a brand mention (`ai-search-visibility`). Favor action queries (local service + city, "<competitor> alternative for <industry>", cost tools).
5. **Score:** customer impact 40%, fit with what we sell 30%, search potential 20%, effort 10%. Fencing greens next to topics we own go first.
6. **Refresh:** flag sleeper pages (links but falling traffic) and pages ranking about 8-20 for a refresh brief; a ranking page usually needs a missing section, not a rewrite.
7. **One question = one post.** The title is the question word for word.
8. **Answer intent:** consensus answer, scope (state or US), related questions (PAA only as supporting wording) as H2s or FAQs, and stats needed (stat-log IDs from `stat-sourcing-and-verification`).
9. **Log** in the backlog: keyword, source tag (`Semrush`), volume/KD, industry, stage, light, score, info-gain line, flag. Log Semrush backlink sightings in backlinks/semrush-sightings.md.
10. Hand the chosen keyword to `blog-brief-writing` and `video-research`.

## Learning loop
Weekly with GW Analytics (blueprints/blog.md loop): adjust scoring weights only with evidence from demo signups by UTM; log in the changelog. Related: `gw-lead-generation`, `gw-lead-magnets`.
