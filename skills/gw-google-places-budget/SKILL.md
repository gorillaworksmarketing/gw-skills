---
name: gw-google-places-budget
description: >-
  HARD REQUIREMENT for every Gorilla Works lead lookup (discovery, review count,
  rating, reviews, address, Place ID): use up the free Google Places allowance
  (via Ember) before any browser or signed-out Maps scrape, every month, without
  ever going over, and capture the same full field set whichever path is used.
---
# Google Places budget: allowance first, browser second (HARD REQUIREMENT)
Brennan's rule (Nov 13, 2026): **every month we must use all of the free Google Places allowance before we use the browser.** Not optional: using the browser while free Places lookups remain fails this rule. Detail and examples: blueprints/google-places-budget.md.

## Same full record on every path (HARD REQUIREMENT, Brennan Nov 13, 2026, 4:44 PM PT)
Every path (Ember Places, signed-out browser, or both) gives the same complete record, everything we can get:
- Business name, Google Place ID, Maps listing URL, full address, city and state, service-area flag
- Phone and website; rating and live review count
- Reviews: the 5 most recent (up to 10 when needed) read in full, chosen 5-star line(s) in the standard format with screenshot proof
- Description (Google editorial summary or the business's Maps description), primary and other categories
- Hours, business status, price level, photo count, attributes when Maps shows them
- From the company's own website: every published email, extracted text, business LinkedIn and Facebook links

If a path misses a field (Places search returns no emails and may skip the description or reviews past 5), fill it from the other path or the website. A row is complete only when every field is filled or marked not available on Maps or the site. Same output and Notion fields on every path. Never overwrite a filled field with a blank. Never invent a value or pay for enrichment (guide v3.22 0.5).

## Source of truth
- Places runs through Ember's Google Maps Places integration (`EMBER_API_KEY`; base `https://ember-email.replit.app/api/marketing`). Never print the key.
- `GET /places/status` is free (fields: blueprint). Read it at the start of every run and before each batch. Ember's window (rolling, about 32 days) is the binding limit, not the calendar month.
- Keep a ledger of every billed call (date, endpoint, result); reconcile with `/places/status`, which wins.

## Order of lookups
1. **Places first.** While `freeRemaining > 0`, use `POST /places/search` (one page of up to 20 businesses = 1 credit; fields: blueprint). `GET /places/{placeId}` only when it adds fields and credits allow.
2. Max value per credit: full pages of qualifying businesses (trade plus city, more than 30 reviews); never re-search an area.
3. **Browser second:** signed-out Maps scrape only when `freeRemaining` is 0 or Ember Places is down or unauthorized; log the reason.
4. Browser use where Places can't do the job (review screenshots, missing fields, reviews past 5) is not a fallback.

## Never go over
- Before each billed call, check it fits in `freeRemaining`; never go past the free limit; respect `perMinuteLimit`.
- Never retry a failed or timed-out Places call (a failure still uses a credit): log it, read back `/places/status` and the ledger. Only free reads (`/places/status`) may retry (429 Retry-After; 409/5xx up to 3).
- Over the free limit: tell Brennan right away (usage vs. limit) and stop billed calls.

## Use it all before it resets
Each run, work out credits left and days to reset; spread them evenly so the allowance is used by reset. With 2 days left, raise the daily target so every remaining credit is used, staying under the limit.

## Report and learning loop
Every run logs credits used and remaining, plus browser lookups and why. The weekly tally shows Places usage vs. the free limit; log what worked in the blueprint.
