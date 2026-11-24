---
name: notion-shared-rate-limit
description: >-
  Use whenever any Gorilla Works bot reads or writes Notion (Cold Leads queries,
  row creates, patches, or bulk pushes), and whenever Ember's Hunter worker may
  be running: every bot, Ember included, shares one Notion rate limit.
---
# Shared Notion rate limit

Every Gorilla Works bot and Ember use the same Notion integration (Replit Marketing Integration), so they share one Notion rate limit. A burst from one actor can make Ember's already-paid Hunter→Notion save fail with 429, a connection reset, or "allowance unavailable." Incident: 2026-11-24 America/Phoenix; recovery is `hunter-notion-save-recovery`. Other API errors: `api-issue-handling`.

## Rules
1. **One request at a time.** After each Notion call, pause about 350 ms. Notion allows about 3 requests per second **in total** across every bot and Ember, not 3 per bot.
2. **Back off on 429.** Wait the `Retry-After` header (or a conservative backoff if it is missing), then retry the same read, or a write you have re-read and confirmed did not land. Log the status, the wait, and the retry.
3. **Targeted filtered queries, not full scans.** Query by the fields you need (page ID, Status, domain) instead of paginating an entire Cold Leads database when a filtered query will do.
4. **Do not collide with Ember Hunter or with copy/edit work.** When avoidable, never run bulk scans or bulk writes while Ember's Hunter worker is running, or during the copy and edit windows (pipeline steps 8–11):
   - GW Email Copywriter: 7:00 AM, 1:30 PM, 5:30 PM PT (8:00 AM, 2:30 PM, 6:30 PM America/Phoenix in winter).
   - GW Email Editor: 9:30 AM, 3:30 PM, 7:30 PM PT (10:30 AM, 4:30 PM, 8:30 PM America/Phoenix in winter).
   Since 2026-11-24 4:02 PM PT no stage has a daily cap, so each window works every eligible row and can run long; leave a wide margin after each start. Sending stays draft-only. If you know or can see the Hunter worker is processing jobs, wait.
5. **Log request counts.** Each run, record how many Notion requests you made (reads vs writes) and whether you hit a 429, so later collisions are visible.

## Lead Research bulk pushes
Creating many new Cold Leads rows must be batched and paced under these rules so a large intake does not flood the shared limit. Same pacing applies to recovery PATCHes: the 2026-11-24 recovery writes themselves likely overlapped one later held job. Detail: `cold-email-lead-research` and blueprints/cold-email.md.

## Never
- Fire parallel Notion requests, or skip the ~350 ms pause, to go faster.
- Retry a write blindly (`api-issue-handling`).
- Re-run Hunter or spend credits to recover a missed Notion save (`hunter-notion-save-recovery`).
