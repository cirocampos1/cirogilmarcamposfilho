# Tarefas: [NOME_DA_FEATURE]

**Input**: Documentos de design de `/specs/[###-nome-da-feature]/`
**Pré-requisitos**: plan.md (obrigatório), spec.md (obrigatório para user stories)

---

## 📋 Formato: `[ID] [P?] [Story] Descrição`

- **[P]**: Pode rodar em paralelo (arquivos diferentes, sem dependências)
- **[Story]**: Qual user story esta tarefa pertence (ex: US1, US2, US3)
- **Inclua caminhos de arquivo exatos nas descrições**

---

## Convenções de Caminho

- **Projeto único**: `src/`, `tests/` na raiz do repositório
- **Web app**: `backend/src/`, `frontend/src/`
- **Caminhos mostrados assumem projeto único - ajuste conforme plan.md**

---

## Fase 1: Setup (Infraestrutura Compartilhada)

**Propósito**: Inicialização do projeto e estrutura básica

- [ ] T001 Criar estrutura de projeto conforme plano de implementação
- [ ] T002 Inicializar projeto Python com dependências (FastAPI, SQLAlchemy, etc.)
- [ ] T003 [P] Configurar ferramentas de linting e formatação (ruff, mypy)
- [ ] T004 Configurar pytest e estrutura de testes
- [ ] T005 Criar `conftest.py` com fixtures base

---

## Fase 2: Fundacional (Pré-requisitos Bloqueantes)

**Propósito**: Infraestrutura core que DEVE estar completa antes de QUALQUER user story

⚠️ **CRÍTICO**: Nenhum trabalho de user story pode começar até esta fase estar completa

Exemplos de tarefas fundacionais (ajuste conforme seu projeto):

- [ ] T006 [P] Configurar conexão com banco de dados (read-only Sankhya)
- [ ] T007 [P] Implementar estrutura de autenticação/autorização
- [ ] T008 Configurar estrutura de rotas e middleware da API
- [ ] T009 Criar modelos base/entidades que todas as stories dependem
- [ ] T010 Configurar tratamento de erros e logging estruturado
- [ ] T011 Configurar gerenciamento de configuração de ambiente

**Checkpoint**: Fundação pronta - implementação de user stories pode começar em paralelo

---

## Fase 3: User Story 1 - [Título] (Prioridade: P1) 🎯 MVP

**Objetivo**: [Breve descrição do que esta story entrega]

**Teste Independente**: [Como verificar esta story funcionando sozinha]

### Testes para User Story 1 (OPCIONAL - apenas se testes solicitados) ⚠️

> **NOTA: Escreva estes testes PRIMEIRO, garanta que FALHEM antes da implementação**

- [ ] T012 [P] [US1] Teste de contrato para [endpoint] em `tests/contract/test_[nome].py`
- [ ] T013 [P] [US1] Teste de integração para [jornada do usuário] em `tests/integration/test_[nome].py`

### Implementação para User Story 1

- [ ] T014 [P] [US1] Criar modelo [Entidade1] em `src/models/[entidade1].py`
- [ ] T015 [P] [US1] Criar modelo [Entidade2] em `src/models/[entidade2].py`
- [ ] T016 [US1] Implementar [Serviço] em `src/services/[servico].py` (depende de T014, T015)
- [ ] T017 [US1] Implementar [endpoint/feature] em `src/api/[arquivo].py`
- [ ] T018 [US1] Adicionar validação e tratamento de erros
- [ ] T019 [US1] Adicionar logging para operações da user story 1
- [ ] T020 [US1] Criar CLI para [funcionalidade] em `src/cli/[comando].py`

**Checkpoint**: Neste ponto, User Story 1 deve estar totalmente funcional e testável independentemente

---

## Fase 4: User Story 2 - [Título] (Prioridade: P2)

**Objetivo**: [Breve descrição do que esta story entrega]

**Teste Independente**: [Como verificar esta story funcionando sozinha]

### Testes para User Story 2 (OPCIONAL)

- [ ] T021 [P] [US2] Teste de contrato para [endpoint] em `tests/contract/test_[nome].py`
- [ ] T022 [P] [US2] Teste de integração para [jornada] em `tests/integration/test_[nome].py`

### Implementação para User Story 2

- [ ] T023 [P] [US2] Criar modelo [Entidade] em `src/models/[entidade].py`
- [ ] T024 [US2] Implementar [Serviço] em `src/services/[servico].py`
- [ ] T025 [US2] Implementar [endpoint/feature] em `src/api/[arquivo].py`
- [ ] T026 [US2] Integrar com componentes da User Story 1 (se necessário)

**Checkpoint**: Neste ponto, User Stories 1 E 2 devem funcionar independentemente

---

## Fase 5: User Story 3 - [Título] (Prioridade: P3)

**Objetivo**: [Breve descrição do que esta story entrega]

**Teste Independente**: [Como verificar esta story funcionando sozinha]

### Testes para User Story 3 (OPCIONAL)

- [ ] T027 [P] [US3] Teste de contrato para [endpoint] em `tests/contract/test_[nome].py`
- [ ] T028 [P] [US3] Teste de integração para [jornada] em `tests/integration/test_[nome].py`

### Implementação para User Story 3

- [ ] T029 [P] [US3] Criar modelo [Entidade] em `src/models/[entidade].py`
- [ ] T030 [US3] Implementar [Serviço] em `src/services/[servico].py`
- [ ] T031 [US3] Implementar [endpoint/feature] em `src/api/[arquivo].py`

**Checkpoint**: Todas as user stories devem estar funcionalmente independentes

---

## Fase N: Polimento & Preocupações Transversais

**Propósito**: Melhorias que afetam múltiplas user stories

- [ ] TXXX [P] Atualizações de documentação em `docs/`
- [ ] TXXX Limpeza de código e refatoração
- [ ] TXXX Otimização de performance em todas as stories
- [ ] TXXX [P] Testes unitários adicionais (se solicitados) em `tests/unit/`
- [ ] TXXX Fortalecimento de segurança
- [ ] TXXX Executar validação do quickstart.md

---

## 🔗 Dependências & Ordem de Execução

### Dependências de Fase

```
Setup (Fase 1) → Foundational (Fase 2) → User Stories (Fase 3+)
     ↓                ↓ (BLOQUEIA)            ↓ (paralelo possível)
  Sem deps      Bloqueia todas stories    Cada story independente
```

- **Setup (Fase 1)**: Sem dependências - pode começar imediatamente
- **Fundacional (Fase 2)**: Depende da conclusão do Setup - BLOQUEIA todas as user stories
- **User Stories (Fase 3+)**: Todas dependem da conclusão da Fase Fundacional
  - User stories podem prosseguir em paralelo (se houver equipe)
  - Ou sequencialmente em ordem de prioridade (P1 → P2 → P3)
- **Polimento (Fase Final)**: Depende de todas as user stories desejadas estarem completas

### Dependências de User Story

- **User Story 1 (P1)**: Pode começar após Fundacional (Fase 2) - Sem dependências em outras stories
- **User Story 2 (P2)**: Pode começar após Fundacional (Fase 2) - Pode integrar com US1 mas deve ser testável independentemente
- **User Story 3 (P3)**: Pode começar após Fundacional (Fase 2) - Pode integrar com US1/US2 mas deve ser testável independentemente

### Dentro de Cada User Story

1. Testes (se incluídos) DEVEM ser escritos e FALHAR antes da implementação
2. Modelos antes de serviços
3. Serviços antes de endpoints
4. Implementação core antes de integração
5. Story completa antes de mover para próxima prioridade

### Oportunidades de Paralelização

- Todas as tarefas de Setup marcadas [P] podem rodar em paralelo
- Todas as tarefas Fundacionais marcadas [P] podem rodar em paralelo (dentro da Fase 2)
- Uma vez que Fundacional completa, todas as user stories podem começar em paralelo (se capacidade da equipe permitir)
- Todos os testes para uma user story marcados [P] podem rodar em paralelo
- Modelos dentro de uma story marcados [P] podem rodar em paralelo
- Diferentes user stories podem ser trabalhadas em paralelo por diferentes membros da equipe

---

## 🎯 Estratégias de Implementação

### MVP First (Apenas User Story 1)

1. Completar Fase 1: Setup
2. Completar Fase 2: Fundacional (CRÍTICO - bloqueia todas as stories)
3. Completar Fase 3: User Story 1
4. **PARAR E VALIDAR**: Testar User Story 1 independentemente
5. Deploy/demo se pronto

### Entrega Incremental

1. Completar Setup + Fundacional → Fundação pronta
2. Adicionar User Story 1 → Testar independentemente → Deploy/Demo (MVP!)
3. Adicionar User Story 2 → Testar independentemente → Deploy/Demo
4. Adicionar User Story 3 → Testar independentemente → Deploy/Demo
5. Cada story adiciona valor sem quebrar stories anteriores

### Estratégia de Equipe Paralela

Com múltiplos desenvolvedores:

1. Equipe completa Setup + Fundacional juntos
2. Uma vez Fundacional pronto:
   - Desenvolvedor A: User Story 1
   - Desenvolvedor B: User Story 2
   - Desenvolvedor C: User Story 3
3. Stories completam e integram independentemente

---

## 📝 Notas

- `[P]` tarefas = arquivos diferentes, sem dependências
- `[Story]` label mapeia tarefa para user story específica para rastreabilidade
- Cada user story deve ser completável e testável independentemente
- Verifique que testes falham antes de implementar
- Commit após cada tarefa ou grupo lógico
- Pare em qualquer checkpoint para validar story independentemente
- Evite: tarefas vagas, conflitos de mesmo arquivo, dependências cross-story que quebram independência

---

*Template v1.0 -  SDD*
