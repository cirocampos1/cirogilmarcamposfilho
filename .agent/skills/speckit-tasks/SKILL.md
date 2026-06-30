# speckit-tasks

Gera uma lista de tarefas executáveis baseada no plano de implementação, com mapeamento completo para as 3400+ skills do .

---

## Quando usar

Use esta skill quando:
- O plano de implementação (plan.md) está completo
- Precisar de uma lista de tarefas detalhada para execução
- Quiser organizar o trabalho por user stories e prioridades
- Necessite atribuir skills específicas do catálogo para cada tarefa

---

## Comando de Ativação

```
/speckit.tasks
```

Ou:

```
@ gerar tarefas para [###-nome-da-feature]
```

---

## Pré-requisitos

- Arquivo `specs/###-nome-da-feature/plan.md` deve existir
- Arquivo `specs/###-nome-da-feature/spec.md` deve existir
- Opcional: `data-model.md`, `contracts/`, `research.md`
- Catálogo de skills disponível: `.agent/skills/INDEX.md`

---

## Fluxo de Trabalho

### 1. Ler documentos de entrada

```bash
# Obrigatórios
cat specs/###-nome-da-feature/plan.md
cat specs/###-nome-da-feature/spec.md

# Opcionais (se existirem)
cat specs/###-nome-da-feature/data-model.md 2>/dev/null
cat specs/###-nome-da-feature/contracts/api-contracts.md 2>/dev/null
cat specs/###-nome-da-feature/research.md 2>/dev/null
```

### 2. Extrair informações

De `spec.md`:
- User stories (P1, P2, P3...)
- Critérios de aceitação por story
- Requisitos funcionais
- **Skills já recomendadas**

De `plan.md`:
- Estrutura de projeto escolhida
- Decisões técnicas
- Gates constitutionais
- **Mapeamento de skills por fase**

De `data-model.md`:
- Entidades a criar
- Relacionamentos

De `contracts/`:
- Endpoints a implementar
- Eventos a publicar/consumir

### 3. Buscar Skills no Catálogo

Para cada tipo de tarefa, busque skills específicas:

```bash
# Skills de modelagem
ls .agent/skills/ | grep -E "database|sqlalchemy|model"

# Skills de API
ls .agent/skills/ | grep -E "fastapi|api|endpoint"

# Skills de teste
ls .agent/skills/ | grep -E "test|contract|integration"

# Skills de segurança
ls .agent/skills/ | grep -E "security|vulnerability|auth"
```

### 4. Gerar tasks.md

Copie `.agent/templates/tasks-template.md` para `specs/###-nome-da-feature/tasks.md` e preencha com tarefas específicas.

#### Estrutura de Tarefas

**Formato**: `[ID] [P?] [Story] Descrição`**Skill**: `skill-name`**

- **[P]**: Pode rodar em paralelo
- **[Story]**: US1, US2, US3, etc.
- **Skill**: Skill do catálogo  (3400+ disponíveis)

#### Fase 1: Setup

Tarefas de infraestrutura com skills atribuídas:

```markdown
- [ ] T001 Criar estrutura de projeto conforme plano
  **Skill**: `clean-code`
  
- [ ] T002 Inicializar projeto Python com uv
  **Skill**: `python-patterns`
  
- [ ] T003 [P] Configurar ruff e mypy
  **Skill**: `ruff-patterns`, `mypy-patterns`
  
- [ ] T004 Configurar pytest
  **Skill**: `testing-patterns`
  
- [ ] T005 Criar conftest.py com fixtures
  **Skill**: `pytest-patterns`
```

#### Fase 2: Fundacional

Baseada em `plan.md` com skills específicas:

```markdown
- [ ] T006 [P] Configurar conexão com banco (read-only Sankhya)
  **Skill**: `database-design`, `sqlalchemy-patterns`
  
- [ ] T007 [P] Configurar Redis/cache
  **Skill**: `redis-patterns`, `caching-patterns`
  
- [ ] T008 Configurar logging estruturado
  **Skill**: `logging-patterns`, `observability-patterns`
  
- [ ] T009 Criar modelos base
  **Skill**: `database-design`, `sqlalchemy-patterns`
  
- [ ] T010 Configurar tratamento de erros
  **Skill**: `error-handling-patterns`
```

#### Fase 3+: User Stories

Para cada user story em `spec.md`, criar tarefas com skills:

```markdown
## Fase X: User Story N - [Título] (Prioridade: PN) 🎯

**Objetivo**: [Do spec.md]

**Teste Independente**: [Do spec.md]

### Testes para User Story N

- [ ] T0XX [P] [USN] Teste de contrato para [endpoint]
  **Skill**: `contract-testing`, `api-testing-patterns`
  
- [ ] T0XX [P] [USN] Teste de integração para [jornada]
  **Skill**: `integration-testing-patterns`, `pytest-patterns`

### Implementação para User Story N

- [ ] T0XX [P] [USN] Criar modelo [Entidade] em `src/models/[entidade].py`
  **Skill**: `database-design`, `sqlalchemy-patterns`
  
- [ ] T0XX [USN] Implementar [Serviço] em `src/services/[servico].py`
  **Skill**: `service-layer-patterns`, `clean-code`
  
- [ ] T0XX [USN] Implementar [endpoint] em `src/api/[rota].py`
  **Skill**: `fastapi-router`, `api-patterns`
  
- [ ] T0XX [USN] Criar CLI em `src/cli/[comando].py`
  **Skill**: `cli-design-patterns`, `click-patterns`
  
- [ ] T0XX [USN] Adicionar validação e tratamento de erros
  **Skill**: `input-validation-patterns`, `error-handling-patterns`
  
- [ ] T0XX [USN] Adicionar logging
  **Skill**: `logging-patterns`
```

**Regras de dependência**:
- Modelos antes de serviços
- Serviços antes de endpoints
- Testes antes de implementação
- Marcar [P] apenas se arquivos diferentes e sem dependências

### 5. Calcular dependências

Documente no final do tasks.md:

```markdown
## 🔗 Dependências & Ordem de Execução

### Fase 1 (Setup) → Fase 2 (Fundacional) → Fase 3+ (User Stories)

**Setup**: Sem dependências
**Fundacional**: Depende de Setup → BLOQUEIA todas as stories
**User Stories**: Depende de Fundacional → Podem rodar em paralelo

### Dentro de cada User Story

1. Testes primeiro (devem falhar)
2. Modelos → Serviços → Endpoints → CLI
3. Story completa antes de próxima prioridade

## 🤖 Skills por Squad

### Engenharia (Backend)
- `fastapi-router` - APIs FastAPI
- `api-patterns` - Design REST
- `sqlalchemy-patterns` - ORM
- `service-layer-patterns` - Lógica de negócio

### Dados
- `database-design` - Modelagem
- `redis-patterns` - Cache
- `query-optimization` - SQL
- `caching-patterns` - Estratégias de cache

### Segurança
- `vulnerability-scanner` - Scan de segurança
- `input-validation-patterns` - Validação
- `authentication-patterns` - Auth
- `jwt-security` - Tokens

### QA
- `testing-patterns` - Testes gerais
- `contract-testing` - Contratos
- `integration-testing-patterns` - Integração
- `pytest-patterns` - Pytest específico

### DevOps
- `docker-expert` - Containerização
- `deployment-procedures` - Deploy
- `ci-cd-patterns` - CI/CD
```

---

## Exemplo de Saída

```markdown
# Tarefas: Sistema de Autenticação

## Fase 1: Setup

- [ ] T001 Criar estrutura de projeto
  **Skill**: `clean-code`
  
- [ ] T002 Inicializar projeto Python com uv
  **Skill**: `python-patterns`

## Fase 2: Fundacional

- [ ] T005 [P] Configurar conexão PostgreSQL (read-only)
  **Skill**: `database-design`, `sqlalchemy-patterns`
  
- [ ] T006 [P] Configurar Redis para sessões
  **Skill**: `redis-patterns`

## Fase 3: User Story 1 - Login (P1) 🎯

### Testes
- [ ] T008 [P] [US1] Teste de contrato POST /auth/login
  **Skill**: `contract-testing`
  
- [ ] T009 [P] [US1] Teste de integração fluxo de login
  **Skill**: `integration-testing-patterns`

### Implementação
- [ ] T010 [P] [US1] Criar modelo User em src/models/user.py
  **Skill**: `database-design`, `sqlalchemy-patterns`
  
- [ ] T011 [US1] Implementar AuthService em src/services/auth.py
  **Skill**: `service-layer-patterns`, `authentication-patterns`
  
- [ ] T012 [US1] Implementar POST /auth/login em src/api/auth.py
  **Skill**: `fastapi-router`, `api-patterns`
  
- [ ] T013 [US1] Criar CLI auth em src/cli/auth.py
  **Skill**: `cli-design-patterns`

**Checkpoint**: User Story 1 funcional

## Fase 4: User Story 2 - Recuperação (P2)
...
```

---

## Próximos Passos

Após criar tasks.md:
1. Revisar priorização com o usuário
2. Confirmar atribuição de skills
3. Iniciar implementação com `/speckit.implement`
4. Ou delegar tarefas para agentes especialistas usando as skills atribuídas

---

## Consulta de Skills

Para buscar skills no catálogo:

```bash
# Total de skills
ls .agent/skills/ | wc -l

# Buscar por termo
ls .agent/skills/ | grep "[termo]"

# Ver índice organizado
cat .agent/skills/INDEX.md
```

---

*Skill v1.0 -  SDD*
