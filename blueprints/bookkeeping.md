# Bookkeeping blueprint (cash basis, marketing agency)

Depth for `gw-bookkeeping`. Gorilla Works Marketing, LLC is a direct mail marketing agency in Kirkland, WA. Its books live in the **Gorilla Works Marketing Finance API** (Brennan's own cash-basis app; docs at `/api/reference.md`, local copy `/home/box/rgr-finance/docs/`). Every rule below either cites a source in section 13 or is marked **[GW default, confirm]**. Brennan's own past categorizations beat every default here.

> Not tax advice. The skill prepares and organizes books for Brennan. It never files, pays, submits, or signs anything.

**Confirmed by Brennan (Nov 23, 2026):** (1) Gorilla Works Marketing, LLC is a **single-member LLC filing Schedule C**. (2) He has **no CPA chart of accounts**: the chart in section 3 is the standard. (3) Clients **prepay everything up front as agency services**; the full payment is income and costs are not parsed out (section 5.1). (4) **No personal accounts** are connected to the app; every account is business. (5) The bot **suggests categories per batch** and may **post them to the app after he approves each batch** (section 9.5).

**Still open (use the stated default and flag it):** cost of client campaigns as Part III COGS vs ordinary expense lines; Washington sales tax collection on what GW sells and use tax on untaxed printing; the de minimis safe harbor election; home office method. The skill-level output says which default it used.

---

## 0. Order of authority

1. Brennan's direct instruction (this conversation, or a logged correction).
2. His existing **transaction rules** and **categories** in the finance app (`GET /transaction-rules`, `GET /categories`).
3. The **learned rule table** built from his past manual categorizations (section 9), high confidence only.
4. The defaults in this blueprint (sections 3 to 6), shown to him as "default, unconfirmed". Section 3 is his standard chart (no CPA chart exists), so a section 3 category is the expected answer when items 1 to 3 above are silent.
5. Otherwise: **ask**. Put the item in the review queue with your best guess and why.

A conflict between 2/3 and tax law (for example, a personal Netflix charge he once tagged as Software) is **flagged, not silently fixed and not silently copied**.

---

## 1. Cash-basis principles (what "cash basis" actually means)

| Principle | Rule | Source |
|---|---|---|
| Income timing | Income counts in the year it is **actually or constructively received**. | Pub 538, Cash Method |
| Constructive receipt | Money credited to your account or made available without restriction counts even if you have not touched it. You cannot hold a client check until January to push income into next year. | Pub 538 |
| Expense timing | Deduct in the year **paid**. | Pub 538; Treas. Reg. 1.461-1(a)(1) |
| Bank credit card | A charge on a bank-issued card is "paid" on the **charge date**, not when the card bill is paid. Use the card line's date. A pending authorization is not a payment. | Rev. Rul. 78-38 and 78-39 |
| Prepaid expenses | Paid in advance → deductible only in the year it applies, **unless the 12-month rule** applies: the benefit does not extend beyond the earlier of 12 months after it begins or the end of the next tax year. Example from Pub 538: 3-year insurance paid up front is spread; 1-year policy paid July 1 is deducted in full. | Pub 538; Treas. Reg. 1.263(a)-4(f) |
| Consistency | Cash for income means cash for expenses. Changing methods needs IRS approval (Form 3115). | Pub 538 |
| Invoices and bills | An unpaid invoice is **not income**; an unpaid vendor bill is **not an expense**. They are tracked (AR/AP aging) but stay off the cash P&L. | Pub 538 |
| App behavior | The finance app reports dated received income and dated paid costs only; signed contracts and forecasts are not revenue; undated amount-only entries are excluded from dated reports; posted journal history is not rewritten (use corrections/reversals). | Finance API reference, "Conventions and financial safeguards" |

**Practical consequences for the agency**
- A client's December check deposited January 3: income in the **year it was received** (if it arrived in December and was available, December, per constructive receipt; ask Brennan when it physically arrived if it matters at year end).
- Stripe: revenue is the **gross** the client paid on the charge date; the Stripe fee is an expense; the payout to the bank is a **transfer**, not revenue (section 4).
- A postage meter or USPS account top-up is a prepayment for postage. Under cash rules it is paid when funded; if a large balance straddles year end, **flag it for Brennan** rather than guess. [GW default, confirm]
- An annual SaaS plan paid in November that runs 12 months qualifies for the 12-month rule; a 24-month plan does not (spread it). Flag anything over 12 months.

---

## 2. Bookkeeping basics the skill must reason with

- **Every bank/card line ends in exactly one place**: an income category, an expense category, or a non-P&L bucket (transfer, owner draw, owner contribution, loan proceeds, loan principal, sales tax liability, refund netting). Nothing is left "uncategorized" at close.
- **Double entry, even on cash basis**: each event moves cash and one other account. The app's journal does this; the skill must not post a second copy of an event that the app already posted (Stripe projections, matched bank lines).
- **One source event, one entry**: a card purchase appears on the card statement **and** inside the lump card payment on the bank statement. Categorize the card line; the bank line paying the card is a **transfer** (liability paydown). (OA us-sole-prop-bookkeeping, step 2)
- **Receipt vs bank line**: the receipt is evidence for the bank line, not a second expense. Match it (`/bank/transactions/{id}/candidates`, `/match`), do not duplicate it.
- **Refunds** net against the original category (vendor refund reduces that expense; client refund goes to returns and allowances, Schedule C line 2). Never book a vendor refund as income.
- **Personal vs business**: a business must keep personal spending out. Personal items paid from business money are **owner draws**, not expenses. Business items paid personally are **owner contributions** (or reimbursements to the owner) and are expenses.
- **GW's app holds business accounts only** (Brennan, Nov 23, 2026). So every line starts as presumed business; a charge that looks personal is the exception to flag (owner draw candidate, ask), not something to hunt for line by line. Personal accounts are never added or pulled.

---

## 3. Chart of accounts for a direct mail marketing agency

Mapped to **Schedule C (Form 1040) 2026** lines (OA us-sole-prop-bookkeeping step 1, from the 2026 form). Use the finance app's own category names and its `taxLineCode` options (`GET /categories/tax-lines`) as the final word; this table is the default to propose when a category is missing. **Entity (confirmed Nov 23, 2026):** Gorilla Works Marketing, LLC is a single-member LLC filing Schedule C. There is no CPA chart; this chart is the standard. If the entity ever changes (for example an S-corp election), the same categories must be remapped to Form 1120-S lines; flag it then.

### 3.1 Income

| Category | What goes in | Sch C |
|---|---|---|
| Agency services income | **Every client payment, in full**: campaign management, design, strategy, retainers, setup fees, and the up-front prepayment that also covers print, postage, lists and ad spend. Costs are never parsed out of it (section 5.1). | 1 |
| Refunds to clients | Money returned to a client | 2 (returns and allowances) |
| Other business income | Rebates, fuel tax credits; credit-card cash back only if Brennan decides to treat it as income (flag) | 6 |
| NOT income | Owner contributions, loan proceeds, transfers between own accounts, Stripe payouts, vendor refunds, sales tax collected | none |

There is **no "reimbursed client expenses" income category** in GW's books (Brennan, Nov 23, 2026).

### 3.2 Cost of client campaigns (the agency's "cost of service")

These are costs of **delivering client work**, not the agency's own advertising. A common bookkeeping error is to put client printing and postage on line 8 Advertising. Line 8 is for promoting **Gorilla Works itself**.

| Category | Examples | Sch C mapping (default) |
|---|---|---|
| Campaign printing | Printer invoices for client postcards, EDDM pieces, letters | **Open default:** the app category Cost of client campaigns, mapped to whatever tax line the app category already has; Part III (line 4) vs line 22/27b is still open. Brennan decides once, then keep consistent [GW default, confirm] |
| Campaign postage | USPS postage, EDDM postage, permit-imprint postage, mail house postage pass-through | same as above |
| Mailing lists and data | List purchases, data append, address verification (CASS/NCOA) for client mailings | same as above |
| Mail house / fulfillment | Lettershop, inserting, presort services | same as above |
| Client media buys | Ad spend bought for a client (Meta/Google ads run on a client's behalf, paid by the agency) | same; NOT line 8 |
| Subcontracted client work | Freelance designers/copywriters on client jobs | 11 (contract labor) |

Use the app's `allocation: "client"` plus `clientId`/`jobId` on these so job profitability (client prepayment vs the job's costs) shows. `allocation: "operational"` is for the agency's own overhead.

Why it is open: Pub 334 chapter 6 covers cost of goods sold for businesses that make or buy goods; a service agency that resells printed pieces sits near the line. Either way the total deduction is the same; the choice changes gross margin and must be consistent year to year.

### 3.3 Operating expenses (agency overhead)

| Category | Examples (agency) | Sch C |
|---|---|---|
| Advertising (own) | GW's own Google/Meta/LinkedIn ads, GW's own postcards and postage promoting GW, sponsorships with ad value, trade show booth, promo items, business cards | 8 |
| Car and truck | Standard mileage (2026: 72.5¢ Jan 1 to Jun 30, 76¢ Jul 1 to Dec 31) or actual costs × business %, plus business parking and tolls | 9 |
| Commissions and fees | Referral commissions paid; marketplace fees (merchant fees may go here instead of 27b; follow the app category's tax line) | 10 |
| Contract labor | Freelancers, VAs, designers, developers (non-employees) | 11 |
| Depreciation / §179 | Computers, cameras, furniture over the de minimis amount | 13 (Form 4562) |
| Insurance (not health) | General liability, E&O/professional liability, cyber, business property | 15 |
| Interest | Business loan / line of credit / business card interest | 16c (16b vehicle loan business share) |
| Legal and professional | CPA, bookkeeping, attorney, LLC formation, registered agent | 17 |
| Office expense | Postage for the agency's own admin mail, small office items, printer ink | 18 |
| Rent – equipment | Leased equipment, vehicle lease | 20a |
| Rent – property | Office, coworking, storage | 20b |
| Repairs and maintenance | Computer repair, equipment service | 21 |
| Supplies | Materials consumed delivering work (sample mailers, envelopes) | 22 |
| Taxes and licenses | WA B&O tax, city business license, WA annual report fee, employer payroll taxes; NOT federal income tax | 23 |
| Travel | Overnight business trips: airfare, lodging, rental car, local transport while away | 24a |
| Meals | Business meals with a client/prospect/contractor, documented, 50% | 24b |
| Utilities | Business phone line, business internet share | 25 |
| Wages | W-2 employees (not the owner of a sole prop / SMLLC) | 26 |
| Other expenses (Part V) | Software/SaaS, cloud hosting, domains, bank fees, merchant/Stripe fees, dues and subscriptions, education and training, postage machine rental | 27b |
| Business use of home | Simplified $5/sq ft up to 300 sq ft, or actual method (Form 8829) | 30 |

### 3.4 Non-P&L (balance sheet) buckets

| Bucket | Examples | Effect |
|---|---|---|
| Transfer | Checking → savings, bank → card payment, Stripe payout | none |
| Owner draw | Personal purchases from business accounts, transfers to Brennan | equity, not an expense |
| Owner contribution | Brennan funding the business, business costs paid personally | equity |
| Loan proceeds / principal | SBA/LOC draws, principal repayments | liability; only interest is an expense |
| Sales tax collected / remitted | WA retail sales tax on taxable sales (5.3) | liability |
| Security deposits | Office deposit | asset |
| Equipment (capitalized) | Items over the de minimis amount | asset → depreciation |

---

## 4. Receipt / transaction categorization decision tree

Run top to bottom. Stop at the first match.

1. **Duplicate?** Same date ± 3 days, same amount, same vendor already posted or matched (or a Stripe projection exists). → Mark as duplicate candidate; do not post.
2. **Movement between own accounts?** Transfer, card payment, Stripe/PayPal/Square payout. → Transfer.
3. **Loan?** Proceeds → liability. Payment → split principal (liability) vs interest (16c) using the lender statement; no statement → ask.
4. **Owner money?** Transfer to Brennan / payment to a personal card → owner draw (personal accounts are not in the app, so these show up only as outflows from business accounts). Brennan paying a business cost personally → expense + owner contribution.
5. **Tax payment?** IRS/EFTPS/estimated tax → owner draw (federal income tax is never Sch C). WA DOR excise return → split B&O tax (line 23) vs sales tax remitted (liability) using the return; no return → ask.
6. **Refund / credit / chargeback?** Vendor refund → negative in the original category. Client refund → line 2.
7. **Brennan's rule or learned rule matches with high confidence?** → Apply it (section 9). Show "learned: n of m, last seen <date>".
8. **Personal-looking?** Groceries, streaming, gym, clothing, medical, personal Amazon, Venmo to friends. All app accounts are business, so this is an exception: owner draw candidate, ask. Never deduct a personal-looking item by default.
9. **Client job cost?** Ties to a client campaign (printer, postage for a client drop, list buy, client ad spend, freelancer on a job). → Cost of client campaigns with `allocation: client`, `clientId`, `jobId`.
10. **Own marketing?** Promotes Gorilla Works itself. → Advertising (8).
11. **Overhead by type** → section 3.3 table.
12. **Capital item?** Single item/invoice over $2,500 (no AFS) → capitalize or flag for §179/bonus; ≤ $2,500 → expense under the de minimis safe harbor **if** the annual election is made on the return (the election is open: flag it). (Notice 2015-82; Treas. Reg. 1.263(a)-1(f))
13. **Mixed receipt?** Lines belong to different categories → split by receipt lines (`/receipts/{id}/post-mixed`); preserve tax-inclusive line costs; sales tax on the receipt is part of the cost, not a second expense (Finance API reference, receipt posting).
14. **Still unsure** → review queue with best guess, reason, and the one question that would settle it.

### 4.1 Agency examples (illustrative vendors; categories are defaults)

| Bank/receipt description (sample) | Default treatment | Why |
|---|---|---|
| `USPS PO 5410 KIRKLAND` $612.40, memo "Acme Roofing EDDM drop" | Cost of client campaigns: Postage, allocation client, client Acme Roofing | client mailing |
| `USPS.COM CLICKNSHIP` $9.85 | Office expense (18) | own admin mail |
| `STAMPS.COM` monthly fee | Other expenses: software/postage service (27b) | subscription fee |
| Printer invoice "5,000 6x9 postcards – Smith Fencing" | Cost of client campaigns: Printing, client | client job |
| `FACEBK *ADS` for GW's own lead-gen campaign | Advertising (8) | own marketing |
| `GOOGLE *ADS` charged on agency card for a client's campaign | Cost of client campaigns: Client media, client | client media buy |
| `STRIPE PAYOUT` | Transfer | payout, not revenue |
| `STRIPE FEE` / fee inside a charge | Merchant fees (27b, or 10 if the app category maps there) | processor fee |
| `CANVA`, `ADOBE`, `SEMRUSH`, `NOTION`, `GOOGLE *WORKSPACE` | Software and subscriptions (27b) | SaaS |
| `GODADDY` / `NAMECHEAP` domain renewal | Software/web (27b) [or 8 if Brennan uses Advertising for web] | his history wins |
| `UPWORK` / `FIVERR` designer | Contract labor (11); platform reports, usually no 1099-NEC from GW | platform |
| Zelle to an individual "logo design" | Contract labor (11); **1099 tracking** (section 8) | non-card payment |
| `LINKEDIN PREMIUM` | Dues and subscriptions (27b) | business networking |
| `WEWORK` / coworking day pass | Rent – property (20b) | office |
| Lunch with a roofing prospect, receipt notes attendee + purpose | Meals (24b), 50% deductible | business meal |
| Starbucks alone | Owner draw / personal | no business contact |
| Seahawks tickets with a client | Entertainment: 0% deductible; record as nondeductible | IRC 274(a) |
| Holiday gift baskets to 10 clients at $60 each | Gifts: deductible $25 per recipient per year; record excess as nondeductible | IRC 274(b) |
| `WA DEPT OF REVENUE` | Split B&O (23) vs sales tax remitted (liability) | needs the return |
| `IRS USATAXPYMT` | Owner draw (income tax) | never Sch C |
| `AMAZON MKTPLACE` no receipt | Review queue; ask for the receipt (business account, so presumed business, but the category needs the items; personal items → owner draw) | needs receipt |
| `AMAZON` receipt: printer toner + kids' shoes | Split: toner → Office (18); shoes → owner draw | mixed |
| `DELL` laptop $1,899 | Equipment ≤ $2,500 → expense under de minimis (if elected) or capitalize; flag | Notice 2015-82 |
| `VERIZON` single phone, business+personal | Utilities (25) business share only; ask the % once, then reuse | mixed use |
| `CHASE CARD AUTOPAY` from business checking | Transfer (paying the business card) / owner draw if it pays a personal card | OA step 2 |
| `SBA EIDL PMT` | Split principal vs interest using the lender statement | loan |
| `HISCOX` professional liability | Insurance (15) | business insurance |
| `GUSTO` | Wages (26) + employer taxes (23); fees 27b | payroll |
| `QUICKBOOKS` / bookkeeping software | Other (27b) | software |
| Tax preparer invoice for business + personal return | Split: business part → Legal/pro (17); personal part → owner draw | OA professional services |
| `SHELL` fuel | Only on actual-cost vehicle method, business %; standard mileage already includes fuel | OA vehicle |
| Client prepayment "Spring EDDM campaign" (covers design, print, postage) | Agency services income, full amount, when received; tag client/job | Brennan's practice, 5.1 |

---

## 5. Agency-specific hard cases

### 5.1 Client payments and campaign costs (Brennan's practice, Nov 23, 2026)

Brennan: clients "pay me for everything up front and then i charge my expenses... they pay upfront as agency services. the cost isn't parsed out."

- **Income:** book each client payment **in full** as **Agency services income** on the date received (cash basis: income when received, Pub 538). Tag `clientId`/`jobId`. Do not split out a "reimbursement" or "postage" portion, and do not create a reimbursement income line.
- **Costs:** printing, postage, lists, mail house and client ad buys are **separate expenses on the date paid**, category Cost of client campaigns, `allocation: client`, same `clientId`/`jobId`. Never net them against the client payment.
- **Job margin** = client payments received for the job minus the job's tagged costs. Report it; don't book it.
- **Prepaid but not yet spent:** on cash basis the prepayment is still income when received, even if the campaign mails next month or next year. A December prepayment with January costs lands in two tax years; say so in the close report and do not move either entry.
- **Client pays a vendor directly** (client's own postage permit or printer account): nothing enters GW's books for that cost.
- **Washington B&O:** B&O is on **gross** receipts, so the full client payment is the measure. WA DOR says ad agencies generally cannot exclude client advances or reimbursements anyway unless a strict three-part agent test is met (WA DOR, "Advertising agencies – requirements for excluding advances and reimbursements"). Because GW does not parse costs out, treat the full payment as Service and Other Activities gross income for the excise return inputs.
- **Direct mail postage (open default):** WA allows a B&O deduction (RCW 82.04.4272) and a retail sales tax exclusion (RCW 82.08.807) for direct mail delivery charges **only when separately stated on the invoice**. GW's invoices do not parse costs out, so the default is no deduction; note it once as a possible saving for Brennan to decide on, not every month.

### 5.2 Ad spend: own vs client

Ask "who does the ad promote?" GW → line 8. A client → cost of client campaigns with the client tagged. Same vendor (Meta, Google) can be both; the learned table must key on account/memo, not vendor alone, when Brennan's history shows both uses.

### 5.3 Washington taxes (GW is in Kirkland, WA)

- WA has no state income tax; it levies **B&O tax on gross receipts**. Service and Other Activities rate 1.5% for 2026 if prior-year income in that class was under $1,000,000; small business credit can remove it at low volume (OA wa-bo-tax, citing RCW 82.04.290 and 82.04.4451). B&O tax paid is a line 23 expense.
- **Printing bought by an ad agency** for its own or its clients' use (not resold) is a retail sale subject to WA retail sales tax (WAC 458-20-144(4)(b)). If a printer charged no sales tax, flag a possible **use tax** question for Brennan (open).
- Whether GW must collect sales tax on what it bills depends on what it sells (pure advertising services vs printed matter resold vs mailing services). WA DOR has treated combined print-and-mail as retailing in at least one determination (Det. No. 18-0146). **Never decide this; flag it.**

### 5.4 Meals, entertainment, gifts

- Meals with a documented business purpose and attendee: 50% (IRC 274(n)). Record the full amount in Meals and note "50% deductible"; let the tax software apply the limit unless Brennan's app category is set up as "deductible portion".
- Entertainment (tickets, golf, concerts): 0% (IRC 274(a)). Keep a separate nondeductible category so the books still reconcile.
- Gifts: $25 per recipient per year (IRC 274(b)).
- Substantiation for meals/travel/gifts: amount, date, place, business purpose, business relationship (IRC 274(d)). Missing → ask for it; do not invent attendees or purposes.

### 5.5 Home office and vehicle

- Home office: regular and exclusive use; simplified method $5 per sq ft, max 300 sq ft (IRS simplified option page). It is a tax-return computation, not a monthly bookkeeping entry; do not book personal rent/mortgage as an expense.
- Vehicle: needs a contemporaneous mileage log (date, destination, purpose, miles). Without a log, flag. Commuting is never deductible. Business parking and tolls are deductible on top of the standard rate (OA vehicle rules; IRS mileage page).

### 5.6 Owner's personal items that are NOT business expenses for an SMLLC/sole prop
GW's app has no personal accounts; these appear only if paid from a business account, and then they are owner draws.
Owner health insurance, owner retirement contributions, federal/state income tax, personal Netflix/gym/groceries → owner draw (health insurance and retirement go to Form 1040 schedules, not Schedule C). (OA us-sole-prop-bookkeeping)

---

## 6. Records and receipts

- Keep receipts/invoices for every expense; IRC 274(d) items need the substantiation above. Attach the file to the receipt record in the app (`/receipts/upload-url` → PUT → `/extract` → review → post).
- Keep records at least **3 years** from filing (generally), **6 years** if income is underreported by more than 25%, **7 years** for bad debt/worthless securities claims, **employment tax records 4 years**, asset records until the period of limitations for the year of disposal ends. (IRS "How long should I keep records?")
- W-9 on file for every contractor before first payment (see 8).
- Never derive a missing paid date from an upload/creation timestamp (Finance API reference).

---

## 7. Month-end close checklist

Run within the first 5 business days of the next month (OA month-end-close). Output a close report; change nothing in the app without Brennan's approval of the batch.

1. **Pull** the month: `/bank/transactions` per account, `/expenses`, `/income`, `/receipts?status=in_review` and `uploaded`, `/financials/journal-transactions`, `/stripe/status` (pending items).
2. **Completeness:** every account has a confirmed statement for the month (`/bank/statements`). If one is missing, that account is reported as **not closed** (no reconciled balance is claimed) and the statement is requested.
3. **Categorize** every uncategorized line via section 4; anything below high confidence goes to the review queue.
4. **Match** receipts and ledger entries to bank lines (`/candidates`, then match only with evidenced date/amount agreement).
5. **Duplicates and anomalies:** same vendor/amount twice, amounts > 2× the vendor's usual, new vendors, round-number transfers.
6. **Transfers and card payments** both sides present and excluded from the P&L.
7. **Reconcile** each account: statement ending balance vs book balance (`/bank/statements/{id}/reconciliation`). Difference must be $0 or explained line by line. Common causes: pending items, fees not imported, split or duplicate entries.
8. **Job costs:** every campaign cost tagged to a client/job; list untagged campaign costs and jobs whose costs exceed the prepayment received.
9. **AR/AP aging (memo only):** unpaid invoices and bills, not on the cash P&L.
10. **Stripe:** gross charges = payouts + fees + refunds ± timing; pending Stripe review items listed.
11. **1099 tracker** updated (section 8).
12. **Sales tax / B&O:** gross receipts by WA classification for the excise return; postage separately stated?
13. **Reports:** `/financials/income-statement`, `/financials/cash-flow-statement`, `/financials/pl-drilldown` for the month; compare to prior month and same month last year; explain swings > 20%.
14. **Review queue** to Brennan: each item with best guess, reason, and one question.
15. **Learned rules refresh** with his answers (section 9.6).

Close report format:

```
MONTH-END CLOSE — <Month YYYY> (cash basis)
Accounts reconciled: <n>/<n> (differences: $0 or listed)
Lines categorized: <n> | by Brennan's rules <n> | learned <n> | defaults <n> | in review <n>
Income $X | Expenses $Y | Net $Z  (from the app's income statement)
Flags: duplicates <n>, unbilled client costs <n>, missing receipts <n>, 1099 watch <n>
Questions for Brennan: 1) ... 2) ...
```

---

## 8. 1099-NEC contractor tracking

- File Form 1099-NEC for each **non-employee paid $2,000 or more** for services in the year, **for payments made after December 31, 2025** (was $600). Indexed for inflation from 2027. (Instructions for Forms 1099-MISC and 1099-NEC, Rev. December 2026; Pub 1099 (2026))
- Attorneys: reportable at the same threshold even if incorporated.
- Payments by **credit card or through a payment settlement entity** (PayPal goods-and-services, Stripe, Upwork/Fiverr) are reported by the processor on 1099-K and are left off 1099-NEC. Zelle, ACH, wire, check and cash are reportable by GW. (i1099mec)
- Generally exempt: payments to C/S corporations (except attorneys), payments for merchandise, freight, telephone.
- Track per payee: legal name, W-9 on file (Y/N), entity type, payment method, YTD total, status (REPORTABLE ≥ $2,000; WATCH $1,500 to $1,999 [GW default watch band]; below). Due to recipients and IRS by January 31 (moved to the next business day on a weekend). The skill **prepares the list; it never files**.
- No W-9 → flag before the next payment (backup withholding applies to reportable payments without a TIN).

---

## 9. Learn from Brennan's past categorizations

Goal: copy how **Brennan** categorizes, then apply it to new transactions, asking when unsure.

### 9.1 Access and safety
- Credential: a `gwf_` API key in the runner's encrypted credential store, sent only as `Authorization: Bearer` to the same origin. Never print, echo, log, or store it in files, the store, or the repo. Base URL from Grok Bot's setup.
- Start with `GET /context` (contract hash, capabilities) and `GET /settings` (confirm `accountingMethod` is cash).
- Rate limit 60 requests/minute per key; honor `Retry-After` on 429. Every mutation needs a unique `Idempotency-Key` (16 to 128 chars). Do not blindly retry 409 accounting conflicts.
- **Suggest, approve, then post** (Brennan, Nov 23, 2026: "You may post them in the app after we approve each batch after you suggest categories"). History pulls are read-only. Writes (categorize, post, create/patch categories or rules, match, exclude) happen only for a batch Brennan has approved, exactly as approved. One exception: storing an emailed receipt as an **unposted draft** (upload, extract) before approval is allowed because it creates no ledger entry (section 13.6). Never `autoPost: true` without his explicit OK. Never delete; deactivate categories instead of deleting. Never touch Stripe connect/disconnect, API keys, or auth (human-only anyway).

### 9.2 Pull the history (all dates)
| Call | Why |
|---|---|
| `GET /categories`, `GET /categories/tax-lines` | His category names, Schedule C mapping, `needsReview` flags |
| `GET /transaction-rules` | Rules he already wrote (strongest signal) |
| `GET /expenses?dateFrom=<earliest>&dateTo=<today>` | Vendor, description, category, subcategory, allocation, client/job, payment method |
| `GET /income?...` | Income categories, payer → client patterns |
| `GET /receipts?status=posted` then `GET /receipts/{id}` | Line items: how he splits mixed receipts |
| `GET /financials/journal-transactions?dateFrom&dateTo` | Full posted journal incl. Stripe |
| `GET /bank/accounts`, `GET /bank/transactions?accountId=` | Raw bank descriptions, exclusions (= transfers/personal he removed) |
| `GET /stripe/client-rules` | Payer name → client mapping |
| `POST /receipts/vendor-lookup` (no ledger change, but requires an `Idempotency-Key`) | App's own suggestion and confidence for a vendor; a tie-breaker, not authority |
| `GET /transaction-rules/candidates?source=bank` (and `receipt`) | Uncategorized items waiting for a rule |

Treat entries as **his manual decisions** only if they were set manually (expenses he entered/edited, receipts he posted, `clientAssignment: manual`). Entries produced by rules are evidence of the rule, not extra votes.

### 9.3 Normalize vendors
Uppercase; strip processor prefixes (`SQ *`, `TST*`, `PAYPAL *`, `PP*`, `POS`, `DEBIT CARD PURCHASE`, `ACH`, `CHECKCARD`), store numbers, trailing city/state, dates, card digits, reference numbers, `.COM` variants. Keep a raw → key map so the rule can be shown with real examples. Merge obvious aliases (`FACEBK`, `META`, `FB.ME`) only when his categories agree.

### 9.4 Build the rule table
For each vendor key (and, when his history splits by memo/amount, vendor key + memo token or amount band):
- `n` = manual decisions; `top` = most common category (+ subcategory, allocation, client if consistent); `share` = top/n; `first_seen`, `last_seen`; `last3` = categories of the 3 most recent.
- **Confidence**
  - **High**: n ≥ 3 and share ≥ 90%, and the last 3 agree.
  - **Medium**: n ≥ 2 and share ≥ 75%; or n = 1 within the last 6 months.
  - **Low**: anything else, or two categories each ≥ 25% with no separating memo/amount pattern.
  [GW default thresholds, tune with Brennan]
- **Drift**: if his category for a vendor changed and stayed changed (the last 3 agree on the new one), use the new one from its first date and note "changed on <date>". Do not re-categorize old periods unless he asks.
- **Splits**: if his posted mixed receipts for a vendor show a stable split (same categories, percentages within ±5 points across ≥ 3 receipts), store the split pattern; otherwise "split by receipt lines, ask".
- **Allocation/client**: record when a vendor is always client-allocated, or the client follows a memo token (e.g., a client name in the memo).
- **Tax-law check**: if his habit conflicts with section 5 (personal item as expense, income tax as expense, client postage on Advertising), mark `conflict` and ask once; his answer becomes the rule.

### 9.5 Apply to new transactions
1. His explicit rules (app `transaction-rules`; preview with `POST /transaction-rules/preview`, which needs an `Idempotency-Key` but posts nothing).
2. Learned **high** → propose as "learned (n/m, last <date>)".
3. Learned **medium** → propose but put in review with the alternative.
4. **Low** / new vendor → decision tree default, marked "default, unconfirmed", in review.
5. Never let a learned rule override a duplicate/transfer/owner-draw/loan check (steps 1 to 6 of the tree).
6. **Batch flow** (Brennan, Nov 23, 2026):
   1. Suggest: send the batch as the section 11 table, with basis and confidence for every line and the review items separate.
   2. Approve: Brennan approves, or corrects lines. Log each correction in `finance/corrections-log.md` and update the learned rule.
   3. Post: write exactly the approved lines (create/patch expenses or income, post receipts, match bank lines) with a fresh `Idempotency-Key` per mutation. Lines he did not approve stay unposted. A 409 accounting conflict is reported, not retried blindly.
   4. Confirm: re-read the affected lists and report what posted, what failed, and the request IDs for failures.
7. Offer to turn stable high-confidence learned rules into app transaction rules (`autoPost: false`), one list for his approval.

### 9.6 Store the learned rules PRIVATELY
- Location: the private GW store, **`/cursor/stores/store-64a113bb-11d0-4ce0-98d5-988465b287d9/finance/`**:
  - `learned-rules.json` (machine table: key, patterns, category, subcategory, taxLineCode, allocation, client, n, share, first/last seen, confidence, notes, conflict)
  - `learned-rules.md` (readable summary for Brennan)
  - `corrections-log.md` (date, item, old → new, Brennan's reason)
- **Never** put transaction data, vendor amounts, account numbers, client names from his books, or the learned table in the public `gw-skills` repo or any public place. Examples in the repo use made-up data only.
- Refresh: rebuild monthly at close, and immediately apply any correction he makes (log it, bump that rule).

### 9.7 Learned table format (readable)

```
| Vendor key | Category (sub) | Alloc | n | Share | Last seen | Conf | Notes |
| USPS | Campaign postage | client | 14 | 93% | 2026-10-28 | High | client from memo |
| FACEBK ADS | Advertising | operational | 6 | 100% | 2026-11-02 | High | own ads only |
| AMAZON | split | — | 9 | 44% | 2026-11-10 | Low | ask per receipt |
```
(sample rows, made-up)

---

## 10. Guardrails (full list)

1. Never invent an amount, date, vendor, attendee, business purpose, mileage, or receipt. Missing → ask.
2. Never file, pay, submit, e-file, or sign anything (1099s, B&O/excise returns, estimated taxes, Form 1040). Prepare lists and drafts only.
3. Suggest per batch; categorize, post or match in the finance app only the batch Brennan approved, exactly as approved (unposted receipt drafts are allowed before approval, section 13.6); no `autoPost` without explicit OK; no deletes.
4. Keep personal and business separate; the app holds business accounts only, so a personal-looking charge is an owner draw candidate to ask about.
5. Transfers, card payments, loan principal, owner draws, owner contributions, income tax payments, Stripe payouts and sales tax remitted are **not** expenses or income.
6. Refunds net against the original category.
7. Every expense needs evidence; flag missing receipts, never fabricate one.
8. Brennan's history wins over defaults; tax-law conflicts are flagged, not copied and not silently "fixed".
9. The API key is a secret: never shown, logged or stored outside the credential store.
10. Learned rules and real data live only in the private store, never in the public repo.
11. Not tax advice. Resolved: entity (SMLLC, Schedule C), chart (section 3), client payments (full income, costs separate). Still open defaults: COGS vs expense, WA sales tax collection and use tax, de minimis election, home office method; state the default used and flag it.
13. Client payments are never split into reimbursements or netted against costs (section 5.1).
14. Receipt emails are read and labeled only: never replied to, forwarded, trashed or archived. Unpaid invoices are bills, not expenses, until paid (section 13).
12. Figures (mileage rates, thresholds) change; re-check the cited source each tax year.

---

## 11. Output formats

**Categorization batch**

```
| # | Date | Description | Amount | Proposed category (Sch C) | Alloc/client | Basis | Conf | Question |
```
Basis ∈ {Brennan rule, learned n/m, default, Brennan said}. Then: counts by basis; review items; anything not P&L (transfers/draws) listed separately.

**Review queue item**: what it is, best guess, why, the one question.

---

## 12. Test prompts (skill-creator method; made-up data only)

1. "Categorize these 10 receipts for Gorilla Works" (mix: USPS client EDDM postage, own Facebook ads, Stripe payout, Canva, Zelle to a freelancer, client lunch, Seahawks tickets with a client, personal Amazon, Chase card autopay, WA DOR payment). Pass if: payout and card autopay → transfer; Zelle → contract labor + 1099 watch; tickets 0%; lunch 50% with substantiation request; client postage not on line 8; personal → owner draw; WA DOR split asked; nothing invented.
2. "Close October." Pass if: follows section 7 order, reconciles each account to statement balances, lists untagged campaign costs, 1099 tracker, B&O inputs, review queue, changes nothing without approval.
3. "Client prepaid $3,000 on Sept 28 for an October mailing; we paid USPS $840 and the printer $1,100 in October. How do I book it?" Pass if: $3,000 agency services income on Sept 28 in full (no reimbursement split); $840 and $1,100 Cost of client campaigns in October, tagged to the client/job; no netting; job margin reported, not booked; B&O on the gross $3,000; separately-stated postage noted once as an open default.
5. "Log today's receipts from the grok@ inbox." (sample: a paid printer invoice PDF, a USPS email receipt with no attachment, an unpaid SaaS invoice, a promo email, a duplicate forwarded receipt) Pass if: `to:grok@` scoped search; printer and USPS uploaded as drafts (USPS body rendered to PDF); unpaid invoice logged as open bill, not expense; promo logged not-receipt; duplicate skipped by message id/vendor-amount-date; nothing posted before approval; no reply/forward; log updated; label applied.
4. "Learn how I categorize from the finance app." Pass if: read-only pulls in 9.2, normalization, confidence table, drift and splits handled, stored in the private store, no data in the repo, proposes app rules with autoPost false.

---

## 13. Receipt intake from email (Brennan, Nov 23, 2026)

Brennan: "my grok@gorillaworksmarketing.com email gmail address will get receipts that i need you to also add to the finance app."

### 13.1 Source and access
- **Inbox:** receipts sent to **grok@gorillaworksmarketing.com**, read through the Gmail connector.
- **Connector check (Nov 23, 2026):** the Gmail connector is signed in as **hello@gorillaworksmarketing.com**. grok@ is not a send-as alias there, but mail addressed to grok@ does show up in that mailbox (a `to:grok@gorillaworksmarketing.com` search returns matches). So always scope searches with `to:grok@gorillaworksmarketing.com` (or `deliveredto:`). If a run finds nothing addressed to grok@, report "grok@ mail not reaching the connected mailbox" instead of guessing. Brennan may later connect grok@ directly; then drop the `to:` scope.
- **Read tools only, plus labels:** `search_emails`, `read_email`, `get_thread`, attachments via DownloadFile (`source.fileId` = `<messageId>/<attachmentId>`) onto the box. Labels (`create_label`, `update_email_labels`) are the only mailbox changes allowed.
- **Never** reply to, forward, draft from, trash, archive, spam-mark or unsubscribe from a receipt email. Never send anything to a vendor.

### 13.2 Find candidate emails (daily)
Base query, newest first, since the last run date in the processed log (first run: last 90 days, then ask Brennan whether to go further back):

```
to:grok@gorillaworksmarketing.com -label:Receipts/Logged after:<YYYY/MM/DD>
  (receipt OR invoice OR "order confirmation" OR "your order" OR "payment received" OR "payment confirmation" OR "thank you for your payment" OR "paid" OR "billing" OR "subscription" OR "renewal" OR "refund" OR has:attachment filename:pdf OR filename:jpg OR filename:png OR filename:heic)
```

Add `from:` terms for vendors that already appear in his learned rules or app expenses (for example postage, printing, SaaS and ad platforms). Read each candidate's body and attachment names before deciding.

### 13.3 Classify each email first
| Email is | Treatment |
|---|---|
| Paid receipt / payment confirmation / paid invoice ("paid", "payment received", card charged, amount and date shown) | Intake (13.4) |
| Refund or credit confirmation | Intake as a refund: negative against the original category (section 2) |
| **Invoice or bill still to be paid** (due date, "amount due", "pay now") | **Not an expense on cash basis until paid.** Log it as an open bill in the processed log (vendor, invoice number, due date) and in the month-end AP memo. Intake it later when the payment shows (bank line or paid receipt). |
| Order confirmation with no charge yet, quote, estimate, renewal reminder, trial notice, failed-payment notice | Not a receipt; log as `not-receipt` with the reason |
| Shipping/delivery notice, marketing/promo, newsletter | Not a receipt; log as `not-receipt`, no label needed beyond the processed log |
| Client payment notice (Stripe, check, ACH from a client) | Income evidence: Agency services income per 5.1 (Stripe income usually already exists in the app via Stripe sync; check before adding anything) |
| Unclear | Review queue with the question |

### 13.4 Extract (never invent)
From the attachment first, else the email body: **vendor, paid date, total, sales tax, payment method (card last 4 if shown), invoice/order number, line items, client/job hints in the memo.** A field that is not on the document stays **null and flagged**; never infer a paid date from the email's sent time unless the email itself says it was charged that day, and never infer amounts. Currency other than USD → flag.

### 13.5 Dedupe (before anything is written)
1. **Gmail message id** already in `finance/receipts-processed-log.md` → skip.
2. Same **vendor + total + paid date (±3 days)** (or same invoice/order number) already in the log, in `GET /receipts` (any status, including `/receipts/drafts`), or in `GET /expenses` → duplicate candidate; skip and note.
3. Same amount/date in `GET /bank/transactions` → not a duplicate; it is the **bank line this receipt evidences**. Note the bank transaction id for matching after posting.
4. Forwarded copies and threads with several messages: one receipt per charge, not per email.
The app has no receipt-duplicate endpoint; bank lines carry `fingerprint`/`duplicateOfId`, and receipt posting is built to avoid duplicate cash entries, but the bot still dedupes first.

### 13.6 Add to the finance app: what happens before vs after Brennan's approval
**Choice:** the raw receipt is stored in the app as an **unposted draft** before approval; categorizing and posting wait for approval.
- **Why this is allowed:** in the app a receipt record has `status` `uploaded` → `in_review` → `posted`. Only `POST /receipts/{id}/post` (or `/post-income`, `/post-mixed`) creates ledger entries. An uploaded or extracted receipt is evidence storage that appears in `GET /receipts/drafts`, not a P&L post, so it does not break the Nov 23 rule ("You may post them in the app after we approve each batch after you suggest categories"). It also keeps the file safe in the app and lets the app's own reader propose fields.
- **Before approval (allowed):**
  1. `POST /receipts/upload-url` with `{ "filename": "<vendor>-<YYYY-MM-DD>.pdf", "contentType": "<real MIME type>" }` (+ optional `clientId`, `jobId`) and an `Idempotency-Key`. Returns `uploadUrl`, `fileUrl`, `receiptId`. Non-replayable: never auto-retry; if uncertain, check the receipt list first.
  2. `PUT` the bytes to `uploadUrl` with the file's content type and **no** finance Authorization header.
  3. `POST /receipts/{id}/extract` (optional body `rawOcrText`: all numbered PDF pages, OCR for scanned pages) with a new key. Non-replayable; never auto-retry.
  4. `GET /receipts/{id}` and compare the app's extraction with your own (13.4). Disagreements go in the batch table.
  - **Email with no attachment** (body-only receipt): render the email body to a PDF on the box and upload that, so the app holds a file; pass the body text as `rawOcrText`.
  - `POST /receipts` (`ReceiptInput`: `filename` required; `fileUrl`, `rawOcrText`, `vendor`, `cashPaidDate`, `total`, `salesTax`, `clientId`, `jobId`) exists to create a record after an upload; use it only if the upload-url step did not already create the receipt.
- **After Brennan approves the batch (section 9.5):**
  5. `PATCH /receipts/{id}` with the approved facts (`vendor`, `cashPaidDate`, `paymentMethod`, `total`, `salesTax`, `direction`, `clientId`, `jobId`, `lineItems` with `category`, `subcategory`, `allocation`, `kind`) and `reviewedFlags` for fields checked against the document.
  6. `POST /receipts/{id}/post` (`PostReceiptInput`, with `expectedUpdatedAt`) for a single-category or multi-line purchase; `/post-mixed` only with separately evidenced cash events; `/post-income` for income evidence. Keep tax-inclusive line costs; receipt-level sales tax is evidence, not a second cost line.
  7. Link to the bank line: `GET /bank/transactions/{id}/candidates`, then `PUT /bank/transactions/{id}/match` with `{ "ledgerType": "expense", "ledgerId": <expense id created by the post> }`, only when date and amount agree.
- **Not approved / corrected:** leave the draft unposted; apply his corrections; log them (`corrections-log.md`). Never delete a draft without his OK.
- **File types and size:** the API docs do not list allowed file types or a size limit (the documented example is `application/pdf`). Send the attachment's real MIME type (PDF, JPEG, PNG; convert HEIC to JPEG or PDF on the box first). If the API rejects a file (400/413), report it, don't retry with a different file.

### 13.7 Propose the category
Run the section 4 tree on each receipt (and section 9 learned rules). The intake batch uses the section 11 table plus two columns: **Gmail message id** and **app receipt id**. Open bills and not-receipts are listed separately.

### 13.8 Track processed emails
- **Private log (source of truth):** `finance/receipts-processed-log.md` in the private store: date run, Gmail message id, from, subject (no amounts beyond what the batch needs), classification (receipt / refund / open bill / not-receipt / duplicate), app receipt id, status (draft, approved, posted, matched, rejected). Never copy it to the public repo.
- **Gmail label:** create `Receipts/Logged` once (`create_label`) and add it (`update_email_labels`) to each email whose receipt is in the app as a draft or posted; optionally `Receipts/Not-a-receipt` for skipped ones. Labels never replace the log. Do not remove other labels or mark read/unread.

### 13.9 Cadence
Daily, as a routine the finance bot's owner creates (for example every morning at 7:00 AM Pacific): search → classify → dedupe → upload drafts → send one batch for approval. Post only after Brennan approves. If nothing new, report "no new receipts" in one line.

## 14. Sources

| Source | Used for | URL |
|---|---|---|
| IRS Pub 538 (Rev. Jan 2022), Accounting Periods and Methods | Cash method, constructive receipt, expense paid in advance, 12-month rule | https://www.irs.gov/publications/p538 |
| IRS Pub 334 (for 2025 returns, latest on site), Tax Guide for Small Business | Schedule C expenses, cost of goods sold (ch. 6) | https://www.irs.gov/pub/irs-pdf/p334.pdf |
| Schedule C (Form 1040) 2026 | Line map (via OA us-sole-prop-bookkeeping) | https://www.irs.gov/pub/irs-pdf/f1040sc.pdf |
| Treas. Reg. 1.461-1(a)(1) | Deduct in year paid | https://www.law.cornell.edu/cfr/text/26/1.461-1 |
| Rev. Rul. 78-38 / 78-39 | Bank credit card charge = payment on charge date | https://bradfordtaxinstitute.com/Endnotes/Rev_Rul_78-39.pdf |
| IRS Tangible property regulations page; Notice 2015-82; Treas. Reg. 1.263(a)-1(f) | De minimis $2,500 per invoice/item (no AFS) | https://www.irs.gov/businesses/small-businesses-self-employed/tangible-property-final-regulations |
| IRS Standard mileage rates page | 2026: 72.5¢ (Jan–Jun), 76¢ (Jul–Dec) | https://www.irs.gov/tax-professionals/standard-mileage-rates |
| IRS Simplified option for home office | $5/sq ft, max 300 sq ft | https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction |
| IRS How long should I keep records? | 3/4/6/7-year rules | https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records |
| Instructions for Forms 1099-MISC and 1099-NEC (Rev. Dec 2026); Pub 1099 (2026) | $2,000 threshold for payments after 2025; 1099-K exclusion; corporations | https://www.irs.gov/pub/irs-pdf/i1099mec.pdf |
| 26 U.S.C. 274 | Entertainment 0%, gifts $25, substantiation, meals 50% | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec274.htm |
| WA DOR: Advertising agencies – excluding advances and reimbursements | B&O treatment of client reimbursements | https://dor.wa.gov/forms-publications/publications-subject/tax-topics/advertising-agencies-requirements-excluding-advances-and-reimbursements-gross-income |
| WAC 458-20-144 (Printing industry) | Printing sold to ad agencies is a retail sale | https://app.leg.wa.gov/wac/default.aspx?cite=458-20-144 |
| RCW 82.04.4272; WA 36 WTD 089 (reconsideration of Det. No. 15-0093) | Direct mail delivery charges deduction when separately stated | https://apps.leg.wa.gov/rcw/default.aspx?cite=82.04.4272 |
| WA Det. No. 18-0146 (38 WTD 224) | Print-and-mail treated as retailing in that case | https://dor.wa.gov/sites/default/files/2021-10/38WTD224.pdf |
| OpenAccountants `us-sole-prop-bookkeeping`, `wa-bo-tax`, `bookkeeping-workflow-base` (OA Skills License; adapted, not copied) | Line map, pattern library, Tier 1/2/3 confidence idea, B&O rates | https://github.com/openaccountants/openaccountants |
| Open Accountant skills `smart-categorize`, `month-end-close`, `contractor-tracking`, `smart-split`, Paperclip `bookkeeper` agent (MIT) | Rule-learning loop, close checklist, escalation stance | https://github.com/openaccountant/skills |
| Gorilla Works Marketing Finance API reference (contract 0e651225…), live copy https://rgr-finance.replit.app/api/llms-full.txt (same as local, checked Nov 23, 2026) | Endpoints, safeguards, write rules, receipt upload/extract/post flow | `/api/reference.md`; local `/home/box/rgr-finance/docs/` |

Unconfirmed (re-check): 2026 Schedule C instructions; Pub 334 for 2026 returns not yet posted.
