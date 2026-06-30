import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mplsoccer import Pitch, PyPizza, Bumpy
import io
import base64

def get_base64_image(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', transparent=True, dpi=120)
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

def get_pitch():
    # Campinho verde clássico com linhas brancas
    return Pitch(
        pitch_type='opta',
        pitch_color='#1B8C42',
        line_color='#ffffff',
        linewidth=1.2
    )

def plot_heatmap(heatmap_data):
    if not heatmap_data:
        return None

    import cmasher as cmr
    pitch = get_pitch()
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#000000')
    
    x = [pt.get('x', pt.get('playerCoordinates', {}).get('x')) for pt in heatmap_data]
    y = [pt.get('y', pt.get('playerCoordinates', {}).get('y')) for pt in heatmap_data]
    x = [val for val in x if val is not None]
    y = [val for val in y if val is not None]

    if not x or not y:
        return get_base64_image(fig)

    # Mapa de calor usando o colormap cmr.nuclear
    pitch.kdeplot(
        x, y, 
        ax=ax, 
        fill=True, 
        levels=100, 
        cmap='cmr.nuclear', 
        alpha=0.75
    )
    
    return get_base64_image(fig)

def plot_shotmap(shots):
    if not shots:
        return None

    pitch = get_pitch()
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#000000')
    
    for s in shots:
        coords = s.get('playerCoordinates', {})
        if not coords:
            continue
            
        is_goal = s.get('shotType') == 'goal'
        # Verde para gol e Vermelho para outros chutes
        color = '#10b981' if is_goal else '#ef4444'
        marker_size = 220 if is_goal else 130
        marker_edge = 'white' if is_goal else 'none'
        
        pitch.scatter(coords['x'], coords['y'], 
                     s=marker_size, color=color, edgecolors=marker_edge, 
                     ax=ax, alpha=0.9, zorder=3)
                     
    return get_base64_image(fig)

def plot_passmap(passes):
    """Fallback clássico: mapa de passes individual."""
    if not passes:
        return None

    pitch = get_pitch()
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#000000')
    
    for p in passes:
        coords = p.get('playerCoordinates', {})
        end_coords = p.get('passEndCoordinates', {})
        
        if not coords or not end_coords:
            continue
            
        outcome = p.get('outcome', True)
        # Verde para completo e Vermelho para incompleto
        color = '#10b981' if outcome else '#ef4444'
        
        pitch.arrows(coords['x'], coords['y'], 
                    end_coords['x'], end_coords['y'], 
                    width=1.5, headwidth=4, 
                    color=color, ax=ax, alpha=0.8)
                    
    return get_base64_image(fig)

def plot_pass_network(passes_list, player_names_map, team_side):
    """Gera uma Pass Network (Rede de Passes) tática do time."""
    pitch = get_pitch()
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#000000')
    
    if not passes_list:
        return get_base64_image(fig)
        
    color = '#10b981' if team_side == 'home' else '#ef4444'
    
    # 1. Calcular a posição média de cada jogador baseada nos eventos
    player_positions = {}
    player_names = {}
    
    for p in passes_list:
        p_id = p.get('player_id')
        p_name = p.get('player_name', player_names_map.get(p_id, ''))
        x = p.get('x') or p.get('playerCoordinates', {}).get('x')
        y = p.get('y') or p.get('playerCoordinates', {}).get('y')
        
        if p_id is not None and x is not None and y is not None:
            if p_id not in player_positions:
                player_positions[p_id] = []
                player_names[p_id] = p_name
            player_positions[p_id].append((x, y))
            
    player_avg_positions = {}
    for p_id, coords in player_positions.items():
        avg_x = sum(c[0] for c in coords) / len(coords)
        avg_y = sum(c[1] for c in coords) / len(coords)
        player_avg_positions[p_id] = (avg_x, avg_y)
        
    # 2. Contar passes completos entre os jogadores do mesmo time
    pass_counts = {}
    player_pass_totals = {}
    
    for p in passes_list:
        if not p.get('outcome', True):
            continue
        sender = p.get('player_id')
        # Tenta descobrir o recebedor do evento (se existir)
        receiver = p.get('receiver_id')
        
        if sender is not None and receiver is not None and sender in player_avg_positions and receiver in player_avg_positions:
            pair = (sender, receiver)
            pass_counts[pair] = pass_counts.get(pair, 0) + 1
            player_pass_totals[sender] = player_pass_totals.get(sender, 0) + 1

    if not player_avg_positions:
        return get_base64_image(fig)
        
    # 3. Desenhar linhas de conexão (limiar de mínimo 2 passes para reduzir ruído)
    max_passes_between = max(pass_counts.values()) if pass_counts else 1
    for (sender, receiver), count in pass_counts.items():
        if count < 2:
            continue
        start_x, start_y = player_avg_positions[sender]
        end_x, end_y = player_avg_positions[receiver]
        
        linewidth = (count / max_passes_between) * 4 + 0.5
        alpha = min(0.7, (count / max_passes_between) * 0.5 + 0.2)
        
        pitch.arrows(start_x, start_y, end_x, end_y,
                     width=linewidth, headwidth=3, color=color,
                     alpha=alpha, ax=ax, zorder=2)
                     
    # 4. Desenhar os nós dos jogadores (tamanho proporcional ao volume de passes)
    max_passes_player = max(player_pass_totals.values()) if player_pass_totals else 1
    for p_id, (x, y) in player_avg_positions.items():
        passes_count = player_pass_totals.get(p_id, 1)
        node_size = (passes_count / max_passes_player) * 350 + 80
        
        pitch.scatter(x, y, s=node_size, color='#121212', edgecolors=color,
                      linewidth=2, ax=ax, zorder=3)
                      
        name = player_names.get(p_id, '')
        display_name = name.split()[-1] if name else ''
        if display_name:
            ax.text(x, y - 3.5, display_name, color='#ffffff', fontsize=8,
                    ha='center', va='center', zorder=4,
                    bbox=dict(facecolor='#000000', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.15'))
                    
    return get_base64_image(fig)

def plot_pizza(stats_dict, team_side):
    """Gera um gráfico PyPizza (circular radar) para o jogador."""
    params = [
        "Aproveit. Passes %",
        "Gols",
        "Finaliz. Alvo",
        "Duelos Ganhos %",
        "Desarmes Certos",
        "Recuperacoes"
    ]
    
    total_p = stats_dict.get('total_pass', 0)
    acc_p = stats_dict.get('accurate_pass', 0)
    pass_pct = round((acc_p / total_p * 100), 1) if total_p > 0 else 70.0
    
    g_won = stats_dict.get('duel_won', 0)
    g_lost = stats_dict.get('duel_lost', 0)
    duel_total = g_won + g_lost
    duel_pct = round((g_won / duel_total * 100), 1) if duel_total > 0 else 50.0
    
    goals = stats_dict.get('goals', 0)
    shots_on_target = stats_dict.get('on_target_scoring_attempt', 0)
    tackles = stats_dict.get('won_tackle', 0)
    recoveries = stats_dict.get('ball_recovery', 0)
    
    values = [
        int(pass_pct),
        int(min(100, goals * 25)),
        int(min(100, shots_on_target * 20)),
        int(duel_pct),
        int(min(100, tackles * 20)),
        int(min(100, recoveries * 10))
    ]
    
    color = '#10b981' if team_side == 'home' else '#ef4444'
    
    baker = PyPizza(
        params=params,
        background_color="#000000",
        straight_line_color="#1f2937",
        last_circle_color="#374151",
        other_circle_color="#1f2937",
        inner_circle_size=5,
        straight_line_lw=1,
        last_circle_lw=1,
        other_circle_lw=1
    )
    
    fig, ax = baker.make_pizza(
        values,
        figsize=(6, 6),
        param_location=110,
        slice_colors=[color] * len(params),
        value_colors=["#ffffff"] * len(params),
        value_bck_colors=[color] * len(params),
        kwargs_params=dict(color="#94a3b8", fontsize=10)
    )
    
    fig.set_facecolor('#000000')
    return get_base64_image(fig)

def plot_comparison_pizza(stats_a, stats_b, team_side):
    """Gera um gráfico PyPizza de comparação de percentis (Player Percentile Rank Viz)."""
    params = [
        "Aproveit. Passes %",
        "Gols",
        "Finaliz. Alvo",
        "Duelos Ganhos %",
        "Desarmes Certos",
        "Recuperacoes"
    ]
    
    def get_pizza_values(stats):
        if not stats:
            return [0] * len(params)
        stats_dict = dict(stats)
        total_p = stats_dict.get('total_pass', 0)
        acc_p = stats_dict.get('accurate_pass', 0)
        pass_pct = round((acc_p / total_p * 100), 1) if total_p > 0 else 70.0
        
        g_won = stats_dict.get('duel_won', 0)
        g_lost = stats_dict.get('duel_lost', 0)
        duel_total = g_won + g_lost
        duel_pct = round((g_won / duel_total * 100), 1) if duel_total > 0 else 50.0
        
        goals = stats_dict.get('goals', 0)
        shots_on_target = stats_dict.get('on_target_scoring_attempt', 0)
        tackles = stats_dict.get('won_tackle', 0)
        recoveries = stats_dict.get('ball_recovery', 0)
        
        return [
            int(pass_pct),
            int(min(100, goals * 25)),
            int(min(100, shots_on_target * 20)),
            int(duel_pct),
            int(min(100, tackles * 20)),
            int(min(100, recoveries * 10))
        ]

    values_a = get_pizza_values(stats_a)
    
    # Cores fixas para a comparação
    color_a = '#10b981' # Verde para o Jogador A
    color_b = '#ef4444' # Vermelho para o Jogador B
    
    baker = PyPizza(
        params=params,
        background_color="#000000",
        straight_line_color="#1f2937",
        last_circle_color="#374151",
        other_circle_color="#1f2937",
        inner_circle_size=5,
        straight_line_lw=1,
        last_circle_lw=1,
        other_circle_lw=1
    )
    
    if stats_b:
        values_b = get_pizza_values(stats_b)
        # Plot de comparação
        fig, ax = baker.make_pizza(
            values_a,
            compare_values=values_b,
            figsize=(6.5, 6.5),
            param_location=110,
            slice_colors=[color_a] * len(params),
            compare_slice_colors=[color_b] * len(params),
            value_colors=["#ffffff"] * len(params),
            compare_value_colors=["#ffffff"] * len(params),
            value_bck_colors=[color_a] * len(params),
            compare_value_bck_colors=[color_b] * len(params),
            kwargs_params=dict(color="#94a3b8", fontsize=10)
        )
    else:
        # Plot simples se não houver o segundo jogador
        color = color_a if team_side == 'home' else color_b
        fig, ax = baker.make_pizza(
            values_a,
            figsize=(6.5, 6.5),
            param_location=110,
            slice_colors=[color] * len(params),
            value_colors=["#ffffff"] * len(params),
            value_bck_colors=[color] * len(params),
            kwargs_params=dict(color="#94a3b8", fontsize=10)
        )
        
    fig.set_facecolor('#000000')
    return get_base64_image(fig)

def plot_action_map(events, title):
    if not events:
        return None

    pitch = Pitch(pitch_type='opta', pitch_color='#000000', line_color='#2c3e50')
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#000000')

    for e in events:
        coords = e.get('playerCoordinates', {})
        if not coords:
            continue
        x = coords.get('x', 0)
        y = coords.get('y', 0)
        pitch.scatter(x, y, s=150, color='#9B59B6', edgecolors='white', ax=ax)

    return get_base64_image(fig)
