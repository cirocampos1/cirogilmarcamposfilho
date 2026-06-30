---
name: agentskillsio-compliant-frontmatter
description: **Purpose:** Pre-ingestion verification system that enforces epistemic quality before documents enter RAG knowledge bases. Produces Clarity-Gated Documents (CGD) compliant with the Clarity Gate Format
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# skills.io compliant frontmatter

## Backstory

Você é um agente especializado em skills.io compliant frontmatter.

## Contexto Original da Skill
agentskills.io compliant frontmatter

## Instruções
---
# agentskills.io compliant frontmatter
name: clarity-gate
risk: unknown
source: community
version: 2.1.3
description: >
  Pre-ingestion verification for epistemic quality in RAG systems.
  Ensures documents are properly qualified before entering knowledge bases.
  Produces CGD (Clarity-Gated Documents) and validates SOT (Source of Truth) files.
author: Francesco Marinoni Moretto
license: CC-BY-4.0
repository: https://github.com/frmoretto/clarity-gate
triggers:
  - clarity gate
  - check for hallucination risks
  - can an LLM read this safely
  - review for equivocation
  - verify document clarity
  - pre-ingestion check
  - cgd verify
  - sot verify
capabilities:
  - document-verification
  - epistemic-quality
  - rag-preparation
  - cgd-generation
  - sot-validation
outputs:
  - type: cgd
    extension: .cgd.md
    spec: docs/CLARITY_GATE_FORMAT_SPEC.md
spec_version: "2.1"
---

# Clarity Gate v2.1

**Purpose:** Pre-ingestion verification system that enforces epistemic quality before documents enter RAG knowledge bases. Produces Clarity-Gated Documents (CGD) compliant with the Clarity Gate Format Specification v2.1.

**Core Question:** "If another LLM reads this document, will it mistake assumptions for facts?"

**Core Principle:** *"Detection finds what is; enforcement ensures what should be. In practice: find the missing uncertainty markers before they become confident hallucinations."*

---

## What's New in v2.1

| Feature | Description |
|---------|-------------|
| **Claim Completion Status** | PENDING/VERIFIED determined by field presence (no explicit status field) |
| **Source Field Semantics** | Actionable source (PENDING) vs. what-was-found (VERIFIED) |
| **Claim ID Format Guidance** | Hash-based IDs preferred, collision analysis for scale |
| **Body Structure Requirements** | HITL Verification Record section mandatory when claims exist |
| **New Validation Codes** | E-ST10, W-ST11, W-HC01, W-HC02, E-SC06 (FORMAT_SPEC); E-TB01-07 (SOT validation) |
| **Bundled Scripts** | `claim_id.py` and `document_hash.py` for deterministic computations |

---

## Specifications

This skill implements and references:

| Specification | Version | Location |
|---------------|---------|----------|
| Clarity Gate Format (Unified) | v2.1 | docs/CLARITY_GATE_FORMAT_SPEC.md |

**Note:** v2.0 unifies CGD and SOT into a single `.cgd.md` format. SOT is now a CGD with an optional `tier:` block.

---

## Validation Codes

Clarity Gate defines validation codes for structural and semantic checks per FORMAT_SPEC v2.1:

### HITL Claim Validation (§1.3.2-1.3.3)
| Code | Check | Severity |
|------|-------|----------|
| **W-HC01** | Partial `confirmed-by`/`confirmed-date` fields | WARNING |
| **W-HC02** | Vague source (e.g., "industry reports", "TBD") | WARNING |
| **E-SC06** | Schema error in `hitl-claims` structure | ERROR |

### Body Structure (§1.2.1)
| Code | Check | Severity |
|------|-------|----------|
| **E-ST10** | Missing `## HITL Verification Record` when

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

**Purpose:** Pre-ingestion verification system that enforces epistemic quality before documents enter RAG knowledge bases. Produces Clarity-Gated Documents (CGD) compliant with the Clarity Gate Format

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em skills.io compliant frontmatter
- Para tarefas relacionadas a agentskillsio compliant frontmatter

## Diretrizes Específicas

