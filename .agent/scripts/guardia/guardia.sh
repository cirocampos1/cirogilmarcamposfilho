#!/usr/bin/env bash
# ==============================================================================
# 🛡️  GUARDIA — Sistema de Restore Points 
# ==============================================================================
# Uso:
#   ./guardia.sh save [nome]        → Cria restore point com tag git
#   ./guardia.sh list               → Lista todos os restore points
#   ./guardia.sh restore <tag>      → Restaura módulos de um restore point
#   ./guardia.sh diff <tag>         → Mostra o que mudou desde o restore point
#   ./guardia.sh status             → Mostra o último restore point criado
# ==============================================================================

set -euo pipefail

VERDE='\033[0;32m'
AMARELO='\033[1;33m'
VERMELHO='\033[0;31m'
AZUL='\033[0;34m'
RESET='\033[0m'
BOLD='\033[1m'

# Prefixo interno das tags (invisível para quem não sabe o que procurar)
TAG_PREFIX="rp"
LOG_FILE=".agent/scripts/guardia/.guardia.log"

_log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG_FILE"
}

_header() {
    echo -e "\n${AZUL}${BOLD}🛡️  Guardia —  Restore Points${RESET}"
    echo -e "${AZUL}────────────────────────────────────${RESET}\n"
}

_ok() { echo -e "${VERDE}✅  $*${RESET}"; }
_warn() { echo -e "${AMARELO}⚠️   $*${RESET}"; }
_err() { echo -e "${VERMELHO}❌  $*${RESET}"; }
_info() { echo -e "${AZUL}ℹ️   $*${RESET}"; }

# ==============================================================================
# SAVE — Cria um restore point (tag git local)
# ==============================================================================
cmd_save() {
    local nome="${1:-auto}"
    local timestamp
    timestamp=$(date '+%Y%m%d-%H%M%S')
    local tag="${TAG_PREFIX}/${timestamp}-${nome}"

    _header

    # Verifica se há mudanças não commitadas
    if ! git diff --quiet HEAD 2>/dev/null; then
        _warn "Há mudanças não commitadas. Saving stash snapshot também..."
        git stash push -m "guardia:${tag}" --quiet 2>/dev/null || true
        git stash pop --quiet 2>/dev/null || true
    fi

    # Cria a tag local (anotada com mensagem)
    local current_commit
    current_commit=$(git rev-parse HEAD)

    git tag -a "${tag}" "${current_commit}" \
        -m "Guardia RP: ${nome} | $(date '+%Y-%m-%d %H:%M') | commit: ${current_commit:0:8}" \
        2>/dev/null

    _ok "Restore point criado: ${BOLD}${tag}${RESET}"
    _info "Commit base: ${current_commit:0:12}"
    _log "SAVE tag=${tag} commit=${current_commit:0:12}"

    echo ""
    echo -e "${BOLD}  Para restaurar mais tarde:${RESET}"
    echo -e "  ${AMARELO}./guardia.sh restore ${tag}${RESET}"
    echo ""
}

# ==============================================================================
# LIST — Lista todos os restore points
# ==============================================================================
cmd_list() {
    _header

    local tags
    tags=$(git tag -l "${TAG_PREFIX}/*" | sort -r 2>/dev/null)

    if [[ -z "$tags" ]]; then
        _warn "Nenhum restore point encontrado."
        echo ""
        echo -e "  Crie um com: ${AZUL}./guardia.sh save [nome]${RESET}"
        return 0
    fi

    echo -e "${BOLD}  Restore Points disponíveis:${RESET}\n"

    local count=0
    while IFS= read -r tag; do
        count=$((count + 1))
        local msg
        msg=$(git tag -l -n1 "$tag" | awk '{for(i=2;i<=NF;i++) printf $i " "; print ""}' | sed 's/Guardia RP: //')

        if [[ $count -eq 1 ]]; then
            echo -e "  ${VERDE}${BOLD}→ ${tag}${RESET} ${BOLD}(MAIS RECENTE)${RESET}"
            echo -e "    ${msg}"
        else
            echo -e "  ${AZUL}  ${tag}${RESET}"
            echo -e "    ${msg}"
        fi
        echo ""
    done <<< "$tags"

    echo -e "  Total: ${BOLD}${count} restore point(s)${RESET}\n"
}

# ==============================================================================
# RESTORE — Restaura arquivos de módulos específicos
# ==============================================================================
cmd_restore() {
    local tag="${1:-}"

    if [[ -z "$tag" ]]; then
        _err "Especifique a tag para restaurar. Use: ./guardia.sh list"
        exit 1
    fi

    # Verifica se a tag existe
    if ! git tag -l "$tag" | grep -q "$tag"; then
        # Tenta com prefixo parcial
        local found
        found=$(git tag -l "${TAG_PREFIX}/*" | grep "$tag" | head -1)
        if [[ -z "$found" ]]; then
            _err "Tag '${tag}' não encontrada. Use: ./guardia.sh list"
            exit 1
        fi
        tag="$found"
    fi

    _header
    echo -e "${BOLD}  Restaurando a partir de: ${AMARELO}${tag}${RESET}\n"

    # Módulos protegidos (adicione os seus aqui)
    local modulos=(
        "app/routers"
        "app/services"
        "app/repositories"
        "app/schemas"
        "app/templates"
        "app/static"
    )

    echo -e "  Módulos que serão restaurados:"
    for m in "${modulos[@]}"; do
        echo -e "  ${AZUL}  • ${m}${RESET}"
    done
    echo ""

    read -rp "  ⚠️  Confirma restauração? (s/N): " confirm
    if [[ "$confirm" != "s" && "$confirm" != "S" ]]; then
        _warn "Operação cancelada."
        exit 0
    fi

    echo ""
    local restored=0
    for modulo in "${modulos[@]}"; do
        if git show "${tag}:${modulo}" &>/dev/null 2>&1 || git ls-tree -r "${tag}" --name-only | grep -q "^${modulo}/"; then
            git checkout "${tag}" -- "${modulo}" 2>/dev/null && {
                _ok "Restaurado: ${modulo}"
                restored=$((restored + 1))
            } || _warn "Skipped (não encontrado no snapshot): ${modulo}"
        fi
    done

    echo ""
    _ok "Restauração concluída! ${restored} módulo(s) restaurados."
    _log "RESTORE tag=${tag} modules=${restored}"
    echo ""
    echo -e "  ${BOLD}Próximo passo:${RESET} Reinicie o servidor FastAPI para aplicar as mudanças."
    echo ""
}

# ==============================================================================
# DIFF — Mostra o que mudou desde um restore point
# ==============================================================================
cmd_diff() {
    local tag="${1:-}"

    if [[ -z "$tag" ]]; then
        # Usa o mais recente
        tag=$(git tag -l "${TAG_PREFIX}/*" | sort -r | head -1)
        if [[ -z "$tag" ]]; then
            _err "Nenhum restore point encontrado."
            exit 1
        fi
        _info "Usando restore point mais recente: ${tag}"
    fi

    _header
    echo -e "${BOLD}  Mudanças desde: ${AMARELO}${tag}${RESET}\n"

    git diff "${tag}" HEAD -- \
        app/routers/ \
        app/services/ \
        app/repositories/ \
        app/schemas/ \
        app/templates/ \
        --stat 2>/dev/null

    echo ""

    # Lista arquivos modificados pelos outros
    local changed
    changed=$(git diff "${tag}" HEAD --name-only -- app/ 2>/dev/null | wc -l | tr -d ' ')
    
    if [[ "$changed" -eq 0 ]]; then
        _ok "Nenhuma mudança nos módulos desde o restore point."
    else
        echo -e "  ${AMARELO}${BOLD}${changed} arquivo(s) modificado(s) nos módulos desde o último restore point.${RESET}"
        echo ""
        echo -e "  Para restaurar: ${AZUL}./guardia.sh restore ${tag}${RESET}"
    fi
    echo ""
}

# ==============================================================================
# STATUS — Estado atual
# ==============================================================================
cmd_status() {
    _header

    local ultimo
    ultimo=$(git tag -l "${TAG_PREFIX}/*" | sort -r | head -1 2>/dev/null || echo "")

    if [[ -z "$ultimo" ]]; then
        _warn "Nenhum restore point criado ainda."
        echo -e "  Crie agora: ${AZUL}./guardia.sh save stable${RESET}"
        return 0
    fi

    local commit_rp
    commit_rp=$(git rev-parse "${ultimo}")
    local commit_atual
    commit_atual=$(git rev-parse HEAD)

    echo -e "  ${BOLD}Último restore point:${RESET} ${VERDE}${ultimo}${RESET}"
    echo -e "  ${BOLD}Commit do RP:${RESET}        ${commit_rp:0:12}"
    echo -e "  ${BOLD}Commit atual:${RESET}        ${commit_atual:0:12}"
    echo ""

    local commits_desde
    commits_desde=$(git rev-list "${ultimo}..HEAD" --count 2>/dev/null || echo "0")

    if [[ "$commits_desde" -eq 0 ]]; then
        _ok "Você está no restore point mais recente."
    else
        _warn "${commits_desde} commit(s) feito(s) desde o último restore point."
    fi

    local arquivos_mudados
    arquivos_mudados=$(git diff "${ultimo}" HEAD --name-only -- app/ 2>/dev/null | wc -l | tr -d ' ')
    
    if [[ "$arquivos_mudados" -gt 0 ]]; then
        echo -e "  ${AMARELO}  • ${arquivos_mudados} arquivo(s) de módulo modificados${RESET}"
        echo ""
        echo -e "  Para ver o que mudou: ${AZUL}./guardia.sh diff${RESET}"
        echo -e "  Para criar novo RP:   ${AZUL}./guardia.sh save [nome]${RESET}"
    fi
    echo ""
}

# ==============================================================================
# MAIN
# ==============================================================================
mkdir -p "$(dirname "$LOG_FILE")"

case "${1:-help}" in
    save)    cmd_save "${2:-auto}" ;;
    list)    cmd_list ;;
    restore) cmd_restore "${2:-}" ;;
    diff)    cmd_diff "${2:-}" ;;
    status)  cmd_status ;;
    help|*)
        _header
        echo -e "  ${BOLD}Comandos disponíveis:${RESET}\n"
        echo -e "  ${AZUL}./guardia.sh save [nome]${RESET}        Cria restore point (default: 'auto')"
        echo -e "  ${AZUL}./guardia.sh list${RESET}               Lista todos os restore points"
        echo -e "  ${AZUL}./guardia.sh status${RESET}             Estado atual vs último RP"
        echo -e "  ${AZUL}./guardia.sh diff [tag]${RESET}         Ver mudanças desde um RP"
        echo -e "  ${AZUL}./guardia.sh restore <tag>${RESET}      Restaurar módulos para um RP"
        echo ""
        ;;
esac
