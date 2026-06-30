---
name: padroes-de-commits
description: "Padrões de commits com emojis baseados na convenção iuricode/padroes-de-commits"
tools: bash, git
squad: Engenharia
---

# Padrões de Commits (iuricode style)

## Objetivo
Você é um especialista em padrões de commit utilizando emojis e boas práticas da comunidade, baseando-se especificamente no repositório `iuricode/padroes-de-commits`. 
**Sempre** utilize esta skill quando for solicitado para formatar commits com emojis, adotar os padrões convencionais de git commit ou se a task de SDD/Maestro instruir a formatação de commits.

## Tipos de Commits e Emojis Correspondentes

Ao fazer commits, analise as alterações realizadas e enquadre na melhor categoria abaixo, utilizando o Emoji e o Prefixo exato:

| Emoji | Markdown Emoji | Prefixo | Descrição |
|-------|-----------------|---------|-----------|
| 🎉 | `:tada:` | `init:` | Commit inicial do projeto |
| ✨ | `:sparkles:` | `feat:` | Adição ou desenvolvimento de uma nova feature |
| 🐛 | `:bug:` | `fix:` | Corrige um bug ou problema (ex: loop infinito, erro no código) |
| 📚 | `:books:` | `docs:` | Atualizações em documentação (ex: README, wiki) |
| 💡 | `:bulb:` | `docs:` | Comentários e/ou documentações inline no código |
| ♻️ | `:recycle:` | `refactor:` | Refatoração de código (melhoria ou reescrita sem mudança no comportamento) |
| ⚡️ | `:zap:` | `perf:` | Melhorias de performance / tempo de resposta |
| 💄 | `:lipstick:` | `feat:` | Mudanças focadas em estilização CSS/UI e novas telas |
| 🎨 | `:art:` | `style:` | Melhorias de estrutura ou formatação de código (espaçamento, aspas) |
| 🚨 | `:rotating_light:`| `lint:` | Resolvendo problemas indicados no linter/avaliação estática |
| 🧪 | `:test_tube:` | `test:` | Criando e adicionando um novo teste |
| ✅ | `:white_check_mark:`| `test:`| Testes aprovados ou adicionados em suíte existente |
| 🏗️ | `:bricks:` | `ci:` | Modificações de CI/CD (ex: Dockerfile, github actions, gitlab-ci) |
| 📦️ | `:package:` | `build:` | Mudanças que afetam o build ou dependências (npm, uv, requirements.txt) |
| 🔧 | `:wrench:` | `chore:` | Tarefas de configuração, manutenção, ferramentas estruturais |
| 🚚 | `:truck:` | `chore:` | Movendo arquivos ou diretórios, renomeando |
| 💥 | `:boom:` | `fix:` | Revertendo mudanças ineficientes ou que quebram o código seriamente |
| 🧹 | `:broom:` | `cleanup:` | Eliminando código lixo, comentários antigos, var. não utilizadas |
| 🗑️ | `:wastebasket:` | `remove:` | Removendo arquivos inteiros do projeto |
| 🔖 | `:bookmark:` | `release:`| Lançamentos / Versionamento |
| 🗃️ | `:card_file_box:`| `raw:` | Atualização de dados brutos / raw data |

## Estrutura do Commit

Todas as mensagens devem obrigatoriamente seguir esta estrutura:

```
<emoji em texto> <tipo/prefixo>: <mensagem curta em Pt-Br, modo imperativo e tempo presente>

<corpo (opcional) detalhando o porquê da mudança>
```

**Exemplos Reais Padrão iuricode:**
- `:sparkles: feat: Adiciona página de login`
- `:bug: fix: Resolve loop infinito na linha 50`
- `:books: docs: Atualização do README`
- `:recycle: refactor: Passando para arrow functions`
- `:broom: cleanup: Eliminando blocos de código comentados e variáveis não utilizadas`
- `:wastebasket: remove: Removendo arquivos não utilizados do projeto`
- `:lipstick: feat: Estilização CSS do formulário`
- `:tada: init: Commit inicial`

## Passos para o Agente Executar um Commit
1. Analise o `git diff` de forma abrangente para entender a essência e o domínio do que realmente foi alterado.
2. Identifique na tabela o tipo correto de commit e seu respectivo emoji (markdown label).
3. Elabore uma mensagem clara, concisa, em Português (Pt-Br) e preferencialmente no Imperativo ("Adiciona...", "Corrige...").
4. Formate a string, garantindo espaço entre o emoji, o prefixo e a mensagem.
5. Utilize seu comando bash/git para efetuar o commit usando a mensagem gerada. Mantenha as mensagens curtas e objetivas (< 80 caracteres no título).
