---
name: apify-actorization
description: Actorization converts existing software into reusable serverless applications compatible with the Apify platform. Actors are programs packaged as Docker images that accept well-defined JSON input, per
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Apify Actorization

## Backstory

Você é um agente especializado em Apify Actorization.

## Contexto Original da Skill
Apify Actorization

## Instruções
---
name: apify-actorization
description: "Actorization converts existing software into reusable serverless applications compatible with the Apify platform. Actors are programs packaged as Docker images that accept well-defined JSON input, perform an action, and optionally produce structured JSON output."
risk: unknown
source: community
---

# Apify Actorization

Actorization converts existing software into reusable serverless applications compatible with the Apify platform. Actors are programs packaged as Docker images that accept well-defined JSON input, perform an action, and optionally produce structured JSON output.

## Quick Start

1. Run `apify init` in project root
2. Wrap code with SDK lifecycle (see language-specific section below)
3. Configure `.actor/input_schema.json`
4. Test with `apify run --input '{"key": "value"}'`
5. Deploy with `apify push`

## When to Use This Skill

- Converting an existing project to run on Apify platform
- Adding Apify SDK integration to a project
- Wrapping a CLI tool or script as an Actor
- Migrating a Crawlee project to Apify

## Prerequisites

Verify `apify` CLI is installed:

```bash
apify --help
```

If not installed:

```bash
brew install apify-cli

# Or: npm install -g apify-cli
# Or install from an official release package that your OS package manager verifies
```

Verify CLI is logged in:

```bash
apify info  # Should return your username
```

If not logged in, check if `APIFY_TOKEN` environment variable is defined. If not, ask the user to generate one at https://console.apify.com/settings/integrations, add it to their shell or secret manager without putting the literal token in command history, then run:

```bash
apify login
```

## Actorization Checklist

Copy this checklist to track progress:

- [ ] Step 1: Analyze project (language, entry point, inputs, outputs)
- [ ] Step 2: Run `apify init` to create Actor structure
- [ ] Step 3: Apply language-specific SDK integration
- [ ] Step 4: Configure `.actor/input_schema.json`
- [ ] Step 5: Configure `.actor/output_schema.json` (if applicable)
- [ ] Step 6: Update `.actor/actor.json` metadata
- [ ] Step 7: Test locally with `apify run`
- [ ] Step 8: Deploy with `apify push`

## Step 1: Analyze the Project

Before making changes, understand the project:

1. **Identify the language** - JavaScript/TypeScript, Python, or other
2. **Find the entry point** - The main file that starts execution
3. **Identify inputs** - Command-line arguments, environment variables, config files
4. **Identify outputs** - Files, console output, API responses
5. **Check for state** - Does it need to persist data between runs?

## Step 2: Initialize Actor Structure

Run in the project root:

```bash
apify init
```

This creates:
- `.actor/actor.json` - Actor configuration and metadata
- `.actor/input_schema.json` - Input definition for the Apify Console
- `Dockerfile` (if not present) - Container image definition

## Step 3: Apply Language-Specific Changes

Choose based on you

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Actorization converts existing software into reusable serverless applications compatible with the Apify platform. Actors are programs packaged as Docker images that accept well-defined JSON input, per

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Apify Actorization
- Para tarefas relacionadas a apify actorization

## Diretrizes Específicas

