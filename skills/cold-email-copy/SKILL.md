---
name: cold-email-copy
description: >-
  Use whenever GW Email Copywriter writes a Gorilla Works cold email: the
  roofing landing-page email (personal page click), subject and preview,
  follow-ups, or objection replies (roofing first, then other trades). Built on
  Brennan's format spec, cold-email training and videos. Email only, no
  LinkedIn. Use it even if the request just says "write the emails for these
  leads".
---
# Cold email copy (GW Email Copywriter)
Spec, examples, pipeline: blueprints/cold-email.md. Apply `gw-brand-guidelines` (persona reset; pass `brand_check.py --channel cold-email` before handoff; cite in the claim table, not the copy), `gw-content-rules`, `gw-claims-guardrails`, `gw-fact-check`; hand drafts to `cold-email-editing`. Bots draft; Brennan sends.

## Goal (roofing, every lead)
One job: a click through to the personal landing page built for their company. No call booking, "reply yes", or offer dollar amounts. Brennan owns the Ember HTML; you write only the copy, never the greeting, "Inside your page" checklist, channel strip, signature, or footer/opt-out.

## Before writing
Brief from `cold-email-lead-research`, sourced hooks. **No hook, or Reviews says NO QUALIFYING REVIEW: hold the row and say why.**

## Where it goes
Notion **Email Copy** (Cold Leads – Roofing), plain text, one labeled line per slot, in order, spelled exactly:
Subject: / Preview: / Eyebrow: / Headline: / Review quote: / Review name: / Body paragraph 1: / Body paragraph 2: / Proof line: / CTA:

## Slot rules
1. **Subject:** short, with the company name ("Built a page for Titan Roofing"). No fake Re:, urgency, pitch words.
2. **Preview:** one line, under 90 characters. Default: "Your Google reviews, a sample mailer and the homes near your recent roofs."
3. **Eyebrow:** "<Review Count> Google reviews at <Rating, 1 decimal>", matching the row's properties.
4. **Headline:** 3-8 words, from a verified hook.
5. **Review quote:** only from a ★5 line in the row's **Reviews** field (Google Maps; usually the first), word for word. Cut only with "..."; never reword, fix typos, or merge. Max 20 words.
6. **Review name:** exactly as the source shows it.
7. **Body paragraph 1:** 25-40 words: one or two verified company details, then a line tying it to nearby homes needing the same work.
8. **Body paragraph 2:** the spec's fixed sentence; only the short company name changes.
9. **Proof line:** always exactly `Real Great Roofing: "$90,000 in leads from just one mail drop."` One client's result; no campaign details, no other stats.
10. **CTA:** `See my page -> ` + the row's Prospect Page URL, else `{{page_link}}`. Never invent or edit a URL; no google.com/url wrappers.

## Hard rules
- No price or cost wording ($0.78, "under $1", stamp comparisons, "$750 value", "$500 off"). Only dollar figure in our words: the proof line. Verbatim review quote exempt.
- Never: "thousands of other customers".
- No hashtags, em dashes, AI tells or clichés; grade 6-7.
- Draft only. Never set Status = Send or touch Ember send settings. Set Editing; no other workflow fields.
- Coherence check in template order. Attach the `gw-fact-check` claim table: count, rating, quote source (stars, date), each company fact, proof line.

## 1-day rule (Nov 13)
Ready for Summary rows are assigned, drafted, and edited within 1 day unless they fail (Claude/Replit 25 a day, Grok Bot the rest). Run reports list rows past 1 day and why. Grok Bot checks daily, fixes stalls with the step's owner.

## Follow-ups and replies
Roofing follow-ups and positive-reply text: PENDING Brennan (spec covers email 1). Replies are drafts; no auto-send until he approves. Other trades: legacy offer-arm flow (blueprint) until Brennan extends this.

## Learning loop
Weekly with GW Analytics (blueprints/cold-email.md loop): page clicks and positive replies by headline, hook, review choice; Editor fixes. Log in its changelog.
