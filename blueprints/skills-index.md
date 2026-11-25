# Skills index blueprint

Detail moved out of `gw-skills-index` to keep it at or under 3,500 characters. Nothing here was dropped; these are the full versions of the index entries that point here.

## Standing rule (2): new training files
New training files arrive in `cold-email/` and `lead-gen/` (video notes: `cold-email/brennan-video-notes.md`). At session start, merge each into the matching email or lead-gen skill and its blueprint. Do not create a blueprint per source.

## Standing rule (4): depth file pointers
SEO/GEO basics: blueprints/blog.md; email copy depth: blueprints/email-copy-frameworks.md.

## Standing rule (6): source of truth
Source of truth is `gorillaworksmarketing/gw-skills`, `skills/<slug>/SKILL.md`. GW Skill Builder pushes changes. Do not treat a local `/workspace` checkout as newer than `main` unless Skill Builder just pushed.

## Blog and long-form (when-to-use)
- `blog-keyword-research`: GW Blog Research. Find, qualify, and prioritize blog topics. Semrush is the only keyword research source (Brennan, Nov 24): use only the `user-Semrush` MCP connector, the free tier (10 web searches a day), and buy no units. All or almost all posts come from Semrush keywords plus GW Video Research. PAA is not the topic source; it may support question wording and AEO answers after the keyword is chosen. Depth: blueprints/blog.md.
- `blog-brief-writing`: GW Blog Research / Copywriter. Turn a qualified Semrush keyword plus Video Research notes into a brief or refresh brief. Video Research is a main input for every brief, not an add-on.
- `video-research`: GW Video Research / Blog Research. Main brief input. Transcripts to information-gain notes and briefs for a Semrush keyword (or a pasted link, or library building). Do not take topics from PAA or Google Trends.

## Shared: `gw-brand-guidelines`
Every bot, every piece: input guard, persona reset, voice, words, inline citations, visuals, editor retry loop. Files: `brand/brand-guidelines.md`, `scripts/`.

## Finance: `gw-bookkeeping`
- **Who:** Bookkeeper, Expense Manager, Grok Bot (and any bot touching Gorilla Works money records).
- **When:** categorizing receipts, bank or card lines, or Stripe activity; "what category is this"; month-end close and reconciliation; client campaign costs (printing, postage, lists, client ad spend) and client prepayments (booked in full as agency services income); 1099-NEC contractor tracking; Schedule C mapping; learning how Brennan categorizes from his finance app (Gorilla Works Marketing Finance API) history.
- **Depth:** `blueprints/bookkeeping.md` (cash-basis rules, agency chart of accounts, decision tree, month-end close, 1099s, learn-from-history procedure, sources).
- **Private data:** learned category rules, corrections and any real transaction data live only in the private store `finance/` folder, never in the public gw-skills repo.
- **Entity:** Gorilla Works Marketing, LLC, single-member LLC filing Schedule C; the blueprint chart is the standard (Brennan, Nov 23, 2026).
- **Batch flow:** suggest categories per batch; after Brennan approves a batch, post exactly that batch to the app.
- **Never:** file, pay, submit or sign anything; write to the finance app without Brennan's approval of the batch.

## Analytics (GW Analytics)
- Uses `gw-lead-generation` (leading vs lagging, UTM conversion) and each blueprint's learning loop.

## Cold email: Guide v3.22 §0 contract
- Guide v3.22 §0 = Ember/landing-page contract (scope, roles, retries, receipts); Brennan's direct rules win.

## Operations: `gw-executive-assistant`
- **Who:** Grok Bot and the Executive Assistant bot.
- **When:** capturing, dictating or updating Brennan's operations tasks and to-dos (relative dates, importance, status, blocked and waiting-on items, recurring to-dos); "what do I have today", "what's my week", "what's overdue"; "done with X", "push X to Friday"; Monday weekly view and Friday progress report ("how am I doing"); meeting follow-ups; an empty chat opener (today's view).
- **Where tasks live:** the planning workspace in the Gorilla Works Marketing Finance API (`GET /api/planning`, `POST /api/planning/commands`); there is no `/tasks` path.
- **Depth:** `blueprints/executive-assistant.md` (Brennan's outline rules marked [B], which win; field and status mapping, `ea:` notes footer, write protocol and errors, ranking, daily/weekly/progress formats, habits, routines, guardrails, examples).
- **Never:** read, create, edit or delete finance data (that is `gw-bookkeeping`); reveal or log the API key; delete a task without his explicit yes; invent tasks, dates or completion status; send email or messages; write calendar events.


## Section owners (moved out of the index headings)
- Blog and long-form: GW Blog Research, Copywriter, Editor.
- Social: GW Social Research, Copywriter, Editor.
- Engagement: GW Engagement.
- Backlinks: GW Backlinks.
- Analytics: GW Analytics.
- Cold email: GW Lead Research, Email Copywriter, Email Editor; Grok Bot owns `hunter-notion-save-recovery` and shares deliverability.
- Finance: Bookkeeper, Expense Manager, Grok Bot.
- Operations: Grok Bot, Executive Assistant.

## Shared: `api-access-guide` (always-on)
Use before any Gorilla Works bot calls a Gorilla Works API or connector (Notion, Ember, Hunter, Google Places, RGR Finance, Semrush, GitHub, X, Resend, or other connected MCP tools). Shared hard rules, then one compact entry per API: what it's for, base URL, where the key lives (env var or file path name only), the helper, the auth header, rate limits, the owner, and key don'ts. Depth, endpoints, re-audit quotas, IDs, and paths: `blueprints/api-access-guide.md`. Live docs win over that snapshot. Related: `api-issue-handling`, `notion-shared-rate-limit`, `hunter-notion-save-recovery`, `gw-google-places-budget`, `gw-bookkeeping`, `x-api-mcp-guide`.

## Shared: `api-issue-handling` (always-on)
Use on any API access issue for any Gorilla Works API (Notion, Ember, Hunter, RGR Finance, Semrush, Google Places, X, and others). Brennan's rule (2026-11-24, America/Phoenix): every API access issue must be reported to Brennan or handled with a documented fix captured in the skills. Never leave one silent.
- Classify: auth 401/403; rate limit 429; quota or allowance; timeout or connection; 4xx bad input; 5xx server.
- Retry with backoff on 429 (wait `Retry-After`), 5xx, and timeouts only when the call is safe to repeat (a free read, or a write with an Idempotency-Key or a confirmed not-landed check). Never retry a write blindly. Never retry a paid call that may already have been charged (Places, Hunter). Never rotate or revoke keys; no credit purchases; never print keys.
- Escalate to Brennan on auth failure, quota exhausted, a bug in his apps, or data lost or held.
- After a fix, send the cause and the fix to GW Skill Builder so the relevant skill is updated. Log the incident with times in America/Phoenix.
- Worked example: the 2026-11-24 Ember Hunter held-save incident; lasting skills `notion-shared-rate-limit` and `hunter-notion-save-recovery`.

## Shared: `notion-shared-rate-limit` (always-on for any Notion read or write)
Every Gorilla Works bot and Ember use the same Notion integration (Replit Marketing Integration) and share one Notion rate limit. One request at a time, about 350 ms pause (about 3 requests per second in total). Back off on 429 using `Retry-After`. Targeted filtered queries, not full scans. When avoidable, no bulk scans or writes while Ember's Hunter worker is running, or while copywriters and the editor are writing pipeline steps 8–11. Copy windows: 7:00 AM, 1:30 PM, 5:30 PM PT. Edit windows: 9:30 AM, 3:30 PM, 7:30 PM PT (one hour later in America/Phoenix in winter). Since 2026-11-24 4:02 PM PT no stage has a daily cap, so each window can run long. Log request counts. Lead Research must batch large row-creation pushes. See blueprints/cold-email.md and `hunter-notion-save-recovery`.

## Cold email: `hunter-notion-save-recovery`
Owner: Grok Bot. Pipeline step 7b after Ember Hunter, and step 0b of the daily 12:30 PM America/Phoenix cold-email check. Recovers already-paid Hunter results when Ember holds or fails the Notion save. Try reconcile first; on 409 `HUNTER_NO_WRITE_RECEIPT`, write Ember's field format only if the row is still at Email Lookup with empty Hunter fields. Usable verified email → Ready for Summary; no usable email → Failed (Brennan, Nov 18); Hunter never ran → leave for Ember's next scan. Never re-run Hunter or spend credits. Exact Evidence JSON: blueprints/cold-email.md.
