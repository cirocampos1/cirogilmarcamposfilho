import unittest
from pathlib import Path

from app.services import processed_data


class CompactPenaltyDestinationsTest(unittest.TestCase):
    def setUp(self):
        database_path = Path(__file__).resolve().parents[1] / "data" / "dashboard.sqlite3"
        if not database_path.exists():
            self.skipTest("Compact dashboard database is not available.")
        processed_data.configure_database_path(database_path)

    def tearDown(self):
        processed_data.configure_database_path(None)

    def test_world_cup_final_penalties_preserve_statsbomb_destinations(self):
        payload = processed_data.load_match_payload(3869685)
        penalties = payload["events"]["penalties"]

        self.assertEqual(11, len(penalties))
        self.assertTrue(all(attempt.get("end_y") is not None for attempt in penalties))
        self.assertTrue(all(attempt.get("end_z") is not None for attempt in penalties))

        montiel = next(
            attempt
            for attempt in penalties
            if attempt["player"] == "Gonzalo Ariel Montiel"
        )
        self.assertAlmostEqual(37.9, montiel["end_y"], places=1)
        self.assertAlmostEqual(0.2, montiel["end_z"], places=1)
        self.assertTrue(montiel["scored"])
        self.assertEqual(4, montiel["attempt_number"])

