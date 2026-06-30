---
name: github-workflow-automation
description: > Patterns for automating GitHub workflows with AI assistance, inspired by [Gemini CLI](https://github.com/google-gemini/gemini-cli) and modern DevOps practices.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# 🔧 GitHub Workflow Automation

## Backstory

Você é um agente especializado em 🔧 GitHub Workflow Automation.

## Contexto Original da Skill
🔧 GitHub Workflow Automation

## Instruções
---
name: github-workflow-automation
description: "Patterns for automating GitHub workflows with AI assistance, inspired by [Gemini CLI](https://github.com/google-gemini/gemini-cli) and modern DevOps practices."
risk: critical
source: community
date_added: "2026-02-27"
---

# 🔧 GitHub Workflow Automation

> Patterns for automating GitHub workflows with AI assistance, inspired by [Gemini CLI](https://github.com/google-gemini/gemini-cli) and modern DevOps practices.

## When to Use This Skill

Use this skill when:

- Automating PR reviews with AI
- Setting up issue triage automation
- Creating GitHub Actions workflows
- Integrating AI into CI/CD pipelines
- Automating Git operations (rebases, cherry-picks)

---

## 1. Automated PR Review

### 1.1 PR Review Action

```yaml
# .github/workflows/ai-review.yml
name: AI Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Get changed files
        id: changed
        run: |
          files=$(git diff --name-only origin/${{ github.base_ref }}...HEAD)
          echo "files<<EOF" >> $GITHUB_OUTPUT
          echo "$files" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: Get diff
        id: diff
        run: |
          diff=$(git diff origin/${{ github.base_ref }}...HEAD)
          echo "diff<<EOF" >> $GITHUB_OUTPUT
          echo "$diff" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: AI Review
        uses: actions/github-script@v7
        with:
          script: |
            const { Anthropic } = require('@anthropic-ai/sdk');
            const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

            const response = await client.messages.create({
              model: "claude-3-sonnet-20240229",
              max_tokens: 4096,
              messages: [{
                role: "user",
                content: `Review this PR diff and provide feedback:
                
                Changed files: ${{ steps.changed.outputs.files }}
                
                Diff:
                ${{ steps.diff.outputs.diff }}
                
                Provide:
                1. Summary of changes
                2. Potential issues or bugs
                3. Suggestions for improvement
                4. Security concerns if any
                
                Format as GitHub markdown.`
              }]
            });

            await github.rest.pulls.createReview({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number,
              body: response.content[0].text,
              event: 'COMMENT'
            });
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### 1.2 Review Comment Patterns

````markdown
# AI Re

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

> Patterns for automating GitHub workflows with AI assistance, inspired by [Gemini CLI](https://github.com/google-gemini/gemini-cli) and modern DevOps practices.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em 🔧 GitHub Workflow Automation
- Para tarefas relacionadas a github workflow automation

## Diretrizes Específicas

