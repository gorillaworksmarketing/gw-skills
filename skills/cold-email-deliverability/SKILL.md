---
name: cold-email-deliverability
description: >-
  Use when setting up, warming, or monitoring the Gorilla Works cold email
  sending domain and mailboxes, checking whether a draft is safe to send, or
  when bounces, complaints, or replies drop. For GW Email Editor, GW Lead
  Research (list verification), and Grok Bot. Free tools only. Use it even if
  the request just says "why are replies down?".
---
# Cold email deliverability
Detail: blueprints/cold-email.md (Deliverability). Bots never send; Brennan approves sends, domains, and spend.

## Why it matters
One burned domain costs months, so stop-loss beats any meeting target and volume never rises to hit a number.

## Setup
1. **Secondary sending domain**, forwarded to the main site. hello@gorillaworksmarketing.com is never used for cold email.
2. **SPF, DKIM, DMARC** verified (MxToolbox, Google Admin Toolbox CheckMX). Add Google Postmaster Tools.
3. **Two mailboxes** to start; scale by adding mailboxes (2-3 per domain), not volume.
4. **Content defaults:** plain text, no link or image in email 1, company name in the signature not hyperlinked [V6], open and click tracking off, word-level spintax, about 125 words or fewer, opt-out line plus Gorilla Works Marketing, LLC, 13120 NE 85th St Unit 123, Kirkland, WA 98033.
5. Never bulk-send cold from a CRM or marketing tool (HubSpot-type) [V5].

## Warm-up ramp (team.md)
- Weeks 1-2: warm-up only, 5-20 a day with real replies.
- Weeks 3-4: about 20 cold emails per mailbox per day to verified, well-matched leads.
- Then +10 a week toward 40-50. Hold at about 30 until reply and bounce data look healthy [JUDGMENT]. A brand-new domain rests first. Provider ceilings are not targets.

## List hygiene
Verify every address within 7 days of sending (Bulk Email Checker free tier). Flag catch-alls. Suppress unsubscribes, bounces, and "no" replies across every mailbox at once.

## Weekly health check
1. Postmaster and warm-up reputation. 2. Seed test (directional). 3. Pull an inbox with 100+ sends under 1% replies. 4. Auto-responder test: about 80% return, kill under 60%. 5. Keep about 50% spare warmed capacity.

## Thresholds
- **Early warning (review copy, list, and volume):** bounces over 2%, complaints near 0.1%, reply rate under 1% after 300+ sends.
- **Hard pause (stop and tell Brennan):** bounces over 5%, complaints over 0.3%, or a sudden reply drop.

## When results drop, triage in this order
Scope (one inbox or all?), authentication, reputation, list quality, then content last. Bad lists and identical copy are the usual causes, not spam words. Fix: re-verify, recheck DNS, refresh spintax, lower volume. Diagnose the full funnel in order: list, deliverability, copy, then sales (reply to booked) [V7]. Judge each offer arm after about 1,000 sends; no positive reply by then means change the offer, not the domain. For speed add warmed mailboxes (Brennan approves), never push volume.

## Metrics
Bounce, complaint, unsubscribe, and **human** reply rate per inbox (exclude out-of-office and auto-replies; watch OOO spikes) [V6]; booked calls. Opens are not used.

## Later, not now (free-tools budget) [V6]
Redundant inbox sets, mixed providers, matching sender to recipient provider (vendor claim), residential IPs. Log ideas; Brennan decides.

## Learning loop
Weekly with GW Analytics: inbox health first, so copy isn't blamed for deliverability. Log dated changes in the blueprint changelog.

Related: `cold-email-copy`, `cold-email-editing`.
