---
name: video-research
description: >-
  Use when a Gorilla Works blog keyword, PAA question, or Google Trends keyword
  needs fresh information gain from what contractors and marketers say in
  YouTube, TikTok, or Instagram videos; when someone pastes a video link to
  transcribe or learn from; or when building the fencing, roofing, HVAC, or
  direct mail video-notes library. Finds, transcribes, and extracts videos into
  notes and a blog brief. Use it even if 'transcribe' is never said.
---
# GW video research
Videos hold what owners and marketers write nowhere: mine them for information gain; transcripts are source material, never the post.
Toolkit: store `tools/video-research/` (RUN.md; library in `library/`).

## Inputs
A keyword or PAA question (`blog-keyword-research`, Google Trends), pasted YouTube, TikTok or Instagram links, or a niche to build up (mix: team/industry-mix.md).

## Steps
1. **Library first:** `library_search.py "<keyword>" --niche <n>`. 3+ relevant notes: go to step 5 (any length; views and age still apply).
2. **Discover** (keyword runs): 3-5 variants (references/niches.md), `discover.py ... --max 15`, or a watch-list; pick 5-8.
3. **Transcribe (Brennan, Nov 10):** YouTube goes through the TubeAlfred connector: views from free yt-dlp metadata (`youtube_video_get` costs a credit: fallback only), then `youtube_video_transcript` for picks that pass. About 50 free a month: never re-fetch a library video; log credits in library/tubealfred-usage.md; stop at 50. TikTok and Instagram: `fetch_transcript.py`. Pasted links start here.
4. **Extract** each transcript per templates/extraction_prompt.md, then run `save_notes.py`. Paraphrase only; checkable numbers go in claims_to_verify.
5. **Brief:** most videos teach a tactic, not a trade: apply sound ones to every industry, adapted to direct mail. Fill the `blog-brief-writing` template from the 3-5 strongest notes (information-gain line from them) plus the fresh-material and Sources tables in templates/blog_brief.md. Save to blog/briefs/<date>/; hand to GW Blog Copywriter, then `gw-longform-editor`.
6. **Report:** videos used, blocks, save paths.

## Quality bar
**Every video, library included (Brennan, Nov 10):** YouTube 15,000+ views; TikTok and Instagram 1,000+; under 2 years old; anything about AI under 3 months.
**Length (Brennan, Nov 10, 4:49 PM PT):** over 9 minutes applies to NEW collection only. Videos in the library before that rule stay usable at any length; editors and copywriters never reject them for being short.
Check new picks before transcribing (yt-dlp, `discover.py`); fail or unknown = skip.
Prefer practitioners, specifics (blueprint), and ideas two independent videos back up (else flag single-source). Skip empty ads.

## Hard rules
1. **Never copy.** Ideas in our own words with the Gorilla Works angle; quotes under 20 words, attributed, rare; never republish transcripts.
2. **Credit and link** the creator for any specific idea or number.
3. **Verify** every creator number via `stat-sourcing-and-verification` (V/S stat IDs); unverified = cut, never hedged (`gw-fact-check`).
4. **GW rules apply** (`gw-content-rules`, `gw-claims-guardrails`): no price or cost, even a creator's mailer cost; custom direct mail first; only what Gorilla Works does; no invented results. Missing GW data becomes `[NEEDS GORILLA WORKS DATA: ...]`.
5. **Coherence:** the brief's main point fits in one sentence and the outline never contradicts it (`gw-qa-gate` check 9).
6. **No evasion:** at a login wall, captcha, or rate limit, stop on that source and report. Never log into Brennan's accounts; proxies or cookies only if Brennan sets them up.
7. **Privacy:** only the creator's name and details, no private individuals'.
8. Free tools only (incl. TubeAlfred's free tier); paid upgrades go on the "later" list.

## Learning loop
Weekly, log in blueprints/blog.md creator claims that failed verification per niche and which briefs' posts ranked or got cited; prune the watch-list.
