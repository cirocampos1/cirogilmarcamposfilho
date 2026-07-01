import { api } from '../services/api.js?v=3';
import { PlayerSelector } from './PlayerSelector.js?v=3';
import { MatchSelector } from './MatchSelector.js?v=3';
import { StatsRadar } from './StatsRadar.js?v=3';

const STAT_GROUPS = {
    attack: [
        { key: 'goals', label: 'Gols', icon: '⚽', suffix: '' },
        { key: 'onTargetScoringAttempt', label: 'No Alvo', icon: '🎯', suffix: '' },
        { key: 'shotOffTarget', label: 'Fora', icon: '❌', suffix: '' },
        { key: 'blockedScoringAttempt', label: 'Bloq.', icon: '🚫', suffix: '' },
        { key: 'bigChanceCreated', label: 'G. Chances', icon: '💎', suffix: '' },
    ],
    passing: [
        { key: 'totalPass', label: 'Passes', icon: '⤴️', suffix: '' },
        { key: 'accuratePass', label: 'Acerto', icon: '✓', suffix: '%', pct: true, base: 'totalPass' },
        { key: 'goalAssist', label: 'Assist.', icon: '🎯', suffix: '' },
        { key: 'totalCross', label: 'Cruzam.', icon: '×', suffix: '' },
        { key: 'accurateCross', label: 'C. Certos', icon: '✓', suffix: '%', pct: true, base: 'totalCross' },
    ],
    defense: [
        { key: 'duelWon', label: 'D. Ganhos', icon: '💪', suffix: '' },
        { key: 'duelLost', label: 'D. Perd.', icon: '💔', suffix: '' },
        { key: 'totalTackle', label: 'Desarmes', icon: '🛡️', suffix: '' },
        { key: 'wonTackle', label: 'D. Certos', icon: '✓', suffix: '' },
        { key: 'interceptions', label: 'Recuper.', icon: '↩️', suffix: '' },
        { key: 'clearances', label: 'Cortes', icon: '🧹', suffix: '' },
        { key: 'wasFouled', label: 'Faltas Sof.', icon: '⚡', suffix: '' },
        { key: 'fouls', label: 'Faltas', icon: '🟨', suffix: '' },
    ],
};

const ALL_KEYS = [...STAT_GROUPS.attack, ...STAT_GROUPS.passing, ...STAT_GROUPS.defense];

export class Dashboard {
    constructor() {
        this.matchSelector = new MatchSelector(
            document.getElementById('match-select')
        );
        this.selector = new PlayerSelector(
            document.getElementById('player-select')
        );
        this.compareSelector = document.getElementById('compare-player-select');
        this.radar = new StatsRadar(
            document.getElementById('stats-radar')
        );
        this.currentMatchId = null;
        this.currentPlayerId = null;
        this.comparePlayerId = null;
        
        this.lastStats = null;
        this.compareStats = null;
        this.lastImages = null;
        this.compareImages = null;
        this.lastEvents = null;
        
        this.playersList = [];
        this.activeEventFilter = 'all'; // 'all', 'success', 'failed'
        this.loading = false;
    }

    async init() {
        try {
            const initialMatchId = await this.matchSelector.load();
            this.currentMatchId = initialMatchId;

            const initialPlayerId = await this.selector.load(initialMatchId);
            
            
            // Carrega lista de jogadores para popular dropdown de comparação
            this.playersList = await api.getPlayers(initialMatchId);
            this.populateCompareSelect(initialPlayerId);

            this.matchSelector.onChange(async (matchId) => {
                await this.loadMatch(matchId);
            });

            this.selector.onChange(async (playerId) => {
                await this.loadPlayer(playerId);
            });
            
            this.compareSelector.addEventListener('change', async (e) => {
                const compareId = e.target.value;
                if (compareId) {
                    await this.loadComparison(compareId);
                } else {
                    this.clearComparison();
                }
            });

            await this.loadPlayer(initialPlayerId);
            this.initStatTabs();
            this.initEventFilters();
        } catch (error) {
            console.error('Error initializing dashboard:', error);
            this.showError('Falha ao inicializar dashboard');
        }
    }

    async loadMatch(matchId) {
        if (this.loading || matchId === this.currentMatchId) return;
        this.currentMatchId = matchId;
        this.showLoading();
        this.clearComparison();

        try {
            const newPlayerId = await this.selector.load(matchId);
            this.playersList = await api.getPlayers(matchId);
            this.populateCompareSelect(newPlayerId);
            this.matchSelector.enable();
            await this.loadPlayer(newPlayerId, true);
        } catch (error) {
            console.error('Error loading match:', error);
            this.hideLoading();
            this.matchSelector.enable();
            this.showError('Erro ao carregar dados da partida');
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

    showLoading() {
        this.loading = true;
        document.querySelectorAll('.skeleton-img').forEach(s => s.classList.add('active'));
        document.getElementById('stats-skeleton').classList.add('active');
        document.getElementById('events-skeleton').classList.add('active');
        document.getElementById('radar-skeleton').classList.add('active');
        document.querySelectorAll('.img-placeholder').forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.map-view-box img').forEach(img => img.classList.add('hidden'));
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

    async loadPlayer(playerId, force = false) {
        if ((this.loading || playerId === this.currentPlayerId) && !force) return;
        this.currentPlayerId = playerId;
        this.showLoading();
        
        // Limpa a comparação caso mude o jogador principal
        this.clearComparison();
        this.populateCompareSelect(playerId);

        try {
            const data = await api.getDashboardData(playerId, this.currentMatchId);
            this.lastStats = data.stats;
            this.lastEvents = data.events;
            this.lastImages = data.images;
            
            this.renderImages(data.images);
            this.renderEvents(data.events, data.stats);
            this.radar.render(data.stats);
            this.renderStatsGrid(data.stats, 'all');
            this.renderPlayerInfo(data.stats);
            this.hideLoading();
            this.selector.enable();
            this.matchSelector.enable();
        } catch (error) {
            console.error('Error loading player dashboard:', error);
            this.hideLoading();
            this.selector.enable();
            this.matchSelector.enable();
            this.showError('Erro ao carregar dados do jogador');
        }
    }

    renderImages(images) {
        this.lastImages = images;
        ['heatmap', 'shotmap', 'passmap'].forEach(type => {
            const img = document.getElementById(`${type}-img`);
            const placeholder = document.getElementById(`${type}-placeholder`);

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

    renderEvents(events, stats) {
        const eventTypes = [
            { type: 'pass', icon: '⤴️', label: 'Passes', color: '#10b981' },
            { type: 'dribble', icon: '💨', label: 'Dribles', color: '#f59e0b' },
            { type: 'defensive', icon: '🛡️', label: 'Defensivas', color: '#8b5cf6' },
            { type: 'ball_carry', icon: '🏃', label: 'Conduções', color: '#06b6d4' },
        ];

        const grid = document.getElementById('events-grid');
        const empty = document.getElementById('events-empty');
        let hasAny = false;

        eventTypes.forEach(({ type, color }) => {
            let list = events?.[type] || [];
            
            // Aplica filtro de sucesso/falha
            if (this.activeEventFilter === 'success') {
                list = list.filter(e => e.outcome !== false);
            } else if (this.activeEventFilter === 'failed') {
                list = list.filter(e => e.outcome === false);
            }
            
            const countEl = document.getElementById(`event-${type}-count`);
            const barEl = document.getElementById(`event-${type}-bar`);
            const detailEl = document.getElementById(`event-${type}-detail`);

            countEl.textContent = list.length;
            if (list.length > 0) {
                hasAny = true;
                const success = list.filter(e => e.outcome !== false).length;
                const pct = list.length > 0 ? Math.round((success / list.length) * 100) : 0;
                barEl.style.width = Math.max(pct, type === 'defensive' ? 100 : (type === 'ball_carry' ? 80 : pct)) + '%';
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
                } else if (type === 'ball_carry') {
                    detailEl.textContent = `Conduções: ${list.length}`;
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

    renderPlayerInfo(stats) {
        const rating = stats.rating || '-';
        const mins = stats.minutesPlayed || '-';
        const info = document.getElementById('player-info');
        info.innerHTML = `
            <span class="info-badge">⭐ ${rating}</span>
            <span class="info-badge">⏱ ${mins} min</span>
            <span class="info-badge">⚽ ${stats.goals || 0} gols</span>
        `;
    }

    renderStatsGrid(stats, group = 'all') {
        const grid = document.getElementById('stats-grid');
        grid.innerHTML = '';

        const keys = group === 'all' ? ALL_KEYS : STAT_GROUPS[group] || ALL_KEYS;

        keys.forEach(({ key, label, icon, suffix, pct, base }, index) => {
            let primaryValue = stats[key] ?? 0;
            if (pct && base) {
                const baseVal = stats[base] ?? 0;
                primaryValue = baseVal > 0 ? Math.round((primaryValue / baseVal) * 100) : 0;
            }

            const card = document.createElement('div');
            card.className = 'stat-card';
            card.style.animationDelay = (index * 0.03) + 's';

            if (this.compareStats) {
                let compareValue = this.compareStats[key] ?? 0;
                if (pct && base) {
                    const baseVal = this.compareStats[base] ?? 0;
                    compareValue = baseVal > 0 ? Math.round((compareValue / baseVal) * 100) : 0;
                }

                card.classList.add('compare-card');
                
                const isPrimaryBetter = primaryValue > compareValue;
                const isCompareBetter = compareValue > primaryValue;

                card.innerHTML = `
                    <div class="stat-compare-values">
                        <span class="primary-val ${isPrimaryBetter ? 'winner' : (isCompareBetter ? 'loser' : '')}">${primaryValue}${suffix}</span>
                        <span class="compare-separator">vs</span>
                        <span class="compare-val ${isCompareBetter ? 'winner' : (isPrimaryBetter ? 'loser' : '')}">${compareValue}${suffix}</span>
                    </div>
                    <div class="stat-label">${icon} ${label}</div>
                `;
            } else {
                card.innerHTML = `
                    <div class="stat-value">${primaryValue}${suffix}</div>
                    <div class="stat-label">${icon} ${label}</div>
                `;
            }
            grid.appendChild(card);
        });
    }

    /* ── MÉTODOS AUXILIARES DE COMPARAÇÃO & FILTRO ────────────── */

    populateCompareSelect(primaryPlayerId) {
        this.compareSelector.innerHTML = '<option value="">Comparar com...</option>';
        if (!this.playersList || this.playersList.length === 0) {
            this.compareSelector.disabled = true;
            return;
        }

        this.playersList.forEach(p => {
            if (p.id !== primaryPlayerId) {
                const option = document.createElement('option');
                option.value = p.id;
                option.textContent = p.name;
                this.compareSelector.appendChild(option);
            }
        });
        this.compareSelector.disabled = false;
    }

    async loadComparison(compareId) {
        if (this.loading || compareId === this.comparePlayerId) return;
        this.comparePlayerId = compareId;
        this.showLoading();

        try {
            const data = await api.getDashboardData(compareId, this.currentMatchId);
            this.compareStats = data.stats;
            this.compareImages = data.images;

            // Renderiza mapas lado a lado
            this.renderComparisonImages(this.lastImages, this.compareImages);
            
            // Renderiza radar com sobreposição dos dois jogadores
            this.radar.render(this.lastStats, this.compareStats);

            // Atualiza o grid de estatísticas gerais no modo comparação
            this.renderStatsGrid(this.lastStats, document.querySelector('.stat-tab.active')?.dataset.group || 'all');

            // Habilita classes CSS do modo de comparação
            ['heatmap', 'shotmap', 'passmap'].forEach(type => {
                document.getElementById(`${type}-grid`).classList.add('compare-active');
                document.getElementById(`${type}-box-compare`).classList.remove('hidden');
                document.getElementById(`${type}-label-primary`).classList.remove('hidden');
            });

            // Insere os nomes nas labels dos mapas
            const primaryName = this.selector.select.options[this.selector.select.selectedIndex]?.text || 'Jogador A';
            const compareName = this.compareSelector.options[this.compareSelector.selectedIndex]?.text || 'Jogador B';
            
            ['heatmap', 'shotmap', 'passmap'].forEach(type => {
                document.getElementById(`${type}-label-primary`).textContent = primaryName;
                document.getElementById(`${type}-label-compare`).textContent = compareName;
            });

            this.hideLoading();
            this.compareSelector.disabled = false;
        } catch (error) {
            console.error('Error loading comparison:', error);
            this.hideLoading();
            this.compareSelector.disabled = false;
            this.showError('Erro ao carregar comparação');
        }
    }

    clearComparison() {
        this.comparePlayerId = null;
        this.compareStats = null;
        this.compareImages = null;
        this.compareSelector.value = '';

        // Remove classes de comparação e esconde os elementos do segundo jogador
        ['heatmap', 'shotmap', 'passmap'].forEach(type => {
            const grid = document.getElementById(`${type}-grid`);
            if (grid) grid.classList.remove('compare-active');
            
            const compareBox = document.getElementById(`${type}-box-compare`);
            if (compareBox) compareBox.classList.add('hidden');
            
            const primaryLabel = document.getElementById(`${type}-label-primary`);
            if (primaryLabel) primaryLabel.classList.add('hidden');
        });

        // Re-renderiza o radar e as estatísticas apenas com o jogador principal
        if (this.lastStats) {
            this.radar.render(this.lastStats);
            this.renderStatsGrid(this.lastStats, document.querySelector('.stat-tab.active')?.dataset.group || 'all');
        }
    }

    renderComparisonImages(primaryImages, compareImages) {
        ['heatmap', 'shotmap', 'passmap'].forEach(type => {
            const primaryImg = document.getElementById(`${type}-img`);
            const compareImg = document.getElementById(`${type}-compare-img`);
            const placeholder = document.getElementById(`${type}-placeholder`);

            const hasPrimary = !!primaryImages?.[type];
            const hasCompare = !!compareImages?.[type];

            if (hasPrimary || hasCompare) {
                placeholder.classList.remove('active');
                
                if (hasPrimary) {
                    primaryImg.src = 'data:image/png;base64,' + primaryImages[type];
                    primaryImg.classList.remove('hidden');
                } else {
                    primaryImg.classList.add('hidden');
                }
                
                if (hasCompare) {
                    compareImg.src = 'data:image/png;base64,' + compareImages[type];
                    compareImg.classList.remove('hidden');
                } else {
                    compareImg.classList.add('hidden');
                }
            } else {
                primaryImg.classList.add('hidden');
                compareImg.classList.add('hidden');
                placeholder.classList.add('active');
            }
        });
    }

    initEventFilters() {
        document.querySelectorAll('.event-filter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.event-filter-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.activeEventFilter = btn.dataset.filter;
                if (this.lastEvents && this.lastStats) {
                    this.renderEvents(this.lastEvents, this.lastStats);
                }
            });
        });
    }
}
