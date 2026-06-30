export class StatsRadar {
    constructor(canvasElement) {
        this.canvas = canvasElement;
        this.chart = null;
    }

    render(stats) {
        if (!stats) {
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

        const values = [
            stats.accuratePass || 0,
            stats.wonTackle || 0,
            stats.totalTackle || 0,
            stats.duelWon || 0,
            stats.interceptions || 0,
            stats.onTargetScoringAttempt || 0,
            stats.wasFouled || 0,
            stats.clearances || 0,
        ];

        const maxVal = Math.max(...values, 1);

        if (this.chart) {
            this.chart.destroy();
        }

        this.chart = new Chart(this.canvas.getContext('2d'), {
            type: 'radar',
            data: {
                labels,
                datasets: [{
                    label: 'Atributos do Jogador',
                    data: values.map(v => (v / maxVal) * 100),
                    backgroundColor: 'rgba(16, 185, 129, 0.15)',
                    borderColor: '#10b981',
                    pointBackgroundColor: '#10b981',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: '#10b981',
                    borderWidth: 2,
                    pointRadius: 4,
                }]
            },
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
                    legend: { display: false },
                    tooltip: {
                        callbacks: {
                            label: (ctx) => {
                                const idx = ctx.dataIndex;
                                return `${labels[idx]}: ${values[idx]}`;
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
