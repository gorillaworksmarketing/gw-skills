---
name: hunter-notion-save-recovery
description: >-
  Use when Ember Hunter jobs are held or failed on the Notion save, or as step
  0b of Grok Bot's daily 12:30 PM America/Phoenix cold-email check: recover
  already-paid Hunter results into Notion without re-running Hunter.
---
# Hunter Notion save recovery (owner: Grok Bot)

Ember owns the first Hunter→Notion write (pipeline step 7). When that write never happens, a paid result can sit in a held job while the row stays at Email Lookup with empty Hunter fields. Brennan ruled (2026-11-24) that saving those results is Grok Bot's job. Pipeline step 7b; step 0b of the daily 12:30 PM America/Phoenix cold-email check. Pace Notion calls per `notion-shared-rate-limit`. API errors: `api-issue-handling`. Evidence JSON (`save.py`, 2026-11-24): blueprints/cold-email.md. Draft only: never send email.

## Procedure
1. **List.** `GET https://ember-email.replit.app/api/marketing/hunter/workflow` (Bearer `EMBER_API_KEY`; never print the key). Read `jobs` and `totals`. Returns recent owner-scoped jobs; if `totals.held` exceeds held jobs in `jobs`, report the gap (no other list path is documented). Select jobs held or failed on the Notion save (Nov 24: `state`/`phase` = `held`, `notionWriteAttempted` = false, Notion error in `message`: 429/rejected, connection/transport failure, incomplete response, or allowance unavailable). Do not write preflight `held`/`skipped` jobs (Hunter never ran).
2. **Reconcile first.** `POST /api/marketing/hunter/workflow/jobs/{id}/reconcile` (64-character hex id). Path must include `/api/marketing/` (else 404). Receipt-only: never PATCHes or re-runs a paid lookup. On 200, do not also PATCH.
3. **On 409 `HUNTER_NO_WRITE_RECEIPT`** ("No Notion write was attempted... cannot be replayed"): re-read the row. Write only if Status is still `Email Lookup` and Hunter Email Status and Hunter Evidence are empty; otherwise skip.
4. **Write Ember's field format, then read back.**
   - Verified + usable email: `Hunter Email Status` = `Verified`; fill `Hunter Evidence`; set `Hunter Discovered Emails` to empty rich text (discovered addresses go in Evidence); Status = `Ready for Summary`.
   - `Unknown` and no usable email: `Hunter Email Status` = `Unknown — no usable email; retry`; fill Evidence; clear Discovered Emails; Status = `Failed`; prepend Extraction Note `Failed YYYY-MM-DD (Grok Bot): No Hunter email found (Brennan rule Nov 18)` (standing rule), keeping any existing note.
   - Hunter never ran (no result to save): leave the row at Email Lookup for Ember's next scan. Do not write.
5. **Verify.** Re-read: Status, Hunter Email Status, Extraction Note (when Failed), and Evidence JSON must match. Log job id and outcome.

## Hunter Evidence keys
JSON in `Hunter Evidence`, text split at 1,900 characters. Always include `recoveredFromHeldJob`: `{emberJobId, savedBy: "Grok Bot", savedAt, reason}` with `reason` = `Ember job held without a Notion write: ` plus the job's `message`.

Verified: `checkedAt`, `provider` ("hunter"), `checkedEmail` (the usable address), `businessDomain` (row Website, no leading `www.`), `result` ("Verified"), `verification` (`status`, `result`, `score` from that address's check), `verificationUsage`, `discoveryUsage`, `discoveredEmails`, `usableEmails`, `checks`.

Unknown / no usable email: `provider`, `checkedEmail` (""), `businessDomain`, `result` ("Unknown"), empty `verification`, null usage fields, empty `discoveredEmails` / `usableEmails` / `checks`.

## Never
- Re-run Hunter, call `POST /api/marketing/hunter/workflow/run`, or spend credits.
- Write over a row no longer at Email Lookup or that already has Hunter fields.
- Invent an email, or mark Verified when `usableEmails` is empty. No real prospect names or emails in public examples.
