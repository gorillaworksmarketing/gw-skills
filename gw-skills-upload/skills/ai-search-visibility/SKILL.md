---
name: ai-search-visibility
description: Use to get Gorilla Works found, accurately described, and cited by AI answers (Google AI Overviews, ChatGPT, Perplexity, Gemini). Covers GEO vs SEO, the answer-first quotable format, the Graphite playbook, the monthly six-gap check, entities/schema, misinformation fixes, mention tiers, experiments, and AI measurement. Use it whenever AEO, GEO, AI Overviews, or brand mentions come up, even if the request just asks how to show up in ChatGPT.
---
# AI search visibility
Details: blueprints/blog.md (AEO and GEO sections). Stats: research/stat-log-pending.md (attribute). Base rule: helpful-first quality, written for the real reader.
**GEO vs SEO:** SEO ranks in results; GEO gets us named and cited in AI answers. Same core: a trusted page that clearly answers a real question. AIs crawl, store, and pick sources like Google.

## Steps
1. **Questions:** turn money terms (ours and competitors') into questions; add sales/support/Reddit questions. Filters: "do we deserve to show up?", then "can AI fully satisfy it?" (if yes, aim for a mention inside the answer).
2. **Cheap answer tracker:** ask each question several times, in variants, on 3 surfaces (ChatGPT, Perplexity, Google AIO). Log share of voice, average position, cited domains, and **accuracy/sentiment**.
3. **Monthly check:** classify the **six gaps** (visibility, narrative, topic, format, web mentions, demand) and plan **fix / build / influence**. Quarterly competitor audit.
4. **Pages:** match the cited page type and answer every follow-up. **Quotable format:** answer first under every heading, headings are the real questions, lists and small tables, each chunk self-contained; entities and one approved fact nobody else has (`longform-seo-article`).
5. **Entities and defense:** list the branded entities and approved brand-named frameworks. Keep facts identical on Wikidata, Grokipedia (never paid indexing), GBP, Bing Places, Yelp, Apple Maps, LinkedIn, Crunchbase, directories. Answer misinformation with an **official, specific FAQ/help center** first, then request corrections.
6. **Technical (recommend to Brennan):** SSR/prerendering (raw HTML is empty today); sitemap in **Bing Webmaster Tools**; **Organization** (with sameAs) and **Article** schema; never block search/index bots (GPTBot, ClaudeBot) in robots.txt; consider llms.txt; redirect hallucinated 404s.
7. **Mentions, three tiers:** Tier 1 editorial/listicles, expert quotes, and unlinked-mention reclaims (via `link-building`); Tier 2 genuine Reddit/Quora answers on cited threads (`reddit-comment`); Tier 3 own YouTube/LinkedIn. **Outreach is draft-only; Brennan approves every send. No paid placements for now (Brennan, Oct 14).**
8. **Experiment:** test vs. control question sets (e.g. 100/100), 2 weeks before/after with GW Analytics; reproduce before promoting a rule.
8b. **Semrush handoff:** log any backlink data seen in backlinks/semrush-sightings.md.
9. **Freshness:** refresh top and sleeper pages meaningfully; verify any citation on 3 different days.
10. **Measure (GW Analytics):** GEO = whether AIs name us for key questions over time (step 2); the GA4 "AI traffic" channel regex; training vs. citation bots in the logs; **lead → SQL → closed-won by channel**; and the "How did you hear about us?" field with AI options on /book-demo.

Skills to reference: `gw-lead-generation` (leading vs lagging, response time, conversion by UTM).
