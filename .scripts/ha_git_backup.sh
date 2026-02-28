#!/bin/bash
set -euo pipefail

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ CONFIGURATION & LOGGING                                                  │
# ╰──────────────────────────────────────────────────────────────────────────╯
LOG_DIR="/config/.logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/ha_git_backup.log"

# Rotation simple : on garde les 1000 dernières lignes
if [[ -f "$LOG_FILE" ]]; then
    tail -n 1000 "$LOG_FILE" > "${LOG_FILE}.tmp" && mv "${LOG_FILE}.tmp" "$LOG_FILE"
fi

# Fonction de log (écrit dans le fichier et reste silencieux en console pour HA)
log() { printf '%s %s\n' "$(date '+%F %T %Z')" "$*" >> "$LOG_FILE"; }

cd /config || { echo "❌ /config introuvable"; exit 1; }

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ GARDE-FOUS GIT                                                           │
# ╰──────────────────────────────────────────────────────────────────────────╯
CUR_BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo main)"
if [[ "$CUR_BRANCH" == "master" ]]; then
    log "❌ Sur la branche master — ABANDON (protégée)"
    exit 1
fi

# Sécurité pour les répertoires distants (utile sur x86)
git config --global --add safe.directory /config || true

# Config utilisateur par défaut
git config user.name  >/dev/null 2>&1 || git config user.name  "BerrySwann (HAOS)"
git config user.email >/dev/null 2>&1 || git config user.email "BerrySwann@users.noreply.github.com"

# Sécurité critique : on ne push JAMAIS les secrets
if git ls-files --error-unmatch secrets.yaml >/dev/null 2>&1; then
    log "❌ secrets.yaml est tracké par git — ABANDON POUR SÉCURITÉ"
    exit 1
fi

git remote get-url origin >/dev/null 2>&1 || { log "❌ Remote 'origin' absent"; exit 1; }
BRANCH="$CUR_BRANCH"

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ RÈGLE SENS UNIQUE : HA → GITHUB                                          │
# │ git fetch / git pull / git merge sont INTERDITS dans ce script.          │
# │ GitHub ne met jamais à jour /config. Push uniquement.                    │
# ╰──────────────────────────────────────────────────────────────────────────╯

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ PRÉPARATION DU MESSAGE & VERSION                                         │
# ╰──────────────────────────────────────────────────────────────────────────╯
INPUT_ARG="${1:-}"
HA_VER=""
if command -v ha >/dev/null 2>&1; then
    HA_VER="$(ha core info 2>/dev/null | sed -n 's/.*"version": *"\([^"]*\)".*/\1/p' | head -n1 || true)"
elif [[ -f /config/.HA_VERSION ]]; then
    HA_VER="$(cat /config/.HA_VERSION 2>/dev/null || true)"
fi

IS_WEEKLY="false"
if [[ "$INPUT_ARG" == "weekly" ]]; then
    MSG="HAOS weekly backup: $(date '+%Y-%m-%d %H:%M:%S')${HA_VER:+ (HA ${HA_VER})}"
    IS_WEEKLY="true"
elif [[ -n "$INPUT_ARG" ]]; then
    MSG="$INPUT_ARG"
else
    MSG="HAOS auto-backup: $(date '+%Y-%m-%d %H:%M:%S')${HA_VER:+ (HA ${HA_VER})}"
fi

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ COMMIT & PUSH                                                            │
# ╰──────────────────────────────────────────────────────────────────────────╯
git add -A
if git commit -m "$MSG" >/dev/null 2>&1; then
    log "📝 Commit créé : $MSG"
    # [2026-02-28 modif] Capture erreur push dans variable pour logging réel
    if PUSH_ERR=$(git push origin "$BRANCH" 2>&1); then
        log "✅ Push réussi sur $BRANCH"
    else
        log "⚠️  Echec push $BRANCH : $PUSH_ERR"
        if PUSH_ERR2=$(git push origin main 2>&1); then
            log "✅ Push réussi sur main (fallback)"
        else
            log "❌ Push impossible : $PUSH_ERR2"
        fi
    fi
else
    log "✅ État déjà à jour (rien à committer)"
fi

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ GESTION DU TAG WEEKLY                                                    │
# ╰──────────────────────────────────────────────────────────────────────────╯
if [[ "$IS_WEEKLY" == "true" ]]; then
    # fetch tags uniquement — pas de pull contenu
    # [2026-02-28 modif] Suppression -q : erreur visible dans le log
    git fetch --tags 2>/dev/null || log "⚠️  fetch --tags échoué (tags locaux uniquement)"

    TAG_BASE="weekly-$(date +'%G-W%V')"
    TAG="$TAG_BASE"

    # Gestion des doublons de tags la même semaine
    if git rev-parse -q --verify "refs/tags/${TAG}" >/dev/null 2>&1; then
        TAG="${TAG_BASE}-$(date +'%H%M')"
    fi

    # [2026-02-28 modif] Capture erreur push tag — plus de silence sur échec
    if git tag -a "$TAG" -m "Weekly backup $(date +'%F')${HA_VER:+ (HA ${HA_VER})}"; then
        if TAG_ERR=$(git push origin "$TAG" 2>&1); then
            log "🏷️  Tag créé et poussé : $TAG"
        else
            log "❌ Push tag $TAG échoué : $TAG_ERR"
        fi
    else
        log "❌ Création du tag $TAG échouée"
    fi
fi

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ NOTIFICATION HOME ASSISTANT                                              │
# ╰──────────────────────────────────────────────────────────────────────────╯
TOKEN_FILE="/config/.secrets/ha_token"
if [[ -f "$TOKEN_FILE" ]]; then
    TOKEN="$(cat "$TOKEN_FILE")"
    curl -s -X POST \
        -H "Authorization: Bearer ${TOKEN}" \
        -H "Content-Type: application/json" \
        -d "{\"title\":\"Backup GitHub\",\"message\":\"$MSG\"}" \
        http://supervisor/core/api/services/persistent_notification/create >/dev/null || true
fi

# annotations_log:
# [2026-02-28] Suppression bloc SSH (inutile sur re-build HTTPS)
# [2026-02-28] Push branche : -q supprimé, erreur capturée dans PUSH_ERR
# [2026-02-28] Push tag     : -q && log remplacé par if/else + TAG_ERR
# [2026-02-28] fetch --tags : -q supprimé, || log ajouté
# [2026-02-28] Tag création : else ajouté pour logger l'échec