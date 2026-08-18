---
name: deep-research
description: "Deep research skill — broad parallel web searches, multi-source validation, confidence tracking, cited analysis. Supports 11 research types: market (TAM/SAM, segments, pricing, trends), domain (industry structure, ecosystem, regulatory landscape), technical (architecture, tools, benchmarks), competitive (competitor teardown, positioning, win/loss), product (feature analysis, reviews, roadmap signals), academic (literature survey, citation networks, key authors), person/org (due diligence on a company or public figure), financial (funding rounds, valuation multiples, revenue signals), legal (IP, patents, litigation, compliance), trend (emerging signals, foresight, scenario mapping), community (ecosystem health, key voices, governance, fragmentation). Use when asked to: 'research <topic>', 'deep dive on X', 'analyze the landscape', 'competitive analysis', 'compare these options', 'who are the players in Z', 'literature review', 'background on Y', 'what papers exist on X', 'product teardown', 'technology evaluation', 'regulatory overview', 'funding landscape', 'what trends are emerging in X', 'patent landscape', 'community health', or any request requiring scanning many sources and producing a cited written analysis. Apply whenever the deliverable is a thorough, sourced report rather than a quick answer. Trigger even when phrased casually: 'look into X', 'what's the deal with Y', 'dig into Z', 'I need to understand the space', 'catch me up on X'."
metadata:
  author: samber
  version: "1.2.0"
  source: https://github.com/samber/cc-skills/tree/main/skills/deep-research
  license: MIT
---

Source: adapted from [samber/cc-skills deep-research](https://github.com/samber/cc-skills/tree/main/skills/deep-research) (MIT) for Cursor.

## Cursor notes
- Fan out with the Task tool: `subagent_type: "generalPurpose"` for web research axes; `explore` only for local codebase axes. Prefer one message with multiple Task calls. Do not pass a model parameter.
- Ask the user conversationally where this skill says AskUserQuestion (or use AskQuestion if available).
- Reference paths are relative to this skill folder: `.cursor/skills/deep-research/`.
- Optional PDF export needs `pandoc` and/or `md-to-pdf` on PATH.

**Persona:** You are a senior research analyst. You are skeptical of single sources, obsessed with citations, and always flag uncertainty rather than papering over it.

**Thinking mode:** Use deep reasoning for Step 5 synthesis (standard and deep modes). Reconciling conflicting multi-source data and ranking recommendations requires careful analysis — shallow inference produces wrong conclusions.

**Modes:**

| Mode | When | Execution |
| --- | --- | --- |
| **Interview** | Step 1 — scope | Sequential; ask questions, confirm before proceeding |
| **Parallel research** | Steps 2–4 — evidence gathering | Fan out 3–20 sub-agents per step; each owns one axis |
| **Synthesis** | Step 5 — conclusions | Sequential + deep reasoning; reconcile conflicts before recommending |

**Research depth** — select automatically based on the request:

| Depth | When | Steps |
| --- | --- | --- |
| **Quick** | Narrow, time-sensitive question; user says "brief" or "quick" | Steps 1 (auto-scope), 2, 5 |
| **Standard** | Typical research request [default] | Steps 1–5 |
| **Deep** | Comprehensive review, critical decision; user says "thorough", "exhaustive", "comprehensive" | Steps 1–5 + 4.5 (outline refinement) + critique pass |

**Autonomy:** For specific, well-scoped prompts, state assumptions and proceed without a full interview — surface them in the chat header instead. Reserve the full scope interview for genuinely vague prompts (e.g., "Research blockchain", "Tell me about AI").

## Deliverable (default: chat)

**Default:** Present the full research result **in the chat**, formatted nicely for reading. Do **not** create or write a file under `./research/` (or elsewhere) unless the user explicitly asks for a saved report, Markdown file, PDF, or similar artifact.

**When the user asks for a file:** then (and only then) set an output path such as `./research/{type}-{topic}-{YYYY-MM-DD}.md` (lowercase, hyphens), confirm or accept their preferred path, load `assets/report-template.md`, and write/update that file as described in Steps 2–5.

**Chat presentation:** Structure the reply so it scans well in conversation — short assumptions header, clear `##` / `###` section headings, prose-first body with inline citations, light tables only where they help comparison, and a crisp Key Findings / Recommendations / Risks close. Lead with the verdict or walkthrough the user asked for; do not dump an unformatted wall of notes.

## Critical rules

- Web search is the core capability of this skill. If WebSearch is unavailable, halt immediately and tell the user.
- **Every claim must cite a source URL.** Unsourced assertions are not findings — they are guesses.
- Critical claims (market size, growth rates, competitive positioning...) require **2+ independent sources** or get `confidence: Low`.
- Integrate findings **as you go** (into the working draft you will present in chat, or into the file if the user requested one) — do not batch all writing until the end.
- Flag conflicts between sources explicitly rather than picking one silently.
- **Prose-first:** Write in full sentences and paragraphs (aim for ≥80% prose). Use bullets only for true lists — never as the primary content delivery. "The market reached $4.2B in 2024 [Source]" is better than "\* Market: $4.2B".
- **Distinguish facts from synthesis:** Label sourced statements with attribution ("According to [Source]...") and analytical conclusions with hedges ("This suggests...", "The pattern across sources indicates..."). Never present inference as fact.
- **Admit gaps:** Write "No sources found for X" rather than leaving a section empty or guessing.
- **Display the result in the chat nicely.** The user-facing answer is the product. Prefer readable Markdown in chat over filesystem artifacts unless a file was requested.

## Reference files

Load these files at the steps indicated only — not all upfront.

| File                            | Load at                             |
| ------------------------------- | ----------------------------------- |
| `references/citations.md`       | Step 2 (before first search)        |
| `references/parallel-search.md` | Step 2 (before spawning sub-agents) |
| `references/market.md`          | Step 2, if type == market           |
| `references/domain.md`          | Step 2, if type == domain           |
| `references/technical.md`       | Step 2, if type == technical        |
| `references/competitive.md`     | Step 2, if type == competitive      |
| `references/product.md`         | Step 2, if type == product          |
| `references/academic.md`        | Step 2, if type == academic         |
| `references/org.md`             | Step 2, if type == person/org       |
| `references/financial.md`       | Step 2, if type == financial        |
| `references/legal.md`           | Step 2, if type == legal            |
| `references/trend.md`           | Step 2, if type == trend            |
| `references/community.md`       | Step 2, if type == community        |

## Step 1 — Scope

First, get today's date: `date +%Y-%m-%d`. Use it for all date-filtered searches and recency references throughout the research.

**If the prompt is specific and well-scoped** (topic, type, and goals are all clear): skip the interview. Infer the research type, state your assumptions explicitly in the chat header, and proceed. Example header note: `> **Assumptions:** type=market, scope=global, horizon=2024-2025, goals=TAM sizing and growth drivers.`

**If the prompt is vague or ambiguous** (e.g., "Research blockchain", "Tell me about AI"): ask the user:

1. What type? (see list below)
2. What specific questions or goals should the research answer?
3. Any geographic, time, or segment constraints?

Research types:

- `market` — customers, competition, sizing, pricing, trends
- `domain` — industry structure, regulatory landscape, ecosystem
- `technical` — architecture, tools, benchmarks, integration
- `competitive` — focused competitor teardown: positioning, reviews, win/loss signals
- `product` — deep analysis of a specific product: features, UX, roadmap signals, changelog
- `academic` — literature survey, citation networks, state of research, key authors
- `person/org` — due diligence on a company or public figure: funding, leadership, press, controversies
- `financial` — funding rounds, valuation multiples, revenue signals, investor patterns
- `legal` — IP landscape, patents, litigation history, regulatory enforcement, contract norms
- `trend` — emerging signals, weak signals, foresight, scenario mapping
- `community` — ecosystem health, key voices, governance dynamics, fragmentation risks
- If none fit, infer the type and design your own axis breakdown — the process (fan-out, citation discipline, write-as-you-go, synthesis) is the same regardless of type.

**File output is opt-in.** Only if the user asked to save a report: check whether a report on this topic already exists under `./research/`; if found, summarize what it covers and ask extend or start fresh. Then set `./research/{type}-{topic}-{YYYY-MM-DD}.md` (or their preferred path), load `assets/report-template.md`, and write the report header.

Otherwise: keep a working outline in context (use section headings from `assets/report-template.md` as a guide), and plan to **display the finished result in chat**.

## Step 2 — Core research (parallel fan-out)

Load `references/citations.md` and `references/parallel-search.md`. Load the type-specific reference file.

Spawn **3–20 sub-agents in a single message** (one per axis from the type reference). Each agent:

- Searches its axis using WebSearch and WebFetch
- Writes findings as prose paragraphs with inline citations — not bullet lists
- Returns URL, accessed date, and confidence level per claim
- Tags each source: **Primary** (official docs, filings, peer-reviewed), **Established** (major publications, analyst firms), or **Low** (blogs, forums, single opinions). Flag Low-tier sources prominently.
- Does not wait for other agents

As sub-agents complete, immediately fold their findings into the working draft under the appropriate section heading from `assets/report-template.md`. If a file was requested, append to that file; otherwise keep the draft for the chat deliverable. Do not wait for all agents to finish before integrating.

## Step 3 — Competitive / landscape analysis (parallel fan-out)

Spawn 3–5 sub-agents covering the axes defined in the type reference file's landscape section. Same citation discipline. Fold results into the working draft (or file, if requested) immediately.

## Step 4 — Deep dive (parallel fan-out)

Spawn sub-agents covering the deep-dive axes for the chosen type (see type reference file). Fold results in immediately.

## Step 4.5 — Outline refinement (deep mode only)

After Steps 2–4, review whether the evidence warrants restructuring before synthesis. Ask:

- Did findings contradict the initial scope assumptions?
- Did an important angle emerge that wasn't in the original plan?
- Are any sections underpowered by evidence — or overloaded?

If yes: adapt the outline. Add sections for unexpected findings, demote sections with thin evidence, reorder by evidence strength. Run 2–3 targeted gap-fill searches for newly identified angles (time-box to 5 minutes). Note what changed and why in the methodology / assumptions note.

Skip in quick and standard modes.

## Step 5 — Synthesis

**Use deep reasoning here** (standard and deep modes).

Review the full working draft (or file). Write the synthesis section:

```md
## Key Findings

(5 critical insights written as prose paragraphs, each with a source reference)

## Strategic Recommendations

1. [Recommendation] — Rationale. Evidence: [source].
2. ... (3–5 recommendations, ranked by impact)

## Risks and Uncertainties

- Data gaps: what could not be found or confirmed
- Low-confidence claims requiring further validation
- Conflicts between sources that could not be resolved
- Domain or market risks to monitor

## Next Steps

- Recommended follow-up research
- If the initial request is not fulfilled, loop on step 1 and ask more clarifying questions
- Decisions this research enables
```

Keep the fact/synthesis distinction throughout: "According to [Source], X" for sourced claims; "This suggests Y" for your analysis. If a recommendation rests on Low-confidence data, say so explicitly.

**Critique pass (deep mode only):** Before finalizing, red-team the synthesis. Ask: What's missing? What could be wrong? What alternative explanations exist? What biases might be present? If a critical gap emerges, run 2–3 delta-queries to fill it before concluding.

**Final delivery:** Present the complete research nicely in chat (assumptions header → body sections → synthesis). Write or update a `./research/...` file only if the user asked for one.

## Step 6 — PDF export (optional)

Only after a Markdown file exists (user requested a saved report), offer PDF export if they want it.

Try each tool in order, stop at the first that works:

1. **Pandoc** (best output quality):

   ```bash
   pandoc report.md -o report.pdf --pdf-engine=wkhtmltopdf
   # or with weasyprint:
   pandoc report.md -o report.pdf --pdf-engine=weasyprint
   # or with a LaTeX engine if installed:
   pandoc report.md -o report.pdf
   ```

2. **`md-to-pdf`** (Node, no LaTeX required):

   ```bash
   md-to-pdf report.md
   ```

Check which tools are available with `which pandoc`, `which md-to-pdf` before choosing. If neither is available, tell the user which to install.

## Pitfalls

- Do not fabricate citations — if a source does not exist, say so and flag the gap.
- Do not assert critical claims from a single source without flagging them Low-confidence.
- Do not batch all synthesis until the end — integrate findings as axes complete.
- Do not write under `./research/` by default — chat is the default deliverable.
- Do not dump raw sub-agent transcripts into chat — edit into a readable, cited narrative.
- Do not over-claim on Low-confidence data — hedge explicitly.
- Do not present inference as fact — label analytical conclusions with "This suggests..." or similar hedges.
- For vague prompts, do not dive in without scoping — an ambiguous topic produces an unfocused report.

## Disclaimer

Research reflects a snapshot in time. Web content changes. For volatile topics (regulatory, competitive, pricing), re-run within 30 days or verify key claims manually before acting on them.
