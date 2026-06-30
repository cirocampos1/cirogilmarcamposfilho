---
name: nx-workspace-patterns
description: Production patterns for Nx monorepo management.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Nx Workspace Patterns

## Backstory

Você é um agente especializado em Nx Workspace Patterns.

## Contexto Original da Skill
Nx Workspace Patterns

## Instruções
---
name: nx-workspace-patterns
description: "Configure and optimize Nx monorepo workspaces. Use when setting up Nx, configuring project boundaries, optimizing build caching, or implementing affected commands."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Nx Workspace Patterns

Production patterns for Nx monorepo management.

## Do not use this skill when

- The task is unrelated to nx workspace patterns
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Use this skill when

- Setting up new Nx workspaces
- Configuring project boundaries
- Optimizing CI with affected commands
- Implementing remote caching
- Managing dependencies between projects
- Migrating to Nx

## Core Concepts

### 1. Nx Architecture

```
workspace/
├── apps/              # Deployable applications
│   ├── web/
│   └── api/
├── libs/              # Shared libraries
│   ├── shared/
│   │   ├── ui/
│   │   └── utils/
│   └── feature/
│       ├── auth/
│       └── dashboard/
├── tools/             # Custom executors/generators
├── nx.json            # Nx configuration
└── workspace.json     # Project configuration
```

### 2. Library Types

| Type | Purpose | Example |
|------|---------|---------|
| **feature** | Smart components, business logic | `feature-auth` |
| **ui** | Presentational components | `ui-buttons` |
| **data-access** | API calls, state management | `data-access-users` |
| **util** | Pure functions, helpers | `util-formatting` |
| **shell** | App bootstrapping | `shell-web` |

## Templates

### Template 1: nx.json Configuration

```json
{
  "$schema": "./node_modules/nx/schemas/nx-schema.json",
  "npmScope": "myorg",
  "affected": {
    "defaultBase": "main"
  },
  "tasksRunnerOptions": {
    "default": {
      "runner": "nx/tasks-runners/default",
      "options": {
        "cacheableOperations": [
          "build",
          "lint",
          "test",
          "e2e",
          "build-storybook"
        ],
        "parallel": 3
      }
    }
  },
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["production", "^production"],
      "cache": true
    },
    "test": {
      "inputs": ["default", "^production", "{workspaceRoot}/jest.preset.js"],
      "cache": true
    },
    "lint": {
      "inputs": ["default", "{workspaceRoot}/.eslintrc.json"],
      "cache": true
    },
    "e2e": {
      "inputs": ["default", "^production"],
      "cache": true
    }
  },
  "namedInputs": {
    "default": ["{projectRoot}/**/*", "sharedGlobals"],
    "production": [
      "default",
      "!{projectRoot}/**/?(*.)+(spec|test).[jt]s?(x)?(.snap)",
      "!{projectRoot}/tsconfig.spec.json",
      "!{projectRoot}/jest.config.[jt]s",
      "!{projectRoot}/.eslintrc.json"
   

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Production patterns for Nx monorepo management.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Nx Workspace Patterns
- Para tarefas relacionadas a nx workspace patterns

## Diretrizes Específicas

