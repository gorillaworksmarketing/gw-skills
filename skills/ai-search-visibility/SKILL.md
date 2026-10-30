---
name: ai-search-visibility
description: >-
  Use to get Gorilla Works found, accurately described, cited, and recommended
  by AI answers (Google AI Overviews, ChatGPT, Perplexity, Gemini). Covers the
  visibility ladder, answer-first format, the six-gap check, entities, accuracy
  fixes, mentions, and measurement. Use it whenever AEO, GEO, AI Overviews, or
  brand mentions come up, even if the request just asks how to show up in
  ChatGPT.
---
# AI search visibility
Details: blueprints/blog.md (AEO and GEO sections). Stats: research/stat-log-pending.md (attribute). Base rule: helpful-first quality for the real reader.
**GEO vs SEO:** SEO ranks pages; GEO gets us named in AI answers. Same core: a trusted page that clearly answers a real question. Google says no special AI markup or files are needed and warns against writing separate content for AI.

## The ladder
Retrieved, then cited (our page is a source), then mentioned (our name appears), then **recommended** (on the shortlist). Citations come from useful pages; recommendations come mostly from what the rest of the web says. Test: if an AI ignored our site, would reviews, directories, press, and forums still put us on the list?

## Steps
1. **Questions:** money terms (ours and competitors') as questions, plus sales, cold-email, Reddit questions. Filters: "do we deserve to show up?", then "can AI fully answer it?" (if yes, aim for a mention).
2. **Tracker:** run each question 3-5 times on ChatGPT, Perplexity, and Google AIO. Log rate with sample size ("named 2/5"), position, cited domains, framing. One run is an anecdote.
3. **Monthly six-gap check** (visibility, narrative, topic, format, web mentions, demand): plan fix, build, or influence. Quarterly competitor audit.
4. **Pages:** match the cited page type; answer first under real-question headings; small tables; one approved fact nobody else has (`longform-seo-article`).
5. **Accuracy ledger:** log each claim an AI makes about us (accurate, stale, false, missing qualifier), its likely source, and severity (price or service errors first). Fix our own page first (plain, dated fact), then request corrections.
6. **Entities:** identical facts and NAP on GBP, Bing Places, Yelp, Apple Maps, LinkedIn, Crunchbase, Wikidata, Grokipedia (never paid indexing), directories.
7. **Technical (recommend to Brennan):** SSR or prerendering (raw HTML is empty today); sitemap in Bing Webmaster Tools; Organization (sameAs) and Article schema; allow search bots (OAI-SearchBot, Claude-SearchBot, PerplexityBot) and decide training bots (GPTBot, ClaudeBot, Google-Extended) separately; consider llms.txt; redirect hallucinated 404s.
8. **Mentions, three tiers:** Tier 1 editorial lists, expert quotes, unlinked-mention reclaims (`link-building`); Tier 2 genuine Reddit/Quora answers on cited threads (`reddit-comment`); Tier 3 own LinkedIn and YouTube. Outreach is draft-only; Brennan approves sends. No paid placements.
9. **Experiment:** test vs. control question sets, 2 weeks before and after, with GW Analytics; reproduce before promoting a rule.
10. **Freshness:** real refreshes; verify a citation on 3 different days.
11. **Measure:** naming rate over time; GA4 "AI traffic" regex; bot logs; lead to closed-won by channel; "How did you hear about us?" with AI options on /book-demo. Log Semrush backlink sightings in backlinks/semrush-sightings.md.

## Learning loop
Monthly tracker diff plus the weekly blog loop; log in blueprints/blog.md changelog.
