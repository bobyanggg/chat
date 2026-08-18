---
name: research-deep
description: Read a research outline and deeply research each item into structured JSON via parallel agents. Use after /research when the user invokes /research-deep or asks to run deep investigation on an outline.
disable-model-invocation: true
---

# Research Deep - Deep Research

Source: adapted from [Weizhena/Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills) (MIT) for Cursor.

## Trigger
`/research-deep`

## Cursor notes
- Use Task (`generalPurpose`, `run_in_background: true`) for each agent batch. Do not inherit a different model.
- Validation script path: `.cursor/skills/research/validate_json.py` (requires `pyyaml`).
- Web researcher guidance: `.cursor/skills/research/references/web-search-agent.md` and modules under `.cursor/skills/research/references/web-search-modules/`.

## Workflow

### Step 1: Auto-locate Outline
Find `*/outline.yaml` file in current working directory, read items list, execution config (including items_per_agent).

### Step 2: Resume Check
- Check completed JSON files in output_dir
- Skip completed items

### Step 3: Batch Execution
- Batch by batch_size (need user approval before next batch)
- Each agent handles items_per_agent items
- Launch web-researcher Tasks (background parallel)

**Parameter Retrieval**:
- `{topic}`: topic field from outline.yaml
- `{item_name}`: item's name field
- `{item_related_info}`: item's complete yaml content (name + category + description etc.)
- `{output_dir}`: execution.output_dir from outline.yaml (default: ./results)
- `{fields_path}`: absolute path to {topic}/fields.yaml
- `{output_path}`: absolute path to {output_dir}/{item_name_slug}.json (slugify item_name: replace spaces with _, remove special chars)
- `{repo_root}`: absolute path to the git/workspace root (where `.cursor/skills` lives)

**Hard Constraint**: The following prompt must be strictly reproduced, only replacing variables in {xxx}, do not modify structure or wording.

**Prompt Template**:
```python
prompt = f"""## Task
Research {item_related_info}, output structured JSON to {output_path}

## Field Definitions
Read {fields_path} to get all field definitions

## Web research
Follow .cursor/skills/research/references/web-search-agent.md
Load relevant modules from .cursor/skills/research/references/web-search-modules/ before searching.
Use WebSearch and WebFetch.

## Output Requirements
1. Output JSON according to fields defined in fields.yaml
2. Mark uncertain field values with [uncertain]
3. Add uncertain array at the end of JSON, listing all uncertain field names
4. All field values must be in English

## Output Path
{output_path}

## Validation
After completing JSON output, run validation script to ensure complete field coverage:
python {repo_root}/.cursor/skills/research/validate_json.py -f {fields_path} -j {output_path}
Task is complete only after validation passes.
"""
```

**One-shot Example** (assuming researching GitHub Copilot):
```
## Task
Research name: GitHub Copilot
category: International Product
description: Developed by Microsoft/GitHub, first mainstream AI coding assistant, ~40% market share, output structured JSON to {project_dir}/results/GitHub_Copilot.json

## Field Definitions
Read {project_dir}/fields.yaml to get all field definitions

## Web research
Follow .cursor/skills/research/references/web-search-agent.md
Load relevant modules from .cursor/skills/research/references/web-search-modules/ before searching.
Use WebSearch and WebFetch.

## Output Requirements
1. Output JSON according to fields defined in fields.yaml
2. Mark uncertain field values with [uncertain]
3. Add uncertain array at the end of JSON, listing all uncertain field names
4. All field values must be in English

## Output Path
{project_dir}/results/GitHub_Copilot.json

## Validation
After completing JSON output, run validation script to ensure complete field coverage:
python {repo_root}/.cursor/skills/research/validate_json.py -f {project_dir}/fields.yaml -j {project_dir}/results/GitHub_Copilot.json
Task is complete only after validation passes.
```

### Step 4: Wait and Monitor
- Wait for current batch to complete
- Ask user before launching next batch
- Display progress

### Step 5: Summary Report
After all complete, output:
- Completion count
- Failed/uncertain marked items
- Output directory

## Agent Config
- Background execution: Yes
- Resume support: Yes
