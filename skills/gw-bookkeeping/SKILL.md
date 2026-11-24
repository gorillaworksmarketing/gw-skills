---
name: gw-bookkeeping
description: >-
  Use for any Gorilla Works bookkeeping or accounting task on the cash basis:
  categorizing receipts, bank or card lines, or Stripe activity; logging receipt
  emails from grok@gorillaworksmarketing.com into the finance app; month-end
  close and reconciliation; client campaign costs (printing, postage, lists,
  client ad spend); 1099-NEC contractor tracking; Schedule C mapping; or
  learning how Brennan categorizes from his finance app history. Use it even if
  he just says "what category is this", "log my receipts" or "close the month".
---
# GW bookkeeping (cash basis, direct mail agency)
Depth: blueprints/bookkeeping.md. Books: Gorilla Works Marketing Finance API. Single-member LLC, Schedule C. Blueprint §3 is the standard chart (no CPA chart). Every app account is business. Not tax advice: you prepare, Brennan decides.

## Authority (§0)
Brennan's instruction or logged correction → his app rules and categories → high-confidence learned rules (§9) → blueprint defaults ("default, unconfirmed") → ask. A habit that breaks tax law is flagged, not copied or silently fixed.

## Cash basis (§1)
Income when received or made available. Expense when paid; a bank card charge counts on its charge date. Prepaids over 12 months are spread. Unpaid invoices and bills stay off the P&L.

## Categorize (§4, first match wins)
Non-P&L first: duplicate, transfer/card payment/Stripe payout, loan (principal vs interest), owner draw or contribution, tax payment (income tax = draw; WA DOR = B&O vs sales tax split), refund (nets against its category). Then his or a learned rule → client job cost → own marketing → overhead → capital item over $2,500 → split mixed receipts by line → review queue.
Client printing, postage, lists and ad buys are cost of client campaigns (allocation `client` + client/job), never line 8 (line 8 promotes GW only). Meals 50% with attendee and purpose; entertainment 0%; gifts $25/person/year. 1099-NEC: track contractors paid by Zelle, ACH, check or cash ($2,000+ YTD in 2026); card/platform payments excluded.

## Client payments (§5.1)
Clients prepay everything: book the full payment as agency services income when received. Never split out a reimbursement or net against costs. Campaign costs are separate expenses when paid, tagged to client/job. Flag WA B&O on the gross.

## Learn from history (§9)
Read-only pulls of all history, normalize vendors, count his manual choices (High = 3+ uses, 90%+ share, last 3 agree); handle drift and splits. Learned rules stay in private store `finance/`, never the repo.

## Receipt emails (§13, daily)
Search Gmail `to:grok@gorillaworksmarketing.com` for receipts, invoices, payment confirmations, PDF/image attachments. Paid receipt or refund → intake; unpaid invoice = open bill, no expense until paid; promos → not-receipt. Extract from the document only (missing = null, flagged). Dedupe (message id; vendor+amount+date vs the app). Upload as an unposted draft (upload-url → PUT → extract). Log in `finance/receipts-processed-log.md`; label `Receipts/Logged`. Never reply, forward, trash or archive.

## Batch flow (§9.5) and month-end (§7)
Suggest the batch → Brennan approves or corrects (log corrections) → post exactly the approved batch with an Idempotency-Key, then match bank lines → read back and report.
Month-end: categorize, match, dedupe, reconcile each account to its statement ($0 or explain), update 1099/B&O inputs, run reports, send the review queue.

## Guardrails (§10)
- Never invent amounts, dates, vendors, attendees, purposes, mileage or receipts.
- Never file, pay, submit or sign anything.
- Categorize, post or match only after Brennan approves that batch (unposted receipt drafts OK, §13.6); no `autoPost` without his OK; never delete.
- Transfers, card payments, loan principal, draws, contributions, income tax, payouts and sales tax remitted are not P&L.
- Keep receipts; never show the API key.
- COGS vs expense, sales tax, de minimis: open defaults; name the one used.

Output: §11 batch table, non-P&L items, review queue.
