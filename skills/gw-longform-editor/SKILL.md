---
name: gw-longform-editor
description: >-
  Use when editing a Gorilla Works long-form draft or framework (blog, Medium,
  Substack) into the final publish-ready version, or refreshing a page that
  already ranks: AEO direct answer, stronger hook, Seven Sweeps, AI-tell
  removal, demo CTA, verified links and stats, and the QA gate. The GW Blog
  Editor's core skill. Use it even if the request just says "edit this post".
---
# GW long-form editor
Inputs: draft, brief, platform blueprint. Apply `gw-content-rules`, `gw-claims-guardrails`, then `gw-qa-gate`. Examples: blog/drafts/2026-10-15/.

## First, diagnose
Save the incoming draft as `<name>.orig.md`. Run the coherence check (12b) first; a miss means (A). Then decide: (A) generic or AI-sounding, so rebuild from the brief; (B) real voice with problems, so edit line by line; (C) a point fix, so touch only that. If a sentence is specific, true, and sounds like Brennan, leave it alone.

## Steps
1. **AEO up top:** a 40-60-word answer, consensus first, US/state scope; each H2 question answered in its first 40-60 words.
2. **Hook:** 3 headline variants (the blog title stays the exact question); sharpen the first 2 sentences.
3. **Seven Sweeps,** one pass each: clarity; voice (Brennan, plain); so what (every section tied to a fence or roofing owner's leads); prove it (claims backed or cut); specificity (could a competitor publish this line? then sharpen it); emotion (their real pain, no drama); zero risk (the CTA feels easy).
4. **AI-tell sweep** (team/editor-brief.md, `gw-content-rules`): em dashes; "delve/landscape/unlock/elevate"; contrast reveals; negation lists; colon reveals; self-answered questions; threes padding; generic openers and tidy closers; wisdom-shaped lines; uniform rhythm; summary lines ending every section.
5. **Craft:** cut adverbs and filler, one reader, 2-3 sentence paragraphs, no keyword stuffing.
6. **Info gain and research:** confirm the brief's information-gain line and its research (Blog Research PAA/SERP, Video Research notes) made it in; missing = back to the writer; check against the top results; run the "search over" test.
7. **Demo CTA:** "Book a free demo" (gorillaworksmarketing.com/book-demo) near the top and at the end.
8. **Links:** open every internal link (trailing-slash URL). Off-site links get UTMs per research/utm-link-strategy.md, logged in research/link-log.csv. 5-10 in-body internal links.
9b. **Fact check (required, Nov 10):** rerun `gw-fact-check` step 4 yourself; every claim, quote, example, and link traced to a real source, or cut.
9. **Stats:** each number matches a V/S stat-log ID or approved fact; no per-mailer price at all ($0.78, under $1, stamp comparison); claims that can't be backed get `[NEED: ...]` or are cut.
10. **Length:** cover the topic fully; never pad [JUDGMENT; Brennan to confirm vs. the old target].
11. **Structure:** answer-first sections that stand alone, TL;DR, TOC, ✅ checklists, FAQ, Sources; platform format (blog: no images or HTML). About a 5th-grade reading level; AI-answer writing per blueprints/blog.md. A human edit is required.
12. **Refresh edits:** for a page that ranks, add the missing section and update stale facts; keep what works; no date-only changes. Record position and CTR, then wait 3-4 weeks.
12b. **Coherence (required):** read it as the target owner: each line follows from the last, never contradicts itself, stats in plain words, no jargon, main point fits one sentence. A miss = rewrite, not polish (`gw-qa-gate` 9).
13. **Score** 1-10 as a fence owner, an SEO reviewer, and Brennan; ship at 7+ each and 8+ average.
14. **Publishing path** (blog/publishing-path.md) as in `longform-seo-article`.
15. **Output:** final file, change log (word count, link check, scores), and the `gw-qa-gate` result.

## Learning loop
Weekly (blueprints/blog.md): log repeat fixes so briefs and drafts improve.
