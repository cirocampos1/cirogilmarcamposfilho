import { api } from '../services/api.js';

export class PlayerSelector {
    constructor(selectElement) {
        this.select = selectElement;
        this.onChangeCallback = null;
    }

    async load(defaultPlayerId = '866469', matchId = null) {
        const players = await api.getPlayers(matchId);
        this.select.innerHTML = '';

        if (players.length === 0) {
            const option = document.createElement('option');
            option.value = '';
            option.textContent = 'Nenhum jogador';
            this.select.appendChild(option);
            this.select.disabled = true;
            return '';
        }

        players.forEach(p => {
            const option = document.createElement('option');
            option.value = p.id;
            option.textContent = p.name;
            if (p.id === defaultPlayerId) {
                option.selected = true;
            }
            this.select.appendChild(option);
        });

        // Caso o defaultPlayerId não exista nessa lista de jogadores, seleciona o primeiro
        if (!players.some(p => p.id === defaultPlayerId)) {
            this.select.selectedIndex = 0;
        }

        this.select.disabled = false;
        return this.select.value;
    }

    onChange(callback) {
        this.onChangeCallback = callback;
        this.select.addEventListener('change', (e) => {
            this.select.disabled = true;
            setTimeout(() => {
                this.onChangeCallback(e.target.value);
            }, 100);
        });
    }

    enable() {
        this.select.disabled = false;
    }
}
