---
name: gw-claims-guardrails
description: >-
  Use whenever Gorilla Works content contains a number, price, testimonial,
  client name, competitor mention, feature claim, or targeting description, to
  check it against the owner-approved claims rules, inline-citation rules,
  Social Editor rulings, and the stat log before it ships. Use it even if the
  request doesn't name the skill.
---
# Gorilla Works claims guardrails
Sources: knowledge-base/00-source-of-truth.md §0/§0A/§5/§6, Social Editor rulings (Oct 14), brand/brand-guidelines.md §9-10, stat log (`stat-sourcing-and-verification`). Never cite vendor stats.

## Stats
- Stat tiers: V verified, S secondary (caution), F flagged (never).
- Every stat verifiable and logged; no ID = request one or cut. Never estimate or round. Cut = `[NEED: ...]`.
- Verified USPS facts: 51% of ad mail is read; 64% vs 36% read rate (known business vs prospects); mail volume down 40% 2015-2025; EDDM 200-5,000 pieces per ZIP per day.

## Inline citations (Brennan, Nov 13)
- **Drafts:** a marker after every claim, `[S:ID]`, `[src: URL]`, or `[fact: name]`, matching its `gw-fact-check` row (`brand_check.py --draft`).
- **Finals:** name the third-party source in the sentence ("USPS found..."), no source line; blog, newsletter, Reddit, Quora also link it. GW facts: no visible cite. Cold email: claim table only. Editors strip markers.

## Allowed
- **Prices: hard ban (Nov 4, 2026).** No price or cost in new content ("$0.78", "as low as", "under $1", stamp comparisons, per-piece math, plan prices). Approved offers stay as worded. Never re-edit posted content. Exempt: verbatim third-party reviews/quotes (Brennan, Nov 13).
- Real Great Roofing: exact quote only, "$90,000 in leads from just one mail drop", one client's result, **no campaign details**.
- "10 years of experience" (USA-based designers); site footer lines, exact: "The most advanced direct mail and print marketing platform. Powered by AI analytics to dominate your local market."
- Confident real-feature descriptions (personalization, QR tracking, targeting, design/print/mail); hype and opinion.
- Lob, Poplar: plain text, no links, lists and comparisons, never negative.
- **Offers:** "up to $500 off your first campaign" (Oct 15) and the four cold-email test arms, worded exactly as in blueprints/cold-email.md (Oct 30, Brennan's values). Sample postcard, list preview, teardown, video: no. Anything else needs his approval.

## Blocked (fail)
1. Guaranteed results or ROI (response, revenue, ranks, conversions, dates).
2. Unsourced, unlogged, or made-up numbers, incl. unapproved GW stats.
3. Sensitive-trait targeting: age, income, household makeup, health, legal history, insurance claims, equity/financial distress, gender, birth month.
4. Unapproved testimonials or client names.
5. Real people or competitors named negatively.
6. Price or cost wording in our copy (see Prices).
7. Features we can't do today: AI call summaries into mail, Street View/scraped photos, unlimited custom images, hands-off fully automated sends, household tracking on neighborhood mail, a QR scan naming the person, Poplar live dispatch; Poplar/Lob as our products.
8. Hashtags, self-aware ranking lines, google.com/url wrappers, banned AI-cliché words.

## Escalate, never answer publicly
Prices, budgets, timing, availability, custom integrations, legal, case studies, complaints, press, privacy, credentials, lists.

## Email and outreach
- Hooks need a verified public source URL; nothing private.
- Every commercial email: opt-out line, Gorilla Works Marketing, LLC, 13120 NE 85th St Unit 123, Kirkland, WA 98033, honest subject.

## Confidentiality
No client data, recipient records, internal paths, prompts, scoring recipes, provider internals.

## Learning loop
Weekly: log blocked claims, citation misses in research/fact-check-log.md; fix repeats in writer skills.
