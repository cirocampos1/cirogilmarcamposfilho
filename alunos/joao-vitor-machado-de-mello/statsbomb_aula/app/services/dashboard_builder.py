import importlib.util
import json
import logging
import math
from pathlib import Path

from app.services import statsbomb_parser


LOGGER = logging.getLogger(__name__)
TABLE_ARTIFACTS = {
    "team_metrics",
    "player_metrics",
    "shot_map",
    "pass_map",
    "momentum",
    "player_action_maps",
    "events",
    "carries",
    "pressures",
}
MATCH_JSON_ARTIFACTS = {
    "match_summary.json",
    "player_radars.json",
    "xg_flow.json",
    "tactical_insights.json",
    "pressure_maps.json",
}
PARQUET_METADATA_KEY = b"dashboard_storage"
NESTED_COLUMNS_METADATA_KEY = b"nested_json_columns"
INT8_COLUMNS = {"period", "second", "attempt_number"}
INT16_COLUMNS = {
    "minute",
    "start",
    "end",
    "possession",
    "bucket_minutes",
}
INT32_COLUMNS = {
    "match_id",
    "index",
    "player_id",
    "team_id",
    "possession_team_id",
    "pass_recipient_id",
    "substitution_outcome_id",
    "substitution_replacement_id",
}


def parquet_engine_available():
    return bool(importlib.util.find_spec("pyarrow"))


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _clean_scalar(value):
    if isinstance(value, float) and math.isnan(value):
        return None
    return value


def _encode_nested_columns(rows):
    all_columns = list(dict.fromkeys(
        key
        for row in rows
        for key in row
    ))
    nested_columns = {
        key
        for row in rows
        for key, value in row.items()
        if isinstance(value, (dict, list, tuple))
    }
    encoded_rows = []
    for row in rows:
        encoded = {}
        for key in all_columns:
            value = row.get(key)
            value = _clean_scalar(value)
            if key in nested_columns:
                encoded[key] = (
                    json.dumps(
                        value,
                        ensure_ascii=False,
                        separators=(",", ":"),
                        sort_keys=True,
                    )
                    if value is not None
                    else None
                )
            else:
                encoded[key] = value
        encoded_rows.append(encoded)
    return encoded_rows, sorted(nested_columns)


def _compact_arrow_types(table):
    import pyarrow as pa
    import pyarrow.compute as pc

    for index, field in enumerate(table.schema):
        target = None
        if field.name in INT8_COLUMNS and pa.types.is_integer(field.type):
            target = pa.int8()
        elif field.name in INT16_COLUMNS and pa.types.is_integer(field.type):
            target = pa.int16()
        elif field.name in INT32_COLUMNS and pa.types.is_integer(field.type):
            target = pa.int32()
        elif pa.types.is_floating(field.type):
            target = pa.float32()
        if target is None or field.type == target:
            continue
        try:
            table = table.set_column(
                index,
                field.name,
                pc.cast(table.column(index), target, safe=True),
            )
        except (ValueError, TypeError):
            LOGGER.warning(
                "Keeping inferred Parquet type for column %s.",
                field.name,
            )
    return table


def _table_with_metadata(rows, compression):
    import pyarrow as pa

    encoded_rows, nested_columns = _encode_nested_columns(rows)
    table = pa.Table.from_pylist(encoded_rows)
    table = _compact_arrow_types(table)
    metadata = dict(table.schema.metadata or {})
    metadata[PARQUET_METADATA_KEY] = json.dumps(
        {
            "version": 1,
            "compression": compression,
        },
        separators=(",", ":"),
    ).encode("utf-8")
    metadata[NESTED_COLUMNS_METADATA_KEY] = json.dumps(
        nested_columns,
        separators=(",", ":"),
    ).encode("utf-8")
    return table.replace_schema_metadata(metadata)


def write_table(base_path, rows):
    base_path.parent.mkdir(parents=True, exist_ok=True)
    parquet_path = base_path.with_suffix(".parquet")
    json_path = base_path.with_suffix(".json")
    if not parquet_engine_available():
        raise RuntimeError(
            "pyarrow is required to build processed dashboard tables."
        )

    import pyarrow.parquet as parquet

    temporary_path = parquet_path.with_suffix(".parquet.tmp")
    last_error = None
    for compression in ("zstd", "snappy"):
        try:
            table = _table_with_metadata(rows, compression)
            parquet.write_table(
                table,
                temporary_path,
                compression=compression,
                use_dictionary=True,
                write_statistics=True,
            )
            temporary_path.replace(parquet_path)
            json_path.unlink(missing_ok=True)
            return parquet_path
        except Exception as exc:
            last_error = exc
            temporary_path.unlink(missing_ok=True)
            if compression == "zstd":
                LOGGER.warning(
                    "Zstandard compression failed for %s; retrying with Snappy.",
                    base_path.name,
                )
    raise RuntimeError(
        f"Could not write Parquet artifact {parquet_path}"
    ) from last_error


def build_manifest(matches, display_matches=None):
    display_by_id = {
        int(match["match_id"]): match
        for match in (display_matches or [])
    }
    manifest = [
        {
            "match_id": int(match["match_id"]),
            "date": match.get("match_date"),
            "stage": match.get("competition_stage"),
            "home_team": match.get("home_team"),
            "away_team": match.get("away_team"),
            "home_score": int(match.get("home_score") or 0),
            "away_score": int(match.get("away_score") or 0),
            "display_name": display_by_id.get(
                int(match["match_id"]),
                {},
            ).get(
                "display_label",
                (
                    f"{match.get('home_team')} "
                    f"{int(match.get('home_score') or 0)}-"
                    f"{int(match.get('away_score') or 0)} "
                    f"{match.get('away_team')}"
                ),
            ),
        }
        for match in matches
    ]
    manifest.sort(key=lambda match: (match["date"] or "", match["match_id"]))
    return manifest


def match_artifacts_exist(match_dir):
    tables_exist = all(
        (match_dir / f"{name}.parquet").exists()
        for name in TABLE_ARTIFACTS
    )
    return tables_exist and all(
        (match_dir / filename).exists()
        for filename in MATCH_JSON_ARTIFACTS
    )


def build_compact_player_radars(players):
    fields = (
        "player",
        "team",
        "position",
        "position_group",
        "macro_position",
        "minutes",
        "influence_index",
        "influence_delta_pct",
        "contextual_score",
        "xg",
        "xa",
        "completed_passes",
        "pass_accuracy",
        "progressive_passes",
        "progressive_carries",
        "total_progression_distance",
        "pressures",
        "counterpressures",
        "ball_recoveries",
        "eligible_for_radar",
        "eligible_for_ranking",
        "low_minutes",
        "impact_score",
        "team_flag_code",
        "team_flag_url",
        "radar",
        "dimension_scores",
        "dimension_average_scores",
        "position_average_radar",
        "metric_labels",
        "radar_labels",
        "metrics",
    )
    return [
        {
            field: player.get(field)
            for field in fields
        }
        for player in players
    ]


def build_event_rows(events):
    common_fields = (
        "id",
        "index",
        "match_id",
        "period",
        "timestamp",
        "minute",
        "second",
        "type",
        "possession",
        "possession_team",
        "possession_team_id",
        "play_pattern",
        "team",
        "team_id",
        "player",
        "player_id",
        "position",
        "duration",
        "under_pressure",
        "counterpress",
        "location",
    )
    rows = []
    for event in events:
        row = {
            field: event.get(field)
            for field in common_fields
            if event.get(field) is not None
        }
        details = {
            key: value
            for key, value in event.items()
            if key not in common_fields and value is not None
        }
        if details:
            row["details"] = details
        rows.append(row)
    return rows


def build_team_metric_rows(advanced, period_metrics):
    rows = [
        {"scope": "home", "period": None, "metrics": advanced["home"]},
        {"scope": "away", "period": None, "metrics": advanced["away"]},
    ]
    rows.extend(
        {
            "scope": "period",
            "period": str(period),
            "metrics": values,
        }
        for period, values in period_metrics.items()
    )
    return rows


def build_shot_map_rows(interactive_shots, penalty_events):
    return [
        {"record_type": "shot", **row}
        for row in interactive_shots
    ] + [
        {"record_type": "penalty", **row}
        for row in penalty_events
    ]


def build_momentum_rows(momentum):
    rows = []
    for index, bucket in enumerate(momentum["buckets"]):
        rows.append(
            {
                "bucket_minutes": momentum["bucket_minutes"],
                "start": bucket["start"],
                "end": bucket["end"],
                "home": bucket["home"],
                "away": bucket["away"],
                "series": momentum["series"] if index == 0 else None,
            }
        )
    return rows


def build_match_artifacts(match, tournament_reference):
    from app.services import plotter

    match_id = int(match["match_id"])
    events = statsbomb_parser.get_match_events(match_id)
    if not events:
        raise FileNotFoundError(f"Raw events not found for match {match_id}")
    lineups = statsbomb_parser.get_match_lineups(match_id)
    match_events = statsbomb_parser.exclude_penalty_shootout(events)
    home_team = match["home_team"]
    away_team = match["away_team"]
    home_display = statsbomb_parser.get_team_display(home_team)
    away_display = statsbomb_parser.get_team_display(away_team)
    colors = statsbomb_parser.resolve_match_colors(home_display, away_display)

    shots = statsbomb_parser.extract_shots(match_events)
    passes = statsbomb_parser.extract_passes(match_events)
    pressures = statsbomb_parser.extract_pressure_events(match_events)
    player_positions = statsbomb_parser.build_player_positions(match_events, lineups)
    player_minutes = statsbomb_parser.build_player_minutes(lineups, match_events)
    advanced = statsbomb_parser.calculate_advanced_metrics(
        match_events,
        home_team,
        away_team,
        player_positions,
        player_minutes,
        tournament_reference,
    )
    period_metrics = statsbomb_parser.calculate_period_metrics(
        match_events,
        home_team,
        away_team,
        player_positions,
    )
    interactive = statsbomb_parser.build_interactive_events(
        match_events,
        home_team,
        away_team,
    )
    penalty_shootout = statsbomb_parser.build_penalty_shootout(
        events,
        home_team,
        away_team,
    )
    penalty_events = statsbomb_parser.build_penalty_events(
        events,
        home_team,
        away_team,
    )
    goals = statsbomb_parser.build_goal_events(
        match_events,
        home_team,
        away_team,
    )
    grouped_goals = statsbomb_parser.build_grouped_goal_events(
        match_events,
        home_team,
        away_team,
    )
    action_maps = statsbomb_parser.build_player_action_events(
        match_events,
        home_team,
        away_team,
    )
    momentum = statsbomb_parser.build_match_momentum(
        match_events,
        home_team,
        away_team,
    )
    match_summary = {
        "total_shots": len(shots),
        "total_passes": len(passes),
        "home_team": home_display["name"],
        "away_team": away_display["name"],
        "home_team_raw": home_team,
        "away_team_raw": away_team,
        "home_flag": home_display["flag"],
        "away_flag": away_display["flag"],
        "home_flag_code": home_display["flag_code"],
        "away_flag_code": away_display["flag_code"],
        "home_flag_style": home_display["flag_style"],
        "away_flag_style": away_display["flag_style"],
        "home_flag_url": home_display["flag_url"],
        "away_flag_url": away_display["flag_url"],
        "home_primary_color": colors["home"],
        "away_primary_color": colors["away"],
        "home_secondary_color": home_display["secondary_color"],
        "away_secondary_color": away_display["secondary_color"],
        "used_secondary_away": colors["used_secondary_away"],
        "competition_stage_raw": match.get("competition_stage", ""),
        "competition_stage": statsbomb_parser.translate_stage(
            match.get("competition_stage", "")
        ),
        "stadium": (
            f"{match.get('stadium', '')}, "
            f"{match.get('stadium_country_name', '')}"
        ),
        "referee": match.get("referee", ""),
        "home_manager": match.get("home_managers", ""),
        "away_manager": match.get("away_managers", ""),
        "home_goals": goals["home"],
        "away_goals": goals["away"],
        "home_goals_grouped": grouped_goals["home"],
        "away_goals_grouped": grouped_goals["away"],
        "penalty_shootout": penalty_shootout,
        "penalties_occurred": bool(penalty_events),
        "score": (
            f"{int(match.get('home_score') or 0)} - "
            f"{int(match.get('away_score') or 0)}"
        ),
        "date": match.get("match_date"),
        "date_display": statsbomb_parser.format_match_date(
            match.get("match_date")
        ),
        "kick_off": match.get("kick_off"),
        "teams": {
            "home": home_display,
            "away": away_display,
        },
    }
    return {
        "match_summary.json": match_summary,
        "team_metrics": build_team_metric_rows(
            advanced,
            period_metrics,
        ),
        "player_metrics": advanced["player_comparison"],
        "player_radars.json": build_compact_player_radars(
            advanced["player_radars"]
        ),
        "shot_map": build_shot_map_rows(
            interactive["shots"],
            penalty_events,
        ),
        "pass_map": interactive["passes"],
        "xg_flow.json": statsbomb_parser.extract_xg_flow(
            shots,
            home_team,
            away_team,
        ),
        "momentum": build_momentum_rows(momentum),
        "tactical_insights.json": {
            "notes": advanced["tactical_notes"],
            "top_impacts": advanced["top_impacts"],
        },
        "player_action_maps": action_maps,
        "events": build_event_rows(match_events),
        "carries": [
            row for row in action_maps
            if row["source_type"] == "Carry"
        ],
        "pressures": [
            row for row in action_maps
            if row["source_type"] == "Pressure"
        ],
        "pressure_maps.json": plotter.plot_pressure_heatmaps(
            pressures,
            home_team,
            away_team,
            colors["home"],
            colors["away"],
        ),
    }


def write_match_artifacts(match_dir, artifacts):
    match_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for name, payload in artifacts.items():
        if name in TABLE_ARTIFACTS:
            written.append(
                write_table(
                    match_dir / name,
                    payload,
                )
            )
        else:
            path = match_dir / name
            write_json(path, payload)
            written.append(path)
    expected_paths = {path.resolve() for path in written}
    for old_path in match_dir.iterdir():
        if (
            old_path.is_file()
            and old_path.resolve() not in expected_paths
            and old_path.suffix in {".json", ".parquet", ".tmp"}
        ):
            old_path.unlink()
    return written
