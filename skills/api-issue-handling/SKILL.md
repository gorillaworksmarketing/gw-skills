---
name: api-issue-handling
description: >-
  Use on any API access issue for any Gorilla Works API (Notion, Ember, Hunter,
  RGR Finance, Semrush, Google Places, X, and others): classify it, handle it
  safely, and either fix it or report it to Brennan. Never leave one silent.
---
# API issue handling (all bots)

Brennan's rule (2026-11-24, America/Phoenix): every API access issue on any API must be reported to Brennan or handled with a documented fix captured in the skills. Never leave one silent. How to call each API, where keys live, and per-API don'ts: `api-access-guide`.

## 1. Classify
- **Auth:** 401 or 403.
- **Rate limit:** 429.
- **Quota or allowance:** exhausted credits, "allowance unavailable," or a cap reached.
- **Timeout or connection:** timeouts, connection reset, incomplete response.
- **4xx bad input:** 400, 404, 409 (other than a documented conflict you already handle), or a validation error.
- **5xx server:** 500–504 or an upstream outage.

## 2. Safe handling
- **Retry with backoff** on 429 (wait `Retry-After`), 5xx, and timeouts — only when the call is safe to repeat: a free read, or a write that has an Idempotency-Key or that you have re-read and confirmed did not already land.
- **Never retry a write blindly.** Re-read first. Many APIs (including Notion) have no Idempotency-Key; a second PATCH can duplicate or overwrite.
- **Never retry a paid call** that may already have been charged (Google Places lookups; Hunter verify or search). A failed Places call still uses a credit (`gw-google-places-budget`). Never re-run Hunter to recover a missed Notion save (`hunter-notion-save-recovery`).
- **Never rotate or revoke keys.** Never print or log API keys.
- **No credit purchases.** If allowance is exhausted, stop and escalate; do not buy credits.

## 3. Escalate to Brennan
When auth fails; quota or allowance is exhausted; you find a bug in his apps (Ember, the finance app, and others); or data is lost or held (a paid result not saved, a held job, a missing receipt). Include the API, the error class, times in America/Phoenix, and what you already tried.

## 4. After a fix
Send the cause and the fix to GW Skill Builder so the relevant skill (and blueprint, if needed) is updated. A one-off script is not the lasting record.

## 5. Log the incident with times
Record when it started and ended (America/Phoenix), the endpoint, the status or error code, and the outcome. Do not log secrets or real prospect emails in public files.

## Worked example (2026-11-24)
Eight Ember Hunter jobs were paid for, then held without a Notion save (429, connection reset, and Notion allowance unavailable). Three failures around 2:47–2:48 PM America/Phoenix overlapped other bots' Notion queries and bulk row writes on the shared integration. Ember's `POST /api/marketing/hunter/workflow/jobs/{id}/reconcile` returned 409 `HUNTER_NO_WRITE_RECEIPT`, so it could not recover them. Grok Bot saved the already-paid results. Lasting fixes: `notion-shared-rate-limit` and `hunter-notion-save-recovery`. Requested Ember product fix (blueprints/cold-email.md): retry its own Notion save with backoff on 429 or connection errors instead of holding the job.

## Worked example (2026-11-25): Reddit and box web search
Public Reddit JSON from this box returns 403; RSS 404 or 429 (unsigned datacenter IP block, not auth — do not rotate keys). Current fix: cited web-search candidates; store the thread URL and quote in Owner Evidence (`/workspace/reddit-leads/README.md`). The box cannot do its own web search (DuckDuckGo captcha, Bing junk); website discovery needs an agent with web search. Official Reddit API pending Brennan's approval, not approved. Detail: blueprints/api-access-guide.md.
