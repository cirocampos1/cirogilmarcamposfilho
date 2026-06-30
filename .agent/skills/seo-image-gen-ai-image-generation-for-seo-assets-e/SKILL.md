---
name: seo-image-gen-ai-image-generation-for-seo-assets-e
description: Generate production-ready images for SEO use cases using Gemini's image generation via the banana Creative Director pipeline. Maps SEO needs to optimized domain modes, aspect ratios, and resolution de
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# SEO Image Gen: AI Image Generation for SEO Assets (Extension)

## Backstory

Você é um agente especializado em SEO Image Gen: AI Image Generation for SEO Assets (Extension).

## Contexto Original da Skill
SEO Image Gen: AI Image Generation for SEO Assets (Extension)

## Instruções
---
name: seo-image-gen
description: "Generate SEO-focused images such as OG cards, hero images, schema assets, product visuals, and infographics. Use when image generation is part of an SEO workflow or content publishing task."
risk: unknown
source: "https://github.com/AgriciDaniel/claude-seo"
date_added: "2026-03-21"
argument-hint: "[og|hero|product|infographic|custom|batch] <description>"
user-invokable: true
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# SEO Image Gen: AI Image Generation for SEO Assets (Extension)

Generate production-ready images for SEO use cases using Gemini's image generation
via the banana Creative Director pipeline. Maps SEO needs to optimized domain modes,
aspect ratios, and resolution defaults.

## When to Use

- Use when generating OG images, hero images, schema visuals, infographics, or similar SEO assets.
- Use when image generation is part of a broader SEO or publishing workflow.
- Use only when the required image-generation extension is available.

## Architecture Note

This skill has two components with distinct roles:
- **SKILL.md** (this file): Handles interactive `/seo image-gen` commands for generating images
- **Agent** (`agents/seo-image-gen.md`): Audit-only analyst spawned during `/seo audit` to assess existing OG/social images and produce a generation plan (never auto-generates)

## Prerequisites

This skill requires the banana extension to be installed:
```bash
./extensions/banana/install.sh
```

**Check availability:** Before using any image generation tool, verify the MCP server
is connected by checking if `gemini_generate_image` or `set_aspect_ratio` tools are
available. If tools are not available, inform the user the extension is not installed
and provide install instructions.

## Quick Reference

| Command | What it does |
|---------|-------------|
| `/seo image-gen og <description>` | Generate OG/social preview image (1200x630 feel) |
| `/seo image-gen hero <description>` | Blog hero image (widescreen, dramatic) |
| `/seo image-gen product <description>` | Product photography (clean, white BG) |
| `/seo image-gen infographic <description>` | Infographic visual (vertical, data-heavy) |
| `/seo image-gen custom <description>` | Custom image with full Creative Director pipeline |
| `/seo image-gen batch <description> [N]` | Generate N variations (default: 3) |

## SEO Image Use Cases

Each use case maps to pre-configured banana parameters:

| Use Case | Aspect Ratio | Resolution | Domain Mode | Notes |
|----------|-------------|------------|-------------|-------|
| **OG/Social Preview** | `16:9` | `1K` | Product or UI/Web | Clean, professional, text-friendly |
| **Blog Hero** | `16:9` | `2K` | Cinema or Editorial | Dramatic, atmospheric, editorial quality |
| **Schema Image** | `4:3` | `1K` | Product | Clean, descriptive, schema ImageObject |
| **Social Square** | `1:1` | `1K` | UI/Web | Platform-optimized square |
| **Product Photo** | `4:3` | `2K` | Product | Whit

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Generate production-ready images for SEO use cases using Gemini's image generation via the banana Creative Director pipeline. Maps SEO needs to optimized domain modes, aspect ratios, and resolution de

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em SEO Image Gen: AI Image Generation for SEO Assets (Extension)
- Para tarefas relacionadas a seo image gen ai image generation for seo assets e

## Diretrizes Específicas

