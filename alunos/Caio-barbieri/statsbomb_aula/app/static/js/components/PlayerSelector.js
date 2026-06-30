/**
 * CBF Academy - Statsbomb World Cup 2022
 * Component to populate and manage player selectors for comparison
 */

export class PlayerSelector {
    constructor(selectElement1Id, selectElement2Id, onChangeCallback) {
        this.select1 = document.getElementById(selectElement1Id);
        this.select2 = document.getElementById(selectElement2Id);
        this.onChangeCallback = onChangeCallback;
        
        if (this.select1 && this.select2) {
            this.select1.addEventListener('change', () => this.handleSelectionChange());
            this.select2.addEventListener('change', () => this.handleSelectionChange());
        }
    }

    /**
     * Populate selectors with players grouped by team
     * @param {Object} playerStats Dictionary of player stats from API
     * @param {string} homeTeam Name of the home team
     * @param {string} awayTeam Name of the away team
     */
    populate(playerStats, homeTeam, awayTeam) {
        if (!this.select1 || !this.select2) return;

        // Reset selectors
        this.select1.innerHTML = '<option value="" disabled selected>Selecionar Jogador 1</option>';
        this.select2.innerHTML = '<option value="" disabled selected>Selecionar Jogador 2</option>';

        // Group players by team
        const homePlayers = [];
        const awayPlayers = [];

        Object.values(playerStats).forEach(player => {
            if (player.team === homeTeam) {
                homePlayers.push(player);
            } else {
                awayPlayers.push(player);
            }
        });

        // Sort alphabetically
        homePlayers.sort((a, b) => a.name.localeCompare(b.name));
        awayPlayers.sort((a, b) => a.name.localeCompare(b.name));

        // Create options string
        const createGroupedOptions = (placeholder) => {
            let html = `<option value="" disabled selected>${placeholder}</option>`;
            
            if (homePlayers.length > 0) {
                html += `<optgroup label="${homeTeam}">`;
                homePlayers.forEach(p => {
                    html += `<option value="${p.player_id}">${p.name}</option>`;
                });
                html += `</optgroup>`;
            }

            if (awayPlayers.length > 0) {
                html += `<optgroup label="${awayTeam}">`;
                awayPlayers.forEach(p => {
                    html += `<option value="${p.player_id}">${p.name}</option>`;
                });
                html += `</optgroup>`;
            }
            return html;
        };

        this.select1.innerHTML = createGroupedOptions('Selecionar Jogador 1');
        this.select2.innerHTML = createGroupedOptions('Selecionar Jogador 2');
        
        // Auto select first player from home and first from away if available
        if (homePlayers.length > 0) {
            this.select1.value = homePlayers[0].player_id;
        }
        if (awayPlayers.length > 0) {
            this.select2.value = awayPlayers[0].player_id;
        }

        // Trigger change callback initially
        this.handleSelectionChange();
    }

    handleSelectionChange() {
        const val1 = this.select1.value;
        const val2 = this.select2.value;
        if (this.onChangeCallback) {
            this.onChangeCallback(val1, val2);
        }
    }
}
