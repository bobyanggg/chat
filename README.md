# chat

## Cursor skills

Project skills under `.cursor/skills/`.

### Outline-based research (Weizhena)

From [Weizhena/Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills) (MIT), adapted for Cursor.

| Command | Skill | Purpose |
|---------|-------|---------|
| `/research` | `research` | Generate outline (`outline.yaml` + `fields.yaml`) |
| `/research-add-items` | `research-add-items` | Add items to an existing outline |
| `/research-add-fields` | `research-add-fields` | Add fields to `fields.yaml` |
| `/research-deep` | `research-deep` | Deep-research each item to JSON |
| `/research-report` | `research-report` | Build `report.md` from JSON results |

Requires Python + `pyyaml` for JSON validation (`pip install pyyaml`).

### Cited report research (samber)

From [samber/cc-skills deep-research](https://github.com/samber/cc-skills/tree/main/skills/deep-research) (MIT), adapted for Cursor.

| Command / trigger | Skill | Purpose |
|-------------------|-------|---------|
| `/deep-research` or “research X / deep dive / landscape analysis” | `deep-research` | Parallel multi-source web research → cited Markdown report under `./research/` |

Supports 11 types (market, domain, technical, competitive, product, academic, person/org, financial, legal, trend, community). Optional PDF export if `pandoc` or `md-to-pdf` is installed.
