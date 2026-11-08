# CONTRIBUTING.md — English edition (skeleton)

> **Status:** Stub. The English translation is planned but not yet started.

## Goal

Translate the Russian encyclopedia (61 entries as of 2026-07) into English, following the same 10-section template and using the same alias paths so the renderer can build both.

## Structure (planned)

```
en/
├── CONTRIBUTING.md                ← this file
├── AGENTS.md                      ← rules for English-language entries
├── 0. Resources.md
├── 1. Introduction.md
├── 2. Evolutionary Roots.md
├── 3. Dialectical Link.md
├── 4. Taxonomy.md
└── 5. Catalog/                    ← translated entries, one file per bias
    └── Confirmation Bias.md       ← first entry, translation of ru/5. Каталог/Confirmation Bias.md
```

## Where to start

1. Translate the **foundational files** (`0–3`) first — they establish terminology for the catalog
2. Then translate **one entry from each category** as a reference style
3. Translate the rest of the catalog in batches

## Translation guidelines

- Keep the **same H1 format**: `# English Name (Russian name)` — Russian names in parentheses help Russian-speaking readers cross-reference
- **Aliases**: include the original Russian term if commonly used in English literature (e.g. "Loss Aversion (Неприятие потерь)")
- **Категории → Categories**: use the English category names (суждение → Judgment, память → Memory, etc.)
- **Wiki-links** in `## Связанные искажения` should use English filenames: `[[Anchoring]]` instead of `[[ru/5. Каталог/Anchoring]]`
- **Wikipedia link**: replace the Russian Wikipedia link with the English one
- **Sources**: prefer English-language sources when available; Russian-only sources can stay with a note

## Tag convention

| Russian | English |
|---------|---------|
| суждение | judgment |
| память | memory |
| само | self |
| социальное | social |
| внимание | attention |
| вероятность | probability |

## Status

- [ ] `0. Resources.md`
- [ ] `1. Introduction.md`
- [ ] `2. Evolutionary Roots.md`
- [ ] `3. Dialectical Link.md`
- [ ] `4. Taxonomy.md`
- [ ] `5. Catalog/Confirmation Bias.md` (sample, English-first)
- [ ] (rest of the catalog — 60 entries)

## See also

- `ru/CONTRIBUTING.md` — original Russian rules and template
- `AGENTS.md` (Obsidian vault root, outside this repo) — vault-wide instructions
- `README.md` — project overview