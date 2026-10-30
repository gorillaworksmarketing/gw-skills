---
name: stat-sourcing-and-verification
description: >-
  Trace every statistic to its original primary source (USPS, ANA, Census, BLS)
  and tier it verified / secondary / flagged. Use whenever a post, article,
  brief, or reply will contain a number, when another bot asks for stats, or
  when a stat came from a competitor or aggregator page.
---
# Stat sourcing and verification

Why: one invented or misattributed number can sink trust in the brand and hand traffic or credit to competitors. A short list of true numbers beats a long list of guesses.

## Steps
1. **Collect the claim.** Write down the exact number, what it measures, and where you saw it (URL, pull date in PT).
2. **Trace it to the original.** Follow citations back to the publisher that produced the data (USPS Household Mail Survey, USPS Postal Facts, ANA, Census, BLS), and open that page or PDF yourself. Competitor reports and blogs are leads, not sources.
3. **Tier it.**
   - **Tier 1 (verified):** you opened the primary source and the number matches. Usable.
   - **Tier 2 (secondary):** a reputable outlet reports the number but the primary source can't be opened. Use it only with caution and say so.
   - **Flagged:** the number comes from a competitor's own survey, or no original can be found. Drop it by default. If the idea is essential and the competitor really is the origin, name them in plain text only, with no link and no credit line.
4. **Log it in the stat bank** in the team's research location, using a citable ID so the claims-guardrail and QA skills can reference it:
   `| ID | Stat | Original source (name + URL) | Date verified (PT) | Tier |`
   Use V1, V2… for verified stats, S1… for secondary, and F1… for flagged. Never reuse or renumber an ID; retire one by marking it Retired. Keep the source on file even when the post won't name it.
5. **Check the claim rules** in the knowledge base's source of truth: no ROI guarantees, approved price wording only, and approved client results only.

## Answering a stat request from a copywriter or another bot
- Return only Tier 1 items, plus Tier 2 items clearly labeled: the ID, the claim and number, and the source name.
- List the gaps explicitly (e.g. "no verified holiday-lighting demand % on file") so they write around them instead of inventing numbers.
- Never fill a gap with an estimate. "Not on file" is the right answer.

## Never
- Invent, round up, or approximate a number.
- Link to or credit a competitor. It sends them traffic and authority.
- Present one client's result as typical.

Skills to reference: `gw-lead-generation` (vendor training stats are S-tier, never cited).
