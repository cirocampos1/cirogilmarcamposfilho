---
name: codex-review
description: Professional code review with auto CHANGELOG generation, integrated with Codex AI
version: 3.0
architecture_focus: "Option B"
last_updated: 2026-03-28
verification_script: "scripts/verify.py"
---

# codex-review

## Overview
Professional code review with auto CHANGELOG generation, integrated with Codex AI

## When to Use
- When you want professional code review before commits
- When you need automatic CHANGELOG generation
- When reviewing large-scale refactoring

## Installation
```bash
npx skills add -g BenedictKing/codex-review
```

## Step-by-Step Guide
1. Install the skill using the command above
2. Ensure Codex CLI is installed
3. Use `/codex-review` or natural language triggers

## Examples
See [GitHub Repository](https://github.com/BenedictKing/codex-review) for examples.

## Best Practices
- Keep CHANGELOG.md in your project root
- Use conventional commit messages

## Troubleshooting
See the GitHub repository for troubleshooting guides.


## 🚀 Option B: Efficiency Guidelines (MANDATORY)

1. **Direct Action**: Never explain what you are going to do. Just do it.
2. **Token Economy**: Minimize chatter. Use the most concise tool calls possible.
3. **Verification First**: Run validation scripts immediately after any change.
4. **GPU Acceleration**: Use local GPU/Ollama for heavy analysis tasks when possible.

## Related Skills
- context7-auto-research, tavily-web, exa-search, firecrawl-scraper
