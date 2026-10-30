# HA_GIT_BACKUP - Script de sauvegarde automatique vers GitHub

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-System-ff9800?style=flat-square)](.)

</div>

> **Script shell :** `ha_git_backup.sh`
> **Emplacement prod :** `/config/.scripts/ha_git_backup.sh`
> **Emplacement local :** `docs/01_docs_config_system/01_config_system_SH_PY_YAML/.scripts/01_scripts.sh/ha_git_backup.sh` (copie identique dans `docs/04_docs_scripts/04_docs_scripts_SH/Ha_git_backup/Ha_git_backup.sh`)
> **Appelé par :** `shell_command.git_backup_push`, `git_backup_push_manual` et `git_backup_push_weekly` (fichier `shell_command/GitHub/GitHub_backup_GitHub.yaml`), lancés par 6 actions de `automations.yaml` (lignes 96, 115, 129, 170, 181 et 2315, relevé du 2026-10-18)
> **Dernière modif :** 2026-08-08 (date du fichier ; dernière entrée du journal du script : 2026-08-01). Fiche relue contre le script le 2026-10-18.
> **Empreinte relevée le 2026-10-18 :** MD5 `57ae9a6e`, 15054 octets, copies identiques à la prod

---

## 📝 Description

Sauvegarde automatique de la configuration HA vers GitHub (`home_assistant_re-build`, branche `main`).
Gère 3 modes d'exécution selon l'argument passé.

---

## 🔢 Modes d'exécution

| Argument | Déclencheur | Comportement |
|:---------|:------------|:-------------|
| *(aucun)* | Automation H+10 (00:10, 01:10…) | Commit + push si changements `.yaml/.yml/.md/.sh` |
| `weekly` | Dimanche / bouton manuel weekly | Commit + push + **tag ISO hebdomadaire** même si rien à committer |
| `Manuel` | Bouton dashboard | Commit + push - notifie si déjà à jour |

---

## ⚙️ Fonctionnement détaillé

### Garde-fous pré-commit
- Vérifie que `secrets.yaml` **n'est pas tracké** par git → exit 1 si c'est le cas
- Nettoie un éventuel rebase-merge orphelin (`/config/.git/rebase-merge`)
- Force la branche `main` (évite push en detached HEAD)

### Détection des changements
`git add -A` est fait en premier (suppressions et renommages compris). La liste des fichiers modifiés est ensuite filtrée sur `.yaml`, `.yml`, `.md` et `.sh`. Ce filtre ne sert qu'à décider s'il y a quelque chose à pousser : le commit prend tout ce qui est indexé, sauf ce que `.gitignore` ignore (donc aussi des `.py`).
Si la liste est vide, qu'aucun commit local n'attend d'être poussé et que le mode n'est pas `weekly` : sortie 0 et notification HA "déjà à jour".

### Message de commit
Format : `HAOS auto-backup:`, `HAOS weekly backup:` ou `HAOS MANUEL-backup:`, suivi de la date, de l'heure et du fuseau (`AAAA-MM-JJ HH:MM:SS TZ`).
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

- **`secrets.yaml` ne doit JAMAIS être tracké** - le garde-fou ligne 70 bloque le script si c'est le cas.
- **`!secret` ne fonctionne pas en bash** - le token GitHub est stocké directement dans l'URL remote git (`~/.git/config`), pas dans `secrets.yaml`.
- **"Manuel ne fonctionne pas"** → comportement normal si H+10 a déjà tout poussé (rien à committer).
- **`set -euo pipefail`** - le `trap ERR` logue toute erreur inattendue avec numéro de ligne.
- **stdout bloqué** (`exec 1>/dev/null`) - seuls les `>> "$LOG"` explicites apparaissent dans le log.

---

## 🔗 Dépendances

| Composant | Rôle |
|:----------|:-----|
| `shell_command/GitHub/GitHub_backup_GitHub.yaml` | Expose `git_backup_push`, `git_backup_push_manual` et `git_backup_push_weekly` (et aussi `audit_md5` et `audit_md5_md_yaml`) |
| Automations (6 appels) | Déclenchent le script selon le planning (lignes 96, 115, 129, 170, 181 et 2315 de `automations.yaml`) |
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
| 2026-08-01 | FIX : `git add -A` déplacé AVANT la détection des changements (évite les fantômes GitHub après un renommage) |

## Écarts relevés le 2026-10-18 entre la fiche et le script

- Le commentaire d'en-tête du script (lignes 18-19 et 33) dit encore "uniquement .yaml .yml .md" et "git pull --rebase". Le code filtre aussi `.sh` (ligne 90) et utilise `git push --force-with-lease` (ligne 156).
- Le garde-fou `secrets.yaml` est à la ligne 70 du script (l'en-tête du script dit ligne 22).
- Le nom du dossier local et les noms des commandes `shell_command` ont changé depuis la rédaction de cette fiche. Elle a été mise à jour en conséquence.
- Le script n'est pas modifié.