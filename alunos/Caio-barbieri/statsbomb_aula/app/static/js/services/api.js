/**
 * CBF Academy - Statsbomb World Cup 2022
 * API Service for client-side data fetching
 */

export async function fetchMatches() {
    try {
        const response = await fetch('/api/matches');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data.matches || [];
    } catch (error) {
        console.error('Failed to fetch matches:', error);
        throw error;
    }
}

export async function fetchMatchDetails(matchId) {
    try {
        const response = await fetch(`/api/matches/${matchId}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Failed to fetch match details for match ${matchId}:`, error);
        throw error;
    }
}
