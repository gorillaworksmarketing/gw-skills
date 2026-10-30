---
name: gw-linkedin-editor
description: Use when turning a LinkedIn framework or draft into the final Gorilla Works post for Brennan's profile or the company page, with mention, keyword-led hook, line breaks, bar, CTA, humanizer pass, and QA. This is GW Social Editor's (fbaef014-a2d0-4dc1-820c-12fa3f64155b) LinkedIn skill. Use it even if the request doesn't name the skill.
---
# GW LinkedIn editor
Platform rules: blueprints/linkedin.md; patterns: blueprints/swipe/linkedin.md; voice: research/linkedin-voice-brennan.md; editor brief: team/editor-brief.md. Apply `gw-content-rules`, `gw-claims-guardrails`, then `gw-qa-gate`.

## Steps
1. **Line 1:** a real @Gorilla Works Marketing mention. Then a keyword-led hook that makes the topic clear in the first 1-2 lines.
2. **Format:** short lines, a blank line between thoughts, mobile-first; emojis few and purposeful (one marker type per list); no hashtags.
3. **Body:** 1-3-1 or a numbered list with Title Case mini-headers and 2-4 short lines each; 150-350 words by default (list posts up to about 450).
4. **Voice:** Brennan's analytical, confident, blunt style; hard numbers (approved or with V/S stat IDs only).
5. **Bar:** a punchy two-sentence close, then ONE CTA (UTM /book-demo or a native ask).
6. **Humanize:** the AI-pattern sweep; cut adverbs; vary rhythm; show emotion.
- **Rulings:** stats need no source in the post but must be logged (V/S IDs); prices only "as low as $0.78" / "under $1", no stamp comparison; Real Great Roofing exact quote only, no campaign details; lead-gen posts carry the /book-demo UTM; no hashtags or self-aware ranking lines (`gw-claims-guardrails`).
- **Links (required):** build every gorillaworksmarketing.com link per research/utm-link-strategy.md (UPDATE Oct 14: utm_source=<platform>, utm_campaign=`<industry>_<type>` in that order, e.g. `fencing_faq`; utm_term=<article slug>; utm_medium=format; utm_content=unique post id, never reused; lowercase; blog internal and canonical links stay clean) and log each one in research/link-log.csv (`date,platform,account,post_url,link_url,utm_campaign,utm_content,industry,type,utm_term`).
7. Output the final post, a change log, and the `gw-qa-gate` result. Brennan posts manually; never publish.

Skills to reference: `gw-lead-generation` (lead-magnet naming and CTA rules, clear not clever, Proof+Promise+Plan, reading-level check, one CTA, front-loaded hook).

Oct 19 checks: 75% value / 25% lead-gen mix; 200-280 words; no offer hook on the company page; no Real Great Roofing quote as the lead; li-p1 "51%" hook retired; log hook A/B in Notion and -a/-b on utm_content. Replies: ~75% pure value, soft CTA or "shoot me a DM" ok; fail drafts that force a URL on every reply.
