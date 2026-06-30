---
name: architecture
description: Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisions or analyzing system design.
allowed-tools: Read, Glob, Grep
version: 3.0
architecture_focus: "Option B"
last_updated: 2026-03-28
verification_script: "scripts/verify.py"
---

# Architecture Decision Framework

> "Requirements drive architecture. Trade-offs inform decisions. ADRs capture rationale."

## 🎯 Selective Reading Rule

**Read ONLY files relevant to the request!** Check the content map, find what you need.

| File | Description | When to Read |
|------|-------------|--------------|
| `context-discovery.md` | Questions to ask, project classification | Starting architecture design |
| `trade-off-analysis.md` | ADR templates, trade-off framework | Documenting decisions |
| `pattern-selection.md` | Decision trees, anti-patterns | Choosing patterns |
| `examples.md` | MVP, SaaS, Enterprise examples | Reference implementations |
| `patterns-reference.md` | Quick lookup for patterns | Pattern comparison |

---

## 🔗 Related Skills

| Skill | Use For |
|-------|---------|
| `@[skills/database-design]` | Database schema design |
| `@[skills/api-patterns]` | API design patterns |
| `@[skills/deployment-procedures]` | Deployment architecture |

---

## Core Principle

**"Simplicity is the ultimate sophistication."**

- Start simple
- Add complexity ONLY when proven necessary
- You can always add patterns later
- Removing complexity is MUCH harder than adding it

---

## Validation Checklist

Before finalizing architecture:

- [ ] Requirements clearly understood
- [ ] Constraints identified
- [ ] Each decision has trade-off analysis
- [ ] Simpler alternatives considered
- [ ] ADRs written for significant decisions
- [ ] Team expertise matches chosen patterns


## 🚀 Option B: Efficiency Guidelines (MANDATORY)

1. **Direct Action**: Never explain what you are going to do. Just do it.
2. **Token Economy**: Minimize chatter. Use the most concise tool calls possible.
3. **Verification First**: Run validation scripts immediately after any change.
4. **GPU Acceleration**: Use local GPU/Ollama for heavy analysis tasks when possible.
