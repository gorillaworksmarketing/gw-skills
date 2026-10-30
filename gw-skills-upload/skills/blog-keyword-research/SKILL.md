---
name: blog-keyword-research
description: Use to find and qualify blog topics for the Gorilla Works website, mining Google People Also Ask questions on direct mail keywords by industry priority, checking competition and existing pages, and logging them in the keyword backlog with search intent (intent over volume) and SEO/AEO answer intents. Use it even if the request doesn't name the skill.
---
# Blog keyword research (People Also Ask, SEO/AEO)
Platform rules: blueprints/blog.md. Backlog: blog/keyword-backlog.md.

## Steps
1. **Seed** direct-mail keywords per industry, rotating per team/industry-mix.md (fencing, HVAC, roofing, siding, electrical, plumbing, landscaping, windows/doors, home services, B2B; at most 1-2 of every 5 on fencing), plus questions and objections from team/handoffs.md.
2. **Harvest People Also Ask** questions from a live SERP. Tag them `PAA` (read live) or `PAA-candidate` (found indirectly; confirm in a live SERP before writing).
3. **Qualify each question:**
   - Big-brand count: skip if more than 7 of the 10 results are big brands.
   - `site:gorillaworksmarketing.com "kw"`: if a page already answers it, add an internal-link task instead.
   - Volume and difficulty only from a real tool (Semrush); otherwise `n/a`. Never guess.
   - **Intent over volume:** tag informational, navigational, commercial, or transactional from what ranks. Favor money modifiers ("best X for Y", "X vs Z", "X cost", "X under [budget]") over high-volume, no-buyer queries.
3b. **AI filter** (blueprints/blog.md, VT-AHR/VT-AEO): if AI can fully satisfy the query, the goal is a brand mention (hand it to `ai-search-visibility`); prioritize action/transactional queries (local service + city, "<competitor> alternatives", calculators/cost tools). Add fan-out subqueries (best, top, versus, review, alternative).
3a. **BID vetting:** Business potential, Intent, Difficulty, then the AI filter. Tool queries keep clicks. Fan-out subqueries are a topic map (most have zero volume). Flag sleeper pages (backlinks but declining traffic) for refresh.
3b2. **Prompt mining:** pull fears, doubts, and context from Brennan's sales-call notes (if shared), support emails, and Reddit. Apply "do we deserve to show up?". Add "<competitor> alternative for <industry>", three-way listicles, and tool ideas (cost calculator [JUDGMENT]).
3a2. **Traffic light (Deel):** tag green (wants our solution), yellow (maybe or later), red (never buys); write greens high-to-low volume. **Cluster by SERP overlap** (same results = one page); prioritize volume × topical authority × intent; start next to topics we own (fencing first).
3c. **Seeds:** ask an AI for 10 short seeds plus 5+ modifiers; expand in a keyword tool.
3d. **Clusters:** tag each question to the money page it supports (topical authority before link outreach).
4. **One question = one post.** The title is the question word for word.
5. **Answer intent:** note the consensus answer, the geographic scope (state/US), and which related PAAs become H2s or FAQ entries. Note any stats needed; request stat-log IDs from `stat-sourcing-and-verification`.
5b. **Semrush handoff:** log any backlink data seen in backlinks/semrush-sightings.md.
6. **Log it** in the backlog: keyword, source tag, volume/KD, industry, intent, awareness stage, flag (unused/used).
7. Hand the chosen question to `blog-brief-writing`.

Skills to reference: `gw-lead-generation` (awareness levels, top-20% traits, FAQs, magnet problems).
