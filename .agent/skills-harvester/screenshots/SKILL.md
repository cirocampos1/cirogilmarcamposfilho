---
name: screenshots
description: Generate marketing-quality screenshots of your app using Playwright directly. Screenshots are captured at true HiDPI (2x retina) resolution using `deviceScaleFactor: 2`.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Screenshots

## Backstory

Você é um agente especializado em Screenshots.

## Contexto Original da Skill
Screenshots

## Instruções
---
name: screenshots
description: "Generate marketing screenshots of your app using Playwright. Use when the user wants to create screenshots for Product Hunt, social media, landing pages, or documentation."
risk: safe
source: "https://github.com/Shpigford/skills/tree/main/screenshots"
date_added: "2026-02-27"
---

# Screenshots

Generate marketing-quality screenshots of your app using Playwright directly. Screenshots are captured at true HiDPI (2x retina) resolution using `deviceScaleFactor: 2`.

## When to Use This Skill

Use this skill when:
- User wants to create screenshots for Product Hunt
- Creating screenshots for social media
- Generating images for landing pages
- Creating documentation screenshots
- User requests marketing-quality app screenshots

## Prerequisites

Playwright must be available. Check for it:
```bash
npx playwright --version 2>/dev/null || npm ls playwright 2>/dev/null | grep playwright
```

If not found, inform the user:
> Playwright is required. Install it with: `npm install -D playwright` or `npm install -D @playwright/test`

## Step 1: Determine App URL

If `$1` is provided, use it as the app URL.

If no URL is provided:
1. Check if a dev server is likely running by looking for `package.json` scripts
2. Use `AskUserQuestion` to ask the user for the URL or offer to help start the dev server

Common default URLs to suggest:
- `http://localhost:3000` (Next.js, Create React App, Rails)
- `http://localhost:5173` (Vite)
- `http://localhost:4000` (Phoenix)
- `http://localhost:8080` (Vue CLI, generic)

## Step 2: Gather Requirements

Use `AskUserQuestion` with the following questions:

**Question 1: Screenshot count**
- Header: "Count"
- Question: "How many screenshots do you need?"
- Options:
  - "3-5" - Quick set of key features
  - "5-10" - Comprehensive feature coverage
  - "10+" - Full marketing suite

**Question 2: Purpose**
- Header: "Purpose"
- Question: "What will these screenshots be used for?"
- Options:
  - "Product Hunt" - Hero shots and feature highlights
  - "Social media" - Eye-catching feature demos
  - "Landing page" - Marketing sections and benefits
  - "Documentation" - UI reference and tutorials

**Question 3: Authentication**
- Header: "Auth"
- Question: "Does the app require login to access the features you want to screenshot?"
- Options:
  - "No login needed" - Public pages only
  - "Yes, I'll provide credentials" - Need to log in first

If user selects "Yes, I'll provide credentials", ask follow-up questions:
- "What is the login page URL?" (e.g., `/login`, `/sign-in`)
- "What is the email/username?"
- "What is the password?"

The script will automatically detect login form fields using Playwright's smart locators.

## Step 3: Analyze Codebase for Features

Thoroughly explore the codebase to understand the app and identify screenshot opportunities.

### 3.1: Read Documentation First

**Always start by reading these files** to understand what the app does:

1. **README.md** (and any README files in 

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Generate marketing-quality screenshots of your app using Playwright directly. Screenshots are captured at true HiDPI (2x retina) resolution using `deviceScaleFactor: 2`.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Screenshots
- Para tarefas relacionadas a screenshots

## Diretrizes Específicas

