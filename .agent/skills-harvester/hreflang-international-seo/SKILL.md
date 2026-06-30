---
name: hreflang-international-seo
description: - Use when validating or generating hreflang for multilingual or multiregional sites. - Use when the user mentions international SEO, language tags, x-default, or hreflang issues. - Use when auditing 
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Hreflang & International SEO

## Backstory

Você é um agente especializado em Hreflang & International SEO.

## Contexto Original da Skill
Hreflang & International SEO

## Instruções
---
name: seo-hreflang
description: >
  Hreflang and international SEO audit, validation, and generation. Detects
  common mistakes, validates language/region codes, and generates correct
  hreflang implementations. Use when user says "hreflang", "i18n SEO",
  "international SEO", "multi-language", "multi-region", or "language tags".
risk: unknown
source: "https://github.com/AgriciDaniel/claude-seo"
date_added: "2026-03-21"
user-invokable: true
argument-hint: "[url]"
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
---

# Hreflang & International SEO

## When to Use

- Use when validating or generating hreflang for multilingual or multiregional sites.
- Use when the user mentions international SEO, language tags, x-default, or hreflang issues.
- Use when auditing locale alternates across HTML, headers, or sitemap implementations.

Validate existing hreflang implementations or generate correct hreflang tags
for multi-language and multi-region sites. Supports HTML, HTTP header, and
XML sitemap implementations.

## Validation Checks

### 1. Self-Referencing Tags
- Every page must include an hreflang tag pointing to itself
- The self-referencing URL must exactly match the page's canonical URL
- Missing self-referencing tags cause Google to ignore the entire hreflang set

### 2. Return Tags
- If page A links to page B with hreflang, page B must link back to page A
- Every hreflang relationship must be bidirectional (A→B and B→A)
- Missing return tags invalidate the hreflang signal for both pages
- Check all language versions reference each other (full mesh)

### 3. x-default Tag
- Required: designates the fallback page for unmatched languages/regions
- Typically points to the language selector page or English version
- Only one x-default per set of alternates
- Must also have return tags from all other language versions

### 4. Language Code Validation
- Must use ISO 639-1 two-letter codes (e.g., `en`, `fr`, `de`, `ja`)
- Common errors:
  - `eng` instead of `en` (ISO 639-2, not valid for hreflang)
  - `jp` instead of `ja` (incorrect code for Japanese)
  - `zh` without region qualifier (ambiguous; use `zh-Hans` or `zh-Hant`)

### 5. Region Code Validation
- Optional region qualifier uses ISO 3166-1 Alpha-2 (e.g., `en-US`, `en-GB`, `pt-BR`)
- Format: `language-REGION` (lowercase language, uppercase region)
- Common errors:
  - `en-uk` instead of `en-GB` (UK is not a valid ISO 3166-1 code)
  - `es-LA` (Latin America is not a country; use specific countries)
  - Region without language prefix

### 6. Canonical URL Alignment
- Hreflang tags must only appear on canonical URLs
- If a page has `rel=canonical` pointing elsewhere, hreflang on that page is ignored
- The canonical URL and hreflang URL must match exactly (including trailing slashes)
- Non-canonical pages should not be in any hreflang set

### 7. Protocol Consistency
- All URLs in an hreflang set must use the same protocol (HTTPS or HTTP)
- Mixed HTTP/HTTPS in hreflang sets causes va

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

- Use when validating or generating hreflang for multilingual or multiregional sites. - Use when the user mentions international SEO, language tags, x-default, or hreflang issues. - Use when auditing 

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Hreflang & International SEO
- Para tarefas relacionadas a hreflang international seo

## Diretrizes Específicas

