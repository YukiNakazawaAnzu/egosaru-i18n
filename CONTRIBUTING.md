# Contributing a translation

Thank you. A few rules keep the translations correct and consistent.

1. **Write for a native reader.** Natural, clear, friendly and professional. Not word for word.
2. **Do not promise more than the source.** Egosaru collects autocomplete suggestions; it does not show search volume, does not remove suggestions, and offers PDF export only in Japanese and English. Do not add numbers, prices, features or guarantees.
3. **Keep keys, key order, `{placeholders}` and HTML tags.** Only change the text.
4. **Consistency.** Use the words in `lang/glossary/<code>.json` for "suggest", "keyword", "expand", "new keyword", "API key" and "free" everywhere in your language (site and API docs). If you think a glossary word is wrong, change it in the glossary and everywhere it is used, in one pull request.
5. **Brand and technical names stay in Latin letters:** Egosaru, Google, Bing, YouTube, Amazon, eBay, Shopee, DuckDuckGo, Baidu, Yandex, Naver, Daum, Suggest API, CSV, JSON, API.
6. **Digits 0–9 only.** No direction-control characters in Arabic, Persian, Urdu or Hebrew.
7. **The Japanese file `lang/ja.json` is the source** and is maintained by the Egosaru team. If you think the source itself is unclear or wrong, open an issue.

## Checking your change

```
EGOSARU_UI_DIR=lang EGOSARU_LANGUAGES_JSON=config/languages.json python scripts/validate_ui_lang.py fr
python scripts/validate_api_docs.py fr
```

Both print `ok` when the file is fine. A pull request runs the same checks automatically, so you do not have to.

## License and credit

By submitting a change you agree that it may be used on gstudio1.com and is made available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). We list contributors in `CONTRIBUTORS.md`; say so if you prefer not to be listed. Volunteers who send useful fixes can ask for a free API key with higher limits as thanks.
