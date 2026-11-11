#!/usr/bin/env python3
"""Checks application/language/ui/{code}.json against ja.json (the source of truth).

    python scripts/validate_ui_lang.py            # every language file found
    python scripts/validate_ui_lang.py ru ko      # only these

Per key it verifies: the key exists (keys starting with "ja_only." are exempt), the type matches
(string / list), lists have the same length, {placeholders} are identical, HTML tags are identical,
and (outside ja/zh/zh-tw) no kana is left over. Exit code 1 when anything is wrong.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# EGOSARU_UI_DIR / EGOSARU_LANGUAGES_JSON: the public translation repository (egosaru-i18n) runs this script with its own layout.
UI = os.environ.get('EGOSARU_UI_DIR') or os.path.join(HERE, '..', 'application', 'language', 'ui')
KANA = re.compile(r'[぀-ヿ]')
PH = re.compile(r'\{[a-z_]+\}')
TAG = re.compile(r'</?[a-zA-Z][^>]*>')
LANGS = json.load(open(os.environ.get('EGOSARU_LANGUAGES_JSON') or os.path.join(HERE, '..', 'application', 'config', 'languages.json'), encoding='utf-8'))


def tags(s):
    return sorted(re.sub(r'\s+', ' ', t) for t in TAG.findall(s))


# Script of each non-Latin edition: share of letters (outside tags/placeholders) that must be in it.
SCRIPT = {
    'ru': 'Ѐ-ӿ', 'uk': 'Ѐ-ӿ', 'bg': 'Ѐ-ӿ', 'kk': 'Ѐ-ӿ', 'zh': '一-鿿', 'zh-tw': '一-鿿', 'ko': '가-힯', 'th': '฀-๿',
    'ar': '؀-ۿ', 'fa': '؀-ۿ', 'ur': '؀-ۿ', 'hi': 'ऀ-ॿ', 'mr': 'ऀ-ॿ', 'ne': 'ऀ-ॿ', 'bn': 'ঀ-৿', 'ta': '஀-௿',
    'te': 'ఀ-౿', 'gu': '઀-૿', 'he': '֐-׿', 'el': 'Ͱ-Ͽἀ-῿', 'am': 'ሀ-፿', 'my': 'က-႟',
}
# Markers that must (or must not) appear somewhere in the dictionary: catches a translation in the wrong, closely related language.
MUST = {
    'fa': r'[پچژگ]', 'ur': r'[ٹڈڑںے]', 'kk': r'[әғқңөұүі]', 'mr': r'आहे|करा', 'ne': r'छ|गर्नुहोस्', 'az': r'ə',
    'ro': r'[șț]', 'cs': r'[řěů]', 'sk': r'[ľôä]', 'uz': r'ʻ', 'hu': r'[őű]', 'da': r'[æø]', 'nb': r'[æø]', 'sv': r'[åäö]',
    'fi': r'[äö]', 'hr': r'[čćđšž]', 'sr': r'[čćđšž]', 'ca': r'[àèòç]',
}
MUST_NOT = {
    'fa': r'[يك]', 'ur': r'[يك]', 'sk': r'[řěů]', 'cs': r'[ľô]', 'mr': r'(?<![ऀ-ॿ])है(?![ऀ-ॿ])',
    'ne': r'(?<![ऀ-ॿ])है(?![ऀ-ॿ])', 'ms': r'\b(?:unduh|berkas|peramban)\b', 'sr': r'[А-Яа-яЂЈЉЊЋЏђјљњћџ]|\btko\b',
    'hr': r'\bšta\b', 'az': r'(?<![A-Za-zçğıöşüə])ı?(?:yor|yorsunuz)\b', 'uz': r"\b[OoGg]'",
}
DIRECTION_MARKS = re.compile('[‎‏‪-‮⁦-⁩]')
NON_ASCII_DIGITS = re.compile('[٠-٩۰-۹०-९০-৯௦-௯౦-౯૦-૯၀-၉]')


def text_of(d):
    parts = []
    for k, v in d.items():
        for s in (v if isinstance(v, list) else [v]):
            if isinstance(s, str):
                parts.append(PH.sub(' ', TAG.sub(' ', s)))
    return ' '.join(parts)


def script_checks(code, dst):
    errs = []
    txt = text_of(dst)
    if code in SCRIPT:
        letters = re.findall(r'[^\W\d_]', txt)
        own = re.findall('[' + SCRIPT[code] + ']', txt)
        share = len(own) / max(1, len(letters))
        if share < 0.5:
            errs.append('script: only %d%% of letters are in the %s script' % (share * 100, code))
    if code in MUST and not re.search(MUST[code], txt):
        errs.append('wrong language? none of the characters/words typical of %s found (%s)' % (code, MUST[code]))
    if code in MUST_NOT:
        hits = sorted(set(re.findall(MUST_NOT[code], txt)))
        if hits:
            errs.append('wrong language? found %s (typical of a related language)' % ', '.join(hits[:5]))
    if DIRECTION_MARKS.search(txt):
        errs.append('direction control characters found (the page sets the direction itself)')
    if NON_ASCII_DIGITS.search(txt):
        errs.append('non-ASCII digits found (keep 0-9)')
    if not LANGS.get(code, {}).get('pdf', False) and re.search(r'PDF', txt):
        errs.append('mentions PDF, but this edition has no PDF export (languages.json "pdf": false)')
    if dst.get('site.name') not in (None, 'Egosaru') and code not in ('ja',):
        errs.append('site.name must be "Egosaru"')
    return errs


def check(code, src, dst):
    errs = []
    for k, v in src.items():
        if k.startswith('ja_only.'):
            continue
        if k not in dst:
            errs.append('missing key: ' + k)
            continue
        w = dst[k]
        if isinstance(v, list):
            if not isinstance(w, list) or len(w) != len(v):
                errs.append('list length differs: ' + k)
                continue
            pairs = list(zip(v, w))
        else:
            if not isinstance(w, str):
                errs.append('not a string: ' + k)
                continue
            pairs = [(v, w)]
        for a, b in pairs:
            if not isinstance(b, str) or not b.strip():
                errs.append('empty: ' + k)
                continue
            if sorted(PH.findall(a)) != sorted(PH.findall(b)):
                errs.append('placeholders differ in %s: %s vs %s' % (k, PH.findall(a), PH.findall(b)))
            if tags(a) != tags(b):
                errs.append('html tags differ in ' + k)
            if code not in ('ja', 'zh', 'zh-tw') and KANA.search(b):
                errs.append('Japanese text left in ' + k)
    own = set(LANGS.get(code, {}).get('platforms', []))   # landings only this edition has (zh-tw: yahoo)
    for k in dst:
        if k not in src and not k.startswith('ja_only.'):
            m = re.match(r'(?:intro|examples)\.([a-z]+)', k)
            if m and m.group(1) in own and ('examples.' + m.group(1)) not in src:
                continue
            errs.append('unknown key: ' + k)
    if code not in LANGS:
        errs.append('not in languages.json: ' + code)
    return errs + script_checks(code, dst)


def main():
    src = json.load(open(os.path.join(UI, 'ja.json'), encoding='utf-8'))
    codes = sys.argv[1:] or sorted(f[:-5] for f in os.listdir(UI) if f.endswith('.json') and f != 'ja.json' and not f.startswith('_'))
    import ui_source_hash
    stale = ui_source_hash.stale(ui_source_hash.load(), ui_source_hash.ja_hashes())
    bad = 0
    for code in codes:
        path = os.path.join(UI, code + '.json')
        if not os.path.isfile(path):
            print('%-6s MISSING FILE' % code)
            bad += 1
            continue
        try:
            dst = json.load(open(path, encoding='utf-8'))
        except ValueError as e:
            print('%-6s INVALID JSON: %s' % (code, e))
            bad += 1
            continue
        errs = check(code, src, dst)
        old = stale.get(code, [])
        errs += ['stale (Japanese changed since translated): ' + k for k in old if k.startswith(('pricing.', 'limit.'))]
        warn = [k for k in old if not k.startswith(('pricing.', 'limit.'))]
        print('%-6s %s' % (code, 'ok (%d keys)' % len(dst) if not errs else '%d problems' % len(errs)))
        for e in errs[:40]:
            print('       ' + e)
        if warn:
            print('       warning: %d stale keys (python scripts/ui_source_hash.py --stale)' % len(warn))
        bad += 1 if errs else 0
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
