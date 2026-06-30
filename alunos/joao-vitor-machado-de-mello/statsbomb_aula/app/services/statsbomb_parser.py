import os
import json
import math
from collections import Counter
from functools import lru_cache

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
TOURNAMENT_REFERENCE_FILE = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "tournament_macroposition_reference.json",
)

DEFENSIVE_EVENT_TYPES = {"Pressure", "Duel", "Interception", "Block", "Ball Recovery"}
SHOT_ON_TARGET_OUTCOMES = {"Goal", "Saved", "Saved to Post"}
SUCCESSFUL_TACKLE_OUTCOMES = {"Success In Play", "Success Out", "Won"}
GOALKEEPER_SAVE_TYPES = {"Shot Saved", "Shot Saved to Post"}

POSITION_PROFILES = {
    "Goleiro": {
        "keys": ["goalkeeper_saves", "goalkeeper_claims", "completed_passes", "ball_recoveries", "defensive_actions", "pressures"],
        "labels": {
            "goalkeeper_saves": "Defesas",
            "goalkeeper_claims": "Bolas dominadas",
            "completed_passes": "Passes certos",
            "ball_recoveries": "Recuperações",
            "defensive_actions": "Ações defensivas",
            "pressures": "Pressões",
        },
    },
    "Defensor": {
        "keys": ["successful_tackles", "interceptions", "clearances", "blocks", "ball_recoveries", "completed_passes"],
        "labels": {
            "successful_tackles": "Desarmes certos",
            "interceptions": "Interceptações",
            "clearances": "Cortes",
            "blocks": "Bloqueios",
            "ball_recoveries": "Recuperações",
            "completed_passes": "Passes certos",
        },
    },
    "Meio-campista": {
        "keys": ["completed_passes", "progressive_passes", "progressive_carries", "ball_recoveries", "pressures", "xa"],
        "labels": {
            "completed_passes": "Passes certos",
            "progressive_passes": "Passes progressivos",
            "progressive_carries": "Conduções progressivas",
            "ball_recoveries": "Recuperações",
            "pressures": "Pressões",
            "xa": "Assistências esperadas (xA)",
        },
    },
    "Atacante": {
        "keys": ["xg", "xa", "shots_on_target", "successful_dribbles", "progressive_carries", "pressures"],
        "labels": {
            "xg": "Gols esperados (xG)",
            "xa": "Assistências esperadas (xA)",
            "shots_on_target": "Chutes certos",
            "successful_dribbles": "Dribles certos",
            "progressive_carries": "Conduções progressivas",
            "pressures": "Pressões",
        },
    },
}

GENERAL_RADAR_LABELS = {
    "attack": "Ataque",
    "creation": "Criação",
    "progression": "Progressão",
    "passing": "Passe",
    "defense": "Defesa",
    "pressure": "Pressão",
}

MACRO_POSITIONS = (
    "Goleiro",
    "Zagueiro",
    "Lateral/Ala",
    "Volante/Meio-campista",
    "Meia ofensivo/Ponta",
    "Centroavante",
)

LINE_DIMENSION_LABELS = {
    "attack": "Ataque",
    "creation": "Criação",
    "progression": "Progressão",
    "passing": "Passe",
    "defense": "Defesa",
    "pressure": "Pressão",
}

GOALKEEPER_DIMENSION_LABELS = {
    "goal_defense": "Defesa do gol",
    "footwork": "Jogo com os pés",
    "long_balls": "Bolas longas",
    "sweeper": "Ações fora da área",
    "pressure_received": "Pressão recebida",
    "build_up": "Participação na construção",
}

BASE_LINE_DIMENSIONS = {
    "attack": {"xg": 0.55, "shots_on_target": 0.25, "successful_dribbles": 0.20},
    "creation": {"xa": 0.70, "progressive_passes": 0.30},
    "progression": {
        "progressive_passes": 0.45,
        "progressive_carries": 0.35,
        "total_progression_distance": 0.20,
    },
    "passing": {
        "completed_passes": 0.50,
        "completed_passes_under_pressure": 0.25,
        "completed_long_passes": 0.25,
    },
    "defense": {
        "successful_tackles": 0.20,
        "interceptions": 0.18,
        "clearances": 0.12,
        "blocks": 0.12,
        "ball_recoveries": 0.20,
        "defensive_actions": 0.18,
    },
    "pressure": {"pressures": 0.75, "defensive_actions": 0.25},
}

GOALKEEPER_DIMENSIONS = {
    "goal_defense": {"goalkeeper_saves": 0.65, "goalkeeper_claims": 0.35},
    "footwork": {
        "completed_passes": 0.60,
        "completed_passes_under_pressure": 0.40,
    },
    "long_balls": {"completed_long_passes": 0.70, "long_passes": 0.30},
    "sweeper": {"goalkeeper_actions_outside_box": 0.70, "defensive_actions": 0.30},
    "pressure_received": {
        "passes_under_pressure": 0.55,
        "completed_passes_under_pressure": 0.45,
    },
    "build_up": {"passes": 0.35, "completed_passes": 0.45, "ball_recoveries": 0.20},
}

INFLUENCE_WEIGHTS = {
    "Zagueiro": {"attack": 0.03, "creation": 0.05, "progression": 0.17, "passing": 0.25, "defense": 0.35, "pressure": 0.15},
    "Lateral/Ala": {"attack": 0.10, "creation": 0.13, "progression": 0.22, "passing": 0.18, "defense": 0.20, "pressure": 0.17},
    "Volante/Meio-campista": {"attack": 0.05, "creation": 0.12, "progression": 0.23, "passing": 0.22, "defense": 0.20, "pressure": 0.18},
    "Meia ofensivo/Ponta": {"attack": 0.22, "creation": 0.24, "progression": 0.20, "passing": 0.12, "defense": 0.05, "pressure": 0.17},
    "Centroavante": {"attack": 0.38, "creation": 0.22, "progression": 0.14, "passing": 0.08, "defense": 0.03, "pressure": 0.15},
    "Goleiro": {"goal_defense": 0.35, "footwork": 0.18, "long_balls": 0.12, "sweeper": 0.12, "pressure_received": 0.08, "build_up": 0.15},
}

PLAYER_PER90_KEYS = {
    "goals",
    "xg",
    "xa",
    "shots",
    "shots_on_target",
    "completed_passes",
    "progressive_passes",
    "progressive_carries",
    "progressive_pass_distance",
    "progressive_carry_distance",
    "successful_dribbles",
    "dribbles",
    "successful_tackles",
    "pressures",
    "defensive_actions",
    "interceptions",
    "clearances",
    "blocks",
    "ball_recoveries",
    "goalkeeper_saves",
    "goalkeeper_claims",
    "passes",
    "long_passes",
    "completed_long_passes",
    "passes_under_pressure",
    "completed_passes_under_pressure",
    "goalkeeper_actions_outside_box",
    "passes_into_final_third",
    "passes_into_box",
    "crosses",
    "completed_crosses",
    "shot_assists",
    "cutbacks",
    "through_balls",
    "counterpressures",
    "pressures_final_third",
    "tackles",
    "duels",
    "duels_won",
    "aerial_duels",
    "aerial_duels_won",
    "fouls_committed",
    "fouls_won",
    "cards",
    "offensive_recoveries",
    "goalkeeper_shots_faced",
    "goalkeeper_goals_conceded",
    "goalkeeper_xg_faced",
    "goalkeeper_actions",
}
TOURNAMENT_REFERENCE_MINUTES = 90

EFFICIENCY_METRICS = {
    "pass_accuracy": ("completed_passes", "passes"),
    "passes_under_pressure_accuracy": (
        "completed_passes_under_pressure",
        "passes_under_pressure",
    ),
    "long_pass_accuracy": ("completed_long_passes", "long_passes"),
    "cross_accuracy": ("completed_crosses", "crosses"),
    "dribble_accuracy": ("successful_dribbles", "dribbles"),
    "tackle_accuracy": ("successful_tackles", "tackles"),
    "duel_accuracy": ("duels_won", "duels"),
    "aerial_duel_accuracy": ("aerial_duels_won", "aerial_duels"),
    "shot_conversion": ("goals", "shots"),
    "shots_on_target_conversion": ("goals", "shots_on_target"),
    "counterpress_percentage": ("counterpressures", "pressures"),
}

COMPARISON_CATEGORY_METRICS = {
    "Passe": (
        "passes", "completed_passes", "pass_accuracy",
        "passes_under_pressure", "passes_under_pressure_accuracy",
        "long_passes", "long_pass_accuracy",
    ),
    "Progressão": (
        "progressive_passes", "progressive_carries",
        "total_progression_distance", "passes_into_final_third",
        "passes_into_box",
    ),
    "Criação": (
        "xa", "shot_assists", "cutbacks", "through_balls", "passes_into_box",
    ),
    "Finalização": (
        "xg", "shots", "shots_on_target", "xg_per_shot",
        "shot_conversion", "shots_on_target_conversion",
    ),
    "Pressão": (
        "pressures", "counterpressures", "counterpress_percentage",
        "pressures_final_third",
    ),
    "Defesa": (
        "ball_recoveries", "successful_tackles", "tackles",
        "tackle_accuracy", "interceptions", "blocks", "clearances",
        "duels_won", "duel_accuracy", "aerial_duels_won",
        "aerial_duel_accuracy",
    ),
    "Disciplina": ("fouls_committed", "fouls_won", "cards"),
}

TEAM_DISPLAY = {
    "Argentina": {"name": "Argentina", "flag": "🇦🇷"},
    "Australia": {"name": "Austrália", "flag": "🇦🇺"},
    "Belgium": {"name": "Bélgica", "flag": "🇧🇪"},
    "Brazil": {"name": "Brasil", "flag": "🇧🇷"},
    "Cameroon": {"name": "Camarões", "flag": "🇨🇲"},
    "Canada": {"name": "Canadá", "flag": "🇨🇦"},
    "Costa Rica": {"name": "Costa Rica", "flag": "🇨🇷"},
    "Croatia": {"name": "Croácia", "flag": "🇭🇷"},
    "Denmark": {"name": "Dinamarca", "flag": "🇩🇰"},
    "Ecuador": {"name": "Equador", "flag": "🇪🇨"},
    "England": {"name": "Inglaterra", "flag": "🏴"},
    "France": {"name": "França", "flag": "🇫🇷"},
    "Germany": {"name": "Alemanha", "flag": "🇩🇪"},
    "Ghana": {"name": "Gana", "flag": "🇬🇭"},
    "Iran": {"name": "Irã", "flag": "🇮🇷"},
    "Japan": {"name": "Japão", "flag": "🇯🇵"},
    "Mexico": {"name": "México", "flag": "🇲🇽"},
    "Morocco": {"name": "Marrocos", "flag": "🇲🇦"},
    "Netherlands": {"name": "Holanda", "flag": "🇳🇱"},
    "Poland": {"name": "Polônia", "flag": "🇵🇱"},
    "Portugal": {"name": "Portugal", "flag": "🇵🇹"},
    "Qatar": {"name": "Catar", "flag": "🇶🇦"},
    "Saudi Arabia": {"name": "Arábia Saudita", "flag": "🇸🇦"},
    "Senegal": {"name": "Senegal", "flag": "🇸🇳"},
    "Serbia": {"name": "Sérvia", "flag": "🇷🇸"},
    "South Korea": {"name": "Coreia do Sul", "flag": "🇰🇷"},
    "Spain": {"name": "Espanha", "flag": "🇪🇸"},
    "Switzerland": {"name": "Suíça", "flag": "🇨🇭"},
    "Tunisia": {"name": "Tunísia", "flag": "🇹🇳"},
    "United States": {"name": "Estados Unidos", "flag": "🇺🇸"},
    "Uruguay": {"name": "Uruguai", "flag": "🇺🇾"},
    "Wales": {"name": "País de Gales", "flag": "🏴"},
}

TEAM_FLAG_META = {
    "Argentina": {"code": "ARG", "colors": ["#74acdf", "#ffffff", "#74acdf"]},
    "Australia": {"code": "AUS", "colors": ["#012169", "#ffcd00", "#00843d"]},
    "Belgium": {"code": "BEL", "colors": ["#000000", "#ffd90c", "#ef3340"]},
    "Brazil": {"code": "BRA", "colors": ["#009b3a", "#ffdf00", "#002776"]},
    "Cameroon": {"code": "CMR", "colors": ["#007a5e", "#ce1126", "#fcd116"]},
    "Canada": {"code": "CAN", "colors": ["#ff0000", "#ffffff", "#ff0000"]},
    "Costa Rica": {"code": "CRC", "colors": ["#002b7f", "#ffffff", "#ce1126"]},
    "Croatia": {"code": "CRO", "colors": ["#ff0000", "#ffffff", "#171796"]},
    "Denmark": {"code": "DEN", "colors": ["#c60c30", "#ffffff", "#c60c30"]},
    "Ecuador": {"code": "ECU", "colors": ["#ffdd00", "#034ea2", "#ed1c24"]},
    "England": {"code": "ENG", "colors": ["#ffffff", "#ce1124", "#ffffff"]},
    "France": {"code": "FRA", "colors": ["#0055a4", "#ffffff", "#ef4135"]},
    "Germany": {"code": "GER", "colors": ["#000000", "#dd0000", "#ffce00"]},
    "Ghana": {"code": "GHA", "colors": ["#ce1126", "#fcd116", "#006b3f"]},
    "Iran": {"code": "IRN", "colors": ["#239f40", "#ffffff", "#da0000"]},
    "Japan": {"code": "JPN", "colors": ["#ffffff", "#bc002d", "#ffffff"]},
    "Mexico": {"code": "MEX", "colors": ["#006847", "#ffffff", "#ce1126"]},
    "Morocco": {"code": "MAR", "colors": ["#c1272d", "#006233", "#c1272d"]},
    "Netherlands": {"code": "NED", "colors": ["#ae1c28", "#ffffff", "#21468b"]},
    "Poland": {"code": "POL", "colors": ["#ffffff", "#dc143c"]},
    "Portugal": {"code": "POR", "colors": ["#006600", "#ff0000"]},
    "Qatar": {"code": "QAT", "colors": ["#ffffff", "#8a1538"]},
    "Saudi Arabia": {"code": "KSA", "colors": ["#006c35", "#ffffff", "#006c35"]},
    "Senegal": {"code": "SEN", "colors": ["#00853f", "#fdef42", "#e31b23"]},
    "Serbia": {"code": "SRB", "colors": ["#c6363c", "#0c4076", "#ffffff"]},
    "South Korea": {"code": "KOR", "colors": ["#ffffff", "#c60c30", "#003478"]},
    "Spain": {"code": "ESP", "colors": ["#aa151b", "#f1bf00", "#aa151b"]},
    "Switzerland": {"code": "SUI", "colors": ["#ff0000", "#ffffff", "#ff0000"]},
    "Tunisia": {"code": "TUN", "colors": ["#e70013", "#ffffff", "#e70013"]},
    "United States": {"code": "USA", "colors": ["#b22234", "#ffffff", "#3c3b6e"]},
    "Uruguay": {"code": "URU", "colors": ["#ffffff", "#0038a8", "#fcd116"]},
    "Wales": {"code": "WAL", "colors": ["#ffffff", "#d30731", "#00ad36"]},
}

TEAM_UI_PALETTE = {
    "Netherlands": {"primary": "#f36c21", "secondary": "#102a43"},
    "Japan": {"primary": "#001f5b", "secondary": "#ffffff"},
    "England": {"primary": "#ffffff", "secondary": "#ce1124"},
    "Iran": {"primary": "#ffffff", "secondary": "#da0000"},
    "Australia": {"primary": "#ffcd00", "secondary": "#00843d"},
    "Croatia": {"primary": "#ffffff", "secondary": "#ff0000"},
    "Germany": {"primary": "#ffffff", "secondary": "#000000"},
}

STAGE_LABELS = {
    "Group Stage": "Fase de Grupos",
    "Round of 16": "Oitavas de Final",
    "Quarter-finals": "Quartas de Final",
    "Semi-finals": "Semifinal",
    "3rd Place Final": "Disputa de 3º Lugar",
    "Final": "Final",
}

EVENT_LABELS = {
    "Goal": "Gol",
    "Saved": "Defendido",
    "Saved to Post": "Defendido na trave",
    "Off T": "Fora",
    "Blocked": "Bloqueado",
    "Post": "Na trave",
    "Wayward": "Muito fora",
    "Incomplete": "Incompleto",
    "Out": "Para fora",
    "Pass Offside": "Impedimento",
    "Unknown": "Desconhecido",
    "Complete": "Completo",
    "Success In Play": "Certo em jogo",
    "Success Out": "Certo para fora",
    "Won": "Ganho",
    "Lost Out": "Perdido para fora",
    "Lost In Play": "Perdido em jogo",
    "Left Foot": "Pé esquerdo",
    "Right Foot": "Pé direito",
    "Head": "Cabeça",
    "Other": "Outro",
}


def _as_float(value, default=0.0):
    if value is None:
        return default
    if isinstance(value, float) and math.isnan(value):
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _is_truthy(value):
    if value is None:
        return False
    if isinstance(value, float) and math.isnan(value):
        return False
    if isinstance(value, str):
        return value.lower() in {"true", "1", "yes"}
    return bool(value)


def _get_name(value):
    if isinstance(value, dict):
        return value.get("name")
    if isinstance(value, float) and math.isnan(value):
        return None
    return value


def _color_luminance(hex_color):
    color = hex_color.lstrip("#")
    if len(color) != 6:
        return 0
    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)
    return (0.299 * red + 0.587 * green + 0.114 * blue) / 255


def _hex_rgb(hex_color):
    color = (hex_color or "").lstrip("#")
    if len(color) != 6:
        return (0, 0, 0)
    return tuple(int(color[index:index + 2], 16) for index in (0, 2, 4))


def _color_distance(first, second):
    first_rgb = _hex_rgb(first)
    second_rgb = _hex_rgb(second)
    return math.sqrt(
        sum((first_rgb[index] - second_rgb[index]) ** 2 for index in range(3))
    )


def _accent_colors(colors, distinct_threshold=70):
    usable = [color for color in colors if _color_luminance(color) < 0.86]
    if not usable:
        usable = colors
    primary = usable[0]
    secondary = next(
        (
            color for color in colors
            if color.lower() != primary.lower()
            and _color_distance(primary, color) >= distinct_threshold
        ),
        "#ffffff",
    )
    return primary, secondary


def resolve_match_colors(home_display, away_display, threshold=105):
    distance = _color_distance(
        home_display["primary_color"],
        away_display["primary_color"],
    )
    away_color = away_display["primary_color"]
    if distance < threshold:
        away_color = away_display["secondary_color"]
    return {
        "home": home_display["primary_color"],
        "away": away_color,
        "used_secondary_away": away_color != away_display["primary_color"],
    }


def get_team_display(team_name):
    meta = TEAM_DISPLAY.get(team_name, {})
    flag_meta = TEAM_FLAG_META.get(team_name, {"code": (team_name or "TBD")[:3].upper(), "colors": ["#f7f4ee", "#a7b0ba"]})
    colors = flag_meta["colors"]
    palette = TEAM_UI_PALETTE.get(team_name)
    if palette:
        primary_color = palette["primary"]
        secondary_color = palette["secondary"]
    else:
        primary_color, secondary_color = _accent_colors(colors)
    step = 100 / len(colors)
    stops = []
    for index, color in enumerate(colors):
        stops.append(f"{color} {index * step:.1f}% {(index + 1) * step:.1f}%")
    return {
        "raw_name": team_name,
        "name": meta.get("name", team_name),
        "flag": meta.get("flag", "🏳"),
        "flag_code": flag_meta["code"],
        "flag_style": f"linear-gradient(90deg, {', '.join(stops)})",
        "flag_url": f"/static/flags/{flag_meta['code'].lower()}.svg",
        "primary_color": primary_color,
        "secondary_color": secondary_color,
    }


def format_match_date(date_value):
    if not date_value or not isinstance(date_value, str):
        return ""
    parts = date_value.split("-")
    if len(parts) != 3:
        return date_value
    year, month, day = parts
    return f"{day}/{month}/{year}"


def _get_team_key(team_name, home_team, away_team):
    if team_name == home_team:
        return "home"
    if team_name == away_team:
        return "away"
    return None


def _opponent_key(team_key):
    return "away" if team_key == "home" else "home"


def _valid_location(value):
    return isinstance(value, list) and len(value) >= 2


def _in_pitch(value):
    return _valid_location(value) and 0 <= _as_float(value[0]) <= 120 and 0 <= _as_float(value[1]) <= 80


def _minute_label(event):
    minute = int(_as_float(event.get("minute"), 0))
    second = int(_as_float(event.get("second"), 0))
    return f"{minute}:{second:02d}"


def _goal_minute_label(event):
    minute = int(_as_float(event.get("minute"), 0))
    period = int(_as_float(event.get("period"), 0))
    if period == 1 and minute > 45:
        return f"45+{minute - 45}'"
    if period == 2 and minute > 90:
        return f"90+{minute - 90}'"
    return f"{minute}'"


def _team_side(event, home_team, away_team):
    team_name = _get_name(event.get("team")) or _get_name(event.get("possession_team"))
    side = _get_team_key(team_name, home_team, away_team)
    return team_name, side


def _label(value, default="-"):
    if not value:
        return default
    return EVENT_LABELS.get(value, value)


def translate_stage(stage):
    return STAGE_LABELS.get(stage, stage or "")


def exclude_penalty_shootout(events):
    return [event for event in events if int(_as_float(event.get("period"), 0)) != 5]


def _translate_position(position):
    if not position:
        return "Posição não informada"
    translations = {
        "Goalkeeper": "Goleiro",
        "Center Back": "Zagueiro",
        "Right Center Back": "Zagueiro direito",
        "Left Center Back": "Zagueiro esquerdo",
        "Right Back": "Lateral direito",
        "Left Back": "Lateral esquerdo",
        "Right Wing Back": "Ala direito",
        "Left Wing Back": "Ala esquerdo",
        "Center Defensive Midfield": "Volante",
        "Right Defensive Midfield": "Volante direito",
        "Left Defensive Midfield": "Volante esquerdo",
        "Center Midfield": "Meio-campista central",
        "Right Center Midfield": "Meio-campista direito",
        "Left Center Midfield": "Meio-campista esquerdo",
        "Center Attacking Midfield": "Meia ofensivo",
        "Right Attacking Midfield": "Meia ofensivo direito",
        "Left Attacking Midfield": "Meia ofensivo esquerdo",
        "Right Wing": "Ponta direita",
        "Left Wing": "Ponta esquerda",
        "Center Forward": "Centroavante",
        "Right Center Forward": "Atacante direito",
        "Left Center Forward": "Atacante esquerdo",
        "Secondary Striker": "Segundo atacante",
    }
    return translations.get(position, position)


def _position_group(position):
    position = position or ""
    if position == "Goalkeeper":
        return "Goleiro"
    if any(term in position for term in ("Back", "Wing Back")):
        return "Defensor"
    if any(term in position for term in ("Midfield", "Midfielder")):
        return "Meio-campista"
    if any(term in position for term in ("Wing", "Forward", "Striker")):
        return "Atacante"
    return "Meio-campista"


def macro_position_for(position):
    position = position or ""
    if position == "Goalkeeper":
        return "Goleiro"
    if "Center Back" in position or position == "Center Back":
        return "Zagueiro"
    if "Back" in position or "Wing Back" in position:
        return "Lateral/Ala"
    if "Defensive Midfield" in position or position in {
        "Center Midfield",
        "Right Center Midfield",
        "Left Center Midfield",
    }:
        return "Volante/Meio-campista"
    if "Attacking Midfield" in position or "Wing" in position:
        return "Meia ofensivo/Ponta"
    if "Forward" in position or "Striker" in position:
        return "Centroavante"
    return "Volante/Meio-campista"


def contextual_score(value, p05, p95):
    value = _as_float(value)
    p05 = _as_float(p05)
    p95 = _as_float(p95)
    if p95 <= p05:
        return 50
    return round(max(0.0, min(100.0, ((value - p05) / (p95 - p05)) * 100)))


def _percentile(values, percentile):
    ordered = sorted(_as_float(value) for value in values)
    if not ordered:
        return 0.0
    if len(ordered) == 1:
        return ordered[0]
    index = (len(ordered) - 1) * percentile
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return ordered[lower]
    weight = index - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def build_player_positions(events, lineups=None):
    observed = {}
    for event in exclude_penalty_shootout(events):
        player = _get_name(event.get("player"))
        position = _get_name(event.get("position"))
        if player and position:
            observed.setdefault(player, Counter())[position] += 1

    lineup_positions = {}
    if isinstance(lineups, dict):
        for players in lineups.values():
            for player in players or []:
                positions = player.get("positions") or []
                if positions:
                    lineup_positions[player.get("player_name")] = positions[0].get("position")

    names = set(observed) | {name for name in lineup_positions if name}
    output = {}
    for player in names:
        raw_position = observed[player].most_common(1)[0][0] if player in observed else lineup_positions.get(player)
        output[player] = {
            "position": _translate_position(raw_position),
            "position_raw": raw_position,
            "position_group": _position_group(raw_position),
            "macro_position": macro_position_for(raw_position),
        }
    return output


def _clock_to_seconds(value):
    if value is None:
        return None
    parts = str(value).split(":")
    if len(parts) != 2:
        return None
    try:
        return int(parts[0]) * 60 + int(parts[1])
    except (TypeError, ValueError):
        return None


def build_player_minutes(lineups, events=None):
    match_events = exclude_penalty_shootout(events or [])
    event_end_seconds = max(
        (
            int(_as_float(event.get("minute"), 0)) * 60
            + int(_as_float(event.get("second"), 0))
            for event in match_events
        ),
        default=90 * 60,
    )
    recorded_ends = []
    if isinstance(lineups, dict):
        for players in lineups.values():
            for player in players or []:
                for position in player.get("positions") or []:
                    end = _clock_to_seconds(position.get("to"))
                    if end is not None:
                        recorded_ends.append(end)
    match_end_seconds = max([event_end_seconds, *recorded_ends, 90 * 60])

    minutes = {}
    if not isinstance(lineups, dict):
        return minutes
    for players in lineups.values():
        for player in players or []:
            player_name = player.get("player_name")
            if not player_name:
                continue
            seconds_played = 0
            for position in player.get("positions") or []:
                start = _clock_to_seconds(position.get("from"))
                end = _clock_to_seconds(position.get("to"))
                start = 0 if start is None else start
                end = match_end_seconds if end is None else end
                seconds_played += max(0, end - start)
            minutes[player_name] = round(seconds_played / 60, 2)
    return minutes


def build_penalty_events(events, home_team, away_team):
    attempts = []
    shootout_counts = {"home": 0, "away": 0}
    for event in events:
        period = int(_as_float(event.get("period"), 0))
        is_shootout = period == 5
        if (
            event.get("type") != "Shot"
            or (event.get("shot_type") != "Penalty" and not is_shootout)
        ):
            continue
        team_name, side = _team_side(event, home_team, away_team)
        if not side:
            continue
        outcome = event.get("shot_outcome")
        team_display = get_team_display(team_name)
        end_location = event.get("shot_end_location") or []
        shootout_counts[side] += int(is_shootout)
        attempt_number = shootout_counts[side] if is_shootout else None
        player = _get_name(event.get("player")) or "Jogador não informado"
        result = _label(outcome, "Sem resultado")
        minute_label = f"Cobrança {attempt_number}" if is_shootout else _goal_minute_label(event)
        attempts.append(
            {
                "id": event.get("id"),
                "player": player,
                "team": side,
                "team_name": team_display["name"],
                "flag_code": team_display["flag_code"],
                "flag_url": team_display["flag_url"],
                "period": period,
                "minute": int(_as_float(event.get("minute"), 0)),
                "minute_label": minute_label,
                "result": result,
                "outcome": outcome,
                "scored": outcome == "Goal",
                "shootout": is_shootout,
                "shot_type": "Penalty",
                "attempt_number": attempt_number,
                "end_y": round(_as_float(end_location[1], 40.0), 2) if len(end_location) >= 2 else 40.0,
                "end_z": round(_as_float(end_location[2], 0.0), 2) if len(end_location) >= 3 else 0.0,
                "body_part": _label(event.get("shot_body_part")),
                "tooltip": f"{player} | {team_display['name']} | {result} | {minute_label}",
            }
        )
    return attempts


def build_penalty_shootout(events, home_team, away_team):
    shootout_attempts = [
        attempt for attempt in build_penalty_events(events, home_team, away_team)
        if attempt["shootout"]
    ]
    attempts = {
        "home": [attempt for attempt in shootout_attempts if attempt["team"] == "home"],
        "away": [attempt for attempt in shootout_attempts if attempt["team"] == "away"],
    }
    return {
        "occurred": bool(attempts["home"] or attempts["away"]),
        "home_score": sum(attempt["scored"] for attempt in attempts["home"]),
        "away_score": sum(attempt["scored"] for attempt in attempts["away"]),
        "home_attempts": attempts["home"],
        "away_attempts": attempts["away"],
    }


def _is_completed_pass(event):
    return event.get("type") == "Pass" and not event.get("pass_outcome")


def _is_progressive_pass(event):
    if not _is_completed_pass(event):
        return False
    start = event.get("location")
    end = event.get("pass_end_location")
    if not _valid_location(start) or not _valid_location(end):
        return False
    gain = _as_float(end[0]) - _as_float(start[0])
    enters_final_third = _as_float(start[0]) < 80 <= _as_float(end[0])
    return gain >= 10 or enters_final_third


def _is_progressive_carry(event):
    if event.get("type") != "Carry":
        return False
    start = event.get("location")
    end = event.get("carry_end_location")
    if not _valid_location(start) or not _valid_location(end):
        return False
    gain = _as_float(end[0]) - _as_float(start[0])
    enters_final_third = _as_float(start[0]) < 80 <= _as_float(end[0])
    return gain >= 10 or enters_final_third


def safe_percentage(numerator, denominator):
    denominator = _as_float(denominator)
    if denominator <= 0:
        return None
    return round((_as_float(numerator) / denominator) * 100, 1)


def format_efficiency(numerator, denominator):
    percentage = safe_percentage(numerator, denominator)
    label = "N/D" if percentage is None else f"{percentage:g}%"
    return f"{label} ({int(_as_float(numerator))}/{int(_as_float(denominator))})"


def _enters_final_third(event):
    start = event.get("location")
    end = event.get("pass_end_location")
    return (
        _valid_location(start)
        and _valid_location(end)
        and _as_float(start[0]) < 80 <= _as_float(end[0])
    )


def _enters_box(event):
    end = event.get("pass_end_location")
    return (
        _valid_location(end)
        and _as_float(end[0]) >= 102
        and 18 <= _as_float(end[1]) <= 62
    )


def _empty_team_metrics():
    return {
        "xg": 0.0,
        "xa": 0.0,
        "goals": 0,
        "shots": 0,
        "shots_on_target": 0,
        "passes": 0,
        "completed_passes": 0,
        "successful_dribbles": 0,
        "dribbles": 0,
        "tackles": 0,
        "successful_tackles": 0,
        "corners": 0,
        "fouls_committed": 0,
        "passes_under_pressure_total": 0,
        "passes_under_pressure_completed": 0,
        "progressive_passes": 0,
        "progressive_carries": 0,
        "high_turnovers": 0,
        "counterpressures": 0,
        "pressure_events": 0,
        "pressures_final_third": 0,
        "offensive_recoveries": 0,
        "total_progression_distance": 0.0,
        "defensive_actions": 0,
        "opponent_zone_passes": 0,
        "ppda": None,
    }


def _empty_player_metrics(player_name, team_name, position=None, minutes=0):
    position = position or {
        "position": "Posição não informada",
        "position_raw": None,
        "position_group": "Meio-campista",
        "macro_position": "Volante/Meio-campista",
    }
    return {
        "player": player_name,
        "team": team_name,
        **position,
        "minutes": round(_as_float(minutes), 2),
        "xg": 0.0,
        "xa": 0.0,
        "goals": 0,
        "shots": 0,
        "shots_on_target": 0,
        "completed_passes": 0,
        "passes": 0,
        "long_passes": 0,
        "completed_long_passes": 0,
        "passes_under_pressure": 0,
        "completed_passes_under_pressure": 0,
        "progressive_passes": 0,
        "progressive_carries": 0,
        "progressive_pass_distance": 0.0,
        "progressive_carry_distance": 0.0,
        "successful_dribbles": 0,
        "dribbles": 0,
        "successful_tackles": 0,
        "pressures": 0,
        "defensive_actions": 0,
        "interceptions": 0,
        "clearances": 0,
        "blocks": 0,
        "ball_recoveries": 0,
        "goalkeeper_saves": 0,
        "goalkeeper_claims": 0,
        "goalkeeper_actions_outside_box": 0,
        "passes_into_final_third": 0,
        "passes_into_box": 0,
        "crosses": 0,
        "completed_crosses": 0,
        "shot_assists": 0,
        "cutbacks": 0,
        "through_balls": 0,
        "counterpressures": 0,
        "pressures_final_third": 0,
        "tackles": 0,
        "duels": 0,
        "duels_won": 0,
        "aerial_duels": 0,
        "aerial_duels_won": 0,
        "fouls_committed": 0,
        "fouls_won": 0,
        "cards": 0,
        "offensive_recoveries": 0,
        "goalkeeper_shots_faced": 0,
        "goalkeeper_goals_conceded": 0,
        "goalkeeper_xg_faced": 0.0,
        "goalkeeper_actions": 0,
        "impact_score": 0.0,
    }


def _profile_for_player(player):
    return POSITION_PROFILES.get(player.get("position_group"), POSITION_PROFILES["Meio-campista"])


def _dimension_definitions(macro_position):
    if macro_position == "Goleiro":
        return GOALKEEPER_DIMENSIONS
    dimensions = {
        name: dict(weights)
        for name, weights in BASE_LINE_DIMENSIONS.items()
    }
    if macro_position == "Zagueiro":
        dimensions["defense"] = {
            "successful_tackles": 0.15,
            "interceptions": 0.22,
            "clearances": 0.20,
            "blocks": 0.16,
            "ball_recoveries": 0.12,
            "defensive_actions": 0.15,
        }
        dimensions["passing"] = {
            "completed_passes": 0.55,
            "completed_long_passes": 0.30,
            "completed_passes_under_pressure": 0.15,
        }
    elif macro_position == "Lateral/Ala":
        dimensions["progression"] = {
            "progressive_passes": 0.35,
            "progressive_carries": 0.40,
            "total_progression_distance": 0.25,
        }
    elif macro_position == "Volante/Meio-campista":
        dimensions["passing"] = {
            "completed_passes": 0.45,
            "completed_passes_under_pressure": 0.35,
            "completed_long_passes": 0.20,
        }
    elif macro_position == "Meia ofensivo/Ponta":
        dimensions["creation"] = {"xa": 0.60, "progressive_passes": 0.40}
        dimensions["attack"] = {
            "xg": 0.40,
            "shots_on_target": 0.20,
            "successful_dribbles": 0.40,
        }
    elif macro_position == "Centroavante":
        dimensions["attack"] = {
            "xg": 0.65,
            "shots_on_target": 0.25,
            "successful_dribbles": 0.10,
        }
    return dimensions


def _weighted_score(scores, weights):
    total_weight = sum(weights.values())
    if total_weight <= 0:
        return 50.0
    return round(
        sum(_as_float(scores.get(key)) * weight for key, weight in weights.items())
        / total_weight,
        1,
    )


def _dimension_scores(metric_scores, macro_position):
    return {
        dimension: _weighted_score(metric_scores, weights)
        for dimension, weights in _dimension_definitions(macro_position).items()
    }


def _efficiency_payload(row):
    if row.get("macro_position") == "Goleiro":
        radar_keys = (
            "goalkeeper_save_percentage",
            "pass_accuracy",
            "long_pass_accuracy",
            "passes_under_pressure_accuracy",
            "goalkeeper_claim_percentage",
            "goalkeeper_sweeper_percentage",
        )
        volume_keys = {
            "goalkeeper_save_percentage": (
                "goalkeeper_saves",
                "goalkeeper_shots_faced",
            ),
            "goalkeeper_claim_percentage": (
                "goalkeeper_claims",
                "goalkeeper_actions",
            ),
            "goalkeeper_sweeper_percentage": (
                "goalkeeper_actions_outside_box",
                "goalkeeper_actions",
            ),
        }
    else:
        radar_keys = (
            "pass_accuracy",
            "passes_under_pressure_accuracy",
            "dribble_accuracy",
            "tackle_accuracy",
            "duel_accuracy",
            "aerial_duel_accuracy",
            "shot_conversion",
            "cross_accuracy",
        )
        volume_keys = {}
    radar = {}
    volumes = {}
    for key in radar_keys:
        numerator_key, denominator_key = volume_keys.get(
            key,
            EFFICIENCY_METRICS.get(key, (key, key)),
        )
        numerator = _as_float(row.get(numerator_key))
        denominator = _as_float(row.get(denominator_key))
        radar[key] = row.get(key) if row.get(key) is not None else 0
        volumes[key] = {
            "numerator": round(numerator, 2),
            "denominator": round(denominator, 2),
            "display": format_efficiency(numerator, denominator),
        }
    return radar, volumes


def _comparison_categories(row):
    categories = {}
    for category, keys in COMPARISON_CATEGORY_METRICS.items():
        categories[category] = []
        for key in keys:
            is_rate = key in EFFICIENCY_METRICS or key == "xg_per_shot"
            item = {
                "key": key,
                "raw_value": round(_as_float(row.get(key)), 2),
                "per90_value": (
                    None
                    if is_rate
                    else round(_as_float(row.get("per90", {}).get(key)), 2)
                ),
                "percentage_value": None,
                "volume_numerator": None,
                "volume_denominator": None,
                "display": None,
            }
            if key in EFFICIENCY_METRICS:
                numerator_key, denominator_key = EFFICIENCY_METRICS[key]
                numerator = _as_float(row.get(numerator_key))
                denominator = _as_float(row.get(denominator_key))
                item.update(
                    {
                        "percentage_value": safe_percentage(numerator, denominator),
                        "volume_numerator": round(numerator, 2),
                        "volume_denominator": round(denominator, 2),
                        "display": format_efficiency(numerator, denominator),
                    }
                )
            categories[category].append(item)
    return categories


def _local_macro_reference(rows):
    grouped = {}
    for row in rows:
        grouped.setdefault(row["macro_position"], []).append(row)
    reference = {}
    for macro_position, group_rows in grouped.items():
        metric_keys = set(PLAYER_PER90_KEYS) | {"total_progression_distance"}
        metrics = {}
        for key in metric_keys:
            values = [_as_float(row["per90"].get(key)) for row in group_rows]
            mean_value = sum(values) / len(values) if values else 0
            metrics[key] = {
                "p05": _percentile(values, 0.05),
                "p95": _percentile(values, 0.95),
                "mean_per90": mean_value,
            }
        mean_scores = {
            key: contextual_score(value["mean_per90"], value["p05"], value["p95"])
            for key, value in metrics.items()
        }
        reference[macro_position] = {
            "players": len(group_rows),
            "minutes": sum(_as_float(row["minutes"]) for row in group_rows),
            "metrics": metrics,
            "dimension_average_scores": _dimension_scores(mean_scores, macro_position),
        }
    return reference


def _prepare_player_rows(players, tournament_reference=None):
    rows = []
    for row in players.values():
        row["xg"] = round(row["xg"], 2)
        row["xa"] = round(row["xa"], 2)
        row["progressive_pass_distance"] = round(row["progressive_pass_distance"], 1)
        row["progressive_carry_distance"] = round(row["progressive_carry_distance"], 1)
        row["total_progression_distance"] = round(
            row["progressive_pass_distance"] + row["progressive_carry_distance"],
            1,
        )
        minutes = _as_float(row.get("minutes"))
        row["per90"] = {
            key: round((_as_float(row.get(key)) * 90 / minutes), 2) if minutes > 0 else 0
            for key in PLAYER_PER90_KEYS
        }
        row["per90"]["total_progression_distance"] = (
            round(row["total_progression_distance"] * 90 / minutes, 2) if minutes > 0 else 0
        )
        row["eligible_for_radar"] = minutes >= 30
        row["eligible_for_ranking"] = minutes >= 45
        row["low_minutes"] = minutes < 30
        rows.append(row)

    reference = tournament_reference or _local_macro_reference(rows)
    for row in rows:
        macro_position = row["macro_position"]
        macro_reference = reference.get(macro_position, {})
        metric_reference = macro_reference.get("metrics", {})
        metric_keys = set(PLAYER_PER90_KEYS) | {"total_progression_distance"}
        metric_layers = {}
        metric_scores = {}
        for key in metric_keys:
            ref = metric_reference.get(key, {})
            per90_value = _as_float(row["per90"].get(key))
            score = contextual_score(per90_value, ref.get("p05"), ref.get("p95"))
            metric_layers[key] = {
                "raw_value": round(_as_float(row.get(key)), 2),
                "per90_value": round(per90_value, 2),
                "percentage_value": None,
                "volume_denominator": None,
                "score_0_100": score,
                "position_average_per90": round(_as_float(ref.get("mean_per90")), 2),
                "position_average_score_0_100": contextual_score(
                    ref.get("mean_per90"),
                    ref.get("p05"),
                    ref.get("p95"),
                ),
                "difference_vs_position_average": round(
                    per90_value - _as_float(ref.get("mean_per90")),
                    2,
                ),
                "percentile_or_rank": score,
            }
            metric_scores[key] = score
        for key, (numerator_key, denominator_key) in EFFICIENCY_METRICS.items():
            numerator = _as_float(row.get(numerator_key))
            denominator = _as_float(row.get(denominator_key))
            percentage = safe_percentage(numerator, denominator)
            metric_layers[key] = {
                "raw_value": round(numerator, 2),
                "per90_value": None,
                "percentage_value": percentage,
                "volume_denominator": round(denominator, 2),
                "score_0_100": percentage if percentage is not None else 0,
                "position_average_per90": None,
                "position_average_score_0_100": None,
                "difference_vs_position_average": None,
                "percentile_or_rank": None,
            }
        dimension_scores = _dimension_scores(metric_scores, macro_position)
        dimension_average_scores = macro_reference.get("dimension_average_scores") or {
            key: 50 for key in dimension_scores
        }
        influence_weights = INFLUENCE_WEIGHTS[macro_position]
        player_weighted = _weighted_score(dimension_scores, influence_weights)
        average_weighted = _weighted_score(dimension_average_scores, influence_weights)
        influence_index = round(
            (player_weighted / average_weighted) * 100 if average_weighted > 0 else 100,
            1,
        )
        row["metric_layers"] = metric_layers
        row["dimension_scores"] = dimension_scores
        row["dimension_average_scores"] = dimension_average_scores
        row["radar"] = dimension_scores
        row["position_average_radar"] = dimension_average_scores
        row["radar_labels"] = (
            GOALKEEPER_DIMENSION_LABELS
            if macro_position == "Goleiro"
            else LINE_DIMENSION_LABELS
        )
        row["radar_metrics"] = dimension_scores
        row["radar_metrics_per90"] = dimension_scores
        row["influence_index"] = influence_index
        row["influence_delta_pct"] = round(influence_index - 100, 1)
        row["contextual_score"] = round(player_weighted, 1)
        row["impact_score"] = influence_index
        row["radar_reference_scope"] = "tournament_macroposition_p05_p95"
        row["radar_reference_players"] = macro_reference.get("players", 0)
        profile = _profile_for_player(row)
        row["display_metrics"] = {
            key: row.get(key, 0)
            for key in profile["keys"]
        }
        row["efficiency_radar"], row["efficiency_volumes"] = _efficiency_payload(row)
        row["comparison_categories"] = _comparison_categories(row)
    rows.sort(key=lambda item: item["influence_index"], reverse=True)
    return rows


def _build_player_radars(prepared_rows, limit_per_group=2):
    selected = []
    eligible_rows = [row for row in prepared_rows if row["eligible_for_radar"]]
    for group in MACRO_POSITIONS:
        selected.extend(
            [row for row in eligible_rows if row["macro_position"] == group][:limit_per_group]
        )
    selected_names = {row["player"] for row in selected}
    selected.extend(
        row for row in eligible_rows
        if row["player"] not in selected_names
    )
    selected = selected[:9]

    radars = []
    for row in selected:
        team_display = get_team_display(row["team"])
        radars.append(
            {
                "player": row["player"],
                "team": team_display["name"],
                "team_flag_url": team_display["flag_url"],
                "team_flag_code": team_display["flag_code"],
                "position": row["position"],
                "position_group": row["position_group"],
                "macro_position": row["macro_position"],
                "impact_score": row["impact_score"],
                "influence_index": row["influence_index"],
                "influence_delta_pct": row["influence_delta_pct"],
                "metrics": row["display_metrics"],
                "metrics_per90": row["radar_metrics_per90"],
                "metric_labels": row["radar_labels"],
                "radar": row["radar"],
                "position_average_radar": row["position_average_radar"],
                "radar_reference_scope": row["radar_reference_scope"],
                "radar_reference_players": row["radar_reference_players"],
                "minutes": row["minutes"],
                "per90": row["per90"],
                "metric_layers": row["metric_layers"],
                "dimension_scores": row["dimension_scores"],
                "dimension_average_scores": row["dimension_average_scores"],
                "eligible_for_radar": row["eligible_for_radar"],
            }
        )
    return radars


def _build_player_comparison(prepared_rows):
    rows = []
    for row in prepared_rows:
        passes = row.get("completed_passes", 0)
        team_display = get_team_display(row["team"])
        comparison_row = {
            "player": row["player"],
            "team": team_display["name"],
            "team_raw": row["team"],
            "team_flag_url": team_display["flag_url"],
            "team_flag_code": team_display["flag_code"],
            "position": row["position"],
            "position_group": row["position_group"],
            "macro_position": row["macro_position"],
            "xg": round(row["xg"], 2),
            "xa": round(row["xa"], 2),
            "shots": row["shots"],
            "shots_on_target": row["shots_on_target"],
            "completed_passes": passes,
            "progressive_passes": row["progressive_passes"],
            "progressive_carries": row["progressive_carries"],
            "progressive_pass_distance": row["progressive_pass_distance"],
            "progressive_carry_distance": row["progressive_carry_distance"],
            "total_progression_distance": row["total_progression_distance"],
            "successful_dribbles": row["successful_dribbles"],
            "successful_tackles": row["successful_tackles"],
            "pressures": row["pressures"],
            "defensive_actions": row["defensive_actions"],
            "interceptions": row["interceptions"],
            "clearances": row["clearances"],
            "blocks": row["blocks"],
            "ball_recoveries": row["ball_recoveries"],
            "goalkeeper_saves": row["goalkeeper_saves"],
            "goalkeeper_claims": row["goalkeeper_claims"],
            "passes": row["passes"],
            "long_passes": row["long_passes"],
            "completed_long_passes": row["completed_long_passes"],
            "passes_under_pressure": row["passes_under_pressure"],
            "completed_passes_under_pressure": row["completed_passes_under_pressure"],
            "goalkeeper_actions_outside_box": row["goalkeeper_actions_outside_box"],
            **{
                key: row.get(key)
                for key in (
                    "goals", "pass_accuracy", "passes_into_final_third",
                    "passes_into_box", "crosses", "completed_crosses",
                    "cross_accuracy", "shot_assists", "cutbacks",
                    "through_balls", "xg_per_shot", "shot_conversion",
                    "shots_on_target_conversion", "counterpressures",
                    "counterpress_percentage", "pressures_final_third",
                    "tackles", "tackle_accuracy", "duels", "duels_won",
                    "duel_accuracy", "aerial_duels", "aerial_duels_won",
                    "aerial_duel_accuracy", "fouls_committed", "fouls_won",
                    "cards", "offensive_recoveries", "dribbles",
                    "dribble_accuracy", "passes_under_pressure_accuracy",
                    "long_pass_accuracy", "goalkeeper_shots_faced",
                    "goalkeeper_goals_conceded", "goalkeeper_xg_faced",
                    "goalkeeper_goals_prevented", "goalkeeper_save_percentage",
                    "goalkeeper_actions",
                )
            },
            "impact_score": row["impact_score"],
            "influence_index": row["influence_index"],
            "influence_delta_pct": row["influence_delta_pct"],
            "contextual_score": row["contextual_score"],
            "minutes": row["minutes"],
            "eligible_for_radar": row["eligible_for_radar"],
            "eligible_for_ranking": row["eligible_for_ranking"],
            "low_minutes": row["low_minutes"],
            "per90": row["per90"],
            "radar": row["radar"],
            "position_average_radar": row["position_average_radar"],
            "radar_reference_scope": row["radar_reference_scope"],
            "radar_reference_players": row["radar_reference_players"],
            "radar_labels": row["radar_labels"],
            "radar_metrics": row["radar_metrics"],
            "radar_metrics_per90": row["radar_metrics_per90"],
            "metric_layers": row["metric_layers"],
            "dimension_scores": row["dimension_scores"],
            "dimension_average_scores": row["dimension_average_scores"],
            "efficiency_radar": row["efficiency_radar"],
            "efficiency_volumes": row["efficiency_volumes"],
            "comparison_categories": row["comparison_categories"],
        }
        comparison_row["total_progression"] = comparison_row["progressive_passes"] + comparison_row["progressive_carries"]
        rows.append(comparison_row)
    return rows


def _build_tactical_notes(metrics, home_team, away_team, player_radars):
    notes = []
    home = metrics["home"]
    away = metrics["away"]
    home_label = get_team_display(home_team)["name"]
    away_label = get_team_display(away_team)["name"]

    xa_gap = round(home["xa"] - away["xa"], 2)
    if abs(xa_gap) >= 0.15:
        leader = home_label if xa_gap > 0 else away_label
        leader_xa = home["xa"] if xa_gap > 0 else away["xa"]
        other_xa = away["xa"] if xa_gap > 0 else home["xa"]
        notes.append(
            f"{leader} criou mais: {leader_xa:.2f} xA contra {other_xa:.2f} "
            "em passes que viraram finalização."
        )

    if home["ppda"] is not None and away["ppda"] is not None:
        home_pressed_more = home["ppda"] < away["ppda"]
        pressing_team = home_label if home_pressed_more else away_label
        pressing_ppda = home["ppda"] if home_pressed_more else away["ppda"]
        other_team = away_label if home_pressed_more else home_label
        other_ppda = away["ppda"] if home_pressed_more else home["ppda"]
        notes.append(
            f"{pressing_team} pressionou mais: PPDA {pressing_ppda:.2f} "
            f"contra {other_ppda:.2f} de {other_team}."
        )

    counter_gap = home["counterpressures"] - away["counterpressures"]
    if abs(counter_gap) >= 3:
        leader = home_label if counter_gap > 0 else away_label
        leader_value = home["counterpressures"] if counter_gap > 0 else away["counterpressures"]
        other_value = away["counterpressures"] if counter_gap > 0 else home["counterpressures"]
        notes.append(
            f"{leader} ativou mais counterpress após a perda: "
            f"{leader_value} ações contra {other_value}."
        )

    if player_radars:
        top = player_radars[0]
        notes.append(
            f"{top['player']} liderou a influência contextual com índice "
            f"{top['influence_index']:.1f} ({top['influence_delta_pct']:+.1f}% "
            "vs média da função)."
        )

    return notes[:4]


def _top_impact_reason(player):
    labels = {
        "attack": "ameaça ofensiva",
        "creation": "criação",
        "progression": "progressão",
        "passing": "volume e qualidade de passe",
        "defense": "ações defensivas",
        "pressure": "pressão",
        "goal_defense": "defesa do gol",
        "footwork": "jogo com os pés",
        "long_balls": "bolas longas",
        "sweeper": "ações fora da área",
        "pressure_received": "resposta sob pressão",
        "build_up": "participação na construção",
    }
    dimensions = sorted(
        player.get("dimension_scores", {}).items(),
        key=lambda item: item[1],
        reverse=True,
    )[:3]
    strengths = " e ".join(
        f"{labels.get(key, key)} ({score:.0f}/100)"
        for key, score in dimensions[:2]
    )
    return (
        f"Influência {player['influence_index']:.1f} "
        f"({player['influence_delta_pct']:+.0f}% vs média da função), "
        f"com destaque em {strengths}."
    )


def _build_top_impacts(prepared_rows, limit=5):
    return [
        {
            "player": row["player"],
            "team": get_team_display(row["team"])["name"],
            "position": row["position"],
            "influence_index": row["influence_index"],
            "influence_delta_pct": row["influence_delta_pct"],
            "contextual_score": row["contextual_score"],
            "reason": _top_impact_reason(row),
        }
        for row in prepared_rows
        if row["eligible_for_ranking"]
    ][:limit]

def replace_nan(obj):
    if isinstance(obj, float) and math.isnan(obj):
        return None
    elif isinstance(obj, dict):
        return {k: replace_nan(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_nan(i) for i in obj]
    return obj

def get_matches():
    matches_file = os.path.join(DATA_DIR, "matches.json")
    if not os.path.exists(matches_file):
        return []
    with open(matches_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return replace_nan(data)


def get_display_matches():
    display_matches = []
    for match in get_matches():
        home = get_team_display(match.get("home_team"))
        away = get_team_display(match.get("away_team"))
        home_score = match.get("home_score", 0)
        away_score = match.get("away_score", 0)
        penalty_shootout = {"occurred": False, "home_score": 0, "away_score": 0}
        if (
            home_score == away_score
            and match.get("competition_stage") != "Group Stage"
        ):
            penalty_shootout = build_penalty_shootout(
                get_match_events(match.get("match_id")),
                match.get("home_team"),
                match.get("away_team"),
            )
        colors = resolve_match_colors(home, away)
        if penalty_shootout["occurred"]:
            display_label = (
                f"{home['name']} ({penalty_shootout['home_score']}) "
                f"{home_score}-{away_score} "
                f"({penalty_shootout['away_score']}) {away['name']}"
            )
        else:
            display_label = f"{home['name']} {home_score}-{away_score} {away['name']}"
        display_match = dict(match)
        display_match.update(
            {
                "home_team_raw": match.get("home_team"),
                "away_team_raw": match.get("away_team"),
                "home_team": home["name"],
                "away_team": away["name"],
                "home_flag": home["flag"],
                "away_flag": away["flag"],
                "home_flag_code": home["flag_code"],
                "away_flag_code": away["flag_code"],
                "home_flag_style": home["flag_style"],
                "away_flag_style": away["flag_style"],
                "home_flag_url": home["flag_url"],
                "away_flag_url": away["flag_url"],
                "home_primary_color": colors["home"],
                "away_primary_color": colors["away"],
                "home_secondary_color": home["secondary_color"],
                "away_secondary_color": away["secondary_color"],
                "used_secondary_away": colors["used_secondary_away"],
                "penalty_shootout": penalty_shootout,
                "match_date_display": format_match_date(match.get("match_date")),
                "competition_stage_raw": match.get("competition_stage", ""),
                "competition_stage": translate_stage(match.get("competition_stage", "")),
                "score": f"{home_score} - {away_score}",
                "display_label": display_label,
                "sort_key": f"{match.get('match_date', '')}T{str(match.get('kick_off') or '00:00:00').replace('.000', '')}",
            }
        )
        display_matches.append(display_match)
    display_matches.sort(key=lambda item: (item.get("sort_key") or "", item.get("match_id") or 0))
    return display_matches

def get_match_events(match_id):
    events_file = os.path.join(DATA_DIR, f"match_{match_id}", "events.json")
    if not os.path.exists(events_file):
        return []
    with open(events_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return replace_nan(data)

def get_match_lineups(match_id):
    lineups_file = os.path.join(DATA_DIR, f"match_{match_id}", "lineups.json")
    if not os.path.exists(lineups_file):
        return {}
    with open(lineups_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return replace_nan(data)

def extract_shots(events):
    shots = []
    for e in exclude_penalty_shootout(events):
        if e.get("type") == "Shot":
            shots.append(e)
    return shots

def extract_passes(events):
    passes = []
    for e in exclude_penalty_shootout(events):
        if e.get("type") == "Pass":
            passes.append(e)
    return passes

def extract_pressure_events(events):
    pressures = []
    for e in exclude_penalty_shootout(events):
        if e.get("type") == "Pressure":
            pressures.append(e)
    return pressures


def build_interactive_events(events, home_team, away_team):
    shots = []
    passes = []

    for event in exclude_penalty_shootout(events):
        event_type = event.get("type")
        team_name, side = _team_side(event, home_team, away_team)
        if not side:
            continue

        player = _get_name(event.get("player")) or "Jogador não informado"
        team_display = get_team_display(team_name)
        location = event.get("location")

        if event_type == "Shot" and _in_pitch(location):
            outcome = _label(event.get("shot_outcome"), "Sem resultado")
            shots.append(
                {
                    "id": event.get("id"),
                    "team": side,
                    "team_name": team_display["name"],
                    "flag": team_display["flag"],
                    "flag_code": team_display["flag_code"],
                    "flag_style": team_display["flag_style"],
                    "flag_url": team_display["flag_url"],
                    "player": player,
                    "period": int(_as_float(event.get("period"), 0)),
                    "minute": int(_as_float(event.get("minute"), 0)),
                    "minute_label": _minute_label(event),
                    "x": round(_as_float(location[0]), 2),
                    "y": round(_as_float(location[1]), 2),
                    "xg": round(_as_float(event.get("shot_statsbomb_xg")), 2),
                    "result": outcome,
                    "is_goal": event.get("shot_outcome") == "Goal",
                    "on_target": event.get("shot_outcome") in SHOT_ON_TARGET_OUTCOMES,
                    "shot_type": _label(event.get("shot_type")),
                    "body_part": _label(event.get("shot_body_part")),
                    "tooltip": f"{player} | {team_display['name']} | {outcome} | {_minute_label(event)} | xG {round(_as_float(event.get('shot_statsbomb_xg')), 2)}",
                }
            )

        if event_type == "Pass" and _in_pitch(location) and _in_pitch(event.get("pass_end_location")):
            end = event.get("pass_end_location")
            recipient = _get_name(event.get("pass_recipient")) or "Sem recebedor"
            outcome = "Completo" if _is_completed_pass(event) else _label(event.get("pass_outcome"), "Incompleto")
            passes.append(
                {
                    "id": event.get("id"),
                    "team": side,
                    "team_name": team_display["name"],
                    "flag": team_display["flag"],
                    "flag_code": team_display["flag_code"],
                    "flag_style": team_display["flag_style"],
                    "flag_url": team_display["flag_url"],
                    "player": player,
                    "recipient": recipient,
                    "period": int(_as_float(event.get("period"), 0)),
                    "minute": int(_as_float(event.get("minute"), 0)),
                    "minute_label": _minute_label(event),
                    "x": round(_as_float(location[0]), 2),
                    "y": round(_as_float(location[1]), 2),
                    "end_x": round(_as_float(end[0]), 2),
                    "end_y": round(_as_float(end[1]), 2),
                    "length": round(_as_float(event.get("pass_length")), 1),
                    "result": outcome,
                    "completed": _is_completed_pass(event),
                    "progressive": _is_progressive_pass(event),
                    "shot_assist": _is_truthy(event.get("pass_shot_assist")),
                    "tooltip": f"{player} para {recipient} | {team_display['name']} | {outcome} | {_minute_label(event)}",
                }
            )

    return {"shots": shots, "passes": passes}


def build_player_action_events(events, home_team, away_team):
    actions = []
    supported = {
        "Pass", "Carry", "Pressure", "Ball Recovery", "Duel",
        "Interception", "Shot", "Block", "Clearance",
    }
    for event in exclude_penalty_shootout(events):
        event_type = event.get("type")
        location = event.get("location")
        player = _get_name(event.get("player"))
        team_name, side = _team_side(event, home_team, away_team)
        if (
            event_type not in supported
            or not player
            or not side
            or not _valid_location(location)
        ):
            continue
        action_type = {
            "Ball Recovery": "recovery",
            "Interception": "interception",
            "Pressure": "counterpress" if _is_truthy(event.get("counterpress")) else "pressure",
            "Duel": "tackle" if event.get("duel_type") == "Tackle" else "defensive",
            "Block": "defensive",
            "Clearance": "defensive",
            "Shot": "shot",
            "Carry": "progressive_carry" if _is_progressive_carry(event) else "carry",
            "Pass": "progressive_pass" if _is_progressive_pass(event) else "pass",
        }[event_type]
        end = (
            event.get("pass_end_location")
            or event.get("carry_end_location")
            or event.get("shot_end_location")
            or location
        )
        actions.append(
            {
                "id": event.get("id"),
                "event_type": action_type,
                "source_type": event_type,
                "player": player,
                "team": side,
                "team_name": get_team_display(team_name)["name"],
                "minute": int(_as_float(event.get("minute"))),
                "minute_label": _minute_label(event),
                "x": round(_as_float(location[0]), 2),
                "y": round(_as_float(location[1]), 2),
                "end_x": round(_as_float(end[0]), 2) if _valid_location(end) else None,
                "end_y": round(_as_float(end[1]), 2) if _valid_location(end) else None,
                "completed": _is_completed_pass(event) if event_type == "Pass" else None,
                "xg": round(_as_float(event.get("shot_statsbomb_xg")), 3),
                "counterpress": _is_truthy(event.get("counterpress")),
                "tooltip": f"{player} · {_label(event_type)} · {_minute_label(event)}",
            }
        )
    return actions


def build_match_momentum(events, home_team, away_team, bucket_minutes=5):
    match_events = exclude_penalty_shootout(events)
    final_minute = max(
        [int(_as_float(event.get("minute"))) for event in match_events] + [90]
    )
    bucket_count = math.ceil((final_minute + 1) / bucket_minutes)
    buckets = [
        {
            "start": index * bucket_minutes,
            "end": (index + 1) * bucket_minutes,
            "home": {
                "xg": 0.0, "shots": 0, "pressures": 0, "counterpress": 0,
                "progressive_passes": 0, "progressive_carries": 0,
                "offensive_recoveries": 0,
            },
            "away": {
                "xg": 0.0, "shots": 0, "pressures": 0, "counterpress": 0,
                "progressive_passes": 0, "progressive_carries": 0,
                "offensive_recoveries": 0,
            },
        }
        for index in range(bucket_count)
    ]
    for event in match_events:
        team_name, side = _team_side(event, home_team, away_team)
        if not side:
            continue
        index = min(
            int(_as_float(event.get("minute"))) // bucket_minutes,
            bucket_count - 1,
        )
        values = buckets[index][side]
        event_type = event.get("type")
        if event_type == "Shot":
            values["shots"] += 1
            values["xg"] += _as_float(event.get("shot_statsbomb_xg"))
        if event_type == "Pressure":
            values["pressures"] += 1
        if _is_truthy(event.get("counterpress")):
            values["counterpress"] += 1
        if _is_progressive_pass(event):
            values["progressive_passes"] += 1
        if _is_progressive_carry(event):
            values["progressive_carries"] += 1
        location = event.get("location")
        if (
            event_type == "Ball Recovery"
            and _valid_location(location)
            and _as_float(location[0]) >= 80
            and not _is_truthy(event.get("ball_recovery_recovery_failure"))
        ):
            values["offensive_recoveries"] += 1
    for bucket in buckets:
        for side in ("home", "away"):
            bucket[side]["xg"] = round(bucket[side]["xg"], 3)
    return {
        "bucket_minutes": bucket_minutes,
        "buckets": buckets,
        "series": {
            "xg": ("xg",),
            "pressure": ("pressures", "counterpress"),
            "progression": (
                "progressive_passes",
                "progressive_carries",
                "offensive_recoveries",
            ),
            "shots": ("shots",),
        },
    }


def build_goal_events(events, home_team, away_team):
    goals = {"home": [], "away": []}

    for event in exclude_penalty_shootout(events):
        if event.get("type") != "Shot" or event.get("shot_outcome") != "Goal":
            continue

        team_name, side = _team_side(event, home_team, away_team)
        if not side:
            continue

        player = _get_name(event.get("player")) or "Jogador não informado"
        goal = {
            "id": event.get("id"),
            "team": side,
            "team_name": get_team_display(team_name)["name"],
            "player": player,
            "minute": int(_as_float(event.get("minute"), 0)),
            "minute_label": _goal_minute_label(event),
            "xg": round(_as_float(event.get("shot_statsbomb_xg")), 2),
            "body_part": _label(event.get("shot_body_part")),
        }
        goals[side].append(goal)

    for side in goals:
        goals[side].sort(key=lambda item: item["minute"])
    return goals


def build_grouped_goal_events(events, home_team, away_team):
    grouped = {"home": [], "away": []}
    for side, goals in build_goal_events(events, home_team, away_team).items():
        players = {}
        order = []
        for goal in goals:
            key = goal["player"]
            if key not in players:
                players[key] = {
                    "player": goal["player"],
                    "team": goal["team"],
                    "team_name": goal["team_name"],
                    "minutes": [],
                    "minute_labels": [],
                    "goals": 0,
                    "xg": 0.0,
                }
                order.append(key)
            players[key]["minutes"].append(goal["minute"])
            players[key]["minute_labels"].append(goal["minute_label"])
            players[key]["goals"] += 1
            players[key]["xg"] = round(players[key]["xg"] + goal["xg"], 2)
        grouped[side] = [players[key] for key in order]
    return grouped


def calculate_advanced_metrics(
    events,
    home_team,
    away_team,
    player_positions=None,
    player_minutes=None,
    tournament_reference=None,
):
    events = exclude_penalty_shootout(events)
    player_positions = player_positions or build_player_positions(events)
    minutes_were_supplied = player_minutes is not None
    player_minutes = player_minutes or {}
    metrics = {
        "home": _empty_team_metrics(),
        "away": _empty_team_metrics(),
    }
    shot_xg_by_id = {}
    players = {}

    for event in events:
        if event.get("type") == "Shot":
            shot_id = event.get("id")
            if shot_id:
                shot_xg_by_id[shot_id] = _as_float(event.get("shot_statsbomb_xg"))
    
    for e in events:
        event_type = e.get("type")
        team = _get_name(e.get("team")) or _get_name(e.get("possession_team"))
        side = "home" if team == home_team else "away" if team == away_team else None

        if not side:
            continue

        player_name = _get_name(e.get("player"))
        player_row = None
        if player_name:
            if player_name not in players:
                players[player_name] = _empty_player_metrics(
                    player_name,
                    team,
                    player_positions.get(player_name),
                    player_minutes.get(player_name, 0 if minutes_were_supplied else 90),
                )
            player_row = players[player_name]

        if event_type == "Shot":
            shot_xg = _as_float(e.get("shot_statsbomb_xg"))
            metrics[side]["xg"] += shot_xg
            metrics[side]["shots"] += 1
            if e.get("shot_outcome") in SHOT_ON_TARGET_OUTCOMES:
                metrics[side]["shots_on_target"] += 1
            if e.get("shot_outcome") == "Goal":
                metrics[side]["goals"] += 1
            if player_row:
                player_row["xg"] += shot_xg
                player_row["shots"] += 1
                if e.get("shot_outcome") in SHOT_ON_TARGET_OUTCOMES:
                    player_row["shots_on_target"] += 1
                if e.get("shot_outcome") == "Goal":
                    player_row["goals"] += 1
                
        if event_type == "Pass":
            metrics[side]["passes"] += 1
            completed_pass = _is_completed_pass(e)
            pass_length = _as_float(e.get("pass_length"))
            if _is_completed_pass(e):
                metrics[side]["completed_passes"] += 1
            if e.get("pass_type") == "Corner":
                metrics[side]["corners"] += 1

            loc = e.get("location")
            if _valid_location(loc) and _as_float(loc[0]) <= 72:
                metrics[_opponent_key(side)]["opponent_zone_passes"] += 1

            if player_row:
                player_row["passes"] += 1
                if completed_pass:
                    player_row["completed_passes"] += 1
                if pass_length >= 30:
                    player_row["long_passes"] += 1
                    if completed_pass:
                        player_row["completed_long_passes"] += 1
                if _is_truthy(e.get("under_pressure")):
                    player_row["passes_under_pressure"] += 1
                    if completed_pass:
                        player_row["completed_passes_under_pressure"] += 1
                if _enters_final_third(e):
                    player_row["passes_into_final_third"] += 1
                if _enters_box(e):
                    player_row["passes_into_box"] += 1
                if _is_truthy(e.get("pass_cross")):
                    player_row["crosses"] += 1
                    if completed_pass:
                        player_row["completed_crosses"] += 1
                if _is_truthy(e.get("pass_shot_assist")):
                    player_row["shot_assists"] += 1
                if _is_truthy(e.get("pass_cut_back")):
                    player_row["cutbacks"] += 1
                if _is_truthy(e.get("pass_through_ball")):
                    player_row["through_balls"] += 1

            if _is_truthy(e.get("under_pressure")):
                metrics[side]["passes_under_pressure_total"] += 1
                if completed_pass:
                    metrics[side]["passes_under_pressure_completed"] += 1

            if _is_progressive_pass(e):
                metrics[side]["progressive_passes"] += 1
                if player_row:
                    player_row["progressive_passes"] += 1
                    start = e.get("location") or []
                    end = e.get("pass_end_location") or []
                    player_row["progressive_pass_distance"] += max(
                        0,
                        _as_float(end[0]) - _as_float(start[0]),
                    )
                    metrics[side]["total_progression_distance"] += max(
                        0,
                        _as_float(end[0]) - _as_float(start[0]),
                    )

            if _is_truthy(e.get("pass_shot_assist")):
                assisted_shot_id = e.get("pass_assisted_shot_id")
                assist_xg = shot_xg_by_id.get(assisted_shot_id, 0.0)
                metrics[side]["xa"] += assist_xg
                if player_row:
                    player_row["xa"] += assist_xg

        if event_type == "Foul Committed":
            metrics[side]["fouls_committed"] += 1
            if player_row:
                player_row["fouls_committed"] += 1
                if e.get("foul_committed_card"):
                    player_row["cards"] += 1

        if event_type == "Foul Won" and player_row:
            player_row["fouls_won"] += 1

        if event_type == "Carry" and _is_progressive_carry(e):
            metrics[side]["progressive_carries"] += 1
            if player_row:
                player_row["progressive_carries"] += 1
                start = e.get("location") or []
                end = e.get("carry_end_location") or []
                player_row["progressive_carry_distance"] += max(
                    0,
                    _as_float(end[0]) - _as_float(start[0]),
                )
                metrics[side]["total_progression_distance"] += max(
                    0,
                    _as_float(end[0]) - _as_float(start[0]),
                )

        if event_type == "Dribble":
            metrics[side]["dribbles"] += 1
            if player_row:
                player_row["dribbles"] += 1
            if e.get("dribble_outcome") == "Complete":
                metrics[side]["successful_dribbles"] += 1
                if player_row:
                    player_row["successful_dribbles"] += 1

        if event_type == "Duel":
            duel_type = e.get("duel_type") or ""
            duel_won = (
                e.get("duel_outcome") in SUCCESSFUL_TACKLE_OUTCOMES
                or duel_type == "Aerial Won"
            )
            if player_row:
                player_row["duels"] += 1
                if duel_won:
                    player_row["duels_won"] += 1
                if duel_type in {"Aerial Won", "Aerial Lost"}:
                    player_row["aerial_duels"] += 1
                    if duel_type == "Aerial Won":
                        player_row["aerial_duels_won"] += 1
            if duel_type == "Tackle":
                metrics[side]["tackles"] += 1
                if player_row:
                    player_row["tackles"] += 1
                if duel_won:
                    metrics[side]["successful_tackles"] += 1
                    if player_row:
                        player_row["successful_tackles"] += 1

        if event_type == "Pressure":
            metrics[side]["pressure_events"] += 1
            if player_row:
                player_row["pressures"] += 1
            location = e.get("location")
            if _valid_location(location) and _as_float(location[0]) >= 80:
                metrics[side]["pressures_final_third"] += 1
                if player_row:
                    player_row["pressures_final_third"] += 1
            if _is_truthy(e.get("counterpress")) and player_row:
                player_row["counterpressures"] += 1

        if player_row and event_type == "Interception":
            player_row["interceptions"] += 1

        if player_row and event_type == "Clearance":
            player_row["clearances"] += 1

        if player_row and event_type == "Block":
            player_row["blocks"] += 1

        if player_row and event_type == "Ball Recovery":
            if not _is_truthy(e.get("ball_recovery_recovery_failure")):
                player_row["ball_recoveries"] += 1
            recovery_location = e.get("location")
            if _valid_location(recovery_location) and _as_float(recovery_location[0]) >= 80:
                player_row["offensive_recoveries"] += 1
                metrics[side]["offensive_recoveries"] += 1

        if player_row and event_type == "Goal Keeper":
            player_row["goalkeeper_actions"] += 1
            if e.get("goalkeeper_type") in GOALKEEPER_SAVE_TYPES:
                player_row["goalkeeper_saves"] += 1
            if e.get("goalkeeper_outcome") == "Claim":
                player_row["goalkeeper_claims"] += 1
            location = e.get("location")
            if _valid_location(location) and _as_float(location[0]) > 18:
                player_row["goalkeeper_actions_outside_box"] += 1

        if event_type in DEFENSIVE_EVENT_TYPES:
            loc = e.get("location")
            if _valid_location(loc) and _as_float(loc[0]) >= 48:
                metrics[side]["defensive_actions"] += 1
                if player_row:
                    player_row["defensive_actions"] += 1
            if _valid_location(loc) and _as_float(loc[0]) >= 80:
                metrics[side]["high_turnovers"] += 1
            if _is_truthy(e.get("counterpress")):
                metrics[side]["counterpressures"] += 1
                if player_row and event_type != "Pressure":
                    player_row["counterpressures"] += 1

    for team_key in ["home", "away"]:
        team_metrics = metrics[team_key]
        defensive_actions = team_metrics["defensive_actions"]
        team_metrics["xg"] = round(team_metrics["xg"], 2)
        team_metrics["xa"] = round(team_metrics["xa"], 2)
        team_metrics["pass_accuracy"] = round((team_metrics["completed_passes"] / team_metrics["passes"]) * 100, 1) if team_metrics["passes"] else 0
        team_metrics["shot_accuracy"] = round((team_metrics["shots_on_target"] / team_metrics["shots"]) * 100, 1) if team_metrics["shots"] else 0
        team_metrics["dribble_accuracy"] = round((team_metrics["successful_dribbles"] / team_metrics["dribbles"]) * 100, 1) if team_metrics["dribbles"] else 0
        team_metrics["tackle_accuracy"] = round((team_metrics["successful_tackles"] / team_metrics["tackles"]) * 100, 1) if team_metrics["tackles"] else 0
        team_metrics["xg_per_shot"] = round(team_metrics["xg"] / team_metrics["shots"], 2) if team_metrics["shots"] else 0
        team_metrics["shot_conversion"] = safe_percentage(team_metrics["goals"], team_metrics["shots"])
        team_metrics["shots_on_target_conversion"] = safe_percentage(team_metrics["goals"], team_metrics["shots_on_target"])
        team_metrics["passes_under_pressure_accuracy"] = safe_percentage(
            team_metrics["passes_under_pressure_completed"],
            team_metrics["passes_under_pressure_total"],
        )
        team_metrics["counterpress_percentage"] = safe_percentage(
            team_metrics["counterpressures"],
            team_metrics["pressure_events"],
        )
        team_metrics["ppda"] = round(team_metrics["opponent_zone_passes"] / defensive_actions, 2) if defensive_actions else None

    for player_row in players.values():
        player_row["pass_accuracy"] = safe_percentage(
            player_row["completed_passes"], player_row["passes"]
        )
        player_row["passes_under_pressure_accuracy"] = safe_percentage(
            player_row["completed_passes_under_pressure"],
            player_row["passes_under_pressure"],
        )
        player_row["long_pass_accuracy"] = safe_percentage(
            player_row["completed_long_passes"], player_row["long_passes"]
        )
        player_row["cross_accuracy"] = safe_percentage(
            player_row["completed_crosses"], player_row["crosses"]
        )
        player_row["dribble_accuracy"] = safe_percentage(
            player_row["successful_dribbles"], player_row["dribbles"]
        )
        player_row["tackle_accuracy"] = safe_percentage(
            player_row["successful_tackles"], player_row["tackles"]
        )
        player_row["duel_accuracy"] = safe_percentage(
            player_row["duels_won"], player_row["duels"]
        )
        player_row["aerial_duel_accuracy"] = safe_percentage(
            player_row["aerial_duels_won"], player_row["aerial_duels"]
        )
        player_row["xg_per_shot"] = (
            round(player_row["xg"] / player_row["shots"], 2)
            if player_row["shots"] else 0
        )
        player_row["shot_conversion"] = safe_percentage(
            player_row["goals"], player_row["shots"]
        )
        player_row["shots_on_target_conversion"] = safe_percentage(
            player_row["goals"], player_row["shots_on_target"]
        )
        player_row["counterpress_percentage"] = safe_percentage(
            player_row["counterpressures"], player_row["pressures"]
        )

    for side, opponent_side in (("home", "away"), ("away", "home")):
        team_name = home_team if side == "home" else away_team
        goalkeeper = next(
            (
                row for row in players.values()
                if row["team"] == team_name and row["macro_position"] == "Goleiro"
            ),
            None,
        )
        if goalkeeper:
            goalkeeper["goalkeeper_shots_faced"] = metrics[opponent_side]["shots_on_target"]
            goalkeeper["goalkeeper_goals_conceded"] = metrics[opponent_side]["goals"]
            goalkeeper["goalkeeper_xg_faced"] = metrics[opponent_side]["xg"]
            goalkeeper["goalkeeper_goals_prevented"] = round(
                goalkeeper["goalkeeper_xg_faced"]
                - goalkeeper["goalkeeper_goals_conceded"],
                2,
            )
            goalkeeper["goalkeeper_save_percentage"] = safe_percentage(
                goalkeeper["goalkeeper_saves"],
                goalkeeper["goalkeeper_shots_faced"],
            )
            goalkeeper["goalkeeper_claim_percentage"] = safe_percentage(
                goalkeeper["goalkeeper_claims"],
                goalkeeper["goalkeeper_actions"],
            )
            goalkeeper["goalkeeper_sweeper_percentage"] = safe_percentage(
                goalkeeper["goalkeeper_actions_outside_box"],
                goalkeeper["goalkeeper_actions"],
            )

    prepared_players = _prepare_player_rows(players, tournament_reference)
    player_radars = _build_player_radars(prepared_players)
    metrics["player_radars"] = player_radars
    metrics["player_comparison"] = _build_player_comparison(prepared_players)
    metrics["top_impacts"] = _build_top_impacts(prepared_players)
    metrics["tactical_notes"] = _build_tactical_notes(metrics, home_team, away_team, player_radars)

    return metrics


def _build_tournament_macroposition_reference(match_ids):
    aggregated = {}
    matches_by_id = {match["match_id"]: match for match in get_matches()}
    for match_id in match_ids:
        match = matches_by_id.get(match_id)
        if not match:
            continue
        events = get_match_events(match_id)
        lineups = get_match_lineups(match_id)
        match_events = exclude_penalty_shootout(events)
        positions = build_player_positions(match_events, lineups)
        minutes = build_player_minutes(lineups, match_events)
        metrics = calculate_advanced_metrics(
            match_events,
            match["home_team"],
            match["away_team"],
            positions,
            minutes,
            tournament_reference={},
        )
        for row in metrics["player_comparison"]:
            if row["minutes"] <= 0:
                continue
            key = (row["player"], row["macro_position"])
            total = aggregated.setdefault(
                key,
                {
                    "macro_position": row["macro_position"],
                    "minutes": 0.0,
                    **{
                        metric: 0.0
                        for metric in set(PLAYER_PER90_KEYS) | {"total_progression_distance"}
                    },
                },
            )
            total["minutes"] += row["minutes"]
            for metric in set(PLAYER_PER90_KEYS) | {"total_progression_distance"}:
                total[metric] += _as_float(row.get(metric))

    grouped = {}
    for total in aggregated.values():
        minutes = total["minutes"]
        if minutes < TOURNAMENT_REFERENCE_MINUTES:
            continue
        per90 = {
            metric: (_as_float(total.get(metric)) * 90 / minutes)
            for metric in set(PLAYER_PER90_KEYS) | {"total_progression_distance"}
        }
        grouped.setdefault(total["macro_position"], []).append(
            {
                "minutes": minutes,
                "raw": total,
                "per90": per90,
            }
        )

    reference = {}
    metric_keys = set(PLAYER_PER90_KEYS) | {"total_progression_distance"}
    for macro_position, rows in grouped.items():
        total_minutes = sum(row["minutes"] for row in rows)
        metric_reference = {}
        for metric in metric_keys:
            values = [row["per90"][metric] for row in rows]
            weighted_mean = (
                sum(_as_float(row["raw"].get(metric)) for row in rows)
                * 90
                / total_minutes
                if total_minutes > 0
                else 0
            )
            metric_reference[metric] = {
                "p05": round(_percentile(values, 0.05), 4),
                "p95": round(_percentile(values, 0.95), 4),
                "mean_per90": round(weighted_mean, 4),
            }
        mean_metric_scores = {
            metric: contextual_score(
                values["mean_per90"],
                values["p05"],
                values["p95"],
            )
            for metric, values in metric_reference.items()
        }
        reference[macro_position] = {
            "players": len(rows),
            "minutes": round(total_minutes, 2),
            "metrics": metric_reference,
            "dimension_average_scores": _dimension_scores(
                mean_metric_scores,
                macro_position,
            ),
        }
    return reference


@lru_cache(maxsize=1)
def _cached_tournament_macroposition_reference():
    if os.path.exists(TOURNAMENT_REFERENCE_FILE):
        with open(TOURNAMENT_REFERENCE_FILE, "r", encoding="utf-8") as reference_file:
            return json.load(reference_file)
    return _build_tournament_macroposition_reference(
        tuple(match["match_id"] for match in get_matches())
    )


def build_tournament_macroposition_reference(match_ids=None):
    if match_ids is None:
        return _cached_tournament_macroposition_reference()
    return _build_tournament_macroposition_reference(tuple(match_ids))


def build_tournament_position_reference(match_ids=None):
    """Alias compatível para consumidores anteriores da API."""
    return build_tournament_macroposition_reference(match_ids)


def calculate_period_metrics(events, home_team, away_team, player_positions=None):
    match_events = exclude_penalty_shootout(events)
    periods = {"all": match_events}
    periods["1"] = [event for event in match_events if int(_as_float(event.get("period"), 0)) == 1]
    periods["2"] = [event for event in match_events if int(_as_float(event.get("period"), 0)) == 2]

    output = {}
    for period, period_events in periods.items():
        metrics = calculate_advanced_metrics(period_events, home_team, away_team, player_positions)
        output[period] = {
            "home": metrics["home"],
            "away": metrics["away"],
        }
    return output

def extract_xg_flow(shots, home_team, away_team):
    # Sort shots by minute
    sorted_shots = sorted(exclude_penalty_shootout(shots), key=lambda x: x.get('minute', 0))
    flow = {"home": {"minutes": [0], "xg": [0.0]}, "away": {"minutes": [0], "xg": [0.0]}}
    
    home_xg = 0.0
    away_xg = 0.0
    
    for s in sorted_shots:
        team_raw = s.get('possession_team') or s.get('team')
        team = team_raw.get("name") if isinstance(team_raw, dict) else team_raw
        
        minute = s.get('minute', 0)
        xg = s.get('shot_statsbomb_xg', 0.0) or 0.0
        
        if team == home_team:
            home_xg += xg
            flow["home"]["minutes"].append(minute)
            flow["home"]["xg"].append(round(home_xg, 2))
        elif team == away_team:
            away_xg += xg
            flow["away"]["minutes"].append(minute)
            flow["away"]["xg"].append(round(away_xg, 2))
            
    # Append final minute
    final_minute = max([s.get('minute', 90) for s in shots] + [90])
    flow["home"]["minutes"].append(final_minute)
    flow["home"]["xg"].append(round(home_xg, 2))
    flow["away"]["minutes"].append(final_minute)
    flow["away"]["xg"].append(round(away_xg, 2))
    
    return flow
