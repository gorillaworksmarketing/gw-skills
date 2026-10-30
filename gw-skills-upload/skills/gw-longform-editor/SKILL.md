---
name: gw-longform-editor
description: Use when editing a Gorilla Works long-form draft or framework (blog, Medium, Substack) into the final publish-ready version, with AEO direct answer, stronger hook, humanized prose, demo CTA, verified links and stats, target word count, and the QA gate. This is the GW Blog Editor's core skill (blog-edit-qa). Use it even if the request doesn't name the skill.
---
# GW long-form editor
Inputs: the draft plus its brief and platform blueprint. Apply `gw-content-rules` and `gw-claims-guardrails`, then `gw-qa-gate`. Examples: blog/drafts/2026-10-15/.

## Steps
1. **Keep the original:** save the incoming draft as `<name>.orig.md` before editing.
2. **AEO direct answer up top:** a 40-60-word answer, consensus first, US/state scope; each H2 question answered in its first 40-60 words.
3. **Stronger hook:** 3 headline variants, pick the best (the blog title stays the exact question; no H1 in the body), then sharpen the first 2 sentences.
4. **AI-pattern sweep** (team/editor-brief.md): em-dashes, "delve/landscape/unlock/elevate", rule-of-three padding, "not X but Y", generic openers and closers, hedging, uniform rhythm, filler, summary lines closing every section.
5. **Craft:** cut adverbs, show don't tell, one reader, 2-3 sentence paragraphs, no keyword stuffing or repetition.
6. **Demo CTA:** "Book a free demo" linking gorillaworksmarketing.com/book-demo near the top and at the end. Off-site pieces (Medium/Substack in-body links) get UTMs; blog internal links stay clean.
7. **Links (required):** verify every internal link resolves (open it; use the trailing-slash URL to avoid 301 hops). Build any UTM link per research/utm-link-strategy.md (utm_source=<platform>, utm_campaign=<industry>_<type> (e.g. fencing_faq), utm_term=<article slug>, lowercase; see the UPDATE section) and log every link in research/link-log.csv.
8. **No unverified stats:** each number matches a V/S stat-log ID or an approved fact; prices only "as low as $0.78" / "under $1"; cut the rest.
9. **Length:** cover the topic completely; treat the brief's range as a guide, never pad (per Ahrefs, most cited pages are under 1,000 words, S-AHR8) [JUDGMENT; Brennan to confirm vs. the old target].
9b. **AEO structure:** BLUF in every section; atomic, standalone H2s; entity-rich, simple declarative sentences; TL;DR and TOC; lists/comparisons where they fit.
9b2. **Checks:** information gain vs. the top results; the "search over" test; 5-10 in-body internal links; about a 5th-grade reading level. A human edit is required; no fully automated AI content.
9c. **Freshness:** sleeper or top pages get meaningful updates, not date changes; flag posts older than 30 days in the top set for a refresh request.
10. **Structure:** clear H2/H3s, ✅ checklists, FAQ, Sources; platform format (the blog has no images or HTML).
10b. **Publishing path** (blog/publishing-path.md): website first; Medium via "Import a story" with the Published URL (sets the canonical); Substack repost with the canonical URL set to the Published URL plus "Originally published at <link>". Only after the Published URL exists; in-body links get UTMs; log every URL in research/link-log.csv.
11. **Output:** the final file, a short change log (including word count and link check results), and the `gw-qa-gate` result.

Skills to reference: `gw-lead-generation` (clear not clever, one CTA, reading-level check, front-loaded hook).
