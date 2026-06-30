---
name: varlock-security-skill
description: <!-- security-allowlist: curl-pipe-bash -->
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Varlock Security Skill

## Backstory

Você é um agente especializado em Varlock Security Skill.

## Contexto Original da Skill
Varlock Security Skill

## Instruções
---
name: varlock
description: "Secure-by-default environment variable management for Claude Code sessions."
risk: critical
source: "https://github.com/dmno-dev/varlock"
version: 1.0.0
---

<!-- security-allowlist: curl-pipe-bash -->

# Varlock Security Skill

Secure-by-default environment variable management for Claude Code sessions.

> **Repository**: https://github.com/dmno-dev/varlock
> **Documentation**: https://varlock.dev

## When to Use

- You need to work with environment variables or secrets in a Claude Code session without exposing their values.
- The task involves validating, loading, or auditing secrets while keeping them out of logs, diffs, and assistant context.
- You want a secure-by-default workflow built around Varlock instead of direct `.env` inspection.

## Core Principle: Secrets Never Exposed

When working with Claude, secrets must NEVER appear in:
- Terminal output
- Claude's input/output context
- Log files or traces
- Git commits or diffs
- Error messages

This skill ensures all sensitive data is properly protected.

---

## CRITICAL: Security Rules for Claude

### Rule 1: Never Echo Secrets

```bash
# ❌ NEVER DO THIS - exposes secret to Claude's context
echo $CLERK_SECRET_KEY
cat .env | grep SECRET
printenv | grep API

# ✅ DO THIS - validates without exposing
varlock load --quiet && echo "✓ Secrets validated"
```

### Rule 2: Never Read .env Directly

```bash
# ❌ NEVER DO THIS - exposes all secrets
cat .env
less .env
Read tool on .env file

# ✅ DO THIS - read schema (safe) not values
cat .env.schema
varlock load  # Shows masked values
```

### Rule 3: Use Varlock for Validation

```bash
# ❌ NEVER DO THIS - exposes secret in error
test -n "$API_KEY" && echo "Key: $API_KEY"

# ✅ DO THIS - Varlock validates and masks
varlock load
# Output shows: API_KEY 🔐sensitive └ ▒▒▒▒▒
```

### Rule 4: Never Include Secrets in Commands

```bash
# ❌ NEVER DO THIS - secret in command history
curl -H "Authorization: Bearer sk_live_xxx" https://api.example.com

# ✅ DO THIS - use environment variable
curl -H "Authorization: Bearer $API_KEY" https://api.example.com
# Or better: varlock run -- curl ...
```

---

## Quick Start

### Installation

```bash
# Install Varlock CLI
curl -sSfL https://varlock.dev/install.sh | sh -s -- --force-no-brew

# Add to PATH (add to ~/.zshrc or ~/.bashrc)
export PATH="$HOME/.varlock/bin:$PATH"

# Verify
varlock --version
```

### Initialize Project

```bash
# Create .env.schema from existing .env
varlock init

# Or create manually
touch .env.schema
```

---

## Schema File: .env.schema

The schema defines types, validation, and sensitivity for each variable.

### Basic Structure

```bash
# Global defaults
# @defaultSensitive=true @defaultRequired=infer

# Application
# @type=enum(development,staging,production) @sensitive=false
NODE_ENV=development

# @type=port @sensitive=false
PORT=3000

# Database - SENSITIVE
# @type=url @required
DATABASE_URL=

# @type=string @required @sensitive
DATABASE_PASSWORD=

# API Ke

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

<!-- security-allowlist: curl-pipe-bash -->

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Varlock Security Skill
- Para tarefas relacionadas a varlock security skill

## Diretrizes Específicas

