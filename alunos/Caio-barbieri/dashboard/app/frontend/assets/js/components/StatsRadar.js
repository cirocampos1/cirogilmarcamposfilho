export class StatsRadar {
    constructor(canvasElement) {
        this.canvas = canvasElement;
        this.chart = null;
    }

    render(statsA, statsB) {
        if (!statsA && !statsB) {
            this.destroy();
            return;
        }

        const labels = [
            'Passes Certos',
            'Dribles',
            'Desarmes',
            'Duelos Ganhos',
            'Recuperações',
            'Finalizações',
            'Faltas Sofridas',
            'Cortes',
        ];

        const getValues = (s) => s ? [
            s.accuratePass || 0,
            s.wonTackle || 0,
            s.totalTackle || 0,
            s.duelWon || 0,
            s.interceptions || 0,
            s.onTargetScoringAttempt || 0,
            s.wasFouled || 0,
            s.clearances || 0,
        ] : [0, 0, 0, 0, 0, 0, 0, 0];

        const valuesA = getValues(statsA);
        const valuesB = getValues(statsB);

        const maxVal = Math.max(...valuesA, ...valuesB, 1);

        if (this.chart) {
            this.chart.destroy();
        }

        const datasets = [];
        if (statsA) {
            datasets.push({
                label: 'Jogador A',
                data: valuesA.map(v => (v / maxVal) * 100),
                backgroundColor: 'rgba(16, 185, 129, 0.35)',
                borderColor: '#10b981',
                pointBackgroundColor: '#10b981',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: '#10b981',
                borderWidth: 2,
                pointRadius: 4,
            });
        }
        if (statsB) {
            datasets.push({
                label: 'Jogador B',
                data: valuesB.map(v => (v / maxVal) * 100),
                backgroundColor: 'rgba(239, 68, 68, 0.35)',
                borderColor: '#ef4444',
                pointBackgroundColor: '#ef4444',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: '#ef4444',
                borderWidth: 2,
                pointRadius: 4,
            });
        }

        this.chart = new Chart(this.canvas.getContext('2d'), {
            type: 'polarArea',
            data: { labels, datasets },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                scales: {
                    r: {
                        angleLines: { color: 'rgba(255, 255, 255, 0.06)' },
                        grid: { color: 'rgba(255, 255, 255, 0.06)' },
                        pointLabels: {
                            color: '#94a3b8',
                            font: { family: 'Outfit', size: 11, weight: '600' }
                        },
                        ticks: { display: false, max: 100 }
                    }
                },
                plugins: {
                    legend: {
                        display: true,
                        labels: {
                            color: '#94a3b8',
                            font: { family: 'Outfit' }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: (ctx) => {
                                const idx = ctx.dataIndex;
                                const isA = ctx.dataset.label === 'Jogador A';
                                const rawVal = isA ? valuesA[idx] : valuesB[idx];
                                return `${ctx.dataset.label}: ${rawVal}`;
                            }
                        }
                    }
                }
            }
        });
    }

    destroy() {
        if (this.chart) {
            this.chart.destroy();
            this.chart = null;
        }
    }
}
