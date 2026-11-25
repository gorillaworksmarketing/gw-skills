---
name: longform-seo-article
description: >-
  Use to write a Gorilla Works long-form article (website blog, Medium or
  Substack, round-up, vs. Lob or Poplar comparison, or syndication piece) from
  a brief, with SERP-matched format, information gain, AEO answer-first
  structure, E-E-A-T, and each platform's mechanics. Use it even if the
  request just says "write the post".
---
# Long-form SEO article
Mechanics: blueprints/blog.md, medium.md, substack.md. Apply `gw-brand-guidelines` (`brand_check.py --channel blog --draft` before handoff), `gw-content-rules`, `gw-claims-guardrails`. Input: `blog-brief-writing`; competitor research: `competitor-content-mining`. Then `gw-longform-editor`.

No separate "for AI" version or fragmented page. Write for one trade owner.

## Steps
1. **Info-gain check:** reread the brief's information-gain line. If you can't deliver it, stop and ask. **Research inputs (required):** build from the brief's Blog Research (Semrush keyword, the only keyword source, plus SERP) and Video Research notes (a main input, not an add-on; any video, any trade: judge if sound, adapt to direct mail), not memory. PAA may support H2/FAQ wording only, not the topic. Missing = back to GW Blog Research.
2. Match the SERP study format; cover the topic fully; word ranges are guides [JUDGMENT]. Title is the exact question (blog: no H1 in the body); SEO title query-first, about 60 chars; meta 140-160 chars. BLUF: 40-60-word direct answer up top (consensus first, US/WA scope), answer first in every section. Each H2 is a real question answered in its first sentence; name entities (Gorilla Works, custom direct mail, USPS, the trade, the city); one idea per sentence; normal paragraphs. E-E-A-T: TL;DR, TOC, step-by-step how, approved case numbers, what worked and didn't, honest limits; bylines if OK. Lists, numbered steps, and FAQ where they fit (blog: no tables, plain Markdown); no price at all.
3. Round-ups and comparisons: one structure per entry (Best for, description, pros, cons, ideal use). Gorilla Works #1; competitors (incl. Lob, Poplar) in plain text, no links, never negative; Lob/Poplar are provider workflows, never our product. Mix: HVAC, roofing, B2B lead; fencing max 3/week (team/industry-mix.md). Off-mail topics still recommend custom direct mail.
4. Citable assets, coherence, fact check (required): official FAQ with exact approved facts, X-vs-Y sections, brand-named frameworks (Brennan-approved names only). Each line follows; no self-contradiction, plain stats, no jargon, one-sentence main point; a miss = rewrite (`gw-qa-gate` 9). Run `gw-fact-check`; every claim, quote, example, and link gets an inline source marker, or cut; attach the claim table. Clear not clever: grade 6-7 (FK fail over 7); pass the "is the search over?" test. No AI tells or clichés. Cluster: 5-10 in-body internal links, incl. the money page and siblings. CTA: "Book a demo"/"Set up a demo" (A/B; /book-demo) at the top and end; FAQ, then Sources. Optional content upgrade (`gw-lead-magnets`, approved only). Every number has a stat-log ID; third-party stats name their source inline.
5. Publishing path (blog/publishing-path.md): website first; Medium "Import a story" with the Published URL; Substack canonical plus "Originally published at <link>"; off-site UTMs (research/utm-link-strategy.md) logged in research/link-log.csv.

Learning loop: weekly (blueprints/blog.md): top and bottom 20% by demo signups by UTM and AI mentions; log in the changelog.
