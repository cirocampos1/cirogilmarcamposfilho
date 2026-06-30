# 📋 Checklist de Testes - Integração CRM 

> **Agente**: AuditorDev  
> **Data**: 2026-03-19  
> **Versão**: 1.0

---

## 🚀 Setup Inicial

| # | Item | Status | Observações |
|---|------|--------|-------------|
| 1 |  rodando na porta 8000 | ⬜ | `python -m app.main` ou `uvicorn app.main:app --reload` |
| 2 | Banco de dados Sankhya acessível | ⬜ | Verificar conexão com `SANKHYA_TESTE` |
| 3 | Arquivos estáticos em `crm/out/` | ✅ | Build presente (21 arquivos/pastas) |
| 4 | Variáveis de ambiente configuradas | ⬜ | Verificar `.env` do  |

---

## 🔌 APIs Backend

### Clientes
| # | Endpoint | Esperado | Status |
|---|----------|----------|--------|
| 5 | `GET /api/crm/clientes?limit=5` | Lista de clientes do TGFPAR | ⬜ |
| 6 | `GET /api/crm/clientes/{codparc}` | Detalhes de um cliente | ⬜ |
| 7 | `GET /api/crm/clientes/{codparc}/pedidos` | Histórico de pedidos do cliente | ⬜ |

### Pedidos/Orçamentos
| # | Endpoint | Esperado | Status |
|---|----------|----------|--------|
| 8 | `GET /api/crm/pedidos?limit=5&tipo=orcamento` | Lista de orçamentos | ⬜ |
| 9 | `GET /api/crm/pedidos?limit=100` | Lista com todos os filtros | ⬜ |
| 10 | `GET /api/crm/pedidos/{nunota}/itens` | Itens de um pedido | ⬜ |
| 11 | `PUT /api/crm/pedidos/{nunota}/status` | Atualização de status | ⬜ |

### Outros
| # | Endpoint | Esperado | Status |
|---|----------|----------|--------|
| 12 | `GET /api/crm/vendedores` | Lista de vendedores (TGFVEN) | ⬜ |
| 13 | `GET /api/crm/prospectos` | Prospectos não-clientes | ⬜ |
| 14 | `GET /api/crm/analytics/funnel` | Dados mockados do funil | ⬜ |
| 15 | `POST /api/crm/advisor` | Insights do Advisor AI | ⬜ |

---

## 🎨 Frontend

| # | Item | Status | Observações |
|---|------|--------|-------------|
| 16 | Acesso a `http://localhost:8000/crm` | ⬜ | Página de login deve carregar |
| 17 | Login funciona | ⬜ | Autenticação via sessão  |
| 18 | Dashboard carrega | ⬜ | Sem erros de console |
| 19 | Kanban mostra dados reais | ⬜ | Orçamentos do Sankhya |
| 20 | Cards mapeados corretamente | ⬜ | Verificar colunas do Kanban |
| 21 | Drag-and-drop funciona | ⬜ | Movimentação entre colunas |
| 22 | Detalhes do pedido abrem | ⬜ | Modal/drawer com itens |
| 23 | Filtros por vendedor funcionam | ⬜ | Dropdown de vendedores |

---

## 🔄 Mapeamento Kanban

| Estágio | Regra SQL | Teste | Status |
|---------|-----------|-------|--------|
| **qualificacao** | `STATUSNOTA = 'P'` | Orçamento pendente | ⬜ |
| **bloqueado_negociacao** | `STATUS_PEDIDO = 'BLOQUEADO'` | View VW_STATUS_PEDIDO | ⬜ |
| **revisao_tecnica** | `AD_VAL_LIB_ORC > 0` | Valor liberado | ⬜ |
| **fechado_ganho** | `STATUSNOTA = 'L'` | Liberado | ⬜ |
| **perdido** | `STATUSNOTA = 'C'` | Cancelado | ⬜ |

---

## 🔧 Fallback de 3 Níveis (Backend)

| Nível | Descrição | Teste | Status |
|-------|-----------|-------|--------|
| **1 - Full** | Com `VW_STATUS_PEDIDO` e `FC_SALDOPROP_` | Ambos existem | ⬜ |
| **2 - Sem View** | Sem `VW_STATUS_PEDIDO`, mas com function | View ausente | ⬜ |
| **3 - Safe Mode** | Sem colunas AD, sem functions | Tudo padrão | ⬜ |

---

## 🛡️ Segurança

| # | Item | Status | Observações |
|---|------|--------|-------------|
| 24 | CORS configurado para `localhost:3000` | ✅ | `app/main.py` linha 59-65 |
| 25 | Autenticação requerida nas APIs | ✅ | `@router.get` verifica `get_current_user` |
| 26 | SQL Injection protegido | ✅ | Uso de parametrização/filtros sanitizados |
| 27 | Dados sensíveis não expostos | ⬜ | Verificar logs |

---

## 🐛 Testes de Erro

| # | Cenário | Esperado | Status |
|---|---------|----------|--------|
| 28 | Usuário não autenticado | HTTP 401 | ⬜ |
| 29 | Cliente não encontrado | HTTP 404 | ⬜ |
| 30 | Erro de banco de dados | HTTP 500 + log | ⬜ |
| 31 | Fallback query funciona | Retorna dados (modo degradado) | ⬜ |

---

## ✅ Resumo

```
Total de itens: 31
Aprovados: 0
Pendentes: 31
Reprovados: 0
N/A: 5 (configuração CORS/Segurança já validada em código)
```

---

## 📝 Notas do Auditor

### ✅ Pontos Positivos
1. **Estrutura de arquivos** completa e organizada
2. **Fallback de 3 níveis** implementado corretamente em `crm.py`
3. **Mapeamento Kanban** consistente entre backend e frontend
4. **CORS** configurado para porta 3000
5. **AD_OBSERVACAO** removido conforme especificação
6. **Build estático** gerado com sucesso

### ⚠️ Riscos Identificados
1. **VW_STATUS_PEDIDO** - View customizada pode não existir no banco (fallback cobre)
2. **FC_SALDOPROP_** - Function customizada pode não existir (fallback cobre)
3. **AD_VAL_LIB_ORC** - Coluna customizada da TGFCAB (fallback cobre)

### 📌 Próximos Passos
1. Subir o  e testar as APIs manualmente
2. Verificar se o build estático serve corretamente
3. Validar integração completa end-to-end

---

**Status Geral**: 🟡 **PRONTO PARA TESTES** (Código validado, aguardando execução)
