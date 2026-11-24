# Skills index blueprint

Detail moved out of `gw-skills-index` to keep it at or under 3,500 characters. Nothing here was dropped; these are the full versions of the index entries that point here.

## Standing rule (2): new training files
New training files arrive in `cold-email/` and `lead-gen/` (video notes: `cold-email/brennan-video-notes.md`). At session start, merge each into the matching email or lead-gen skill and its blueprint. Do not create a blueprint per source.

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
