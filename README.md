# Egosaru translations

**Help improve Egosaru in your language / あなたの言語でエゴサるをよくする手伝いを:**

[日本語](docs/ja.md) · [简体中文](docs/zh.md) · [繁體中文](docs/zh-tw.md) · [हिन्दी](docs/hi.md) · [Bahasa Indonesia](docs/id.md) · [한국어](docs/ko.md) · [Tiếng Việt](docs/vi.md) · [ไทย](docs/th.md) · [বাংলা](docs/bn.md) · [اردو](docs/ur.md) · [Bahasa Melayu](docs/ms.md) · [தமிழ்](docs/ta.md) · [Filipino](docs/fil.md) · [Қазақша](docs/kk.md) · [తెలుగు](docs/te.md) · [मराठी](docs/mr.md) · [Oʻzbekcha](docs/uz.md) · [नेपाली](docs/ne.md) · [ગુજરાતી](docs/gu.md) · [မြန်မာ](docs/my.md) · [العربية](docs/ar.md) · [Türkçe](docs/tr.md) · [فارسی](docs/fa.md) · [עברית](docs/he.md) · [Kiswahili](docs/sw.md) · [Azərbaycanca](docs/az.md) · [አማርኛ](docs/am.md) · [Français](docs/fr.md) · [Русский](docs/ru.md) · [Deutsch](docs/de.md) · [Italiano](docs/it.md) · [Polski](docs/pl.md) · [Українська](docs/uk.md) · [Nederlands](docs/nl.md) · [Română](docs/ro.md) · [Magyar](docs/hu.md) · [Ελληνικά](docs/el.md) · [Català](docs/ca.md) · [Čeština](docs/cs.md) · [Svenska](docs/sv.md) · [Dansk](docs/da.md) · [Srpski](docs/sr.md) · [Български](docs/bg.md) · [Hrvatski](docs/hr.md) · [Slovenčina](docs/sk.md) · [Suomi](docs/fi.md) · [Norsk bokmål](docs/nb.md) · [English](docs/en.md) · [Español](docs/es.md) · [Português](docs/pt.md)

The interface text of [Egosaru](https://gstudio1.com/suggest/en/posts/google) (a free tool that collects search autocomplete suggestions from Google, Bing, YouTube, Amazon and more, expanded letter by letter) and of its [Suggest API documentation](https://gstudio1.com/api/en/), in 50 languages.

**The translations were written with AI (Claude) and have not been reviewed by native speakers yet. If you read one of these languages, you can make them better.** It takes a minute.

## The easiest way: report one sentence

Open an [issue with the translation form](../../issues/new/choose), pick the language, paste the sentence that sounds wrong and write what it should say. That is all. No GitHub account? Use the [contact form](https://gstudio1.com/suggest/en/contact).

## Editing the files yourself

- [`lang/`](lang/): the site's interface text, one file per language (`fr.json`, `bn.json`, …). The Japanese file [`lang/ja.json`](lang/ja.json) is the source; [`lang/en.json`](lang/en.json) is a reviewed English version that helps to understand it.
- [`lang/glossary/`](lang/glossary/): the fixed words of each language (the word for "suggest", "keyword", "API key" …). Keep them consistent.
- [`api-docs/`](api-docs/): the strings of the API documentation pages.

You can edit a file in your browser (the pencil icon on GitHub) and open a pull request. A check runs automatically and tells you if something is off (a missing key, a broken `{placeholder}` or HTML tag, text in the wrong script or language); we also read each change before using it.

## Please keep

- **The keys and their order.** Change only the values (the text on the right).
- **`{placeholders}` and HTML tags** exactly as they are.
- **Facts.** Do not add features, numbers, prices or promises the Japanese/English text does not make. Egosaru does **not** show search volume.
- **Brand and product names** in Latin letters: Egosaru, Google, Bing, YouTube, Amazon, DuckDuckGo, Suggest API, CSV, JSON.
- **Digits 0–9** (no Arabic-Indic, Persian, Bengali, Devanagari or Burmese digits), and no direction-control characters in right-to-left languages.

More detail: [TRANSLATION_BRIEF.md](TRANSLATION_BRIEF.md), [API_DOCS_BRIEF.md](API_DOCS_BRIEF.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## Thanks for volunteers

People who send useful fixes can get a free API key with higher limits (the same limits as the Starter plan) as thanks. Mention it in your issue or pull request if you would like one; we set it up by hand.

## Credit and license

Contributors are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md) (tell us if you would rather not be). Contributions are made available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and are used on gstudio1.com.

Egosaru is developed by Yuki Nakazawa and operated by SkyClear Co., Ltd.

---

## 日本語

[エゴサる](https://gstudio1.com/suggest/) の画面の文言と [Suggest API のドキュメント](https://gstudio1.com/api/) を 50 言語で管理しています。翻訳は AI（Claude）で作ったもので、母語話者の確認はまだです。不自然な文を見つけたら、[翻訳の修正フォーム](../../issues/new/choose)から、言語・今の文・直した文を送ってください。1 文だけでも助かります。GitHub のアカウントが無い場合は[お問い合わせ](https://gstudio1.com/suggest/contact)からどうぞ。

原文は [`lang/ja.json`](lang/ja.json) です。役に立つ修正を送ってくださった方には、お礼として上限を広げた無料の API キー（Starter プランと同じ上限）をお渡しします。希望される場合は issue か pull request に書いてください。
