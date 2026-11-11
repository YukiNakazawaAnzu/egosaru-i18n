# UI translation brief (エゴサる / Egosaru)

Source of truth: `application/language/ui/ja.json`. You write `application/language/ui/<code>.json` in the same folder:
same keys, same order, UTF-8 JSON (`ensure_ascii=false`, indent 1). Check with `python scripts/validate_ui_lang.py <code>` until it prints `ok`.

## What the product is
Egosaru is a free web tool that collects the search-autocomplete suggestions ("suggest") of Google, Bing, YouTube, Amazon and
DuckDuckGo for a keyword and expands them in one go: the keyword + a space, + each native letter, + A–Z, + 0–9. Results can be
copied or exported as CSV. A free JSON API exists. Visitors are bloggers, SEO people, e-commerce sellers and marketers.
The Japanese site also covers Rakuten and Yahoo! Japan; other languages do not.

## Rules
1. Translate for a native reader of the target language: natural, idiomatic, helpful, SEO-minded. Not word for word.
2. Keep every key. Do not add or drop keys. Keys starting with `ja_only.` are Japan-only: do **not** include them.
3. Keep `{placeholders}` exactly (same names, any position, any number of times as the sentence needs). Never translate them.
4. Keep HTML tags and attributes (`<a href="{url}">…</a>`) unchanged; translate only the text between tags.
5. Strings that are JSON lists keep the same number of items (`date.months` = 12 month names, `examples.*` = 3 items, `intro.*.uses` = same count).
6. Brand: write **Egosaru** (Latin letters) wherever the Japanese says エゴサる (`site.name` = "Egosaru"). Google, Bing, YouTube, Amazon, DuckDuckGo, CSV, PDF, API, JSON, SEO, FAQ stay as they are.
7. Japanese-only mechanics must be rewritten, not translated. The Japanese text talks about kana (あ〜ん, あ行〜わ行, 50音). In your language the tool
   adds, after the keyword: a space, the language's own extra letters (if any) and A–Z and 0–9. `{expand}` is the list of those groups, e.g. `А–Я, A–Z, 0–9`.
   Describe that accurately. Do not claim "100+ combinations"; say "dozens of variations" / "hundreds of related terms" instead.
8. Remove Japan-market claims ("国内最大級", "日本語環境では", Rakuten) and replace them with true, neutral statements about the service in general.
   Do not invent numbers, prices, features or guarantees that are not in the source.
9. `examples.<platform>`: three realistic searches people in that language/country really make for that platform (not translations of the Japanese ones).
   Mix of everyday topics, avoid sensitive, adult, political or brand-defamation terms. `landing.api_sample_q` is one short everyday keyword.
10. `common.sep` is the separator used when listing items ("Google, Bing, YouTube": ", " or " / " or "、" as is normal in your language).
11. `date.format` is a PHP `date()` format for a short numeric date in your locale (e.g. `d.m.Y`, `Y/m/d`, `d/m/Y`). `date.months`: 12 month names in the form used before a year
    ("October 2026" → `date.month_year` = `{month} {year}`; adapt word order/particles if your language needs it).
12. Titles and meta descriptions (`*.title*`, `*.meta*`) are search-result snippets: keep them natural and about 60 / 155 characters or less where the Japanese is similar in length.
13. UI labels (buttons, tabs, aria texts) must be short.
14. Right-to-left (ar, fa, ur, he): translate normally; do not insert direction marks (U+200E/F, U+202A–E, U+2066–9). Keep `{placeholders}` and Latin words as they are.
15. `result.summary` is "main <n> / <groups> expansion": keep both placeholders.
16. No Japanese characters may remain (zh / zh-tw may use Han characters naturally).
17. Numbers stay as ASCII digits (0-9) everywhere, also in Arabic-script, Bengali, Devanagari and Burmese text (prices, limits, "50").
18. `header.region_*` are the four group titles of the language menu (Asia / Middle East & Africa / Europe / Americas): short.
    `pricing.unavailable` replaces the buy buttons in editions where paid plans are not sold: one neutral sentence.
19. PDF export exists only where `languages.json` has `"pdf": true` (ja, en). Every other edition must not mention PDF:
    "CSV・PDF" becomes "CSV" (e.g. `platform.meta`, `landing.step3_d`, `landing.feat3_t`, `landing.feat3_d`).
20. Translation engine: Claude Opus or Fable only (owner's rule: not Sonnet / Haiku). Aim for natural native wording, not a calque of the Japanese.

## Fixed terms (glossary)
Before the dictionary, write `application/language/ui/glossary/<code>.json` (format: `glossary/ja.json`): the one word or phrase your
language uses for each concept below, then use exactly those words in the dictionary and in the API docs (`api_app/docs/i18n/<code>.json`).

| key | meaning |
|---|---|
| `suggest` | search autocomplete suggestions (the service's core noun) |
| `keyword` | keyword typed into the search box |
| `expand` | the expansion: adding a space, letters, A–Z, 0–9 after the keyword |
| `related` | related keywords / searches |
| `new_keyword` | "new keyword" = a keyword not fetched yet (the paid-plan quota unit) |
| `cached` | already fetched and cached (7 days) |
| `api_key` | API key |
| `free` | free of charge (not "free trial") |
| `negation_volume` | the sentence "Egosaru does not show search volume" in your language (the negation must survive) |

## Register per language
ru: formal "вы". uk: "ви", real Ukrainian (no Russian calques). zh: Simplified Chinese, mainland vocabulary. zh-tw: Traditional Chinese, Taiwan vocabulary.
ko: polite formal (합니다/하세요체). es: neutral international Spanish, "tú". pt: Brazilian Portuguese, "você". fr: French (France), "vous". de: German, "Sie".
it: "tu". id: Indonesian, "Anda". vi: "bạn". th: Thai, polite and gender-neutral (no ครับ/ค่ะ). tr: "siz". ar: Modern Standard Arabic.
hi: Hindi (Devanagari), "आप"; common SEO terms may stay in Latin script. pl: Polish, direct and friendly. nl: Dutch, "je/jij".
bn: Bengali (Bangladesh and West Bengal), "আপনি"; standard written Bengali (চলিত ভাষা); SEO/tech terms may stay in Latin script.
ur: Urdu, "آپ"; Naskh rendering is fine; Urdu letters (ٹ ڈ ڑ ں ے ہ ی), not Arabic substitutes.
ms: Malay (Malaysia), "Anda"; Malaysian vocabulary (muat turun, fail, pelayar, carian), not Indonesian (unduh, berkas, peramban, pencarian).
ta: Tamil, "நீங்கள்"; formal written Tamil; SEO/tech terms may stay in Latin script.
fa: Persian (Iran), "شما"; Persian letters (پ چ ژ گ, ی not ي, ک not ك); ZWNJ (U+200C) where Persian orthography needs it.
ro: Romanian, "dumneavoastră"; ș and ț with comma below (U+0219, U+021B). hu: Hungarian, "Ön". el: Greek, "εσείς", monotonic orthography.
ca: Catalan (central standard), "vostè". he: Hebrew, avoid gendered second person where possible (infinitives / impersonal forms); no niqqud.
sw: Swahili (standard, Kenya and Tanzania), "wewe"; English tech terms acceptable where common. fil: Filipino, "ikaw/mo" without "po"; English tech terms are normal.
kk: Kazakh in Cyrillic, "Сіз" (letters ә ғ қ ң ө ұ ү һ і). cs: Czech, "vy". sv: Swedish, "du". da: Danish, "du".
te: Telugu, "మీరు". mr: Marathi, "तुम्ही"; Marathi function words (आहे, आणि, करा), not Hindi (है, और, करें).
uz: Uzbek in Latin script, "siz"; oʻ gʻ with U+02BB (ʻ). sr: Serbian in Latin script only, "Vi"; ekavian, Serbian vocabulary (ko, šta, pretraga), not Croatian.
bg: Bulgarian, "Вие". hr: Croatian, "Vi"; ijekavian, Croatian vocabulary (tko, što, tražilica). sk: Slovak, "vy" (no Czech ř/ě/ů). fi: Finnish, "sinä".
nb: Norwegian Bokmål, "du" (not Danish spellings). ne: Nepali, "तपाईं"; Nepali function words (छ, गर्नुहोस्, र), not Hindi. gu: Gujarati, "તમે".
az: Azerbaijani in Latin script, "siz" (ə, not Turkish spellings). am: Amharic, "እርስዎ" (formal); Ethiopic script. my: Burmese, polite register; Unicode (not Zawgyi).

## Tone
Friendly, clear, professional; second person where the language normally uses it; no exclamation marks unless the Japanese has them.
