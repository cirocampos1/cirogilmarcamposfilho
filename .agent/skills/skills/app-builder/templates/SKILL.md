---
name: templates
description: Project scaffolding templates for new applications. Use when creating new projects from scratch. Contains 12 templates for various tech stacks.
allowed-tools: Read, Glob, Grep
version: 3.0
architecture_focus: "Option B"
last_updated: 2026-03-28
verification_script: "scripts/verify.py"
---

# Project Templates

> Quick-start templates for scaffolding new projects.

---

## 🎯 Selective Reading Rule

**Read ONLY the template matching user's project type!**

| Template | Tech Stack | When to Use |
|----------|------------|-------------|
| [nextjs-fullstack](nextjs-fullstack/TEMPLATE.md) | Next.js + Prisma | Full-stack web app |
| [nextjs-saas](nextjs-saas/TEMPLATE.md) | Next.js + Stripe | SaaS product |
| [nextjs-static](nextjs-static/TEMPLATE.md) | Next.js + Framer | Landing page |
| [express-api](express-api/TEMPLATE.md) | Express + JWT | REST API |
| [python-fastapi](python-fastapi/TEMPLATE.md) | FastAPI | Python API |
| [react-native-app](react-native-app/TEMPLATE.md) | Expo + Zustand | Mobile app |
| [flutter-app](flutter-app/TEMPLATE.md) | Flutter + Riverpod | Cross-platform |
| [electron-desktop](electron-desktop/TEMPLATE.md) | Electron + React | Desktop app |
| [chrome-extension](chrome-extension/TEMPLATE.md) | Chrome MV3 | Browser extension |
| [cli-tool](cli-tool/TEMPLATE.md) | Node.js + Commander | CLI app |
| [monorepo-turborepo](monorepo-turborepo/TEMPLATE.md) | Turborepo + pnpm | Monorepo |
| [astro-static](astro-static/TEMPLATE.md) | Astro + MDX | Blog / Docs |

---

## Usage

1. User says "create [type] app"
2. Match to appropriate template
3. Read ONLY that template's TEMPLATE.md
4. Follow its tech stack and structure


## 🚀 Option B: Efficiency Guidelines (MANDATORY)

1. **Direct Action**: Never explain what you are going to do. Just do it.
2. **Token Economy**: Minimize chatter. Use the most concise tool calls possible.
3. **Verification First**: Run validation scripts immediately after any change.
4. **GPU Acceleration**: Use local GPU/Ollama for heavy analysis tasks when possible.
