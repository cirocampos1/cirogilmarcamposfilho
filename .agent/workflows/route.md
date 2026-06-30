---
name: route
description: Roteamento inteligente de agentes baseado em contexto
tools: Read, Grep, Glob
model: inherit
---

# 🎯 Roteamento Inteligente de Agentes

## Propósito

Analisa a solicitação do usuário e recomenda o(s) agente(s) mais adequado(s) do catálogo de 1.211+ especialistas.

## Como Usar

```markdown
/route [descrição da tarefa]
```

Ou simplesmente:

```markdown
"Preciso de ajuda com [tarefa]"
```

## Lógica de Roteamento

### 1. Análise de Contexto

Extrai palavras-chave da solicitação:
- **Tecnologia:** python, javascript, react, nestjs, fastapi, etc.
- **Domínio:** backend, frontend, database, security, mobile, etc.
- **Ação:** criar, otimizar, auditar, migrar, testar, etc.

### 2. Mapeamento por Squad

```yaml
Engenharia:
  keywords: [code, api, backend, frontend, devops, docker, kubernetes, aws, azure, gcp]
  agentes: [nestjs-expert, fastapi-router, react-patterns, docker-expert, kubernetes-deployment-workflow]

Dados:
  keywords: [sql, database, analytics, ml, ai, vector, postgres, mongodb, redis]
  agentes: [vector-database-engineer, database-design, data-pipeline-architecture, ml-pipeline-workflow]

Segurança:
  keywords: [security, audit, pentest, vulnerability, compliance, gdpr, auth]
  agentes: [vulnerability-scanner, pentest-checklist, red-team-tools-and-methodology, gdpr-data-handling]

UI/UX:
  keywords: [ui, ux, design, frontend, react, css, tailwind, mobile]
  agentes: [ui-ux-pro-max, frontend-design, tailwind-design-system, react-patterns, mobile-design-system]
```

### 3. Recomendação

Retorna:
1. **Agente Primário:** O mais especializado para a tarefa
2. **Agentes de Suporte:** Complementares ao primário
3. **Esquadrão Sugerido:** Para tarefas complexas (usa maestro-leo)

## Exemplos

### Exemplo 1: Backend API
```markdown
Usuário: "Preciso criar uma API REST com Python"

Roteamento:
├── Squad: Engenharia
├── Agente Primário: fastapi-router
├── Agente de Suporte: python-patterns
└── Comando: Ative fastapi-router
```

### Exemplo 2: Banco de Dados
```markdown
Usuário: "Otimizar queries lentas no PostgreSQL"

Roteamento:
├── Squad: Dados
├── Agente Primário: postgresql-optimization-workflow
├── Agente de Suporte: database-design
└── Comando: Ative postgresql-optimization-workflow
```

### Exemplo 3: Segurança
```markdown
Usuário: "Auditar vulnerabilidades da aplicação"

Roteamento:
├── Squad: Segurança
├── Agente Primário: vulnerability-scanner
├── Agente de Suporte: security-auditing-workflow-bundle
└── Comando: Ative vulnerability-scanner
```

### Exemplo 4: Tarefa Complexa
```markdown
Usuário: "Criar um SaaS completo com backend, frontend e mobile"

Roteamento:
├── Modo: Orquestração Multi-Agente
├── Condutor: maestro-leo
├── Esquadrão:
│   ├── nestjs-expert (backend)
│   ├── react-patterns (frontend web)
│   ├── react-native-architecture (mobile)
│   ├── docker-expert (containerização)
│   └── vulnerability-scanner (segurança)
└── Comando: /maestro-leo ative esquadrão para SaaS
```

## Comandos Relacionados

- `/route [tarefa]` - Roteia para o agente ideal
- `/maestro-leo` - Ativa orquestração multi-agente
- `/skills [categoria]` - Lista skills por categoria
- `/agents [squad]` - Lista agentes por squad

## Dicas

1. **Seja específico:** "Criar API com FastAPI" é melhor que "Criar API"
2. **Mencione tecnologias:** Inclua nomes de frameworks/bibliotecas
3. **Descreva o objetivo:** "Otimizar", "Criar", "Auditar", "Migrar"
4. **Para tarefas complexas:** O sistema sugere automaticamente o maestro-leo
