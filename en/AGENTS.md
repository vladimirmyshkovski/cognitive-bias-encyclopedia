# AGENTS.md — English edition

> **Audience:** AI agents (Claude / GPT / others) writing or editing entries in `en/`.
> **Status:** Stub. The Russian edition in `ru/` is canonical; English mirrors it.

---

## 0. TL;DR

- English edition is a **1:1 translation** of the Russian edition. Don't add new content; mirror the structure.
- Each entry follows the **same 10-section template** as `ru/` (see `ru/CONTRIBUTING.md`).
- Tag taxonomy mirrors Russian, in English (judgment/memory/self/social/attention/probability).
- Filenames: English (`Confirmation Bias.md`, **not** `Подтверждение предвзятости.md`).

---

## 1. Layout

```
en/
├── AGENTS.md                  ← this file
├── CONTRIBUTING.md            ← translation guidelines
├── 0. Resources.md
├── 1. Introduction.md
├── 2. Evolutionary Roots.md
├── 3. Dialectical Link.md
├── 4. Taxonomy.md
└── 5. Catalog/                ← one file per bias (English filename)
    └── Confirmation Bias.md   ← English-first name
```

## 2. Entry template (mirror of ru/)

Same 10 sections as `ru/CONTRIBUTING.md`:

1. Определение → **Definition**
2. Пример → **Example**
3. Механизм → **Mechanism**
4. Эволюционная функция → **Evolutionary Function**
5. Диалектическое зеркало → **Dialectical Mirror** (keep this English section name — same as on the live site)
6. Философские параллели → **Philosophical Parallels**
7. Как поймать → **How to Catch**
8. Как смягчить → **How to Mitigate**
9. Связанные искажения → **Related Biases**
10. Источники → **Sources**

## 3. Header

```markdown
**Status:** `reference`
**Date:** YYYY-MM-DD
**Domain:** `encyclopedia`

# Confirmation Bias (Предвзятость подтверждения)
```

Russian name in parentheses is **kept** — it helps Russian-speaking readers cross-reference and matches the file-naming convention of the Russian edition.

## 4. Categories (English)

| English | Russian | When to use |
|---------|---------|-------------|
| **judgment** | суждение | оценка информации, аргументов, вариантов |
| **memory** | память | искажение воспоминаний, hindsight |
| **self** | само | самооценка, самоатрибуция |
| **social** | социальное | влияние других людей, групп, иерархии |
| **attention** | внимание | что замечаем, что игнорируем |
| **probability** | вероятность | оценка вероятностей, рисков, шансов |

## 5. Cross-references

- `[[Anchoring]]` — no path prefix needed (we're in `en/` already)
- Reference the English name, not the Russian one
- The site renderer maps `[[Anchoring]]` → `/biases/anchoring/`

## 6. Sources

- **Prefer English-language sources**: Kahneman 2011, Dobelli 2013, etc.
- Keep one Russian Wikipedia link if the Russian article is significantly better than English
- English Wikipedia link is **required** (one of the standard sources)

## 7. Anti-patterns

- ❌ Don't add new biases that aren't in `ru/`
- ❌ Don't paraphrase in ways that lose meaning
- ❌ Don't translate philosophical terms with loose equivalents — keep proper nouns in original (Kant, Nietzsche, Sartre)
- ❌ Don't add English-only concepts that have no Russian equivalent (yet)

## 8. See also

- `../ru/CONTRIBUTING.md` — full template and validation rules
- `../AGENTS.md` (root) — vault-wide rules
- `../README.md` — project overview