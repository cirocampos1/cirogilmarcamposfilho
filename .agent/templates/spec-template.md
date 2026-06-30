# Especificação de Feature: [NOME_DA_FEATURE]

**Feature Branch**: `[###-nome-da-feature]`  
**Criado em**: [DATA]  
**Status**: Draft  
**Origem**: Descrição do usuário: "$ARGUMENTS"

---

## 🎯 Visão Geral

<!-- Descreva O QUE esta feature faz e POR QUE é importante -->

[Resumo em 2-3 parágrafos do objetivo da feature e do valor entregue ao usuário]

---

## 👤 User Stories & Cenários de Teste *(obrigatório)*

<!--
  IMPORTANTE: User stories devem ser PRIORIZADAS como jornadas ordenadas por importância.
  Cada user story deve ser INDEPENDENTEMENTE TESTÁVEL.
  
  Atribua prioridades (P1, P2, P3...), onde P1 é a mais crítica.
  Cada story é uma fatia standalone que pode ser:
  - Desenvolvida independentemente
  - Testada independentemente
  - Deployada independentemente
  - Demonstrada aos usuários independentemente
-->

### User Story 1 - [Título Breve] (Prioridade: P1)

[Descreva esta jornada do usuário em linguagem simples]

**Por que esta prioridade**: [Explique o valor e por que tem este nível de prioridade]

**Teste Independente**: [Como esta story pode ser testada independentemente]

**Critérios de Aceitação**:

1. **Dado** [estado inicial], **Quando** [ação], **Então** [resultado esperado]
2. **Dado** [estado inicial], **Quando** [ação], **Então** [resultado esperado]

---

### User Story 2 - [Título Breve] (Prioridade: P2)

[Descreva esta jornada do usuário em linguagem simples]

**Por que esta prioridade**: [Explique o valor]

**Teste Independente**: [Como testar]

**Critérios de Aceitação**:

1. **Dado** [estado inicial], **Quando** [ação], **Então** [resultado esperado]

---

### User Story 3 - [Título Breve] (Prioridade: P3)

[Descreva esta jornada do usuário em linguagem simples]

**Por que esta prioridade**: [Explique o valor]

**Teste Independente**: [Como testar]

**Critérios de Aceitação**:

1. **Dado** [estado inicial], **Quando** [ação], **Então** [resultado esperado]

---

### Casos de Borda *(obrigatório)*

<!--
  ACTION REQUIRED: Preencha com os casos de borda específicos desta feature
-->

- O que acontece quando [condição de limite]?
- Como o sistema lida com [cenário de erro]?
- O que ocorre se [condição inesperada]?
- Como tratar [estado inválido]?

---

## 📋 Requisitos *(obrigatório)*

<!--
  ACTION REQUIRED: Preencha os requisitos específicos.
  Use [NEEDS CLARIFICATION: pergunta específica] para marcar ambiguidades.
-->

### Requisitos Funcionais

- **RF-001**: O sistema DEVE [capacidade específica]
- **RF-002**: O sistema DEVE [capacidade específica]
- **RF-003**: Usuários DEVEM poder [interação chave]
- **RF-004**: O sistema DEVE [requisito de dados]
- **RF-005**: O sistema DEVE [comportamento]

*Exemplo de marcação para requisitos não claros:*

- **RF-006**: O sistema DEVE autenticar usuários via [NEEDS CLARIFICATION: método de auth não especificado - email/senha, SSO, OAuth?]
- **RF-007**: O sistema DEVE reter dados do usuário por [NEEDS CLARIFICATION: período de retenção não especificado]

### Requisitos Não-Funcionais

- **RNF-001**: Performance - [métrica específica, ex: "resposta < 200ms p95"]
- **RNF-002**: Segurança - [requisito de segurança]
- **RNF-003**: Disponibilidade - [ex: "99.9% uptime"]
- **RNF-004**: Escalabilidade - [ex: "suportar 10k usuários simultâneos"]

### Entidades Principais *(incluir se a feature envolve dados)*

- **[Entidade 1]**: [O que representa, atributos chave sem implementação]
- **[Entidade 2]**: [O que representa, relacionamentos com outras entidades]

---

## ✅ Critérios de Sucesso *(obrigatório)*

<!--
  ACTION REQUIRED: Defina critérios de sucesso mensuráveis.
  Devem ser agnósticos de tecnologia e mensuráveis.
-->

### Resultados Mensuráveis

- **CS-001**: [Métrica mensurável, ex: "Usuários completam ação em menos de 2 minutos"]
- **CS-002**: [Métrica de performance, ex: "Sistema processa 1000 requisições/segundo sem degradação"]
- **CS-003**: [Métrica de satisfação, ex: "90% dos usuários completam tarefa na primeira tentativa"]
- **CS-004**: [Métrica de negócio, ex: "Reduzir tickets de suporte relacionados a [X] em 50%"]

---

## 🏛️ Checklist de Conformidade Constitucional

Antes de prosseguir para o plano de implementação, verifique:

- [ ] Esta feature pode ser implementada como biblioteca independente? (Artigo I)
- [ ] A interface pode ser exposta via CLI? (Artigo II)
- [ ] Os testes podem ser escritos antes da implementação? (Artigo III)
- [ ] Não estamos criando abstrações desnecessárias? (Artigo VIII)
- [ ] Estamos usando ≤3 projetos/estruturas? (Artigo VII)

---

## 📝 Notas & Decisões

<!-- Registre decisões importantes durante a especificação -->

### Decisões Tomadas

- **[DATA]**: [Decisão] - [Racional]

### Questões em Aberto

- [NEEDS CLARIFICATION: descrição da dúvida]

### Dependências

- [Dependência de sistema/serviço existente]

---

## 🔒 Nota de Segurança

> **⚠️ IMPORTANTE**: Conforme o GUIA_MESTRE v3.1:
> - **NUNCA JAMAIS ESCREVA NO BANCO SANKHYA SEM AUTORIZAÇÃO DO HUMANO**
> - Toda interação com dados sensíveis deve ser auditada
> - Seguir princípios de Security-First do 

---

## 🔗 Rastreabilidade de Código (Obrigatório)

> [!IMPORTANT]
> Esta seção deve ser preenchida pelo agente após a implementação. Liste todos os componentes de código que pertencem a esta especificação.

| Tipo | Arquivo / Componente | Descrição da Responsabilidade |
|:---|:---|:---|
| Backend | `caminho/do/arquivo.py` | [Descrição da lógica implementada] |
| Frontend | `caminho/do/componente.tsx` | [Descrição da interface] |
| SQL | `sql/procedura_xyz.sql` | [Descrição da Stored Procedure] |
| Test | `tests/test_xyz.py` | [Descrição da cobertura de teste] |

---

## 📎 Referências


- [Links para documentação relacionada]
- [Links para pesquisas anteriores]
- [Links para specs de features relacionadas]

---

*Template v1.0 -  SDD*
