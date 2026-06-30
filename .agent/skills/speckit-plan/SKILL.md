# speckit-plan

Cria um plano de implementação técnico baseado na especificação de feature, integrando com as 3400+ skills do .

---

## Quando usar

Use esta skill quando:
- Uma spec.md já existe e foi aprovada
- Precisar definir abordagem técnica, stack e arquitetura
- Quiser criar research.md, data-model.md e contracts/
- Necessite mapear tarefas para skills específicas do catálogo

---

## Comando de Ativação

```
/speckit.plan [contexto técnico opcional]
```

Ou:

```
@ criar plano de implementação para [###-nome-da-feature]
```

---

## Pré-requisitos

- Arquivo `specs/###-nome-da-feature/spec.md` deve existir
- Spec deve estar em status "Approved" ou equivalente
- Catálogo de skills disponível em `.agent/skills/INDEX.md`

---

## Fluxo de Trabalho

### 1. Ler a especificação

```bash
cat specs/###-nome-da-feature/spec.md
```

Extrair:
- User stories e prioridades
- Requisitos funcionais
- Entidades mencionadas
- Restrições e requisitos não-funcionais
- **Skills já recomendadas na spec**

### 2. Pesquisar Skills no Catálogo

Com base na spec, busque skills adicionais no catálogo de 3400+:

```bash
# Buscar por tecnologia
ls .agent/skills/ | grep -E "fastapi|database|redis"

# Buscar no índice
grep -i "cache" .agent/skills/INDEX.md

# Ver skills de segurança
ls .agent/skills/ | grep -E "(security|vulnerability|pentest)"
```

### 3. Executar Gates Constitucionais

Antes de qualquer planejamento, verifique:

```markdown
## 🏛️ Constitution Check - Gates de Pré-Implementação

### Gate de Simplicidade (Artigo VII)
- [ ] Usando ≤3 projetos/estruturas?
- [ ] Sem "future-proofing" excessivo?

### Gate Anti-Abstração (Artigo VIII)
- [ ] Usando framework diretamente (FastAPI, SQLAlchemy)?
- [ ] Representação única de modelos (não duplicar)?

### Gate Test-First (Artigo III)
- [ ] Contratos definidos antes da implementação?
- [ ] Testes de contrato escritos?

### Gate Integration-First (Artigo IX)
- [ ] Preferir bancos reais sobre mocks?
- [ ] Ambiente de teste realista definido?

### Gate Library-First (Artigo I)
- [ ] Feature pode ser extraída como biblioteca?
- [ ] Interface CLI identificada?

### Gate de Segurança (Artigo X)
- [ ] Nenhuma escrita Sankhya sem validação humana?
- [ ] Dados sensíveis protegidos?
```

**Se algum gate falhar**: Documente a justificativa na seção "Rastreamento de Complexidade"

### 4. Mapeamento de Skills por Fase

Crie um mapeamento detalhado de skills para cada fase:

```markdown
## 🤖 Mapeamento de Skills por Fase

### Fase 1: Setup
| Tarefa | Skills Recomendadas | Squad |
|--------|---------------------|-------|
| Estrutura de projeto | `clean-code`, `python-patterns` | Core |
| Configurar lint/format | `ruff-patterns`, `mypy-patterns` | Core |
| Setup de testes | `testing-patterns`, `pytest-patterns` | QA |

### Fase 2: Fundacional
| Tarefa | Skills Recomendadas | Squad |
|--------|---------------------|-------|
| Modelagem de dados | `database-design`, `sqlalchemy-patterns` | Dados |
| Configurar cache | `redis-patterns`, `caching-patterns` | Dados |
| Estrutura API | `fastapi-router`, `api-patterns` | Engenharia |
| Autenticação | `authentication-patterns`, `jwt-security` | Segurança |

### Fase 3+: User Stories
| User Story | Skills Recomendadas | Squad |
|------------|---------------------|-------|
| US1 - Consulta | `sql-query-optimizer`, `pagination-patterns` | Dados |
| US2 - Cache | `caching-patterns`, `redis-patterns` | Dados |
| US3 - Export | `excel-export-patterns`, `async-task-patterns` | Engenharia |

### Transversal (Todas as Fases)
| Aspecto | Skills Recomendadas | Squad |
|---------|---------------------|-------|
| Segurança | `vulnerability-scanner`, `input-validation-patterns` | Segurança |
| Testing | `contract-testing`, `integration-testing-patterns` | QA |
| DevOps | `docker-expert`, `deployment-procedures` | DevOps |
```

### 5. Fase 0: Pesquisa Técnica (research.md)

Crie `specs/###-nome-da-feature/research.md`:

```markdown
# Pesquisa Técnica: [FEATURE]

## Opções de Tecnologia Avaliadas

| Tecnologia | Prós | Contras | Decisão |
|------------|------|---------|---------|
| [Opção A] | [lista] | [lista] | [✅/❌] |

## Decisões Técnicas

- **[DECISÃO-001]**: [Decisão] - [Racional vinculado a requisito da spec]

## Skills do Catálogo Consultadas

- `skill-name-1` - [Como se aplica]
- `skill-name-2` - [Como se aplica]

## Riscos Identificados

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| [Risco 1] | Alta/Média/Baixa | Alto/Médio/Baixo | [Estratégia] |
```

### 6. Fase 1: Design

#### 6.1 Data Model (data-model.md)

Crie `specs/###-nome-da-feature/data-model.md`:

```markdown
# Modelo de Dados: [FEATURE]

## Entidades

### [Entidade 1]
```python
class Entidade1(Base):
    __tablename__ = "entidade1"
    
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    campo1: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime]
```

## Relacionamentos

```
[Entidade1] 1:N [Entidade2]
[Entidade2] N:1 [Entidade3]
```

## Índices

- `idx_entidade1_campo1` em `entidade1.campo1`

## Skills Aplicáveis

- `database-design` - Modelagem
- `sqlalchemy-patterns` - Implementação
- `migration-patterns` - Migrations
```

#### 6.2 API Contracts (contracts/api-contracts.md)

Crie `specs/###-nome-da-feature/contracts/api-contracts.md`:

```markdown
# Contratos de API: [FEATURE]

## Endpoints

### POST /api/v1/[recurso]

**Request**:
```json
{
  "campo1": "string",
  "campo2": 123
}
```

**Response 200**:
```json
{
  "id": "uuid",
  "campo1": "string",
  "created_at": "2026-01-01T00:00:00Z"
}
```

## Skills Aplicáveis

- `api-patterns` - Design de endpoints
- `fastapi-router` - Implementação
- `contract-testing` - Validação
```

### 7. Plano de Implementação (plan.md)

Copie `.agent/templates/plan-template.md` para `specs/###-nome-da-feature/plan.md` e preencha:

**Seções obrigatórias**:
- Contexto Técnico (linguagem, dependências, storage)
- Constitution Check (todos os gates)
- **Mapeamento de Skills por Fase** (integração com catálogo)
- Estrutura do Projeto (documentação + código)
- Fase 0: Pesquisa (resumo do research.md)
- Fase 1: Design (resumo do data-model.md e contracts/)
- Rastreamento de Complexidade (se houver violações)

### 8. Quickstart (quickstart.md)

Crie `specs/###-nome-da-feature/quickstart.md`:

```markdown
# Quickstart: [FEATURE]

## Validação Rápida

### Testar User Story 1

```bash
# 1. Iniciar serviços
docker-compose up -d

# 2. Executar migrations
uv run alembic upgrade head

# 3. Testar endpoint
curl -X POST http://localhost:8000/api/v1/[endpoint] \
  -H "Content-Type: application/json" \
  -d '{"campo": "valor"}'
```

## Cenários de Validação

- [ ] User Story 1 funciona conforme critérios de aceitação
- [ ] User Story 2 funciona conforme critérios de aceitação
- [ ] Casos de borda são tratados corretamente

## Skills para Validação

- `testing-patterns` - Execução de testes
- `contract-testing` - Validação de contratos
- `api-testing-patterns` - Testes de API
```

---

## Saída Esperada

Após executar esta skill, o diretório deve conter:

```
specs/###-nome-da-feature/
├── spec.md              # (já existia)
├── plan.md              # (novo) - INCLUI MAPEAMENTO DE SKILLS
├── research.md          # (novo) - INCLUI SKILLS CONSULTADAS
├── data-model.md        # (novo) - INCLUI SKILLS APLICÁVEIS
├── quickstart.md        # (novo) - INCLUI SKILLS PARA VALIDAÇÃO
└── contracts/
    └── api-contracts.md # (novo) - INCLUI SKILLS APLICÁVEIS
```

---

## Próximos Passos

Após criar o plano:
1. Revisar decisões técnicas com o usuário
2. Confirmar mapeamento de skills
3. Ajustar se necessário
4. Executar `/speckit.tasks` para gerar lista de tarefas com skills atribuídas

---

## Integração com Catálogo de Skills

Para consultar skills disponíveis:

```bash
# Índice completo
cat .agent/skills/INDEX.md

# Buscar por squad
grep -A5 "Engenharia" .agent/skills/INDEX.md

# Listar todas as skills
ls .agent/skills/ | wc -l  # ~3400 skills
```

---

*Skill v1.0 -  SDD*
