# Contributing to the Cognitive Bias Encyclopedia

Thank you for your interest in this project! This guide is for **humans** who want to add a new cognitive bias, improve an existing entry, or translate the encyclopedia into another language. (AI agents should see [[AGENTS]] for their specific rules.)

## Project Overview

The Cognitive Bias Encyclopedia is an **open, multilingual** reference documenting systematic errors in human thinking. We currently have **34 entries** in Russian and are working toward **~180** known biases. The unique angle of this project:

- Grouping by **function** (judgment, memory, self, social, attention, probability) rather than alphabet
- Connection to **evolutionary origin** of each bias
- **Dialectical mirror** — each bias as a shadow of a useful heuristic
- **Philosophical parallels** — Stoics, Buddhism, Kant, Nietzsche, Socrates
- Strong **cross-linking** between entries

## How to Contribute

### 1. Open an Issue First

Before starting work, open an Issue describing:
- **What** you want to add or change
- **Why** it matters (link to research, real-world example)
- **Which sources** you used

This avoids duplicate work and aligns approach.

### 2. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/cognitive-bias-encyclopedia.git
cd cognitive-bias-encyclopedia
```

### 3. Create a Branch

```bash
git checkout -b add-bias-name
# or
git checkout -b improve-existing-bias
# or
git checkout -b translate-to-language
```

### 4. Add or Modify the Entry

**Adding a new bias** — follow [[AGENTS]] strictly (10 sections, English-first filenames, 6 categories, 3–5 cross-references).

**Improving existing** — add examples, sources, philosophical parallels. Do not change structure unless necessary.

**Translating** — create `en/` (or `de/`, `fr/`, etc.) directory and mirror the structure of `ru/`.

### 5. Quality Check

Before opening a Pull Request, verify:

- [ ] File follows the 10-section template (correct order)
- [ ] All wiki-links resolve (open in Obsidian, check clickability)
- [ ] Category is correct (one of 6: judgment, memory, self, social, attention, probability)
- [ ] At least 2 academic sources + Wikipedia link
- [ ] Added to [[4. Taxonomy]] (if new bias)
- [ ] File added to README.md table

### 6. Pull Request

Create a PR describing:
- **What** changed
- **Why** (Issue link)
- **How to verify** (any special instructions)

If you added new tags, verify `obsidian tags --strict` returns 0 errors.

---

## What NOT to Do

- ❌ **No YAML frontmatter** — this project uses inline metadata (`**Status:**`, `**Date:**`, `**Domain:**`)
- ❌ **No Russian filenames** — `Confirmation Bias.md`, not `Предвзятость подтверждения.md`
- ❌ **No extra sections** without coordination (open an Issue first)
- ❌ **No skipping `## Dialectical mirror`** — this is our unique feature
- ❌ **No first-person voice** — articles should be impersonal
- ❌ **No emoji** in content (clean academic style)

---

## Source Quality

**Accepted:**
- Peer-reviewed journal articles
- Books from academic publishers
- Verified online resources (Wikipedia, Britannica, YourBias.is)

**Not accepted:**
- Anonymous blogs
- Reddit, Quora, Stack Exchange
- AI-generated text without human editing
- Self-citation (unless original research)

---

## Categories

Each entry must have **exactly one** category:

| Category | When to use |
|----------|-------------|
| **judgment** | Evaluating information, arguments, choices |
| **memory** | Distortion of recollections |
| **self** | Self-assessment, self-attribution |
| **social** | Influence of others, groups, hierarchies |
| **attention** | What we notice, what we ignore |
| **probability** | Evaluating probabilities, risks, chances |

Full list of existing biases — see [[4. Taxonomy]].

---

## Translation Workflow

If you want to translate the encyclopedia:

1. Create a new directory `xx/` (where `xx` is the language code: `en`, `de`, `fr`, etc.)
2. Mirror the structure of `ru/`
3. Translate file contents, but **keep technical terms** in English (e.g., "Confirmation Bias" stays English; only the description is translated)
4. Update `README.md` to add a link to your language
5. Add your language to the statistics table

Currently supported languages:
- 🇷🇺 Russian (`ru/`) — full, 34 entries
- 🇬🇧 English (`en/`) — coming soon

---

## License

All contributions are licensed under **CC BY-SA 4.0**:
- Free to use, modify, distribute
- Attribution required
- Derivative works must use the same license

Full text in `LICENSE`.

---

## Code of Conduct

- Be respectful in discussions
- Use data, not opinions, to justify claims
- When in doubt, ask in an Issue before doing
- Remember: goal is quality reference material, not maximum speed

---

## See Also

- [[AGENTS]] — instructions for AI agents
- [[README]] — project overview
- [[4. Taxonomy]] — master catalog of all known biases
- [Cognitive Bias Codex](https://upload.wikimedia.org/wikipedia/commons/8/8a/Cognitive_Bias_Codex.jpg) — visual classification by John Manoogian III
- [Wikipedia: Cognitive bias](https://en.wikipedia.org/wiki/Cognitive_bias)
- Buster Benson's [Cognitive Bias Codex](https://betterhumans.pub/cognitive-bias-cheat-sheet-55a461476b03)

---

**Document version**: 1.0
**License**: CC BY-SA 4.0