import { api } from '../services/api.js?v=20260614-six-maps';
import { PlayerSelector } from './PlayerSelector.js?v=20260614-six-maps';
import { StatsRadar } from './StatsRadar.js?v=20260614-six-maps';

const STAT_GROUPS = {
    attack: [
        { key: 'goals', label: 'Gols', icon: 'G', suffix: '' },
        { key: 'onTargetScoringAttempt', label: 'No Alvo', icon: 'A', suffix: '' },
        { key: 'shotOffTarget', label: 'Fora', icon: 'F', suffix: '' },
        { key: 'blockedScoringAttempt', label: 'Bloq.', icon: 'B', suffix: '' },
        { key: 'bigChanceCreated', label: 'G. Chances', icon: 'GC', suffix: '' },
    ],
    passing: [
        { key: 'totalPass', label: 'Passes', icon: 'P', suffix: '' },
        { key: 'accuratePass', label: 'Acerto', icon: '✓', suffix: '%', pct: true, base: 'totalPass' },
        { key: 'goalAssist', label: 'Assist.', icon: 'A', suffix: '' },
        { key: 'totalCross', label: 'Cruzam.', icon: '×', suffix: '' },
        { key: 'accurateCross', label: 'C. Certos', icon: '✓', suffix: '%', pct: true, base: 'totalCross' },
    ],
    defense: [
        { key: 'duelWon', label: 'D. Ganhos', icon: 'DG', suffix: '' },
        { key: 'duelLost', label: 'D. Perd.', icon: 'DP', suffix: '' },
        { key: 'totalTackle', label: 'Desarmes', icon: 'D', suffix: '' },
        { key: 'wonTackle', label: 'D. Certos', icon: '✓', suffix: '' },
        { key: 'interceptions', label: 'Recuper.', icon: 'R', suffix: '' },
        { key: 'clearances', label: 'Cortes', icon: 'C', suffix: '' },
        { key: 'wasFouled', label: 'Faltas Sof.', icon: 'FS', suffix: '' },
        { key: 'fouls', label: 'Faltas', icon: 'F', suffix: '' },
    ],
};

const ALL_KEYS = [...STAT_GROUPS.attack, ...STAT_GROUPS.passing, ...STAT_GROUPS.defense];

export class Dashboard {
    constructor() {
        this.selector = new PlayerSelector(
            document.getElementById('player-select')
        );
        this.radar = new StatsRadar(
            document.getElementById('stats-radar')
        );
        this.matchSelect = document.getElementById('match-select');
        this.compareSelect = document.getElementById('compare-player-select');
        this.comparisonSummary = document.getElementById('comparison-summary');
        this.currentPlayerId = null;
        this.currentMatchId = null;
        this.currentEventFilter = 'all';
        this.loading = false;
        this.players = [];
        this.lastEvents = {};
        this.lastImages = {};
        this.comparisonStats = null;
        this.comparisonEvents = null;
        this.comparisonVisuals = null;
    }

    async init() {
        try {
            await this.loadMatches();
            this.initEventFilters();
            this.initChartControls();

            const initialPlayerId = await this.loadPlayersForMatch();
            if (!initialPlayerId) {
                this.renderEmptyState();
                this.showError('Nenhum jogador encontrado no banco ou nos JSONs locais');
                return;
            }

            this.matchSelect.addEventListener('change', async (event) => {
                this.currentMatchId = event.target.value;
                this.currentPlayerId = null;
                this.clearComparison();
                const playerId = await this.loadPlayersForMatch();
                await this.loadPlayer(playerId);
            });

            this.selector.onChange(async (playerId) => {
                this.clearComparison();
                await this.loadPlayer(playerId);
            });

            this.compareSelect.addEventListener('change', async () => {
                await this.loadComparison();
            });

            await this.loadPlayer(initialPlayerId);
            this.initStatTabs();
        } catch (error) {
            console.error('Error initializing dashboard:', error);
            this.renderEmptyState();
            this.showError(error.message || 'Falha ao inicializar dashboard');
        }
    }

    async loadMatches() {
        const matches = await api.getMatches();
        this.matchSelect.innerHTML = '';

        matches.forEach(match => {
            const option = document.createElement('option');
            option.value = String(match.match_id);
            const label = `${match.home_team || 'Home'} x ${match.away_team || 'Away'}`;
            option.textContent = `${label} (${match.match_id})`;
            this.matchSelect.appendChild(option);
        });

        if (matches.length === 0) {
            const option = document.createElement('option');
            option.value = '';
            option.textContent = 'Nenhuma partida disponível';
            this.matchSelect.appendChild(option);
            this.matchSelect.disabled = true;
            this.currentMatchId = null;
            return;
        }

        this.matchSelect.disabled = false;
        this.currentMatchId = this.matchSelect.value;
    }

    async loadPlayersForMatch() {
        const initialPlayerId = await this.selector.load('866469', this.currentMatchId);
        this.players = await api.getPlayers(this.currentMatchId);
        this.populateCompareSelect(initialPlayerId);
        return initialPlayerId;
    }

    populateCompareSelect(primaryPlayerId) {
        this.compareSelect.innerHTML = '<option value="">Comparar com...</option>';
        this.players
            .filter(player => player.id !== primaryPlayerId)
            .forEach(player => {
                const option = document.createElement('option');
                option.value = player.id;
                option.textContent = player.name || `Jogador ${player.id}`;
                this.compareSelect.appendChild(option);
            });
        this.compareSelect.disabled = this.players.length < 2;
    }

    initStatTabs() {
        document.querySelectorAll('.stat-tab').forEach(tab => {
            tab.addEventListener('click', () => {
                document.querySelectorAll('.stat-tab').forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                const group = tab.dataset.group;
                this.renderStatsGrid(this.lastStats, group);
            });
        });
    }

    initEventFilters() {
        document.querySelectorAll('.event-filter').forEach(button => {
            button.addEventListener('click', () => {
                document.querySelectorAll('.event-filter').forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');
                this.currentEventFilter = button.dataset.type || 'all';
                this.renderCurrentEvents();
            });
        });
    }

    initChartControls() {
        document.querySelectorAll('.chart-mode').forEach(button => {
            button.addEventListener('click', () => {
                document.querySelectorAll('.chart-mode').forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');
                this.radar.setMode(button.dataset.mode || 'radar');
            });
        });
    }

    showLoading() {
        this.loading = true;
        document.querySelectorAll('.skeleton-img').forEach(s => s.classList.add('active'));
        document.getElementById('stats-skeleton').classList.add('active');
        document.getElementById('events-skeleton').classList.add('active');
        document.getElementById('radar-skeleton').classList.add('active');
        document.querySelectorAll('.img-placeholder').forEach(p => p.classList.remove('active'));
        document.getElementById('stats-grid').innerHTML = '';
        document.getElementById('events-grid').classList.add('hidden');
        document.getElementById('events-empty').classList.add('hidden');
    }

    hideLoading() {
        this.loading = false;
        document.querySelectorAll('.skeleton-img').forEach(s => s.classList.remove('active'));
        document.getElementById('stats-skeleton').classList.remove('active');
        document.getElementById('events-skeleton').classList.remove('active');
        document.getElementById('radar-skeleton').classList.remove('active');
    }

    showError(message) {
        const toast = document.getElementById('error-toast');
        document.getElementById('error-message').textContent = message;
        toast.classList.remove('hidden');
        setTimeout(() => toast.classList.add('hidden'), 5000);
    }

    async loadPlayer(playerId) {
        if (this.loading || playerId === this.currentPlayerId) return;
        if (!playerId) {
            this.renderEmptyState();
            return;
        }
        this.currentPlayerId = playerId;
        this.showLoading();

        try {
            const data = await api.getDashboardData(playerId, this.currentMatchId);
            const stats = data.stats || {};
            this.comparisonStats = null;
            this.comparisonEvents = null;
            this.comparisonVisuals = null;
            this.lastImages = data.images || {};
            this.lastStats = stats;
            this.lastEvents = data.events || {};
            this.renderImages(this.lastImages);
            this.renderEvents(this.lastEvents, stats);
            this.radar.render(stats);
            this.renderStatsGrid(stats, 'all');
            this.renderPlayerInfo(stats);
            this.populateCompareSelect(playerId);
            this.hideLoading();
            this.selector.enable();
        } catch (error) {
            console.error('Error loading player dashboard:', error);
            this.currentPlayerId = null;
            this.hideLoading();
            this.selector.enable();
            this.renderEmptyState();
            this.showError(error.message || 'Erro ao carregar dados do jogador');
        }
    }

    renderEmptyState() {
        this.lastStats = {};
        this.lastEvents = {};
        this.lastImages = {};
        this.comparisonStats = null;
        this.comparisonEvents = null;
        this.comparisonVisuals = null;
        this.hideLoading();
        this.renderImages({});
        this.renderEvents({}, {});
        this.renderStatsGrid({}, 'all');
        this.renderPlayerInfo({});
        this.clearComparison();
    }

    async loadComparison() {
        const comparePlayerId = this.compareSelect.value;
        if (!this.currentPlayerId || !comparePlayerId) {
            this.comparisonStats = null;
            this.comparisonEvents = null;
            this.comparisonVisuals = null;
            this.renderImages(this.lastImages || {});
            this.radar.render(this.lastStats || {});
            this.renderEvents(this.lastEvents, this.lastStats || {});
            this.clearComparison();
            return;
        }

        try {
            const data = await api.comparePlayers(
                [this.currentPlayerId, comparePlayerId],
                this.currentMatchId
            );
            this.radar.renderComparison(data.players || []);
            this.renderComparisonSummary(data.players || []);
            this.comparisonStats = this.aggregateComparisonStats(data.players || []);
            this.comparisonEvents = data.events || {};
            this.comparisonVisuals = data.visuals || null;
            if (this.comparisonVisuals) {
                this.renderComparisonImages(this.comparisonVisuals);
            } else {
                this.renderImages(data.images || this.lastImages || {});
            }
            this.renderCurrentEvents();
        } catch (error) {
            console.error('Error loading comparison:', error);
            this.showError(error.message || 'Erro ao comparar jogadores');
        }
    }

    aggregateComparisonStats(players) {
        const aggregate = { _comparisonCount: players.length };
        players.forEach(player => {
            Object.entries(player.stats || {}).forEach(([key, value]) => {
                if (typeof value === 'number' && Number.isFinite(value)) {
                    aggregate[key] = (aggregate[key] || 0) + value;
                }
            });
        });
        return aggregate;
    }

    renderComparisonSummary(players) {
        if (!players || players.length < 2) {
            this.clearComparison();
            return;
        }

        this.comparisonSummary.classList.remove('hidden');
        this.comparisonSummary.innerHTML = players.map(player => {
            const stats = player.stats || {};
            return `
                <div class="comparison-card">
                    <strong>${player.name}</strong>
                    <span>Rating ${stats.rating || '-'}</span>
                    <span>${stats.totalPass || 0} passes</span>
                    <span>${stats.duelWon || 0} duelos ganhos</span>
                    <span>${this.formatMetric(stats.dribbleValueNormalized || 0)} valor drible</span>
                </div>
            `;
        }).join('');
    }

    clearComparison() {
        this.comparisonStats = null;
        this.comparisonEvents = null;
        this.comparisonVisuals = null;
        this.renderImages(this.lastImages || {});
        this.compareSelect.value = '';
        this.comparisonSummary.classList.add('hidden');
        this.comparisonSummary.innerHTML = '';
    }

    renderCurrentEvents() {
        if (this.comparisonStats) {
            this.renderEvents(this.comparisonEvents || {}, this.comparisonStats);
            return;
        }
        this.renderEvents(this.lastEvents, this.lastStats || {});
    }

    renderImages(images) {
        ['heatmap', 'shotmap', 'passmap'].forEach(type => {
            const img = document.getElementById(`${type}-img`);
            const placeholder = document.getElementById(`${type}-placeholder`);
            const wrapper = document.getElementById(`${type}-wrapper`);
            const comparisonGrid = document.getElementById(`${type}-comparison`);

            wrapper.classList.remove('hidden');
            comparisonGrid?.classList.add('hidden');
            if (comparisonGrid) comparisonGrid.innerHTML = '';

            if (images?.[type]) {
                img.src = 'data:image/png;base64,' + images[type];
                img.alt = `${type} do jogador`;
                img.classList.remove('hidden');
                placeholder.classList.remove('active');
            } else {
                img.classList.add('hidden');
                placeholder.classList.add('active');
            }
        });
    }

    renderComparisonImages(visuals) {
        ['heatmap', 'shotmap', 'passmap'].forEach(type => {
            const wrapper = document.getElementById(`${type}-wrapper`);
            const comparisonGrid = document.getElementById(`${type}-comparison`);

            wrapper.classList.add('hidden');
            comparisonGrid.classList.remove('hidden');
            comparisonGrid.innerHTML = visuals.map(player => {
                const image = player.images?.[type];
                const content = image
                    ? `<img src="data:image/png;base64,${image}" alt="${type} de ${player.name}">`
                    : `<div class="img-placeholder active">
                            <span class="placeholder-icon">${type === 'heatmap' ? 'HM' : type === 'shotmap' ? 'SM' : 'PM'}</span>
                            <span class="placeholder-text">Mapa indisponível</span>
                       </div>`;
                return `
                    <div class="comparison-map-card">
                        <div class="comparison-map-title">${player.name}</div>
                        <div class="img-wrapper comparison-map-frame">${content}</div>
                    </div>
                `;
            }).join('');
        });
    }

    renderEvents(events, stats) {
        const eventTypes = [
            { type: 'pass', label: 'Passes', color: '#10b981' },
            { type: 'dribble', label: 'Dribles', color: '#f59e0b' },
            { type: 'defensive', label: 'Defensivas', color: '#8b5cf6' },
            { type: 'ball_carry', label: 'Conduções', color: '#06b6d4' },
        ];

        const grid = document.getElementById('events-grid');
        const empty = document.getElementById('events-empty');
        let hasAny = false;

        eventTypes.forEach(({ type, color }) => {
            const list = events?.[type] || [];
            const metric = this.getEventMetric(type, list, stats);
            const categoryEl = document.querySelector(`.event-category[data-type="${type}"]`);
            const visible = this.currentEventFilter === 'all' || this.currentEventFilter === type;
            categoryEl?.classList.toggle('hidden', !visible);
            const countEl = document.getElementById(`event-${type}-count`);
            const barEl = document.getElementById(`event-${type}-bar`);
            const detailEl = document.getElementById(`event-${type}-detail`);

            countEl.textContent = metric.display;
            if (visible && metric.hasValue) {
                hasAny = true;
                const success = list.length > 0
                    ? list.filter(e => e.outcome !== false).length
                    : metric.count;
                const pct = metric.count > 0 ? Math.round((success / metric.count) * 100) : metric.barPct;
                barEl.style.width = Math.max(pct, type === 'defensive' ? 100 : (type === 'ball_carry' ? 80 : pct)) + '%';
                barEl.style.background = color;

                if (type === 'pass') {
                    const acc = stats?.accuratePass && stats?.totalPass
                        ? Math.round((stats.accuratePass / stats.totalPass) * 100) + '%'
                        : pct + '%';
                    detailEl.textContent = `Precisão: ${acc}`;
                } else if (type === 'dribble') {
                    detailEl.textContent = metric.count > 0
                        ? `Sucesso: ${pct}%`
                        : `${stats?._comparisonCount ? 'Valor combinado' : 'Valor'}: ${this.formatMetric(metric.value)}`;
                } else if (type === 'defensive') {
                    detailEl.textContent = `Ações: ${metric.display}`;
                } else if (type === 'ball_carry') {
                    detailEl.textContent = `Conduções: ${metric.display}`;
                }
            } else {
                barEl.style.width = '0%';
                detailEl.textContent = 'Nenhum evento';
            }
        });

        if (hasAny) {
            grid.classList.remove('hidden');
            empty.classList.add('hidden');
        } else {
            grid.classList.add('hidden');
            empty.classList.remove('hidden');
        }
    }

    getEventMetric(type, list, stats = {}) {
        const listCount = list.length;
        if (listCount > 0) {
            return {
                count: listCount,
                display: String(listCount),
                hasValue: true,
                value: listCount,
                barPct: 100,
            };
        }

        const fallbackByType = {
            pass: stats.totalPass || 0,
            dribble: stats.totalContest || stats.wonContest || 0,
            defensive: (stats.interceptions || 0) + (stats.totalTackle || 0) + (stats.clearances || 0),
            ball_carry: stats.ballCarriesCount || 0,
        };

        const value = type === 'dribble'
            ? (fallbackByType.dribble || stats.dribbleValueNormalized || 0)
            : fallbackByType[type];
        const isFractional = Math.abs(value) > 0 && Math.abs(value) < 1;
        const display = isFractional ? this.formatMetric(value) : String(Math.round(value || 0));

        return {
            count: fallbackByType[type] || 0,
            display,
            hasValue: value !== null && value !== undefined && value !== 0,
            value,
            barPct: Math.min(100, Math.max(8, Math.round(Math.abs(value || 0) * 100))),
        };
    }

    formatMetric(value) {
        return Number(value || 0).toLocaleString('pt-BR', {
            maximumFractionDigits: 2,
        });
    }

    renderPlayerInfo(stats) {
        const rating = stats.rating || '-';
        const mins = stats.minutesPlayed || '-';
        const info = document.getElementById('player-info');
        info.innerHTML = `
            <span class="info-badge">Rat ${rating}</span>
            <span class="info-badge">${mins} min</span>
            <span class="info-badge">${stats.goals || 0} gols</span>
        `;
    }

    renderStatsGrid(stats, group = 'all') {
        const grid = document.getElementById('stats-grid');
        grid.innerHTML = '';

        const keys = group === 'all' ? ALL_KEYS : STAT_GROUPS[group] || ALL_KEYS;

        keys.forEach(({ key, label, icon, suffix, pct, base }) => {
            let value = stats[key] ?? 0;
            if (pct && base) {
                const baseVal = stats[base] ?? 0;
                value = baseVal > 0 ? Math.round((value / baseVal) * 100) : 0;
            }
            const card = document.createElement('div');
            card.className = 'stat-card';
            card.style.animationDelay = (keys.indexOf({ key, label, icon, suffix, pct, base }) * 0.05) + 's';
            card.innerHTML = `
                <div class="stat-value">${value}${suffix}</div>
                <div class="stat-label">${icon} ${label}</div>
            `;
            grid.appendChild(card);
        });
    }
}
