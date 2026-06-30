# 🌾 Skill: Knowledge Harvester (Manu)

Esta skill permite que o agente realize pesquisas profundas e harvesting de conhecimento utilizando um pipeline local (DuckDuckGo + Trafilatura + Ollama).

## 🚀 Objetivo
Transformar uma query de pesquisa em um documento estruturado no formato Obsidian, consolidando informações de múltiplas fontes da web.

## 🛠️ Como Usar
O agente deve invocar o script `main.py` localizado em `tools/autosearch-harvesting/`.

### Comando
```bash
uv run --project tools/autosearch-harvesting python tools/autosearch-harvesting/main.py "[TEMA DE PESQUISA]"
```

## 📋 Fluxo de Execução
1. **Planejamento**: Decomposição da query em subqueries.
2. **Busca**: Coleta de URLs via DuckDuckGo.
3. **Harvesting**: Extração de texto limpo das páginas.
4. **Síntese**: Processamento via Ollama (modelo local).
5. **Arquivamento**: Geração de Markdown na pasta `docs/harvest/` ou similar.

## ⚠️ Restrições
- Requer Ollama rodando localmente.
- Respeita o Artigo XI (Documentação Localizada).
