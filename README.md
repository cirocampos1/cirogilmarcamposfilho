<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/pt/a/a6/Escudo_da_Sele%C3%A7%C3%A3o_Brasileira_de_Futebol.svg" alt="CBF Logo" width="120"/>
  <h1>🏫 CBF Academy — Python para Dados</h1>
  <p><strong>Repositório Oficial do Curso: Aprenda Analytics Avançado de Futebol com Python e Inteligência Artificial Agentic</strong></p>
</div>

---

## 🎯 Sobre o Projeto

Este é o **Monorepo didático** da **CBF Academy** para o curso de **Python para Dados**. 
Aqui, os alunos não apenas aprendem a manipular dados táticos e criar visualizações de alto nível no futebol (usando dados reais como **SofaScore** e **StatsBomb**), mas também aprendem a trabalhar no estado da arte da engenharia de software contemporânea: **usando Agentes Autônomos de IA**.

O seu papel neste curso não é apenas "digitar código infinitamente", mas atuar como um **Arquiteto de Software e Analista Tático**. Você vai projetar as soluções (*Spec-Driven Development*), e o nosso time de Inteligências Artificiais vai ajudá-lo a construir as ferramentas, guiado pelos nossos guias de orquestração.

---

## 🤖 Trabalhando com a Nossa Equipe (Agentes IA)

Para dominar o desenvolvimento impulsionado por Inteligência Artificial, temos uma estrutura clara de papéis definidos no arquivo [`AGENTS.md`](./AGENTS.md) e as regras do jogo de governança em [`ORQUESTRA.md`](./orquestra.md).

Sempre que precisar, invoque nossa equipe durante os seus desafios:
- 🧙‍♂️ **Maestro Leo:** Seu braço direito para orquestrar o trabalho, delegar tarefas e gerenciar o fluxo do desafio.
- 👨‍🏫 **Professor Léo:** Nossa inteligência pedagógica. Peça a ele para explicar métricas táticas (como xG e PPDA) ou detalhar como um trecho complexo de código em Python funciona!
- 📊 **Tech Lead:** Responsável por mensurar o esforço, custo de engenharia e complexidade da implementação.
- 🎨 **ui-ux-pro-max:** O mestre do visual. Se precisar que o seu dashboard atinja o exigente *Padrão WOW Premium*, chame-o!

> **Como invocar?** Interaja normalmente no seu terminal/chat, mencionando o agente (`@Maestro Leo`, `@Professor Léo`) ou utilizando os comandos de Workflow mapeados na nossa infraestrutura!

---

## 📦 Nossos Módulos e Projetos Bases

| Diretório | Descrição | Stack Principal |
|-----------|-----------|-----------------|
| 📓 [`analise-dados/`](./analise-dados/) | **Fundamentos & EDA:** Notebooks didáticos abordando o ABC do Python, Pandas, Matplotlib, e Análise Exploratória do Brasileirão (Série A/B). | `Jupyter`, `Pandas`, `Matplotlib`, `mplsoccer` |
| 📊 [`dashboard/`](./dashboard/) | **SofaScore Dashboard:** API em FastAPI consumindo e processando dados (via Playwright Scraping) para uma interface Web visualmente rica. | `FastAPI`, `Playwright`, `Vanilla JS`, `Chart.js` |
| ⚽ [`statsbomb_aula/`](./statsbomb_aula/) | **Analytics Avançado:** Motor robusto de processamento e extração de insights táticos a partir do StatsBomb Open Data (v4.0). | `FastAPI`, `mplsoccer`, `Pandas`, `Seaborn` |

---

## 🏋️ Desafios (Para Casa)

Para colocar a mão na massa e evoluir o seu portfólio, os alunos farão os "Para Casa" dentro de suas pastas individuais e isoladas: `alunos/seu-nome/`. Lá vocês atuarão como os engenheiros principais!

### 🏆 [Desafio 1: Melhorar o SofaScore Dashboard](./alunos/README.md)
* **Objetivo:** Copie o projeto base `dashboard/` para a sua pasta. Invoque os Agentes (`Maestro Leo`, especialistas em `ui/ux`) para evoluir o sistema: adicione novos filtros, otimize o sistema de cache ou deixe os gráficos e layout com uma estética visual *premium e moderna*.

### 🏆 [Desafio 2: Evolução Tática do Dashboard (StatsBomb)](./statsbomb_aula/README_DESAFIO_2.md)
* **Objetivo:** Dentro da mesma pasta do Desafio 1, você agora vai integrar as rotas do motor tático recém-criado em `statsbomb_aula/`! Crie um Frontend interativo aplicando o Analytics Avançado estudado: *Pressão Pós-Perda (PPDA)*, *radares de performance de jogadores* e *Expected Goals (xG)*, garantindo que o seu painel provoque o "efeito WOW".

> ⚠️ **Regra de Ouro:** Leia os READMEs específicos de cada desafio para o passo-a-passo completo. Nunca altere os códigos do projeto base nas pastas originais. Seu ambiente de trabalho exclusivo e seguro é dentro da pasta `alunos/`.

---

## 🚀 Setup Rápido (Ambiente Único)

Nós utilizamos o **`uv`** (um gerenciador de pacotes ultrarrápido escrito em Rust) juntamente com o conceito de **Workspaces** para unificar todos os projetos de forma elegante.

```bash
# 1. Clonar o repositório para sua máquina local
git clone https://github.com/leojoker/Aula_Cbf.git
cd Aula_Cbf

# 2. Instalar todas as dependências do monorepo de uma só vez
uv sync

# 3. Baixar os binários dos navegadores do Playwright (Essencial para o scraping automatizado do SofaScore)
uv run playwright install chromium
```

---

## 💻 Como Rodar e Testar

### 🖥️ O SofaScore Dashboard (`dashboard/`)

Você precisará de pelo menos um terminal rodando o servidor. Abra um terminal e certifique-se de estar na pasta `dashboard/`:

```bash
# Terminal 1 — Iniciar a API REST (Servidor Local)
cd dashboard
uv run uvicorn app.main:app --reload --port 8000
# 👉 O Dashboard estará acessível em: http://127.0.0.1:8000/dashboard/
```

```bash
# Terminal 2 — Opcional: Acionar a rotina de Ingestão de Dados (Scraping Local Manual)
cd dashboard
uv run python -m app.infra.persist
```

### 📓 Explorando os Notebooks (`analise-dados/`)

Para rodar os notebooks interativos de ciência de dados:

```bash
cd analise-dados
uv run jupyter notebook
```

---

## 🧪 Testes de Qualidade

Nosso ambiente possui um conjunto de testes automatizados (`pytest`) pré-configurados para garantir a solidez da infraestrutura. Você pode rodá-los na raiz ou na pasta do dashboard.

```bash
cd dashboard && uv run pytest app/tests/ -v
```

> **Exemplo de sucesso:**
> ```
> collected 7 items
> test_api.py .........    [57%]
> test_database.py ....    [100%]
> ========================= 7 passed in 0.41s ===============
> ```

---

## 🛠️ Tecnologias e Stack do Projeto

| Camada | Tecnologias Utilizadas |
|--------|-----------------------|
| **Core & Engine** | Python 3.13+ |
| **Backend & APIs** | FastAPI, Uvicorn, Starlette |
| **Automação & Coleta** | Playwright (Headless Chromium) |
| **Banco e Ciência de Dados** | SQLite, Pandas, NumPy |
| **Visualização Tática** | `mplsoccer`, Matplotlib, Seaborn |
| **Frontend UI/UX** | Vanilla JS (ES Modules), CSS Moderno (Glassmorphism), Chart.js |
| **Ferramental, MLOps & Testes**| `uv` (Package Manager Workspace), `pytest`, Jupyter Notebooks |

---

## 📁 Estrutura de Arquivos Resumida

```text
/
├── analise-dados/          # Notebooks: Python intro, Análise Exploratória (Série A/B), Visualizações de Campo
├── dashboard/              # 📊 Projeto Base 1: SofaScore App (FastAPI backend + Vanilla JS frontend)
├── statsbomb_aula/         # ⚽ Projeto Base 2: Motor de processamento tático (StatsBomb Analytics)
├── alunos/                 # 🚀 SEU LOCAL DE TRABALHO: Copie os projetos bases para cá e crie a sua magia!
├── images/                 # Assets de imagens e referências estéticas
├── AGENTS.md               # A Matriz de Papéis da nossa equipe de IA Orquestrada
├── orquestra.md            # Governança de IA (O manual de Spec-Driven Development)
└── pyproject.toml          # Configuração Root Workspace (A espinha dorsal das bibliotecas)
```

---

<div align="center">
  <p><strong>Licença MIT</strong> — Livre para uso educacional e acadêmico.</p>
  <p>Feito com paixão pelo ⚽, Python e muita IA Agentic durante as formações da <strong>CBF Academy</strong>!</p>
</div>
