---
name: cold-email-editing
description: >-
  Use whenever GW Email Editor reviews, edits, scores, or approves a Gorilla
  Works cold email, follow-up, objection reply, positive-reply draft, or nurture
  email before it goes to Brennan. Runs hard fails, Seven Sweeps for email,
  AI-tell removal, CAN-SPAM, offer-arm and claims checks, and a 1-10 panel
  score, then outputs PASS or FAIL with a change log. Use it even if the request
  just says "check these emails".
---
# Cold email editing (GW Email Editor)
Scorecard: blueprints/email-copy-frameworks.md §14 (AI tells §11, CTA §7, follow-ups §8). Rules and offer test: blueprints/cold-email.md. Apply `gw-claims-guardrails`, then `gw-qa-gate`. The editor never sends.

## How to think about it
Generic or AI-sounding drafts go back with notes; good drafts in Brennan's voice get line edits only. If a line is specific, true, and sounds like Brennan, leave it.

## Pass 1: hard fails (any one = FAIL, list the fix)
- A hook without a source URL, or one that is private-feeling or sensitive. Open each URL.
- An offer not worded exactly as one of the four arms (A-D in cold-email.md), or two arms in one sequence. Sample postcard, list preview, teardown, audit, or video offers are unapproved.
- Any other claim, number, or proof not approved (Real Great Roofing's exact quote only). No stamp comparison, guarantee, ROI promise. Write `[NEED: ...]` instead of softening.
- Email 1 names the deliverable or jargon (AI, data modeling, 200+ variables, targeting) instead of the outcome (more jobs).
- A problem the niche isn't already aware of, or one we made up.
- Missing opt-out line or postal address (Gorilla Works Marketing, LLC, 13120 NE 85th St Unit 123, Kirkland, WA 98033). Hyperlinked company name.
- Misleading or fake Re:/Fwd: subject. Any link in email 1. More than one ask. Any em dash.

## Pass 2: Seven Sweeps for email
1. **Clarity:** one idea; 7th-grade level or lower; scannable on a phone.
2. **Voice:** Brennan, peer to peer.
3. **So what:** every line ties to their jobs or money.
4. **Prove it:** each claim backed or cut.
5. **Specificity:** swap in another company's name; if it still works, the hook is thin.
6. **Emotion:** their real pain in one line.
7. **Zero risk:** "yes" claims a free thing via a 15-minute call; "no" is easy.

## Pass 3: AI tells and mechanics
Remove §11 patterns ("quick question", "just checking in", contrast reveals, tidy closers). Check: subject and opener pair; about 125 words or fewer; spintax natural; follow-ups stand alone; 3-4 touches (email 3 new thread); only the hook line varies; one niche per list. **Visual format pending from Brennan;** plain text until then.

## Positive-reply drafts
Thanks, the claimed offer named, two times for the 15-minute call. Nothing else promised. Drafted within 2 minutes; no auto-send until Brennan approves the reply agent.

## Pass 4: panel score
1-10 as the busy fence owner, a deliverability reviewer, a copywriter, and Brennan. PASS needs every score 7+ and an average of 8+. Note why the lowest is low.

## Test hygiene
One variable changed and the hypothesis written. Offer arms first. Flag any call on tiny samples (blueprint minimums).

## Output
Edited email, change log, four scores, PASS or FAIL, held leads. Brennan approves every send.

## Learning loop
Weekly: log repeat fixes in blueprints/cold-email.md. Compare scores to real positive replies and booked calls; if they disagree, recalibrate and note it in the changelog.
