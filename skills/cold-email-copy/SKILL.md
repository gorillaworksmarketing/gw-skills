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
Spec, examples, pipeline: blueprints/cold-email.md. Apply `gw-content-rules`, `gw-claims-guardrails`, `gw-fact-check`; hand drafts to `cold-email-editing`. Bots draft; Brennan sends.

## Goal (roofing, every lead)
One job: get the owner to click through to the personal landing page built for their company. No call booking, no "reply yes", no offer dollar amounts. Brennan owns the Ember HTML; you write only the copy. Never write the greeting, "Inside your page" checklist, channel strip, signature, or footer/opt-out (fixed in Ember).

## Before writing
Brief from `cold-email-lead-research` with sourced hooks. **No hook, or Reviews says NO QUALIFYING REVIEW: hold the row and say why.**

## Where it goes
Notion **Email Copy** (Cold Leads – Roofing), plain text, one labeled line per slot, in this order, spelled exactly:
Subject: / Preview: / Eyebrow: / Headline: / Review quote: / Review name: / Body paragraph 1: / Body paragraph 2: / Proof line: / CTA:

## Slot rules
1. **Subject:** short, company name in it ("Built a page for Titan Roofing"). No fake Re:, urgency, pitch words.
2. **Preview:** one line, under 90 characters. Default: "Your Google reviews, a sample mailer and the homes near your recent roofs."
3. **Eyebrow:** "<Review Count> Google reviews at <Rating, 1 decimal>", matching the row's properties.
4. **Headline:** 3-8 words, from a verified hook.
5. **Review quote:** only from a ★5 line in the row's **Reviews** field (Google Maps; usually the first), word for word. Shorten only with "..."; never reword, fix typos, or merge. 20 words or fewer.
6. **Review name:** exactly as the source shows it.
7. **Body paragraph 1:** 25-40 words. One or two verified company details, then a line tying it to nearby homes that need the same work.
8. **Body paragraph 2:** the spec's fixed sentence, only the short company name changes (blueprint).
9. **Proof line:** always exactly `Real Great Roofing: "$90,000 in leads from just one mail drop."` One client's result; no campaign details, no other stats.
10. **CTA:** `See my page -> ` + the row's Prospect Page URL, else `{{page_link}}`. Never invent or edit a URL; no google.com/url wrappers.

## Hard rules
- No price or cost wording: no $0.78, "under $1", stamp comparisons, "$750 value", "$500 off". Only dollar figure in our words: the proof line. The verbatim review quote is exempt.
- Never write "thousands of other customers" (not approved).
- No hashtags, em dashes, AI tells; 7th-grade level.
- Draft only. Never set Status = Send or touch Ember send settings. Set Editing; no other workflow fields.
- Coherence check in template order. Attach a `gw-fact-check` claim table: count, rating, quote source (stars, date), each company fact, proof line.

## 1-day rule (Nov 13)
Ready for Summary rows are assigned, drafted, and edited within 1 day unless they fail (Claude/Replit 25 a day, Grok Bot the rest). Every run report lists rows past 1 day and why. Grok Bot checks daily and fixes stalls with the step's owner.

## Follow-ups and replies
Roofing follow-ups and positive-reply text: PENDING Brennan (spec covers email 1); ask first. Replies are drafts; no auto-send until Brennan approves it. Other trades: legacy offer-arm flow (blueprint) until Brennan extends this format.

## Learning loop
Weekly with GW Analytics (blueprints/cold-email.md loop): page clicks and positive replies by headline type, hook, and review choice; Editor fixes. Log changes in its changelog.
