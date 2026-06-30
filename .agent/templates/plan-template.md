# Plano de Implementação: [FEATURE]

**Branch**: `[###-nome-da-feature]` | **Data**: [DATA] | **Spec**: [link para spec.md]
**Input**: Especificação de feature de `specs/[###-nome-da-feature]/spec.md`

---

## 📋 Resumo

[Extraído da spec: requisito principal + abordagem técnica da pesquisa]

---

## 🛠️ Contexto Técnico

<!--
  ACTION REQUIRED: Substitua o conteúdo desta seção com os detalhes técnicos
  do projeto.
-->

| Aspecto | Definição |
|---------|-----------|
| **Linguagem/Versão** | Python 3.11+ |
| **Dependências Principais** | FastAPI, SQLAlchemy, Pydantic |
| **Storage** | PostgreSQL (Sankhya), Redis (cache) |
| **Testing** | pytest, pytest-asyncio |
| **Target Platform** | Linux server / Docker |
| **Tipo de Projeto** | API / CLI / Library |
| **Metas de Performance** | [ex: < 200ms p95] |
| **Restrições** | [ex: memória < 512MB] |
| **Escala/Escopo** | [ex: 1k usuários] |

---

## 🏛️ Constitution Check - Gates de Pré-Implementação

*GATE: Deve passar antes da Fase 0 de pesquisa. Re-verificar após Fase 1 de design.*

### Gate de Simplicidade (Artigo VII)

- [ ] Usando ≤3 projetos/estruturas?
- [ ] Sem "future-proofing" excessivo?
- [ ] Cada projeto tem responsabilidade clara?

### Gate Anti-Abstração (Artigo VIII)

- [ ] Usando framework diretamente (FastAPI, SQLAlchemy)?
- [ ] Representação única de modelos (não duplicar)?
- [ ] Evitando wrappers desnecessários?

### Gate Test-First (Artigo III)

- [ ] Contratos definidos antes da implementação?
- [ ] Testes de contrato escritos?
- [ ] Estratégia de testes planejada?

### Gate Integração-First (Artigo IX)

- [ ] Preferir bancos reais sobre mocks?
- [ ] Ambiente de teste realista definido?
- [ ] Testes de integração planejados?

### Gate Library-First (Artigo I)

- [ ] Feature pode ser extraída como biblioteca?
- [ ] Dependências minimizadas?
- [ ] Interface CLI identificada?

---

## 📁 Estrutura do Projeto

### Documentação (esta feature)

```text
specs/[###-feature]/
├── spec.md              # Especificação (/speckit.specify)
├── plan.md              # Este arquivo (/speckit.plan)
├── research.md          # Fase 0 - Pesquisa técnica
├── data-model.md        # Fase 1 - Modelo de dados
├── quickstart.md        # Fase 1 - Guia de validação
├── contracts/           # Fase 1 - Contratos de API
│   ├── api-contracts.md
│   └── event-contracts.md (se aplicável)
└── tasks.md             # Fase 2 - Tarefas (/speckit.tasks)
```

### Código Fonte (raiz do repositório)

```text
# Opção 1: Projeto Único (PADRÃO )
src/
├── __init__.py
├── models/              # Entidades SQLAlchemy/Pydantic
├── services/            # Lógica de negócio
├── api/                 # Rotas FastAPI
├── cli/                 # Interface de linha de comando
└── lib/                 # Utilitários compartilhados

tests/
├── __init__.py
├── contract/            # Testes de contrato
├── integration/         # Testes de integração
├── unit/                # Testes unitários
└── conftest.py          # Fixtures pytest

# Opção 2: Múltiplos Projetos (se necessário)
backend/                 # API FastAPI
├── src/
└── tests/

frontend/                # Se houver interface web
├── src/
└── tests/
```

**Decisão de Estrutura**: [Documente a estrutura selecionada]

---

## 🔬 Fase 0: Pesquisa Técnica

<!-- Gerado pelo comando /speckit.plan -->

### Opções de Tecnologia Avaliadas

| Tecnologia | Prós | Contras | Decisão |
|------------|------|---------|---------|
| [Opção A] | [lista] | [lista] | [✅/❌] |
| [Opção B] | [lista] | [lista] | [✅/❌] |

### Decisões Técnicas

- **[DECISÃO-001]**: [Decisão] - [Racional vinculado a requisito da spec]
- **[DECISÃO-002]**: [Decisão] - [Racional]

### Riscos Identificados

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| [Risco 1] | Alta/Média/Baixa | Alto/Médio/Baixo | [Estratégia] |

---

## 🗄️ Fase 1: Design

<!-- Gerado pelo comando /speckit.plan -->

### Modelo de Dados

Ver `data-model.md` para detalhes completos.

**Entidades Principais**:

```python
# Exemplo de estrutura (não implementação)
class EntidadePrincipal:
    id: UUID
    campo_obrigatorio: str
    created_at: datetime
    updated_at: datetime
```

### Contratos de API

Ver `contracts/api-contracts.md` para detalhes completos.

**Endpoints Principais**:

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| GET | /api/v1/... | [Descrição] | [Sim/Não] |
| POST | /api/v1/... | [Descrição] | [Sim/Não] |

### Fluxo de Dados

```
[Cliente] → [API] → [Service] → [Repository] → [Banco]
                ↓
           [Eventos] → [Queue] → [Workers]
```

---

## 📊 Rastreamento de Complexidade

> **Preencha SOMENTE se houver violações dos Gates Constitucionais que precisem ser justificadas**

| Violação | Por que Necessário | Alternativa Mais Simples Rejeitada Porque |
|----------|-------------------|------------------------------------------|
| [ex: 4º projeto] | [necessidade atual] | [por que 3 projetos são insuficientes] |
| [ex: Repository pattern] | [problema específico] | [por que acesso direto ao DB é insuficiente] |

---

## 🚀 Fases de Implementação

### Fase 1: Setup (Infraestrutura Compartilhada)

- [ ] Criar estrutura de projeto conforme plano
- [ ] Configurar dependências no `pyproject.toml`
- [ ] Configurar linting (ruff) e formatação
- [ ] Setup de testes (pytest, fixtures)

### Fase 2: Fundacional (Pré-requisitos Bloqueantes)

⚠️ **CRÍTICO**: Nenhum trabalho de user story pode começar até esta fase estar completa

- [ ] Setup de conexão com banco (read-only para Sankhya)
- [ ] Implementar estrutura base de autenticação/autorização
- [ ] Configurar logging e tratamento de erros
- [ ] Criar modelos base que todas as stories dependem

**Checkpoint**: Fundação pronta - implementação de user stories pode começar em paralelo

### Fase 3+: User Stories (ver tasks.md)

Cada user story é implementada independentemente conforme `tasks.md`.

---

## 📝 Notas de Implementação

### Padrões a Seguir

1. **Test-First**: Testes antes da implementação
2. **Type Hints**: Sempre usar tipagem completa
3. **Docstrings**: Documentar funções públicas
4. **Logging**: Usar structlog para logs estruturados
5. **Erros**: Usar exceções customizadas do 

### Convenções de Código

- Seguir PEP 8
- Usar `ruff` para lint/format
- Usar `mypy --strict` para type checking
- Máximo 100 caracteres por linha

---

## 🔒 Considerações de Segurança

> **⚠️ ATENÇÃO**: Conforme GUIA_MESTRE v3.1

- [ ] Nenhuma escrita no Sankhya sem validação humana
- [ ] Dados sensíveis são mascarados em logs
- [ ] Autenticação em todos os endpoints
- [ ] Validação de input em todas as APIs
- [ ] Rate limiting configurado
- [ ] Auditoria de ações críticas

---

*Template v1.0 -  SDD*
