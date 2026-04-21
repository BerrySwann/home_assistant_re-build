<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--11-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Dashboard%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord/` *(page inline dashboard Home)* |
| 🔗 **Accès depuis** | Heading "Système" → tap → `/dashboard-tablette/0` |
| 🏗️ **Layout** | `type: grid` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-11 |
| 🏠 **Version HA** | 2025.2.x → v2.0 |

---

# ⚙️ PAGE SYSTÈME — DOCUMENTATION COMPLÈTE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture de la page](#architecture-de-la-page)
3. [Section GITHUB](#section-github)
4. [Section RESTART VSCODE](#section-restart-vscode)
5. [Section MARIADB](#section-mariadb)
6. [Entités utilisées](#entités-utilisées--provenance-complète)
7. [Automations liées](#automations-liées)
8. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page de maintenance système regroupant 3 blocs fonctionnels :
- **GitHub** : statut du backup Git, tag hebdomadaire, branche active, journal des 10 derniers backups, graphique OK/KO 7 jours, boutons push manuel et weekly.
- **Restart VSCode** : bouton de redémarrage de Studio Code Server.
- **MariaDB** : graphique d'évolution de la taille de la base sur 7 jours, bouton de purge + repack.

### Intégrations requises

- ✅ **command_line** — sensors `sensor.backup_github_status`, `sensor.git_last_weekly_tag`, `sensor.backup_github_journal`, `sensor.github_default_branch`
- ✅ **sql** — `sensor.taille_db_home_assistant`
- ✅ **input_button** — `input_button.git_push_manuel`, `input_button.git_push_weekly_manuel`
- ✅ **shell_command** — `git_backup_push_manual`, `git_backup_push_weekly`

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:bubble-card` | Séparateurs de sections (GitHub / VSCode / MariaDB) |
| `custom:mushroom-chips-card` | Chips statut backup, tag, branche, push |
| `custom:mushroom-title-card` | Titre "Journal Backup" |
| `custom:apexcharts-card` | Graphique OK/KO 7j + évolution taille DB |
| `custom:button-card` | Boutons Restart VSCode et Purge MariaDB |

---

## 🏗️ ARCHITECTURE DE LA PAGE

```
┌─────────────────────────────────────────────┐
│  HEADING : Système  (tap → /0)              │
├─────────────────────────────────────────────┤
│  SEPARATOR : GitHub                         │
├─────────────────────────────────────────────┤
│  vertical-stack                             │
│  ├── chips : statut OK/KO + timestamp       │
│  ├── chips : tag weekly · branche · push    │
│  ├── title : Journal Backup (10 derniers)   │
│  ├── markdown : journal des backups         │
│  └── apexcharts : OK/KO 7 jours            │
├─────────────────────────────────────────────┤
│  SEPARATOR : Restart VSCode                 │
├─────────────────────────────────────────────┤
│  button-card : Redémarrer Studio Code       │
├─────────────────────────────────────────────┤
│  SEPARATOR : MariaDB                        │
├─────────────────────────────────────────────┤
│  apexcharts : évolution taille DB 7j        │
├─────────────────────────────────────────────┤
│  button-card : Purge MariaDB + Repack       │
└─────────────────────────────────────────────┘
```

---

## 📍 SECTION GITHUB

### Chip 1 — Statut backup

Affiche `Backup OK` ou `Backup KO` + le timestamp du dernier backup réussi.
Pas d'action au tap ni au hold (lecture seule).

```yaml
- type: template
  entity: sensor.backup_github_status
  icon: mdi:github
  content: >-
    {{ iif(states('sensor.backup_github_status')=='OK','Backup OK','Backup KO') }}
    · {{ state_attr('sensor.backup_github_status','ts') or 'jamais' }}
  icon_color: >-
    {{ iif(states('sensor.backup_github_status')=='OK','green','red') }}
  tap_action:
    action: none
  hold_action:
    action: none
```

### Chips 2 — Tag weekly · Branche · Push

| Chip | Tap | Hold |
|------|-----|------|
| **Tag weekly** | Ouvre GitHub/tags | Lance `input_button.git_push_weekly_manuel` + confirmation |
| **Branche** | Ouvre GitHub repo principal | — |
| **Push** | Lance `input_button.git_push_manuel` | Ouvre GitHub/commits/main |

> ⚠️ **Pièges :**
> - Utiliser `perform-action` (pas `call-service`) pour appeler `input_button.press`
> - La `confirmation` doit être **dans** `hold_action`, pas au même niveau
> - Appeler `input_button.*` et non `shell_command.*` directement (les chips mushroom ne supportent pas bien l'appel direct aux shell_command)

```yaml
- type: template
  entity: sensor.git_last_weekly_tag
  icon: mdi:tag
  content: "{{ states('sensor.git_last_weekly_tag') or 'no tag' }}"
  icon_color: >-
    {% set tag = states('sensor.git_last_weekly_tag') %}
    {% set iso = now().isocalendar() %}
    {% set current = "weekly-%04d-W%02d" | format(iso[0], iso[1]) %}
    {{ 'green' if (tag and tag.startswith(current)) else 'amber' }}
  tap_action:
    action: url
    url_path: https://github.com/BerrySwann/home_assistant_re-build/tags
    new_tab: true
  hold_action:
    action: perform-action
    perform_action: input_button.press
    target:
      entity_id: input_button.git_push_weekly_manuel
    confirmation:
      text: Créer un tag hebdomadaire ?

- type: template
  entity: sensor.github_default_branch
  icon: mdi:source-branch
  content: "Branche: {{ states('sensor.github_default_branch') or 'unknown' }}"
  icon_color: >-
    {% set b = states('sensor.github_default_branch') %}
    {{ 'green' if b == 'main' else 'amber' }}
  tap_action:
    action: url
    url_path: https://github.com/BerrySwann/home_assistant_re-build
    new_tab: true

- type: template
  icon: mdi:cloud-upload-outline
  content: Push
  icon_color: deep-orange
  tap_action:
    action: perform-action
    perform_action: input_button.press
    target:
      entity_id: input_button.git_push_manuel
  hold_action:
    action: url
    url_path: https://github.com/BerrySwann/home_assistant_re-build/commits/main
    new_tab: true
```

### Journal backup (markdown)

Affiche les 10 dernières lignes `OK` du log `/config/.logs/ha_git_backup.log`.

> ⚠️ **Pièges :**
> - Ne pas entourer le template de triple backticks — cela crée un bloc `<pre>` qui résiste au `font-size`
> - `font-size` et `text-align` doivent être sur `.card-content`, pas sur `ha-card`

```yaml
- type: markdown
  content: "{{ state_attr('sensor.backup_github_journal','text') or '—' }}"
  card_mod:
    style: |
      ha-card {
        border: none !important;
        box-shadow: none !important;
        background: transparent;
      }
      .card-content {
        font-size: 11px;
        text-align: center;
      }
```

### Graphique ApexCharts OK/KO

Graphique en colonnes sur 7 jours — transforme `OK` → `1` et `KO` → `0`, groupé par tranches de 6h.

---

## 📍 SECTION RESTART VSCODE

Bouton déclenchant l'automation `automation.redemarrage_quotidien_studio_code_server`.

> ⚠️ Utilise encore `call-service` / `automation.trigger` — fonctionnel mais à migrer vers `perform-action` / `automation.trigger` si HA >= 2024.8.

---

## 📍 SECTION MARIADB

### Graphique évolution taille DB

ApexCharts area sur 7 jours — `sensor.taille_db_home_assistant` en MiB, groupé par jour (`func: last`).

### Bouton Purge + Repack

Déclenche l'automation `automation.db_purge_mariadb_repack`.

---

## 📊 ENTITÉS — PROVENANCE COMPLÈTE

### 📁 `command_line/github_maintenance/github_maintenance.yaml`
> Sensors lisant le log Git et interrogeant le dépôt local.

| Entité | unique_id | Rôle |
|--------|-----------|------|
| `sensor.backup_github_status` | `backup_github_status` | OK/KO + timestamp dernier backup |
| `sensor.git_last_weekly_tag` | `git_last_weekly_tag` | Dernier tag weekly local |
| `sensor.backup_github_journal` | `backup_github_journal` | 10 dernières lignes OK du log |
| `sensor.github_default_branch` | `github_default_branch` | Branche git active |

### 📁 `sql.yaml`
| Entité | unique_id | Rôle |
|--------|-----------|------|
| `sensor.taille_db_home_assistant` | `taille_db_home_assistant` | Taille DB MariaDB en MiB |

### 📁 `input_button.yaml`
| Entité | Rôle |
|--------|------|
| `input_button.git_push_manuel` | Déclenche automation `[04-Backup]` → push manuel |
| `input_button.git_push_weekly_manuel` | Déclenche automation `[05-Backup]` → push + tag weekly |

### 📁 `shell_command.yaml`
| Commande | Rôle |
|----------|------|
| `shell_command.git_backup_push_manual` | Appelle `.scripts/ha_git_backup.sh "Manuel"` |
| `shell_command.git_backup_push_weekly` | Appelle `.scripts/ha_git_backup.sh weekly` |

### 📁 `.scripts/ha_git_backup.sh`
Script bash — 3 modes : `auto` (horaire H+10), `weekly` (dim 01:30 + tag ISO), `Manuel` (bouton dashboard).
Auth HTTPS via token dans l'URL remote Git (`.git/config`).

---

## ⚙️ AUTOMATIONS LIÉES

> Toutes les automations ci-dessous sont définies dans `automations.yaml`.

### Automations actives (backup GitHub)

| ID | Alias | Déclencheur | Action principale |
|----|-------|-------------|-------------------|
| `1772274342928` | **[01-Backup] Git hourly H+10** | Toutes les heures à H+10 | `shell_command.git_backup_push` |
| `1772274384811` | **[02-Backup] Git daily (03:00)** | Tous les jours à 03:00 | `shell_command.git_backup_push` |
| `1772274292302` | **[03-Backup] Git weekly (dim 01:30)** | Dimanche 01:30 | `shell_command.git_backup_push_weekly` + notif mobile |
| `1772276622703` | **[04-Backup] Git push manuel** | `input_button.git_push_manuel` → `on` | `shell_command.git_backup_push_manual` |
| `1772289095104` | **[05-Backup] Git push weekly manuel** | `input_button.git_push_weekly_manuel` → `on` | `shell_command.git_backup_push_weekly` |
| `1772275440416` | **[00-Backup] Alerte si KO 15 min** | `sensor.backup_github_status` = `KO` pendant 15 min | Notification persistante + mobile + log erreur |

### Chaîne d'appel complète (boutons dashboard → script)

```
Chip [Push]
  └─ perform-action: input_button.press
       └─ input_button.git_push_manuel → state: on
            └─ Automation [04-Backup] (trigger: state)
                 └─ shell_command.git_backup_push_manual
                      └─ .scripts/ha_git_backup.sh "Manuel"

Chip [Tag weekly] (hold)
  └─ perform-action: input_button.press
       └─ input_button.git_push_weekly_manuel → state: on
            └─ Automation [05-Backup] (trigger: state)
                 └─ shell_command.git_backup_push_weekly
                      └─ .scripts/ha_git_backup.sh weekly
```

### Automations à créer (non présentes dans automations.yaml)

| Alias futur | Rôle | Déclencheur prévu |
|-------------|------|--------------------|
| `redemarrage_quotidien_studio_code_server` | Redémarrer addon Studio Code Server | Bouton dashboard → `button-card: call-service` |
| `db_purge_mariadb_repack` | Purge + repack base MariaDB | Bouton dashboard → `call-service: recorder.purge` |

> ⚠️ Ces deux automations sont référencées dans le code YAML du dashboard mais n'existent pas encore dans `automations.yaml`. Le bouton Restart VSCode et Purge MariaDB ne fonctionneront pas tant qu'elles ne seront pas créées.

---

## 🐛 DÉPANNAGE

### Boutons Push ne font rien
1. Vérifier que `input_button.git_push_manuel` et `input_button.git_push_weekly_manuel` existent dans HA
2. Vérifier que les automations `[04-Backup]` et `[05-Backup]` sont activées
3. Utiliser `perform-action` + `input_button.press` — ne pas appeler `shell_command.*` directement depuis les chips

### Journal affiche `—`
1. Vérifier que `/config/.logs/ha_git_backup.log` existe et contient des lignes `Backup GitHub OK:`
2. Forcer un backup manuel depuis le terminal : `/config/.scripts/ha_git_backup.sh`
3. Recharger le sensor : **Outils développeur → YAML → Recharger command_line**

### Push échoue (token expiré)
1. Générer un nouveau token sur GitHub (Settings → Developer settings → PAT → repo scope)
2. Mettre à jour l'URL remote : `git -C /config remote set-url origin https://TOKEN@github.com/BerrySwann/home_assistant_re-build.git`
3. Tester : `git -C /config push origin main`

### Graphique ApexCharts bleu uniforme (pas de couleur OK/KO)
- Vérifier la présence du `transform: "EVAL: return x === 'OK' ? 1 : 0;"`
- Le sensor doit avoir un historique dans MariaDB

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `sensor.backup_github_status` | `command_line` | ✅ Essentiel |
| `sensor.backup_github_journal` | `command_line` | ✅ Essentiel |
| `sensor.git_last_weekly_tag` | `command_line` | ✅ Essentiel |
| `sensor.github_default_branch` | `command_line` | ✅ Essentiel |
| `input_button.git_push_manuel` | `input_button.yaml` | ✅ Essentiel |
| `input_button.git_push_weekly_manuel` | `input_button.yaml` | ✅ Essentiel |
| `.scripts/ha_git_backup.sh` | Script bash | ✅ Essentiel |
| Token GitHub dans URL remote `.git/config` | Secret Git | ✅ Essentiel |
| `sensor.taille_db_home_assistant` | `sql.yaml` | ✅ Essentiel |
| `custom:mushroom-chips-card` | HACS | ✅ Essentiel |
| `custom:apexcharts-card` | HACS | ✅ Essentiel |
| `custom:bubble-card` | HACS | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

### Configuration YAML
- `command_line/github_maintenance/github_maintenance.yaml`
- `input_button.yaml`
- `shell_command.yaml`
- `sql.yaml`
- `.scripts/ha_git_backup.sh`

### Documentation
- `docs/L5C3_MARIADB/L5C3_VIGNETTE_MARIADB.md` — vignette MariaDB (jauge horseshoe)

---

← Retour : `HOME` | → Suivant : `PAGE_RESERVE`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L5C3_VIGNETTE_MARIADB]]*
