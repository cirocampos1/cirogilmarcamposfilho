# 🏆 Champions League Dashboard — CBF Academy
## Desafio 2: Evolução Tática do Dashboard (Para Casa)

Este documento documenta as melhorias aplicadas no **StatsBomb World Cup 2022 Tactical Analytics Dashboard** pelo aluno **Caio Barbieri**.

---

## 🎯 1. Visão Geral & Escopo Entregue (Nível 110%)

O dashboard foi evoluído de uma página estática de partida única para uma aplicação analítica interativa com suporte a seleção de partidas da Copa do Mundo de 2022, cálculo dinâmico de KPIs avançados, mapas táticos avançados gerados em backend e um sistema de comparação de jogadores via gráfico de radar com normalização estatística e destaques inteligentes.

### Funcionalidades Implementadas (Entrega Estendida):
1. **Design Padrão WOW Premium:** 
   - Tema escuro sofisticado com paleta de cores balanceada (Home: Azul `#1A78CF` | Away: Amarelo/Dourado `#F1C40F`).
   - Efeitos de **Glassmorphism** com `backdrop-filter: blur(12px)` e bordas sutis brilhantes.
   - Tipografia moderna usando a fonte do Google **Outfit** (`font-family: 'Outfit', sans-serif`).
   - Micro-animações e estados de hover elegantes (`hover-glass`, `scale` e `fadeInUp`).
   - Layout responsivo adaptado para diferentes telas usando CSS Grid e Flexbox.

2. **Novas Métricas de Analytics Avançado:**
   - **Expected Goals (xG):** Probabilidade acumulada de gol de cada finalização efetuada na partida.
   - **Expected Assists (xA):** Acúmulo de xG gerado por passes-chave que resultaram em finalizações.
   - **Passes Progressivos:** Passes que aproximam significativamente a bola do gol adversário (avançam pelo menos 30m na defesa, 15m no meio ou 10m no ataque).
   - **Passes sob Pressão:** Quantidade de passes efetuados e taxa de conclusão sob marcação ativa (`under_pressure`).
   - **High Turnovers:** Recuperações de bola no terço ofensivo (x >= 80).
   - **PPDA (Passes Per Defensive Action):** Nova métrica de intensidade de pressão. Mede a média de passes que a equipe adversária consegue trocar antes de sofrer uma ação defensiva da equipe em campo de ataque. **(Menor valor = Maior intensidade de marcação/pressing)**.

3. **Radar de Performance Comparativa & Tabela de Destaque Inteligente:**
   - Comparação visual lado a lado de dois jogadores selecionados em tempo real na tela.
   - Normalização de 0 a 100% baseada no valor máximo registrado para aquela métrica na partida específica.
   - **Destaques Visuais Comparativos:** A tabela abaixo do radar compara dinamicamente os valores absolutos de cada métrica e destaca em **verde brilhante (`text-emerald-400 font-extrabold`)** o jogador que venceu o duelo estatístico na partida.

4. **Mapas Táticos de Alto Nível:**
   - **Mapa de Finalizações (Shot Map):** Renderizado com `mplsoccer.Pitch.jointgrid` mostrando finalizações e distribuições marginais (KDE) da posição dos chutes.
   - **Fluxo de xG (xG Flow):** Gráfico temporal em degraus mostrando a dinâmica de criação ofensiva no decorrer do tempo.
   - **Rede de Passes (Pass Network):** Grafo mostrando a posição média dos jogadores do time da casa e a força da conexão de passes entre eles.
   - **Mapa de Pressão (Pressure Heatmap):** Mapa de calor por densidade (Kernel Density Estimation) mostrando as zonas de maior pressão defensiva no campo de jogo.

---

## 🛠 2. Arquitetura Técnica

A aplicação foi estruturada de forma modular, respeitando a alta coesão e baixo acoplamento:

```text
statsbomb_aula/
├── app/
│   ├── api/
│   │   └── routes.py           # Endpoints de busca de partidas e processamento dinâmico
│   ├── services/
│   │   ├── statsbomb_parser.py # Lógica de processamento de dados e cálculo de métricas avançadas (com PPDA)
│   │   └── plotter.py          # Lógica gráfica usando Matplotlib, Seaborn e mplsoccer
│   ├── templates/
│   │   └── index.html          # Frontend responsivo estruturado com Tailwind & Custom CSS (com grid de 5 KPIs)
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css      # Design System CSS com Glassmorphism e tipografia Outfit
│   │   └── js/
│   │       ├── app.js          # Arquivo JavaScript principal (Entrypoint do ES Modules - vincula KPI de PPDA)
│   │       ├── components/
│   │       │   ├── PlayerSelector.js # Controle de seletores de jogadores agrupados por time
│   │       │   └── StatsRadar.js     # Gráfico de Radar usando Chart.js + Comparador e realces visuais
│   │       └── services/
│   │           └── api.js      # Serviço HTTP client de consumo de rotas
│   └── main.py                 # Arquivo de inicialização FastAPI
├── tests/
│   └── test_parser.py          # Suíte de testes unitários com asserção matemática de PPDA
```

---

## 🧬 3. Regras de Negócio & Algoritmos

### Passes Progressivos (`is_progressive_pass`)
A lógica de passe progressivo foi modelada medindo a variação da distância cartesiana do ponto inicial $(x_1, y_1)$ e final $(x_2, y_2)$ do passe em relação ao centro do gol adversário $(120, 40)$:
$$\text{distancia\_inicial} = \sqrt{(120-x_1)^2 + (40-y_1)^2}$$
$$\text{distancia\_final} = \sqrt{(120-x_2)^2 + (40-y_2)^2}$$
$$\text{progressao} = \text{distancia\_inicial} - \text{distancia\_final}$$

O passe é considerado progressivo se:
- Iniciado na metade defensiva ($x_1 < 60$) e avançar $\ge 30$ metros.
- Iniciado no meio-campo ($60 \le x_1 < 80$) e avançar $\ge 15$ metros.
- Iniciado no terço ofensivo ($x_1 \ge 80$) e avançar $\ge 10$ metros.

### Expected Assists (xA)
No processamento de eventos, para cada passe-chave (`shot_key_pass_id`), identificamos o chute correspondente e associamos a probabilidade de gol (`shot_statsbomb_xg`) ao passador que efetuou a assistência, gerando o acúmulo de Expected Assists (xA).

### Passes Per Defensive Action (PPDA)
Calculado dinamicamente:
$$\text{PPDA} = \frac{\text{Passes permitidos ao oponente na sua metade de construção } (x \le 80)}{\text{Ações defensivas em campo de ataque } (x \ge 40)}$$
As ações defensivas consideradas são: Duelo, Interceptação, Bloqueio, Faltas Cometidas, Pressão e Recuperação de Bola.

---

## 🚀 4. Como Executar e Validar

### Pré-requisitos
Certifique-se de ter o Python 3.12 ou superior instalado, ou utilize o `uv` (gerenciador rápido):
```bash
# Executar a sincronização das dependências no diretório do projeto
uv sync
```

### Inicialização do Servidor
No diretório `alunos/Caio-barbieri/statsbomb_aula`, inicie o servidor:
```bash
.venv\Scripts\python.exe -m uvicorn app.main:app --port 8000 --reload
```
Acesse `http://localhost:8000` no seu navegador para utilizar o Dashboard.

### Rodando a Suíte de Testes
A suíte de testes unitários garante a robustez das métricas calculadas:
```bash
# Do diretório raiz da Aula_Cbf
$env:PYTHONPATH="alunos/Caio-barbieri/statsbomb_aula"; .venv\Scripts\pytest.exe alunos/Caio-barbieri/statsbomb_aula/tests/
```

---
*Relatório técnico finalizado de nível 110% pelos agentes de orquestração sob supervisão do Maestro Leo para a CBF Academy.*
