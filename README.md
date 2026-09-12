# chat

## Cursor skills

Project skills under `.cursor/skills/`. All of them are slash-only (`disable-model-invocation: true`). Casual chat does not start a skill.

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

| Command | Skill | Purpose |
|---------|-------|---------|
| `/deep-research` | `deep-research` | Parallel multi-source web research → cited Markdown report under `./research/` |

Slash-only: `disable-model-invocation: true`. Casual “research X / look into Y” does not start this skill.

Supports 11 types (market, domain, technical, competitive, product, academic, person/org, financial, legal, trend, community). Optional PDF export if `pandoc` or `md-to-pdf` is installed.

### Japan trip planning (abalmeo)

From [abalmeo/claude-skill-japan-recs](https://github.com/abalmeo/claude-skill-japan-recs) (MIT), adapted for Cursor.

| Command | Skill | Purpose |
|---------|-------|---------|
| `/japan-recs <area>` | `japan-recs` | Research one area (restaurants / activities / vibes) → Markdown or CSV |
| `/japan-trip <city> <days>` | `japan-trip` | Full trip plan by neighborhood → `./japan-trip/` |

Examples:

```
/japan-recs Shinjuku
/japan-recs Shinjuku --both --csv
/japan-trip Tokyo 7 days
/japan-trip Osaka 5 days --interests "ramen, nightlife"
```

Slash-only: `disable-model-invocation: true`. Markdown/CSV need no extra tools. `--sheet` needs `gws` (`npm i -g @googleworkspace/cli`).

### General trip planner (skywain)

From [skywain/trip-planner-skill](https://github.com/skywain/trip-planner-skill) (MIT), adapted for Cursor.

| Command | Skill | Purpose |
|---------|-------|---------|
| `/trip-planner` | `trip-planner` | Full trip: cities, flights, hour-by-hour days, hotels, HTML + KML |

Slash-only: `disable-model-invocation: true`. Casual “plan me 12 days in Japan” does not start this skill.

```
/trip-planner Japan, 12-15 days in October from London, mid budget, history and food
```

Needs Python 3.9+. Optional: `fast-flights` for live flight prices. Working files go in `./trips/`.

