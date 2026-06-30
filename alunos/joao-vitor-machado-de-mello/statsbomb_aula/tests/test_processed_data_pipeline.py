import json
import importlib.util
import sqlite3
import tempfile
import unittest
import zlib
from pathlib import Path
from unittest import mock

from app.services import dashboard_builder
from app.services import processed_data


class ProcessedDataPipelineTest(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.processed_dir = Path(self.temp_dir.name)
        self.match_id = 123
        self.match_dir = self.processed_dir / "matches" / str(self.match_id)
        self.match_dir.mkdir(parents=True)
        (self.processed_dir / "manifest.json").write_text(
            json.dumps(
                [
                    {
                        "match_id": self.match_id,
                        "date": "2022-11-21",
                        "stage": "Group Stage",
                        "home_team": "England",
                        "away_team": "Iran",
                        "home_score": 6,
                        "away_score": 2,
                        "display_name": "England 6-2 Iran",
                    }
                ]
            ),
            encoding="utf-8",
        )
        payloads = {
            "match_summary.json": {"score": "6 - 2"},
            "team_metrics.json": {"home": {}, "away": {}, "period_metrics": {}},
            "player_metrics.json": [],
            "player_radars.json": [],
            "player_comparison.json": [],
            "shot_map.json": {"shots": [], "passes": [], "penalties": []},
            "xg_flow.json": {"home": {}, "away": {}},
            "momentum.json": {"buckets": [], "series": {}},
            "tactical_insights.json": {"notes": [], "top_impacts": []},
            "player_action_maps.json": [],
            "pressure_maps.json": [],
        }
        for name, payload in payloads.items():
            (self.match_dir / name).write_text(
                json.dumps(payload),
                encoding="utf-8",
            )
        processed_data.configure_processed_dir(self.processed_dir)

    def tearDown(self):
        processed_data.configure_database_path(None)
        processed_data.configure_processed_dir(None)
        self.temp_dir.cleanup()

    def test_manifest_and_match_loaders_are_cached(self):
        first_manifest = processed_data.load_manifest()
        second_manifest = processed_data.load_manifest()
        first_summary = processed_data.load_match_summary(self.match_id)
        second_summary = processed_data.load_match_summary(self.match_id)

        self.assertIs(first_manifest, second_manifest)
        self.assertIs(first_summary, second_summary)
        self.assertEqual(self.match_id, first_manifest[0]["match_id"])

    def test_match_payload_is_assembled_from_processed_artifacts(self):
        payload = processed_data.load_match_payload(self.match_id)

        self.assertEqual(self.match_id, payload["match_id"])
        self.assertEqual("6 - 2", payload["summary"]["score"])
        self.assertIn("player_actions", payload["events"])
        self.assertIn("momentum", payload["charts"])

    def test_api_source_uses_only_processed_match_loader(self):
        routes_path = (
            Path(__file__).resolve().parents[1]
            / "app"
            / "api"
            / "routes.py"
        )
        source = routes_path.read_text(encoding="utf-8")

        self.assertIn("processed_data.load_match_payload(match_id)", source)
        self.assertNotIn("calculate_advanced_metrics(", source)
        self.assertNotIn("get_match_events(", source)

    def test_frontend_schedules_secondary_renders(self):
        template_path = (
            Path(__file__).resolve().parents[1]
            / "app"
            / "templates"
            / "index.html"
        )
        source = template_path.read_text(encoding="utf-8")

        self.assertIn("scheduleSecondaryRenders", source)
        self.assertIn("requestIdleCallback", source)

    def test_penalty_map_does_not_invent_a_default_destination(self):
        template_path = (
            Path(__file__).resolve().parents[1]
            / "app"
            / "templates"
            / "index.html"
        )
        source = template_path.read_text(encoding="utf-8")

        self.assertIn(
            "if (event.end_y == null || event.end_z == null)",
            source,
        )
        self.assertNotIn("Number(event.end_y || 40)", source)
        self.assertIn("penaltyDestination(event.end_y)", source)

    def test_compact_database_loaders_preserve_runtime_contract(self):
        database_path = self.processed_dir / "dashboard.sqlite3"
        manifest = [{"match_id": self.match_id, "display_name": "England 6-2 Iran"}]
        payload = {
            "match_id": self.match_id,
            "summary": {"score": "6 - 2"},
            "events": {"shots": [], "passes": [], "penalties": [], "player_actions": []},
            "charts": {"xg_flow": {}, "momentum": {}},
            "images": {"pressure_maps": []},
        }
        processed_data.write_compact_database(
            database_path,
            manifest,
            {self.match_id: payload},
        )
        processed_data.configure_database_path(database_path)

        first = processed_data.load_manifest()
        second = processed_data.load_manifest()
        loaded_payload = processed_data.load_match_payload(self.match_id)

        self.assertIs(first, second)
        self.assertEqual(manifest, first)
        self.assertEqual(payload, loaded_payload)

        with sqlite3.connect(database_path) as connection:
            stored = connection.execute(
                "SELECT compressed_size, uncompressed_size FROM matches"
            ).fetchone()
        self.assertLess(stored[0], stored[1])

    def test_compact_database_cache_refreshes_when_database_changes(self):
        database_path = self.processed_dir / "dashboard.sqlite3"
        manifest = [{"match_id": self.match_id, "display_name": "England 6-2 Iran"}]
        first_payload = {
            "match_id": self.match_id,
            "events": {"penalties": [{"end_y": None}]},
        }
        processed_data.write_compact_database(
            database_path,
            manifest,
            {self.match_id: first_payload},
        )
        processed_data.configure_database_path(database_path)

        self.assertIsNone(
            processed_data.load_match_payload(self.match_id)
            ["events"]["penalties"][0]["end_y"]
        )

        second_payload = {
            "match_id": self.match_id,
            "events": {"penalties": [{"end_y": 37.9}]},
        }
        raw_payload = json.dumps(
            second_payload,
            separators=(",", ":"),
        ).encode("utf-8")
        compressed_payload = zlib.compress(raw_payload, level=9)
        with sqlite3.connect(database_path) as connection:
            connection.execute(
                """
                UPDATE matches
                SET payload = ?, compressed_size = ?, uncompressed_size = ?
                WHERE match_id = ?
                """,
                (
                    compressed_payload,
                    len(compressed_payload),
                    len(raw_payload),
                    self.match_id,
                ),
            )
            connection.commit()

        self.assertEqual(
            37.9,
            processed_data.load_match_payload(self.match_id)
            ["events"]["penalties"][0]["end_y"],
        )

    @unittest.skipUnless(
        importlib.util.find_spec("pyarrow"),
        "pyarrow is required for the Parquet storage contract",
    )
    def test_parquet_table_round_trip_restores_nested_values(self):
        rows = [
            {
                "match_id": 123,
                "minute": 12,
                "second": 7,
                "xg": 0.42,
                "player": "Test Player",
                "nested": {"score": 86, "labels": ["A", "B"]},
            }
        ]
        base_path = self.match_dir / "nested_table"

        written = dashboard_builder.write_table(base_path, rows)
        loaded = processed_data._load_table(str(base_path))

        self.assertEqual(".parquet", written.suffix)
        self.assertFalse(base_path.with_suffix(".json").exists())
        self.assertEqual(rows[0]["nested"], loaded[0]["nested"])
        self.assertEqual(123, loaded[0]["match_id"])
        self.assertAlmostEqual(0.42, loaded[0]["xg"], places=5)

        import pyarrow.parquet as parquet

        metadata = parquet.read_metadata(written)
        self.assertEqual("ZSTD", metadata.row_group(0).column(0).compression)

    def test_table_encoding_preserves_columns_that_only_exist_in_later_rows(self):
        rows = [
            {
                "record_type": "shot",
                "player": "Jogador A",
                "xg": 0.35,
            },
            {
                "record_type": "penalty",
                "player": "Jogador B",
                "end_y": 37.9,
                "end_z": 0.2,
                "scored": True,
                "attempt_number": 4,
            },
        ]
        loaded, _ = dashboard_builder._encode_nested_columns(rows)

        self.assertIsNone(loaded[0]["end_y"])
        self.assertAlmostEqual(37.9, loaded[1]["end_y"], places=5)
        self.assertAlmostEqual(0.2, loaded[1]["end_z"], places=5)
        self.assertTrue(loaded[1]["scored"])
        self.assertEqual(4, loaded[1]["attempt_number"])

    def test_large_artifacts_are_declared_as_parquet_tables(self):
        expected = {
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

        self.assertTrue(expected.issubset(dashboard_builder.TABLE_ARTIFACTS))
        self.assertNotIn(
            "player_comparison.json",
            dashboard_builder.MATCH_JSON_ARTIFACTS,
        )

    def test_player_comparison_reuses_canonical_player_metrics(self):
        canonical = [{"player": "A", "metric_layers": {"xg": {"raw_value": 1}}}]
        with mock.patch.object(
            processed_data,
            "load_player_metrics",
            return_value=canonical,
        ):
            self.assertIs(
                canonical,
                processed_data.load_player_comparison(self.match_id),
            )


if __name__ == "__main__":
    unittest.main()
