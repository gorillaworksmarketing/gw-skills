---
name: api-access-guide
description: >-
  Use before any Gorilla Works bot calls a Gorilla Works API or connector
  (Notion, Ember, Hunter, Google Places, RGR Finance, Semrush, GitHub, X,
  Resend, or other MCP tools).
---
# API access guide (all bots)
Depth: blueprints/api-access-guide.md (live docs win). Never print, log, commit, or paste keys, tokens, or prefixes. Read keys at request time from the named env var or store file; do not hard-code or cache them.

## Shared hard rules
Never buy credits or paid units. Exhausted allowance: stop and tell Brennan or use the free fallback. Never rotate or revoke keys; only Grok Bot renews RGR (`renew-key.mjs`). Report every API issue to Brennan, or send the fix to GW Skill Builder (`api-issue-handling`); never leave one silent. Never retry a paid call that may already have been charged, or a write blindly (re-read first). Ember sending stays frozen. Never set `Status` = `Send`. Never publish landing pages. Draft only.

## Per-API hard rules
**Notion REST:** key `NOTION_API_KEY`; Auth Bearer; `Notion-Version: 2026-03-11`; MCP `user-Notion` shares the limit (`notion-shared-rate-limit`). Don't change Prospect Page Codes, blank filled fields, or bulk-write during Hunter or copy/edit windows.
**Ember, Hunter, and Places:** key `EMBER_API_KEY` (prefer) or `/workspace/secrets/ember-api-key.txt`; helper `ember.sh`; Auth Bearer (capital). Re-read `GET /hunter/account` before spending. Places: status first (`gw-google-places-budget`); never retry a failed billed call. Hunter through Ember only. Grok Bot recovers held saves (`hunter-notion-save-recovery`); Lead Research owns Places. Don't POST `/hunter/email-finder` or `/hunter/workflow/run`, or re-run a paid lookup to recover a save. No usable email -> Failed (Nov 18). Job list ~50. Send caps 0.
**RGR Finance:** key `/home/box/rgr-finance/secrets/credentials.json` (store wins after renewal); fallback `BUSINESS_APP_API_KEY` if the store is missing; helper `rgr.sh`; Auth Bearer from the store. Writes need a fresh `IDEMPOTENCY_KEY`. 60 req/key/min, shared. Don't follow redirects with the key, call login or rotate/revoke, loosen permissions, or file/pay without approval (unposted drafts excepted). `AUDIT TEST 2026-11-24` records are not real data.
**Semrush:** the only blog keyword/topic source (Brennan, Nov 24). Volume and KD only from Semrush (else `n/a`); never guess. MCP `user-Semrush` only; no box key; free tier; 10 web searches a day; buy no units. Log sightings in `backlinks/semrush-sightings.md`. On `no_api_units`, stop and write `n/a`.
**GitHub:** `gorillaworksmarketing/gw-skills` (`main`). Key `GH_TOKEN`. Prefer `cursor-github`; never print the token. Shared limits; don't poll. Skill Builder owns pushes. Other bots must not push.
**X:** MCP `user-X` / built-in tools; OAuth via the X plugin Connect card only. No `X_BEARER_TOKEN`. Skill: `x-api-mcp-guide`. On 429, wait `x-rate-limit-reset` and retry once. Don't ask for tokens, call `api.x.com`, or post/DM without a yes on the exact text.
**Resend:** no `RESEND_API_KEY`. Disabled sending path; Ember `POST /api/marketing/webhooks/resend`. Don't send mail or simulate webhooks.
**Other connectors:** use connected MCP tools; never scrape session tokens. Report a disconnected connector (`api-issue-handling`). `user-Gmail`: don't send, reply, forward, trash, or archive unless Brennan asked for that exact message. Other MCP: requested work only; no paid upgrades or production changes without Brennan.
