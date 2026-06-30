# 🗺️ Guia do Grafo de Conhecimento (Graphify) - 

Este repositório utiliza o **Graphify** para mapear a arquitetura, dependências e o fluxo de dados entre o código Python, SQL e a UI Javascript.

## 🚀 Como visualizar o mapa
Não é necessário instalar nada para visualizar. Basta abrir o arquivo abaixo em qualquer navegador:
👉 [**graphify-out/graph.html**](graphify-out/graph.html)

- **Interatividade:** O grafo é dinâmico (estilo Obsidian). Você pode arrastar, dar zoom e clicar nos nós para ver detalhes.
- **Busca:** Use a barra de busca no topo para encontrar funções, procedures ou arquivos específicos.
- **Legenda:** Clique nos nomes das comunidades à direita para destacar ou ocultar módulos inteiros.

---

## 🧠 Redução de Tokens (Benefício para IA)
**Sim, este grafo é um redutor de tokens massivo.**

Quando você trabalha com um Agente de IA (como Antigravity, Claude ou Codex), o custo e a precisão dependem do "Context Window".
- **Sem Grafo:** A IA precisa ler centenas de arquivos para entender quem chama quem, gastando milhares de tokens e correndo o risco de "alucinar" por falta de contexto.
- **Com Grafo:** O arquivo [**graphify-out/GRAPH_REPORT.md**](graphify-out/GRAPH_REPORT.md) serve como um "índice cerebral". A IA lê esse relatório em milissegundos, entende a hierarquia do projeto e vai direto ao ponto, economizando ~90% de tokens de exploração.

---

## 🛠️ Como atualizar o grafo
O motor oficial fica versionado como submodule em `tools/graphify`. Depois de clonar o repositório, inicialize o submodule uma vez:

```bash
git submodule update --init --recursive
```

Instale o CLI no ambiente virtual local:

```bash
python -m pip install -e tools/graphify
```

No Windows/PowerShell, se o comando `graphify` não estiver no PATH, use:

```powershell
.\.venv\Scripts\graphify.exe update .
```

Para manter o OpenCode sempre orientado pelo grafo, a integração fica versionada em `AGENTS.md` e `.opencode/`.
Se precisar reinstalar manualmente:

```bash
graphify opencode install
```

Para instalar os hooks locais de atualização pós-commit/pós-checkout:

```bash
graphify hook install
```

Se você fizer mudanças estruturais grandes no código, atualize o mapa rodando:

```bash
graphify update .
```

No PowerShell, se aparecer erro de encoding ao imprimir relatórios, rode antes:

```powershell
$env:PYTHONIOENCODING = "utf-8"
```

---

## 📋 Regras de Ouro
1. **Nomenclature:** Os rótulos das comunidades foram ajustados para o domínio da **CBF Academy** (Futebol e Analytics).
2. **Privacidade:** Este grafo é exclusivo da nossa turma. Referências a projetos corporativos de outras empresas são estritamente proibidas para não poluir o contexto tático.
3. **Física:** A visualização HTML está configurada com física ativa para facilitar a percepção de clusters de código correlacionado.

---
*Gerado automaticamente via Graphify Engine.*
