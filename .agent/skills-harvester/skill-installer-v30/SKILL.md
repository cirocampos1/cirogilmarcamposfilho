---
name: skill-installer-v30
description: Instala, valida, registra e verifica novas skills no ecossistema. 10 checks de seguranca, copia, registro no orchestrator e verificacao pos-instalacao.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Installer v3.0

## Backstory

Você é um agente especializado em Installer v3.0.

## Contexto Original da Skill
Skill Installer v3.0

## Instruções
---
name: skill-installer
description: Instala, valida, registra e verifica novas skills no ecossistema. 10 checks de seguranca, copia, registro no orchestrator e verificacao pos-instalacao.
risk: safe
source: community
date_added: '2026-03-06'
author: renat
tags:
- skill-management
- deployment
- validation
- installation
tools:
- claude-code
- antigravity
- cursor
- gemini-cli
- codex-cli
---

# Skill Installer v3.0

## Overview

Instala, valida, registra e verifica novas skills no ecossistema. 10 checks de seguranca, copia, registro no orchestrator e verificacao pos-instalacao.

## When to Use This Skill

- When the user mentions "instalar skill" or related topics
- When the user mentions "install skill" or related topics
- When the user mentions "registrar skill" or related topics
- When the user mentions "nova skill" or related topics
- When the user mentions "new skill" or related topics
- When the user mentions "adicionar skill ao ecossistema" or related topics

## Do Not Use This Skill When

- The task is unrelated to skill installer
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

Agente instalador enterprise-grade que garante que toda skill criada (via skill-creator
ou manualmente) seja corretamente instalada, registrada e verificada no ecossistema.
Inclui auto-repair, rollback, dry-run, dashboard, e diagnostico avancado.

## Principio: Redundancia Maxima

Seis camadas de validacao garantem que nenhuma skill fique mal-instalada:

| Camada | Script | O que valida |
|--------|--------|-------------|
| 1 | detect_skills.py | SKILL.md existe + tem frontmatter |
| 2 | validate_skill.py | 10 checks profundos |
| 3 | install_skill.py (pre) | Conflitos, permissoes, espaco, versao |
| 4 | install_skill.py (pos) | Arquivos copiados corretamente |
| 5 | scan_registry.py | Skill aparece no registry (com deduplicacao) |
| 6 | package_skill.py | ZIP valido sem backslashes, nao-vazio, integrity check |

---

## Localizacao

```
C:\Users\renat\skills\skill-installer\
├── SKILL.md              <- este arquivo
├── scripts/
│   ├── install_skill.py  <- instalador principal (11 passos) + todos os comandos
│   ├── detect_skills.py  <- scanner de skills nao-instaladas
│   ├── validate_skill.py <- validacao profunda (10 checks)
│   ├── package_skill.py  <- empacotador ZIP + verificador de integridade
│   └── requirements.txt
├── references/
│   └── known-locations.md
└── data/
    ├── install_log.json  <- log de operacoes (auto-gerado, com rotacao)
    ├── backups/          <- backups antes de sobrescrever
    └── staging/          <- area temporaria para copias seguras
```

---

## Workflow Principal

Quando esta skill for ativada, siga estes passos na ordem:

## Cenario 1: Apos Skill-Creator Finalizar

O skill-creator acabou de criar uma skill em algum diretorio. Execute:

```bash
python C:\Users\renat\skills\skill-installer\scripts\install_skill.py --source "<camin

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Instala, valida, registra e verifica novas skills no ecossistema. 10 checks de seguranca, copia, registro no orchestrator e verificacao pos-instalacao.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Installer v3.0
- Para tarefas relacionadas a skill installer v30

## Diretrizes Específicas

