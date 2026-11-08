# Changelog

All notable changes to the Cognitive Bias Encyclopedia are documented here. Format: [Keep a Changelog](https://keepachangelog.com/). Versions follow [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### Added

- **Автоматическая пересборка сайта**: workflow `notify-site.yml` отправляет `repository_dispatch` типа `content-update` в `cognitive-bias-site` при каждом пуше в `main`. Требуется секрет `SITE_DISPATCH_TOKEN` (fine-grained PAT с правом Contents: Read and write на репозиторий сайта); без него пересборка пропускается с warning, CI не падает

### Fixed

- **validate.py**: `AGENTS = RU_DIR / "AGENTS.md"` указывал на несуществующий файл (переименован в `CONTRIBUTING.md`); в `EXTERNAL_LINKS` `"AGENTS"` заменено на `"CONTRIBUTING"`, чтобы устаревшая ссылка ловилась валидатором. Добавлена проверка существования `CONTRIBUTING.md` и `4. Таксономия.md` — переименование этих файлов теперь ломает CI, а не проходит молча
- **Битые ссылки после переименования AGENTS.md → CONTRIBUTING.md**: `[[AGENTS]]` в `ru/4. Таксономия.md` → `[[CONTRIBUTING]]`; в схемах структуры (`README.md`, `ru/CONTRIBUTING.md`) исправлено имя файла; markdown-ссылки `[AGENTS.md](../../AGENTS.md)` в `ru/CONTRIBUTING.md` вели на несуществующий путь — заменены на wiki-ссылку `[[AGENTS]]` (корневой AGENTS.md лежит в Obsidian-хранилище, вне репозитория)
- **Форматирование**: убран trailing whitespace в CHANGELOG, восстановлен горизонтальный разделитель `---` в записи [0.3] (слипся с текстом пункта), в `ru/0`…`ru/3` возвращена пустая строка после `---` — как в остальных файлах

- **OG image generation**: refactored from Astro integration hook (which failed with "Vite module runner has been closed") to standalone Node script. Generates 62 PNGs (61 entries + default) using `@fontsource/inter` instead of a broken bundled WOFF
- **Repository structure**: removed `scripts/symlink-content.sh` (machine-specific, replaced by `CONTENT_PATH` env var)
- **Dependencies**: removed unused `@astrojs/rss` and `flowbite` packages; added `@fontsource/inter` for OG generation
- **Documentation**: created `en/` skeleton (AGENTS.md + CONTRIBUTING.md) for the planned English translation
- **Documentation**: renamed `ru/AGENTS.md` → `ru/CONTRIBUTING.md` to disambiguate from the root `AGENTS.md` (the encyclopedia-specific file describes how to contribute, the root describes vault-wide agent rules)
- **Documentation**: updated site README with current architecture (post-OG-fixes)

### Migration planned (not done in this release)

- `loadAllBiases()` → Astro Content Collections. Plan documented in `docs/MIGRATION_TO_CONTENT_COLLECTIONS.md`. Current implementation is functional but uses direct file reads instead of Astro's built-in collection API. Target: ~4-6 hours of focused work.

---

## [0.4] — 2026-07-29

### Fixed

- **Search bug**: search input button was hidden below 1024px breakpoint — mobile users had no access to search. Now icon is always visible; "Поиск..." label appears from 640px+
- **Search magnifier icon**: Pagefind renders the magnifier via `.pagefind-ui__form::before` with `mask-image` (not `background-image`). My earlier `background-image: none` fix didn't work. Replaced with `display: none !important` on the `::before` pseudo-element
- **Search results highlighting**: added yellow `<mark>` styling (yellow-200 / yellow-600 in dark mode) for matched terms in result titles and excerpts
- **Pagination**: added pagination to `/biases/` (pageSize 24) and category pages. URLs: `/biases/`, `/biases/page/2/`, `/categories/<name>/`, `/categories/<name>/page/2/`
- **Description rendering**: extended `renderMarkdown()` to accept `base` parameter; catalog wiki-links now produce kebab-case URLs (`availability-heuristic`) with the correct base prefix; non-catalog wiki-links (e.g. `[[Диалектическое мышление]]`) render as plain italic text instead of broken 404 links
- **OG description**: was leaking raw markdown (`**bold**`) and was truncated mid-word. Now uses `stripMarkdown()` + `truncateDescription()` (cuts at sentence boundary within 155 chars)
- **Footer links**: `CONTRIBUTING.md` and `LICENSE` now point to GitHub repo (they don't exist on the deployed site)
- **Internal links**: fixed `404` issues on category links by adding missing `/categories/` index page

### Changed

- **Navbar logo**: changed from "Cognitive Bias Encyclopedia" / "CBE" to "Энциклопедия" (with full name in `sr-only` span for screen readers)
- **Home page H1**: changed from "Cognitive Bias Encyclopedia" to "Энциклопедия когнитивных искажений"
- **Header consistency**: fixed `Dunning-Kruger.md` H1 from "Dunning-Kruger Effect" to "Dunning-Kruger" (matches the filename and the 11 inbound `[[Dunning-Kruger]]` wiki-links)
- **Definition lengths**: expanded 5 shortest definitions (Optimism Bias, Loss Aversion, Backfire Effect, In-group Bias, Anchoring) from <30 words to 40-80 words. Compressed 4 longest definitions (Motivated Reasoning, Barnum-Forer, Mandela, Hawthorne) by moving historical context into "Пример" section

### Added

- `src/components/Pagination.astro` — reusable pagination component
- `src/components/Search.astro` — fullscreen modal overlay for Pagefind search (replaces inline `<div>` that was invisible)
- `scripts/generate-og.ts` — standalone OG image generator (run via `npm run og` after `astro build`)

### Content quality

- Fixed 5 quote attribution errors:
  - `Reactance`: Сартр → Камю (`L'Homme révolté` is Camus, not Sartre)
  - `Cognitive Dissonance`: rephrased dubious Nietzsche quote as paraphrase
  - `Motivated Reasoning`: rephrased dubious Nietzsche quote as paraphrase
  - `Mandela Effect`: kept Nietzsche but marked as paraphrase (no verbatim quote)
  - `Frequency Illusion`: removed duplicated Nietzsche paraphrase
  - `In-group Bias`: cited Kant's categorical imperative properly (*Основы метафизики нравов*, 1785)
- Removed `[[Доказательство отсутствия Бога как создателя]]` (article doesn't exist) from 9 entries (FAE + 8 others)
- Added back-links to 18 orphaned entries (now 0 orphans in the catalog graph)
- Renamed `## Дialectical mirror` → `## Диалектическое зеркало` across all 61 entries (typo fix)
- Translated English fragment-indicators (e.g. "Diversify your sources", "Reading across the aisle") to Russian; kept academic psychology terms (e.g. "Cognitive dissonance reduction", "Diffusion of responsibility") as-is

---

## [0.3] — 2026-07-05

### Added

- Initial multilingual structure with `ru/` and planned `en/`
- 10-section template documented in `ru/AGENTS.md`
- Inline metadata convention (`**Status:**`, `**Date:**`, `**Tags:**`) instead of YAML frontmatter

---

## [0.2] — 2026-07-05

### Added

- 29th entry (Authority Bias) — first entry to follow the formalized AGENTS.md template
- Strict template rules: 10 sections in fixed order, H1 format `# English (Русский)`, category taxonomy (6 canonical categories)

---

## [0.1] — Initial

### Added

- 34 cognitive biases in Russian (initial commit)
- Obsidian-vault structure with inline metadata
- CC BY-SA 4.0 license