# speckit-specify

Cria uma especificação de feature estruturada a partir de uma descrição do usuário.

---

## Quando usar

Use esta skill quando:
- Um usuário descrever uma nova feature ou funcionalidade
- Precisar criar uma especificação formal antes da implementação
- Quiser iniciar o processo SDD (Spec-Driven Development)

---

## Comando de Ativação

```
/speckit.specify [descrição da feature]
```

Ou:

```
@ especificar feature: [descrição]
```

---

## Fluxo de Trabalho

### 1. Determinar o próximo número de feature

Escaneie o diretório `specs/` para encontrar o próximo número disponível:

```bash
ls -la specs/ | grep -E '^d' | tail -5
```

Formato: `###-nome-da-feature` (ex: `001-auth-system`, `002-payment-gateway`)

### 2. Criar estrutura de diretórios

```bash
mkdir -p specs/###-nome-da-feature/contracts
```

### 3. Gerar spec.md a partir do template

Copie `.agent/templates/spec-template.md` para `specs/###-nome-da-feature/spec.md` e preencha:

**Seções a preencher**:
- `[NOME_DA_FEATURE]`: Nome descritivo em português
- `[###-nome-da-feature]`: Branch name (kebab-case)
- `[DATA]`: Data atual
- `$ARGUMENTS`: Descrição original do usuário
- **User Stories**: Mínimo 1, máximo 3 para MVP inicial
  - Sempre priorizar como P1, P2, P3
  - Garantir que cada story seja independentemente testável
- **Requisitos Funcionais**: RF-001, RF-002, etc.
- **Critérios de Sucesso**: Métricas mensuráveis
- **Casos de Borda**: Mínimo 3 cenários

### 4. Marcar ambiguidades

Use `[NEEDS CLARIFICATION: pergunta específica]` para marcar:
- Métodos de autenticação não especificados
- Períodos de retenção não definidos
- Escopo de dados não claro
- Integrações necessárias não mencionadas

### 5. Identificar Skills Relevantes

Com base na especificação, identifique skills do catálogo (3400+ disponíveis):

```bash
# Buscar skills relevantes no índice
grep -i "[termo]" .agent/skills/INDEX.md | head -10
```

Adicione seção na spec:

```markdown
## 🤖 Skills Recomendadas

Baseado na análise da feature, as seguintes skills do catálogo  são recomendadas:

### Fase 2: Fundacional
- `database-design` - Modelagem de entidades
- `fastapi-router` - Estrutura da API
- `redis-patterns` - Configuração de cache

### Fase 3: User Stories
- `sql-query-optimizer` - Otimização de queries
- `caching-patterns` - Implementação de cache
- `api-patterns` - Design de endpoints

### Segurança (Transversal)
- `vulnerability-scanner` - Scan de segurança
- `input-validation-patterns` - Validação de entrada

Ver `.agent/skills/INDEX.md` para catálogo completo (3400+ skills).
```

### 6. Validação Constitutional

Verifique na spec:
- [ ] Feature pode ser biblioteca? (Artigo I)
- [ ] Interface CLI identificável? (Artigo II)
- [ ] Testes podem ser escritos primeiro? (Artigo III)

---

## Template de Saída

O arquivo `specs/###-nome-da-feature/spec.md` deve conter:

```markdown
# Especificação de Feature: [NOME]

**Feature Branch**: `[###-nome-da-feature]`
**Criado em**: [DATA]
**Status**: Draft
**Origem**: [descrição do usuário]

## 🎯 Visão Geral
...

## 👤 User Stories & Cenários de Teste
...

## 📋 Requisitos
...

## ✅ Critérios de Sucesso
...

## 🤖 Skills Recomendadas
...

## 🏛️ Checklist de Conformidade Constitucional
...
```

---

## Exemplo de Uso

**Input do usuário**:
```
/speckit.specify Sistema de autenticação com login por email/senha e recuperação de senha
```

**Ações**:
1. Verificar último número em `specs/` → `005-dashboard-ui`
2. Próximo número: `006`
3. Criar `specs/006-auth-system/`
4. Gerar `spec.md` com:
   - User Story 1 (P1): Login com email/senha
   - User Story 2 (P2): Recuperação de senha
   - User Story 3 (P3): Logout e sessão
   - Requisitos RF-001 a RF-008
   - Casos de borda: credenciais inválidas, conta bloqueada, token expirado
   - **Skills recomendadas**:
     - `authentication-patterns`
     - `jwt-security`
     - `password-hashing-patterns`
     - `session-management`
     - `vulnerability-scanner`

---

## Próximos Passos

Após criar a spec:
1. Revisar com o usuário
2. Esclarecer marcadores [NEEDS CLARIFICATION]
3. Confirmar skills recomendadas
4. Quando aprovado, executar `/speckit.plan`

---

*Skill v1.0 -  SDD*
