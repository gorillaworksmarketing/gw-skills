---
name: gw-fact-check
description: >-
  Use on EVERY Gorilla Works post, reply, comment, article, newsletter, or
  email, after drafting and again at the editor, to make sure nothing is
  invented: build a claim table, verify every stat, quote, attribution, Gorilla
  Works fact, rule, and link against a real source, cut or mark anything
  unverified, and flag fake examples. gw-qa-gate fails work without it. Use it
  even if the request just says "check this" or "edit this".
---
# GW fact check (no made-up facts)
Brennan's rule (Nov 10 2026): nothing we publish anywhere may be invented, guessed, or "probably true". This check runs on every post, reply, comment, article, newsletter and email, after drafting and again at the editor, and `gw-qa-gate` fails anything without it.

## Why
AI drafts sound sure even when they're wrong: a made-up stat, a quote no one said, a feature we don't have, a USPS rule that changed. One wrong claim costs more trust than ten good posts earn.

## 1. Build the claim table (writer)
List every checkable claim, one row each: `| Claim (as written) | Type | Source (stat ID, URL, or file) | Status |`.
Types: number or stat; quote; something a person, company, or video said; Gorilla Works fact (service, feature, result, offer, client); rule, law, or USPS fact; date, event, or "new" trend; tool or platform behavior; link.
Opinion and advice need no row, but advice can't rest on a claim that has none.

## 2. Verify each row
- **Numbers:** a V or S stat-log ID (`stat-sourcing-and-verification`). Never estimate, round, or "about" a number we don't have.
- **Quotes:** word for word from the source, which you opened this session; under 20 words; credited.
- **"X says / a video shows":** the source actually says it (re-read the transcript or page). Video notes: only items moved from claims_to_verify to verified.
- **Gorilla Works facts:** only what's in knowledge-base/00-source-of-truth.md or `gw-claims-guardrails`. No new results, clients, features, or offers.
- **Rules, laws, USPS:** a primary source (usps.com, ftc.gov, pe.usps.com) checked this session.
- **Links:** open every URL; it must load and support the sentence it sits in.
- **Examples:** a made-up scenario says so ("say a roofer in Mesa mails..."). Never present one as a real client, a real number, or a real person.
Status is `verified`, `cut`, or `[NEED: ...]`. If you can't verify it, cut it or mark it; never soften it into "studies show", "experts say", or "many owners" to slip it through.

## 3. Red flags (check twice)
Precise numbers with no source; percentages that add up too neatly; named studies, surveys, or reports; years and "in 2026" trend claims; quotes; anything about competitors; superlatives ("the only", "first", "#1" outside approved ranked lists); "guaranteed"; claims about what someone else posted (replies must match what they actually wrote); facts from memory or from another bot's message with no source attached.

## 4. Editor re-check
The editor doesn't trust the table. Open the source for every number, quote, and Gorilla Works claim, plus a sample of the rest, and confirm the draft says exactly what the source says (watch for drift: "up to" becoming a flat number, a range becoming one figure, a 2019 stat called current). A wrong row sends the piece back to the writer.

## 5. Gate result
- PASS: every row is verified, or cut, with nothing left as [NEED].
- FAIL: a missing table, any unverified claim in the copy, a quote or stat that doesn't match its source, or an invented example shown as real.
Attach the table to the handoff so `gw-qa-gate` and Brennan can see it. Never publish.

## Learning loop
Log every caught invention (claim, who wrote it, how it was caught) in research/fact-check-log.md. Weekly, the top repeat patterns go back into the writer skills and this red-flag list.
