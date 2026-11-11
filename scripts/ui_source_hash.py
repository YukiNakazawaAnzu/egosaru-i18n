#!/usr/bin/env python3
"""Records which version of the Japanese source each translation was made from (DateSealed's _source_hash.json method).

    python scripts/ui_source_hash.py ru ko      after (re)translating these languages: store the hash of every ja.json value
    python scripts/ui_source_hash.py --all      same for every language file (use once to start tracking)
    python scripts/ui_source_hash.py --stale    list, per language, the keys whose Japanese changed since they were translated

application/language/ui/_source_hash.json = {language: {key: first 8 hex of sha1(ja value)}}.
validate_ui_lang.py reports stale keys as warnings (pricing.* and limit.* as errors).
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
UI = os.environ.get('EGOSARU_UI_DIR') or os.path.join(HERE, '..', 'application', 'language', 'ui')
PATH = os.path.join(UI, '_source_hash.json')


def ja_hashes():
    src = json.load(open(os.path.join(UI, 'ja.json'), encoding='utf-8'))
    return {k: hashlib.sha1(json.dumps(v, ensure_ascii=False).encode('utf-8')).hexdigest()[:8]
            for k, v in src.items() if not k.startswith('ja_only.')}


def load():
    return json.load(open(PATH, encoding='utf-8')) if os.path.isfile(PATH) else {}


def languages():
    return sorted(f[:-5] for f in os.listdir(UI) if f.endswith('.json') and f != 'ja.json' and not f.startswith('_'))


def stale(stored, cur):
    return {code: sorted(k for k, h in cur.items() if keys.get(k) != h) for code, keys in stored.items()}


def main():
    args = sys.argv[1:]
    cur = ja_hashes()
    data = load()
    if args == ['--stale']:
        for code, keys in sorted(stale(data, cur).items()):
            if keys:
                print('%-6s %d stale: %s' % (code, len(keys), ', '.join(keys[:20])))
        return
    codes = languages() if args == ['--all'] else args
    for code in codes:
        data[code] = dict(cur)
    json.dump(dict(sorted(data.items())), open(PATH, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1, sort_keys=True)
    print('recorded', len(codes), 'languages')


if __name__ == '__main__':
    main()
