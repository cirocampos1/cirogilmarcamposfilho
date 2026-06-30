class ApiClient {
    async getMatches() {
        const response = await fetch('/api/matches');
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const data = await response.json();
        return data.matches || [];
    }

    async getPlayers(matchId) {
        const url = matchId ? `/api/players?match_id=${matchId}` : '/api/players';
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const data = await response.json();
        return data.players || [];
    }

    async getDashboardData(playerId, matchId) {
        const url = matchId 
            ? `/api/dashboard-data?player_id=${playerId}&match_id=${matchId}` 
            : `/api/dashboard-data?player_id=${playerId}`;
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
    }
}

export const api = new ApiClient();
