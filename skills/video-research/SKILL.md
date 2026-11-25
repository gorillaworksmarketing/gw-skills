---
name: video-research
description: >-
  Use when a Gorilla Works Semrush blog keyword needs information gain from
  YouTube, TikTok, or Instagram; when someone pastes a video link to transcribe;
  or when building the fencing, roofing, HVAC, or direct mail video-notes
  library. Use it even if 'transcribe' is never said.
---
# GW video research
Transcripts are source material, never the post. Toolkit: store `tools/video-research/` (RUN.md; library/). Depth: blueprints/blog.md.

## Inputs
A Semrush keyword from `blog-keyword-research`, pasted YouTube, TikTok or Instagram links, or a niche (team/industry-mix.md). Semrush is the only keyword source. All or almost all posts come from Semrush keywords plus this research, a main brief input, not an add-on. Do not take topics from PAA or Google Trends.

## Steps (detail: blueprints/blog.md)
1. **Library first:** `library_search.py "<keyword>" --niche <n>`. 3+ relevant notes: go to step 5 (any length; views and age still apply).
2. **Discover:** 3-5 variants (references/niches.md), `discover.py ... --max 15`, or a watch-list; pick 5-8.
3. **Transcribe (Brennan, Nov 10):** YouTube through TubeAlfred: views from free yt-dlp metadata (`youtube_video_get` costs a credit: fallback only), then `youtube_video_transcript` for picks that pass. ~50 free/month; never re-fetch a library video; log credits in library/tubealfred-usage.md; stop at 50. TikTok and Instagram: `fetch_transcript.py`. Pasted links start here.
4. **Extract** per templates/extraction_prompt.md, then `save_notes.py`. Paraphrase only; checkable numbers go in claims_to_verify.
5. **Brief:** apply sound tactics to every industry, adapted to direct mail (tactic, not a trade). Fill the `blog-brief-writing` template from the 3-5 strongest notes (info-gain from them) plus templates/blog_brief.md. Save under blog/briefs/<date>/; hand to the Blog Copywriter, then `gw-longform-editor`.
6. **Report:** videos used, blocks, save paths.

## Quality bar (Nov 10; blueprints/blog.md)
Every video including library: YouTube 15,000+ views; TikTok/IG 1,000+; under 2 years; AI topics under 3 months. Over 9 minutes for NEW collection only (4:49 PM PT); pre-rule library videos stay usable at any length (never reject for being short). Check new picks before transcribing (yt-dlp, `discover.py`); fail or unknown = skip. Prefer practitioners, specifics, two-video support (else flag single-source); skip empty ads.

## Hard rules
Never copy (our words, GW angle; quotes under 20 words, attributed, rare; never republish transcripts). Credit and link the creator for a specific idea or number. Verify every creator number via `stat-sourcing-and-verification` (V/S IDs); unverified = cut, never hedged (`gw-fact-check`). GW rules (`gw-content-rules`, `gw-claims-guardrails`): no price or cost, even a creator's mailer cost; custom direct mail first; only what Gorilla Works does; no invented results; missing GW data: `[NEEDS GORILLA WORKS DATA: ...]`. Coherence: one-sentence main point; outline never contradicts it (`gw-qa-gate` check 9). No evasion: login wall, captcha, or rate limit: stop on that source and report; never log into Brennan's accounts; proxies or cookies only if he sets them up. Privacy: creator details only, no private individuals'. Free tools only (incl. TubeAlfred's free tier); paid upgrades go on the "later" list.

Learning loop: weekly, log failed verifications and which briefs ranked or got cited in blueprints/blog.md; prune the watch-list.
