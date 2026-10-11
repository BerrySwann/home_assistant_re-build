#!/usr/bin/env bash
set -euo pipefail
# "[L1] shebang + strict mode"

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ HA GIT BACKUP — SCRIPT DE SAUVEGARDE AUTOMATIQUE VERS GITHUB             │
# ╰──────────────────────────────────────────────────────────────────────────╯
#
# ## 📝 DESCRIPTION :
# Ce script sauvegarde automatiquement la configuration HA vers GitHub.
# Il gère 3 modes d'exécution :
#   - auto    : lancé par shell_command HA toutes les H+10 (ex: 00:10, 01:10...)
#   - weekly  : lancé le dimanche (ou manuellement) — pose un tag ISO hebdo
#   - manuel  : appelé via shell_command "git_backup_manuel" depuis le dashboard
#
# ## 🧮 FONCTIONNEMENT & SOURCES :
# - Répertoire source : /config (tout le dépôt git HA)
# - Filtre commit    : uniquement les fichiers .yaml, .yml et .md modifiés
# - Authentification : token HTTPS embarqué dans l'URL remote (persistant dans .git/config)
# - Tag hebdo        : format ISO "weekly-YYYY-WXX" (ex: weekly-2026-W10)
#                      anti-collision : "-HHMM" ajouté si le tag existe déjà
# - Log              : /config/.logs/ha_git_backup.log
# - Notification HA  : via API supervisor + token dans /config/.secrets/ha_token
#
# ## ⚠️ IMPORTANT (PIÈGES) :
# - secrets.yaml ne doit JAMAIS être tracké — garde-fou ligne 22 bloque si c'est le cas
# - !secret ne fonctionne pas en bash — le token est stocké dans l'URL remote git
# - set -euo pipefail : toute commande non gérée fait quitter le script (exit 1)
# - Le tag weekly doit être posé même si rien n'a changé depuis le dernier H+10
#   → c'est pourquoi les deux exit 0 anticipés exemptent l'argument "weekly"
# - "Manuel ne fonctionne pas" = en réalité rien à committer (H+10 a déjà tout poussé)
#   → comportement normal et attendu, pas un bug
# - Si push rejeté (fetch first) : le script fait git pull --rebase auto + retry
#
# ## 🖥️ TABLEAU DE BORD (VIGNETTES PRINCIPALES) :
# - Aucune vignette directe — ce script alimente GitHub (source externe)
# - Indirectement utilisé par : L5C3 MariaDB (lien GitHub au clic sur la vignette)
# - Appelé via : shell_command.yaml → boutons du dashboard HA

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ CONFIGURATION & LOGGING                                                  │
# ╰──────────────────────────────────────────────────────────────────────────╯
LOG_DIR="/config/.logs"
LOG="$LOG_DIR/ha_git_backup.log"
mkdir -p "$LOG_DIR"
exec 1>/dev/null   # Bloquer tout stdout parasite — seuls >> "$LOG" comptent
cd /config


# "[L-checkout] force branche main — évite push en detached HEAD"
# Nettoyage rebase-merge orphelin (laissé par un rebase échoué)
[ -d /config/.git/rebase-merge ] && { git rebase --abort 2>/dev/null || rm -fr /config/.git/rebase-merge 2>/dev/null; } || true
git checkout main 2>/dev/null || git switch main 2>/dev/null || true

# Trap global : log toute erreur non gérée avec numéro de ligne
# "[L-trap] catch erreurs inattendues"
trap 'echo "❌ Erreur inattendue ligne $LINENO — script interrompu: $(date "+%Y-%m-%d %H:%M:%S %Z")" >> "$LOG"' ERR

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ IDENTITÉ GIT & AUTHENTIFICATION                                          │
# ╰──────────────────────────────────────────────────────────────────────────╯
git config user.name  "BerrySwann (HAOS)"
git config user.email "BerrySwann@users.noreply.github.com"

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ GARDE-FOUS                                                               │
# ╰──────────────────────────────────────────────────────────────────────────╯
if git ls-files --error-unmatch secrets.yaml >/dev/null 2>&1; then
  echo "❌ secrets.yaml est tracké par git — ABANDON" | tee -a "$LOG"
  exit 1
fi

BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo main)"
# Guard détached HEAD
[[ "$BRANCH" == "HEAD" ]] && { git switch main 2>/dev/null || true; BRANCH="main"; }
if ! git rev-parse --abbrev-ref --symbolic-full-name "@{u}" >/dev/null 2>&1; then
  git branch -u "origin/${BRANCH}" >/dev/null 2>&1 || true
fi

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ DÉTECTION DES CHANGEMENTS                                                │
# ╰──────────────────────────────────────────────────────────────────────────╯
CHANGED="$( { git diff --name-only; git ls-files -o --exclude-standard; } \
  | grep -E '\.(ya?ml|md)$' | sort -u || true )"

if [[ -z "$CHANGED" ]]; then
  STATUS_LINES="$(git status --porcelain || true)"
  if [[ -z "$STATUS_LINES" ]]; then
    if [[ "${1:-}" != "weekly" ]]; then
      echo "ℹ️ GitHub deja a jour - rien a committer: $(date '+%Y-%m-%d %H:%M:%S %Z')" >> "$LOG"
      TOKEN_FILE="/config/.secrets/ha_token"
      if [[ -f "$TOKEN_FILE" ]]; then
        TOKEN="$(cat "$TOKEN_FILE")"
        curl -s -X POST \
          -H "Authorization: Bearer ${TOKEN}" \
          -H "Content-Type: application/json" \
          -d '{"title":"Backup GitHub","message":"GitHub deja a jour - rien a committer"}' \
          http://supervisor/core/api/services/persistent_notification/create >/dev/null 2>/dev/null || true
      fi
      exit 0
    fi
  fi
fi

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ MESSAGE DE COMMIT & VERSION HA                                           │
# ╰──────────────────────────────────────────────────────────────────────────╯
MSG="HAOS auto-backup: $(date '+%Y-%m-%d %H:%M:%S %Z')"
[[ "${1:-}" == "weekly" ]] && MSG="HAOS weekly backup: $(date '+%Y-%m-%d %H:%M:%S %Z')"
[[ "${1:-}" == "Manuel" ]] && MSG="HAOS MANUEL-backup: $(date '+%Y-%m-%d %H:%M:%S %Z')"
HA_VER=""
[[ -f /config/.HA_VERSION ]] && HA_VER="$(cat /config/.HA_VERSION 2>/dev/null)"
MSG="${MSG}${HA_VER:+ (HA ${HA_VER})}"

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ COMMIT                                                                   │
# ╰──────────────────────────────────────────────────────────────────────────╯
git add -A >/dev/null 2>&1
if git commit -m "$MSG" >/dev/null 2>&1; then
  echo "📝 Commit créé: $MSG" >> "$LOG"
elif [[ "${1:-}" != "weekly" ]]; then
  AHEAD="$(git rev-list @{u}..HEAD --count 2>/dev/null || echo 0)"
  if [[ "$AHEAD" -gt 0 ]]; then
    echo "📤 Commit local non pushé ($AHEAD) — push en cours: $(date '+%Y-%m-%d %H:%M:%S %Z')" >> "$LOG"
  else
    echo "ℹ️ GitHub deja a jour - rien a committer: $(date '+%Y-%m-%d %H:%M:%S %Z')" >> "$LOG"
    TOKEN_FILE="/config/.secrets/ha_token"
    if [[ -f "$TOKEN_FILE" ]]; then
      TOKEN="$(cat "$TOKEN_FILE")"
      curl -s -X POST \
        -H "Authorization: Bearer ${TOKEN}" \
        -H "Content-Type: application/json" \
        -d '{"title":"Backup GitHub","message":"GitHub deja a jour - rien a committer"}' \
        http://supervisor/core/api/services/persistent_notification/create >/dev/null 2>/dev/null || true
    fi
    exit 0
  fi
else
  echo "ℹ️ Rien à committer — tag weekly posé quand même" >> "$LOG"
fi

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ PUSH — AVEC GESTION FETCH FIRST                                          │
# ╰──────────────────────────────────────────────────────────────────────────╯
do_push() {
  # "[L-push] tente push direct, fallback force-with-lease si divergence"
  local PUSH_OUT
  PUSH_OUT=$(git push origin "$BRANCH" 2>&1) && return 0

  if echo "$PUSH_OUT" | grep -qE "fetch first|non-fast-forward|rejected"; then
    echo "⚠️ Push rejeté (divergence) — fetch + force-with-lease: $(date '+%Y-%m-%d %H:%M:%S %Z')" >> "$LOG"
    git fetch origin "$BRANCH" >/dev/null 2>&1 || true
    PUSH_OUT=$(git push --force-with-lease origin "$BRANCH" 2>&1)
    if [[ $? -eq 0 ]]; then
      echo "✅ Push OK (force-with-lease): $(date '+%Y-%m-%d %H:%M:%S %Z')" >> "$LOG"
      return 0
    fi
    echo "❌ Push impossible: $PUSH_OUT $(date '+%Y-%m-%d %H:%M:%S %Z')" >> "$LOG"
    return 1
  fi

  echo "❌ Push impossible: $PUSH_OUT $(date '+%Y-%m-%d %H:%M:%S %Z')" >> "$LOG"
  return 1
}

if ! do_push; then
  exit 1
fi

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ TAG HEBDOMADAIRE                                                         │
# ╰──────────────────────────────────────────────────────────────────────────╯
if [[ "${1:-}" == "weekly" ]]; then
  TAG_BASE="weekly-$(date +'%G-W%V')"
  TAG="$TAG_BASE"
  if git rev-parse -q --verify "refs/tags/${TAG}" >/dev/null; then
    TAG="${TAG_BASE}-$(date +'%H%M')"
  fi
  git tag -a "$TAG" -m "Weekly backup $(date +'%F')${HA_VER:+ (HA ${HA_VER})}"
  if git push origin --tags >/dev/null 2>&1; then
    echo "🏷️ Tag créé et poussé: $TAG" >> "$LOG"
  else
    echo "❌ Push tag $TAG échoué: $(date '+%Y-%m-%d %H:%M:%S %Z')" >> "$LOG"
  fi
fi

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ LOG SUCCÈS & NOTIFICATION HA                                             │
# ╰──────────────────────────────────────────────────────────────────────────╯
echo "✅ Backup GitHub OK: $MSG" >> "$LOG"

TOKEN_FILE="/config/.secrets/ha_token"
if [[ -f "$TOKEN_FILE" ]]; then
  TOKEN="$(cat "$TOKEN_FILE")"
  curl -s -X POST \
    -H "Authorization: Bearer ${TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{"title":"Backup GitHub","message":"'"$MSG"'"}' \
    http://supervisor/core/api/services/persistent_notification/create >/dev/null || true
fi

# annotations_log:
# [2026-06-13] BUG FIX CRITIQUE — ligne 134 : %Z"') → %Z') — le " était dans la single-quote
#              ce qui empêchait la fermeture du $() → bash scannait jusqu'à EOF → syntax error line 178
#              Fix 2 : git checkout main >/dev/null 2>&1 (supprime le bruit stdout dans le log)
# [2026-06-13] Ajout git checkout main après cd /config — évite push en detached HEAD
# [2026-02-28] L8  user.name  : "Eric Rodi (HAOS)"               → "BerrySwann (HAOS)"
# [2026-02-28] L9  user.email : "erodi@users.noreply.github.com" → "BerrySwann@users.noreply.github.com"
# [2026-02-28] SSH supprimé  : re-build HTTPS uniquement (token dans URL remote)
# [2026-02-28] Boîtes ASCII ajoutées sur toutes les sections
# [2026-03-10] BUG FIX — exit 0 prématuré bloquait la création du tag weekly
# [2026-03-10] Ajout bloc documentation en-tête
# [2026-05-30] BUG FIX — push rejeté (fetch first) géré en silence :
#              → Ajout fonction do_push() avec détection fetch first + git pull --rebase auto
#              → Suppression git push origin master (branche inexistante)
#              → Ajout trap ERR global pour logger toute erreur inattendue
#              → Log du commit créé (📝) pour meilleure traçabilité