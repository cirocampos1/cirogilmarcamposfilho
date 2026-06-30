---
name: drift-check
description: On-demand validation to detect Specification Drift. Compares recent unmerged changes on the master branch against ORQUESTRA.md and local specs before Rafa merges to Main.
metadata:
  category: validation
  triggers:
    - "check drift"
    - "drift check"
    - "validar contra orquestra"
    - "pre-merge audit"
---

# Drift Check (Anti-Drift Mechanism)

This skill executes an on-demand validation of the current code state against the primary specification (`ORQUESTRA.md`) and local specs. It is specifically designed to support the workflow of 7 developers coding on the `master` branch and Rafa performing the merge to `Main`.

## When to Use
Invoke this skill BEFORE handing over the code to Rafa for the final merge, or when Rafa is performing the review on `master` before pushing to `Main`. It ensures that the rapid pace of development hasn't caused "Specification Drift" (code evolving away from documented rules).

## Workflow

1. **Extract Recent Changes (Git Diff):**
   Run a `git diff` against the last stable commit or the `Main` branch to see what the 7 devs have introduced on `master`.
   *Command:* `git diff origin/Main...HEAD` (or examine the latest commits on `master`).

2. **Semantic Verification with Graphify:**
   Use the `graphify query` command to understand the semantic intent of the new changes.
   *Example:* `graphify query "What are the latest changes in the database schema or core business logic compared to ORQUESTRA.md?"`

3. **Validation against ORQUESTRA.md:**
   Read the `ORQUESTRA.md` file using `view_file` to ensure that:
   - No architectural rules were violated.
   - Design guidelines (WOW) and SDD methodologies were followed.
   - Code conventions are preserved.

4. **Generate the Drift Report:**
   Output a concise summary for the developers or for Rafa:
   - **🔴 Drift Detected:** Areas where the code contradicts the spec. (e.g., "A new UI component was added but it doesn't follow the Tailwind baseline").
   - **🟢 Compliant:** Areas aligned with the spec.
   - **🟡 Spec Needs Update:** If the code change is correct but the spec is outdated, recommend updating the spec to reflect the new reality (reverse-engineering).

## Principles
- **Non-blocking:** Because it's an on-demand skill, it doesn't block local commits. It acts as an audit layer.
- **Rafa's Assistant:** This is the ultimate tool to speed up Rafa's merge review, providing him with a summarized checklist of what might be breaking the `ORQUESTRA.md` contract.
