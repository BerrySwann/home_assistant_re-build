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
#
# ## 🖥️ TABLEAU DE BORD (VIGNETTES PRINCIPALES) :
# - Aucune vignette directe — ce script alimente GitHub (source externe)
# - Indirectement utilisé par : L5C3 MariaDB (lien GitHub au clic sur la vignette)
# - Appelé via : shell_command.yaml → boutons du dashboard HA

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ CONFIGURATION & LOGGING                                                  │
# ╰──────────────────────────────────────────────────────────────────────────╯
LOG_DIR="/config/.logs"
mkdir -p "$LOG_DIR"  # "[L5] création dossier logs"
cd /config

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ IDENTITÉ GIT & AUTHENTIFICATION                                          │
# ╰──────────────────────────────────────────────────────────────────────────╯
git config user.name  "BerrySwann (HAOS)"                    # "[L8] user.name"
git config user.email "BerrySwann@users.noreply.github.com"  # "[L9] user.email"
# "[L10] Auth HTTPS via token dans URL remote (/config/.git/config — persistant)"

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ GARDE-FOUS                                                               │
# ╰──────────────────────────────────────────────────────────────────────────╯
if git ls-files --error-unmatch secrets.yaml >/dev/null 2>&1; then
  echo "❌ secrets.yaml est tracké par git — ABANDON" | tee -a "$LOG_DIR/ha_git_backup.log"
  exit 1
fi
# "[L20] garde-fou secrets.yaml"
BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo main)"
if ! git rev-parse --abbrev-ref --symbolic-full-name "@{u}" >/dev/null 2>&1; then
  git branch -u "origin/${BRANCH}" || true
fi
# "[L26] branche + upstream"

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ DÉTECTION DES CHANGEMENTS                                                │
# ╰──────────────────────────────────────────────────────────────────────────╯
CHANGED="$( { git diff --name-only; git ls-files -o --exclude-standard; } \
  | grep -E '\.(ya?ml|md)$' | sort -u || true )"
# "[L31] filtre CHANGED"
if [[ -z "$CHANGED" ]]; then
  STATUS_LINES="$(git status --porcelain || true)"
  if [[ -z "$STATUS_LINES" ]]; then
    if [[ "${1:-}" != "weekly" ]]; then  # "[L36] exit anticipé — sauf si weekly (tag doit être posé)"
      echo "ℹ️  Aucun changement" >> "$LOG_DIR/ha_git_backup.log"; exit 0
    fi
  fi
fi
# "[L36] fallback status — weekly exempt de l'exit anticipé"

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ MESSAGE DE COMMIT & VERSION HA                                           │
# ╰──────────────────────────────────────────────────────────────────────────╯
MSG="HAOS auto-backup: $(date '+%Y-%m-%d %H:%M:%S %Z')"
[[ "${1:-}" == "weekly" ]] && MSG="HAOS weekly backup: $(date '+%Y-%m-%d %H:%M:%S %Z')"
[[ "${1:-}" == "Manuel" ]] && MSG="HAOS MANUEL-backup: $(date '+%Y-%m-%d %H:%M:%S %Z')"  # "[L43] modif"
HA_VER=""
[[ -f /config/.HA_VERSION ]] && HA_VER="$(cat /config/.HA_VERSION 2>/dev/null)"
MSG="${MSG}${HA_VER:+ (HA ${HA_VER})}"
# "[L43] commit message + version HA"

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ COMMIT & PUSH                                                            │
# ╰──────────────────────────────────────────────────────────────────────────╯
git add -A
# "[L45] commit — si rien à committer, exit SAUF si weekly (tag doit être posé quoi qu'il arrive)"
if git commit -m "$MSG" 2>/dev/null; then
  git push origin "$BRANCH" || git push origin main || git push origin master
  # "[L48] push (uniquement si nouveau commit)"
elif [[ "${1:-}" != "weekly" ]]; then
  echo "ℹ️  Rien à committer" >> "$LOG_DIR/ha_git_backup.log"; exit 0
else
  echo "ℹ️  Rien à committer — tag weekly posé quand même" >> "$LOG_DIR/ha_git_backup.log"
fi

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ TAG HEBDOMADAIRE — SENS UNIQUE : HA → GITHUB                             │
# ╰──────────────────────────────────────────────────────────────────────────╯
if [[ "${1:-}" == "weekly" ]]; then
  TAG_BASE="weekly-$(date +'%G-W%V')"
  TAG="$TAG_BASE"
  if git rev-parse -q --verify "refs/tags/${TAG}" >/dev/null; then
    TAG="${TAG_BASE}-$(date +'%H%M')"   # "[L57] anti-collision même semaine"
  fi
  git tag -a "$TAG" -m "Weekly backup $(date +'%F')${HA_VER:+ (HA ${HA_VER})}"
  git push origin --tags
  echo "🏷️  Tag créé: $TAG" >> "$LOG_DIR/ha_git_backup.log"
fi
# "[L60] weekly tag ISO week + HA version (collision-safe)"
echo "✅ Backup GitHub OK: $MSG" >> "$LOG_DIR/ha_git_backup.log"
# "[L62] log succès"

# ╭──────────────────────────────────────────────────────────────────────────╮
# │ NOTIFICATION HOME ASSISTANT                                              │
# ╰──────────────────────────────────────────────────────────────────────────╯
TOKEN_FILE="/config/.secrets/ha_token"
if [[ -f "$TOKEN_FILE" ]]; then
  TOKEN="$(cat "$TOKEN_FILE")"
  curl -s -X POST \
    -H "Authorization: Bearer ${TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{"title":"Backup GitHub","message":"'"$MSG"'"}' \
    http://supervisor/core/api/services/persistent_notification/create >/dev/null || true
fi
# "[L70] notif HA optionnelle"

# annotations_log:
# [2026-02-28] L8  user.name  : "Eric Rodi (HAOS)"               → "BerrySwann (HAOS)"
# [2026-02-28] L9  user.email : "erodi@users.noreply.github.com" → "BerrySwann@users.noreply.github.com"
# [2026-02-28] SSH supprimé  : re-build HTTPS uniquement (token dans URL remote)
# [2026-02-28] Boîtes ASCII ajoutées sur toutes les sections
# [2026-03-10] BUG FIX — exit 0 prématuré bloquait la création du tag weekly :
#              L36 : exit anticipé "Aucun changement" désormais exempté si arg="weekly"
#              L45 : "git commit || exit 0" → "if git commit ... elif weekly ... else exit 0"
#              → Le tag weekly-YYYY-WXX est maintenant créé même sans nouveau commit
# [2026-03-10] Ajout bloc documentation en-tête (DESCRIPTION / FONCTIONNEMENT / PIÈGES / VIGNETTES)