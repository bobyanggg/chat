---
name: research-add-fields
description: Add field definitions to an existing research fields.yaml. Use when the user invokes /research-add-fields or wants to expand the field schema after /research.
disable-model-invocation: true
---

# Research Add Fields - Supplement Research Fields

Source: adapted from [Weizhena/Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills) (MIT) for Cursor.

## Trigger
`/research-add-fields`

## Cursor notes
- Ask the user conversationally (or use AskQuestion if available).
- For optional web search, follow `.cursor/skills/research/references/web-search-agent.md` and load modules under `.cursor/skills/research/references/web-search-modules/`.

## Workflow

### Step 1: Auto-locate Fields File
Find `*/fields.yaml` file in current working directory, auto-read existing fields definitions.

### Step 2: Get Supplement Source
Ask user to choose:
- **A. User direct input**: User provides field names and descriptions
- **B. Web Search**: Launch agent to search common fields in this domain

### Step 3: Display and Confirm
- Display suggested new fields list
- User confirms which fields to add
- User specifies field category and detail_level

### Step 4: Save Update
Append confirmed fields to fields.yaml, save file.

## Output
Updated `{topic}/fields.yaml` file (in-place modification, requires user confirmation)
