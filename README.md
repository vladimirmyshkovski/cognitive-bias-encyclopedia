# Cognitive Bias Encyclopedia / Энциклопедия когнитивных искажений

**An open, multilingual encyclopedia of cognitive biases.**
**Открытая многоязычная энциклопедия когнитивных искажений.**

🌐 **[Live site → vladimirmyshkovski.github.io/cognitive-bias-site](https://vladimirmyshkovski.github.io/cognitive-bias-site/)**

---

## Languages / Языки

- 🇷🇺 **[Русский / Russian](ru/)** — 84 записи, полная версия
- 🇬🇧 **[English](en/)** — coming soon / в разработке (skeleton only, see `en/CONTRIBUTING.md`)

> **Note**: All entries follow a strict 10-section template for consistent rendering (see [CONTRIBUTING.md](CONTRIBUTING.md)). The rendered website is built automatically from the Russian entries on every push to `main` (see [cognitive-bias-site](https://github.com/vladimirmyshkovski/cognitive-bias-site)).

---

## About

This encyclopedia catalogues **cognitive biases** — systematic errors in thinking that affect human judgment and decision-making. Unlike alphabetical lists, we group biases by **function** (judgment, memory, self, social, attention, probability) and connect each to its **evolutionary origin**, **dialectical mirror**, and **philosophical parallels** (Stoics, Buddhism, Kant, Nietzsche, Socrates).

**Author**: Vladimir Myshkovski
**License**: [CC BY-SA 4.0](LICENSE)
**Status**: Active development, open to contributions

---

## Structure

Each language directory contains:

```
<lang>/
├── CONTRIBUTING.md         ← rules for adding new entries (was AGENTS.md)
├── AGENTS.md               ← rules for AI agents (English edition only)
├── 0. Ресурсы / Resources.md
├── 1. Введение / Introduction.md
├── 2. Эволюционные корни / Evolutionary Roots.md
├── 3. Связь с диалектическим / Dialectical Link.md
├── 4. Таксономия / Taxonomy.md          ← master catalog of all biases
└── 5. Каталог / Catalog/                ← individual bias entries
```

---

## Deployment / Деплой

Сайт собирается автоматически: пуш в `main` этого репозитория отправляет
`repository_dispatch` в [cognitive-bias-site](https://github.com/vladimirmyshkovski/cognitive-bias-site),
и тот пересобирает и публикует сайт на GitHub Pages.

**Чтобы это работало**, в этом репозитории нужен секрет `SITE_DISPATCH_TOKEN` —
токен с правом на вызов `repository_dispatch` в репозиторий
`vladimirmyshkovski/cognitive-bias-site` (нужен скоуп `repo`).

> **Settings → Secrets and variables → Actions → New repository secret**
>
> - Name: `SITE_DISPATCH_TOKEN`
> - Secret: значение PAT

Секрет настроен (2026-11-08). Если секрет не задан, workflow не падает — он пишет
warning в лог и пропускает пересборку. Сайт при этом просто не обновится автоматически.

> **Узкий вариант.** Сейчас используется classic PAT общего назначения — у него
> скоупы шире, чем нужно для одной задачи. Минимально достаточная замена:
> fine-grained PAT на `cognitive-bias-site` с правом **Contents: Read and write**
> (или **Actions: Read and write**) и сроком действия в несколько месяцев.

Обратная связь работает в одну сторону: пуш в сайт не трогает контент.

---

## How to contribute

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Template structure (10 mandatory sections)
- Naming conventions (English-first filenames)
- Cross-linking policy
- Quality checklist

**Ways to contribute:**
1. Add a missing bias (currently ~84 of ~180 known biases are documented)
2. Improve an existing entry (add sources, examples, philosophical parallels)
3. Translate to a new language (English is the next priority)
4. Fix typos, broken links, formatting

Open an **Issue** or submit a **Pull Request**.

---

## Statistics

| Metric | Value |
|--------|-------|
| Languages available | 1 (Russian) |
| Total biases documented | 84 |
| Coverage of known biases | ~48% (of ~180) |
| Open priority items | ~11 (средний приоритет) |

See the [Taxonomy](https://github.com/vladimirmyshkovski/cognitive-bias-encyclopedia/blob/main/ru/4.%20%D0%A2%D0%B0%D0%BA%D1%81%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F.md) for the full master catalog.

---

## See also

- **[Cognitive Bias Codex](https://upload.wikimedia.org/wikipedia/commons/8/8a/Cognitive_Bias_Codex.jpg)** by John Manoogian III (visual reference)
- **[Wikipedia: Cognitive bias](https://en.wikipedia.org/wiki/Cognitive_bias)** (canonical English list)
- **[Buster Benson's Cognitive Bias Codex](https://betterhumans.pub/cognitive-bias-cheat-sheet-55a461476b03)** (curated categorization)
- Kahneman, D. (2011). *Thinking, Fast and Slow*
- Dobelli, R. (2013). *The Art of Thinking Clearly*

---

**Last updated**: 2026-07-05
**Version**: 0.3 (multilingual structure)