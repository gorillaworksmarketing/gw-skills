---
name: cold-email-deliverability
description: Use when setting up, warming, or monitoring the Gorilla Works cold email sending domain and mailboxes, or when bounces, complaints, or replies drop. For GW Email Editor (deliverability check), GW Lead Research (list verification), and Grok Bot. Free tools only. Use it even if the request doesn't name the skill.
---
# Cold email deliverability
Detail: blueprints/cold-email.md. Bots never send; Brennan approves sends, domain purchase, and any spend.

## Setup
1. **Secondary domain** (separate domain or mail.<domain>). hello@gorillaworksmarketing.com is never used for cold email. Forwarding the sending domain to the main site is fine.
2. **SPF, DKIM, DMARC** verified with MxToolbox and Google Admin Toolbox CheckMX.
3. **Two mailboxes** to start. Scale by adding mailboxes (2-3 per domain), not volume.
4. **Tracking off** (no open or click tracking). Plain text. Opt-out line plus postal address in every email.
5. Optional: animated Gmail account icon (Brennan does it; 24-48h to show).

## Warm-up ramp (team.md)
- Weeks 1-2: warm-up only, 5-20 a day, real replies and conversation.
- Weeks 3-4: about 20 real cold emails per mailbox per day, verified well-matched leads, bounces under 2%.
- Then +10 a week toward 40-50 per mailbox. Hold at about 30 until reply and bounce data look healthy [JUDGMENT].
- A brand-new domain rests first. Free or manual warm-up is slower; patience beats speed.
- Provider ceilings (Gmail 500/day, Workspace 2,000) are not targets.

## List hygiene
Verify every address right before sending (free checkers, Bulk Email Checker free tier; MxToolbox for the domain). Flag catch-alls. Suppress unsubscribes, bounces, and non-engagers after the sequence.

## Weekly inbox health checks
1. Warm-up reputation. 2. Seed-inbox test (directional only). 3. Per-inbox reply rate: pull any inbox with 100+ sends under 1% replies. 4. Auto-responder test: send to saved auto-repliers; about 80% should arrive, kill under 60%. 5. Keep about 50% spare warmed capacity.

## Stop-loss (pause and tell Brennan)
Bounces over 5%, complaints over 0.3%, or a sudden reply drop (suspect content fingerprinting or spam trap). Then re-verify the list, recheck DNS, vary copy with word-level spintax, lower volume.

## Diagnose in order
Infrastructure, then list, then offer. Judge a campaign only after about 1,000 sends; no positive reply by 1,000 means change the offer.

## Metrics
Bounce, complaint, unsubscribe, reply rate per inbox, demos by UTM. Log dated changes in the blueprint changelog. Weekly review with GW Analytics.

Skills to reference: `cold-email-copy`, `cold-email-lead-research`.
