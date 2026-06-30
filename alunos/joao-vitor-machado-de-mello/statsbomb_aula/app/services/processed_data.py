import json
import os
import sqlite3
import zlib
from functools import lru_cache
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_PROCESSED_DIR = BASE_DIR / "data" / "processed"
DEFAULT_DATABASE_PATH = BASE_DIR / "data" / "dashboard.sqlite3"
_processed_dir_override = None
_database_path_override = None


def _file_version(path):
    stat = Path(path).stat()
    return stat.st_mtime_ns, stat.st_size


def get_processed_dir():
    return _processed_dir_override or DEFAULT_PROCESSED_DIR


def get_database_path():
    if _database_path_override is False:
        return None
    return _database_path_override or DEFAULT_DATABASE_PATH


def configure_processed_dir(path):
    global _processed_dir_override
    _processed_dir_override = Path(path) if path is not None else None
    clear_loader_caches()


def configure_database_path(path):
    global _database_path_override
    _database_path_override = Path(path) if path is not None else False
    clear_loader_caches()


@lru_cache(maxsize=256)
def _load_json(path_string):
    path = Path(path_string)
    if not path.exists():
        raise FileNotFoundError(f"Processed artifact not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


@lru_cache(maxsize=128)
def _load_table(base_path_string):
    base_path = Path(base_path_string)
    parquet_path = base_path.with_suffix(".parquet")
    json_path = base_path.with_suffix(".json")
    if parquet_path.exists():
        import pyarrow.parquet as parquet

        table = parquet.read_table(parquet_path)
        metadata = table.schema.metadata or {}
        nested_columns = json.loads(
            metadata.get(b"nested_json_columns", b"[]").decode("utf-8")
        )
        rows = table.to_pylist()
        for row in rows:
            for column in nested_columns:
                value = row.get(column)
                if isinstance(value, str):
                    row[column] = json.loads(value)
        return rows
    return _load_json(str(json_path))


@lru_cache(maxsize=4)
def _load_database_manifest(database_path_string, database_version):
    database_path = Path(database_path_string)
    if not database_path.exists():
        raise FileNotFoundError(
            f"Compact dashboard database not found: {database_path}"
        )
    with sqlite3.connect(database_path) as connection:
        row = connection.execute(
            "SELECT payload FROM metadata WHERE key = ?",
            ("manifest",),
        ).fetchone()
    if row is None:
        raise FileNotFoundError(
            f"Manifest not found in compact database: {database_path}"
        )
    return json.loads(row[0])


@lru_cache(maxsize=128)
def _load_database_match(database_path_string, match_id, database_version):
    database_path = Path(database_path_string)
    if not database_path.exists():
        raise FileNotFoundError(
            f"Compact dashboard database not found: {database_path}"
        )
    with sqlite3.connect(database_path) as connection:
        row = connection.execute(
            "SELECT payload FROM matches WHERE match_id = ?",
            (int(match_id),),
        ).fetchone()
    if row is None:
        raise FileNotFoundError(
            f"Match {match_id} not found in compact database: {database_path}"
        )
    return json.loads(zlib.decompress(row[0]).decode("utf-8"))


def clear_loader_caches():
    _load_json.cache_clear()
    _load_table.cache_clear()
    _load_database_manifest.cache_clear()
    _load_database_match.cache_clear()


def load_manifest():
    database_path = get_database_path()
    if database_path and database_path.exists():
        return _load_database_manifest(
            str(database_path),
            _file_version(database_path),
        )
    return load_manifest_from_artifacts()


def load_manifest_from_artifacts():
    return _load_json(str(get_processed_dir() / "manifest.json"))


def load_tournament_reference():
    base_path = get_processed_dir() / "tournament_reference"
    if base_path.with_suffix(".parquet").exists():
        rows = _load_table(str(base_path))
        return {
            row["macro_position"]: row["reference"]
            for row in rows
        }
    return _load_json(str(base_path.with_suffix(".json")))


def _match_dir(match_id):
    return get_processed_dir() / "matches" / str(int(match_id))


def _load_match_json(match_id, filename):
    return _load_json(str(_match_dir(match_id) / filename))


def _load_match_table(match_id, name):
    return _load_table(str(_match_dir(match_id) / name))


def load_match_summary(match_id):
    return _load_match_json(match_id, "match_summary.json")


def load_team_metrics(match_id):
    match_dir = _match_dir(match_id)
    if (match_dir / "team_metrics.parquet").exists():
        rows = _load_match_table(match_id, "team_metrics")
        bundle = {"home": {}, "away": {}, "period_metrics": {}}
        for row in rows:
            if row["scope"] in {"home", "away"}:
                bundle[row["scope"]] = row["metrics"]
            elif row["scope"] == "period":
                bundle["period_metrics"][str(row["period"])] = row["metrics"]
        return bundle
    return _load_match_json(match_id, "team_metrics.json")


def load_player_metrics(match_id):
    return _load_match_table(match_id, "player_metrics")


def load_player_radars(match_id):
    return _load_match_json(match_id, "player_radars.json")


def load_player_comparison(match_id):
    return load_player_metrics(match_id)


def load_shot_map(match_id):
    match_dir = _match_dir(match_id)
    if (match_dir / "shot_map.parquet").exists():
        shot_rows = _load_match_table(match_id, "shot_map")
        passes = _load_match_table(match_id, "pass_map")
        shots = []
        penalties = []
        for stored_row in shot_rows:
            row = dict(stored_row)
            record_type = row.pop("record_type", "shot")
            if record_type == "penalty":
                penalties.append(row)
            else:
                shots.append(row)
        return {
            "shots": shots,
            "passes": passes,
            "penalties": penalties,
        }
    return _load_match_json(match_id, "shot_map.json")


def load_xg_flow(match_id):
    return _load_match_json(match_id, "xg_flow.json")


def load_momentum(match_id):
    match_dir = _match_dir(match_id)
    if (match_dir / "momentum.parquet").exists():
        rows = _load_match_table(match_id, "momentum")
        if not rows:
            return {"bucket_minutes": 5, "buckets": [], "series": {}}
        series = next(
            (row["series"] for row in rows if row.get("series")),
            {},
        )
        return {
            "bucket_minutes": rows[0]["bucket_minutes"],
            "buckets": [
                {
                    "start": row["start"],
                    "end": row["end"],
                    "home": row["home"],
                    "away": row["away"],
                }
                for row in rows
            ],
            "series": series,
        }
    return _load_match_json(match_id, "momentum.json")


def load_tactical_insights(match_id):
    return _load_match_json(match_id, "tactical_insights.json")


def load_player_action_maps(match_id):
    return _load_match_table(match_id, "player_action_maps")


def load_events(match_id):
    return _load_match_table(match_id, "events")


def load_carries(match_id):
    return _load_match_table(match_id, "carries")


def load_pressures(match_id):
    return _load_match_table(match_id, "pressures")


def load_pressure_maps(match_id):
    return _load_match_json(match_id, "pressure_maps.json")


def load_match_payload_from_artifacts(match_id):
    summary = dict(load_match_summary(match_id))
    team_bundle = load_team_metrics(match_id)
    player_metrics = load_player_metrics(match_id)
    player_radars = load_player_radars(match_id)
    player_comparison = load_player_comparison(match_id)
    tactical = load_tactical_insights(match_id)
    shot_map = load_shot_map(match_id)

    advanced_metrics = {
        "home": team_bundle["home"],
        "away": team_bundle["away"],
        "player_radars": player_radars,
        "player_comparison": player_comparison,
        "tactical_notes": tactical["notes"],
        "top_impacts": tactical["top_impacts"],
    }
    summary.update(
        {
            "advanced_metrics": advanced_metrics,
            "period_metrics": team_bundle["period_metrics"],
            "player_metrics": player_metrics,
            "player_radars": player_radars,
            "player_comparison": player_comparison,
            "tactical_notes": tactical["notes"],
            "top_impacts": tactical["top_impacts"],
        }
    )
    return {
        "match_id": int(match_id),
        "summary": summary,
        "events": {
            "shots": shot_map["shots"],
            "passes": shot_map["passes"],
            "penalties": shot_map["penalties"],
            "player_actions": load_player_action_maps(match_id),
        },
        "charts": {
            "xg_flow": load_xg_flow(match_id),
            "momentum": load_momentum(match_id),
        },
        "images": {
            "pressure_maps": load_pressure_maps(match_id),
        },
    }


def load_match_payload(match_id):
    database_path = get_database_path()
    if database_path and database_path.exists():
        return _load_database_match(
            str(database_path),
            int(match_id),
            _file_version(database_path),
        )
    return load_match_payload_from_artifacts(match_id)


def write_compact_database(database_path, manifest, match_payloads):
    database_path = Path(database_path)
    database_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = database_path.with_suffix(".sqlite3.tmp")
    temporary_path.unlink(missing_ok=True)

    with sqlite3.connect(temporary_path) as connection:
        connection.executescript(
            """
            PRAGMA journal_mode = OFF;
            PRAGMA synchronous = OFF;
            PRAGMA temp_store = MEMORY;
            CREATE TABLE metadata (
                key TEXT PRIMARY KEY,
                payload TEXT NOT NULL
            );
            CREATE TABLE matches (
                match_id INTEGER PRIMARY KEY,
                payload BLOB NOT NULL,
                compressed_size INTEGER NOT NULL,
                uncompressed_size INTEGER NOT NULL
            );
            """
        )
        connection.execute(
            "INSERT INTO metadata (key, payload) VALUES ('manifest', ?)",
            (
                json.dumps(
                    manifest,
                    ensure_ascii=False,
                    separators=(",", ":"),
                ),
            ),
        )
        for match_id, payload in match_payloads.items():
            raw_payload = json.dumps(
                payload,
                ensure_ascii=False,
                separators=(",", ":"),
            ).encode("utf-8")
            compressed_payload = zlib.compress(raw_payload, level=9)
            connection.execute(
                """
                INSERT INTO matches (
                    match_id,
                    payload,
                    compressed_size,
                    uncompressed_size
                ) VALUES (?, ?, ?, ?)
                """,
                (
                    int(match_id),
                    compressed_payload,
                    len(compressed_payload),
                    len(raw_payload),
                ),
            )
        connection.execute(
            "INSERT INTO metadata (key, payload) VALUES ('format_version', '1')"
        )
        connection.commit()
        connection.execute("VACUUM")

    os.replace(temporary_path, database_path)
    clear_loader_caches()
    return database_path


def build_compact_database_from_artifacts(database_path=None):
    manifest = load_manifest_from_artifacts()
    payloads = {
        int(match["match_id"]): load_match_payload_from_artifacts(
            match["match_id"]
        )
        for match in manifest
    }
    return write_compact_database(
        database_path or DEFAULT_DATABASE_PATH,
        manifest,
        payloads,
    )
