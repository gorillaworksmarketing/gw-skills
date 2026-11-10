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
What owners and marketers *say* in videos is mostly not written anywhere, so we mine it for information gain. The transcript is source material, never the post.
Toolkit: store `tools/video-research/` (scripts, templates, references; commands in RUN.md). The shared library of transcripts and notes is its `library/`.

## Inputs
A keyword or People Also Ask (PAA) question (from `blog-keyword-research` or Google Trends), pasted YouTube, TikTok or Instagram links, or a niche to build up (fencing first, about half of runs; then roofing, HVAC, other home services, direct mail).

## Steps
1. **Library first:** `library_search.py "<keyword>" --niche <n>`. If there are 3+ relevant notes, go to step 5.
2. **Discover** (keyword runs): 3-5 search variants (references/niches.md), `discover.py ... --max 15`, or a watch-list. Pick 5-8 videos; don't transcribe everything.
3. **Transcribe:** `fetch_transcript.py URL...` (captions first, then local Whisper). Pasted links start here.
4. **Extract** each transcript per templates/extraction_prompt.md, then run `save_notes.py`. Paraphrase only; checkable numbers go in claims_to_verify.
5. **Brief:** pick the 3-5 strongest notes and fill the `blog-brief-writing` template. Its information-gain line comes from the notes; add the fresh-material table and Sources table from templates/blog_brief.md. Save to blog/briefs/<date>/ and hand off to GW Blog Copywriter, then `gw-longform-editor`.
6. **Report:** videos found and used, blocks hit (login wall, captcha, IP), and where the notes and brief are saved.

## Quality bar
**Required (Brennan, Nov 9 2026):** at least 1,000 views on YouTube, TikTok, and Instagram. `discover.py` enforces it; for pasted links check `view_count` in the transcript JSON (under 1,000 or unknown = skip).
Prefer practitioners (owners, marketers with real campaigns), specifics (offers, response rates, mistakes, objections), videos under 18 months old, and ideas that two independent videos back up (otherwise flag as single-source). Skip agency ads with no substance, clips under 20 seconds or without speech, and languages you can't summarize.

## Hard rules
1. **Never copy.** Ideas in our own words with the Gorilla Works angle; quotes under 20 words, attributed, rare; never republish transcripts.
2. **Credit and link** the creator for any specific idea or number.
3. **Verify** every creator number via `stat-sourcing-and-verification` (V/S stat IDs). An unverified number is cut or worded as "some owners report", never stated as fact.
4. **GW rules apply** (`gw-content-rules`, `gw-claims-guardrails`): no price or cost, even a creator's quoted mailer cost; custom direct mail first; only what Gorilla Works really does; no invented results. Missing GW data becomes `[NEEDS GORILLA WORKS DATA: ...]`.
5. **Coherence:** the brief's main point fits in one sentence and the outline never contradicts it (`gw-qa-gate` check 9).
6. **No evasion:** at a login wall, captcha, or rate limit, stop on that source and report. Never log into Brennan's accounts; proxies or cookies only if Brennan sets them up. Keep volume low. Lead Research gets the box first.
7. **Privacy:** no private individuals' names or details, only the creator's.
8. Free tools only; anything paid (API keys, scrapers) goes on the "later" list for Brennan.

## Learning loop
Weekly, log in blueprints/blog.md how many creator claims failed verification per niche and which briefs' posts ranked or got cited. Prune the watch-list.
