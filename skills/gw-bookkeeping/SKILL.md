---
name: gw-bookkeeping
description: >-
  Use for any Gorilla Works bookkeeping or accounting task on the cash basis:
  categorizing receipts, bank or card lines, or Stripe activity; month-end close
  and reconciliation; client campaign costs (printing, postage, lists, client ad
  spend); 1099-NEC contractor tracking; Schedule C mapping; or learning how
  Brennan categorizes from his finance app history. Use it even if he just says
  "what category is this" or "close the month".
---
# GW bookkeeping (cash basis, direct mail agency)
Depth: blueprints/bookkeeping.md. Books live in the Gorilla Works Marketing Finance API (Brennan's cash-basis app). Gorilla Works Marketing, LLC is a single-member LLC filing Schedule C. No CPA chart: the blueprint chart (§3) is the standard. Every account in the app is business. Not tax advice: you prepare, Brennan decides.

## Order of authority (§0)
Brennan's instruction or logged correction → his app rules and categories (`GET /transaction-rules`, `/categories`) → high-confidence learned rules (§9) → blueprint defaults, labeled "default, unconfirmed" → ask. A habit that conflicts with tax law is flagged, never copied or silently fixed.

## Cash-basis core (§1)
Income when received or made available (constructive receipt). Expense when paid; a bank card charge counts on its charge date. Prepaids over 12 months are spread (12-month rule). Unpaid invoices and bills stay off the P&L.

## Categorize (§4 tree, first match wins)
Non-P&L checks first: duplicate, transfer/card payment/Stripe payout, loan (principal vs interest), owner draw or contribution, tax payment (income tax = draw; WA DOR = B&O vs sales tax split), refund (nets against its category). Then Brennan's or learned rule → client job cost → GW's own marketing → overhead → capital item over $2,500 → mixed receipt split by lines → review queue.
Client printing, postage, lists and ad buys are cost of client campaigns (allocation `client` + client/job), never line 8; line 8 only promotes Gorilla Works. Meals 50% with attendee and purpose; entertainment 0%; gifts $25 per person per year. Track contractors paid by Zelle, ACH, check or cash; 1099-NEC at $2,000+ YTD (2026); card and platform payments don't count.

## Client payments (§5.1, Brennan's practice)
Clients prepay everything as agency services. Book the full payment as agency services income when received: never split out a reimbursement and never net it against costs. Campaign costs are separate expenses when paid, tagged to client/job. WA B&O applies to the gross receipt; flag it.

## Learn from history (§9)
Read-only pulls of all history; normalize vendors; count his manual choices (High = 3+ uses, 90%+ share, last 3 agree); handle drift and stable splits. Store the table only in the private store `finance/` folder, never the public repo.

## Batch flow (§9.5)
Suggest the batch → Brennan approves or corrects (log corrections) → post exactly the approved batch with an Idempotency-Key → read back and report what posted.

## Month-end (§7)
Pull, categorize, match receipts, check duplicates, reconcile every account to the statement ($0 or explain), update 1099 and B&O inputs, run reports, send the review queue.

## Guardrails (§10)
- Never invent amounts, dates, vendors, attendees, purposes, mileage or receipts.
- Never file, pay, submit or sign anything.
- No app write before Brennan approves that batch; no `autoPost` rules without his OK; never delete.
- Transfers, card payments, loan principal, draws, contributions, income tax, payouts and sales tax remitted are not P&L.
- Keep receipts. Never show the API key.
- COGS vs expense, sales tax and the de minimis election are open: name the default used and flag it.

Output: the §11 batch table (with basis and confidence), then non-P&L items, then the review queue.
