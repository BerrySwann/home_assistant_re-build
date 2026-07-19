# AUDIT_MD5 — Script d'audit MD5 PROD vs GitHub

> **Script shell :** `audit_md5.sh`
> **Emplacement prod :** `/config/.scripts/audit_md5.sh`
> **Emplacement local :** `DOCS/04_docs_scripts/docs_scripts_YAML/.scripts/audit_md5.sh`
> **Appelé par :** Boutons dashboard L5C3 (FULL · YAML · ATMA) via `shell_command`
> **Dernière modif :** 2026-06-28

---

## 📝 Description

Compare chaque fichier YAML (et script .sh) entre la prod HA (`/config/`) et le repo GitHub (`home_assistant_re-build/main`).
Produit un rapport en 3 passes avec statut par fichier.

**Statuts possibles :**
- `✅ SYNC` — MD5 identique entre prod et GitHub
- `❌ DIFF` — contenu différent (drift à investiguer)
- `⚠️ PUSH MANQUANT` — fichier présent en prod, absent de GitHub

---

## 🔢 Passes d'exécution

### PASS 1 — TREE LOCAL
Construit la liste des fichiers à auditer via `find` sur les répertoires déclarés.
Exclut : `streamline_templates.example.yaml`, `scenes.yaml`, `zigbee2mqtt/`.

### PASS 2 — MD5 PROD
Calcule le MD5 de chaque fichier présent localement dans `/config/`.

### PASS 3 — MD5 GITHUB
Pour chaque fichier, curl le raw GitHub (`https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/...`) et calcule le MD5 du fichier téléchargé.
Utilise un fichier tmp unique réutilisé (`/tmp/audit_gh_$$.tmp`) — 1 fichier YAML à la fois, impact RAM nul.

---

## 📁 Périmètre audité

| Type | Détail |
|:-----|:-------|
| **Répertoires YAML** | `sensors` `templates` `utility_meter` `command_line` `shell_command` `packages` `groups` `input_booleans` `input_number` |
| **Fichiers YAML racine** | `automations.yaml` `scripts.yaml` `configuration.yaml` `sql.yaml` `input_select.yaml` `input_datetime.yaml` `input_button.yaml` |
| **Scripts shell** | `find .scripts -name "*.sh"` |

---

## 📄 Logs

| Fichier | Contenu |
|:--------|:--------|
| `/config/.logs/md5_audit_YYYY-MM-DD.txt` | Rapport daté du jour |
| `/config/.logs/md5_audit_latest.txt` | Copie du dernier rapport (accès rapide) |

Format du rapport : tableau `FICHIER | PROD_MD5 | GH_MD5 | STATUT` + résumé final.

---

## ⚠️ Points d'attention

- `set -euo pipefail` — toute erreur non gérée stoppe le script. Les `find` utilisent `|| true` pour éviter un exit si un répertoire est absent.
- Le curl utilise `--max-time 15` — un timeout GitHub fait apparaître le fichier en `⚠️ PUSH MANQUANT` à tort. Relancer l'audit dans ce cas.
- `secrets.yaml` n'est jamais dans le scope (non listé dans les répertoires audités).

---

## 🔗 Dépendances

| Composant | Rôle |
|:----------|:-----|
| `shell_command.yaml` | Expose le script à HA via `shell_command.audit_md5` |
| Dashboard L5C3 | Boutons FULL · YAML · ATMA déclenchent le script |
| GitHub `home_assistant_re-build` | Source de vérité n°2 — cible des comparaisons |

---

## 📋 Historique des modifications

| Date | Modification |
|:-----|:-------------|
| 2026-06-14 | Création — 3 passes : tree → md5 prod → md5 github |
| 2026-06-15 | FIX : `git show` → `curl raw URL` (ref stale non résolvable) |
| 2026-06-15 | FIX CRITIQUE : `echo | md5sum` → `curl -o TMP + md5sum TMP` (bytes exacts préservés) |
| 2026-06-15 | EXTRA_FILES étendu : `scripts.yaml` `shell_command.yaml` `configuration.yaml` |
| 2026-06-17 | DIRS : ajout `shell_command/` `packages/` |
| 2026-06-28 | FIX PIPEFAIL : `find` → `|| true` / ajout `.scripts/*.sh` dans le scope |
