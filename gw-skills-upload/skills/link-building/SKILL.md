---
name: link-building
description: >-
  Use for any Gorilla Works backlink or mention work: free outreach, digital PR,
  HARO/Qwoted/Featured/Source of Sources quotes, unlinked mentions, lost/broken
  links, guest posts, competitor gaps, link bait, podcasts, image credits, local
  links, junk audits, Grokipedia. FREE tactics only for now. Use it whenever
  links or mentions come up, even if unnamed.
---
# Link building (GW Backlinks)
Detail: blueprints/backlinks.md. Apply `gw-content-rules`, `gw-claims-guardrails`, `ai-search-visibility`.

## Hard rules
- **No paid backlink tactics until Brennan says otherwise (Oct 14, 2026).** Paid ideas go only to the blueprint's "Later / paid (parked)" list.
- **OUTREACH FREEZE (Oct 19, 2026):** No auto-sends from hello@ until Brennan explicitly re-authorizes. Draft only.
- **Authority floor (Oct 19, 2026):** Guest posts / contributed articles only on sites with **domain authority (or Semrush Authority Score) above 7**. Skip DA ≤7 (e.g. electriciantimes.com DA 3 — skipped). Prefer meaningfully higher when choosing between options. Check Semrush (or Moz/Ahrefs if available) before adding to the pitch queue.
- **Never:** paid links, PBNs, black-hat image claiming, paid indexing.
- Name competitors in plain text, never disparaged. No invented stats (V/S IDs only).
- Every site link follows research/utm-link-strategy.md and is logged in research/link-log.csv.

### Email verify before every send (owner Oct 19, 2026 — critical)
Undeliverables destroy hello@ deliverability. **Do not send** unless `gw-verify-email` returns **PASS**.

```bash
/home/box/bin/gw-verify-email ADDRESS --source-url https://publication.com/contact
# Exit 0 = PASS, 1 = FAIL, 2 = INCONCLUSIVE (draft only)
```

Checks: syntax, dead-list (`backlinks/dead-emails.csv`), MX via DoH, optional on-page, **Hunter mailbox verifier required for PASS**. Published-on-page alone is not enough.

### Clean destination URLs only
Never `google.com/url?q=...` wrappers. Always `https://gorillaworksmarketing.com/...` + UTMs.

### Link insertions required
Skip outlets that forbid link insertions (MarketingProfs = skip).

## A good link
Relevant, indexed, clicked, in body copy, descriptive anchor. Relevance still beats vanity DA, but never below the DA>7 floor for guest/contrib.

## Steps
1. Foundation citations/profiles (free only).
2. Relationships + value-first engagement before asks.
3. Unlinked mentions, lost links, partners.
4. Vet prospect: traffic, index, topical fit, **DA/AS >7**, link-insertion OK, then `gw-verify-email` before any send.
5. Competitor gap / link bait / pitches / expert quotes / podcasts / images / junk audit.
6. Log every prospect in backlinks/prospect-log.csv (DA/AS, verify status, bounce history).

See also: `backlinks/email-verify-before-send.md`, `backlinks/OUTREACH-FREEZE.md`, `backlinks/deliverability-rules-2026-10-19.md`.
