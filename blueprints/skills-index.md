# Skills index blueprint

Detail moved out of `gw-skills-index` to keep it at or under 3,500 characters. Nothing here was dropped; these are the full versions of the index entries that point here.

## Standing rule (2): new training files
New training files arrive in `cold-email/` and `lead-gen/` (video notes: `cold-email/brennan-video-notes.md`). At session start, merge each into the matching email or lead-gen skill and its blueprint. Do not create a blueprint per source.

## Standing rule (4): depth file pointers
SEO/GEO basics: blueprints/blog.md; email copy depth: blueprints/email-copy-frameworks.md.

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
