const METRICS = [
    { key: 'accuratePass', label: 'Passes' },
    { key: 'wonTackle', label: 'D. Certos' },
    { key: 'totalTackle', label: 'Desarmes' },
    { key: 'duelWon', label: 'Duelos' },
    { key: 'interceptions', label: 'Recup.' },
    { key: 'onTargetScoringAttempt', label: 'Finaliz.' },
    { key: 'wasFouled', label: 'F. Sofr.' },
    { key: 'clearances', label: 'Cortes' },
];

export class StatsRadar {
    constructor(canvasElement) {
        this.canvas = canvasElement;
        this.chart = null;
        this.mode = 'radar';
        this.lastStats = null;
        this.lastComparison = null;
    }

    setMode(mode) {
        this.mode = mode;
        if (this.lastComparison) {
            this.renderComparison(this.lastComparison);
        } else {
            this.render(this.lastStats);
        }
    }

    render(stats) {
        if (!stats) {
            this.destroy();
            return;
        }
        this.lastStats = stats;
        this.lastComparison = null;

        const labels = METRICS.map(m => m.label);
        const values = METRICS.map(m => stats[m.key] || 0);

        const maxVal = Math.max(...values, 1);

        if (this.chart) {
            this.chart.destroy();
        }

        this.chart = new Chart(this.canvas.getContext('2d'), {
            type: this.mode,
            data: {
                labels,
                datasets: [{
                    label: 'Atributos do Jogador',
                    data: this.mode === 'radar' ? values.map(v => (v / maxVal) * 100) : values,
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
                responsive: false,
                maintainAspectRatio: false,
                layout: { padding: 32 },
                scales: this.mode === 'radar' ? {
                    r: {
                        angleLines: { color: 'rgba(255, 255, 255, 0.06)' },
                        grid: { color: 'rgba(255, 255, 255, 0.06)' },
                        pointLabels: {
                            color: '#94a3b8',
                            font: { family: 'Outfit', size: 11, weight: '600' }
                        },
                        ticks: { display: false, max: 100 }
                    }
                } : {
                    x: { ticks: { color: '#94a3b8' }, grid: { display: false } },
                    y: { ticks: { color: '#94a3b8' }, grid: { color: 'rgba(255, 255, 255, 0.06)' } },
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

    renderComparison(players) {
        this.lastComparison = players;
        if (!players || players.length === 0) {
            this.render(this.lastStats);
            return;
        }

        if (this.chart) {
            this.chart.destroy();
        }

        const labels = METRICS.map(m => m.label);
        const palette = ['#10b981', '#38bdf8', '#f59e0b'];
        const datasets = players.map((player, index) => ({
            label: player.name,
            data: METRICS.map(m => player.stats?.[m.key] || 0),
            backgroundColor: `${palette[index % palette.length]}33`,
            borderColor: palette[index % palette.length],
            pointBackgroundColor: palette[index % palette.length],
            borderWidth: 2,
        }));

        this.chart = new Chart(this.canvas.getContext('2d'), {
            type: this.mode === 'radar' ? 'radar' : 'bar',
            data: { labels, datasets },
            options: {
                responsive: false,
                maintainAspectRatio: false,
                layout: { padding: 32 },
                scales: this.mode === 'radar' ? {
                    r: {
                        angleLines: { color: 'rgba(255, 255, 255, 0.06)' },
                        grid: { color: 'rgba(255, 255, 255, 0.06)' },
                        pointLabels: { color: '#94a3b8', font: { family: 'Outfit', size: 11, weight: '600' } },
                        ticks: { display: false }
                    }
                } : {
                    x: { ticks: { color: '#94a3b8' }, grid: { display: false } },
                    y: { ticks: { color: '#94a3b8' }, grid: { color: 'rgba(255, 255, 255, 0.06)' } },
                },
                plugins: {
                    legend: { labels: { color: '#cbd5e1', font: { family: 'Outfit' } } }
                }
            }
        });
    }

    destroy() {
        if (this.chart) {
            this.chart.destroy();
            this.chart = null;
        }
        this.lastStats = null;
        this.lastComparison = null;
    }
}
