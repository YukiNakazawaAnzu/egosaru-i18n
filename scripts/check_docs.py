#!/usr/bin/env python3
"""Checks docs/<code>.md (the "help improve Egosaru" page of each language) against docs/en.md.

    python scripts/check_docs.py            every language in config/languages.json
    python scripts/check_docs.py fr de      only these

Same structure (one # heading, the same number of ## headings, numbered steps and paragraphs), the links point to that
language (site page, contact form, lang/<code>.json), the shared links are kept, and the text passes the script /
wrong-language checks of validate_ui_lang.py.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
os.environ.setdefault('EGOSARU_UI_DIR', os.path.join(ROOT, 'lang'))
os.environ.setdefault('EGOSARU_LANGUAGES_JSON', os.path.join(ROOT, 'config', 'languages.json'))
sys.path.insert(0, HERE)
import validate_ui_lang as v  # noqa: E402

LANGS = v.LANGS
SHARED = ['https://github.com/YukiNakazawaAnzu/egosaru-i18n/issues/new/choose', 'https://creativecommons.org/licenses/by/4.0/',
          '../CONTRIBUTORS.md']


def shape(t):
    return (len(re.findall(r'^# ', t, re.M)), len(re.findall(r'^## ', t, re.M)), len(re.findall(r'^\d+\. ', t, re.M)))


def main():
    codes = sys.argv[1:] or list(LANGS)
    en = open(os.path.join(ROOT, 'docs', 'en.md'), encoding='utf-8').read()
    bad = 0
    for code in codes:
        p = os.path.join(ROOT, 'docs', code + '.md')
        if not os.path.isfile(p):
            print('%-6s MISSING' % code)
            bad += 1
            continue
        t = open(p, encoding='utf-8').read()
        errs = []
        if shape(t) != shape(en):
            errs.append('structure differs from en.md: %s vs %s' % (shape(t), shape(en)))
        pre = '' if code == 'ja' else code + '/'
        need = SHARED + ['https://gstudio1.com/suggest/%sposts/google' % pre, 'https://gstudio1.com/suggest/%scontact' % pre,
                         '../lang/%s.json' % code]
        links = re.findall(r'\]\(([^)]+)\)|<(https?://[^>]+)>', t)
        found = {a or b for a, b in links}
        for u in need:
            if u not in found:
                errs.append('missing link ' + u)
        extra = found - set(need)
        if extra:
            errs.append('unexpected links: ' + ', '.join(sorted(extra)))
        if code not in ('ja', 'en'):
            body = re.sub(r'\[[^\]]*\]\([^)]*\)|<https?://[^>]+>|`[^`]*`', ' ', t)
            errs += [e for e in v.script_checks(code, {'t': body}) if 'PDF' not in e and 'site.name' not in e]
            if re.search(r'[぀-ヿ]', t):
                errs.append('Japanese kana left')
        print('%-6s %s' % (code, 'ok' if not errs else '%d problems' % len(errs)))
        for e in errs:
            print('       ' + e)
        bad += 1 if errs else 0
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
