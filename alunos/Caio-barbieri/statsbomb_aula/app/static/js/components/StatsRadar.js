/**
 * CBF Academy - Statsbomb World Cup 2022
 * Component to render and update the performance radar chart using Chart.js
 */

export class StatsRadar {
    constructor(canvasId) {
        this.canvasId = canvasId;
        this.chart = null;
        
        // Colors from design system
        this.colors = {
            player1: {
                border: '#1A78CF',
                bg: 'rgba(26, 120, 207, 0.25)',
                point: '#60a5fa'
            },
            player2: {
                border: '#F1C40F',
                bg: 'rgba(241, 196, 15, 0.25)',
                point: '#fef08a'
            }
        };
    }

    /**
     * Update the radar chart with two players' stats
     * @param {Object} p1 Stats of player 1
     * @param {Object} p2 Stats of player 2
     * @param {Object} allPlayersStats Dictionary of all player stats for normalization
     */
    update(p1, p2, allPlayersStats) {
        const canvas = document.getElementById(this.canvasId);
        if (!canvas) return;

        // Extract and calculate metrics
        const getDefensiveActions = (p) => (p.tackles || 0) + (p.interceptions || 0) + (p.recoveries || 0);

        // Helper to calculate max value in match for normalization
        const getMetricMax = (metricFn) => {
            let max = 0.01; // Avoid division by zero
            Object.values(allPlayersStats).forEach(p => {
                const val = metricFn(p);
                if (val > max) max = val;
            });
            return max;
        };

        const maxMetrics = {
            xg: getMetricMax(p => p.xg || 0),
            xa: getMetricMax(p => p.xa || 0),
            progressive_passes: getMetricMax(p => p.progressive_passes || 0),
            passes_under_pressure: getMetricMax(p => p.passes_under_pressure_completed || 0),
            dribbles: getMetricMax(p => p.dribbles_completed || 0),
            defensive: getMetricMax(p => getDefensiveActions(p))
        };

        // Normalization function (returns 0-100)
        const normalize = (val, max) => Math.round((val / max) * 100);

        // Data for Player 1
        const p1Data = p1 ? [
            normalize(p1.xg || 0, maxMetrics.xg),
            normalize(p1.xa || 0, maxMetrics.xa),
            normalize(p1.progressive_passes || 0, maxMetrics.progressive_passes),
            normalize(p1.passes_under_pressure_completed || 0, maxMetrics.passes_under_pressure),
            normalize(p1.dribbles_completed || 0, maxMetrics.dribbles),
            normalize(getDefensiveActions(p1), maxMetrics.defensive)
        ] : [0, 0, 0, 0, 0, 0];

        // Data for Player 2
        const p2Data = p2 ? [
            normalize(p2.xg || 0, maxMetrics.xg),
            normalize(p2.xa || 0, maxMetrics.xa),
            normalize(p2.progressive_passes || 0, maxMetrics.progressive_passes),
            normalize(p2.passes_under_pressure_completed || 0, maxMetrics.passes_under_pressure),
            normalize(p2.dribbles_completed || 0, maxMetrics.dribbles),
            normalize(getDefensiveActions(p2), maxMetrics.defensive)
        ] : [0, 0, 0, 0, 0, 0];

        const labels = [
            `Expected Goals (Max: ${maxMetrics.xg.toFixed(2)})`,
            `Expected Assists (Max: ${maxMetrics.xa.toFixed(2)})`,
            `Passes Progressivos (Max: ${maxMetrics.progressive_passes})`,
            `Passes sob Pressão (Max: ${maxMetrics.passes_under_pressure})`,
            `Dribles Completados (Max: ${maxMetrics.dribbles})`,
            `Ações Defensivas (Max: ${maxMetrics.defensive})`
        ];

        // Update DOM labels & absolute values if elements exist
        this.updateAbsoluteStatsTable(p1, p2, getDefensiveActions);

        // Destroy previous chart instance if exists
        if (this.chart) {
            this.chart.destroy();
        }

        // Initialize Chart.js Radar
        const ctx = canvas.getContext('2d');
        this.chart = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: p1 ? p1.name : 'Jogador 1',
                        data: p1Data,
                        borderColor: this.colors.player1.border,
                        backgroundColor: this.colors.player1.bg,
                        pointBackgroundColor: this.colors.player1.point,
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: this.colors.player1.border,
                        borderWidth: 2
                    },
                    {
                        label: p2 ? p2.name : 'Jogador 2',
                        data: p2Data,
                        borderColor: this.colors.player2.border,
                        backgroundColor: this.colors.player2.bg,
                        pointBackgroundColor: this.colors.player2.point,
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: this.colors.player2.border,
                        borderWidth: 2
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    r: {
                        angleLines: {
                            color: 'rgba(255, 255, 255, 0.08)'
                        },
                        grid: {
                            color: 'rgba(255, 255, 255, 0.08)'
                        },
                        pointLabels: {
                            color: '#94a3b8',
                            font: {
                                family: "'Outfit', sans-serif",
                                size: 10,
                                weight: '600'
                            }
                        },
                        ticks: {
                            color: '#475569',
                            backdropColor: 'transparent',
                            font: {
                                size: 9
                            },
                            stepSize: 20
                        },
                        min: 0,
                        max: 100
                    }
                },
                plugins: {
                    legend: {
                        labels: {
                            color: '#f8fafc',
                            font: {
                                family: "'Outfit', sans-serif",
                                size: 12,
                                weight: '600'
                            }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `${context.dataset.label}: ${context.raw}% do máximo do jogo`;
                            }
                        }
                    }
                }
            }
        });
    }

    /**
     * Helper to render absolute stat values under the radar
     */
    updateAbsoluteStatsTable(p1, p2, getDefensiveActions) {
        // Player 1 Columns
        const p1Name = document.getElementById('p1-card-name');
        const p1Team = document.getElementById('p1-card-team');
        const p1Xg = document.getElementById('p1-stat-xg');
        const p1Xa = document.getElementById('p1-stat-xa');
        const p1Prog = document.getElementById('p1-stat-prog');
        const p1Press = document.getElementById('p1-stat-press');
        const p1Drib = document.getElementById('p1-stat-drib');
        const p1Def = document.getElementById('p1-stat-def');

        if (p1Name && p1) {
            p1Name.innerText = p1.name;
            p1Team.innerText = p1.team;
            p1Xg.innerText = (p1.xg || 0).toFixed(2);
            p1Xa.innerText = (p1.xa || 0).toFixed(2);
            p1Prog.innerText = p1.progressive_passes || 0;
            p1Press.innerText = `${p1.passes_under_pressure_completed || 0}/${p1.passes_under_pressure_total || 0}`;
            p1Drib.innerText = `${p1.dribbles_completed || 0}/${p1.dribbles_attempted || 0}`;
            p1Def.innerText = getDefensiveActions(p1);
        }

        // Player 2 Columns
        const p2Name = document.getElementById('p2-card-name');
        const p2Team = document.getElementById('p2-card-team');
        const p2Xg = document.getElementById('p2-stat-xg');
        const p2Xa = document.getElementById('p2-stat-xa');
        const p2Prog = document.getElementById('p2-stat-prog');
        const p2Press = document.getElementById('p2-stat-press');
        const p2Drib = document.getElementById('p2-stat-drib');
        const p2Def = document.getElementById('p2-stat-def');

        if (p2Name && p2) {
            p2Name.innerText = p2.name;
            p2Team.innerText = p2.team;
            p2Xg.innerText = (p2.xg || 0).toFixed(2);
            p2Xa.innerText = (p2.xa || 0).toFixed(2);
            p2Prog.innerText = p2.progressive_passes || 0;
            p2Press.innerText = `${p2.passes_under_pressure_completed || 0}/${p2.passes_under_pressure_total || 0}`;
            p2Drib.innerText = `${p2.dribbles_completed || 0}/${p2.dribbles_attempted || 0}`;
            p2Def.innerText = getDefensiveActions(p2);
        }

        // Destaque dinâmico do jogador vencedor em cada métrica
        const highlightWinner = (el1, el2, val1, val2) => {
            if (!el1 || !el2) return;
            
            // Limpa classes anteriores e define cor neutra de texto
            el1.classList.remove('text-emerald-400', 'font-extrabold');
            el2.classList.remove('text-emerald-400', 'font-extrabold');
            el1.classList.add('text-slate-300');
            el2.classList.add('text-slate-300');
            
            if (val1 === val2) return;
            
            if (val1 > val2) {
                el1.classList.remove('text-slate-300');
                el1.classList.add('text-emerald-400', 'font-extrabold');
            } else {
                el2.classList.remove('text-slate-300');
                el2.classList.add('text-emerald-400', 'font-extrabold');
            }
        };

        if (p1 && p2 && p1Xg && p2Xg) {
            highlightWinner(p1Xg, p2Xg, p1.xg || 0, p2.xg || 0);
            highlightWinner(p1Xa, p2Xa, p1.xa || 0, p2.xa || 0);
            highlightWinner(p1Prog, p2Prog, p1.progressive_passes || 0, p2.progressive_passes || 0);
            highlightWinner(p1Press, p2Press, p1.passes_under_pressure_completed || 0, p2.passes_under_pressure_completed || 0);
            highlightWinner(p1Drib, p2Drib, p1.dribbles_completed || 0, p2.dribbles_completed || 0);
            highlightWinner(p1Def, p2Def, getDefensiveActions(p1), getDefensiveActions(p2));
        }
    }
}
