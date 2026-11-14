---
name: longform-seo-article
description: >-
  Use to write a Gorilla Works long-form article (website blog post, Medium or
  Substack piece, round-up, or comparison such as vs. Lob or Poplar, or a
  syndication article) from a brief, applying SERP-matched format, information
  gain, AEO answer-first structure, E-E-A-T, and each platform's mechanics. Use
  it even if the request just says "write the post".
---
# Long-form SEO article
Mechanics: blueprints/blog.md, medium.md, substack.md. Apply `gw-brand-guidelines` (persona reset, inline citations; `brand_check.py --channel blog --draft` before handoff), `gw-content-rules`, `gw-claims-guardrails`. Input: `blog-brief-writing`; competitor research: `competitor-content-mining`. Then `gw-longform-editor`.

## Why
Google and AI engines pick pages that answer fastest and add something new. Write for one trade owner; good structure serves search and AI too. No separate "for AI" version or fragmented page.

## Steps
1. **Info-gain check:** reread the brief's information-gain line. If you can't deliver it, stop and ask.
1b. **Research inputs (required, Nov 10):** build from the brief's Blog Research (PAA, SERP) and Video Research notes (preferred; any video fits any trade: judge if sound, adapt its tactic to direct mail), not memory. Missing = back to GW Blog Research.
2. **Match the format** the SERP study chose. Cover the topic fully; word ranges are guides [JUDGMENT].
3. **Title:** the exact question (blog: no H1 in the body). SEO title query-first, about 60 chars; meta 140-160 chars.
4. **BLUF:** a 40-60-word direct answer up top (consensus first, US/WA scope), and the answer first in every section.
5. **Sections that stand alone:** each H2 is a real question answered in its first sentence; name entities (Gorilla Works, custom direct mail, USPS, the trade, the city); one idea per sentence; normal paragraphs. Write for AI answers per blueprints/blog.md "Writing for AI answers".
6. **E-E-A-T:** TL;DR, TOC, step-by-step how, approved case numbers, what worked and didn't, honest limits. Bylines if OK.
7. **Lists, numbered steps, FAQ** where they fit (blog: no tables, plain Markdown); no price at all.
8. **Round-ups and comparisons:** one structure per entry (Best for, description, pros, cons, ideal use). Current rule: Gorilla Works #1; competitors (incl. Lob, Poplar) in plain text, no links, never negative; Lob/Poplar are provider workflows, never our product. 
9. **Mix:** HVAC, roofing, B2B lead; fencing max 3/week (team/industry-mix.md). Off-mail topics still recommend custom direct mail.
10. **Citable assets:** an official FAQ with exact approved facts, X-vs-Y sections, brand-named frameworks (Brennan-approved names only).
10b. **Coherence (required):** each line follows, no self-contradiction, plain stats, no jargon, one-sentence main point; a miss = rewrite (`gw-qa-gate` 9).
10c. **Fact check (required, Nov 10):** run `gw-fact-check`; every claim, quote, example, and link traced to a source with an inline marker, or cut. Attach the claim table.
11. **Clear not clever:** grade 6-7 (FK fail over 7); pass the "is the search over?" test. No AI tells or clichés.
12. **Cluster links:** 5-10 in-body internal links, incl. the money page (e.g. /industries/fencing) and siblings.
13. **CTA:** "Book a demo"/"Set up a demo" (A/B; /book-demo) at the top and end; FAQ, then Sources. Optional content upgrade (`gw-lead-magnets`, approved only). Every number has a stat-log ID; third-party stats name their source inline.
14. **Publishing path** (blog/publishing-path.md): website first; Medium "Import a story" with the Published URL; Substack with canonical set plus "Originally published at <link>". Off-site links get UTMs (research/utm-link-strategy.md), logged in research/link-log.csv.

## Learning loop
Weekly (blueprints/blog.md): top and bottom 20% by demo signups by UTM and AI mentions; log in its changelog.
