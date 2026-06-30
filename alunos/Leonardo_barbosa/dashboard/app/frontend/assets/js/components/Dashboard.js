import { api } from '../services/api.js?v=4';
import { PlayerSelector } from './PlayerSelector.js?v=4';
import { MatchSelector } from './MatchSelector.js?v=4';
import { StatsRadar } from './StatsRadar.js?v=4';

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
        this.matchSelector = new MatchSelector(document.getElementById('match-select'));
        this.selector = new PlayerSelector(document.getElementById('player-select'));
        this.radar = new StatsRadar(document.getElementById('stats-radar'));
        this.compareSelect = document.getElementById('compare-player-select');
        this.comparisonSummary = document.getElementById('comparison-summary');
        this.currentMatchId = null;
        this.currentPlayerId = null;
        this.loading = false;
        this.players = [];
        this.lastStats = {};
        this.lastEvents = {};
        this.lastImages = {};
    }

    async init() {
        try {
            const initialMatchId = await this.matchSelector.load();
            this.currentMatchId = initialMatchId;

            const initialPlayerId = await this.selector.load(initialMatchId);
            this.currentPlayerId = initialPlayerId;
            this.players = await api.getPlayers(initialMatchId);

            this.matchSelector.onChange(async (matchId) => {
                await this.loadMatch(matchId);
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
            this.initEventFilters();
            this.initTeamShotmapControls();
            this.loadTimeline(initialMatchId);
            this.loadTeamShotmap(initialMatchId, 'all');
        } catch (error) {
            console.error('Error initializing dashboard:', error);
            this.showError(error.message || 'Falha ao inicializar dashboard');
        }
    }

    async loadMatch(matchId) {
        if (this.loading || matchId === this.currentMatchId) return;
        this.currentMatchId = matchId;
        this.showLoading();
        this.clearComparison();

        try {
            const newPlayerId = await this.selector.load(matchId);
            this.players = await api.getPlayers(matchId);
            this.matchSelector.enable();
            this.populateCompareSelect(newPlayerId);
            await this.loadPlayer(newPlayerId, true);
            this.loadTimeline(matchId);
            this.loadTeamShotmap(matchId, 'all');
        } catch (error) {
            console.error('Error loading match:', error);
            this.hideLoading();
            this.matchSelector.enable();
            this.showError(error.message || 'Erro ao carregar dados da partida');
        }
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
        document.querySelectorAll('.event-filter').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.event-filter').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.renderEventsByFilter(btn.dataset.type || 'all');
            });
        });
    }

    initTeamShotmapControls() {
        document.querySelectorAll('.team-shotmap-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.team-shotmap-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.loadTeamShotmap(this.currentMatchId, btn.dataset.team || 'all');
            });
        });
    }

    showLoading() {
        this.loading = true;
        document.querySelectorAll('.skeleton-img').forEach(s => s.classList.add('active'));
        document.getElementById('stats-skeleton').classList.add('active');
        document.getElementById('events-skeleton').classList.add('active');
        document.getElementById('radar-skeleton').classList.add('active');
        document.getElementById('timeline-skeleton').classList.add('active');
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
        document.getElementById('timeline-skeleton').classList.remove('active');
    }

    showError(message) {
        const toast = document.getElementById('error-toast');
        document.getElementById('error-message').textContent = message;
        toast.classList.remove('hidden');
        setTimeout(() => toast.classList.add('hidden'), 5000);
    }

    async loadPlayer(playerId, force = false) {
        if ((this.loading || playerId === this.currentPlayerId) && !force) return;
        this.currentPlayerId = playerId;
        this.showLoading();

        try {
            const data = await api.getDashboardData(playerId, this.currentMatchId);
            this.lastStats = data.stats || {};
            this.lastEvents = data.events || {};
            this.lastImages = data.images || {};
            this.renderImages(this.lastImages);
            this.renderEvents(this.lastEvents, this.lastStats);
            this.radar.render(this.lastStats);
            this.renderStatsGrid(this.lastStats, 'all');
            this.renderPlayerInfo(this.lastStats);
            this.populateCompareSelect(playerId);
            this.hideLoading();
            this.selector.enable();
            this.matchSelector.enable();
        } catch (error) {
            console.error('Error loading player dashboard:', error);
            this.hideLoading();
            this.selector.enable();
            this.matchSelector.enable();
            this.showError(error.message || 'Erro ao carregar dados do jogador');
        }
    }

    populateCompareSelect(primaryPlayerId) {
        this.compareSelect.innerHTML = '<option value="">Comparar com...</option>';
        (this.players || [])
            .filter(p => p.id !== primaryPlayerId)
            .forEach(p => {
                const opt = document.createElement('option');
                opt.value = p.id;
                opt.textContent = p.name || `Jogador ${p.id}`;
                this.compareSelect.appendChild(opt);
            });
        this.compareSelect.disabled = (this.players || []).length < 2;
    }

    async loadComparison() {
        const compareId = this.compareSelect.value;
        if (!this.currentPlayerId || !compareId) {
            this.clearComparison();
            return;
        }

        try {
            const data = await api.comparePlayers(
                [this.currentPlayerId, compareId],
                this.currentMatchId
            );
            const players = data.players || [];
            this.renderComparisonSummary(players);
            this.renderComparisonImages(players);
            this.renderEvents(data.events || {}, this.aggregateStats(players));
        } catch (error) {
            console.error('Error loading comparison:', error);
            this.showError(error.message || 'Erro ao comparar jogadores');
        }
    }

    clearComparison() {
        this.compareSelect.value = '';
        this.comparisonSummary.classList.add('hidden');
        this.comparisonSummary.innerHTML = '';
        document.querySelectorAll('.comparison-map-grid').forEach(g => g.classList.add('hidden'));
        document.querySelectorAll('.img-wrapper').forEach(w => w.classList.remove('hidden'));
        if (this.lastStats) this.renderEvents(this.lastEvents, this.lastStats);
        this.renderImages(this.lastImages);
    }

    aggregateStats(players) {
        const agg = {};
        players.forEach(p => {
            Object.entries(p.stats || {}).forEach(([k, v]) => {
                if (typeof v === 'number') agg[k] = (agg[k] || 0) + v;
            });
        });
        return agg;
    }

    renderComparisonSummary(players) {
        if (!players || players.length < 2) {
            this.clearComparison();
            return;
        }
        this.comparisonSummary.classList.remove('hidden');
        this.comparisonSummary.innerHTML = players.map(p => {
            const s = p.stats || {};
            return `
                <div class="comparison-card">
                    <strong>${s.name || p.id}</strong>
                    <span>Rating ${s.rating || '-'}</span>
                    <span>${s.totalPass || 0} passes</span>
                    <span>${s.duelWon || 0} duelos</span>
                    <span>${s.goals || 0} gols</span>
                </div>
            `;
        }).join('');
    }

    renderComparisonImages(players) {
        ['heatmap', 'shotmap', 'passmap'].forEach(type => {
            const wrapper = document.getElementById(`${type}-wrapper`);
            const grid = document.getElementById(`${type}-comparison`);
            if (!wrapper || !grid) return;

            wrapper.classList.add('hidden');
            grid.classList.remove('hidden');
            grid.innerHTML = players.map(p => {
                const img = (p.images || {})[type];
                return `
                    <div class="comparison-map-card">
                        <div class="comparison-map-title">${p.id}</div>
                        <div class="img-wrapper comparison-map-frame">
                            ${img
                                ? `<img src="data:image/png;base64,${img}" alt="${type}">`
                                : `<div class="img-placeholder active"><span class="placeholder-text">Indisponível</span></div>`
                            }
                        </div>
                    </div>
                `;
            }).join('');
        });
    }

    renderImages(images) {
        ['heatmap', 'shotmap', 'passmap'].forEach(type => {
            const img = document.getElementById(`${type}-img`);
            const placeholder = document.getElementById(`${type}-placeholder`);
            const wrapper = document.getElementById(`${type}-wrapper`);
            if (!img || !placeholder || !wrapper) return;

            wrapper.classList.remove('hidden');
            document.getElementById(`${type}-comparison`)?.classList.add('hidden');

            if (images?.[type]) {
                img.src = 'data:image/png;base64,' + images[type];
                img.classList.remove('hidden');
                placeholder.classList.remove('active');
            } else {
                img.classList.add('hidden');
                placeholder.classList.add('active');
            }
        });
    }

    renderEvents(events, stats) {
        this.lastEvents = events || {};
        this.lastStats = stats || {};
        this.renderEventsByFilter('all');
    }

    renderEventsByFilter(filterType) {
        const events = this.lastEvents || {};
        const stats = this.lastStats || {};
        const types = [
            { type: 'pass', label: 'Passes', color: '#10b981' },
            { type: 'dribble', label: 'Dribles', color: '#f59e0b' },
            { type: 'defensive', label: 'Defensivas', color: '#8b5cf6' },
            { type: 'ball_carry', label: 'Conduções', color: '#06b6d4' },
        ];

        const grid = document.getElementById('events-grid');
        const empty = document.getElementById('events-empty');
        let hasAny = false;

        types.forEach(({ type, color }) => {
            const list = events[type] || [];
            const catEl = document.querySelector(`.event-category[data-type="${type}"]`);
            const visible = filterType === 'all' || filterType === type;
            catEl?.classList.toggle('hidden', !visible);

            const countEl = document.getElementById(`event-${type}-count`);
            const barEl = document.getElementById(`event-${type}-bar`);
            const detailEl = document.getElementById(`event-${type}-detail`);
            if (!countEl || !barEl || !detailEl) return;

            countEl.textContent = list.length;

            if (visible && list.length > 0) {
                hasAny = true;
                const success = list.filter(e => e.outcome !== false).length;
                const pct = list.length > 0 ? Math.round((success / list.length) * 100) : 0;
                barEl.style.width = Math.max(pct, type === 'defensive' ? 100 : pct) + '%';
                barEl.style.background = color;

                if (type === 'pass') {
                    const acc = stats?.accuratePass && stats?.totalPass
                        ? Math.round((stats.accuratePass / stats.totalPass) * 100) + '%'
                        : pct + '%';
                    detailEl.textContent = `Precisão: ${acc}`;
                } else if (type === 'dribble') {
                    detailEl.textContent = `Sucesso: ${pct}%`;
                } else if (type === 'defensive') {
                    detailEl.textContent = `Ações: ${list.length}`;
                } else {
                    detailEl.textContent = `Total: ${list.length}`;
                }
            } else {
                barEl.style.width = '0%';
                detailEl.textContent = visible ? 'Nenhum evento' : '';
            }
        });

        grid?.classList.toggle('hidden', !hasAny);
        empty?.classList.toggle('hidden', hasAny);
    }

    renderPlayerInfo(stats) {
        const el = document.getElementById('player-info');
        if (!el) return;
        el.innerHTML = `
            <span class="info-badge">⭐ ${stats.rating || '-'}</span>
            <span class="info-badge">⏱ ${stats.minutesPlayed || '-'} min</span>
            <span class="info-badge">⚽ ${stats.goals || 0} gols</span>
        `;
    }

    renderStatsGrid(stats, group = 'all') {
        const grid = document.getElementById('stats-grid');
        if (!grid) return;
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
            card.innerHTML = `
                <div class="stat-value">${value}${suffix}</div>
                <div class="stat-label">${icon} ${label}</div>
            `;
            grid.appendChild(card);
        });
    }

    async loadTimeline(matchId) {
        try {
            const moments = await api.getMatchMoments(matchId);
            this.renderTimeline(moments);
        } catch (error) {
            console.error('Error loading timeline:', error);
        }
    }

    renderTimeline(moments) {
        const el = document.getElementById('match-timeline');
        if (!el) return;

        if (!moments || moments.length === 0) {
            el.innerHTML = '<div class="timeline-empty">Nenhum incidente registrado</div>';
            return;
        }

        el.innerHTML = moments.map(m => {
            const min = `${m.minute}'${m.addedTime ? '+' + m.addedTime : ''}`;
            const side = m.isHome ? 'home' : 'away';

            let icon = '●';
            let label = m.text || m.type;
            let detail = '';

            switch (m.type) {
                case 'goal':
                    icon = '⚽';
                    label = `Gol de ${m.playerName || ''}${m.assist ? ` (${m.assist})` : ''}`;
                    detail = `${m.homeScore ?? '?'} - ${m.awayScore ?? '?'}`;
                    break;
                case 'card':
                    icon = m.cardType === 'red' ? '🟥' : '🟨';
                    label = `${m.playerName || ''}${m.reason ? ` - ${m.reason}` : ''}`;
                    break;
                case 'substitution':
                    icon = '🔄';
                    label = `Sai: ${m.playerOut || ''} → Entra: ${m.playerIn || ''}`;
                    break;
                case 'var':
                    icon = '📺';
                    label = `VAR: ${m.decision || ''}${m.reason ? ` (${m.reason})` : ''}`;
                    break;
                case 'penalty':
                    icon = '⚪';
                    label = `Pênalti: ${m.playerName || ''}${m.scored ? ' ✅' : ' ❌'}`;
                    detail = `${m.homeScore ?? ''}${m.awayScore != null ? ` - ${m.awayScore}` : ''}`;
                    break;
            }

            return `
                <div class="timeline-item ${side}" style="--tl-color: ${m.isHome ? 'var(--accent)' : '#e74c3c'}">
                    <div class="timeline-dot">${icon}</div>
                    <div class="timeline-content">
                        <span class="timeline-minute">${min}</span>
                        <span class="timeline-label">${label}</span>
                        ${detail ? `<span class="timeline-detail">${detail}</span>` : ''}
                    </div>
                </div>
            `;
        }).join('');
    }

    async loadTeamShotmap(matchId, team) {
        try {
            const data = await api.getTeamShotmap(matchId, team);
            this.renderTeamShotmap(data);
        } catch (error) {
            console.error('Error loading team shotmap:', error);
        }
    }

    renderTeamShotmap(data) {
        const img = document.getElementById('team-shotmap-img');
        const placeholder = document.getElementById('team-shotmap-placeholder');
        const statsEl = document.getElementById('shotmap-stats');
        if (!img) return;

        if (data?.image) {
            img.src = 'data:image/png;base64,' + data.image;
            img.classList.remove('hidden');
            placeholder?.classList.remove('active');
        } else {
            img.classList.add('hidden');
            placeholder?.classList.add('active');
        }

        if (statsEl && data?.stats) {
            const s = data.stats;
            statsEl.innerHTML = `
                <span class="shotmap-stat">Total: ${s.total || 0}</span>
                <span class="shotmap-stat">⛔ Gols: ${s.goals || 0}</span>
                <span class="shotmap-stat">🎯 No alvo: ${s.onTarget || 0}</span>
                <span class="shotmap-stat">🏠 Casa: ${s.homeShots || 0}</span>
                <span class="shotmap-stat">✈️ Fora: ${s.awayShots || 0}</span>
            `;
        }
    }
}
