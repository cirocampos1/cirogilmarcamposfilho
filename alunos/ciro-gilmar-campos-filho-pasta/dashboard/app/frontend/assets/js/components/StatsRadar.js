export class StatsRadar {
    constructor(canvasElement) {
        this.canvas = canvasElement;
        this.chart = null;
    }

    render(stats, compareStats = null) {
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

        let compareValues = null;
        if (compareStats) {
            compareValues = [
                compareStats.accuratePass || 0,
                compareStats.wonTackle || 0,
                compareStats.totalTackle || 0,
                compareStats.duelWon || 0,
                compareStats.interceptions || 0,
                compareStats.onTargetScoringAttempt || 0,
                compareStats.wasFouled || 0,
                compareStats.clearances || 0,
            ];
        }

        const allValues = compareValues ? [...values, ...compareValues] : values;
        const maxVal = Math.max(...allValues, 1);

        if (this.chart) {
            this.chart.destroy();
        }

        const datasets = [{
            label: 'Jogador Principal',
            data: values.map(v => (v / maxVal) * 100),
            backgroundColor: 'rgba(16, 185, 129, 0.12)',
            borderColor: '#10b981',
            pointBackgroundColor: '#10b981',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: '#10b981',
            borderWidth: 2,
            pointRadius: 4,
        }];

        if (compareValues) {
            datasets.push({
                label: 'Jogador Comparado',
                data: compareValues.map(v => (v / maxVal) * 100),
                backgroundColor: 'rgba(245, 158, 11, 0.12)',
                borderColor: '#f59e0b',
                pointBackgroundColor: '#f59e0b',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: '#f59e0b',
                borderWidth: 2,
                pointRadius: 4,
            });
        }

        this.chart = new Chart(this.canvas.getContext('2d'), {
            type: 'radar',
            data: {
                labels,
                datasets
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
                    legend: {
                        display: !!compareStats,
                        labels: {
                            color: '#94a3b8',
                            font: { family: 'Outfit', size: 11 }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: (ctx) => {
                                const idx = ctx.dataIndex;
                                const val = ctx.datasetIndex === 0 ? values[idx] : compareValues[idx];
                                return `${ctx.dataset.label} - ${labels[idx]}: ${val}`;
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
