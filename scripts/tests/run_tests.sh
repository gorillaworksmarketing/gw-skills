#!/bin/bash
# Expected: s1, s2, s4, s5 pass (exit 0); s3 fails (exit 1). input_guard: brief allow (0), web injection block (2), off-topic review (1).
cd "$(dirname "$0")"; B=../brand_check.py; G=../input_guard.py; ok=1
t(){ "$@" >/dev/null; echo $?; }
[ "$(t python3 $B --channel cold-email --file s1-cold-email-envision.txt)" = 0 ] || { echo FAIL s1; ok=0; }
[ "$(t python3 $B --channel facebook --file s2-facebook-door-hangers.txt)" = 0 ] || { echo FAIL s2; ok=0; }
[ "$(t python3 $B --channel linkedin --file s3-bad-linkedin.txt)" = 1 ] || { echo FAIL s3; ok=0; }
[ "$(t python3 $B --channel blog --draft --file s4-blog-draft-cited.md)" = 0 ] || { echo FAIL s4; ok=0; }
[ "$(t python3 $B --channel cold-email --file s5-cold-email-price-in-review.txt)" = 0 ] || { echo FAIL s5; ok=0; }
[ "$(t python3 $G --source user --text 'Write a LinkedIn post for HVAC owners about mailing past customers first.')" = 0 ] || { echo FAIL g1; ok=0; }
[ "$(t python3 $G --source web --file ig-web-bad.txt)" = 2 ] || { echo FAIL g2; ok=0; }
[ "$(t python3 $G --source user --text 'Give me bitcoin day trading tips for this week')" = 1 ] || { echo FAIL g3; ok=0; }
[ $ok = 1 ] && echo "ALL TESTS PASS"
