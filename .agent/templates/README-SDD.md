# 🚀 Sistema SDD -  Spec-Driven Development

Este diretório contém o sistema completo de **Spec-Driven Development (SDD)** do , integrado com as **3400+ skills** do catálogo.

---

## 📁 Estrutura

```
.agent/
├── templates/                    # Templates para documentação SDD
│   ├── spec-template.md         # Especificação de feature
│   ├── plan-template.md         # Plano de implementação
│   ├── tasks-template.md        # Lista de tarefas
│   ├── constitution-template.md # Constituição do projeto
│   ├── checklist-template.md    # Checklist de qualidade
│   └── README-SDD.md           # Esta documentação
│
├── skills/                       # Skills para execução SDD
│   ├── speckit-specify/         # Criar especificação
│   ├── speckit-plan/            # Criar plano de implementação
│   ├── speckit-tasks/           # Gerar tarefas
│   ├── speckit-implement/       # Executar implementação
│   ├── speckit-router/          # Roteador para 3400+ skills
│   └── ...                      # +3400 skills especializadas
│
├── scripts/                      # Scripts de validação
│   └── sdd_checklist.py         # Checklist com Gates Constitucionais
│
└── specs/                        # Especificações de features (criado por projeto)
    ├── 001-feature-name/
    │   ├── spec.md              # Com skills recomendadas
    │   ├── plan.md              # Com mapeamento de skills
    │   ├── tasks.md             # Com skills atribuídas
    │   ├── research.md
    │   ├── data-model.md
    │   ├── quickstart.md
    │   └── contracts/
    └── 002-another-feature/
        └── ...
```

---

## 🔄 Fluxo de Trabalho SDD + Skills

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  /speckit.specify│────▶│  /speckit.plan  │────▶│  /speckit.tasks │
│                 │     │                 │     │                 │
│  spec.md        │     │  plan.md        │     │  tasks.md       │
│  + skills       │     │  + skills       │     │  + skills       │
│  recomendadas   │     │  mapeadas       │     │  atribuídas     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │ /speckit.implement│
                                               │                 │
                                               │  CÓDIGO         │
                                               │  + skills       │
                                               │  aplicadas      │
                                               └─────────────────┘
```

---

## 🎮 Comandos SDD

### 1. Criar Especificação

```bash
# Comando
/speckit.specify Sistema de autenticação com login e recuperação de senha

# Resultado
specs/007-auth-system/
└── spec.md          # Especificação + skills recomendadas
```

**Saída inclui**:
- Especificação completa
- **Skills recomendadas** do catálogo (3400+ disponíveis)
- Gates constitucionais

### 2. Criar Plano de Implementação

```bash
# Comando
/speckit.plan

# Resultado
specs/007-auth-system/
├── spec.md          # (já existia)
├── plan.md          # Plano técnico + mapeamento de skills
├── research.md      # Pesquisa + skills consultadas
├── data-model.md    # Modelo + skills aplicáveis
├── quickstart.md    # Guia + skills para validação
└── contracts/
    └── api-contracts.md  # Contratos + skills aplicáveis
```

### 3. Gerar Tarefas

```bash
# Comando
/speckit.tasks

# Resultado
specs/007-auth-system/
├── ...              # (arquivos anteriores)
└── tasks.md         # Tarefas com skills atribuídas
```

**Cada tarefa inclui**:
- Descrição detalhada
- **Skill atribuída** do catálogo
- Dependências

### 4. Implementar

```bash
# Comando
/speckit.implement 007-auth-system --all

# Ou tarefa específica
/speckit.implement 007-auth-system --task T001
```

**Processo**:
1. Ler tarefa em `tasks.md`
2. Identificar **skill atribuída**
3. Ler skill do catálogo (`.agent/skills/[skill]/SKILL.md`)
4. Aplicar padrões da skill
5. Implementar código

### 5. Roteamento de Skills

```bash
# Comando
/speckit.router [tarefa]

# Exemplo
/speckit.router qual skill usar para otimizar queries PostgreSQL?

# Resultado
→ Skills recomendadas:
  1. postgresql-optimization-workflow
  2. query-optimization
  3. database-design
```

---

## 🤖 Integração com 3400+ Skills

### Mapeamento por Fase

| Fase SDD | Skills Típicas | Squad |
|----------|----------------|-------|
| **Setup** | `clean-code`, `python-patterns`, `docker-expert` | Core |
| **Fundacional** | `database-design`, `fastapi-router`, `redis-patterns` | Dados/Eng |
| **User Stories** | `api-patterns`, `caching-patterns`, `query-optimization` | Engenharia |
| **Segurança** | `vulnerability-scanner`, `input-validation-patterns` | Segurança |
| **Testing** | `testing-patterns`, `contract-testing` | QA |

### Exemplo de Mapeamento Completo

**Feature**: API de consulta contratos Sankhya com cache

```
Fase 1: Setup
  - clean-code → Estrutura de projeto
  - docker-expert → Containerização

Fase 2: Fundacional
  - database-design → Modelar entidades
  - redis-patterns → Configurar cache
  - fastapi-router → Estrutura da API
  - vulnerability-scanner → Scan inicial

Fase 3: User Story 1 - Consulta
  - sql-query-optimizer → Otimizar queries Sankhya
  - caching-patterns → Implementar cache
  - api-patterns → Design de endpoints
  - testing-patterns → Testes de integração

Fase 4: User Story 2 - Export
  - excel-export-patterns → Exportação XLSX
  - async-task-patterns → Processamento assíncrono
  - celery-task-patterns → Background jobs

Transversal (todas as fases)
  - vulnerability-scanner → Scan de segurança
  - input-validation-patterns → Validação de entrada
  - logging-patterns → Observabilidade
```

---

## 🏛️ Gates Constitucionais

Todo código deve passar pelos **Gates Constitucionais**:

| Gate | Artigo | Descrição | Check |
|------|--------|-----------|-------|
| **Simplicidade** | VII | ≤3 projetos | `sdd_checklist.py` |
| **Anti-Abstração** | VIII | Sem wrappers desnecessários | `sdd_checklist.py` |
| **Test-First** | III | Testes antes de código | `sdd_checklist.py` |
| **Integration-First** | IX | Bancos reais > mocks | `sdd_checklist.py` |
| **Library-First** | I | Features como libs | `sdd_checklist.py` |
| **Segurança** | X | Security-first | `sdd_checklist.py` |

### Executar Checks

```bash
# Todos os checks
python .agent/scripts/sdd_checklist.py .

# Apenas gates constitucionais
python .agent/scripts/sdd_checklist.py . --gates-only

# Apenas segurança
python .agent/scripts/sdd_checklist.py . --security-only

# Validar spec específica
python .agent/scripts/sdd_checklist.py . --spec specs/007-auth-system/spec.md
```

---

## 📜 Constituição 

Os **9 Artigos** governam todo o desenvolvimento:

1. **Library-First**: Toda feature começa como biblioteca
2. **CLI Mandate**: Toda lib expõe CLI
3. **Test-First**: Testes antes do código (NON-NEGOTIABLE)
4. **Simplicidade**: Solução mais simples que funciona
5. **Framework Trust**: Use frameworks diretamente
6. **Single Model**: Uma representação por entidade
7. **≤3 Projects**: Máximo 3 projetos
8. **No Over-Abstraction**: Justifique cada abstração
9. **Integration-First**: Bancos reais, não mocks

**X. Security**: NUNCA ESCREVA NO SANKHYA SEM AUTORIZAÇÃO

---

## 🔍 Consulta de Skills

### Buscar Skills

```bash
# Total de skills
ls .agent/skills/ | wc -l
# → 3403

# Buscar por termo
ls .agent/skills/ | grep "database"

# Ver índice organizado
cat .agent/skills/INDEX.md

# Skills de um squad específico
grep -A5 "Engenharia" .agent/skills/INDEX.md
```

### Ler uma Skill

```bash
# Ler skill específica
cat .agent/skills/fastapi-router/SKILL.md

# Ver padrões
cat .agent/skills/database-design/SKILL.md | head -50
```

---

## 📝 Exemplo Completo

### Input
```
/speckit.specify API para consulta de contratos do Sankhya com cache Redis
```

### Fluxo com Skills

**Fase 1 - Specify**:
```
specs/008-sankhya-contratos/
└── spec.md
    ├── User Story 1 (P1): Consulta de contratos por CPF/CNPJ
    ├── User Story 2 (P2): Cache com TTL configurável
    ├── User Story 3 (P3): Exportação para CSV
    ├── RF-001: Integração read-only com Sankhya
    ├── RF-002: Cache em Redis
    ├── CS-001: Resposta < 100ms quando cache hit
    └── 🤖 Skills Recomendadas:
        - database-design
        - fastapi-router
        - redis-patterns
        - sql-query-optimizer
        - vulnerability-scanner
```

**Fase 2 - Plan**:
```
specs/008-sankhya-contratos/
├── spec.md
├── plan.md              # + Mapeamento de skills por fase
├── research.md          # + Skills consultadas
├── data-model.md        # + Skills aplicáveis
├── quickstart.md        # + Skills para validação
└── contracts/
    └── api-contracts.md # + Skills aplicáveis
```

**Fase 3 - Tasks**:
```
specs/008-sankhya-contratos/
├── ...
└── tasks.md
    ├── Fase 1: Setup
    │   - T001: Estrutura → Skill: clean-code
    │   - T002: Config → Skill: python-patterns
    ├── Fase 2: Fundacional
    │   - T006: DB → Skill: database-design
    │   - T007: Cache → Skill: redis-patterns
    ├── Fase 3: US1 - Consulta
    │   - T012: Modelo → Skill: database-design
    │   - T013: Query → Skill: sql-query-optimizer
    │   - T014: API → Skill: fastapi-router
    └── Fase 4: US2 - Cache
        - T021: Cache → Skill: caching-patterns
        - T022: TTL → Skill: redis-patterns
```

**Fase 4 - Implement**:
```
Para cada tarefa:
  1. Ler tasks.md → identificar skill atribuída
  2. Ler skill → .agent/skills/[skill]/SKILL.md
  3. Aplicar padrões da skill
  4. Implementar código
  5. Validar com gates
```

---

## 🔒 Segurança

### Regras Inegociáveis

1. **NUNCA JAMAIS ESCREVA NO BANCO SANKHYA SEM AUTORIZAÇÃO DO HUMANO**
2. Dados sensíveis nunca em logs
3. Validação de input em todas as APIs
4. Autenticação em todos os endpoints
5. Secrets em variáveis de ambiente
6. `detect-secrets` no pre-commit

### Validação

```bash
# Verificar secrets no código
detect-secrets scan

# Checklist completo de segurança
python .agent/scripts/sdd_checklist.py . --security-only

# Scan de vulnerabilidades
# (usar skill: vulnerability-scanner)
```

---

## 🚀 Integração com GUIA_MESTRE

Este sistema SDD integra-se ao GUIA_MESTRE existente:

| GUIA_MESTRE | SDD + Skills |
|-------------|--------------|
| `/brainstorm` | `/speckit.specify` + skills recomendadas |
| `/maestro-leo` | `/speckit.plan` + roteamento de skills |
| Skills gerais | 3400+ skills especializadas |
| `checklist.py` | `sdd_checklist.py` + Gates |

---

## 📚 Referências

- [GitHub Spec-Kit](https://github.com/github/spec-kit)
- [GUIA_MESTRE.md](../../GUIA_MESTRE.md)
- [Constituição](constitution-template.md)
- [Índice de Skills](../skills/INDEX.md)

---

## 🎯 Resumo dos Comandos

```bash
# Fluxo completo SDD
/speckit.specify "descrição da feature"    # Criar especificação
/speckit.plan                              # Criar plano técnico
/speckit.tasks                             # Gerar tarefas
/speckit.implement 001-feature --all       # Implementar

# Roteamento
/speckit.router "tarefa específica"        # Encontrar skill

# Validação
python .agent/scripts/sdd_checklist.py .   # Todos os checks
```

---

*Sistema SDD v1.0 -  2026*
*Integrado com 3400+ skills do catálogo*
