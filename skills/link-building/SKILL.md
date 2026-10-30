---
name: link-building
description: >-
  Use for any Gorilla Works backlink or mention work: deciding if links are the
  bottleneck, free outreach, HARO/Qwoted/Featured quotes, unlinked mentions,
  lost/broken links, "best X" lists that AI cites, guest posts, competitor gaps,
  link bait, podcasts, local links, anchors, junk audits, Grokipedia. FREE
  tactics only. Use it whenever links or mentions come up, even if unnamed.
---
# Link building (GW Backlinks)
Detail: blueprints/backlinks.md. Apply `gw-content-rules`, `gw-claims-guardrails`, `ai-search-visibility`.

## Hard rules
- **No paid tactics** until Brennan says otherwise (Oct 14). Paid ideas go to the blueprint's parked list. Never PBNs, link swaps for ranking, image claiming, paid indexing, AI-written pitches.
- **OUTREACH FREEZE (Oct 19):** no sends from hello@ until Brennan re-authorizes. Draft only.
- **Authority floor (Oct 19):** guest posts and contributed articles only on sites with DA or Semrush Authority Score above 7.
- **Verify before any send:** `/home/box/bin/gw-verify-email ADDRESS --source-url <contact page>` must return PASS (exit 0). See backlinks/email-verify-before-send.md.
- Clean `https://gorillaworksmarketing.com/...` URLs plus UTMs per research/utm-link-strategy.md, logged in research/link-log.csv. Skip outlets that forbid link insertions. Competitors in plain text, never disparaged. Stats only with V/S IDs.

## Why
A link helps only if it points authority at a page that needs it, or puts our name on a page AI engines already cite. An unrelated homepage link does neither.

## Steps
1. **Pick target pages** (e.g. fencing money and blog pages) and confirm links are the gap: compare referring domains to the 3-5 pages that outrank ours. If they win with similar links, fix the page (`gw-longform-editor`), not the links. Add internal links from our strongest pages first.
2. **Prospects, in order:** unlinked mentions and lost links; partner, vendor, association, and client pages; pages AI cites for our target questions (`ai-search-visibility` tracker), especially "best X" lists naming competitors but not us; competitor link gap; resource pages; broken links; expert quotes; guest posts; link bait (stat hub, cost tools).
3. **Qualify:** relevance first (would a fence or home-service owner read it?), then real traffic and editorial standards, the DA>7 floor where it applies, a named owner of the page, and value to a target page. DA sorts; it never qualifies alone.
4. **Draft outreach** (blueprint templates, Brennan's voice): name their page and what you noticed, one ask, the exact URL, something real to offer, under 100 words. One follow-up about a week later, then stop.
5. **Expert quotes (HARO, Qwoted, Featured):** under 200 words: one-line credential, the point in 2 sentences, one specific example. Brennan writes or approves every quote.
6. **Anchors:** let the site choose; if asked, give the brand or page title. Never request exact-match. Ratios are an audit tool (blueprint).
7. **Log** prospects in backlinks/prospect-log.csv (DA/AS, AI-cited?, target page, status, verify result) and Semrush sightings in backlinks/semrush-sightings.md.

## Measure
New referring domains per target page, rankings for target queries, mentions on AI-cited pages (linked or not), outreach funnel, referral demos by UTM. Report by target page, not total count.

## Learning loop
Weekly (blueprint): skip anyone already contacted, report wins by page, log in its changelog.
