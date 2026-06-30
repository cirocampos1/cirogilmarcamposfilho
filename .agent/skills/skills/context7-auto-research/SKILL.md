---
name: context7-auto-research
description: Automatically fetch latest library/framework documentation for Claude Code via Context7 API
version: 3.0
architecture_focus: "Option B"
last_updated: 2026-03-28
verification_script: "scripts/verify.py"
---

# context7-auto-research

## Overview
Automatically fetch latest library/framework documentation for Claude Code via Context7 API

## When to Use
- When you need up-to-date documentation for libraries and frameworks
- When asking about React, Next.js, Prisma, or any other popular library

## Installation
```bash
npx skills add -g BenedictKing/context7-auto-research
```

## Step-by-Step Guide
1. Install the skill using the command above
2. Configure API key (optional, see GitHub repo for details)
3. Use naturally in Claude Code conversations

## Examples
See [GitHub Repository](https://github.com/BenedictKing/context7-auto-research) for examples.

## Best Practices
- Configure API keys via environment variables for higher rate limits
- Use the skill's auto-trigger feature for seamless integration

## Troubleshooting
See the GitHub repository for troubleshooting guides.


## 🚀 Option B: Efficiency Guidelines (MANDATORY)

1. **Direct Action**: Never explain what you are going to do. Just do it.
2. **Token Economy**: Minimize chatter. Use the most concise tool calls possible.
3. **Verification First**: Run validation scripts immediately after any change.
4. **GPU Acceleration**: Use local GPU/Ollama for heavy analysis tasks when possible.

## Related Skills
- tavily-web, exa-search, firecrawl-scraper, codex-review
