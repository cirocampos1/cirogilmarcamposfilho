import { api } from '../services/api.js';
import { PlayerSelector } from './PlayerSelector.js';
import { StatsRadar } from './StatsRadar.js';

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
        this.matchSelect = document.getElementById('match-select');
        this.selectorA = new PlayerSelector(
            document.getElementById('player-select-a')
        );
        this.selectorB = new PlayerSelector(
            document.getElementById('player-select-b')
        );
        this.radar = new StatsRadar(
            document.getElementById('stats-radar')
        );
        this.currentMatchId = null;
        this.currentPlayerIdA = null;
        this.currentPlayerIdB = null;
        this.lastStatsA = null;
        this.lastStatsB = null;
        this.loadingA = false;
        this.loadingB = false;
    }

    async init() {
        try {
            // 1. Carregar lista de partidas do backend
            const matches = await api.getMatches();
            this.matchSelect.innerHTML = '';
            
            if (matches.length === 0) {
                const option = document.createElement('option');
                option.value = '';
                option.textContent = 'Nenhuma partida disponível';
                this.matchSelect.appendChild(option);
                this.matchSelect.disabled = true;
                return;
            }

            matches.forEach(m => {
                const option = document.createElement('option');
                option.value = m.match_id;
                option.textContent = `${m.home_team} ${m.home_score} x ${m.away_score} ${m.away_team} (${m.match_date}) — ${m.competition}`;
                this.matchSelect.appendChild(option);
            });

            this.matchSelect.disabled = false;
            
            // ID inicial: Sofascore se existir, ou o primeiro
            this.currentMatchId = matches[0].match_id;
            const sofascoreMatch = matches.find(m => String(m.match_id) === '15691379');
            if (sofascoreMatch) {
                this.matchSelect.value = '15691379';
                this.currentMatchId = '15691379';
            }

            this.matchSelect.addEventListener('change', async (e) => {
                this.currentMatchId = e.target.value;
                await this.onMatchChange();
            });

            this.selectorA.onChange(async (playerId) => {
                await this.loadPlayer(playerId, 'a');
            });
            this.selectorB.onChange(async (playerId) => {
                await this.loadPlayer(playerId, 'b');
            });

            this.initStatTabs();
            
            // Inicializa a partida
            await this.onMatchChange();

        } catch (error) {
            console.error('Error initializing dashboard:', error);
            this.showError('Falha ao inicializar dashboard');
        }
    }

    async onMatchChange() {
        this.currentPlayerIdA = null;
        this.currentPlayerIdB = null;
        this.lastStatsA = null;
        this.lastStatsB = null;

        // Se for a partida de demo Sofascore, sugere Igor Thiago (1016907) e Vinicius Jr (868812)
        let defaultIdA = '';
        let defaultIdB = '';
        if (String(this.currentMatchId) === '15691379') {
            defaultIdA = '1016907';
            defaultIdB = '868812';
        }

        const initialPlayerIdA = await this.selectorA.load(defaultIdA, this.currentMatchId);
        const initialPlayerIdB = await this.selectorB.load(defaultIdB, this.currentMatchId);

        if (!initialPlayerIdA && !initialPlayerIdB) return;

        await Promise.all([
            initialPlayerIdA ? this.loadPlayer(initialPlayerIdA, 'a') : Promise.resolve(),
            initialPlayerIdB ? this.loadPlayer(initialPlayerIdB, 'b') : Promise.resolve()
        ]);

        this.updateSelectOptions();
    }

    updateSelectOptions() {
        const valA = this.selectorA.select.value;
        const valB = this.selectorB.select.value;
        
        Array.from(this.selectorA.select.options).forEach(opt => {
            if (opt.value !== '') {
                opt.disabled = (opt.value === valB);
            }
        });
        
        Array.from(this.selectorB.select.options).forEach(opt => {
            if (opt.value !== '') {
                opt.disabled = (opt.value === valA);
            }
        });
    }

    initStatTabs() {
        document.querySelectorAll('.stat-tab').forEach(tab => {
            tab.addEventListener('click', () => {
                document.querySelectorAll('.stat-tab').forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                const group = tab.dataset.group;
                if (this.lastStatsA) this.renderStatsGrid(this.lastStatsA, group, 'a');
                if (this.lastStatsB) this.renderStatsGrid(this.lastStatsB, group, 'b');
            });
        });
    }

    showLoading(side) {
        if (side === 'a') this.loadingA = true;
        if (side === 'b') this.loadingB = true;

        document.querySelectorAll(`#heatmap-skeleton-${side}, #shotmap-skeleton-${side}, #passmap-skeleton-${side}`).forEach(s => s.classList.add('active'));
        document.getElementById(`stats-skeleton-${side}`).classList.add('active');
        document.getElementById(`events-skeleton-${side}`).classList.add('active');
        
        // Hide actual images while loading
        ['heatmap', 'shotmap', 'passmap', 'pizza'].forEach(type => {
            const img = document.getElementById(`${type}-img-${side}`);
            if (img) img.classList.add('hidden');
            const placeholder = document.getElementById(`${type}-placeholder-${side}`);
            if (placeholder) placeholder.classList.remove('active');
        });



        document.getElementById(`stats-grid-${side}`).innerHTML = '';
        document.getElementById(`events-grid-${side}`).classList.add('hidden');
        document.getElementById(`events-empty-${side}`).classList.add('hidden');
    }

    hideLoading(side) {
        if (side === 'a') this.loadingA = false;
        if (side === 'b') this.loadingB = false;

        document.querySelectorAll(`#heatmap-skeleton-${side}, #shotmap-skeleton-${side}, #passmap-skeleton-${side}`).forEach(s => s.classList.remove('active'));
        document.getElementById(`stats-skeleton-${side}`).classList.remove('active');
        document.getElementById(`events-skeleton-${side}`).classList.remove('active');
    }

    showError(message) {
        const toast = document.getElementById('error-toast');
        document.getElementById('error-message').textContent = message;
        toast.classList.remove('hidden');
        setTimeout(() => toast.classList.add('hidden'), 5000);
    }

    async loadPlayer(playerId, side) {
        const isLoading = side === 'a' ? this.loadingA : this.loadingB;
        const currentId = side === 'a' ? this.currentPlayerIdA : this.currentPlayerIdB;
        const selector = side === 'a' ? this.selectorA : this.selectorB;

        if (isLoading || !playerId || playerId === currentId) return;
        
        if (side === 'a') this.currentPlayerIdA = playerId;
        if (side === 'b') this.currentPlayerIdB = playerId;

        this.showLoading(side);

        try {
            const data = await api.getDashboardData(playerId, this.currentMatchId);
            if (side === 'a') this.lastStatsA = data.stats;
            if (side === 'b') this.lastStatsB = data.stats;

            this.renderImages(data.images, side);
            this.renderEvents(data.events, data.stats, side);
            
            const activeTab = document.querySelector('.stat-tab.active');
            const currentGroup = activeTab ? activeTab.dataset.group : 'all';
            this.renderStatsGrid(data.stats, currentGroup, side);
            this.renderPlayerInfo(data.stats, side);
            
            this.hideLoading(side);
            selector.enable();
            this.updateSelectOptions();

            // Render radar only when both or the currently needed are loaded
            if (this.lastStatsA && this.lastStatsB) {
                this.radar.render(this.lastStatsA, this.lastStatsB);
            } else if (this.lastStatsA && side === 'a') {
                this.radar.render(this.lastStatsA, null);
            } else if (this.lastStatsB && side === 'b') {
                this.radar.render(null, this.lastStatsB);
            }
        } catch (error) {
            console.error(`Error loading player dashboard for side ${side}:`, error);
            this.hideLoading(side);
            selector.enable();
            this.showError('Erro ao carregar dados do jogador');
        }
    }

    renderImages(images, side) {
        ['heatmap', 'shotmap', 'passmap', 'pizza'].forEach(type => {
            const img = document.getElementById(`${type}-img-${side}`);
            const placeholder = document.getElementById(`${type}-placeholder-${side}`);

            if (img && placeholder) {
                if (images?.[type]) {
                    img.src = 'data:image/png;base64,' + images[type];
                    img.alt = `${type} do jogador`;
                    img.classList.remove('hidden');
                    placeholder.classList.remove('active');
                } else {
                    img.classList.add('hidden');
                    placeholder.classList.add('active');
                }
            }
        });


    }

    renderEvents(events, stats, side) {
        const eventTypes = [
            { type: 'pass', icon: '⤴️', label: 'Passes', color: side === 'a' ? '#3b82f6' : '#ef4444' },
            { type: 'dribble', icon: '💨', label: 'Dribles', color: side === 'a' ? '#3b82f6' : '#ef4444' },
            { type: 'defensive', icon: '🛡️', label: 'Defensivas', color: side === 'a' ? '#3b82f6' : '#ef4444' },
            { type: 'ball_carry', icon: '🏃', label: 'Conduções', color: side === 'a' ? '#3b82f6' : '#ef4444' },
        ];

        const grid = document.getElementById(`events-grid-${side}`);
        const empty = document.getElementById(`events-empty-${side}`);
        let hasAny = false;
        
        grid.innerHTML = ''; // Clear previous

        eventTypes.forEach(({ type, icon, label, color }) => {
            const list = events?.[type] || [];
            
            if (list.length > 0) {
                hasAny = true;
                const success = list.filter(e => e.outcome !== false).length;
                const pct = Math.round((success / list.length) * 100);
                const width = Math.max(pct, type === 'defensive' ? 100 : (type === 'ball_carry' ? 80 : pct));
                
                let detailText = '';
                if (type === 'pass') {
                    const acc = stats?.accuratePass && stats?.totalPass
                        ? Math.round((stats.accuratePass / stats.totalPass) * 100) + '%'
                        : pct + '%';
                    detailText = `Precisão: ${acc}`;
                } else if (type === 'dribble') {
                    detailText = `Sucesso: ${pct}%`;
                } else if (type === 'defensive') {
                    detailText = `Ações: ${list.length}`;
                } else if (type === 'ball_carry') {
                    detailText = `Conduções: ${list.length}`;
                }

                grid.innerHTML += `
                    <div class="event-category" data-type="${type}">
                        <div class="event-header">
                            <span class="event-icon">${icon}</span>
                            <span class="event-label">${label}</span>
                            <span class="event-count">${list.length}</span>
                        </div>
                        <div class="event-bar-wrapper">
                            <div class="event-bar" style="width: ${width}%; background: ${color}"></div>
                        </div>
                        <div class="event-detail">${detailText}</div>
                    </div>
                `;
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

    renderPlayerInfo(stats, side) {
        const rating = stats.rating || '-';
        const mins = stats.minutesPlayed || '-';
        const info = document.getElementById(`player-info-${side}`);
        info.innerHTML = `
            <span class="info-badge">⭐ ${rating}</span>
            <span class="info-badge">⏱ ${mins} min</span>
            <span class="info-badge">⚽ ${stats.goals || 0} gols</span>
        `;
    }

    renderStatsGrid(stats, group, side) {
        const grid = document.getElementById(`stats-grid-${side}`);
        grid.innerHTML = '';
        
        // Atualizar o nome do jogador no cabeçalho de estatísticas
        const selector = side === 'a' ? this.selectorA : this.selectorB;
        const playerName = selector.select.options[selector.select.selectedIndex]?.text || (side === 'a' ? 'Jogador A' : 'Jogador B');
        const headerEl = document.getElementById(`player-stats-header-${side}`);
        if (headerEl) {
            headerEl.textContent = playerName;
        }
        
        let keysToShow = group === 'all' ? ALL_KEYS : STAT_GROUPS[group];
        const valColorClass = side === 'a' ? 'val-a' : 'val-b';
        
        keysToShow.forEach(({ key, label, icon, suffix, pct, base }) => {
            const value = stats[key] !== undefined ? stats[key] : 0;
            let displayValue = value + suffix;
            
            if (pct && base && stats[base]) {
                const percentage = Math.round((value / stats[base]) * 100);
                displayValue = percentage + '%';
            }
            
            grid.innerHTML += `
                <div class="stat-card">
                    <div class="stat-icon">${icon}</div>
                    <div class="stat-value ${valColorClass}">${displayValue}</div>
                    <div class="stat-label">${label}</div>
                </div>
            `;
        });
    }
}
