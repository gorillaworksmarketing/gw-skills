---
name: gw-blog-to-social
description: >-
  Use when a Gorilla Works blog post (or Medium/Substack article) is published
  and logged in team/handoffs.md, to cut it into standalone LinkedIn and X post
  frameworks that link back to the blog URL. Use it even if the request doesn't
  name the skill.
---
# GW blog to social (content waterfall)
Sources: team/team-structure.md, blog/blog-rules.md (Syndication), blueprints/linkedin.md and x.md.

## Steps
1. Take a published URL from team/handoffs.md. Only use pieces that are live.
2. Pull out the intro angle, the direct answer, one key insight, 3 highlights, and any stats with their stat-log IDs.
3. Draft frameworks (not final copy):
   - **LinkedIn:** 3 posts with different angles (via `gw-linkedin-post`); each stands alone and links the blog URL with UTM tags.
   - **X:** short posts and/or one thread (via `gw-x-post`); link the blog URL where it fits.
4. Each cut-down must stand alone and be tailored to its platform: no identical text across platforms. Rebuild the hook for each (a specific fact, number, or story from the post), not a summary of the article.
4b. Keep the industry mix (50% fencing) across the week's cut-downs.
5. Send them to `gw-linkedin-editor` / `gw-x-editor`, and mark the handoff row as "cut".
6. Reverse direction: log top social posts and reader questions back into handoffs.md as blog topic ideas.

**Links (required):** build every gorillaworksmarketing.com link per research/utm-link-strategy.md (utm_source=<platform>, utm_campaign=`<industry>_<type>`, utm_term=<slug>, unique utm_content, lowercase) and log each in research/link-log.csv.

Skills to reference: `gw-newsletter` (one-idea issue from a post), `gw-lead-generation` (Proof+Promise+Plan, kaleidoscope reuse).

Learning loop: weekly with GW Analytics: which cut-down angles drove blog visits and demos by UTM; log in blueprints/blog.md.
