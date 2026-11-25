# API access guide blueprint (skill `api-access-guide`)

Full detail for the compact skill `api-access-guide`. **Live docs win over this snapshot.** Re-read the live OpenAPI, llms-full, and working guides before a write or a paid call if anything here could have changed.

**Created 2026-11-24 from Brennan all-hands Part A.** Quotas below are as of the Nov 24, 2026 re-audit (about 2:50–3:00 PM America/Phoenix) unless a line says otherwise. Remaining balances marked unverified must be re-read live before spending.

This file is in the public `gorillaworksmarketing/gw-skills` repo. It contains **no secret values**. Keys are named only as environment variables or file paths. Never paste a key, token, or key prefix into chat, logs, git, or this file.

## Related skills

- `api-access-guide` — when to use: any bot about to call a Gorilla Works API or connector.
- `api-issue-handling` — classify and handle or report every API error; never leave one silent.
- `notion-shared-rate-limit` — shared Notion limit with Ember; pacing, 429 backoff, copy/edit windows.
- `hunter-notion-save-recovery` — Grok Bot only; recover already-paid Hunter results Ember failed to save to Notion.
- `gw-google-places-budget` — free Places allowance first, signed-out Maps scrape second; same full record on every path.
- `gw-bookkeeping` — cash-basis books on the RGR Finance API; receipt intake; batch approval before posting.
- `cold-email-lead-research` — paced, batched Notion row creation; Places/Maps discovery.
- `x-api-mcp-guide` — X error handling and MCP usage (managed Cursor skill; not in the gw-skills repo). Also `gw-x-post`, `gw-x-editor`, `social-reply`.
- `gw-skills-index` — start every session here; this guide is in the Shared / always-on section.

## Related guides and helpers (do not copy secrets out of them)

- Notion Cold Leads guide: Notion page `40e92472-fef9-8109-8470-e9e6aa31c60d`; upkeep rule at `/cursor/stores/user/cold-email/notion-api-guide-upkeep.md`; a snapshot lives at `/workspace/api-guide-v317.md` (v3.17 snapshot). Live guide is v4.0 as of Nov 24, 2026, 4:55 PM PT (five retired columns removed; new view column order; section 4 and the 12a template updated).
- Ember helper and older README: `/workspace/ember/ember.sh`, `/workspace/ember/README.md` (last full write-up Oct 23 / Hunter section Nov 5; live OpenAPI is newer). Live docs: `https://ember-email.replit.app/api/marketing/llms-full.txt` and `/api/marketing/openapi.json`. Audit copy: `/workspace/api-audit-2026-11-24/ember-r2/`.
- RGR Finance: working guide `/home/box/rgr-finance/api-guide.md`, helper `/home/box/rgr-finance/rgr.sh`, public docs `https://rgr-finance.replit.app/api/llms.txt`, `/api/llms-full.txt`, `/api/openapi.json`. Audit copy: `/workspace/api-audit-2026-11-24/rgr-r2/`.
- Skills on the box: `/home/box/sand-data/workflows/<skill>/SKILL.md` (also reachable as `/home/box/agent-data/workflows/`, a symlink).
- All-hands source for this snapshot: `/home/box/team/all-hands-2026-11-24.md`.

## Shared hard rules (every API)

- Never print, log, commit, or paste API keys, tokens, or key prefixes. Read a key at request time from the named env var or store file; do not hard-code it or cache it across days.
- Never buy credits or paid API units. If allowance is exhausted, stop and tell Brennan or follow the documented free fallback.
- Never rotate or revoke keys yourself. RGR renewal is only Grok Bot's daily routine (`node /home/box/rgr-finance/renew-key.mjs`).
- Every API access issue is either reported to Brennan or its cause and fix go to GW Skill Builder (`api-issue-handling`). Never leave one silent.
- Never retry a paid call that may already have been charged (Hunter verify/search, Google Places search/details). Never retry a write blindly; re-read first.
- Ember sending stays frozen. Never set Cold Leads `Status` = `Send`. Never publish landing pages. Draft only.

---

## 1. Notion REST

**What it's for:** Cold Leads databases (and other Gorilla Works Notion work). All bots and Ember's Hunter worker share one integration (Replit Marketing Integration) and one rate limit.

**Base URL:** `https://api.notion.com/v1`

**Where the key lives:** env var `NOTION_API_KEY`. (Ember uses the same integration.)

**Auth headers on every request:**

- `Authorization: Bearer $NOTION_API_KEY`
- `Notion-Version: 2026-03-11`
- `Content-Type: application/json`

**Typical endpoints (do not invent new ones):**

- Query a data source: `POST /v1/data_sources/{data_source_id}/query`
- Read or update a page: `GET` or `PATCH /v1/pages/{page_id}`
- Move a page between industry DBs: `POST /v1/pages/{page_id}/move` (parent `data_source_id`)

Prefer targeted, filtered queries over full-database scans. There is no dedicated helper script like `rgr.sh`; use short scripts that read `NOTION_API_KEY` and never print it. MCP `user-Notion` talks to the same workspace and **counts against the same limit**.

**Rate limits:** About 3 requests per second **in total** across every bot and Ember, not per bot. One request at a time; pause about 350 ms after each call. On 429, wait `Retry-After` (or a conservative backoff) and retry only a safe read, or a write you have re-read and confirmed did not land. Skill: `notion-shared-rate-limit`.

**Owner:** Shared. GW Lead Research creates and researches rows; GW Email Copywriter and GW Email Editor write copy in their windows; Ember writes Hunter results; Grok Bot recovers held Hunter saves (step 0b of the 12:30 PM America/Phoenix check; skill `hunter-notion-save-recovery`) and keeps the Replit guide in sync.

**Don'ts:** Never set `Status` = `Send` (only Brennan does). Never change a Prospect Page Code. Never overwrite filled research or copy fields with blanks. Never run bulk scans or bulk writes in parallel with Ember's Hunter worker or during copy/edit windows if it can be avoided. Don't put tokens on the Notion guide page. Never write or re-add Decision Maker Name, Decision Maker Title, Decision Maker Source, DM Note, or Legacy Page ID (deleted Nov 24, 2026, guide v4.0). New Cold Leads tables are built only through `/workspace/pp/notion_writer/cold_leads_schema.py` (`strip_deleted`, then `apply_view_order`); view column order and the nine held columns are in blueprints/cold-email.md.

**IDs (from the all-hands guide; verify live if a write depends on them):** hub parent Cold Leads – US `40892472-fef9-81bd-ad87-d33ec80ff253`; default Fencing data source `a4454d83-7e9f-4e5c-8b81-31fd957e6180`. Active intake is Roofing (data source prefix `4f68dbd1…`). Full UUIDs are in the live guide, not repeated here from stale snapshots. These IDs are internal reference IDs, not secrets.

**Copy and edit windows** (also in `notion-shared-rate-limit` and `blueprints/cold-email.md`): GW Email Copywriter 7:00 AM, 1:30 PM, and 5:30 PM PT (8:00 AM, 2:30 PM, 6:30 PM America/Phoenix in winter). GW Email Editor 9:30 AM, 3:30 PM, and 7:30 PM PT (10:30 AM, 4:30 PM, 8:30 PM America/Phoenix in winter). Since Nov 24, 2026, 4:02 PM PT, no funnel stage has a daily cap, so each window works every eligible row and can run long.

---

## 2. Ember (ember-email.replit.app), including Hunter workflow and Places

**What it's for:** The email / marketing app: Hunter Email Lookup workflow, Google Places (free allowance), prospect pages, writing jobs, and (when Brennan turns it on) sending.

**Base URL:** `https://ember-email.replit.app/api/marketing`

- Health: `https://ember-email.replit.app/api/healthz`
- Public docs: `/api/marketing/llms.txt`, `/api/marketing/llms-full.txt`, `/api/marketing/openapi.json`

**Where the key lives:** env var `EMBER_API_KEY`. A file copy also exists at `/workspace/secrets/ember-api-key.txt` (mode 600). Prefer the env var. Never print either. In-app docs may call the variable `$EMBER_KEY`; on the box it is `EMBER_API_KEY`.

**Helper:** `/workspace/ember/ember.sh` (reads `EMBER_API_KEY`, never prints it). Examples: `ember.sh get /settings`, `get /hunter/workflow`, `get /places/status`, `get /hunter/account`. Writes require `--confirm-write`. send/schedule/activate and `/import` also need `EMBER_ALLOW_SEND=yes-brennan-approved`, which is not authorized.

**Auth header:** `Authorization: Bearer $EMBER_API_KEY` (capital `Bearer`). `X-API-Key` is treated as anonymous. Scheme must be `Bearer`; a lowercase `bearer` was previously rejected (fixed as of the Nov 24 re-audit — still send `Bearer`).

**Documented Hunter paths** (relative to the marketing base; include `/api/marketing/` or the helper will prefix it):

- `GET /hunter/status` — config; no credits
- `GET /hunter/account` — plan / remaining included credits
- `GET /hunter/workflow` — config, enabled flag, recent jobs (list is only the latest ~50)
- `GET` or `POST /hunter/workflow/refresh` — live allowance + Notion field metadata; no email-lookup credits (may 429 `HUNTER_BUSY`)
- `POST /hunter/workflow/jobs/{id}/reconcile` — receipt vs Notion readback; no re-verify
- `POST /hunter/email-verifier` — paid verify of an explicit address (research only)
- `POST /hunter/domain-search` — paid domain search
- `POST /hunter/workflow/run` — **do not call** to recover a missed Notion save; spends credits

**Places (free reads vs billed):**

- `GET /places/status` — free; read at the start of every run
- `POST /places/search` — 1 credit per page of up to 20 businesses
- `GET /places/{placeId}` — billed; only when it adds fields and credits remain

**Rate limits / quotas (Nov 24 re-audit, about 2:50–3:00 PM America/Phoenix):**

- In-app docs (Oct 23 README) said 120 requests/minute/key. The Nov 24 audit observed no API-wide limit and no rate-limit headers, with per-action cooldowns (429 + `Retry-After`, e.g. review-companies, `HUNTER_BUSY`). Treat the 120/min figure as **unverified / possibly stale**; honor 429s.
- Hunter included credits: **about 800 remaining until Dec 5, 2026**. Audit read Hunter's own balance as **802.5** remaining (used 1207.5 of 2010); Ember may show less because of reservations (780 shown vs 802.5 at that time). Remaining after the afternoon scrape is **unverified** — re-read `GET /hunter/account` (free) before spending.
- Workflow `creditCap` is null (no daily cap). With no funnel caps, credits may run out before Dec 5; rows then wait at Email Lookup until the reset.
- Google Places: see section 5. Weekday send caps are all 0. Sending is frozen anyway.

**Owner:** Grok Bot owns access recovery, the daily Hunter→Notion save check, and API audits. Ember's worker runs Hunter and the first Notion write. GW Lead Research uses Places (browser while the free allowance is 0). Copy/edit bots should not hit Ember send or publish routes.

**Don'ts:** Sending stays frozen — no `send` / `schedule` / `activate`, no `/import`, no mailbox or approval changes. Never publish landing pages. Never bind live senders or pages, submit a real questionnaire, or call `/webhooks/resend`. Never use `POST /hunter/email-finder` (Hunter's name-based finder). Never call `POST /hunter/workflow/run` or re-spend credits to recover a missed Notion save. Never buy Hunter or Places credits.

**Requested Ember product fixes** (not bot workarounds; also in `blueprints/cold-email.md`): retry its own Notion save with backoff on 429 or connection errors instead of holding the job; make the Hunter job list pageable/filterable (the list is only the latest ~50, so older holds can scroll out of view); split skipped vs real save failures in totals; when Ember saves a "no usable email" result, set Status to `Failed` (Brennan Nov 18) instead of leaving the row at Email Lookup; a row that is already Verified should not be left at Email Lookup.

---

## 3. Hunter

**What it's for:** Email discovery and verification for Cold Leads Email Lookup.

**How the team must call it:** Through Ember only, with `EMBER_API_KEY`, as in section 2. Brennan's rule (guide v3.16+): do **not** call Hunter.io directly for this table, and do not have Replit/Claude call Hunter.

**Direct API (do not use for Cold Leads):** env var `HUNTER_API_KEY` is present on the box. There is no approved helper for `api.hunter.io` in this pipeline. Older backlink notes that mentioned verifying with `HUNTER_API_KEY` are stale for Cold Leads.

**Quotas:** Starter plan, shared credit model, `resetDate` 2026-12-05. About 800 credits left as of 3:00 PM America/Phoenix on Nov 24 (see section 2). Workflow `creditCap` is null (no daily cap).

**Owner:** Ember runs the workflow. Grok Bot recovers held Notion saves (`hunter-notion-save-recovery`) without re-running Hunter. Replit/Claude does not call Hunter.

**Don'ts:** Never use the name-based finder (`POST /api/marketing/hunter/email-finder`, or any Hunter.io finder-by-name/company/LinkedIn call). Never buy credits. Never re-run a paid lookup to recover a missed Notion save. Never invent an email or mark Verified when there is no usable address. When Hunter finds no usable email, Status must be `Failed` (Brennan Nov 18), not left at Email Lookup.

---

## 4. RGR Finance (Gorilla Works Marketing Finance)

**What it's for:** Books, receipts, income, expenses, jobs, dashboard, planning. Cash-basis bookkeeping for Gorilla Works Marketing. Skill: `gw-bookkeeping`.

**Base URL:** `https://rgr-finance.replit.app/api`

- Public docs: `/api/llms.txt`, `/api/llms-full.txt`, `/api/openapi.json`
- Working guide: `/home/box/rgr-finance/api-guide.md`

**Where the key lives:** shared store `/home/box/rgr-finance/secrets/credentials.json` (directory mode 700, files 600). Fallback env var `BUSINESS_APP_API_KEY` only if the store is missing or empty. After a renewal, the env var may be stale — the store is the source of truth. Never copy the key into `/workspace`, git, chat, or logs.

**Helper:** `/home/box/rgr-finance/rgr.sh`. Examples: `rgr.sh GET /context`, `rgr.sh GET /clients`. Writes need a fresh `IDEMPOTENCY_KEY` (16–128 letters, digits, hyphen, underscore): `IDEMPOTENCY_KEY=... /home/box/rgr-finance/rgr.sh POST /expenses '{"amount":1}'`.

**Auth header** (the helper sets this): `Authorization: Bearer <active secret from the store>`. Scheme must be exactly `Bearer`. Do not follow redirects with the key attached. Do not call `/api/auth/login` or use a dashboard session.

**Rate limits:** 60 requests per key per minute, shared by every bot. Honor `Retry-After` on 429. Confirmed via `context.rateLimit`.

**Owner:** Grok Bot owns key renewal (daily `node /home/box/rgr-finance/renew-key.mjs`; `rgr.sh` also runs that check at most once per 24 hours). GW Bookkeeper uses the API for receipts and categorization (`gw-bookkeeping`) after Brennan approves a batch. All bots may use `rgr.sh`.

**Don'ts:** Never rotate or revoke the key; never call `POST /api/api-key/rotate` or revoke endpoints as a test. Never print the key. Do not loosen secret-file permissions. Do not treat leftover `AUDIT TEST 2026-11-24` records as real data. Do not delete, auto-post, or file/pay anything without Brennan's approval (unposted receipt drafts are the documented exception in `gw-bookkeeping`). Do not sync live Stripe, bank, or vendor cleanup as a test.

---

## 5. Google Places (via Ember)

**What it's for:** Lead discovery: name, Place ID, Maps URL, address, phone, website, rating, review count, reviews, categories, hours, and related fields. Same full record on every path (Ember Places or signed-out Maps scrape). Skill: `gw-google-places-budget`.

**Base URL:** same Ember marketing base. Endpoints: `GET /places/status` (free), `POST /places/search` (1 credit / page of up to 20), `GET /places/{placeId}` (billed).

**Where the key lives:** `EMBER_API_KEY` (Ember holds the Google server key). There is no separate Places key in the box env.

**How to call it:** `/workspace/ember/ember.sh get /places/status` before any billed call. While `freeRemaining > 0`, use Ember search first. When `freeRemaining` is 0, GW Lead Research scrapes Google Maps in a signed-out browser and still captures the same field set (30 or more reviews required, >= 30; fail only 29 or fewer).

**Quotas (2:50 PM America/Phoenix, Nov 24):** `freeLimit` 800, `freeUsed` 800, `freeRemaining` 0, rolling window ~32 days, `perMinuteLimit` 10. 26 requests already that day at 2:50 PM. Exact reset date is **unverified** (parent briefing: about Nov 30). Browser scrape only until it resets. A failed or timed-out billed call still uses a credit — never retry it; only `/places/status` may retry.

**Owner:** GW Lead Research for discovery. Other bots should not spend Places credits. While discovery is on the signed-out browser path, Lead Research has first priority on the shared computer (API calls from other bots are fine; extra browser windows are not).

**Don'ts:** Never go over the free limit. Never buy Places credits or paid enrichment. Never invent a field. Never overwrite a filled field with a blank. 29 or fewer reviews, or an unknown count: no row. Exactly 30 qualifies (settled Nov 25; do not ask Brennan again).

---

## 6. Semrush (free tier)

**What it's for:** Keyword volume and KD, and occasional backlink / Authority Score sightings. Volume and KD come only from Semrush; otherwise write `n/a`. Never guess.

**How to call it:** MCP namespace `user-Semrush` (OAuth / connected Semrush account). There is **no** `SEMRUSH_API_KEY` (or similar) in the box environment. Do not put a Semrush key in a query string from this box. Generic Semrush REST (`https://api.semrush.com/`) is documented in third-party notes but is **not** the approved path here, and paid API units are parked.

**Rate limits / quotas:** Brennan's **10 free Semrush web searches a day**. Log useful backlink / referring-domain numbers in `backlinks/semrush-sightings.md`. The Semrush MCP has often returned `no_api_units` (not retryable; more units would be a purchase — do not buy). Remaining searches on a given day: **unverified**. One Nov 10 note also mentioned “5 allowed lookups”; the standing backlinks rule is 10 free web searches a day — treat “5” as possibly stale.

**Owner:** GW Blog Research (volume/KD) and GW Backlinks (sightings). All bots that use a free search must log it.

**Don'ts:** Never buy API units. If the MCP says `no_api_units`, stop, write `n/a`, and do not retry paid endpoints.

---

## 7. GitHub (`gorillaworksmarketing/gw-skills`)

**What it's for:** Source of truth for GW skills, blueprints, and brand files.

**Repo:** `https://github.com/gorillaworksmarketing/gw-skills` (branch `main`).

**Where the key lives:** env var `GH_TOKEN` (for `gh` or REST fallback only). Prefer built-in `cursor-github` tools, which use Brennan's connected GitHub account and do not need the token printed or passed in a command you write by hand.

**How to call it:** `cursor-github` MCP tools for reads, issues, and PRs. `gh` only as a fallback if those tools are unavailable. Skill Builder owns pushes to `main`. Other bots should not push, force-push, or change workflow permissions.

**Rate limits:** GitHub authenticated limits apply and are shared with cloud agents. Exact remaining budget is **unverified**. Batch and page; don't poll.

**Owner:** GW Skill Builder for skill updates. Every bot reads skills from this repo (or the synced copy under the workflows directory).

**Don'ts:** Never print `GH_TOKEN`. Never collect a token from Brennan or paste it into chat. Do not treat a local `/workspace` skills checkout as newer than `main` unless Skill Builder just pushed.

---

## 8. X

**What it's for:** Reading and searching posts; drafting or (only with Brennan's yes) posting from Brennan's account. Skills: `x-api-mcp-guide`, `gw-x-post`, `gw-x-editor`, `social-reply`.

**How to call it:** MCP `user-X` / built-in X tools. The user signs in through the X plugin Connect card (OAuth). That connection is the only way in.

**Where the key lives:** No X bearer token or `X_BEARER_TOKEN` is used, and none should be requested.

**Rate limits:** On 429, wait for `x-rate-limit-reset` and retry once. Other error handling is in `x-api-mcp-guide`.

**Owner:** GW social / copy / editor bots for drafts. Posts go out only after Brennan approves the exact text.

**Don'ts:** Never ask for or accept a Bearer token, API key, password, or `X_BEARER_TOKEN`. Never call `api.x.com` yourself. Never sign into x.com in a browser to get a token. Never post, DM, or change lists without an explicit yes on the exact text. A Chat PIN, if ever needed, is requested by secret-request only — never typed in chat.

---

## 9. Resend

**Status:** Present only as an Ember webhook and a disabled sending path. **No** `RESEND_API_KEY` in the box environment.

**What exists:** Ember documents `POST /api/marketing/webhooks/resend`. Ember settings text (Oct 23, not re-verified as a live send path on Nov 24): “Resend sending is disabled.” InboxKit is the mailbox provider; `deliveryReady` was historically false. The Nov 24 audits did not call the webhook.

**Don'ts:** Do not send mail through Resend. Do not simulate webhook receipts. Do not invent a Resend integration from generic CLI docs.

---

## 10. Other connected APIs (MCP / connectors)

These have no extra key files in `/workspace/secrets` besides what is already named above. Use the connected MCP tools; never extract tokens from a browser session.

| Service | How to access | Notes |
| --- | --- | --- |
| Notion (MCP) | `user-Notion` | Same workspace and **same rate limit** as Notion REST. Pace it (`notion-shared-rate-limit`). |
| Gmail | `user-Gmail` | Receipt intake and mail reads. Do not send, reply, forward, trash, or archive unless Brennan asked for that exact message. |
| Google Calendar | `user-Google-calendar` | Scheduling only when the task calls for it. |
| Zapier | `user-Zapier` | Use only for requested Zapier work. |
| TubeAlfred (YouTube) | `user-Tubealfred-youtube` | Free tier for video research. No paid upgrades. |
| Replit | `user-Replit` | Ember/finance apps are Replit-hosted; do not change production apps or publish without Brennan. |
| Cursor Origin | `cursor-origin` | Source-control on Origin; prefer built-in tools over cloning. |

If a connector is disconnected or unauthorized, report it (`api-issue-handling`); do not scrape a logged-in session for a token.

---


## Known box and unsigned-IP limits (Nov 25, 2026)

**Reddit:** Public JSON (`https://www.reddit.com/r/<sub>/search.json` and similar) returns a 403 HTML block page from this box; RSS returns 404 or 429. Reddit blocks unsigned datacenter IPs. This is not an auth or key issue. Current fix: do not call those endpoints for discovery; build candidate threads from cited web-search results of public Reddit threads and use `--source file` (`/workspace/reddit-leads/README.md`; `run.py --source reddit` detects the block and stops cleanly). Store the thread URL and put the quote in Owner Evidence (the comment permalink is not in those search results). Full fix: Reddit's official free API with an app ID and secret — only Brennan can approve; pending his decision, not approved.

**Web search from the box:** The box cannot do its own web search (DuckDuckGo serves a captcha; Bing results from the box are junk). Website discovery and any search that needs a web index must be done by an agent with web search.

## Changelog

- 2026-11-25 ~3:41 PM America/Phoenix: live Notion API guide noted as v4.0; never write or re-add the five deleted Cold Leads columns; new tables only via `cold_leads_schema.py`. Added known box limits: Reddit unsigned-IP block (current file-source workaround; official API pending Brennan) and no reliable web search from the box. Places qualify wording settled to 30 or more (>= 30); fail only 29 or fewer.
- Created 2026-11-24 from Brennan all-hands Part A.
