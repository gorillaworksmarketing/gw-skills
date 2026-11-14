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
Spec, pipeline: blueprints/cold-email.md. Apply `gw-brand-guidelines` (persona reset; pass `brand_check.py --channel cold-email`; cite sources in the claim table), `gw-content-rules`, `gw-claims-guardrails`, `gw-fact-check`; hand drafts to `cold-email-editing`. Bots draft; Brennan sends.

## Goal (roofing, every lead)
One job: a click to the personal landing page built for their company. No call booking, "reply yes", or offer amounts. Brennan owns the Ember HTML; never write the greeting, checklist, channel strip, signature, or footer/opt-out.

## Before writing
Brief from `cold-email-lead-research`. **No hook, or NO QUALIFYING REVIEW: hold the row and say why.** DBs come from the guide's **12b registry**, never hardcoded IDs. Template gates are per industry: if 12b shows that industry's email template MISSING, hold only its rows at Ready for Summary and flag Brennan once; other industries run. Write only your own rows.

## Where it goes
**Email Copy**, plain text, one labeled line per slot, in order:
Subject: / Preview: / Eyebrow: / Headline: / Review quote: / Review name: / Body paragraph 1: / Body paragraph 2: / Proof line: / CTA:

## Slot rules
1. **Subject:** short, with the company name ("Built a page for <Company>"). No fake Re:, urgency, pitch words.
2. **Preview:** under 90 characters. Default: "Your Google reviews, a sample mailer and the homes near your recent roofs."
3. **Eyebrow:** "<Review Count> Google reviews at <Rating, 1 decimal>" from the row.
4. **Headline:** 3-8 words, from a verified hook.
5. **Review quote:** only from a ★5 **Reviews** line (Maps; usually the first), word for word. Cut only with "..."; never reword, fix typos, or merge. Max 20 words.
6. **Review name:** exactly as the source shows it.
7. **Body paragraph 1:** 25-40 words: verified company details, then nearby homes needing the same work.
8. **Body paragraph 2:** the spec's fixed sentence; only the short company name changes.
9. **Proof line:** exactly `Real Great Roofing: "$90,000 in leads from just one mail drop."` No details or other stats.
10. **CTA:** `See my page -> ` + the row's Prospect Page URL, else `{{page_link}}`. Never invent or edit it; no google.com/url wrappers.

## Hard rules
- No price or cost wording ($0.78, "under $1", stamp comparisons, "$750 value", "$500 off"); only the proof line has a dollar figure. Review quote exempt.
- Never: "thousands of other customers".
- No hashtags, em dashes, AI tells or clichés; grade 6-7.
- Draft only. Never set Status = Send or Ember send settings. Set Editing; no other workflow fields.
- Coherence check in template order. Attach the `gw-fact-check` table: count, rating, quote source (stars, date), each company fact, proof line.

## Failed rows and 1-day rule
**Failed check:** Status Failed, Bad match, or Drop; Hunter invalid or no usable verified email; editor HOLD or QA FAIL; NO QUALIFYING REVIEW with no listing match. Never draft, backfill, or advance it; report it as failed, with the reason. Other rows: drafted and edited within 1 day (Claude/Replit 25 a day, Grok Bot the rest). Reports list stalled rows and why; Grok Bot fixes stalls with the owner.

## Follow-ups and replies
Roofing follow-ups, reply text: PENDING Brennan. Replies are drafts; no auto-send until he approves. Fencing: legacy flow (blueprint).

## Learning loop
Weekly with GW Analytics: clicks and positive replies by headline, hook, review; Editor fixes. Log in the blueprint.
