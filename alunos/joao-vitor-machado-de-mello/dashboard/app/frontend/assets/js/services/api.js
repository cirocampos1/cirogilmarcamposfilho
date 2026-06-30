class ApiClient {
    constructor(timeoutMs = 15000) {
        this.timeoutMs = timeoutMs;
    }

    async request(path) {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), this.timeoutMs);

        try {
            const response = await fetch(path, { signal: controller.signal });
            let data = {};
            try {
                data = await response.json();
            } catch (error) {
                data = {};
            }

            if (!response.ok) {
                const detail = data.detail || data.message || `HTTP ${response.status}`;
                throw new Error(detail);
            }

            return data;
        } catch (error) {
            if (error.name === 'AbortError') {
                throw new Error('Tempo limite excedido ao carregar dados');
            }
            throw error;
        } finally {
            clearTimeout(timeoutId);
        }
    }

    async getMatches() {
        const data = await this.request('/api/matches');
        return data.matches || [];
    }

    async getPlayers(matchId) {
        const query = matchId ? `?match_id=${encodeURIComponent(matchId)}` : '';
        const data = await this.request(`/api/players${query}`);
        return data.players || [];
    }

    async getDashboardData(playerId, matchId) {
        const params = new URLSearchParams({ player_id: playerId });
        if (matchId) params.set('match_id', matchId);
        return this.request(`/api/dashboard-data?${params.toString()}`);
    }

    async comparePlayers(playerIds, matchId) {
        const params = new URLSearchParams({ player_ids: playerIds.join(',') });
        if (matchId) params.set('match_id', matchId);
        return this.request(`/api/compare?${params.toString()}`);
    }
}

export const api = new ApiClient();
