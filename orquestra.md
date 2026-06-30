🚀 ORQUESTRA:  Spec-Driven
Development (SDD) v4.0


Este documento é a "Fonte Única de Verdade" para o desenvolvimento neste repositório. Ele
define os padrões de engenharia, segurança e orquestração de agentes para o ano de 2026.

🗺 Índice de Navegação

 1. 💎 Metodologia SDD
 2. 🧐 Assertividade Socrática
 3. 🛠 Protocolo de Execução (5 Passos)
 4. 🔗 Matriz de Rastreabilidade
 5. 🕸️ Engine de Context Intelligence (Graphify)
 6. 🧠 Protocolo de Memória Técnica (Graphify)
 7. 🦴 Protocolos de Compressão (RTK & Caveman)
 8. 🧹 Limpeza de Source e Performance
 9. ⚡ Protocolo de Sincronização em Lote (Batch Sync)
 10. 🏛 Constituição 
 11. 📦 Padrões de Projeto
 12. 📚 Catálogo de Skills (3.400+)
 13. 🚦 Status e Governança

💎 Metodologia: Spec-Driven Development (SDD)

O desenvolvimento é guiado por especificações rigorosas. Nenhuma linha de código deve ser
escrita sem uma Spec validada.
 1. Contrato Técnico: Antes de implementar, crie a especificação completa via Sistema
 SDD.
 2. Auditoria Constante: Cada sub-agente valida sua tarefa contra a Spec original.
 3. Segurança em Primeiro Lugar: A Spec deve prever tratamento de erros e proteção de
 dados.
 4. Assertividade Socrática: O Maestro deve fazer perguntas estratégicas ANTES de agir
 para garantir precisão total.
🧐 Assertividade Socrática (MANDATÓRIO)

Para garantir 100% de precisão e evitar retrabalho, o Maestro e seus agentes DEVEM:
 1. Pausar e Perguntar: Antes de qualquer implementação complexa ou alteração
 estrutural, faça perguntas estratégicas.
 2. Entender o "Porquê": Valide o objetivo final e o impacto esperado com o usuário.
 3. Mapear Riscos e Restrições: Questione sobre permissões de banco, limites de gateway
 e fluxos legados.
 4. Validar Hipóteses: Se houver dúvida sobre o comportamento do ERP ou do Banco,
 proponha um teste de hipótese mínima.
 💡 Regra de Ouro: É melhor fazer 5 perguntas assertivas do que 1 implementação com
 premissas erradas.
 5. COMMITS: NUNCA, JAMAIS, FAÇA COMMIT SEM AUTORIZAÇÃO DO HUMANO.

🛠 O Protocolo de Execução SDD (5 Passos)


0. Context Intelligence (Graphify) 🧠

Ação: O Maestro consulta o Grafo de Conhecimento via Graphify para entender
dependências cruzadas (SQL, Python, JS).
 ● Ferramentas: /graphify query (busca semântica), /graphify explain (visão
 360°).
 ● Saída: Relatório de impacto real, God Nodes e surpreendentes conexões afetadas.
 ● Regra: Nunca inicie uma Spec sem consultar o símbolo principal da alteração no Graphify para
 validar a arquitetura antes de especificar.


1. Especificação 📝

Comando: /speckit.specify [descrição da feature]
 ● Ação: Cria specs/###-feature-name/spec.md com user stories, requisitos e skills
 recomendadas.
 ● Saída: Especificação completa + mapeamento inicial de skills do catálogo (3400+
 disponíveis).
 ● Template: .agent/templates/spec-template.md
 /speckit.specify API para consulta de contratos do Sankhya com
 cache Redis


2. Planejamento 🎯

Comando: /speckit.plan
 ● Ação: Cria plano técnico completo com mapeamento de skills por fase.
 ● Saída:
 ○ plan.md - Plano técnico + skills mapeadas
 ○ research.md - Pesquisa de tecnologias
 ○ data-model.md - Modelo de dados
 ○ contracts/api-contracts.md - Contratos de API
 ○ quickstart.md - Guia de validação
 ● Template: .agent/templates/plan-template.md


2.5. TDD (Test-Driven Development) 🧪 [MANDATÓRIO]

Comando: /speckit.tdd [###-feature]
 ● Ação: Cria obrigatoriamente a suíte de testes (Red Phase) antes de qualquer linha de
 código.
 ● Regra de Ouro: Testes de baixo impacto rodam em HOMOLOGAÇÃO. Testes de alto
 impacto usam Mocks ou Sandbox.
 ● Saída: Arquivos em tests/[modulo]/ validados pelo Maestro.
 ● Bloqueio: A fase 4 (Implementação) não inicia se S2.5 não estiver "Done" no Banco Local.


3. Geração de Tarefas 📋

Comando: /speckit.tasks
 ● Ação: Gera lista de tarefas executáveis com skills atribuídas do catálogo.
 ● Saída: tasks.md - Tarefas organizadas por fases e user stories, cada uma com skill
 específica.
 ● Template: .agent/templates/tasks-template.md


4. Implementação 💻
Comando: /speckit.implement [###-feature] [--task TXXX|--phase N|--story USN|--all]
 ● Ação: Executa implementação aplicando padrões das skills atribuídas.
 ● Processo:
 1. Ler tarefa em tasks.md
 2. Identificar skill atribuída
 3. Ler skill do catálogo (.agent/skills/[skill]/SKILL.md)
 4. Aplicar padrões da skill
 5. Implementar código (Green Phase)
 ● Aviso: NUNCA, JAMAIS, EM HIPÓTESE ALGUMA ESCREVA EM PRODUÇÃO. USE
 SEMPRE HOMOLOGAÇÃO.


5. Validação e Entrega ✅

Comando: python .agent/scripts/sdd_checklist.py .
 ● Ação: Validação completa com Gates Constitucionais.
 ● Gates:
 ○ Gate de Simplicidade (Artigo VII) - ≤3 projetos
 ○ Gate Anti-Abstração (Artigo VIII) - Sem wrappers
 ○ Gate Test-First (Artigo III) - Testes primeiro
 ○ Gate Integration-First (Artigo IX) - Bancos reais (HOMOLOGAÇÃO)
 ○ Gate Library-First (Artigo I) - Features como libs
 ○ Gate de Segurança (Artigo X) - Security-first (NO PROD WRITE)
 ● Regra: Se algum Gate falhar, a tarefa é bloqueada até correção.

5.5. Validação Anti-Drift (Pré-Merge) 🚨

Comando: Ativação da skill `drift-check`
 ● Ação: O Rafa (Reviewer) ou os Devs chamam o `drift-check` para comparar o código na branch `master` com o `ORQUESTRA.md` usando o Graphify, evitando o *Specification Drift* antes de jogar para a branch `Main`.

🔗 Matriz de Rastreabilidade SDD (Master Control)

O controle de estado do projeto é gerenciado por um Banco de Dados Local (SQLite) para
performance e escalabilidade, com Audit Log em SQL para versionamento via Git.

Comandos de Gestão:

 ● /speckit.matrix --update: Atualiza o status de uma fase.
 ● /speckit.matrix --render: Atualiza a tabela abaixo com os dados do banco.
 ● /speckit.status: Exibe o dashboard premium no terminal.


📊 View de Rastreabilidade (Renderizada)
| ID | Feature / Módulo | Spec (S1) | Plano (S2) | TDD (S2.5) | Tasks (S3) | Code (S4) | Test (S5) | Handoff (S6) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 001 | Feature 001 | [x] | [x] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 010 | Feature 010 | [x] | [x] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 014 | Feature 014 | [x] | [x] | [ ] | [ ] | [ ] | [ ] | [ ] |


 [!IMPORTANT]
Aos Agentes: A fonte de verdade é o banco specs/orquestra.db. Sempre que alterar o estado,
execute o dump para specs/matrix_audit.sql para garantir a auditoria via Git.

🎼 Orquestração com Maestro leo

Comando: /maestro-leo
 ● Ação: O Maestro lidera o esquadrão baseado na Spec SDD e no Knowledge Graph via
 Graphify.
 ● Integração: O Maestro usa as ferramentas do Graphify para navegar na
 complexidade e o /speckit.router para selecionar skills.
 ● Papéis (Agentes): Condutor, Projetista, Executor, Auditor.
 ● Professor Léo: Agente pedagógico focado em explicar metodologias e códigos de forma didática, respondendo perguntas dos alunos (especial para a CBF Academy).
 ● Co-Piloto de Infraestrutura: O agente harness-leo-custodian atua em paralelo garantindo economia extrema de tokens (via RTK e Caveman) e gerenciando o Blackboard de execução no Graphify.

👥 Humanos no Loop (Desenvolvimento e Validação)
 ● Esquadrão de Devs (7 pessoas): Codificam localmente na branch `master` e garantem a aprovação dos testes. Devem acionar o `drift-check` quando terminam.
 ● Rafa (Code Reviewer & Release Manager): Guardião final. Faz o Code Review da `master` e aplica o merge para produção (`Main`), validando a ausência de *Specification Drift*.

🏢 Sala de Guerra de Diretoria (Opiniões C-Level)

Quando o usuário solicitar opiniões de C-Level ou análise de decisões estratégicas de diretoria, o Maestro ou o agente deve invocar o protocolo da **Sala de Guerra de Diretoria**, assumindo e alternando de forma coesa entre quatro perspectivas fundamentais:
 ● 💰 **CFO (Diretor Financeiro):** Foco em caixa, Burn Rate, Runway, ROI e eficiência operacional financeira.
 ● 📈 **CMO (Diretor de Marketing):** Foco em crescimento, CAC, LTV, funil de vendas e geração de demanda.
 ● 🛠️ **CTO (Diretor de Tecnologia):** Foco em escala de produto, qualidade arquitetural, mitigação de dívida técnica e segurança.
 ● ⚖️ **O Mediador (Orquestrador):** Foco em alinhamento de interesses, síntese estratégica e plano de ação estruturado.

O guia operacional completo com o fluxo de preparação, debate e tomada de decisão estratégica está disponível em:
👉 [.agent/agents/Sala_de_Guerra_Diretoria.md](file:///home/leonardobarbosa/dev//.agent/agents/Sala_de_Guerra_Diretoria.md)

🎯 Sistema de Roteamento Inteligente de Agentes

Com 3.400+ agentes especialistas disponíveis, use o roteamento por contexto:

🧠 Como Funciona

 Sua Solicitação → /speckit.router → Seleção de Skills → Ativação de
 Agente


Comando de Roteamento

 /speckit.router [tarefa ou contexto]



Exemplo:

 /speckit.router qual skill usar para otimizar queries PostgreSQL?
 → Skills recomendadas:
 1. postgresql-optimization-workflow
 2. query-optimization
 3. database-design


📋 Squads e Skills por Categoria



| Squad | Especialidade | Skills de Exemplo |
| :--- | :--- | :--- |
| IA & Contexto | Grafo de Conhecimento, Multimodalidade | graphify, semantic-search, code-archaeologist |
| Engenharia | Desenvolvimento, APIs, Cloud, Git | fastapi-router, api-patterns, clean-code, padroes-de-commits |
| Dados | SQL, Analytics, ML, Vector DB | database-design, postgresql-optimization-workflow, redis-patterns |
| Segurança | Pentest, Auditoria, Compliance | vulnerability-scanner, pentest-checklist, input-validation-patterns |
| UI/UX | Design, Frontend, Mobile | react-patterns, frontend-development-patterns, ui-ux-pro-max |
| DevOps | Deploy, Infra, CI/CD | docker-expert, kubernetes-deployment-workflow, deployment-procedures |
| Ensino & Tutoria | Explicação didática e ensino | professor-leo |
| Sankhya & ERP | Otimização SQL, Procedures, Performance ERP | sankhya-sqlserver-optimization |

🎮 Comandos de Ativação (Context-Aware)


Comando Universal

 "@ preciso de [descrição da tarefa]"


Ativação por Palavras-Chave

Backend & APIs

 "Criar API com..." → Ativa: `speckit.specify` → Skills:
 `fastapi-router`, `api-patterns`
 "Banco de dados..." → Ativa: `speckit.specify` → Skills:
 `database-design`, `sqlalchemy-patterns`
 "Docker/Kubernetes..." → Skills: `docker-expert`,
 `kubernetes-deployment-workflow`



Git & Versionamento

 "Salvar progresso / Fazer commit..." → Skills:
 `padroes-de-commits`, `git-push-workflow`



Frontend & UI

 "Interface React..." → Skills: `react-patterns`,
 `frontend-development-patterns`
 "Design system..." → Skills: `tailwind-design-system`,
 `ui-ux-pro-max`



Dados & ML

 "Vector search..." → Skills: `vector-database-engineer`,
 `similarity-search-patterns`
 "Pipeline de dados..." → Skills: `data-pipeline-architecture`,
 `apache-airflow-dag-patterns`



Segurança

 "Auditar segurança..." → Skills: `vulnerability-scanner`,
 `security-auditing-workflow-bundle`
 "Pentest..." → Skills: `pentest-checklist`,
 `red-team-tools-and-methodology`



Sankhya & ERP

 "Sankhya / SQL Server / Procedure..." → Ativa:
 `sankhya-sqlserver-optimization`
 "Lentidão no ERP / Otimizar query..." → Ativa:
 `sankhya-sqlserver-optimization`


🏛 Constituição  (12 Artigos)

Todo código deve obedecer à Constituição:


| Artigo | Princípio | Descrição |
| :--- | :--- | :--- |
| I | Library-First | Toda feature começa como biblioteca |
| II | CLI Mandate | Toda lib expõe CLI |
| III | Test-First | Testes antes do código (NON-NEGOTIABLE) |
| IV | Simplicidade | Solução mais simples que funciona |
| V | Framework Trust | Use frameworks diretamente |
| VI | Single Model | Uma representação por entidade |
| VII | ≤3 Projects | Máximo 3 projetos |
| VIII | Anti-Abstraction | Justifique cada abstração |
| IX | Integration-First | Bancos reais, não mocks |
| X | Segurança | **NUNCA ESCREVA EM PRODUÇÃO SEM AUTORIZAÇÃO HUMANA.** USE SEMPRE HOMOLOGAÇÃO. O Graphify deve ser usado para validar o impacto de mudanças antes de alterar código crítico. |
| XI | Documentação Localizada | TODA documentação, guia ou artefato gerado deve ser salvo obrigatoriamente seguindo o nível pai da estrutura do projeto (ex: docs/[módulo]/ ou sql/[módulo]/), NUNCA em diretórios temporários (scratch/, brain/) ou de spec. |
| XII | OOP & Design SOLID | Todo código deve ser construído Orientado a Objetos com Alta Coesão, Baixo Acoplamento e aplicando os princípios SOLID. Prefira composição sobre herança, dependa de abstrações e mantenha o encapsulamento rigoroso. |


🧱 Princípios de Design Orientado a Objetos (Artigo XII)

Todo código produzido no repositório deve obedecer aos seguintes princípios de engenharia de software:

1. Paradigma Orientado a Objetos
   O desenvolvimento deve seguir o paradigma OO como padrão primário. Domínios de negócio devem ser modelados como objetos com estado e comportamento coesos, promovendo clareza e reutilização. **CASO A LINGUAGEM SUPORTE O POO**

2. Alta Coesão (Single Responsibility)
   Cada classe, função ou módulo deve ter uma única responsabilidade bem definida. Se uma classe precisa de mais de um motivo para mudar, ela deve ser dividida.

3. Baixo Acoplamento (Dependency Inversion)
   Dependa sempre de abstrações (interfaces, protocolos, ABCs) e nunca de implementações concretas. Módulos de alto nível não devem depender de módulos de baixo nível; ambos devem depender de abstrações.

4. Composição sobre Herança
   Prefira compor comportamentos via injeção de dependências e objetos auxiliares a criar hierarquias profundas de herança. Herança múltipla deve ser evitada; mixins e traits apenas quando justificados.

5. Encapsulamento Rigoroso
   Atributos internos devem ser protegidos (privados/protegidos). Acesso e mutação de estado devem ocorrer exclusivamente via interfaces públicas bem definidas (getters/setters semânticos ou propriedades).

6. Aberto para Extensão, Fechado para Modificação (OCP)
   Novos comportamentos devem ser adicionados estendendo o sistema — via polimorfismo, strategy pattern ou novas implementações de interfaces — sem alterar código existente e testado.

7. Manutenibilidade como Métrica de Qualidade
   O código deve ser legível, testável e de fácil refatoração. Funções e métodos devem ser pequenos (≤30 linhas preferencialmente), com nomes descritivos e sem efeitos colaterais ocultos.

8. Princípio da Segregação de Interfaces (ISP)
   Interfaces devem ser granulares e específicas. Evite "interfaces gordas" que forçam implementações a carregar métodos irrelevantes.

Template: .agent/templates/constitution-template.md

📦 Padrões de Projeto ( Standard)

Todos os projetos devem herdar estes arquivos modulares:
 ● .gitlab-ci.yml: CI/CD rápido via uv (Lint, Test, Security).
 ● .pre-commit-config.yaml: Hooks de ruff, black e detect-secrets.
 ● pyproject.toml: Configuração unificada de ferramentas de qualidade.
 ● .gitignore: Proteção rigorosa contra vazamento de .env, *.key e tokens.
 ● specs/: Diretório de especificações SDD.

📚 Índice Geral de Skills (Catálogo V4.0)

 📊 Total de Agentes Disponíveis: 3.400+
 📁 Local: .agent/skills/
📖 Catálogo Completo: .agent/skills/INDEX.md


🛡 Core & SDD

 ● speckit-specify: Criar especificação de feature.
 ● speckit-plan: Criar plano de implementação.
 ● speckit-tasks: Gerar lista de tarefas.
 ● speckit-implement: Executar implementação.
 ● speckit-router: Roteador para 3.400+ skills.
 ● skill-creator: Criar e otimizar novas skills e agentes baseados em especificações.
 ● maestro-leo: Líder do esquadrão de agentes (integrado ao GitNexus).
 ● harness-leo-custodian: Guardião do estado de execução. Atua em paralelo com o Maestro para gerenciar o Graphify via RTK e Caveman.
 ● drift-check: Validação anti-drift sob demanda para garantir que a `master` respeita a especificação antes do merge do Rafa para a `Main`.
 ● graphify: Navegação profunda em grafos de conhecimento, análise de impacto e busca semântica estruturada.
 ● project-handoff: Gerar documentação técnica de elite (Handoff) ao finalizar um projeto.
 ● brainstorming: Geração de Specs e PRDs.


🌐 UI/UX & Frontend (40+ agentes)

 ● ui-ux-pro-max: Design de elite e estética premium.
 ● frontend-design: Interfaces modernas e interativas.
 ● tailwind-design-system: Sistemas de design com Tailwind.
 ● react-patterns: Padrões avançados de React/Next.js.
 ● awesome-design-md: Coleção de DESIGN.md premium (Vercel, Linear, Stripe, etc.)
 para Padrão WOW.


⚙ Engenharia & DevOps (900+ agentes)

 ● vulnerability-scanner: Auditoria profunda de segurança.
 ● clean-code: Padrões de escrita limpa.
 ● deployment-procedures: Deploy contínuo e seguro.
 ● docker-expert: Containerização e orquestração.
 ● fastapi-router: APIs com FastAPI.
 ● padroes-de-commits: Padronização de tags e emojis de commit (iuricode style).


🗄 Dados & Analytics (150+ agentes)

 ● vector-database-engineer: Pinecone, Weaviate, pgvector.
 ● database-design: Modelagem e otimização SQL.
 ● data-pipeline-architecture: ETLs e pipelines.
 ● redis-patterns: Cache com Redis.


🔒 Segurança (80+ agentes)

 ● pentest-checklist: Testes de penetração.
 ● red-team-tools-and-methodology: Táticas ofensivas.
 ● gdpr-data-handling: Conformidade LGPD/GDPR.


🏢 ERP & Sankhya (Agente Especialista)

 ● sankhya-sqlserver-optimization: Especialista em otimização SQL para ambientes
 Sankhya e SQL Server.

🔍 Como Encontrar o Agente Certo


1. Consulte o Índice

 # Ver catálogo completo
 cat .agent/skills/INDEX.md

 # Total de skills
 ls .agent/skills/ | wc -l

 # Buscar por palavra-chave
 grep -r "nestjs" .agent/skills/ --include="SKILL.md" | head -5
2. Use o Roteamento SDD

 /speckit.router "qual skill devo usar para [tarefa específica]?"


3. Ativação Direta

 "Ative o agente [nome-do-agente]"


🕸️ Engine de Context Intelligence (Graphify)

O  opera com a engine de inteligência de contexto Graphify:

| Engine | Domínio | Propósito | Quando Usar |
| :--- | :--- | :--- | :--- |
| **Graphify** | Conhecimento Geral | Knowledge Graph: documentos, papers, imagens, vídeos, código semântico, community detection e cross-document connections | Explorar arquitetura antes de tocar; conectar conceitos entre docs e código; research corpus; onboarding e codificação |

🛡 Regras de Governança

1. FOCO NO GRAPHIFY PARA CODIFICAÇÃO E CONTEXTO: Durante todo o ciclo de desenvolvimento — especificação, planejamento, implementação e refactor — o Graphify é a ferramenta de context intelligence. Antes de qualquer edição em função, classe ou método, consulte o Graphify. Nunca edite código sem análise de dependências.
2. O Graphify entra em ação durante o desenvolvimento e na fase final, antes do commit, para validação de contexto amplo, documentação do escopo alterado e detecção de conexões cross-document.
3. Sincronização obrigatória: Após grandes refactors, reindexe com `/graphify --update`.

🔶 Graphify — Knowledge Graph

O Graphify transforma qualquer input (código, docs, papers, imagens, vídeos) em um grafo de conhecimento navegável com community detection e audit trail honesto (EXTRACTED / INFERRED / AMBIGUOUS).

Comandos Principais:
● `/graphify` — Pipeline completo no diretório atual → produz `graphify-out/`
● `/graphify <path>` — Pipeline em path específico
● `/graphify <path> --update` — Re-extração incremental (apenas arquivos alterados)
● `/graphify <path> --mode deep` — Extração profunda com edges INFERRED agressivos
● `/graphify query "<question>"` — BFS traversal para contexto amplo
● `/graphify query "<question>" --dfs` — DFS para trace de path específico
● `/graphify path "NodeA" "NodeB"` — Menor caminho entre dois conceitos
● `/graphify explain "NodeName"` — Explicação plain-language de um nó
● `/graphify <path> --watch` — Auto-rebuild em mudanças de código

Outputs:
● `graphify-out/graph.html` — Grafo interativo (abrir no browser)
● `graphify-out/GRAPH_REPORT.md` — Relatório com God Nodes, Surprising Connections e Suggested Questions
● `graphify-out/graph.json` — Dados brutos do grafo (GraphRAG-ready)
● `graphify-out/obsidian/` — Vault para Obsidian (com `--obsidian`)

🧠 Protocolo de Memória Técnica (Graphify)

Para garantir a máxima economia de tokens e precisão arquitetural, o projeto utiliza um sistema
de Grafo de Conhecimento Isento de Ruído via Graphify.

1. Separação de Responsabilidades

 ● Branch master: Contém estritamente o código funcional. Os metadados do Graphify
 são geridos localmente e não entram no versionamento da master.


2. Sincronização de Grafo

Sempre que houver mudanças estruturais (novas classes, grandes refactors), o agente deve:
 1. Commit de Código: Subir as alterações funcionais para a master.
 2. Reindexar: Executar `/graphify --update` no terminal para atualizar o grafo local.
 3. Validar: Pedir ao agente para usar as ferramentas do Graphify para confirmar que a
 versão do grafo está atualizada.

🛡 Gestão do Protocolo ORQUESTRA
(Self-Management)

Para garantir que o ORQUESTRA.md e suas ferramentas (tools/orquestra/) nunca interfiram
no código funcional, seguimos o padrão de Shadow Orchestration.

1. Separação de Responsabilidades

 ● Branch master: Contém apenas os links simbólicos e o registro no .gitignore. Nunca
 possui o histórico desses arquivos.
 ● Branch orquestra-backup: Branch de persistência total dos protocolos, ferramentas de
 TDD e Matriz de Rastreabilidade.


2. Configuração de Ambiente (Worktree)

O uso de Git Worktree é obrigatório para evitar a deleção dos arquivos ao trocar de branch:

 # Estrutura esperada
 ..// # Repositório principal (master)
 ../-orquestra-backup/ # Worktree fixo da branch
 orquestra-backup


3. Fluxo de Sincronização

 1. Edição: Toda edição feita no ORQUESTRA.md na raiz do projeto é refletida no worktree
 (via link simbólico).
 2. Commit: Commits de protocolo devem ser feitos de dentro da pasta
 ../-orquestra-backup/.
 3. Linkagem: Se o link simbólico for perdido em checkouts pesados, restaure-o:
 ln -s ../-orquestra-backup/ORQUESTRA.md ORQUESTRA.md


 4. Consulta para Economia de Tokens (Padrão Pro-Max)

NUNCA leia arquivos de código brutos para entender a arquitetura. Siga esta ordem:
 1. Consulte o Grafo: Use o Graphify (`/graphify query` ou `/graphify explain`) para obter respostas diretas sobre código, contexto amplo e conexões cross-document.
 2. Busca Semântica: Utilize a ferramenta query do Graphify em vez de múltiplos grep.

🦴 Protocolos de Compressão (RTK & Caveman)

O ambiente utiliza o RTK para chamadas de terminal em tempo real e o Caveman para compressão de arquivos pesados, mantendo a sanidade do contexto.

> **💡 Setup Automático:** Todas estas ferramentas de IA (RTK, Caveman, Graphify e demais dependências de Machine Learning) são instaladas automaticamente quando o aluno roda o comando **`uv sync`** na raiz do projeto (conforme ensinado no `README.md`). O ambiente único do `uv` lida com toda a orquestração silenciosamente!

1. Compressão Automática de Terminal (RTK) [MANDATÓRIO]
O RTK intercepta comandos bash (ex: `ls`, `git`, `grep`, test runners) e envia apenas o resumo vital para o LLM. A economia de tokens é automática (redução de 60-90%). Agentes devem usar o terminal livremente sem medo de poluir o contexto.

2. Compressão Semântica (Caveman)

 ● Documentos > 500 linhas: Devem passar pelo caveman-compress antes de serem
 analisados por completo.
 ● Logs de Erro: Utilize o Caveman para extrair apenas a "causa raiz" e o rastro relevante,
 descartando ruído de stack trace repetitivo.
 ● Prompt: "Agente, use o Caveman para comprimir [arquivo/log] antes de prosseguirmos."


2. Governança de Commits

 ● Prefira o uso de caveman commit para garantir que as mensagens sigam o padrão
 semântico de alto nível definido no projeto.


3. Filosofia: Inteligência Máxima, Tokens Mínimos

 ● Regra de Ouro: Se o agente pode entender o problema com 100 tokens (via
 Caveman/Graphify) em vez de 10.000 tokens (leitura bruta), ele deve escolher a via
 comprimida.

⚡ Protocolo de Sincronização em Lote (Batch Sync)

Regra obrigatória para todas as integrações de alto volume (ex: Vibra, SinalSheet, CRM).

1. Proibição de Escrita Unitária

 ● É terminantemente proibido fazer loops de escrita (UPDATE/INSERT) registro a registro
 via HTTP para o Gateway do Sankhya.
 ● O overhead de rede e latência do ERP tornam esse método inaceitável para
 performance Pro-Max.


2. Padrão de Comunicação (XML Batch)

 ● Utilize sempre o padrão XML BATCH enviado via uma Stored Procedure única (ex:
 AD_STP_{MODULO}_SYNC_BATCH).
 ● O XML deve ser gerado no Python usando xml.etree.ElementTree e enviado em um
 parâmetro do tipo XML.
 ● O SQL Server deve processar o lote usando .nodes() para extração em massa.


3. Padrão de Cache (Delta Sync Local)
 ● Antes de processar o lote, o agente deve carregar os registros existentes do Sankhya
 para um dicionário local (existing_map).
 ● Compare os dados novos com o cache em memória ANTES de enviar o lote.
 ● Envie para o banco apenas os registros que efetivamente mudaram (redução de carga
 no SQL).


4. Gestão de Artefatos SQL

 ● O código da Stored Procedure de lote deve ser salvo obrigatoriamente em
 docs/sql/{modulo}_batch_sync.sql.
 ● Mudanças na estrutura da SP devem ser refletidas tanto no repositório Python quanto no
 arquivo SQL de referência.

🧹 Limpeza de Source e Performance (Pro-Max)

Manter o ambiente limpo é crucial para a performance da IA e do desenvolvedor humano.

1. Isolamento de Memória

 ● Assegure-se de que os índices locais do Graphify estejam fora do controle de versão
 principal.


2. Gestão de Ruído

 ● Logs: Logs com mais de 24h ou > 10MB devem ser comprimidos via Caveman ou
 movidos para archive/.
 ● Untracked Files: Mantenha o source livre de arquivos ?? (não rastreados). Se não for
 código ou doc necessária, mova para fora ou adicione ao ignore.


3. Configuração de Editor (Ocultação Visual)

Para foco total, oculte pastas de configuração na interface do usuário:
 ● No VS Code, adicione ao settings.json:



 "files.exclude": {
 "**/.agent": true
 }


🚦 Status e Governança

 ● Maestria: Maestro Leo 🎹
 ● Metodologia: Spec-Driven Development (SDD)
 ● Linguagem: Python (Primary)
 ● Gerenciador: UV 🚀
 ● Segurança: AI-First Guardrails Ativos 🛡 - NUNCA JAMAIS ESCREVA NO BANCO
 SANKHYA SEM A AUTORIZAÇÃO DO HUMANO - NÃO FAÇA COMMIT SEM
 PERMISSÃO HUMANO
 ● Linguagem: Fale sempre em Pt-Br
 ● Total de Agentes: 3.400+ especialistas
 ● Cobertura: Engenharia (75%), Dados (12%), Segurança (7%), UI/UX (3%), Outros (3%)

🗂 Onde Estão os Outros Guias

Como este é o ORQUESTRA (apenas local), os outros documentos estão organizados em:

 specs/
 ├── ./
 │ ├── FLUXO_.md # Fluxo visual completo (v4.0)
 │ └── PLAYBOOK_INICIO_PROJETO.md # Playbook de início
 ├── GUIA_RAPIDO_SDD.md # Guia rápido de uso
 ├── GUIA_USO_SDD.md # Guia completo de uso
 └── .war-room-[projeto]/ # Sala de guerra (criada por
 projeto)
     ├── README.md
     ├── SDD.md # Especificação MACRO
     ├── TODO.md # Backlog
     ├── DECISIONS.md
     └── AGENTS.md

 .agent/
 └── agents/
     └── Sala_de_Guerra_Diretoria.md # Guia de Sala de Guerra de Diretoria (C-Level)



Nota: Todos os arquivos em specs/ são locais (não commitados).
📝 Notas de Uso


Para Tarefas Simples

Use um único agente especialista:

 "Preciso otimizar uma query SQL"
 → Usa: `database-design` ou `postgresql-optimization-workflow`


Para Features Novas (SDD Completo)

Use o fluxo SDD completo:

 "Criar API de consulta de contratos"
 → Fluxo:
 1. /speckit.specify "API de consulta..."
 2. /speckit.plan
 3. /speckit.tasks
 4. /speckit.implement 001-feature --all
 5. python .agent/scripts/sdd_checklist.py .


Para Finalização de Projeto (Handoff)

Use o comando de encerramento para gerar a documentação Pro-Max:

 /speckit.finish



→ Ativa: handoff-specialist → Skills: project-handoff, graphify
→ Gera: ARCHITECTURE.md, API_SPEC.md, MAINTENANCE.md
REGRA DE OURO (Artigo XI): Certifique-se de salvar estas e quaisquer outras
documentações (guias de correção, walkthroughs, logs) exclusivamente seguindo o nível pai
da estrutura do projeto (ex: docs/sinalsheet/ ou sql/sinalsheet/). Agentes não devem deixar
documentações em pastas de specs/ nem em espaços temporários.


Para Tarefas Complexas
Use orquestração multi-agente:

 "Criar um SaaS completo com backend, frontend e mobile"
 → Usa: `maestro-leo` + esquadrão:
 - `speckit-specify` (especificação)
 - `fastapi-router` (backend)
 - `react-patterns` (frontend)
 - `react-native-architecture` (mobile)
 - `docker-expert` (infra)

Para Opiniões de C-Level (Sala de Guerra)
Use o protocolo de debate estratégico de diretoria virtual:
 "Preciso de uma decisão estratégica sobre X"
 → Ativa: `maestro-leo` interpretando a Sala de Guerra:
 - CFO (Caixa & Eficiência)
 - CMO (Crescimento & Funil)
 - CTO (Tecnologia & Escala)
 - Mediador (Síntese & Alinhamento)
 → Guia Operacional completo: [.agent/agents/Sala_de_Guerra_Diretoria.md](file:///home/leonardobarbosa/dev//.agent/agents/Sala_de_Guerra_Diretoria.md)


Para Auditoria

Sempre valide com agentes de segurança:

 "Revisar código antes do deploy"
 → Usa: `vulnerability-scanner` + `sdd_checklist.py`


📖 Documentação SDD

 ● Templates: .agent/templates/
 ● Skills SDD: .agent/skills/speckit-*/
 ● Scripts: .agent/scripts/sdd_checklist.py
 ● Fluxo Completo: specs/./FLUXO_.md
 ● Playbook: specs/./PLAYBOOK_INICIO_PROJETO.md
 ● Guia de Uso: specs/GUIA_USO_SDD.md

🧙‍♂️ Super Poder: Criação Automática de Agentes
(skill-creator)

Agora o sistema possui a capacidade de auto-evolução. O agente skill-creator permite criar
novos especialistas sob demanda.

Como usar:

 1. Defina a intenção: Descreva o que o novo agente deve fazer.
 2. Crie a Spec: Use /speckit.specify para definir o comportamento.
 3. Gere a Skill: O skill-creator criará a estrutura em .agent/skills/[novo-nome]/.
 4. Otimize: Execute o loop de otimização para garantir que o agente ative corretamente:



 python -m .agent.skills.skill-creator.scripts.run_loop --skill-path
 .agent/skills/[novo-nome] --eval-set evals.json --model [model-id]



Este documento é o contrato de operação global do Kit. Atualizado em 2026 com 3.400+
agentes especialistas, capacidade de auto-criação e Protocolo Socrático de Assertividade.

