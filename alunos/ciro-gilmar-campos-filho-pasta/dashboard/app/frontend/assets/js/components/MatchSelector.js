import { api } from '../services/api.js?v=4';

export class MatchSelector {
    constructor(selectElement) {
        this.select = selectElement;
        this.onChangeCallback = null;
    }

    async load(defaultMatchId = '15186850') {
        const matches = await api.getMatches();
        this.select.innerHTML = '';

        let foundDefault = false;
        matches.forEach(m => {
            const option = document.createElement('option');
            option.value = m.match_id;
            const comp = m.competition ? ` - ${m.competition}` : '';
            option.textContent = `${m.home_team} vs ${m.away_team}${comp}`;
            if (m.match_id.toString() === defaultMatchId.toString()) {
                option.selected = true;
                foundDefault = true;
            }
            this.select.appendChild(option);
        });

        if (!foundDefault && matches.length > 0) {
            this.select.options[0].selected = true;
            defaultMatchId = matches[0].match_id;
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
