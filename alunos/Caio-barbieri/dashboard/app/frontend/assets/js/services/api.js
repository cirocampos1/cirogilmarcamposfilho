class ApiClient {
    async getMatches() {
        const response = await fetch('/api/matches');
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const data = await response.json();
        return data.matches || [];
    }

    async getPlayers(matchId = null) {
        const url = matchId ? `/api/players?match_id=${matchId}` : '/api/players';
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const data = await response.json();
        return data.players || [];
    }

    async getDashboardData(playerId, matchId = null, comparePlayerId = null) {
        let url = `/api/dashboard-data?player_id=${playerId}`;
        if (matchId) url += `&match_id=${matchId}`;
        if (comparePlayerId) url += `&compare_player_id=${comparePlayerId}`;
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
    }
}

export const api = new ApiClient();
