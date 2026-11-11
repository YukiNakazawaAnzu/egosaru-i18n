#!/usr/bin/env python3
"""Checks api-docs/<code>.json (strings of the Suggest API documentation) against api-docs/ja.json.

    python scripts/validate_api_docs.py          every language
    python scripts/validate_api_docs.py fr de    only these

Same keys, same HTML tags, same %placeholders% and {placeholders}, no Japanese kana (the quoted あ–ん example
is allowed), not empty. Exit code 1 when anything is wrong.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, '..', 'api-docs')
TAG = re.compile(r'</?[a-zA-Z][^>]*>')
PH = re.compile(r'%[a-z_]+%|\{[a-z_]+\}')
KANA = re.compile(r'[぀-ヿ]')


def main():
    src = json.load(open(os.path.join(DIR, 'ja.json'), encoding='utf-8'))
    codes = sys.argv[1:] or sorted(f[:-5] for f in os.listdir(DIR) if f.endswith('.json') and f != 'ja.json')
    bad = 0
    for code in codes:
        dst = json.load(open(os.path.join(DIR, code + '.json'), encoding='utf-8'))
        errs = []
        extra = sorted(set(dst) - set(src))
        if extra:
            errs.append('unknown keys: ' + ', '.join(extra))
        for k, v in src.items():
            w = dst.get(k)
            if not isinstance(w, str) or not w.strip():
                errs.append('empty or missing: ' + k)
                continue
            if sorted(TAG.findall(v)) != sorted(TAG.findall(w)):
                errs.append('HTML tags differ: ' + k)
            if sorted(PH.findall(v)) != sorted(PH.findall(w)):
                errs.append('placeholders differ: ' + k)
            if code not in ('zh', 'zh-tw') and KANA.search(w.replace('あ–ん', '').replace('あ〜ん', '')):
                errs.append('Japanese kana left: ' + k)
        print('%-6s %s' % (code, 'ok' if not errs else '%d problems' % len(errs)))
        for e in errs[:30]:
            print('       ' + e)
        bad += 1 if errs else 0
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
