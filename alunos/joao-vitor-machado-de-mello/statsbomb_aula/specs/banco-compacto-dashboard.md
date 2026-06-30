# Especificação — banco compacto para execução do dashboard

## Objetivo

Permitir que uma cópia do projeto obtida pelo Git execute o dashboard apenas
com a instalação das dependências e o comando `uvicorn`, sem reconstruir dados
e sem depender da árvore de JSONs brutos.

## Requisitos

1. O artefato distribuído deve ser um único arquivo
   `data/dashboard.sqlite3`.
2. O banco deve conter o manifesto das partidas e o payload completo das 64
   partidas já calculado.
3. Cada payload deve ser serializado em JSON e compactado individualmente com
   `zlib`, permitindo carregar somente a partida selecionada.
4. A API deve consultar primeiro o banco compacto.
5. Os carregadores atuais de `data/processed/` permanecem disponíveis como
   compatibilidade para desenvolvimento e reconstrução.
6. A execução do dashboard não deve importar pandas, PyArrow nem ler
   `data/raw/`.
7. O script `scripts/build_dashboard_data.py` deve gerar ou atualizar o banco
   compacto ao final de uma construção completa.
8. Deve existir uma opção para empacotar artefatos processados já existentes
   sem recalcular as métricas.
9. A versão distribuída no Git não deve precisar de `data/raw/` nem dos
   centenas de arquivos em `data/processed/matches/`.
10. O endpoint e o contrato consumido pela interface devem permanecer iguais.

## Validação

- Carregar o manifesto e partidas diretamente do SQLite.
- Validar cache por partida.
- Subir o FastAPI com somente `dashboard.sqlite3` disponível.
- Abrir partidas em desktop e mobile sem erro.
- Confirmar redução do número de arquivos e do tamanho da pasta `data/`.
