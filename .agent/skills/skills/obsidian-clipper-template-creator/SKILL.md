---
name: obsidian-clipper-template-creator
description: Guide for creating templates for the Obsidian Web Clipper. Use when you want to create a new clipping template, understand available variables, or format clipped content.
version: 3.0
architecture_focus: "Option B"
last_updated: 2026-03-28
verification_script: "scripts/verify.py"
---

# Obsidian Web Clipper Template Creator

This skill helps you create importable JSON templates for the Obsidian Web Clipper.

## Workflow

1.  **Identify User Intent:** specific site (YouTube), specific type (Recipe), or general clipping?
2.  **Check Existing Bases:** The user likely has a "Base" schema defined in `Templates/Bases/`.
    *   **Action:** Read `Templates/Bases/*.base` to find a matching category (e.g., `Recipes.base`).
    *   **Action:** Use the properties defined in the Base to structure the Clipper template properties.
    *   See [references/bases-workflow.md](references/bases-workflow.md) for details.
3.  **Fetch & Analyze Reference URL:** Validate variables against a real page.
    *   **Action:** Ask the user for a sample URL of the content they want to clip (if not provided).
    *   **Action:** Use `WebFetch` to retrieve the page HTML.
    *   **Action:** Analyze the HTML for Schema.org JSON, Meta tags, and CSS selectors.
    *   See [references/analysis-workflow.md](references/analysis-workflow.md) for analysis techniques.
4.  **Draft the JSON:** Create a valid JSON object following the schema.
    *   See [references/json-schema.md](references/json-schema.md).
5.  **Verify Variables:** Ensure the chosen variables (Preset, Schema, Selector) exist in your analysis.
    *   See [references/variables.md](references/variables.md).

## Output Format

**ALWAYS** output the final result as a JSON code block that the user can copy and import.

```json
{
  "schemaVersion": "0.1.0",
  "name": "My Template",
  ...
}
```

## Resources

*   [references/variables.md](references/variables.md) - Available data variables.
*   [references/filters.md](references/filters.md) - Formatting filters.
*   [references/json-schema.md](references/json-schema.md) - JSON structure documentation.
*   [references/bases-workflow.md](references/bases-workflow.md) - How to map Bases to Templates.
*   [references/analysis-workflow.md](references/analysis-workflow.md) - How to validate page data.

### Official Documentation
*   [Variables](https://help.obsidian.md/web-clipper/variables)
*   [Filters](https://help.obsidian.md/web-clipper/filters)
*   [Templates](https://help.obsidian.md/web-clipper/templates)

## Examples

See [assets/](assets/) for JSON examples.


## 🚀 Option B: Efficiency Guidelines (MANDATORY)

1. **Direct Action**: Never explain what you are going to do. Just do it.
2. **Token Economy**: Minimize chatter. Use the most concise tool calls possible.
3. **Verification First**: Run validation scripts immediately after any change.
4. **GPU Acceleration**: Use local GPU/Ollama for heavy analysis tasks when possible.
