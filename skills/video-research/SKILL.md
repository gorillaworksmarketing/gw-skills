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
What owners and marketers say in videos is mostly written nowhere, so we mine it for information gain; transcripts are source material, never the post.
Toolkit: store `tools/video-research/` (commands in RUN.md); shared library in its `library/`.

## Inputs
A keyword or PAA question (`blog-keyword-research`, Google Trends), pasted YouTube, TikTok or Instagram links, or a niche to build up (roofing, HVAC, B2B, direct mail lead; fencing small; team/industry-mix.md).

## Steps
1. **Library first:** `library_search.py "<keyword>" --niche <n>`. If there are 3+ relevant notes, go to step 5.
2. **Discover** (keyword runs): 3-5 search variants (references/niches.md), `discover.py ... --max 15`, or a watch-list. Pick 5-8.
3. **Transcribe (Brennan, Nov 10):** YouTube goes through the TubeAlfred connector: free yt-dlp metadata for views (`youtube_video_get`, which costs a credit, only as fallback), then `youtube_video_transcript` for picks that pass. About 50 free a month: never re-fetch a library video; log credits in library/tubealfred-usage.md; stop at 50. TikTok and Instagram: `fetch_transcript.py`. Pasted links start here.
4. **Extract** each transcript per templates/extraction_prompt.md, then run `save_notes.py`. Paraphrase only; checkable numbers go in claims_to_verify.
5. **Brief:** most videos teach a tactic, not a trade: if it's sound, apply it to every industry and adapt it to direct mail. Pick the 3-5 strongest notes and fill the `blog-brief-writing` template. Its information-gain line comes from the notes; add the fresh-material table and Sources table from templates/blog_brief.md. Save to blog/briefs/<date>/ and hand off to GW Blog Copywriter, then `gw-longform-editor`.
6. **Report:** videos used, blocks hit, save paths.

## Quality bar
**Required (Brennan, Nov 10):** YouTube 15,000+ views; TikTok and Instagram 1,000+. Every video under 2 years old; anything about AI under 3 months. Check both before transcribing (yt-dlp or `discover.py`); fails or unknown = skip.
Prefer practitioners, specifics (offers, response rates, mistakes, objections), and ideas two independent videos back up (else flag single-source). Skip empty ads and clips under 20s.

## Hard rules
1. **Never copy.** Ideas in our own words with the Gorilla Works angle; quotes under 20 words, attributed, rare; never republish transcripts.
2. **Credit and link** the creator for any specific idea or number.
3. **Verify** every creator number via `stat-sourcing-and-verification` (V/S stat IDs). An unverified number is cut, never hedged (`gw-fact-check`).
4. **GW rules apply** (`gw-content-rules`, `gw-claims-guardrails`): no price or cost, even a creator's quoted mailer cost; custom direct mail first; only what Gorilla Works really does; no invented results. Missing GW data becomes `[NEEDS GORILLA WORKS DATA: ...]`.
5. **Coherence:** the brief's main point fits in one sentence and the outline never contradicts it (`gw-qa-gate` check 9).
6. **No evasion:** at a login wall, captcha, or rate limit, stop on that source and report. Never log into Brennan's accounts; proxies or cookies only if Brennan sets them up.
7. **Privacy:** no private individuals' names or details, only the creator's.
8. Free tools only (TubeAlfred's free tier included); paid upgrades go on the "later" list.

## Learning loop
Weekly, log in blueprints/blog.md how many creator claims failed verification per niche and which briefs' posts ranked or got cited. Prune the watch-list.
