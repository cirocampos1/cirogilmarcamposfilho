---
name: vibers-human-code-review-for-ai-generated-projects
description: You push code. We review it against your spec, fix issues, and send a PR.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Vibers — Human Code Review for AI-Generated Projects

## Backstory

Você é um agente especializado em Vibers — Human Code Review for AI-Generated Projects.

## Contexto Original da Skill
Vibers — Human Code Review for AI-Generated Projects

## Instruções
---
name: vibers-code-review
description: Human review workflow for AI-generated GitHub projects with spec-based feedback, security review, and follow-up PRs from the Vibers service.
risk: critical
source: https://github.com/marsiandeployer/vibers-action
date_added: "2026-03-17"
---

# Vibers — Human Code Review for AI-Generated Projects

You push code. We review it against your spec, fix issues, and send a PR.

## When to Use
Use this skill when:

- You want human review for AI-generated code pushed to GitHub
- You have a project spec and want reviewers to check implementation against it
- You want review feedback delivered as a follow-up PR with suggested fixes
- You are comfortable granting the Vibers service collaborator access to the repository

## Quick Start (3 steps)

### Step 1. Add collaborator

Go to your repo → Settings → Collaborators → Add **`marsiandeployer`**

### Step 2. Add GitHub Action

Create `.github/workflows/vibers.yml`:

```yaml
name: Vibers Code Review
on:
  push:
    branches: [main]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 2
      - uses: marsiandeployer/vibers-action@v1
        with:
          spec_url: 'https://docs.google.com/document/d/YOUR_SPEC_ID/edit'
          telegram_contact: '@your_telegram'
```

| Parameter | What it does |
|-----------|-------------|
| `spec_url` | Link to your spec (Google Doc, Notion, etc.). **Must be publicly accessible** (or "anyone with the link can view"). Without access to spec, review is impossible. |
| `review_scope` | `full` (default), `security`, or `spec-compliance` |
| `telegram_contact` | Your Telegram — we'll message you when review is ready |

### Step 3. Add commit rules to your AI agent

Add this block to your project's `CLAUDE.md`, `.cursorrules`, or `AGENTS.md`:

```markdown
## Commit messages

Every commit MUST include a "How to test" section in the body:
- Live URL to open and verify the change
- Step-by-step what to click/check
- Test credentials if login is required
- Expected result for each step

Example:
  feat: Add user registration form

  How to test:
  - Open https://myapp.vercel.app/register
  - Fill in email/password, submit
  - Check that confirmation email arrives
  - Try submitting with invalid email — should show error
  - Login: test@example.com / demo123
```

Without "How to test" the reviewer has to guess what to verify, and the review takes longer.

**Done.** Now every push triggers a notification. You'll get a PR with fixes, usually within 24 hours.

## What Happens After Setup

1. You push code → GitHub Action sends us the commit details
2. We read your spec and review changed files
3. We fix issues directly in code and submit a PR
4. You review the PR, merge or comment

We check: spec compliance, security (OWASP top 10), AI hallucinations (fake APIs/imports), logic bugs, UI issues.

We don't check: code style (use ESLint/Prettier), performance benchmarks, full QA

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

You push code. We review it against your spec, fix issues, and send a PR.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Vibers — Human Code Review for AI-Generated Projects
- Para tarefas relacionadas a vibers human code review for ai generated projects

## Diretrizes Específicas

