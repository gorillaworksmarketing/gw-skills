#!/usr/bin/env python3
"""Gorilla Works deterministic brand check (brand/brand-guidelines.md section 9).

Usage:
  python3 scripts/brand_check.py --channel blog --file draft.md [--draft]
  echo "text" | python3 scripts/brand_check.py --channel linkedin
Channels: cold-email (roofing landing-page email), email, newsletter, blog,
longform, linkedin, facebook, x, x-reply, reddit, quora, gbp.
--draft: the text is a writer handoff, so every flagged number must carry an
inline citation marker ([S:ID], [src: URL], [fact: GW-...]) or a URL.
Output: JSON with pass/fail, each flag, and retry_prompt (the exact error text
the editor feeds back on an automatic rewrite). Exit 0 = pass, 1 = fail.
Standard filler list (STANDARD_FILLER) is an editable default; Brennan's named
words (BRENNAN_BANNED) are fixed.
"""
import argparse, json, re, sys

# --- Word lists (keep in sync with brand/brand-guidelines.md sections 3 and 6) ---
BRENNAN_BANNED = {  # Brennan, Nov 13 2026: explicitly forbidden
    "delve": r"delv(?:e|es|ed|ing)", "tapestry": r"tapestr(?:y|ies)",
    "elevate": r"elevat(?:e|es|ed|ing)", "unlock": r"unlock(?:s|ed|ing)?",
    "game-changer": r"game[- ]?chang(?:er|ers|ing)", "testament": r"testaments?",
}
STANDARD_FILLER = {  # editable standard AI-filler list (Brennan can add/remove)
    "landscape": r"(?:digital |marketing |ever[- ]changing |competitive )?landscape",
    "realm": r"realms?", "navigate": r"navigat(?:e|es|ing) the", "leverage": r"leverag(?:e|es|ed|ing)",
    "harness": r"harness(?:es|ed|ing)?", "seamless": r"seamless(?:ly)?", "robust": r"robust",
    "cutting-edge": r"cutting[- ]edge", "revolutionize": r"revolutioni[sz](?:e|es|ed|ing)",
    "transformative": r"transformative", "empower": r"empower(?:s|ed|ing|ment)?",
    "supercharge": r"supercharg(?:e|es|ed|ing)", "skyrocket": r"skyrocket(?:s|ed|ing)?",
    "synergy": r"synerg(?:y|ies|istic)", "holistic": r"holistic(?:ally)?",
    "paradigm": r"paradigms?", "foster": r"foster(?:s|ed|ing)?", "bustling": r"bustling",
    "vibrant": r"vibrant", "meticulous": r"meticulous(?:ly)?", "pivotal": r"pivotal",
    "crucial": r"crucial(?:ly)?", "embark": r"embark(?:s|ed|ing)?", "journey": r"(?:your|our|the) journey",
    "unleash": r"unleash(?:es|ed|ing)?", "unveil": r"unveil(?:s|ed|ing)?", "beacon": r"beacons?",
    "symphony": r"symphon(?:y|ies)", "intricate": r"intricate", "multifaceted": r"multifaceted",
    "ever-evolving": r"ever[- ]evolving", "dive in": r"(?:let's |deep )?dive (?:in|into)\b|deep dive",
    "in today's world": r"in today'?s (?:fast[- ]paced |digital |modern )?(?:world|age|market)",
    "here's the thing": r"here'?s the thing", "i'll be honest": r"i'?ll be honest",
    "at the end of the day": r"at the end of the day", "it's worth noting": r"it'?s worth noting",
    "in conclusion": r"in conclusion", "furthermore": r"furthermore", "moreover": r"moreover",
    "additionally": r"^additionally|\. additionally", "rest assured": r"rest assured",
    "look no further": r"look no further", "take it to the next level": r"(?:take|taking) (?:it|your \w+) to the next level",
    "next-level": r"next[- ]level", "a must-have": r"must[- ]have", "boasts": r"boasts?",
    "nestled": r"nestled", "treasure trove": r"treasure trove", "plethora": r"plethora",
    "myriad": r"myriad", "showcase": r"showcas(?:e|es|ed|ing)", "streamline": r"streamlin(?:e|es|ed|ing)",
    "optimize your": r"optimi[sz]e your", "in the world of": r"in the (?:world|realm) of",
    "when it comes to": r"when it comes to", "whether you're": r"whether you'?re a",
}
BANNED_LINES = [  # gw-content-rules banned lines (never, in any form)
    "yes, we ranked ourselves first", "yes, us", "admittedly biased", "we put ourselves first",
    "we told you so", "read the rest anyway", "every company on it is a real option", "obviously.",
    "thousands of other customers",
]
ENGAGEMENT_BAIT = r"\b(?:agree\?|thoughts\?|read that again|let that sink in|who else\?|tag a friend|comment below)"
CONTRAST = r"\b(?:it'?s|this is|that'?s) not (?:just )?(?:about )?[\w\s']{1,30}[,;.]\s*(?:it'?s|this is|that'?s)\b"
STOCK_OPENER = r"^(?:the result\?|the truth\?|the answer\?|imagine this|picture this|let'?s face it|newsflash)"
PROOF_LINE = 'Real Great Roofing: "$90,000 in leads from just one mail drop."'
APPROVED_OFFERS = ["up to $500 off your first campaign"]  # plus the 4 offer arms in blueprints/cold-email.md
PRICE_FAIL = [
    (r"\$\s?\d[\d,]*(?:\.\d+)?(?:\s?[kKmM]\b)?", "a dollar amount"),
    (r"\b\d+(?:\.\d+)?\s?(?:cents?|¢)", "a cents amount"),
    (r"\bas low as\b", '"as low as"'), (r"\bunder \$?1\b|\bunder a dollar\b", '"under $1"'),
    (r"\b(?:per|a|each) (?:piece|mailer|postcard|card)\b.{0,20}\$|\$.{0,20}\b(?:per|a|each) (?:piece|mailer|postcard)", "per-piece price math"),
    (r"\b(?:postage )?stamps?\b.{0,40}\b(?:price|cost|same as|cheaper)|\b(?:price|cost|cheaper)\b.{0,40}\bstamps?\b", "a stamp comparison"),
    (r"\b(?:plan|monthly) (?:price|pricing|rate)s?\b|\bessentials plan\b|\bgrowth plan\b|\bauthority plan\b", "plan pricing"),
]
PRICE_WARN = r"\b(?:price[sd]?|pricing|cost[s]?|cheap(?:er|est)?|affordable|budget|fee[s]?|quote[sd]?|estimate[sd]?|free)\b"
ATTRIB = r"(?:\b(?:per|according to|reports?|reported|found|finds|says|said|survey|study|data from|via)\b\s+(?:the\s+)?[A-Z]|\[S:[^\]]+\]|\[src:[^\]]+\]|\[fact:[^\]]+\]|https?://)"
CITE_MARK = r"\[S:[^\]]+\]|\[src:[^\]]+\]|\[fact:[^\]]+\]|https?://\S+"
APPROVED_FACTS = [r"200\+\s*(?:data )?variables", r"200\+\s*data points", r"10 years of experience", re.escape(PROOF_LINE),
                  r"\$90,000 in leads from just one mail drop"]
NUM_CLAIM = r"(?<![\w/#.-])(?:\d[\d,]*(?:\.\d+)?\s?(?:%|percent\b|x\b)|\$\s?\d[\d,]*(?:\.\d+)?|\d{1,3}(?:,\d{3})+|\d{3,}(?!\s?(?:am|pm|AM|PM))|\d+(?:\.\d+)?\s(?:out of|in)\s\d+)"
GRADE_TARGET = {  # (aim, fail above). Sources: cold email 7th max (Brennan V7 / blueprints/cold-email.md);
    # long-form "about 5th grade" (gw-longform-editor); social 3rd-5th (gw-lead-generation).
    # Fail limits for blog (7) and social (6) are calibration, pending Brennan (guidelines section 5).
    "cold-email": (7, 7), "email": (7, 7), "newsletter": (7, 7),
    "blog": (5, 7), "longform": (5, 7), "quora": (5, 7),
    "linkedin": (5, 6), "facebook": (5, 6), "x": (5, 6), "x-reply": (5, 6), "reddit": (5, 6), "gbp": (5, 6),
}
CHANNELS = sorted(GRADE_TARGET)

def strip_exempt(text, channel):
    """Remove spans exempt from price/number checks: verbatim third-party quotes,
    the approved proof line, approved offers (not in roofing cold email)."""
    out = []
    for line in text.splitlines():
        if re.match(r"\s*(?:Review quote|Review name)\s*:", line):
            out.append(""); continue  # verbatim Google review (exempt, Brennan Nov 13 3:18 PM PT)
        line = line.replace(PROOF_LINE, "").replace("$90,000 in leads from just one mail drop", "")
        if channel != "cold-email":
            for o in APPROVED_OFFERS:
                line = re.sub(re.escape(o), "", line, flags=re.I)
        out.append(line)
    t = "\n".join(out)
    t = re.sub(r"\[\[quote\]\].*?\[\[/quote\]\]", " ", t, flags=re.S)  # marked third-party quotes
    t = re.sub(r"^\s*>.*$", " ", t, flags=re.M)  # markdown blockquotes = quotes
    return t

def plain(text):
    t = re.sub(r"https?://\S+", " ", text)
    t = re.sub(r"\[(?:S|src|fact):[^\]]+\]", " ", t)
    t = re.sub(r"[#*_`>|]+", " ", t)
    t = re.sub(r"^\s*(?:Subject|Preview|Eyebrow|Headline|Review quote|Review name|Body paragraph \d|Proof line|CTA)\s*:", " ", t, flags=re.M)
    return t

def syllables(w):
    w = w.lower().strip(".,!?;:'\"()")
    if not w: return 0
    if len(w) <= 3: return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w); w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", w)))

def fk_grade(text):
    t = plain(text)
    sents = [s for s in re.split(r"(?<=[.!?])\s+|\n{1,}", t) if re.search(r"[A-Za-z]", s)]
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", t)
    if len(words) < 30 or not sents: return None, len(words)
    syl = sum(syllables(w) for w in words)
    return round(0.39 * len(words) / len(sents) + 11.8 * syl / len(words) - 15.59, 1), len(words)

def line_of(text, idx): return text.count("\n", 0, idx) + 1

def check(text, channel, draft=False):
    flags = []
    def add(check_name, sev, match, idx, error):
        flags.append({"check": check_name, "severity": sev, "match": match, "line": line_of(text, idx) if idx is not None else None, "error": error})
    low = text.lower()
    # 1. Banned words / AI cliches (exempt verbatim quotes)
    scan = strip_exempt(text, channel)
    for name, pat in list(BRENNAN_BANNED.items()) + list(STANDARD_FILLER.items()):
        for m in re.finditer(r"(?<![\w-])(?:" + pat + r")(?![\w-])", scan, flags=re.I | re.M):
            src = "Brennan's banned list" if name in BRENNAN_BANNED else "the standard AI-filler list"
            add("banned_word", "fail", m.group(0), m.start(), f"used the banned word '{m.group(0)}' ({src}); replace it with a plain, specific word")
    for bl in BANNED_LINES:
        i = scan.lower().find(bl)
        if i >= 0: add("banned_line", "fail", bl, i, f"used the banned line '{bl}'; delete it")
    # 2. AI tells
    for m in re.finditer("[\u2014\u2013]", scan):
        add("em_dash", "fail", m.group(0), m.start(), "used an em or en dash; rewrite the sentence with a period or comma")
        break
    for m in re.finditer(ENGAGEMENT_BAIT, scan, flags=re.I):
        add("engagement_bait", "fail", m.group(0), m.start(), f"used engagement bait '{m.group(0)}'; end with a real takeaway or one CTA")
    for m in re.finditer(CONTRAST, scan, flags=re.I):
        add("contrast_reveal", "fail", m.group(0), m.start(), f"used a contrast reveal ('{m.group(0).strip()}'); state the point directly")
    for m in re.finditer(STOCK_OPENER, scan, flags=re.I | re.M):
        add("stock_opener", "fail", m.group(0), m.start(), f"used a stock opener or colon reveal '{m.group(0)}'; open with the point")
    # 3. Price wording in our own copy
    pscan = scan
    for pat, label in PRICE_FAIL:
        for m in re.finditer(pat, pscan, flags=re.I):
            add("price", "fail", m.group(0), m.start(), f"included price wording ({label}: '{m.group(0)}') in our own copy; remove it (only the verbatim review quote, the exact proof line, and approved offers are exempt)")
    for m in re.finditer(PRICE_WARN, pscan, flags=re.I):
        add("price_word", "warn", m.group(0), m.start(), f"contains '{m.group(0)}'; confirm it is not a price or cost claim about Gorilla Works")
    # 4. Inline citations for numbers
    facts_removed = scan
    for f in APPROVED_FACTS: facts_removed = re.sub(f, " ", facts_removed, flags=re.I)
    facts_removed = re.sub(r"^\s*Eyebrow\s*:.*$", " ", facts_removed, flags=re.M)  # count/rating cited in claim table
    facts_removed = re.sub(r"https?://\S+|utm_\w+=\S+", " ", facts_removed)
    sentences = re.split(r"(?<=[.!?])\s+|\n", facts_removed)
    pos = 0
    for s in sentences:
        for m in re.finditer(NUM_CLAIM, s):
            tok = m.group(0)
            if re.fullmatch(r"(?:19|20)\d\d", tok.strip()): continue  # bare years
            ok = re.search(CITE_MARK if draft else ATTRIB, s, flags=0 if not draft else 0)
            if not ok:
                sev = "fail" if (draft or channel not in ("cold-email",)) else "warn"
                idx = text.find(s.strip()[:40]) if s.strip() else None
                add("citation", sev, tok, idx if idx and idx >= 0 else None,
                    f"stated the number '{tok}' without an inline citation; add the source in the same sentence" + (" as [S:ID] or [src: URL]" if draft else " (e.g. 'USPS found...') or cut it"))
            break
    # 5. Hashtags
    for m in re.finditer(r"(?<![\w&/])#[A-Za-z][\w]*", text):
        add("hashtag", "fail", m.group(0), m.start(), f"used the hashtag '{m.group(0)}'; remove all hashtags")
    # 6. google.com/url wrappers
    for m in re.finditer(r"https?://(?:www\.)?google\.[a-z.]+/url\?\S*", text, flags=re.I):
        add("google_wrapper", "fail", m.group(0)[:60], m.start(), "used a google.com/url redirect wrapper; replace it with the direct URL")
    # 7. Channel specifics
    if channel in ("x", "x-reply") and re.search(r"\btwitter\b|\btweet", low):
        add("platform", "fail", "Twitter", low.find("twitter"), "said 'Twitter' or 'tweet'; say 'X' and 'post'")
    if channel == "x-reply" and len(text.strip()) >= 240:
        add("platform", "fail", str(len(text.strip())), None, f"reply is {len(text.strip())} characters; X replies must be under 240")
    if channel == "linkedin" and text.strip() and "@gorilla works marketing" not in text.strip().splitlines()[0].lower():
        add("platform", "fail", "line 1", 0, "line 1 is missing the @Gorilla Works Marketing mention; add it on top")
    if channel == "cold-email":
        for need in ["Subject:", "Preview:", "Eyebrow:", "Headline:", "Review quote:", "Review name:", "Body paragraph 1:", "Body paragraph 2:", "Proof line:", "CTA:"]:
            if need not in text: add("cold_email_slots", "fail", need, None, f"is missing the labeled line '{need}'")
    # 8. Reading level
    grade, nwords = fk_grade(text)
    aim, limit = GRADE_TARGET[channel]
    if grade is not None and grade > limit:
        add("reading_level", "fail", str(grade), None, f"reads at Flesch-Kincaid grade {grade}; {channel} must be grade {limit} or lower (aim for {aim}), so use shorter sentences and shorter words")
    elif grade is not None and grade > aim:
        add("reading_level", "warn", str(grade), None, f"reads at Flesch-Kincaid grade {grade}; aim for grade {aim} on {channel}")
    fails = [f for f in flags if f["severity"] == "fail"]
    retry = None
    if fails:
        groups = {}
        for f in fails: groups.setdefault(f["check"], []).append(f)
        parts = []
        for chk, fs in groups.items():
            words = sorted({f["match"] for f in fs})
            if chk == "banned_word":
                parts.append("used the banned word" + ("s " if len(words) > 1 else " ") + ", ".join(f"'{w}'" for w in words) + " (replace each with a plain, specific word)")
            elif chk == "price":
                parts.append("included price wording in our own copy (" + ", ".join(f"'{w}'" for w in words) + "); remove it, since only the verbatim review quote, the exact proof line, and approved offers are exempt")
            elif chk == "citation":
                parts.append("stated " + ", ".join(f"'{w}'" for w in words) + " without an inline citation; name the source in the same sentence or cut the number")
            elif chk == "hashtag":
                parts.append("used hashtags (" + ", ".join(words) + "); remove all hashtags")
            else:
                seen = []
                for f in fs:
                    if f["error"] not in seen: seen.append(f["error"])
                parts.extend(seen)
        retry = "Your previous draft " + "; ".join(parts) + ". Rewrite it, fixing only these issues, and keep every verified fact, source, and the required format."
    return {"channel": channel, "draft_mode": draft, "pass": not fails, "reading_grade": grade, "grade_aim": aim, "grade_limit": limit,
            "words": nwords, "fail_count": len(fails), "warn_count": len(flags) - len(fails), "flags": flags, "retry_prompt": retry}

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--channel", required=True, choices=CHANNELS)
    ap.add_argument("--file"); ap.add_argument("--text")
    ap.add_argument("--draft", action="store_true", help="writer handoff: require [S:ID]/[src:]/[fact:] markers")
    a = ap.parse_args()
    text = a.text if a.text is not None else (open(a.file, encoding="utf-8").read() if a.file else sys.stdin.read())
    res = check(text, a.channel, a.draft)
    print(json.dumps(res, indent=2, ensure_ascii=False))
    sys.exit(0 if res["pass"] else 1)

if __name__ == "__main__":
    main()
