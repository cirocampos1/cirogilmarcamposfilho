import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import io
import base64

def get_base64_image(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', transparent=True)
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

def get_pitch():
    return Pitch(
        pitch_type='opta',
        pitch_color='#22312b',
        line_color='#c7d5cc',
        linewidth=1.5
    )

def plot_heatmap(heatmap_data):
    if not heatmap_data:
        return None

    pitch = get_pitch()
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#22312b')
    
    # Extrai coordenadas
    x = [pt.get('x', pt.get('playerCoordinates', {}).get('x')) for pt in heatmap_data]
    y = [pt.get('y', pt.get('playerCoordinates', {}).get('y')) for pt in heatmap_data]
    x = [val for val in x if val is not None]
    y = [val for val in y if val is not None]

    if not x or not y:
        return get_base64_image(fig)

    pitch.kdeplot(
        x, y, 
        ax=ax, 
        fill=True, 
        levels=100, 
        cmap='magma', 
        alpha=0.7
    )
    
    return get_base64_image(fig)

def plot_shotmap(shots):
    if not shots:
        return None

    pitch = get_pitch()
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#22312b')
    
    for s in shots:
        coords = s.get('playerCoordinates', {})
        if not coords:
            continue
            
        is_goal = s.get('shotType') == 'goal'
        color = '#2ECC71' if is_goal else '#F1C40F'
        
        pitch.scatter(coords['x'], coords['y'], 
                     s=200, color=color, edgecolors='white', 
                     ax=ax, alpha=0.9, zorder=3)
                     
    return get_base64_image(fig)

def plot_passmap(passes):
    if not passes:
        return None

    pitch = get_pitch()
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#22312b')
    
    for p in passes:
        coords = p.get('playerCoordinates', {})
        end_coords = p.get('passEndCoordinates', {})
        
        if not coords or not end_coords:
            continue
            
        outcome = p.get('outcome', True)
        color = '#1A78CF' if outcome else '#F64B4B'
        
        pitch.arrows(coords['x'], coords['y'], 
                    end_coords['x'], end_coords['y'], 
                    width=2, headwidth=5, 
                    color=color, ax=ax, alpha=0.9)
                    
    return get_base64_image(fig)

def plot_team_shotmap(shots):
    if not shots:
        return None

    pitch = get_pitch()
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#22312b')

    for s in shots:
        coords = s.get("playerCoordinates", {})
        if not coords:
            x = s.get("x")
            y = s.get("y")
            if x is None:
                continue
        else:
            x = coords.get("x")
            y = coords.get("y")

        shot_type = s.get("shotType", "shot")
        is_home = s.get("isHome", True)

        if shot_type == "goal":
            color = '#2ECC71'
            size = 250
            marker = '*'
        elif shot_type in ("shotOnTarget", "onTarget"):
            color = '#3498DB' if is_home else '#E74C3C'
            size = 180
            marker = 'o'
        elif shot_type == "blocked":
            color = '#95A5A6'
            size = 140
            marker = 's'
        else:
            color = '#F1C40F' if is_home else '#E67E22'
            size = 140
            marker = '^'

        pitch.scatter(x, y, s=size, color=color, edgecolors='white',
                      linewidth=0.5, marker=marker, ax=ax, alpha=0.85, zorder=3)

    return get_base64_image(fig)


def plot_action_map(events, title):
    if not events:
        return None

    pitch = Pitch(pitch_type='opta', pitch_color='#1a1f24', line_color='#ffffff')
    fig, ax = pitch.draw(figsize=(10, 7))

    for e in events:
        coords = e.get('playerCoordinates', {})
        if not coords:
            continue
        x = coords.get('x', 0)
        y = coords.get('y', 0)
        pitch.scatter(x, y, s=150, color='#9B59B6', edgecolors='white', ax=ax)

    return get_base64_image(fig)
