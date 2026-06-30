class ApiClient {
    async request(url) {
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Erro do servidor (${response.status})`);
            }
            return await response.json();
        } catch (error) {
            console.error(`Falha ao requisitar ${url}:`, error);
            if (error.message.includes('Erro do servidor')) {
                throw error;
            }
            throw new Error('Sem conexão com o backend. Verifique se o servidor FastAPI está rodando.');
        }
    }

    async getMatches() {
        const data = await this.request('/api/matches');
        return data.matches || [];
    }

    async getPlayers(matchId) {
        const url = matchId ? `/api/players?match_id=${matchId}` : '/api/players';
        const data = await this.request(url);
        return data.players || [];
    }

    async getDashboardData(playerId, matchId) {
        const url = matchId 
            ? `/api/dashboard-data?player_id=${playerId}&match_id=${matchId}` 
            : `/api/dashboard-data?player_id=${playerId}`;
        return this.request(url);
    }
}

export const api = new ApiClient();
