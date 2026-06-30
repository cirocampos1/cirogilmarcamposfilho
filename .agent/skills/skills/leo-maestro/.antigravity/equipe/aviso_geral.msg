╔══════════════════════════════════════════════════════════════════════════════╗
║                     🚀 LEOMASTER - CONVOCAÇÃO GERAL                          ║
║              Integração CRM  + Sankhya PROD                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

📋 MISSÃO: Finalizar integração do CRM Next.js com dados reais do Sankhya ERP

🧠 RECURSOS DE INTELIGÊNCIA DISPONÍVEIS:
   📁 /home/leonardobarbosa/dev/doc_sankhya/sankhya_assessment_project
   📁 /home/leonardobarbosa/dev/doc_sankhya/temp_mcp_use

🎯 CONTEXTO CRÍTICO:
   - Sankhya PROD ativo (api.sankhya.com.br) - SOMENTE LEITURA
   - Colunas custom: AD_VAL_LIB_ORC, AD_NUFAP, AD_OBSERVACAO  
   - Funções: FC_SALDOPROP_, FC_SALDOPROP__POR_PARC
   - Views: VW_STATUS_PEDIDO
   - Fallback implementado no crm.py (3 níveis)

═══════════════════════════════════════════════════════════════════════════════

👤 AGENTE: @ExploradorSQL
🔍 TAREFA #1: Extrair schema Sankhya do assessment project
   → Mapear TGFCAB, TGFPAR, TGFITE, TGFVEN, TGFPRO
   → Validar existência de AD_VAL_LIB_ORC, VW_STATUS_PEDIDO, FC_SALDOPROP
   → Confirmar tipos de dados e relações
   
   AÇÃO: Ler /home/leonardobarbosa/dev/doc_sankhya/sankhya_assessment_project
         e extrair metadados relevantes para queries CRM

═══════════════════════════════════════════════════════════════════════════════

👤 AGENTE: @BackendDev  
⚙️ TAREFA #2: Validar APIs CRM em app/routers/crm.py
   → Confirmar queries SQL estão otimizadas
   → Verificar fallback de 3 níveis para colunas custom
   → Testar endpoints /api/crm/clientes, /api/crm/pedidos, /api/crm/vendedores
   
   DEPENDÊNCIA: Aguardar dados do ExploradorSQL

═══════════════════════════════════════════════════════════════════════════════

👤 AGENTE: @FrontendDev
💻 TAREFA #3: Integrar Dashboard com APIs reais
   → Atualizar crm/lib//client.ts
   → Conectar crm/app/dashboard/page.tsx com dados reais
   → Remover mocks quando APIs retornarem dados
   
   DEPENDÊNCIA: Aguardar APIs validadas pelo BackendDev

═══════════════════════════════════════════════════════════════════════════════

👤 AGENTE: @AuditorDev
🧪 TAREFA #4: Testar fluxo completo
   → Validar autenticação via sessão 
   → Testar carregamento de dados no Kanban
   → Verificar mapeamento de estágios do funil
   → Confirmar integridade dos dados
   
   DEPENDÊNCIA: Aguardar Frontend integrado

═══════════════════════════════════════════════════════════════════════════════

📡 PROTOCOLO DE COMUNICAÇÃO:
   1. Cada agente cria arquivo em caixa_entrada/ ao iniciar
   2. Atualizar registro_atividades.json ao concluir
   3. Verificar travas/ antes de editar arquivos
   4. Sinalizar bloqueios imediatamente neste canal

🎯 CRITÉRIO DE SUCESSO:
   Acesso a http://localhost:8000/crm mostra Kanban com dados REAIS do Sankhya

═══════════════════════════════════════════════════════════════════════════════

⏰ INÍCIO: Imediato
🎖️ LÍDER: LeoMaster

"A inteligência já existe. Nosso trabalho é conectar."

Assinado: LeoMaster
Data: 2026-03-19
