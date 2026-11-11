# Suggest API docs — translation brief

Source of truth: `api_app/docs/i18n/ja.json`. A reviewed English version is in `i18n/en.json` (use it to understand the Japanese, but translate the meaning, not the English wording).
You write `api_app/docs/i18n/<code>.json`: same keys, same order, UTF-8 JSON (`ensure_ascii=False`, indent 1).
Check with `PYTHONIOENCODING=utf-8 python api_app/docs/build_docs.py --check` and fix every line that starts with your language code
(lines about other languages that are not written yet can be ignored). Do not run the build without `--check` and do not edit any other file.

## What the page is
Developer documentation for "Suggest API" on gstudio1.com: a JSON API (free plan and paid plans) that returns search-autocomplete
suggestions ("suggest") of Google, Bing, YouTube, Amazon, eBay, Shopee, DuckDuckGo and regional engines (Baidu, Yandex, Naver, Daum,
Yahoo!, Rakuten Ichiba), in the site's 50 languages. Japanese is expanded with kana, other languages with a space and the language's own
letters; all with A–Z and 0–9. Readers are developers. The page layout, code samples and endpoint paths are fixed in `template.html`;
you only translate the strings. Use the same fixed terms as the site dictionary's glossary (`suggest/application/language/ui/glossary/<code>.json`).

## Rules
1. Translate for a native developer audience: clear, natural, concise technical writing. Not word for word.
2. Keep every key; do not add or drop keys. Keep the key order.
3. Keep HTML tags exactly (`<code>`, `<strong>`, `<a href="%login_url%">`). Translate only the text between tags. Never translate what is inside `<code>…</code>`.
4. Keep `%login_url%` exactly. `{source}` inside `<code>` is literal and stays.
5. Do not change facts. Translate what the Japanese says (engines, markets, `lang` codes, limits, numbers, HTTP codes, the 7-day cache)
   and do not add or drop any of them. Do not invent features, prices or guarantees.
6. Japanese-only mechanics: "五十音展開 / あ〜ん" means "expansion with the Japanese kana syllabary". Explain it in your language; you may quote `あ–ん`
   (this is the only kana allowed outside `<code>`). No other Japanese characters may remain (zh / zh-tw use Han characters naturally, but no kana).
7. Keep as is: Suggest API, gstudio1.com, Google, Bing, YouTube, Amazon.co.jp, Yahoo!, DuckDuckGo, JSON, API, SLA, UTC, HTTP header names.
   Rakuten: "Rakuten Ichiba" in Latin letters (or the established local name if one exists).
8. `meta.title` stays exactly `Suggest API | gstudio1.com`. `meta.description` is a search snippet: natural, about 155 characters or less.
9. `ui.language` is the word "Language" (label of the language selector). `param.required` is a short parenthesized "(required)".
   `ex.queued` / `ex.ready` are 1–2 word labels used in code comments (`// 202 (queued)`).
10. The user menu item is called "API" in every language; quote it with the quotation marks normal in your language.
11. For common UI terms ("log in", "suggest/autocomplete", "API key") reuse the wording of the site's dictionary
    `public_html/gstudio1.com/suggest/application/language/ui/<code>.json` (e.g. `nav.login`, `landing.api_title`) so the site and the docs match.
12. Right-to-left (ar): translate normally; do not insert direction marks; keep Latin words and tags as they are.

## Tone
Neutral, professional; second person where the language normally uses it in docs; no exclamation marks.
