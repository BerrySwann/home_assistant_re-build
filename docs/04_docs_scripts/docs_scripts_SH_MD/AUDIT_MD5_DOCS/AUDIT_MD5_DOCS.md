# AUDIT_MD5_DOCS - Script d'audit MD5 DOCS 3 niveaux (LOCAL / PROD / GITHUB)

> **Script shell :** `audit_md5_docs.sh`
> **Emplacement local :** `docs/04_docs_scripts/scripts/audit_md5_docs.sh`
> **Exécuté depuis :** Git Bash Windows (local ReBuild - pas sur HA)
> **Auteur :** HERMES
> **Dernière modif :** 2026-08-07

---

## 📝 Description

Compare chaque fichier `.md` (docs/ + README.md + INDEX_GLOBAL.md) entre trois niveaux :
- **LOCAL** (`C:\Users\Berry Swann\Documents\ReBuild\docs\`)
- **PROD** (`H:\docs\` - montage Samba HA)
- **GITHUB** (`raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/`)

La comparaison neutralise l'écart CRLF/LF (local Windows = CRLF, prod H: et GitHub = LF) via un MD5 normalisé.

**Statuts possibles :**
- `✅ SYNC` - MD5 identique sur les 3 niveaux (octets exacts)
- `⚠️ CRLF` - contenu identique après normalisation LF - aucune action requise
- `❌ DIFF` - contenu réellement différent entre niveaux
- `🚫 ABSENT` - fichier manquant sur un ou plusieurs niveaux

---

## 🔢 Passes d'exécution

### PASS 1 - TREE LOCAL
Construit la liste des fichiers à auditer via `find` sur `$LOCAL_ROOT/docs/`.
Ajoute les fichiers racine : `Github/README.md` → `README.md`, `Github/INDEX_GLOBAL.md` → `INDEX_GLOBAL.md`.

### PASS 2 - MD5 LOCAL + PROD
Calcule pour chaque fichier le MD5 brut et le MD5 normalisé (CRLF→LF via `tr -d '\r'`).
Mapping racine : `Github/README.md` (local) → `README.md` (prod H:).

### PASS 3 - MD5 GITHUB (curl ciblé)
Pour chaque fichier, `curl` la raw URL GitHub avec encodage URL Python (`urllib.parse.quote`) pour gérer les espaces et accents.
Fichier tmp sur chemin Windows explicite (`cygpath -m "$LOCALAPPDATA/Temp"`) - le curl natif Windows échoue sur `/tmp` MSYS.

---

## 📁 Périmètre audité

| Type | Détail |
|:-----|:-------|
| **Docs config** | `docs/01_docs_config_system/**/*.md` |
| **Docs dashboard** | `docs/02_docs_dashboard/**/*.md` |
| **Docs automations** | `docs/03_docs_automations/**/*.md` |
| **Docs scripts** | `docs/04_docs_scripts/**/*.md` |
| **Docs système** | `docs/05_docs_MD_system/**/*.md` |
| **Fichiers racine** | `Github/README.md` + `Github/INDEX_GLOBAL.md` (mappés vers racine prod/repo) |

---

## 📄 Logs

| Fichier | Contenu |
|:--------|:--------|
| `historique/hermes_md5_audit_docs_YYYY-MM-DD.txt` | Rapport daté du jour |
| `historique/hermes_md5_audit_docs_latest.txt` | Copie du dernier rapport (accès rapide) |

Format du rapport : tableau `FICHIER | PROD | LOCAL | GITHUB | STATUT` + résumé final.

> **Préfixe `hermes_`** - ne jamais entrer en collision avec les rapports Claude (`claude_md5_audit_docs_*.txt`).

---

## ⚠️ Points d'attention

- `set -euo pipefail` - toute erreur non gérée stoppe le script. Les `find` utilisent `|| true`.
- **curl + MSYS** : le curl natif Windows ne peut pas écrire dans `/tmp` (chemin MSYS). Le script utilise `cygpath -m "$LOCALAPPDATA/Temp"` pour résoudre un chemin Windows valide.
- **Encodage URL** : les noms de fichiers avec espaces ou accents (ex : `Carte Météo Vence.md`) sont encodés via `python -c 'urllib.parse.quote(...)'` avant l'appel curl.
- **CRLF/LF** : les fichiers locaux Windows sont en CRLF. Le MD5 normalisé (`tr -d '\r'`) tranche entre ⚠️ CRLF (pas d'action) et ❌ DIFF (action requise).
- **Source de vérité** : LOCAL = source de vérité. En cas de DIFF, c'est la version locale qui prévaut.
- S'exécute **localement** depuis Git Bash Windows (pas sur HA) - requiert le montage `H:` actif.

---

## 🔗 Dépendances

| Composant | Rôle |
|:----------|:-----|
| `Git Bash Windows` | Environnement d'exécution |
| `H:` monté (Samba HA) | Accès prod HA |
| `python` (Git Bash) | Encodage URL (`urllib.parse.quote`) |
| `curl` | Requêtes raw GitHub par fichier |
| GitHub `home_assistant_re-build` | Source de vérité n°2 - cible des comparaisons |
| `ha_push_md` (skill Cowork) | Pousse les DIFF local → prod après audit |

---

## 📋 Historique des modifications

| Date | Modification |
|:-----|:-------------|
| 2026-08-07 | Création - 3 passes : tree → md5 local+prod → md5 github |
| 2026-08-07 | FIX curl : chemin tmp Windows explicite (`cygpath -m`) - curl natif échoue sur `/tmp` MSYS |
| 2026-08-07 | FIX tableaux associatifs : `declare -A` au lieu de `grep` en boucle |
| 2026-08-07 | Encodage URL : `python urllib.parse.quote` pour espaces/accents |
| 2026-08-07 | Préfixe rapport `hermes_` - pas de collision avec Claude (`claude_md5_audit_docs_*.txt`) |
