import { api } from '../services/api.js?v=4';

export class PlayerSelector {
    constructor(selectElement) {
        this.select = selectElement;
        this.onChangeCallback = null;
    }

    async load(matchId, defaultPlayerId = '866469') {
        const players = await api.getPlayers(matchId);
        this.select.innerHTML = '';

        players.forEach(p => {
            const option = document.createElement('option');
            option.value = p.id;
            option.textContent = p.name;
            if (p.id === defaultPlayerId) {
                option.selected = true;
            }
            this.select.appendChild(option);
        });

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
