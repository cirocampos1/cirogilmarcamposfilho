---
name: concise-planning
description: Use when a user asks for a plan for a coding task, to generate a clear, actionable, and atomic checklist.
version: 3.0
architecture_focus: "Option B"
last_updated: 2026-03-28
verification_script: "scripts/verify.py"
---

# Concise Planning

## Goal

Turn a user request into a **single, actionable plan** with atomic steps.

## Workflow

### 1. Scan Context

- Read `README.md`, docs, and relevant code files.
- Identify constraints (language, frameworks, tests).

### 2. Minimal Interaction

- Ask **at most 1–2 questions** and only if truly blocking.
- Make reasonable assumptions for non-blocking unknowns.

### 3. Generate Plan

Use the following structure:

- **Approach**: 1-3 sentences on what and why.
- **Scope**: Bullet points for "In" and "Out".
- **Action Items**: A list of 6-10 atomic, ordered tasks (Verb-first).
- **Validation**: At least one item for testing.

## Plan Template

```markdown
# Plan

<High-level approach>

## Scope

- In:
- Out:

## Action Items

[ ] <Step 1: Discovery>
[ ] <Step 2: Implementation>
[ ] <Step 3: Implementation>
[ ] <Step 4: Validation/Testing>
[ ] <Step 5: Rollout/Commit>

## Open Questions

- <Question 1 (max 3)>
```

## Checklist Guidelines

- **Atomic**: Each step should be a single logical unit of work.
- **Verb-first**: "Add...", "Refactor...", "Verify...".
- **Concrete**: Name specific files or modules when possible.


## 🚀 Option B: Efficiency Guidelines (MANDATORY)

1. **Direct Action**: Never explain what you are going to do. Just do it.
2. **Token Economy**: Minimize chatter. Use the most concise tool calls possible.
3. **Verification First**: Run validation scripts immediately after any change.
4. **GPU Acceleration**: Use local GPU/Ollama for heavy analysis tasks when possible.
