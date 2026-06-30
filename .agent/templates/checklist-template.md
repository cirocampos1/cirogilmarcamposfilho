# Checklist de Qualidade - 

**Feature**: [NOME_DA_FEATURE]  
**Branch**: [###-nome-da-feature]  
**Data**: [DATA]  
**Responsável**: [NOME]

---

## 🏛️ Gates Constitucionais

### Gate de Simplicidade (Artigo VII)

- [ ] Usando ≤3 projetos/estruturas?
- [ ] Sem "future-proofing" excessivo?
- [ ] Cada projeto tem responsabilidade clara?

**Justificativa se violado**:
```
[Documente por que mais projetos são necessários]
```

### Gate Anti-Abstração (Artigo VIII)

- [ ] Usando framework diretamente (FastAPI, SQLAlchemy)?
- [ ] Representação única de modelos (não duplicar)?
- [ ] Evitando wrappers desnecessários?

**Justificativa se violado**:
```
[Documente por que abstração adicional é necessária]
```

### Gate Test-First (Artigo III)

- [ ] Contratos definidos antes da implementação?
- [ ] Testes de contrato escritos?
- [ ] Testes falhando antes da implementação (Red phase)?

**Evidências**:
```
[Links para testes ou comandos para executar]
```

### Gate Integration-First (Artigo IX)

- [ ] Preferir bancos reais sobre mocks?
- [ ] Ambiente de teste realista definido?
- [ ] Testes de integração planejados/escritos?

**Configuração de teste**:
```
[Descreva como executar testes de integração]
```

### Gate Library-First (Artigo I)

- [ ] Feature pode ser extraída como biblioteca?
- [ ] Interface CLI identificada/implementada?
- [ ] Dependências minimizadas?

**Interface CLI**:
```
[Documente comandos CLI disponíveis]
```

### Gate de Segurança (Artigo X) ⚠️ CRÍTICO

- [ ] **NENHUMA escrita no Sankhya sem validação humana**
- [ ] Dados sensíveis mascarados em logs
- [ ] Autenticação em todos os endpoints
- [ ] Validação de input em todas as APIs
- [ ] Rate limiting configurado
- [ ] Auditoria de ações críticas
- [ ] Secrets em variáveis de ambiente (nunca no código)
- [ ] `detect-secrets` passando

**Revisão de segurança**:
```
[Documente medidas de segurança implementadas]
```

---

## 📋 Completude da Especificação

- [ ] Nenhum marcador [NEEDS CLARIFICATION] permanece
- [ ] Requisitos são testáveis e inequívocos
- [ ] Critérios de sucesso são mensuráveis
- [ ] User stories têm prioridades atribuídas (P1, P2, P3)
- [ ] Casos de borda documentados
- [ ] Dependências identificadas

---

## 🔬 Qualidade Técnica

### Código

- [ ] Type hints em todas as funções públicas
- [ ] Docstrings em módulos, classes e funções públicas
- [ ] `ruff check .` passando sem erros
- [ ] `ruff format --check .` passando
- [ ] `mypy --strict` passando (ou justificativa documentada)
- [ ] Complexidade ciclomática aceitável (< 10 por função)
- [ ] Sem código duplicado (DRY)

### Testes

- [ ] Cobertura mínima de 80%
- [ ] Testes de contrato passando
- [ ] Testes de integração passando
- [ ] Testes unitários passando
- [ ] Todos os testes são determinísticos

### Performance

- [ ] Queries SQL otimizadas (explain analisado)
- [ ] N+1 queries eliminadas
- [ ] Cache aplicado onde apropriado
- [ ] Sem memory leaks aparentes

---

## 📝 Documentação

- [ ] `spec.md` atualizado se houver mudanças
- [ ] `plan.md` atualizado se houver mudanças
- [ ] `tasks.md` marcado com tarefas completas
- [ ] API documentada (OpenAPI/Swagger)
- [ ] CLI documentada (`--help` funcional)
- [ ] README atualizado se necessário
- [ ] CHANGELOG.md atualizado

---

## 🚀 Preparação para Deploy

- [ ] Variáveis de ambiente documentadas
- [ ] Migrations criadas (se aplicável)
- [ ] Scripts de rollback preparados
- [ ] Monitoramento/alertas configurados
- [ ] Feature flags identificadas (se aplicável)

---

## ✅ Aprovação

**Checklist preenchido por**: _________________  
**Data**: _________________

**Revisado por**: _________________  
**Data**: _________________

**Aprovado para merge**: [ ] Sim  [ ] Não - requer correções

**Observações**:
```
[Observações adicionais da revisão]
```

---

*Checklist v1.0 -  SDD*
