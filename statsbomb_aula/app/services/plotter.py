import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import seaborn as sns

def get_base64_image(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', transparent=True)
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

def get_pitch():
    # Statsbomb data coordinates: x = [0, 120], y = [0, 80]
    return Pitch(
        pitch_type='statsbomb',
        pitch_color='#22312b',
        line_color='#c7d5cc',
        linewidth=1.5
    )

def plot_shotmap(shots):
    if not shots:
        return None

    pitch = get_pitch()
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#22312b')
    
    for s in shots:
        loc = s.get('location')
        if not loc or len(loc) < 2:
            continue
            
        x, y = loc[0], loc[1]
        
        shot_outcome = s.get('shot', {}).get('outcome', {}).get('name')
        is_goal = shot_outcome == 'Goal'
        color = '#2ECC71' if is_goal else '#F1C40F'
        
        # We can also scale marker size by xG if it exists
        xg = s.get('shot', {}).get('statsbomb_xg', 0.1)
        marker_size = max(50, xg * 1000)
        
        pitch.scatter(x, y, 
                     s=marker_size, color=color, edgecolors='white', 
                     ax=ax, alpha=0.8, zorder=3)
                     
    return get_base64_image(fig)

def plot_jointgrid_shotmap(shots, lineups):
    if not shots:
        return None

    teams = list(lineups.keys())
    if len(teams) < 2:
        return plot_shotmap(shots)

    home_team = teams[0]
    away_team = teams[1]

    pitch = get_pitch()
    fig, axs = pitch.jointgrid(figheight=8, left=None, bottom=None, grid_height=0.85, axis=False, title_height=0)
    fig.set_facecolor('#22312b')
    for key in ['top', 'left', 'right', 'endnote', 'pitch']:
        if key in axs:
            axs[key].set_facecolor('#22312b')

    home_x, home_y = [], []
    away_x, away_y = [], []

    for s in shots:
        loc = s.get('location')
        if not loc or len(loc) < 2: continue
        
        team_raw = s.get('possession_team') or s.get('team')
        team_name = team_raw.get('name') if isinstance(team_raw, dict) else team_raw
        if team_name == home_team:
            home_x.append(loc[0])
            home_y.append(loc[1])
        else:
            # Flip coordinates to attack opposite side
            away_x.append(120 - loc[0])
            away_y.append(80 - loc[1])

    home_color = '#1A78CF'
    away_color = '#F1C40F'

    # Marginals
    if home_x:
        if 'top' in axs: sns.kdeplot(x=home_x, color=home_color, fill=True, ax=axs['top'])
        if 'left' in axs: sns.kdeplot(y=home_y, color=home_color, fill=True, ax=axs['left'])
        elif 'right' in axs: sns.kdeplot(y=home_y, color=home_color, fill=True, ax=axs['right'])
    if away_x:
        if 'top' in axs: sns.kdeplot(x=away_x, color=away_color, fill=True, ax=axs['top'])
        if 'left' in axs: sns.kdeplot(y=away_y, color=away_color, fill=True, ax=axs['left'])
        elif 'right' in axs: sns.kdeplot(y=away_y, color=away_color, fill=True, ax=axs['right'])

    # Pitch scatter
    if home_x:
        pitch.scatter(home_x, home_y, s=100, color=home_color, edgecolors='white', alpha=0.8, ax=axs['pitch'], label=home_team)
    if away_x:
        pitch.scatter(away_x, away_y, s=100, color=away_color, edgecolors='white', alpha=0.8, ax=axs['pitch'], label=away_team)

    axs['pitch'].legend(loc='lower center', ncol=2, frameon=False, labelcolor='white')

    for ax_key in ['top', 'left', 'right', 'bottom']:
        if ax_key in axs:
            ax_m = axs[ax_key]
            ax_m.spines['top'].set_visible(False)
            ax_m.spines['right'].set_visible(False)
            ax_m.spines['bottom'].set_visible(False)
            ax_m.spines['left'].set_visible(False)
            ax_m.set_xticks([])
            ax_m.set_yticks([])
            ax_m.set_xlabel('')
            ax_m.set_ylabel('')

    return get_base64_image(fig)

def plot_pass_network(passes, lineups):
    if not passes:
        return None

    teams = list(lineups.keys())
    if not teams:
        return None
        
    # Pick the home team to build the pass network for, usually it's the first team in lineups
    home_team = teams[0]
    
    # Filter for home_team passes
    team_passes = []
    for p in passes:
        team_raw = p.get('possession_team') or p.get('team')
        team_name = team_raw.get('name') if isinstance(team_raw, dict) else team_raw
        if team_name == home_team:
            team_passes.append(p)
            
    # player averages
    player_locs = {}
    pass_counts = {}
    
    # pair counts
    pair_counts = {}
    
    for p in team_passes:
        # Check outcome
        if p.get('pass_outcome'): continue # incomplete
        
        player = p.get('player')
        player_name = player.get('name') if isinstance(player, dict) else player
        if not player_name: continue
        
        loc = p.get('location')
        if not loc or len(loc) < 2: continue
        
        recipient = p.get('pass_recipient')
        recipient_name = recipient.get('name') if isinstance(recipient, dict) else recipient
        if not recipient_name: continue
        
        if player_name not in player_locs:
            player_locs[player_name] = [0, 0]
            pass_counts[player_name] = 0
            
        player_locs[player_name][0] += loc[0]
        player_locs[player_name][1] += loc[1]
        pass_counts[player_name] += 1
        
        pair = tuple(sorted([player_name, recipient_name]))
        pair_counts[pair] = pair_counts.get(pair, 0) + 1
        
    for p_name in player_locs:
        if pass_counts[p_name] > 0:
            player_locs[p_name][0] /= pass_counts[p_name]
            player_locs[p_name][1] /= pass_counts[p_name]
        
    pitch = get_pitch()
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#22312b')
    
    # draw edges
    for (p1, p2), count in pair_counts.items():
        if p1 not in player_locs or p2 not in player_locs: continue
        if count < 3: continue # only plot connections with at least 3 passes
        
        x1, y1 = player_locs[p1]
        x2, y2 = player_locs[p2]
        
        # alpha based on count
        alpha = min(count / 15, 0.8)
        lw = min(count / 3, 5)
        
        pitch.lines(x1, y1, x2, y2, lw=lw, color='#c7d5cc', alpha=alpha, zorder=1, ax=ax)
        
    # draw nodes
    for p_name, loc in player_locs.items():
        size = pass_counts[p_name] * 20
        pitch.scatter(loc[0], loc[1], s=size, color='#1A78CF', edgecolors='white', zorder=2, ax=ax)
        
        # labels
        name_parts = p_name.split()
        short_name = name_parts[-1] if len(name_parts) > 1 else name_parts[0]
        ax.text(loc[0], loc[1] + 2, short_name, color='white', fontsize=9, ha='center', zorder=3)
        
    ax.set_title(f"Rede de Passes: {home_team}", color='white', fontsize=14)
    return get_base64_image(fig)

def plot_xg_flow(xg_data, home_team, away_team):
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.set_facecolor('#22312b')
    ax.set_facecolor('#22312b')
    
    home_minutes = xg_data["home"]["minutes"]
    home_xg = xg_data["home"]["xg"]
    
    away_minutes = xg_data["away"]["minutes"]
    away_xg = xg_data["away"]["xg"]
    
    ax.step(home_minutes, home_xg, where='post', color='#1A78CF', linewidth=3, label=home_team)
    ax.step(away_minutes, away_xg, where='post', color='#F1C40F', linewidth=3, label=away_team)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(colors='white')
    ax.set_xlabel('Minuto', color='white', fontsize=12)
    ax.set_ylabel('Gols Esperados (xG)', color='white', fontsize=12)
    ax.set_title('Fluxo de xG', color='white', fontsize=14)
    ax.legend(frameon=False, labelcolor='white')
    ax.grid(axis='y', color='gray', alpha=0.3, linestyle='--')
    
    return get_base64_image(fig)

def plot_pressure_heatmap(pressures, home_team, away_team):
    pitch = get_pitch()
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#22312b')
    ax.set_facecolor('#22312b')
    
    home_x, home_y = [], []
    away_x, away_y = [], []
    
    for p in pressures:
        loc = p.get('location')
        if not loc or len(loc) < 2: continue
        
        team_raw = p.get('possession_team') or p.get('team')
        team_name = team_raw.get('name') if isinstance(team_raw, dict) else team_raw
        
        if team_name == home_team:
            home_x.append(loc[0])
            home_y.append(loc[1])
        elif team_name == away_team:
            away_x.append(120 - loc[0])
            away_y.append(80 - loc[1])
            
    if home_x:
        sns.kdeplot(x=home_x, y=home_y, fill=True, cmap="Blues", alpha=0.5, ax=ax, bw_adjust=0.5)
    if away_x:
        sns.kdeplot(x=away_x, y=away_y, fill=True, cmap="YlOrBr", alpha=0.5, ax=ax, bw_adjust=0.5)
        
    ax.set_title('Mapa de Pressão', color='white', fontsize=14)
    return get_base64_image(fig)
