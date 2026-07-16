# HA_GIT_BACKUP — Script de sauvegarde automatique vers GitHub

> **Script shell :** `ha_git_backup.sh`
> **Emplacement prod :** `/config/.scripts/ha_git_backup.sh`
> **Emplacement local :** `DOCS/04_docs_scripts/docs_scripts_YAML/.scripts/ha_git_backup.sh`
> **Appelé par :** `shell_command.yaml` → automations backup (auto H+10 · weekly · manuel)
> **Dernière modif :** 2026-06-22

---

## 📝 Description

Sauvegarde automatique de la configuration HA vers GitHub (`home_assistant_re-build`, branche `main`).
Gère 3 modes d'exécution selon l'argument passé.

---

## 🔢 Modes d'exécution

| Argument | Déclencheur | Comportement |
|:---------|:------------|:-------------|
| *(aucun)* | Automation H+10 (00:10, 01:10…) | Commit + push si changements `.yaml/.yml/.md` |
| `weekly` | Dimanche / bouton manuel weekly | Commit + push + **tag ISO hebdomadaire** même si rien à committer |
| `Manuel` | Bouton dashboard | Commit + push — notifie si déjà à jour |

---

## ⚙️ Fonctionnement détaillé

### Garde-fous pré-commit
- Vérifie que `secrets.yaml` **n'est pas tracké** par git → exit 1 si c'est le cas
- Nettoie un éventuel rebase-merge orphelin (`/config/.git/rebase-merge`)
- Force la branche `main` (évite push en detached HEAD)

### Détection des changements
Filtre uniquement les fichiers `.yaml`, `.yml`, `.md` modifiés ou non trackés.
Si rien à committer et mode ≠ `weekly` → exit 0 + notification HA "déjà à jour".

### Message de commit
Format : `HAOS [auto|weekly|MANUEL]-backup: YYYY-MM-DD HH:MM:SS TZ (HA X.Y.Z)`
La version HA est lue depuis `/config/.HA_VERSION`.

### Push avec fallback
1. Tentative push direct `git push origin main`
2. Si rejeté (`fetch first` / `non-fast-forward`) → `git fetch` + `git push --force-with-lease`
3. Si toujours impossible → log erreur + exit 1

### Tag hebdomadaire
Format : `weekly-YYYY-WXX` (ex: `weekly-2026-W26`)
Anti-collision : si le tag existe déjà → `weekly-YYYY-WXX-HHMM`

---

## 📄 Logs & Notifications

| Canal | Détail |
|:------|:-------|
| `/config/.logs/ha_git_backup.log` | Log texte de chaque exécution |
| Notification HA | Via API Supervisor (`http://supervisor/core/api/services/persistent_notification/create`) |
| Token HA | Lu depuis `/config/.secrets/ha_token` (hors git) |

---

## ⚠️ Points d'attention

- **`secrets.yaml` ne doit JAMAIS être tracké** — le garde-fou ligne 68 bloque le script si c'est le cas.
- **`!secret` ne fonctionne pas en bash** — le token GitHub est stocké directement dans l'URL remote git (`~/.git/config`), pas dans `secrets.yaml`.
- **"Manuel ne fonctionne pas"** → comportement normal si H+10 a déjà tout poussé (rien à committer).
- **`set -euo pipefail`** — le `trap ERR` logue toute erreur inattendue avec numéro de ligne.
- **stdout bloqué** (`exec 1>/dev/null`) — seuls les `>> "$LOG"` explicites apparaissent dans le log.

---

## 🔗 Dépendances

| Composant | Rôle |
|:----------|:-----|
| `shell_command.yaml` | Expose 3 commandes : `git_backup_auto`, `git_backup_weekly`, `git_backup_manuel` |
| Automations backup (×7) | Déclenchent le script selon planning (H+10, dimanche, bouton) |
| `/config/.secrets/ha_token` | Token API Supervisor pour notifications (hors git, hors `secrets.yaml`) |
| GitHub `home_assistant_re-build` | Destination des commits et tags |
| Dashboard L5C3 | Bouton "Git Backup Manuel" |

---

## 📋 Historique des modifications

| Date | Modification |
|:-----|:-------------|
| 2026-02-28 | Passage SSH → HTTPS token / user.name → BerrySwann / boîtes ASCII ajoutées |
| 2026-03-10 | FIX : exit 0 prématuré bloquait la création du tag weekly |
| 2026-05-30 | FIX : push rejeté géré → `do_push()` avec fallback `force-with-lease` + `trap ERR` |
| 2026-06-13 | FIX CRITIQUE : `%Z"')` → `%Z')` (fermeture single-quote incorrecte → syntax error EOF) |
| 2026-06-13 | Ajout `git checkout main` après `cd /config` (évite detached HEAD) |
