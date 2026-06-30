---
name: project-handoff
description: Automated technical documentation generation for project finalization. Scans specs, analyzes architecture via graphify, and produces ARCHITECTURE.md, API_SPEC.md, and MAINTENANCE.md.
---

# Project Handoff Skill

This skill automates the creation of high-quality technical documentation at the end of a project cycle.

## Workflow

1. **Information Gathering**:
   - Run `graphify update .` to ensure the Knowledge Graph is current.
   - Read `graphify-out/GRAPH_REPORT.md` to identify core modules and dependencies.
   - Scan `specs/` for the implementation specs and task lists.
   - **Traceability Check**: Verify if the `## 🔗 Rastreabilidade de Código` section in the `spec.md` is fully populated.
   - Identify active API routes, database schemas, and external integrations (Sankhya).

2. **Document Generation**:

### [NEW] ARCHITECTURE.md
- Include a **Mermaid.js** diagram showing the module relationships.
- Describe the data flow and technology stack.
- List key "God Nodes" identified by Graphify.

### [NEW] API_SPEC.md
- Document all REST/GraphQL endpoints.
- Provide JSON examples for requests and responses.
- List authentication requirements and common error codes.

### [NEW] MAINTENANCE.md
- **Setup Guide**: How to run the project from scratch.
- **Environment Variables**: Mandatory keys and their purpose.
- **Known Issues/Debt**: Document what wasn't fixed or needs future attention.
- **Deployment**: Specific steps for production.

3. **Validation**:
   - Ensure all links in the documentation are valid.
   - Check if Mermaid diagrams render correctly.

## Quality Standards (Pro-Max)

- Use **GitHub Alerts** (`> [!NOTE]`, `> [!IMPORTANT]`) for emphasis.
- Use **Mermaid.js** for all visualizations.
- Ensure the tone is professional, technical, and concise.
- **No Placeholders**: If information is missing, flag it as a TODO or research it.
