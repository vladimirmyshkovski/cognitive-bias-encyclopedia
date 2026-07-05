#!/usr/bin/env python3
"""
Validate cognitive bias entries against the canonical template.

Usage:
    python3 .github/scripts/validate.py
    python3 .github/scripts/validate.py --verbose

Exit codes:
    0 — all entries valid
    1 — validation errors found
"""

import os
import re
import sys
from pathlib import Path

# Determine repo root (script lives at .github/scripts/)
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
RU_DIR = REPO_ROOT / "ru"
CATALOG_DIR = RU_DIR / "5. Каталог"
TAXONOMY = RU_DIR / "4. Таксономия.md"
AGENTS = RU_DIR / "AGENTS.md"

REQUIRED_SECTIONS = [
    "## Определение",
    "## Пример",
    "## Механизм",
    "## Эволюционная функция",
    "## Дialectical mirror",
    "## Философские параллели",
    "## Как поймать",
    "## Как смягчить",
    "## Связанные искажения",
    "## Источники",
]

VALID_CATEGORIES = ["суждение", "память", "само", "социальное", "внимание", "вероятность"]

# External links to ignore (not part of encyclopedia catalog)
EXTERNAL_LINKS = {
    "Диалектическое и метафизическое мышление",
    "Доказательство отсутствия Бога как создателя",
    "Система — Теги",
    "AGENTS",
    "README",
    "Энциклопедия когнитивных искажений",
    "4. Таксономия",
    "1. Введение",
    "2. Эволюционные корни",
    "3. Связь с диалектическим мышлением",
    "0. Ресурсы для изучения",
    "README",
    "CONTRIBUTING_RU",
    "CONTRIBUTING",
    "LICENSE",
}


def get_catalog_files():
    """Return set of catalog file basenames (without .md)."""
    return {f.stem for f in CATALOG_DIR.glob("*.md")}


def validate_entry(filepath, catalog_files, verbose=False):
    """Validate a single catalog entry. Returns list of errors."""
    errors = []
    filename = filepath.name

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.split("\n")

    # ===== HEADER =====
    if "**Status:** `reference`" not in content:
        errors.append("Header: missing or invalid Status (must be 'reference')")
    if "**Domain:** `encyclopedia`" not in content:
        errors.append("Header: missing or invalid Domain (must be 'encyclopedia')")
    if not re.search(r"\*\*Date:\*\* \d{4}-\d{2}-\d{2}", content):
        errors.append("Header: missing or invalid Date (must be YYYY-MM-DD)")

    # ===== H1 TITLE =====
    h1_match = re.search(r"^# (.+?) \((.+?)\)$", content, re.MULTILINE)
    if not h1_match:
        errors.append("Title: missing or invalid H1 (must be '# English Name (Русское название)')")
    else:
        if verbose:
            print(f"  Title: {h1_match.group(1)} ({h1_match.group(2)})")

    # ===== METADATA BLOCK =====
    if "**Также известно как:**" not in content:
        errors.append("Metadata: missing 'Также известно как:'")
    if "**Категория:**" not in content:
        errors.append("Metadata: missing 'Категория:'")
    else:
        cat_match = re.search(r"\*\*Категория:\*\* (\S+)", content)
        if cat_match:
            cat = cat_match.group(1).rstrip(".,;:")
            if cat not in VALID_CATEGORIES:
                errors.append(
                    f"Metadata: invalid category '{cat}'. "
                    f"Must be one of: {', '.join(VALID_CATEGORIES)}"
                )
    if "**Связанные:**" not in content:
        errors.append("Metadata: missing 'Связанные:'")

    # ===== SEPARATOR =====
    separator_count = content.count("\n---\n")
    if separator_count < 1:
        errors.append("Structure: missing '---' separator after metadata block")

    # ===== REQUIRED SECTIONS IN ORDER =====
    section_positions = []
    for section in REQUIRED_SECTIONS:
        pos = content.find(f"\n{section}\n")
        if pos == -1:
            # Try with \n# at start
            pos = content.find(section)
            if pos == -1 or (pos > 0 and content[pos - 1] != "\n"):
                errors.append(f"Sections: missing '{section}'")
                continue
        section_positions.append((section, pos))

    if len(section_positions) == len(REQUIRED_SECTIONS):
        sorted_sections = sorted(section_positions, key=lambda x: x[1])
        actual_order = [s[0] for s in sorted_sections]
        if actual_order != REQUIRED_SECTIONS:
            errors.append(
                f"Sections: not in correct order. "
                f"Expected: {REQUIRED_SECTIONS}, Got: {actual_order}"
            )

    # ===== SOURCES =====
    sources_match = re.search(
        r"## Источники\n(.*?)(?=\n## |\n---\n|\Z)",
        content,
        re.DOTALL,
    )
    if sources_match:
        sources = sources_match.group(1)
        # Count bullet entries (lines starting with "- ")
        entries = re.findall(r"^- ", sources, re.MULTILINE)
        if len(entries) < 3:
            errors.append(
                f"Sources: only {len(entries)} entries "
                f"(need ≥3: 2 academic + 1 Wikipedia)"
            )
        if "wikipedia.org" not in sources.lower():
            errors.append("Sources: missing Wikipedia link")

    # ===== DIALECTICAL MIRROR =====
    dm_match = re.search(
        r"## Дialectical mirror\n(.*?)(?=\n## |\n---\n|\Z)",
        content,
        re.DOTALL,
    )
    if dm_match:
        dm_content = dm_match.group(1)
        if "Диалектическое и метафизическое мышление" not in dm_content:
            errors.append(
                "Дialectical mirror: should link to "
                "[[Диалектическое и метафизическое мышление]]"
            )

    # ===== WIKI-LINKS RESOLVE =====
    wikilink_pattern = re.compile(r"\[\[([^\[\]\n]+?)\]\]")
    for match in wikilink_pattern.finditer(content):
        link_full = match.group(1).strip()
        # Skip aliases (text after |)
        if "|" in link_full:
            link_full = link_full.split("|")[0].strip()
        # Skip heading anchors
        if "#" in link_full:
            link_full = link_full.split("#")[0].strip()
        # Strip known prefixes
        for prefix in ("ru/5. Каталог/", "5. Каталог/"):
            if link_full.startswith(prefix):
                link_full = link_full[len(prefix):]
        # Skip external/known links
        if not link_full or link_full in EXTERNAL_LINKS:
            continue
        # Check if resolves to catalog file
        if link_full not in catalog_files:
            errors.append(f"Wiki-link broken: [[{match.group(1)}]]")

    # ===== RELATED-LINKS COUNT =====
    related_match = re.search(
        r"## Связанные искажения\n(.*?)(?=\n## |\Z)",
        content,
        re.DOTALL,
    )
    if related_match:
        related_section = related_match.group(1)
        # Count [[wiki-links]] in this section
        related_links = re.findall(r"\[\[", related_section)
        if len(related_links) < 3:
            errors.append(
                f"Связанные искажения: only {len(related_links)} links "
                f"(need ≥3 for Антиизоляция)"
            )

    return errors


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    if not CATALOG_DIR.exists():
        print(f"ERROR: Catalog directory not found: {CATALOG_DIR}")
        sys.exit(2)

    catalog_files = get_catalog_files()
    catalog_list = sorted(CATALOG_DIR.glob("*.md"))

    print(f"Validating {len(catalog_list)} entries in ru/5. Каталог/")
    print(f"Valid categories: {', '.join(VALID_CATEGORIES)}")
    print()

    all_errors = {}
    for filepath in catalog_list:
        if verbose:
            print(f"📄 {filepath.name}")
        errors = validate_entry(filepath, catalog_files, verbose=verbose)
        if errors:
            all_errors[filepath.name] = errors

    print()
    if all_errors:
        print(f"❌ Validation FAILED: {len(all_errors)} file(s) with errors")
        print()
        for filename, errors in all_errors.items():
            print(f"📄 {filename}:")
            for error in errors:
                print(f"   - {error}")
            print()
        sys.exit(1)
    else:
        print(f"✅ All {len(catalog_list)} entries pass validation")
        print("   - 10 mandatory sections in correct order")
        print("   - Required metadata (Status, Date, Domain, aliases, category, related)")
        print("   - Wiki-links resolve to existing files")
        print("   - At least 3 sources (2 academic + Wikipedia)")
        print("   - Dialectical mirror section present")
        sys.exit(0)


if __name__ == "__main__":
    main()