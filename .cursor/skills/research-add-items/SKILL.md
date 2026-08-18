---
name: research-add-items
description: Add research objects (items) to an existing research outline.yaml. Use when the user invokes /research-add-items or wants to expand the item list after /research.
disable-model-invocation: true
---

# Research Add Items - Supplement Research Objects

Source: adapted from [Weizhena/Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills) (MIT) for Cursor.

## Trigger
`/research-add-items`

## Cursor notes
- Ask the user conversationally (or use AskQuestion if available).
- For optional web search, follow `.cursor/skills/research/references/web-search-agent.md` and load modules under `.cursor/skills/research/references/web-search-modules/`.

## Workflow

### Step 1: Auto-locate Outline
Find `*/outline.yaml` file in current working directory, auto-read.

### Step 2: Get Supplement Sources in Parallel
Simultaneously:
- **A. Ask user**: What items to supplement? Any specific names?
- **B. Ask if Web Search needed**: Launch agent to search for more items?

### Step 3: Merge and Update
- Append new items to outline.yaml
- Display to user for confirmation
- Avoid duplicates
- Save updated outline

## Output
Updated `{topic}/outline.yaml` file (in-place modification)
