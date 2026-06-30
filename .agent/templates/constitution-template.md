# Constituição do 

**Versão**: 1.0  
**Data**: 2026  
**Status**: Ativa

> *"Código serve às especificações. Especificações não servem ao código."*

---

## 📜 Preâmbulo

Esta Constituição estabelece os princípios imutáveis que governam o desenvolvimento no . Ela garante consistência, simplicidade e qualidade em todo o código gerado, independentemente de qual LLM ou desenvolvedor esteja trabalhando.

---

## Artigo I: Princípio Library-First

**Texto Constitucional**:

> Toda feature no  DEVE começar sua existência como biblioteca standalone. Nenhuma feature será implementada diretamente dentro do código da aplicação sem primeiro ser abstraída em um componente de biblioteca reutilizável.

**Racional**:
- Força design modular desde o início
- Facilita testes isolados
- Permite reutilização entre projetos
- Reduz acoplamento

**Aplicação**:
- Antes de criar código em `app/` ou `src/`, pergunte: "Isso pode ser uma lib?"
- Estruture features como pacotes independentes
- Use interfaces claras entre componentes

---

## Artigo II: Mandato de Interface CLI

**Texto Constitucional**:

> Toda biblioteca DEVE expor sua funcionalidade através de interface de linha de comando.

**Requisitos da CLI**:
- Aceitar texto como input (via stdin, argumentos ou arquivos)
- Produzir texto como output (via stdout)
- Suportar formato JSON para troca de dados estruturados

**Racional**:
- Garante observabilidade
- Facilita testes e debugging
- Permite automação e scripting
- Torna funcionalidade acessível e verificável

---

## Artigo III: Imperativo Test-First

**Texto Constitucional**:

> **ISSO É NÃO-NEGOCIÁVEL**: Toda implementação DEVE seguir Desenvolvimento Guiado por Testes (TDD) estrito. Nenhum código de implementação será escrito antes de:
> 1. Testes unitários serem escritos
> 2. Testes serem validados e aprovados pelo usuário
> 3. Testes serem confirmados como FALHANDO (fase Vermelha)

**Fluxo TDD**:
1. 🔴 **Red**: Escreva teste, veja falhar
2. 🟢 **Green**: Escreva código mínimo para passar
3. 🔵 **Refactor**: Melhore código mantendo testes passando

**Racional**:
- Especifica comportamento antes da implementação
- Garante cobertura de testes
- Facilita refactoring seguro
- Documenta uso através de exemplos

---

## Artigo IV: Princípio de Simplicidade

**Texto Constitucional**:

> A solução mais simples que funciona é sempre a preferida. Complexidade acidental deve ser eliminada. Abstrações prematuras são proibidas.

**Diretrizes**:
- Resolver o problema atual, não problemas futuros hipotéticos
- Evitar "e se" - implementar apenas o que é necessário agora
- Preferir código explícito sobre código "elegante" e obscuro
- Questionar toda camada de abstração: "Isso realmente é necessário?"

---

## Artigo V: Confiança no Framework

**Texto Constitucional**:

> Use features do framework diretamente em vez de criar wrappers. Não abstraia abstrações.

**Aplicação no **:
- Use FastAPI diretamente (não crie "wrapper routes")
- Use SQLAlchemy diretamente (não crie "base models" desnecessários)
- Use Pydantic diretamente para validação
- Não crie "utilitários" que apenas repassam chamadas

**Exceções permitidas**:
- Quando múltiplas integrações precisam de interface unificada
- Quando necessário para testes (mas preferir testes de integração)

---

## Artigo VI: Representação Única de Modelos

**Texto Constitucional**:

> Cada conceito de domínio deve ter exatamente UMA representação canônica no sistema.

**Proibições**:
- Não duplicar modelos entre camadas (DB, API, Domain)
- Não criar "DTOs" desnecessários
- Não criar "ViewModels" que apenas copiam dados

**Abordagem **:
- Use SQLAlchemy 2.0 com Mapped[] para modelos híbridos
- Use Pydantic models para validação de API
- Converta apenas quando necessário (na borda do sistema)

---

## Artigo VII: Gate de Simplicidade de Projetos

**Texto Constitucional**:

> Máximo de 3 projetos/estruturas para implementação inicial. Projetos adicionais requerem justificativa documentada.

**Contagem**:
- Cada diretório com `pyproject.toml` independente = 1 projeto
- Frontend e backend = 2 projetos
- Adicionar mobile = 3 projetos
- Mais que isso = requer aprovação explícita

**Justificativas aceitáveis**:
- Separação mandatada por requisitos de deploy
- Necessidade de linguagens diferentes
- Restrições de compliance

---

## Artigo VIII: Gate Anti-Abstração

**Texto Constitucional**:

> Toda abstração deve ser justificada por um problema específico que ela resolve. Abstrações "por precaução" são proibidas.

**Checklist antes de criar abstração**:
- [ ] Qual problema específico isso resolve?
- [ ] Por que a solução direta é insuficiente?
- [ ] Quantos lugares usarão isso?
- [ ] O custo da abstração é menor que o custo da duplicação?

**Padrões comumente over-engineered** (requerem justificativa):
- Repository Pattern (use SQLAlchemy diretamente)
- Service Layer desnecessário
- Factory methods para casos simples
- Interfaces para classes com uma única implementação

---

## Artigo IX: Testes Integration-First

**Texto Constitucional**:

> Testes DEVEM usar ambientes realistas:
> - Preferir bancos de dados reais sobre mocks
> - Usar instâncias reais de serviços sobre stubs
> - Testes de contrato são obrigatórios antes da implementação

**Prioridade de Testes**:
1. **Contract tests**: Valida contratos de API
2. **Integration tests**: Testa fluxos completos com dependências reais
3. **Unit tests**: Apenas para lógica pura/complexa

**Exceções para mocks**:
- Serviços externos de terceiros (use contratos)
- Recursos que não podem ser provisionados em CI
- Casos de erro que são difíceis de reproduzir

---

## Artigo X: Segurança como Fundação

**Texto Constitucional**:

> Segurança não é uma feature. É uma fundação. Todo código DEVE considerar segurança desde a concepção.

**Regras Inegociáveis do **:
- **NUNCA JAMAIS ESCREVA NO BANCO SANKHYA SEM AUTORIZAÇÃO DO HUMANO**
- Dados sensíveis nunca em logs
- Validação de input em todas as APIs
- Autenticação em todos os endpoints (exceto explicitamente públicos)
- Auditoria de ações críticas
- Secrets nunca no código (use variáveis de ambiente)

---

## 📋 Processo de Emenda

**Seção 4.2: Processo de Emenda**

Modificações nesta constituição requerem:
1. Documentação explícita da racional para a mudança
2. Revisão e aprovação pelos mantenedores do projeto
3. Avaliação de compatibilidade retroativa
4. Atualização do CHANGELOG.md

**Princípios Imutáveis** (nunca podem ser alterados):
- Artigo III (Test-First)
- Artigo X (Segurança)

---

## ✅ Gates de Pré-Implementação

Antes de iniciar qualquer implementação, verifique:

### Gate de Simplicidade (Artigo VII)
- [ ] Usando ≤3 projetos?
- [ ] Sem "future-proofing" excessivo?

### Gate Anti-Abstração (Artigo VIII)
- [ ] Usando framework diretamente?
- [ ] Representação única de modelos?

### Gate Test-First (Artigo III)
- [ ] Contratos definidos?
- [ ] Testes de contrato escritos?

### Gate Integration-First (Artigo IX)
- [ ] Preferir bancos reais sobre mocks?
- [ ] Ambiente de teste realista definido?

### Gate Library-First (Artigo I)
- [ ] Feature pode ser extraída como biblioteca?
- [ ] Interface CLI identificada?

### Gate de Segurança (Artigo X)
- [ ] Nenhuma escrita Sankhya sem validação?
- [ ] Dados sensíveis protegidos?

---

## 🎯 Aplicação no Fluxo SDD

### Fase 1: Especificação (/speckit.specify)
- Validar contra Constituição antes de aprovar spec
- Marcar violações conhecidas com justificativas

### Fase 2: Plano (/speckit.plan)
- Executar todos os Gates antes de prosseguir
- Documentar exceções na seção "Rastreamento de Complexidade"

### Fase 3: Tarefas (/speckit.tasks)
- Garantir que tarefas de teste vêm antes de implementação
- Estruturar por user stories independentes

### Fase 4: Implementação (/speckit.implement)
- Validar cada PR contra Gates
- Rejeitar código que viola princípios constitucionais

---

*Constituição  v1.0 - Baseada no Spec-Kit GitHub*
