---
name: obsidian-bases-skill
description: - Use when creating or editing `.base` files in Obsidian. - Use for database-like note views with filters, formulas, summaries, or cards/tables. - Use when the user asks about Obsidian Bases specifica
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Obsidian Bases Skill

## Backstory

Você é um agente especializado em Obsidian Bases Skill.

## Contexto Original da Skill
Obsidian Bases Skill

## Instruções
---
name: obsidian-bases
description: Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files, creating database-like views of notes, or when the user mentions Bases, table views, card views, filters, or formulas in Obsidian.
risk: unknown
source: "https://github.com/kepano/obsidian-skills"
date_added: "2026-03-21"
---

# Obsidian Bases Skill

## When to Use

- Use when creating or editing `.base` files in Obsidian.
- Use for database-like note views with filters, formulas, summaries, or cards/tables.
- Use when the user asks about Obsidian Bases specifically.

## Workflow

1. **Create the file**: Create a `.base` file in the vault with valid YAML content
2. **Define scope**: Add `filters` to select which notes appear (by tag, folder, property, or date)
3. **Add formulas** (optional): Define computed properties in the `formulas` section
4. **Configure views**: Add one or more views (`table`, `cards`, `list`, or `map`) with `order` specifying which properties to display
5. **Validate**: Verify the file is valid YAML with no syntax errors. Check that all referenced properties and formulas exist. Common issues: unquoted strings containing special YAML characters, mismatched quotes in formula expressions, referencing `formula.X` without defining `X` in `formulas`
6. **Test in Obsidian**: Open the `.base` file in Obsidian to confirm the view renders correctly. If it shows a YAML error, check quoting rules below

## Schema

Base files use the `.base` extension and contain valid YAML.

```yaml
# Global filters apply to ALL views in the base
filters:
  # Can be a single filter string
  # OR a recursive filter object with and/or/not
  and: []
  or: []
  not: []

# Define formula properties that can be used across all views
formulas:
  formula_name: 'expression'

# Configure display names and settings for properties
properties:
  property_name:
    displayName: "Display Name"
  formula.formula_name:
    displayName: "Formula Display Name"
  file.ext:
    displayName: "Extension"

# Define custom summary formulas
summaries:
  custom_summary_name: 'values.mean().round(3)'

# Define one or more views
views:
  - type: table | cards | list | map
    name: "View Name"
    limit: 10                    # Optional: limit results
    groupBy:                     # Optional: group results
      property: property_name
      direction: ASC | DESC
    filters:                     # View-specific filters
      and: []
    order:                       # Properties to display in order
      - file.name
      - property_name
      - formula.formula_name
    summaries:                   # Map properties to summary formulas
      property_name: Average
```

## Filter Syntax

Filters narrow down results. They can be applied globally or per-view.

### Filter Structure

```yaml
# Single filter
filters: 'status == "done"'

# AND - all conditions must be true
filters:
  and:
    - 'status == "done"'
    - 'prior

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

- Use when creating or editing `.base` files in Obsidian. - Use for database-like note views with filters, formulas, summaries, or cards/tables. - Use when the user asks about Obsidian Bases specifica

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Obsidian Bases Skill
- Para tarefas relacionadas a obsidian bases skill

## Diretrizes Específicas

