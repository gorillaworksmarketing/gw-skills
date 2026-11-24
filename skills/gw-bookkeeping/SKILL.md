---
name: gw-bookkeeping
description: >-
  Use for any Gorilla Works bookkeeping or accounting task on the cash basis:
  categorizing receipts, bank or card lines, or Stripe activity; month-end close
  and reconciliation; client pass-through costs (printing, postage, lists,
  client ad spend) and reimbursements; 1099-NEC contractor tracking; Schedule C
  mapping; or learning how Brennan categorizes from his finance app history. Use
  it even if he just says "what category is this" or "close the month".
---
# GW bookkeeping (cash basis, direct mail agency)
Depth: blueprints/bookkeeping.md. Books live in the Gorilla Works Marketing Finance API (Brennan's own cash-basis app). Not tax advice: you prepare, Brennan and his CPA decide.

## Order of authority
1. Brennan's instruction now, or a logged correction.
2. His app rules and categories (`GET /transaction-rules`, `/categories`).
3. Learned rules from his history, high confidence only (blueprint §9).
4. Blueprint defaults, labeled "default, unconfirmed".
5. Otherwise ask. A habit that conflicts with tax law is flagged, never copied or silently fixed.

## Cash-basis core (§1)
Income when received or made available (constructive receipt). Expense when paid; a bank card charge counts on its charge date. Prepaids over 12 months are spread (12-month rule). Unpaid invoices and bills stay off the P&L.

## Categorize (decision tree, §4)
Stop at the first match: duplicate → own-account transfer, card payment or Stripe payout → loan (principal vs interest) → owner draw or contribution → tax payment (income tax is a draw; WA DOR needs a B&O vs sales tax split) → refund (nets against its category) → Brennan or learned rule → personal → client job cost → GW's own marketing → overhead by type → capital item over $2,500 → mixed receipt split by lines → review queue.
Agency rules: client printing, postage, lists and client ad buys are cost of client campaigns (allocation `client` + client/job), never line 8. Line 8 is only for promoting Gorilla Works. Meals 50% with attendee and purpose; entertainment 0%; gifts $25 per person per year. Track every contractor paid by Zelle, ACH, check or cash; a 1099-NEC is due at $2,000+ YTD (2026). Card and platform payments don't count.

## Client reimbursements (§5.1)
Book the cost when paid and the repayment as income when received. Never net them without a CPA instruction. Flag WA B&O (reimbursements are rarely excludable) and whether the invoice states postage separately.

## Learn from history (§9)
Read-only pulls of categories, rules, expenses, income, posted receipts, journal and bank lines across all dates. Normalize vendors, then count his manual choices: High = 3+ uses, 90%+ share, last 3 agree. Handle drift (newest consistent category wins from its date) and stable splits. Store the table only in the private store `finance/` folder (`learned-rules.json/.md`, `corrections-log.md`), never in the public repo.

## Month-end (§7)
Pull, categorize, match receipts, check duplicates, reconcile every account to the statement to $0 or explain the gap, list unbilled pass-throughs, update 1099 and B&O inputs, run reports, send the review queue.

## Guardrails
- Never invent amounts, dates, vendors, attendees, purposes, mileage or receipts.
- Never file, pay, submit or sign anything.
- App writes only after Brennan approves the batch. Send an Idempotency-Key, never `autoPost` without his OK, never delete.
- Transfers, card payments, loan principal, draws, contributions, income tax, payouts and sales tax remitted are not P&L.
- Keep personal out. Keep receipts. Never show the API key.
- Entity type, COGS vs expense, sales tax, de minimis election and reimbursement treatment are CPA questions. Name the default you used.

## Output
Table: date, description, amount, proposed category (Sch C line), allocation/client, basis (rule, learned n/m, default), confidence, question. Then non-P&L items, then the review queue.
