# Dicionário de Dados: StatsBomb Open Data

Neste documento, traduzimos a especificação oficial do **StatsBomb Open Data** (v4.0.0) para os alunos e exploramos como usar cada bloco de dado para construir inteligência tática (Analytics).

---

## 1. Dicionário de Eventos Principais

### 1.1 Passes (`type.name == "Pass"`)
O evento de passe é um dos mais ricos. Cada passe possui:
- `pass_length` e `pass_angle`: Distância percorrida e ângulo do passe (em radianos).
- `pass_recipient`: Jogador alvo do passe.
- `pass_cross` (Booleano): Se foi um cruzamento (originado da lateral, entrando na área).
- `pass_cut_back`: Se foi um passe atrasado para a entrada da área.
- `pass_switch`: Se foi uma virada de jogo (passou de 50% do campo verticalmente).
- `pass_shot_assist`: Se este passe resultou diretamente em uma finalização.
- `pass_outcome`: Pode ser "Incomplete", "Out", "Pass Offside", etc. Se for vazio, o passe foi concluído com sucesso.

### 1.2 Finalizações (`type.name == "Shot"`)
Descreve todas as tentativas de gol.
- `shot_statsbomb_xg`: O Expected Goals (xG) da finalização (chance de 0.0 a 1.0).
- `shot_end_location`: [x, y, z], indicando onde a bola passou no gol (z é a altura).
- `shot_freeze_frame`: Um *array* com a posição exata de *todos os jogadores* na tela no momento do chute (permitindo cálculos avançados de tráfego/barreira na frente da bola).
- `shot_outcome`: "Goal", "Saved", "Off T" (para fora), "Blocked", "Post" (trave).
- `shot_technique` e `shot_body_part`: Chute normal, voleio, calcanhar, pé esquerdo/direito, cabeça.

### 1.3 Conduções (`type.name == "Carry"`)
Quando o jogador tem a posse e move a bola nos pés.
- `carry_end_location`: Onde a condução terminou. O delta entre `location` e `carry_end_location` permite ver quem mais avançou campo com a bola no pé.

### 1.4 Ações Defensivas (`Pressure`, `Duel`, `Interception`, `Clearance`, `Block`)
Ações sem a posse de bola.
- `counterpress` (Booleano): Presente em eventos defensivos quando a ação ocorre nos 5 segundos imediatamente após o time perder a posse de bola.
- `under_pressure` (Booleano): Flag que aparece nos eventos (como Passe e Condução) indicando que o jogador sofreu pressão durante a execução.

---

## 2. O Que Podemos Fazer (Visão Tática / Professor Léo)

Com base nestes dados crus, proponho as seguintes aplicações para a **CBF Academy**:

### A. Análise de Construtores de Jogo (Playmakers)
> **Métrica Alvo:** Expected Assists (xA) e Passes Quebra-Linhas.
* **Como fazer:** Somar o `shot_statsbomb_xg` das finalizações para o jogador que originou a chance através do `pass_shot_assist`. Com o `pass_end_location`, filtrar passes que começam no meio e terminam no terço final (Passes Progressivos).

### B. Análise de Intensidade Defensiva
> **Métrica Alvo:** PPDA (Passes Allowed Per Defensive Action) e Mapa de *Counterpress*.
* **Como fazer:** Filtrar eventos defensivos com a flag `counterpress == TRUE` para ver onde o time pressionou logo após perder a bola (famoso perde-pressiona estilo Guardiola/Klopp). Contar a taxa de passes do oponente na defesa vs ações de pressão do time.

### C. Valorização da Posse de Bola e Progressão (Ball Progression)
> **Métrica Alvo:** Carries Progressivos.
* **Como fazer:** Usar a diferença entre o `location` e o `carry_end_location` para medir quais jogadores, como zagueiros construtores ou pontas, percorreram mais metros verticais com a bola dominada sem perdê-la.

### D. Radares Individuais (Player Radars)
> **Métrica Alvo:** Comparação Percentil de Atletas.
* **Como fazer:** Criar gráficos radiais comparando um jogador (ex: Casemiro) contra a média de todos os volantes da Copa do Mundo em métricas normalizadas por 90 minutos (Passes Certos P90, Desarmes P90, Passes sob pressão P90).
