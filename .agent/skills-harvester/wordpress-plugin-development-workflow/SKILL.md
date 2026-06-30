---
name: wordpress-plugin-development-workflow
description: Specialized workflow for creating WordPress plugins with proper architecture, hooks system, admin interfaces, REST API endpoints, and security practices. Now includes WordPress 7.0 features for modern
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# WordPress Plugin Development Workflow

## Backstory

Você é um agente especializado em WordPress Plugin Development Workflow.

## Contexto Original da Skill
WordPress Plugin Development Workflow

## Instruções
---
name: wordpress-plugin-development
description: "WordPress plugin development workflow covering plugin architecture, hooks, admin interfaces, REST API, security best practices, and WordPress 7.0 features: Real-Time Collaboration, AI Connectors, Abilities API, DataViews, and PHP-only blocks."
category: granular-workflow-bundle
risk: safe
source: personal
date_added: "2026-02-27"
---

# WordPress Plugin Development Workflow

## Overview

Specialized workflow for creating WordPress plugins with proper architecture, hooks system, admin interfaces, REST API endpoints, and security practices. Now includes WordPress 7.0 features for modern plugin development.

## WordPress 7.0 Plugin Development

### Key Features for Plugin Developers

1. **Real-Time Collaboration (RTC) Compatibility**
   - Yjs-based CRDT for simultaneous editing
   - Custom transport via `sync.providers` filter
   - **Requirement**: Register post meta with `show_in_rest => true`

2. **AI Connector Integration**
   - Provider-agnostic AI via `wp_ai_client_prompt()`
   - Settings > Connectors admin screen
   - Works with OpenAI, Claude, Gemini, Ollama

3. **Abilities API**
   - Declare plugin capabilities for AI agents
   - REST API: `/wp-json/abilities/v1/manifest`
   - MCP adapter support

4. **DataViews & DataForm**
   - Modern admin interfaces
   - Replaces WP_List_Table patterns
   - Built-in validation

5. **PHP-Only Blocks**
   - Register blocks without JavaScript
   - Auto-generated Inspector controls

## When to Use This Workflow

Use this workflow when:
- Creating custom WordPress plugins
- Extending WordPress functionality
- Building admin interfaces
- Adding REST API endpoints
- Integrating third-party services
- Implementing WordPress 7.0 AI/Collaboration features

## Workflow Phases

### Phase 1: Plugin Setup

#### Skills to Invoke
- `app-builder` - Project scaffolding
- `backend-dev-guidelines` - Backend patterns

#### Actions
1. Create plugin directory structure
2. Set up main plugin file with header
3. Implement activation/deactivation hooks
4. Set up autoloading
5. Configure text domain

#### WordPress 7.0 Plugin Header
```php
/*
Plugin Name: My Plugin
Plugin URI: https://example.com/my-plugin
Description: A WordPress 7.0 compatible plugin with AI and RTC support
Version: 1.0.0
Requires at least: 6.0
Requires PHP: 7.4
Author: Developer Name
License: GPL2+
*/
```

#### Copy-Paste Prompts
```
Use @app-builder to scaffold a new WordPress plugin
```

### Phase 2: Plugin Architecture

#### Skills to Invoke
- `backend-dev-guidelines` - Architecture patterns

#### Actions
1. Design plugin class structure
2. Implement singleton pattern
3. Create loader class
4. Set up dependency injection
5. Configure plugin lifecycle

#### WordPress 7.0 Architecture Considerations
- Prepare for iframed editor compatibility
- Design for collaboration-aware data flows
- Consider Abilities API for AI integration

#### Copy-Paste Prompts
```
Use @backend-dev-guidelines to design plugin archite

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Specialized workflow for creating WordPress plugins with proper architecture, hooks system, admin interfaces, REST API endpoints, and security practices. Now includes WordPress 7.0 features for modern

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em WordPress Plugin Development Workflow
- Para tarefas relacionadas a wordpress plugin development workflow

## Diretrizes Específicas

