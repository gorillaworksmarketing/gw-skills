---
name: gw-google-places-budget
description: >-
  HARD REQUIREMENT for every Gorilla Works lead lookup (discovery, review count,
  rating, reviews, address, Place ID): use up the free Google Places allowance
  (via Ember) before any browser or signed-out Maps scrape, every month, without
  ever going over, and capture the same full field set whichever path is used.
---
# Google Places budget: allowance first, browser second (HARD REQUIREMENT)

Brennan's rule (Nov 13, 2026): **every month we must use all of the free Google Places allowance before we use the browser.** This is not optional. A run that uses the browser while free Places lookups are still left has failed this rule.

## Same full record on every path (HARD REQUIREMENT, Brennan Nov 13, 2026, 4:44 PM PT)
No matter where or how the data comes in (Ember Places, signed-out browser, or both), every company ends up with the same complete record. That record is everything we can get:
- Business name, Google Place ID, Maps listing URL, full address, city and state, service-area flag
- Phone number and website
- Rating and live review count
- Reviews: the 5 most recent (up to 10 when needed) read in full, with the chosen 5-star line(s) written in the standard format with screenshot proof
- Description (the Google editorial summary or the business's own Maps description), primary category and other categories
- Hours, business status (operational or closed), price level, photo count, and attributes when Maps shows them
- From the company's own website: every published email, extracted text, and business LinkedIn and Facebook page links

If one path doesn't return a field (Places search won't return emails, and may leave out the description or more than 5 reviews), fill it from the other path or from the website step. A row isn't complete until every field above is filled or marked as not available on Maps or the site. The output format and Notion fields stay identical whichever path is used. Never overwrite a filled field with a blank.

## Source of truth
- Google Places access runs through Ember's Google Maps Places integration (`EMBER_API_KEY`; base `https://ember-email.replit.app/api/marketing`). Never print the key.
- `GET /places/status` is free. It returns `freeLimit`, `freeUsed`, `freeRemaining`, the window, `requestsToday` and `perMinuteLimit`. Read it at the start of every run and before each batch. Ember's window (rolling, about 32 days) is the binding limit, not the calendar month.
- Keep a local ledger of every billed call (date, endpoint, result) and reconcile it with `/places/status`. When they disagree, trust `/places/status`.

## Order of lookups
1. **Places first.** While `freeRemaining > 0`, do every lookup with `POST /places/search`. One page of up to 20 businesses costs 1 credit, and it returns placeId, address, rating, userRatingCount, up to 5 reviews, website and phone. Use `GET /places/{placeId}` only when it adds fields search didn't return and credits allow it.
2. Get the most out of each credit. Use queries that return full pages of qualifying businesses (the trade plus city, more than 30 reviews), and don't search an area that's already been searched.
3. **Browser second.** Switch to the signed-out Google Maps scrape only when `freeRemaining` is 0, or when Ember Places is down or unauthorized. When that happens, log the reason.
4. Still use the browser where Places can't do the job, such as review screenshots, fields Places didn't return, or reading reviews beyond the 5 that search returns. Doing that is not a fallback and doesn't break the rule.

## Never go over
- Before each billed call, check that it fits in `freeRemaining`. Never make a call that would go past the free limit. Respect `perMinuteLimit`.
- Never retry a failed or timed-out Places call, because a failure still uses a credit.
- If usage ever goes over the free limit, tell Brennan right away with usage vs. limit, and stop billed calls.

## Use it all before it resets
- Each run, work out how many credits are left and how many days remain before the window resets. Spread them evenly so the allowance is fully used by reset.
- With 2 days left before reset, if credits remain, raise that day's lookup target so every remaining credit is used over those last 2 days. Leave none behind, and stay under the limit.

## Report
- Every run logs credits used and credits remaining, plus how many lookups went to the browser and why.
- The weekly tally includes Places usage vs. the free limit.
