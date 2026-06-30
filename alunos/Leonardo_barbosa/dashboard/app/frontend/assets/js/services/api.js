class ApiClient {
    async request(path) {
        const response = await fetch(path);
        if (!response.ok) {
            let msg = `Erro no servidor (HTTP ${response.status})`;
            try {
                const data = await response.json();
                if (data && data.detail) msg = data.detail;
            } catch (e) {}
            throw new Error(msg);
        }
        return response.json();
    }

    async getMatches() {
        const data = await this.request('/api/matches');
        return data.matches || [];
    }

    async getPlayers(matchId) {
        const query = matchId ? `?match_id=${matchId}` : '';
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

    async getMatchMoments(matchId) {
        const query = matchId ? `?match_id=${matchId}` : '';
        const data = await this.request(`/api/match-moments${query}`);
        return data.moments || [];
    }

    async getPlayersByPosition(matchId, position) {
        const params = new URLSearchParams();
        if (matchId) params.set('match_id', matchId);
        if (position && position !== 'all') params.set('position', position);
        const data = await this.request(`/api/players-by-position?${params.toString()}`);
        return data.players || [];
    }

    async getTeamShotmap(matchId, team) {
        const params = new URLSearchParams();
        if (matchId) params.set('match_id', matchId);
        if (team) params.set('team', team);
        return this.request(`/api/team-shotmap?${params.toString()}`);
    }
}

export const api = new ApiClient();
