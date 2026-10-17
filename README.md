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

Needs Python 3.9+. Optional: `fast-flights` for live flight prices (`scripts/flight_scan.py`). Working files go in `./trips/`.

### Flight price report (danny0926)

From [danny0926/flight-report](https://github.com/danny0926/flight-report) (MIT), adapted for Cursor.

| Command | Skill | Purpose |
|---------|-------|---------|
| `/flight-report` | `flight-report` | Google Flights 比價 → `./flight-report/` 繁中報告 |

Slash-only: `disable-model-invocation: true`. Casual “找機票 / 國泰多少” does not start this skill.

```
/flight-report 桃園到東京 2027/2/14-2/28 玩5~6天 全服務
/flight-report TPE NRT 2027-02-20 to 2027-02-25 round-trip
```

Needs `fast-flights` (`pip install fast-flights`). Reports go in `./flight-report/`.

