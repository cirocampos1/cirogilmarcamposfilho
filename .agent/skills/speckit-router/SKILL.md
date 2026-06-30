# speckit-router

Roteador inteligente que mapeia tarefas SDD para as 3400+ skills disponíveis no .

---

## Quando usar

Use esta skill quando:
- Precisar identificar qual skill usar para uma tarefa específica
- Quiser orquestrar múltiplas skills para uma feature completa
- Necessitar de roteamento inteligente baseado no contexto

---

## Comando de Ativação

```
/speckit.router [tarefa ou contexto]
```

Ou:

```
@ qual skill devo usar para [tarefa]?
```

---

## Sistema de Mapeamento

### Mapeamento por Tipo de Tarefa

| Tarefa SDD | Skills Recomendadas | Squad |
|------------|---------------------|-------|
| **Backend API** | `fastapi-router`, `api-patterns`, `api-design-principles` | Engenharia |
| **Database** | `database-design`, `postgresql-optimization-workflow`, `prisma-expert` | Dados |
| **Frontend React** | `react-patterns`, `frontend-development-patterns`, `ui-ux-pro-max` | UI/UX |
| **Security Audit** | `vulnerability-scanner`, `pentest-checklist`, `security-auditing-workflow-bundle` | Segurança |
| **Testing** | `testing-patterns`, `contract-testing`, `e2e-testing-patterns` | Qualidade |
| **DevOps** | `docker-expert`, `kubernetes-deployment-workflow`, `deployment-procedures` | DevOps |
| **ML/AI** | `ml-pipeline-workflow`, `scikit-learn`, `vector-database-engineer` | Dados |
| **Mobile** | `react-native-architecture`, `mobile-design-system` | Mobile |

---

## Roteamento por Fase SDD

### Fase 1: Setup → Skills de Infraestrutura

```yaml
setup:
  - skill: "clean-code"
    quando: "Configurar estrutura de projeto Python"
  
  - skill: "docker-expert"
    quando: "Containerização necessária"
  
  - skill: "git-workflow"
    quando: "Configurar git hooks e CI/CD"
  
  - skill: "pre-commit-hooks"
    quando: "Setup de hooks de pre-commit"
```

### Fase 2: Fundacional → Skills Core

```yaml
foundational:
  database:
    - skill: "database-design"
      quando: "Modelagem de dados"
    - skill: "sql-query-optimizer"
      quando: "Otimização de queries"
    - skill: "migration-patterns"
      quando: "Migrations de banco"
  
  auth:
    - skill: "authentication-patterns"
      quando: "Sistema de autenticação"
    - skill: "oauth-implementation"
      quando: "OAuth/SSO"
    - skill: "jwt-security"
      quando: "Tokens JWT"
  
  api:
    - skill: "fastapi-router"
      quando: "API com FastAPI"
    - skill: "api-patterns"
      quando: "Design de APIs REST"
    - skill: "graphql-expert"
      quando: "API GraphQL"
```

### Fase 3+: User Stories → Skills Especializadas

```yaml
user_stories:
  consulta_dados:
    - skill: "query-optimization"
    - skill: "caching-patterns"
    - skill: "pagination-patterns"
  
  processamento_batch:
    - skill: "celery-task-patterns"
    - skill: "background-job-patterns"
    - skill: "queue-management"
  
  integracao_externa:
    - skill: "http-client-patterns"
    - skill: "circuit-breaker-pattern"
    - skill: "retry-policies"
  
  relatorios:
    - skill: "report-generation"
    - skill: "pdf-export-patterns"
    - skill: "excel-export-patterns"
```

---

## Exemplos de Roteamento

### Exemplo 1: API de Consulta Sankhya

**Tarefa**: Criar API para consultar contratos do Sankhya com cache

**Roteamento**:
```
Fase 2 (Fundacional):
  - database-design → Modelar entidades
  - redis-patterns → Configurar cache
  - fastapi-router → Estrutura da API

Fase 3 (User Story 1 - Consulta):
  - sql-query-optimizer → Otimizar queries Sankhya
  - caching-patterns → Implementar cache
  - api-patterns → Design de endpoints

Fase 4 (User Story 2 - Export):
  - excel-export-patterns → Exportação XLSX
  - csv-export-patterns → Exportação CSV
  - async-task-patterns → Processamento assíncrono

Segurança (transversal):
  - vulnerability-scanner → Scan de segurança
  - input-validation-patterns → Validação de entrada
```

### Exemplo 2: Dashboard Analytics

**Tarefa**: Criar dashboard de analytics com gráficos

**Roteamento**:
```
Frontend:
  - react-patterns → Estrutura React
  - data-visualization → Gráficos e charts
  - state-management-patterns → Gerenciamento de estado
  - dashboard-design-system → Design de dashboards

Backend:
  - data-pipeline-architecture → Pipeline de dados
  - clickhouse-analytics-patterns → Queries analíticas
  - caching-patterns → Cache de resultados

Integração:
  - api-integration-patterns → Comunicação FE/BE
  - websocket-patterns → Atualizações em tempo real
```

---

## Uso com /speckit.tasks

Quando gerar `tasks.md`, adicione a skill recomendada em cada tarefa:

```markdown
- [ ] T012 [P] [US1] Criar modelo Contrato em `src/models/contrato.py`
  **Skill**: `database-design` + `sqlalchemy-patterns`

- [ ] T013 [US1] Implementar cache com Redis
  **Skill**: `redis-patterns` + `caching-patterns`

- [ ] T014 [US1] Criar endpoint de consulta
  **Skill**: `fastapi-router` + `api-patterns`
```

---

## Comando de Busca de Skills

Para encontrar a skill certa:

```bash
# Buscar por palavra-chave
grep -r "database" .agent/skills/ --include="SKILL.md" | head -10

# Ver índice completo
cat .agent/skills/INDEX.md | grep -A2 "database"

# Listar skills de um squad
ls .agent/skills/ | grep -E "(security|vulnerability|pentest)"
```

---

## Integração com Maestro Leo

O Maestro Leo pode usar este roteador para montar esquadrões:

```
/speckit.router montar esquadrão para API de contratos Sankhya

→ Esquadrão recomendado:
  1. fastapi-router (Backend Lead)
  2. database-design (Data Modeler)
  3. redis-patterns (Cache Specialist)
  4. vulnerability-scanner (Security)
  5. testing-patterns (QA)
```

---

*Skill v1.0 -  SDD*
