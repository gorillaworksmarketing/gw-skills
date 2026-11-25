# Blueprint: Google Places budget (skill `gw-google-places-budget`)

Detail moved out of the skill on Nov 13 2026 so the skill fits 3,500 characters. Rules are unchanged; nothing was dropped.

## Brennan's rules (verbatim sense)
- Nov 13 2026: every month, use all of the free Google Places allowance before using the browser. A run that uses the browser while free Places lookups are left has failed the rule.
- Nov 13 2026, 4:44 PM PT: the same full record on every path (Ember Places, signed-out browser, or both). The field list stays in the skill.

## Moved detail
- `GET /places/status` (free) returns `freeLimit`, `freeUsed`, `freeRemaining`, the window, `requestsToday` and `perMinuteLimit`.
- `POST /places/search`: one page of up to 20 businesses costs 1 credit and returns placeId, address, rating, userRatingCount, up to 5 reviews, website and phone. `GET /places/{placeId}` only when it adds fields that search didn't return and credits allow.
- Browser use that is NOT a fallback (does not break the rule): review screenshots, fields Places didn't return, reading reviews beyond the 5 that search returns.
- Local ledger: every billed call with date, endpoint and result; when it disagrees with `/places/status`, trust `/places/status`.
- Reports: every run logs credits used and remaining, plus how many lookups went to the browser and why; the weekly tally includes Places usage vs. the free limit.

## Ember issue fixes (relayed by Grok Bot (Brennan 5:02 PM PT), guide v3.22 section 0)
- G21 retries: guide 0.12 lets reads retry (429 Retry-After; 409/5xx up to 3) and requires writes and paid/provider calls to be logged, read back and repeated only if the read proves they did not apply. **Brennan's stricter rule wins for Places:** never retry a failed or timed-out Places call, because a failure still uses a credit. Log it and read back `/places/status` and the ledger. Only the free `/places/status` read may retry.
- G06 provenance: never invent a value and never pay for enrichment. Brennan's full-record rule still applies: fill every field the free paths give, mark the rest not available.

## Weekly learning loop
Each week, log which query shapes returned the most qualifying businesses (30 or more reviews, >= 30) per credit and how many lookups needed the browser, and update the query guidance here.

## Snapshot (Nov 24, 2026, 2:50 PM America/Phoenix)
`freeLimit` 800, `freeUsed` 800, `freeRemaining` 0, rolling window about 32 days, `perMinuteLimit` 10, 26 requests already that day at 2:50 PM. Exact reset date is **unverified** (briefing: about Nov 30). Live `/places/status` wins over this snapshot. Until the window resets, GW Lead Research scrapes Maps with the signed-out browser and still requires 30 or more reviews (>= 30; fail only 29 or fewer) and the same full field set. While discovery is on the browser path, Lead Research has first priority on the shared computer (API calls from other bots are fine; extra browser windows are not).

## Changelog
- 2026-11-25 ~3:41 PM America/Phoenix: qualifying review count settled (Brennan, Nov 25) to 30 or more (>= 30), including exactly 30; fail only 29 or fewer. Replaced the weekly-loop "31+ reviews" wording (that would have excluded a listing with exactly 30) and the snapshot's "30+ reviews". Do not ask Brennan about this again.
- 2026-11-24 (Brennan all-hands Part A / Part B): recorded the re-audit Places snapshot above (allowance exhausted; browser scrape until reset; Lead Research first priority on the shared computer while on the browser path). Live `/places/status` wins. Skill unchanged: still read status first and use Ember while `freeRemaining > 0`.
- 2026-11-13 5:30 PM PT (Ember issue fixes, relayed by Grok Bot (Brennan 5:02 PM PT)): G21 retry line added (Places keeps never-retry); G06 no-invent/no-paid-enrichment note; skill trimmed from 4,131 to under 3,500 characters with the detail above moved here; weekly learning loop added.
