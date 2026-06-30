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

---

## 3. Inventário de Dados Disponíveis

O conjunto local da Copa do Mundo de 2022 contém aproximadamente **234 mil
eventos** e **114 campos** observados nos arquivos `events.json`. Nem todo campo
aparece em todos os eventos: cada tipo de ação possui seu próprio subconjunto
de atributos.

| Categoria | Campos principais | Uso analítico |
|---|---|---|
| Identificação | `id`, `index`, `match_id`, `type` | Identificar, ordenar e relacionar eventos |
| Tempo | `period`, `minute`, `second`, `timestamp`, `duration` | Recortes por período, minuto e duração da ação |
| Posse | `possession`, `possession_team`, `play_pattern` | Sequências de posse e origem da jogada |
| Equipe e jogador | `team`, `team_id`, `player`, `player_id`, `position` | Agrupamentos por equipe, atleta e posição |
| Localização | `location` | Coordenada inicial no campo StatsBomb |
| Passe | `pass_length`, `pass_angle`, `pass_end_location`, `pass_recipient`, `pass_outcome` | Volume, precisão, direção e destino dos passes |
| Tipo de passe | `pass_cross`, `pass_switch`, `pass_cut_back`, `pass_through_ball`, `pass_height` | Cruzamentos, inversões, passes para trás e bolas enfiadas |
| Criação | `pass_shot_assist`, `pass_assisted_shot_id`, `shot_key_pass_id` | Assistências para chute e cálculo de xA |
| Chute | `shot_statsbomb_xg`, `shot_outcome`, `shot_end_location`, `shot_body_part` | xG, resultado e destino da finalização |
| Contexto do chute | `shot_technique`, `shot_type`, `shot_freeze_frame`, `shot_first_time` | Técnica, situação e contexto espacial |
| Condução | `carry_end_location` | Distância e progressão com bola |
| Drible | `dribble_outcome`, `dribble_nutmeg`, `dribble_overrun` | Tentativas, sucesso e tipo de drible |
| Duelo | `duel_type`, `duel_outcome` | Desarmes e duelos aéreos |
| Defesa | `interception_outcome`, `ball_recovery_recovery_failure`, `clearance_aerial_won` | Interceptações, recuperações e cortes |
| Pressão | `under_pressure`, `counterpress`, eventos `Pressure` | Execução pressionada e pressão pós-perda |
| Goleiro | `goalkeeper_type`, `goalkeeper_outcome`, `goalkeeper_end_location` | Defesas, domínio, socos e ações fora do gol |
| Disciplina | `foul_committed_card`, `foul_committed_advantage`, `foul_won_advantage` | Faltas, cartões e vantagens |
| Tática | `tactics`, substituições e posições | Formação, escalação e mudanças durante o jogo |

### 3.1 Convenção espacial StatsBomb

- O campo possui dimensão lógica de **120 x 80**.
- `location = [x, y]` representa o início da ação.
- `pass_end_location = [x, y]` representa o destino do passe.
- `carry_end_location = [x, y]` representa o fim da condução.
- `shot_end_location = [x, y, z]` inclui a altura `z` da bola.
- A origem fica no canto superior esquerdo da representação horizontal.
- O eixo `x` percorre o comprimento do campo e o eixo `y` percorre a largura.

### 3.2 Resultados observados

| Campo | Valores mais comuns |
|---|---|
| `pass_outcome` | `Incomplete`, `Out`, `Unknown`, `Pass Offside` |
| `shot_outcome` | `Goal`, `Saved`, `Off T`, `Blocked`, `Post`, `Wayward` |
| `dribble_outcome` | `Complete`, `Incomplete` |
| `duel_type` | `Tackle`, `Aerial Lost` |
| `duel_outcome` | `Won`, `Success In Play`, `Success Out`, `Lost In Play`, `Lost Out` |
| `interception_outcome` | `Won`, `Success In Play`, `Success Out`, `Lost In Play`, `Lost Out` |
| `goalkeeper_type` | `Shot Faced`, `Shot Saved`, `Collected`, `Punch`, `Keeper Sweeper` |
| `goalkeeper_outcome` | `Success`, `Claim`, `In Play Safe`, `In Play Danger`, `Touched Out`, `Fail` |

> **Importante:** no StatsBomb, a ausência de `pass_outcome` significa que o
> passe foi completado. Portanto, não se deve contar apenas eventos com um
> texto de sucesso.

---

## 4. Métricas Percentuais

### 4.1 Já calculadas no dashboard

| Métrica | Fórmula |
|---|---|
| Precisão dos passes | `passes completos / passes tentados * 100` |
| Precisão dos chutes | `chutes no alvo / finalizações * 100` |
| Aproveitamento dos dribles | `dribles completos / dribles tentados * 100` |
| Aproveitamento dos desarmes | `desarmes certos / tentativas de desarme * 100` |

Essas métricas estão disponíveis para equipe e período da partida.

### 4.2 Deriváveis diretamente com os dados atuais

| Métrica sugerida | Numerador | Denominador |
|---|---|---|
| Precisão de passes sob pressão | Passes completos com `under_pressure` | Todos os passes com `under_pressure` |
| Conversão de finalizações | Gols | Finalizações |
| Conversão de chutes no alvo | Gols | Chutes no alvo |
| Taxa de cruzamentos completos | Cruzamentos completos | Passes com `pass_cross == true` |
| Participação de passes progressivos | Passes progressivos | Passes tentados |
| Precisão no terço final | Passes completos iniciados ou terminados no terço final | Passes tentados no mesmo recorte |
| Precisão de passes longos | Passes longos completos | Passes longos tentados |
| Aproveitamento em duelos | Duelos ganhos | Duelos disputados |
| Aproveitamento em duelos aéreos | Duelos aéreos ganhos | Duelos aéreos disputados |
| Sucesso em interceptações | Interceptações ganhas ou bem-sucedidas | Tentativas de interceptação |
| Sucesso em recuperações | Recuperações sem `recovery_failure` | Tentativas de recuperação |
| Percentual de counterpress | Pressões com `counterpress == true` | Todas as pressões |
| Taxa de defesas do goleiro | Defesas | Chutes no alvo enfrentados |
| Sucesso em ações do goleiro | Ações com resultado positivo | Todas as ações do goleiro |
| Conversão de pênaltis | Pênaltis convertidos | Pênaltis cobrados |

### 4.3 Fórmulas auxiliares

```text
porcentagem = numerador / denominador * 100
```

Quando o denominador for zero, o dashboard deve retornar `0` ou indicar que a
métrica não está disponível, evitando divisão por zero.

Para passes completos:

```text
passe completo = type == "Pass" e pass_outcome está vazio
```

Para chutes no alvo:

```text
chute no alvo = shot_outcome em ["Goal", "Saved", "Saved to Post"]
```

Para desarmes bem-sucedidos:

```text
desarme certo = duel_type == "Tackle"
                 e duel_outcome em ["Won", "Success In Play", "Success Out"]
```

---

## 5. Recomendações para Radares

As porcentagens mais úteis para um radar de eficiência são:

1. Precisão dos passes.
2. Precisão dos passes sob pressão.
3. Aproveitamento dos dribles.
4. Aproveitamento dos desarmes.
5. Aproveitamento em duelos aéreos.
6. Taxa de cruzamentos completos.
7. Conversão de finalizações.
8. Taxa de defesas, para goleiros.

Cada porcentagem deve ser acompanhada pelo volume bruto. Exemplo:

```text
Passes sob pressão: 75% (15/20)
```

Isso evita conclusões enganosas como comparar um atleta com `100% (1/1)` a
outro com `88% (44/50)`.

### 5.1 Percentual, percentil e normalização

São conceitos diferentes:

- **Percentual:** taxa de sucesso de uma ação, como `passes certos / passes`.
- **Percentil:** posição do jogador dentro de uma população comparável.
- **Normalização 0-100:** transformação relativa usada atualmente nos radares,
  comparando o valor do jogador ao maior valor observado no seu grupo
  posicional dentro da partida.

Os valores atuais dos radares são **normalizações**, não percentis
estatísticos. Para produzir percentis reais, é necessário definir uma
população de referência, como todos os volantes da Copa, aplicar um mínimo de
minutos e comparar métricas por 90 minutos.
