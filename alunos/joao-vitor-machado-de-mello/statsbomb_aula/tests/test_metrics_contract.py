import unittest
from pathlib import Path

from app.services import statsbomb_parser


class AdvancedMetricsContractTest(unittest.TestCase):
    def setUp(self):
        matches = statsbomb_parser.get_matches()
        if not matches:
            self.skipTest(
                "Raw StatsBomb fixtures are optional in the compact runtime."
            )
        self.match = matches[0]
        self.events = statsbomb_parser.get_match_events(self.match["match_id"])
        if not self.events:
            self.skipTest(
                "Raw StatsBomb events are optional in the compact runtime."
            )

    def test_desafio_2_team_metrics_are_exposed(self):
        metrics = statsbomb_parser.calculate_advanced_metrics(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
        )

        for side in ["home", "away"]:
            self.assertIn("xa", metrics[side])
            self.assertIn("shots", metrics[side])
            self.assertIn("shots_on_target", metrics[side])
            self.assertIn("shot_accuracy", metrics[side])
            self.assertIn("passes", metrics[side])
            self.assertIn("completed_passes", metrics[side])
            self.assertIn("pass_accuracy", metrics[side])
            self.assertIn("successful_dribbles", metrics[side])
            self.assertIn("dribble_accuracy", metrics[side])
            self.assertIn("successful_tackles", metrics[side])
            self.assertIn("tackle_accuracy", metrics[side])
            self.assertIn("progressive_passes", metrics[side])
            self.assertIn("progressive_carries", metrics[side])
            self.assertIn("counterpressures", metrics[side])
            self.assertIn("ppda", metrics[side])
            self.assertGreaterEqual(metrics[side]["xa"], 0)
            self.assertGreaterEqual(metrics[side]["progressive_passes"], 0)

    def test_expanded_volume_and_efficiency_metrics_are_exposed(self):
        metrics = statsbomb_parser.calculate_advanced_metrics(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
        )
        player = metrics["player_comparison"][0]

        expected = {
            "pass_accuracy", "passes_into_final_third", "passes_into_box",
            "crosses", "completed_crosses", "shot_assists", "cutbacks",
            "through_balls", "xg_per_shot", "shot_conversion",
            "counterpressures", "counterpress_percentage", "pressures_final_third",
            "tackles", "duels", "duels_won", "aerial_duels",
            "aerial_duels_won", "fouls_committed", "fouls_won", "cards",
        }
        self.assertTrue(expected.issubset(player))
        self.assertIn("comparison_categories", player)
        self.assertIn("efficiency_radar", player)
        self.assertIn("efficiency_volumes", player)
        self.assertEqual(
            {"Passe", "Progressão", "Criação", "Finalização", "Pressão", "Defesa", "Disciplina"},
            set(player["comparison_categories"]),
        )

    def test_percentage_helper_preserves_volume_and_zero_denominator(self):
        self.assertIsNone(statsbomb_parser.safe_percentage(0, 0))
        self.assertEqual(75.0, statsbomb_parser.safe_percentage(15, 20))
        self.assertEqual("75% (15/20)", statsbomb_parser.format_efficiency(15, 20))
        self.assertEqual("N/D (0/0)", statsbomb_parser.format_efficiency(0, 0))

    def test_player_actions_momentum_and_top_impacts_are_available(self):
        actions = statsbomb_parser.build_player_action_events(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
        )
        momentum = statsbomb_parser.build_match_momentum(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
        )
        metrics = statsbomb_parser.calculate_advanced_metrics(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
        )
        self.assertTrue(actions)
        self.assertTrue({"event_type", "player", "x", "y"}.issubset(actions[0]))
        self.assertTrue(momentum["buckets"])
        self.assertEqual(
            {"xg", "pressure", "progression", "shots"},
            set(momentum["series"]),
        )
        self.assertTrue(metrics["top_impacts"])
        self.assertIn("reason", metrics["top_impacts"][0])

    def test_player_radars_are_normalized(self):
        metrics = statsbomb_parser.calculate_advanced_metrics(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
        )

        self.assertTrue(metrics["player_radars"])
        for player in metrics["player_radars"]:
            self.assertIn("impact_score", player)
            self.assertIn("metrics", player)
            self.assertIn("position_average_radar", player)
            self.assertIn("per90", player)
            for value in player["radar"].values():
                self.assertGreaterEqual(value, 0)
                self.assertLessEqual(value, 100)

    def test_radar_reference_uses_tournament_position_average(self):
        metric_keys = set(statsbomb_parser.PLAYER_PER90_KEYS) | {
            "total_progression_distance"
        }
        reference = {
            "Volante/Meio-campista": {
                "players": 42,
                "metrics": {
                    key: {"p05": 0, "p95": 10, "mean_per90": 5}
                    for key in metric_keys
                },
                "dimension_average_scores": {
                    key: 50 for key in statsbomb_parser.LINE_DIMENSION_LABELS
                },
            }
        }
        metrics = statsbomb_parser.calculate_advanced_metrics(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
            tournament_reference=reference,
        )
        player = next(
            item for item in metrics["player_comparison"]
            if item["macro_position"] == "Volante/Meio-campista"
        )

        self.assertEqual("tournament_macroposition_p05_p95", player["radar_reference_scope"])
        self.assertEqual(42, player["radar_reference_players"])
        self.assertTrue(
            all(value == 50 for value in player["position_average_radar"].values())
        )

    def test_radars_do_not_depend_on_raw_match_maximum(self):
        metrics = statsbomb_parser.calculate_advanced_metrics(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
        )
        player = metrics["player_comparison"][0]
        self.assertEqual(
            "tournament_macroposition_p05_p95",
            player["radar_reference_scope"],
        )
        self.assertTrue(
            all(0 <= normalized <= 100 for normalized in player["radar"].values())
        )

    def test_macroposition_contextual_scores_and_layers_are_exposed(self):
        reference = statsbomb_parser.build_tournament_macroposition_reference(
            match_ids=[self.match["match_id"]]
        )
        lineups = statsbomb_parser.get_match_lineups(self.match["match_id"])
        positions = statsbomb_parser.build_player_positions(self.events, lineups)
        minutes = statsbomb_parser.build_player_minutes(lineups, self.events)
        metrics = statsbomb_parser.calculate_advanced_metrics(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
            positions,
            minutes,
            reference,
        )

        player = metrics["player_comparison"][0]
        self.assertIn(player["macro_position"], statsbomb_parser.MACRO_POSITIONS)
        self.assertIn("metric_layers", player)
        self.assertIn("dimension_scores", player)
        self.assertIn("dimension_average_scores", player)
        self.assertIn("influence_index", player)
        self.assertIn("influence_delta_pct", player)
        self.assertIn("eligible_for_radar", player)
        for layer in player["metric_layers"].values():
            self.assertEqual(
                {
                    "raw_value",
                    "per90_value",
                    "percentage_value",
                    "volume_denominator",
                    "score_0_100",
                    "position_average_per90",
                    "position_average_score_0_100",
                    "difference_vs_position_average",
                    "percentile_or_rank",
                },
                set(layer),
            )
            self.assertGreaterEqual(layer["score_0_100"], 0)
            self.assertLessEqual(layer["score_0_100"], 100)
        for score in player["dimension_scores"].values():
            self.assertGreaterEqual(score, 0)
            self.assertLessEqual(score, 100)

    def test_contextual_score_formula_and_macroposition_mapping(self):
        self.assertEqual(50, statsbomb_parser.contextual_score(10, 5, 5))
        self.assertEqual(0, statsbomb_parser.contextual_score(2, 5, 15))
        self.assertEqual(50, statsbomb_parser.contextual_score(10, 5, 15))
        self.assertEqual(100, statsbomb_parser.contextual_score(20, 5, 15))
        self.assertEqual("Zagueiro", statsbomb_parser.macro_position_for("Right Center Back"))
        self.assertEqual("Lateral/Ala", statsbomb_parser.macro_position_for("Left Wing Back"))
        self.assertEqual("Meia ofensivo/Ponta", statsbomb_parser.macro_position_for("Right Wing"))
        self.assertEqual("Centroavante", statsbomb_parser.macro_position_for("Center Forward"))

    def test_tournament_reference_aggregates_all_matches_by_macroposition(self):
        reference = statsbomb_parser.build_tournament_macroposition_reference(
            match_ids=[self.match["match_id"]]
        )

        self.assertTrue(reference)
        for group, values in reference.items():
            self.assertIn(group, statsbomb_parser.MACRO_POSITIONS)
            self.assertGreater(values["players"], 0)
            self.assertIn("minutes", values)
            self.assertIn("metrics", values)
            self.assertIn("dimension_average_scores", values)
            for metric in values["metrics"].values():
                self.assertEqual(
                    {"p05", "p95", "mean_per90"},
                    set(metric),
                )

    def test_player_minutes_per90_and_progression_distance_are_exposed(self):
        lineups = statsbomb_parser.get_match_lineups(self.match["match_id"])
        positions = statsbomb_parser.build_player_positions(self.events, lineups)
        minutes = statsbomb_parser.build_player_minutes(lineups, self.events)
        metrics = statsbomb_parser.calculate_advanced_metrics(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
            positions,
            minutes,
        )

        self.assertTrue(minutes)
        self.assertTrue(any(0 < value <= 130 for value in minutes.values()))
        players = metrics["player_comparison"]
        self.assertTrue(players)
        self.assertTrue(any(player["minutes"] > 0 for player in players))
        self.assertTrue(any(player["total_progression_distance"] > 0 for player in players))
        for player in players:
            self.assertIn("per90", player)
            self.assertIn("progressive_pass_distance", player)
            self.assertIn("progressive_carry_distance", player)
            self.assertIn("total_progression_distance", player)
            self.assertIn("position_average_radar", player)

    def test_player_radars_include_nine_highlights_when_available(self):
        england_match = next(match for match in statsbomb_parser.get_matches() if match["match_id"] == 3857271)
        metrics = statsbomb_parser.calculate_advanced_metrics(
            statsbomb_parser.get_match_events(england_match["match_id"]),
            england_match["home_team"],
            england_match["away_team"],
        )

        self.assertGreaterEqual(len(metrics["player_comparison"]), 9)
        self.assertEqual(9, len(metrics["player_radars"]))
        self.assertEqual(9, len({player["player"] for player in metrics["player_radars"]}))

    def test_display_matches_include_translation_flags_and_score_label(self):
        matches = statsbomb_parser.get_display_matches()
        first = matches[0]

        self.assertIn("display_label", first)
        self.assertIn("match_date_display", first)
        self.assertIn("home_flag", first)
        self.assertIn("away_flag", first)
        self.assertIn("home_flag_url", first)
        self.assertTrue(first["home_flag_url"].endswith(".svg"))
        self.assertRegex(first["match_date_display"], r"^\d{2}/\d{2}/\d{4}$")
        self.assertEqual("Fase de Grupos", first["competition_stage"])
        sort_keys = [match["sort_key"] for match in matches]
        self.assertEqual(sort_keys, sorted(sort_keys))

    def test_interactive_events_include_tooltip_contract(self):
        events = statsbomb_parser.build_interactive_events(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
        )

        self.assertTrue(events["shots"])
        self.assertTrue(events["passes"])

        shot = events["shots"][0]
        pass_event = events["passes"][0]
        for item in [shot, pass_event]:
            self.assertIn("team", item)
            self.assertIn("flag", item)
            self.assertIn("flag_url", item)
            self.assertIn("player", item)
            self.assertIn("period", item)
            self.assertIn("minute_label", item)
            self.assertIn("result", item)
            self.assertIn("tooltip", item)
        self.assertIn("is_goal", shot)

    def test_period_metrics_and_player_comparison_are_available(self):
        period_metrics = statsbomb_parser.calculate_period_metrics(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
        )
        full_metrics = statsbomb_parser.calculate_advanced_metrics(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
        )

        self.assertEqual({"all", "1", "2"}, set(period_metrics.keys()))
        self.assertIn("shots", period_metrics["1"]["home"])
        self.assertTrue(full_metrics["player_comparison"])
        self.assertIn("total_progression", full_metrics["player_comparison"][0])
        self.assertIn("team_flag_url", full_metrics["player_comparison"][0])
        self.assertIn("team_flag_code", full_metrics["player_comparison"][0])
        self.assertIn("radar", full_metrics["player_comparison"][0])
        self.assertIn("shots_on_target", full_metrics["player_comparison"][0])
        self.assertIn("successful_dribbles", full_metrics["player_comparison"][0])
        self.assertIn("successful_tackles", full_metrics["player_comparison"][0])

    def test_goal_events_are_grouped_by_team_with_minutes(self):
        goal_match = next(
            match for match in statsbomb_parser.get_matches()
            if (match.get("home_score", 0) + match.get("away_score", 0)) > 0
        )
        events = statsbomb_parser.get_match_events(goal_match["match_id"])
        goals = statsbomb_parser.build_goal_events(
            events,
            goal_match["home_team"],
            goal_match["away_team"],
        )

        self.assertEqual({"home", "away"}, set(goals.keys()))
        self.assertTrue(goals["home"] or goals["away"])
        first_goal = (goals["home"] + goals["away"])[0]
        self.assertIn("player", first_goal)
        self.assertIn("minute_label", first_goal)
        self.assertTrue(first_goal["minute_label"].endswith("'"))

    def test_goal_events_can_be_grouped_by_player(self):
        goal_match = next(
            match for match in statsbomb_parser.get_matches()
            if match.get("match_id") == 3857271
        )
        events = statsbomb_parser.get_match_events(goal_match["match_id"])
        grouped = statsbomb_parser.build_grouped_goal_events(
            events,
            goal_match["home_team"],
            goal_match["away_team"],
        )

        saka = next(goal for goal in grouped["home"] if goal["player"] == "Bukayo Saka")
        taremi = next(goal for goal in grouped["away"] if goal["player"] == "Mehdi Taremi")
        self.assertEqual(2, saka["goals"])
        self.assertEqual(2, taremi["goals"])
        self.assertEqual(["42'", "61'"], saka["minute_labels"])
        self.assertEqual(["64'", "90+12'"], taremi["minute_labels"])

    def test_real_flag_assets_are_available_locally(self):
        flag_path = Path(__file__).resolve().parents[1] / "app" / "static" / "flags" / "irn.svg"
        self.assertTrue(flag_path.exists())
        content = flag_path.read_text(encoding="utf-8")
        self.assertIn("<svg", content)
        self.assertGreater(flag_path.stat().st_size, 1000)

    def test_penalty_shootout_is_separate_from_match_goals_and_xg(self):
        final = next(match for match in statsbomb_parser.get_matches() if match["match_id"] == 3869685)
        events = statsbomb_parser.get_match_events(final["match_id"])
        match_events = statsbomb_parser.exclude_penalty_shootout(events)
        shootout = statsbomb_parser.build_penalty_shootout(
            events,
            final["home_team"],
            final["away_team"],
        )
        goals = statsbomb_parser.build_goal_events(
            match_events,
            final["home_team"],
            final["away_team"],
        )
        metrics = statsbomb_parser.calculate_advanced_metrics(
            match_events,
            final["home_team"],
            final["away_team"],
        )

        self.assertTrue(shootout["occurred"])
        self.assertEqual(4, shootout["home_score"])
        self.assertEqual(2, shootout["away_score"])
        self.assertEqual(3, len(goals["home"]))
        self.assertEqual(3, len(goals["away"]))
        self.assertNotIn(5, {event.get("period") for event in match_events})
        self.assertLess(metrics["home"]["xg"], 4)
        self.assertLess(metrics["away"]["xg"], 4)

    def test_players_receive_position_specific_radar_profiles(self):
        england_match = next(match for match in statsbomb_parser.get_matches() if match["match_id"] == 3857271)
        events = statsbomb_parser.get_match_events(england_match["match_id"])
        lineups = statsbomb_parser.get_match_lineups(england_match["match_id"])
        positions = statsbomb_parser.build_player_positions(events, lineups)
        metrics = statsbomb_parser.calculate_advanced_metrics(
            events,
            england_match["home_team"],
            england_match["away_team"],
            positions,
        )

        stones = next(player for player in metrics["player_comparison"] if player["player"] == "John Stones")
        pickford = next(player for player in metrics["player_comparison"] if player["player"] == "Jordan Pickford")

        self.assertEqual("Defensor", stones["position_group"])
        self.assertEqual("Zagueiro", stones["macro_position"])
        self.assertEqual(
            set(statsbomb_parser.LINE_DIMENSION_LABELS),
            set(stones["radar"]),
        )
        self.assertEqual("Goleiro", pickford["position_group"])
        self.assertEqual(
            set(statsbomb_parser.GOALKEEPER_DIMENSION_LABELS),
            set(pickford["radar"]),
        )

    def test_display_match_includes_penalty_score_when_available(self):
        final = next(match for match in statsbomb_parser.get_display_matches() if match["match_id"] == 3869685)

        self.assertTrue(final["penalty_shootout"]["occurred"])
        self.assertEqual("Argentina (4) 3-3 (2) França", final["display_label"])

    def test_penalty_attempts_include_goal_destination(self):
        final = next(match for match in statsbomb_parser.get_matches() if match["match_id"] == 3869685)
        events = statsbomb_parser.get_match_events(final["match_id"])
        shootout = statsbomb_parser.build_penalty_shootout(
            events,
            final["home_team"],
            final["away_team"],
        )
        attempt = shootout["home_attempts"][0]

        self.assertIn("team", attempt)
        self.assertIn("end_y", attempt)
        self.assertIn("end_z", attempt)
        self.assertIn("flag_url", attempt)

    def test_similar_team_colors_use_secondary_away_color(self):
        home = statsbomb_parser.get_team_display("United States")
        away = statsbomb_parser.get_team_display("Wales")
        colors = statsbomb_parser.resolve_match_colors(home, away)

        self.assertEqual(home["primary_color"], colors["home"])
        self.assertEqual(away["secondary_color"], colors["away"])

    def test_secondary_team_color_is_distinct_or_falls_back_to_white(self):
        morocco = statsbomb_parser.get_team_display("Morocco")
        spain = statsbomb_parser.get_team_display("Spain")
        match_colors = statsbomb_parser.resolve_match_colors(morocco, spain)

        self.assertEqual("#c1272d", morocco["primary_color"])
        self.assertEqual("#006233", morocco["secondary_color"])
        self.assertEqual("#aa151b", spain["primary_color"])
        self.assertEqual("#f1bf00", spain["secondary_color"])
        self.assertEqual("#f1bf00", match_colors["away"])
        self.assertEqual(
            ("#123456", "#ffffff"),
            statsbomb_parser._accent_colors(["#123456", "#123456"]),
        )

    def test_requested_team_color_palettes_are_applied(self):
        expected = {
            "Netherlands": ("#f36c21", "#102a43"),
            "Japan": ("#001f5b", "#ffffff"),
            "England": ("#ffffff", "#ce1124"),
            "Iran": ("#ffffff", "#da0000"),
            "Australia": ("#ffcd00", "#00843d"),
            "Croatia": ("#ffffff", "#ff0000"),
            "Germany": ("#ffffff", "#000000"),
        }

        for team, colors in expected.items():
            display = statsbomb_parser.get_team_display(team)
            self.assertEqual(colors, (
                display["primary_color"],
                display["secondary_color"],
            ))

    def test_momentum_controls_have_compact_layout_contract(self):
        template_path = (
            Path(__file__).resolve().parents[1]
            / "app"
            / "templates"
            / "index.html"
        )
        content = template_path.read_text(encoding="utf-8")

        self.assertIn("grid-template-rows: auto auto minmax(0, 1fr)", content)
        self.assertIn(".momentum-controls .flag-toggle", content)
        self.assertIn("min-height: 32px", content)

    def test_match_metric_naming_and_hierarchy_contract(self):
        template_path = (
            Path(__file__).resolve().parents[1]
            / "app"
            / "templates"
            / "index.html"
        )
        content = template_path.read_text(encoding="utf-8")

        self.assertIn("Métricas da partida", content)
        self.assertIn("Valores calculados somente com base neste jogo", content)
        self.assertNotIn("Métricas por 90 minutos", content)
        self.assertNotIn("Média por 90 da macroposição", content)
        self.assertNotIn("<th>Por 90</th>", content)
        self.assertIn('value="30" selected', content)
        self.assertIn("Amostra pequena", content)
        self.assertIn("Perfil contextual", content)
        self.assertIn("Média da macroposição na Copa", content)
        self.assertIn("Círculo = chute", content)
        self.assertIn("Blocos de 5 minutos", content)
        self.assertIn("comparison-category-tab", content)

    def test_pass_events_expose_completion_and_keep_statsbomb_coordinates(self):
        raw_pass = next(
            event for event in self.events
            if event.get("type") == "Pass"
            and statsbomb_parser._in_pitch(event.get("location"))
            and statsbomb_parser._in_pitch(event.get("pass_end_location"))
        )
        interactive = statsbomb_parser.build_interactive_events(
            self.events,
            self.match["home_team"],
            self.match["away_team"],
        )
        rendered_pass = next(event for event in interactive["passes"] if event["id"] == raw_pass["id"])

        self.assertEqual(not bool(raw_pass.get("pass_outcome")), rendered_pass["completed"])
        self.assertEqual(raw_pass["location"][0], rendered_pass["x"])
        self.assertEqual(raw_pass["location"][1], rendered_pass["y"])
        self.assertEqual(raw_pass["pass_end_location"][0], rendered_pass["end_x"])
        self.assertEqual(raw_pass["pass_end_location"][1], rendered_pass["end_y"])

    def test_template_uses_statsbomb_pitch_pass_colors_and_player_filter_for_both_maps(self):
        template_path = Path(__file__).resolve().parents[1] / "app" / "templates" / "index.html"
        content = template_path.read_text(encoding="utf-8")

        self.assertIn('id="event-player-controls"', content)
        self.assertIn('id="event-player-select"', content)
        self.assertIn("['shots', 'passes'].includes(state.mapMode)", content)
        self.assertIn("const PASS_COMPLETE_COLOR = '#22c55e'", content)
        self.assertIn("const PASS_INCOMPLETE_COLOR = '#ef4444'", content)
        self.assertIn('x="0" y="18" width="18" height="44"', content)
        self.assertIn('x="102" y="18" width="18" height="44"', content)

    def test_pass_filter_arrows_and_radar_tooltips_follow_interaction_contract(self):
        template_path = Path(__file__).resolve().parents[1] / "app" / "templates" / "index.html"
        content = template_path.read_text(encoding="utf-8")

        self.assertIn("state.mapMode === 'shots'", content)
        self.assertIn("state.mapMode === 'passes'", content)
        self.assertIn("Todos os jogadores", content)
        self.assertIn("players[0]", content)
        self.assertIn('marker-end="url(#pass-arrow-', content)
        self.assertIn('class="radar-chart-wrap"', content)
        self.assertIn('class="chart-tooltip radar-tooltip"', content)
        self.assertIn('data-radar-point', content)
        self.assertIn('tabindex="0"', content)
        self.assertIn("bindRadarInteractions", content)

    def test_penalty_events_include_regular_time_and_shootout_attempts(self):
        regular_match = next(match for match in statsbomb_parser.get_matches() if match["match_id"] == 3857271)
        regular_events = statsbomb_parser.build_penalty_events(
            statsbomb_parser.get_match_events(regular_match["match_id"]),
            regular_match["home_team"],
            regular_match["away_team"],
        )
        final = next(match for match in statsbomb_parser.get_matches() if match["match_id"] == 3869685)
        final_events = statsbomb_parser.build_penalty_events(
            statsbomb_parser.get_match_events(final["match_id"]),
            final["home_team"],
            final["away_team"],
        )

        self.assertTrue(any(not attempt["shootout"] for attempt in regular_events))
        self.assertTrue(any(attempt["shootout"] for attempt in final_events))
        self.assertTrue(all(attempt["shot_type"] == "Penalty" for attempt in regular_events))
        self.assertIn("90+", regular_events[0]["minute_label"])

    def test_helpers_modal_and_accented_interface_are_present(self):
        template_path = Path(__file__).resolve().parents[1] / "app" / "templates" / "index.html"
        content = template_path.read_text(encoding="utf-8")

        self.assertIn('id="expand-map"', content)
        self.assertIn('id="map-modal"', content)
        self.assertIn('role="dialog"', content)
        self.assertIn('aria-modal="true"', content)
        self.assertIn("influenceExplanation", content)
        self.assertIn('title="${fullLabel}"', content)
        self.assertIn("openMapModal", content)
        self.assertIn("event.key === 'Escape'", content)
        self.assertIn("Visão geral da partida", content)
        self.assertIn("História do jogo", content)

    def test_dictionary_charts_modal_detail_and_persistent_selection_are_present(self):
        template_path = Path(__file__).resolve().parents[1] / "app" / "templates" / "index.html"
        content = template_path.read_text(encoding="utf-8")

        self.assertIn('id="map-modal-helper"', content)
        self.assertIn("eventHelperMarkup", content)
        self.assertIn("bindMapEventInteractions", content)
        self.assertIn("renderInteractiveMap();", content)
        self.assertIn("pass-selection-outline", content)
        self.assertNotIn("drop-shadow(0 0 3px rgba(255, 248, 234, 0.92))", content)
        self.assertIn('viewBox="${expanded ? \'0 0 80 40\' : \'0 0 120 80\'}"', content)
        self.assertIn('matrix(0 -1 1 0 0 120)', content)
        self.assertIn('id="playmaker-chart"', content)
        self.assertIn('id="progression-chart"', content)
        self.assertIn('id="defensive-intensity-chart"', content)
        self.assertIn('id="per90-table"', content)
        self.assertIn("total_progression_distance", content)
        self.assertIn("position_average_radar", content)
        self.assertIn("renderDictionaryCharts", content)
        self.assertIn("radarMetricChip", content)
        self.assertNotIn("metricHelp(fullLabel)", content)
        self.assertNotIn("Aplicações do dicionário de dados", content)
        self.assertNotIn("A. Construtores de jogo", content)
        self.assertNotIn("B. Intensidade defensiva", content)
        self.assertNotIn("C. Progressões dos jogadores", content)
        self.assertIn("Distância percorrida em progressão", content)
        self.assertIn("ppdaValue / maxPpda", content)
        self.assertIn("renderPer90Table", content)
        self.assertIn("data-per90-sort", content)
        self.assertIn("per90Sort", content)
        self.assertIn("${team.counterpress} counterpress · PPDA", content)
        self.assertIn("Mapa de pressão por equipe", content)
        self.assertIn("Maior intensidade de cor", content)
        self.assertIn("pressure_maps", content)
        self.assertIn("state.mapMode === 'shots' && expanded", content)
        self.assertNotIn("passPitchSvg(events, markerSuffix, expanded)", content)
        plotter_content = (Path(__file__).resolve().parents[1] / "app" / "services" / "plotter.py").read_text(encoding="utf-8")
        self.assertNotIn("Direção do ataque", plotter_content)
        self.assertIn("data-chart-metric", content)
        self.assertIn("bindChartMetricHelpers", content)
        self.assertIn('id="comparison-modal"', content)
        self.assertIn('id="player-modal"', content)
        self.assertIn('id="expand-comparison"', content)
        self.assertNotIn("general_radar", content)
        self.assertIn("openPlayerModal", content)
        self.assertIn("data-player-detail", content)
        self.assertIn('data-per90-sort="team"', content)
        self.assertIn("<th><button class=\"per90-sort\" data-per90-sort=\"team\">Time</button></th>", content)
        self.assertIn("player.metrics || {}", content)
        self.assertNotIn(".map(([key, value]) => radarMetricChip(key, value, player.metric_labels || {}, true))", content)
        self.assertIn('id="modal-compare-player-a"', content)
        self.assertIn('id="modal-compare-player-b"', content)
        self.assertIn("syncComparisonSelection", content)
        self.assertIn('data-chart-context="${summary.home_team', content)
        self.assertIn('data-chart-context="${player.player}"', content)
        image_index = content.index('alt="Mapa de pressão de ${map.team}"')
        direction_index = content.index("Direção do ataque →", image_index)
        self.assertGreater(direction_index, image_index)
        self.assertIn("raw_value", content)
        self.assertNotIn("<th>Por 90</th>", content)
        self.assertIn("score_0_100", content)
        self.assertIn("influence_index", content)
        self.assertIn("Math.round(player.influence_delta_pct)", content)
        self.assertIn("comparisonSummary", content)
        self.assertIn("Amostra pequena", content)
        self.assertIn("player.minutes >= 45", content)
        self.assertIn('data-shot-filter="goals"', content)
        self.assertIn('data-shot-filter="on_target"', content)
        self.assertIn('data-shot-filter="high_xg"', content)
        self.assertIn('id="top-impacts"', content)
        self.assertIn("renderTopImpacts", content)
        self.assertIn('id="player-table-team"', content)
        self.assertIn('id="player-table-macro"', content)
        self.assertIn("comparison_categories", content)
        self.assertIn("efficiency_radar", content)
        self.assertIn("playerActionMapMarkup", content)
        self.assertIn("data-player-action-filter", content)
        self.assertIn("data-momentum-mode", content)
        self.assertIn("renderMomentum", content)


if __name__ == "__main__":
    unittest.main()
