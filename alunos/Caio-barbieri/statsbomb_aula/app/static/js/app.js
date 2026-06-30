/**
 * CBF Academy - Statsbomb World Cup 2022
 * Main entry point coordinating page loading, matches selection and components
 */

import { fetchMatches, fetchMatchDetails } from './services/api.js';
import { PlayerSelector } from './components/PlayerSelector.js';
import { StatsRadar } from './components/StatsRadar.js';

let currentMatchPlayersStats = {};
let playerSelectorInstance = null;
let statsRadarInstance = null;

document.addEventListener('DOMContentLoaded', async () => {
    // Initial UI Elements
    const listEl = document.getElementById('match-list');
    const loadingEl = document.getElementById('loading-matches');
    
    // Initialize Radar instance
    statsRadarInstance = new StatsRadar('radar-canvas');

    // Initialize PlayerSelector instance
    playerSelectorInstance = new PlayerSelector(
        'player1-select',
        'player2-select',
        (player1Id, player2Id) => {
            const p1 = currentMatchPlayersStats[player1Id] || null;
            const p2 = currentMatchPlayersStats[player2Id] || null;
            statsRadarInstance.update(p1, p2, currentMatchPlayersStats);
        }
    );

    try {
        const matches = await fetchMatches();
        if (loadingEl) loadingEl.style.display = 'none';

        if (matches && matches.length > 0) {
            matches.forEach(match => {
                const div = document.createElement('div');
                div.className = 'p-3 rounded-xl border border-slate-700/50 hover-glass group transition-all duration-300 transform hover:-translate-y-0.5';
                div.onclick = () => loadMatch(match.match_id, `${match.home_team} vs ${match.away_team}`, match.match_date, match.home_team, match.away_team);
                
                div.innerHTML = `
                    <p class="font-semibold text-slate-200 group-hover:text-emerald-400 transition-colors">${match.home_team} <span class="text-slate-500 font-normal">vs</span> ${match.away_team}</p>
                    <p class="text-xs text-slate-500 mt-1">${match.match_date}</p>
                `;
                listEl.appendChild(div);
            });
        } else {
            listEl.innerHTML = '<p class="text-center text-slate-500 py-4">Nenhuma partida encontrada. Certifique-se de ter executado a ingestão de dados.</p>';
        }
    } catch (err) {
        console.error(err);
        if (loadingEl) {
            loadingEl.innerHTML = '<span class="text-rose-400">Erro ao carregar partidas da API.</span>';
        }
    }
});

async function loadMatch(matchId, title, date, homeTeam, awayTeam) {
    const emptyState = document.getElementById('empty-state');
    const matchDetails = document.getElementById('match-details');
    const loadingOverlay = document.getElementById('loading-overlay');
    
    if (emptyState) emptyState.classList.add('hidden');
    if (matchDetails) matchDetails.classList.remove('hidden');
    if (loadingOverlay) loadingOverlay.classList.remove('hidden');

    // Reset Map placeholders
    document.getElementById('shotmap-container').innerHTML = '<div class="animate-pulse w-full h-full bg-slate-800 rounded-xl min-h-[300px]"></div>';
    document.getElementById('passmap-container').innerHTML = '<div class="animate-pulse w-full h-full bg-slate-800 rounded-xl min-h-[300px]"></div>';
    document.getElementById('xgflow-container').innerHTML = '<div class="animate-pulse w-full h-full bg-slate-800 rounded-xl min-h-[300px]"></div>';
    document.getElementById('pressuremap-container').innerHTML = '<div class="animate-pulse w-full h-full bg-slate-800 rounded-xl min-h-[300px]"></div>';

    try {
        const data = await fetchMatchDetails(matchId);
        
        if (data.summary) {
            document.getElementById('match-score').innerText = `${title} (${data.summary.score})`;
            document.getElementById('match-date-time').innerText = `${data.summary.date} às ${data.summary.kick_off}`;
            document.getElementById('match-stadium').innerText = data.summary.stadium || "-";
            document.getElementById('match-stage').innerText = data.summary.competition_stage || "-";
            document.getElementById('match-referee').innerText = data.summary.referee || "-";
            
            const homeManager = data.summary.home_manager ? (data.summary.home_manager[0]?.name || data.summary.home_manager) : "-";
            const awayManager = data.summary.away_manager ? (data.summary.away_manager[0]?.name || data.summary.away_manager) : "-";
            document.getElementById('match-managers').innerText = `${homeManager} vs ${awayManager}`;

            document.getElementById('stat-shots').innerText = data.summary.total_shots;
            document.getElementById('stat-passes').innerText = data.summary.total_passes;

            if (data.summary.advanced_metrics) {
                const m = data.summary.advanced_metrics;
                
                const homeXg = m.home && typeof m.home.xg === 'number' ? m.home.xg.toFixed(2) : "0.00";
                const awayXg = m.away && typeof m.away.xg === 'number' ? m.away.xg.toFixed(2) : "0.00";
                const homePpda = m.home && typeof m.home.ppda === 'number' ? m.home.ppda.toFixed(1) : "0.0";
                const awayPpda = m.away && typeof m.away.ppda === 'number' ? m.away.ppda.toFixed(1) : "0.0";
                
                document.getElementById('stat-xg').innerText = `${homeXg} - ${awayXg}`;
                document.getElementById('stat-turnovers').innerText = `${m.home?.high_turnovers || 0} - ${m.away?.high_turnovers || 0}`;
                document.getElementById('stat-ppda').innerText = `${homePpda} - ${awayPpda}`;
                document.getElementById('stat-pressure-home').innerText = `${m.home?.passes_under_pressure_completed || 0} / ${m.home?.passes_under_pressure_total || 0}`;
                document.getElementById('stat-pressure-away').innerText = `${m.away?.passes_under_pressure_completed || 0} / ${m.away?.passes_under_pressure_total || 0}`;
            }
        }
        
        // Render base64 plots
        if (data.images) {
            if (data.images.shotmap) {
                document.getElementById('shotmap-container').innerHTML = `<img src="data:image/png;base64,${data.images.shotmap}" class="w-full h-auto object-contain rounded-xl" alt="Shot Map" />`;
            }
            if (data.images.pass_network) {
                document.getElementById('passmap-container').innerHTML = `<img src="data:image/png;base64,${data.images.pass_network}" class="w-full h-auto object-contain rounded-xl" alt="Pass Map" />`;
            }
            if (data.images.xg_flow) {
                document.getElementById('xgflow-container').innerHTML = `<img src="data:image/png;base64,${data.images.xg_flow}" class="w-full h-auto object-contain rounded-xl" alt="xG Flow Map" />`;
            }
            if (data.images.pressure_heatmap) {
                document.getElementById('pressuremap-container').innerHTML = `<img src="data:image/png;base64,${data.images.pressure_heatmap}" class="w-full h-auto object-contain rounded-xl" alt="Pressure Map" />`;
            }
        }

        // Store active players statistics globally for comparison
        currentMatchPlayersStats = data.player_stats || {};

        // Populate player selectors
        playerSelectorInstance.populate(currentMatchPlayersStats, homeTeam, awayTeam);

    } catch (err) {
        console.error(err);
        alert("Erro ao analisar partida. Verifique se os dados estão corretos no servidor FastAPI.");
    } finally {
        if (loadingOverlay) loadingOverlay.classList.add('hidden');
    }
}
