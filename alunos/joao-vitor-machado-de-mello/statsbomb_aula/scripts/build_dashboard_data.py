import argparse
import logging
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from app.services import dashboard_builder
from app.services import processed_data
from app.services import statsbomb_parser


LOGGER = logging.getLogger("dashboard-data-build")
PROCESSED_DIR = BASE_DIR / "data" / "processed"
MATCHES_DIR = PROCESSED_DIR / "matches"
DATABASE_PATH = BASE_DIR / "data" / "dashboard.sqlite3"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Precompute dashboard artifacts from StatsBomb raw JSON files."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rebuild artifacts even when every expected file already exists.",
    )
    parser.add_argument(
        "--match-id",
        type=int,
        help="Rebuild only one match. The manifest remains global.",
    )
    parser.add_argument(
        "--pack-only",
        action="store_true",
        help="Create the compact runtime database from existing artifacts.",
    )
    return parser.parse_args()


def build(args):
    if args.pack_only:
        LOGGER.info("Packing existing artifacts into %s.", DATABASE_PATH)
        processed_data.build_compact_database_from_artifacts(DATABASE_PATH)
        LOGGER.info("Compact dashboard database completed.")
        return

    if not dashboard_builder.parquet_engine_available():
        raise RuntimeError(
            "pyarrow is required. Install project dependencies before building."
        )

    matches = statsbomb_parser.get_matches()
    if not matches:
        raise RuntimeError("No raw matches were found.")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    dashboard_builder.write_json(
        PROCESSED_DIR / "manifest.json",
        dashboard_builder.build_manifest(
            matches,
            display_matches=statsbomb_parser.get_display_matches(),
        ),
    )
    LOGGER.info("Manifest written with %s matches.", len(matches))

    reference_base_path = PROCESSED_DIR / "tournament_reference"
    reference_path = reference_base_path.with_suffix(".parquet")
    rebuild_reference = (
        not reference_path.exists()
        or (args.force and args.match_id is None)
    )
    if rebuild_reference:
        LOGGER.info("Building tournament reference from all matches.")
        macroposition_reference = (
            statsbomb_parser.build_tournament_macroposition_reference(
                match_ids=[match["match_id"] for match in matches]
            )
        )
        tournament_reference = {
            "_meta": {
                "score_formula": (
                    "clamp((per90_value - p05) / (p95 - p05) * 100, 0, 100)"
                ),
                "fallback_score": 50,
                "minimum_reference_minutes": (
                    statsbomb_parser.TOURNAMENT_REFERENCE_MINUTES
                ),
                "weighted_means": "raw_total / total_minutes * 90",
            },
            **macroposition_reference,
        }
        dashboard_builder.write_table(
            reference_base_path,
            [
                {
                    "macro_position": macro_position,
                    "reference": reference,
                }
                for macro_position, reference in tournament_reference.items()
            ],
        )
        for legacy_name in (
            "tournament_reference.json",
            "tournament_macroposition_reference.json",
            "tournament_position_reference.json",
        ):
            (PROCESSED_DIR / legacy_name).unlink(missing_ok=True)
    else:
        tournament_reference = processed_data.load_tournament_reference()
        LOGGER.info("Reusing existing tournament reference.")

    selected_matches = matches
    if args.match_id is not None:
        selected_matches = [
            match for match in matches
            if int(match["match_id"]) == args.match_id
        ]
        if not selected_matches:
            raise ValueError(f"Unknown match id: {args.match_id}")

    for index, match in enumerate(selected_matches, start=1):
        match_id = int(match["match_id"])
        match_dir = MATCHES_DIR / str(match_id)
        if (
            not args.force
            and dashboard_builder.match_artifacts_exist(match_dir)
        ):
            LOGGER.info(
                "[%s/%s] Match %s is already built; skipping.",
                index,
                len(selected_matches),
                match_id,
            )
            continue
        LOGGER.info(
            "[%s/%s] Building match %s: %s vs %s.",
            index,
            len(selected_matches),
            match_id,
            match["home_team"],
            match["away_team"],
        )
        artifacts = dashboard_builder.build_match_artifacts(
            match,
            tournament_reference,
        )
        dashboard_builder.write_match_artifacts(
            match_dir,
            artifacts,
        )
    if args.match_id is None:
        LOGGER.info("Packing runtime database into %s.", DATABASE_PATH)
        processed_data.build_compact_database_from_artifacts(DATABASE_PATH)
    LOGGER.info("Dashboard data build completed.")


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    build(parse_args())


if __name__ == "__main__":
    main()
