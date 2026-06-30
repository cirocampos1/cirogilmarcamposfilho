# Especificação Técnica: Desafio 1 — Melhorias SofaScore Dashboard

## 1. Escopo e Objetivos
Esta especificação descreve as melhorias implementadas no dashboard de performance de jogadores (SofaScore) para a CBF Academy. O objetivo principal é enriquecer a experiência visual (WOW design), permitir a comparação interativa de estatísticas e mapas táticos de dois jogadores na mesma partida, e adicionar estados de carregamento (shimmers) e tratamento de erros robusto.

## 2. Requisitos de Comparação
- **Seletor**: Um dropdown secundário com ID `compare-player-select`, habilitado apenas após um jogador principal ser selecionado.
- **Gráfico de Radar**: Mostrar o contorno do jogador principal (Verde Esmeralda: `#10b981`) e do jogador comparado (Laranja/Ambar: `#f59e0b` ou Azul: `#3b82f6`).
- **Mapas de Atividades**: Quando a comparação estiver ativa, os mapas de calor, passes e chutes devem ser exibidos lado a lado em colunas de 50%/50% com legendas claras.
- **Cards de Estatísticas**: Cada estatística principal deve ser comparada e exibir qual jogador teve a maior métrica através de um indicador de destaque visual.

## 3. Requisitos de UI / Tratamento de Erro
- **Skeletons**: Ao trocar de jogador ou partida, todos os contêineres de dados devem exibir shimmers animados.
- **Mensagem de Erro**: O toast de erro deve ser exibido caso qualquer chamada de API falhe.
