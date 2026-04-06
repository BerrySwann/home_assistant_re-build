<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--13-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Config%20Racine-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/config/` (racine HA) |
| 🔗 **Accès depuis** | Fichiers système — pas de vignette dashboard |
| 🏗️ **Layout** | — |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-13 |
| 🏠 **Version HA** | 2025.2.x → 2.0 |

---

# ⚙️ CONFIG RACINE — DOCUMENTATION DES FICHIERS `/config/*.yaml`

Documentation des 6 fichiers YAML à la racine de `/config/` qui ne sont pas des sous-dossiers modulaires.

---

## 📋 TABLE DES MATIÈRES

1. [configuration.yaml](#1-configurationyaml)
2. [camera.yaml](#2-camerayaml)
3. [input_button.yaml](#3-input_buttonyaml)
4. [groups.yaml](#4-groupsyaml)
5. [shell_command.yaml](#5-shell_commandyaml)
6. [sql.yaml](#6-sqlyaml)
7. [Dépendances croisées](#7-dépendances-croisées)

---

## 1. `configuration.yaml`

**Rôle :** Point d'entrée principal de Home Assistant. Charge tous les modules via `!include` ou `!include_dir_merge_*`. Contient aussi les entités `climate` (SmartIR), le `recorder` MariaDB, et le `panel_custom`.

### Modules inclus

| Directive | Cible | Mode |
|-----------|-------|------|
| `automation` | `automations.yaml` | include |
| `script` | `scripts.yaml` | include |
| `scene` | `scenes.yaml` | include |
| `sensor` | `sensors/` | include_dir_merge_list |
| `template` | `templates/` | include_dir_merge_list |
| `utility_meter` | `utility_meter/` | include_dir_merge_named |
| `command_line` | `command_line/` | include_dir_merge_list |
| `shell_command` | `shell_command.yaml` | include |
| `camera` | `camera.yaml` | include |
| `input_button` | `input_button.yaml` | include |
| `group` | `groups.yaml` | include |
| `sql` | `sql.yaml` | include |

### Entités générées (climate SmartIR)

| Entité | Télécommande | Sonde T° | Sonde Hum. |
|--------|-------------|----------|------------|
| `climate.clim_bureau_rm4_mini` | `remote.clim_bureau` | `sensor.th_bureau_temperature` | `sensor.th_bureau_humidity` |
| `climate.clim_chambre_rm4_mini` | `remote.clim_chambre` | `sensor.th_chambre_temperature` | `sensor.th_chambre_humidity` |
| `climate.clim_salon_rm4_mini` | `remote.clim_salon` | `sensor.th_salon_temperature` | `sensor.th_salon_humidity` |

> `device_code: 1108` (Bureau + Chambre) / `device_code: 1082` (Salon) — codes SmartIR pour le modèle de clim.

### Recorder MariaDB

| Paramètre | Valeur |
|-----------|--------|
| `db_url` | `!secret mariadb_url` |
| `purge_keep_days` | 7 |
| Domaines exclus | `update`, `persistent_notification`, `sun`, `input_text` |
| Globs exclus | `sensor.127_0_0_1*`, `*linkquality`, `*last_seen`, `sensor.date*`, `sensor.time*` |

### Dépendances

- `secrets.yaml` → `mariadb_url` (non versionné)
- `custom_components/smartir/` → intégration HACS SmartIR
- Tous les sous-dossiers modulaires (`sensors/`, `templates/`, `utility_meter/`, `command_line/`)

---

## 2. `camera.yaml`

**Rôle :** Déclare 2 entités caméra de type `local_file` qui affichent les images de vigilance Météo France téléchargées localement.

### Entités

| Entité | Fichier source | Usage |
|--------|---------------|-------|
| `camera.mf_alerte_today` | `/config/www/weather/meteo_france_alerte_today.png` | Pop-up #ALERT — carte vigilance aujourd'hui |
| `camera.mf_alerte_tomorrow` | `/config/www/weather/meteo_france_alerte_tomorrow.png` | Pop-up #ALERT — carte vigilance demain |

### Dépendances

- `command_line/meteo/carte_meteo_france.yaml` → génère les fichiers PNG via API Météo France (script `wget`).
- Automation `1771872569647` → force la MAJ des images au démarrage HA et aux heures clés (06h32, 16h32).

> ⚠️ Si les images n'apparaissent pas dans le dashboard, vérifier que les PNG existent dans `/config/www/weather/`. En cas d'absence : l'automation tente un retry automatique (5 essais).

---

## 3. `input_button.yaml`

**Rôle :** Déclare 2 boutons virtuels HA (`input_button`) permettant de déclencher manuellement le backup Git depuis l'interface.

### Entités

| Entité | Nom affiché | Icône | Rôle |
|--------|-------------|-------|------|
| `input_button.git_push_manuel` | Git Push Manuel | `mdi:github` | Déclenche un backup Git standard (commit + push) |
| `input_button.git_push_weekly_manuel` | Git Push Weekly Manuel | `mdi:tag-outline` | Déclenche un backup Git avec tag ISO hebdomadaire |

### Dépendances

- Appelle `shell_command.git_backup_push_manual` / `shell_command.git_backup_push_weekly` via automation (à définir dans `automations.yaml`).

---

## 4. `groups.yaml`

**Rôle :** Regroupe les capteurs de batteries par fabricant (IKEA, HUE, SONOFF) pour la surveillance centralisée dans la vignette **L5C1 Batteries**.

### Groupes

| Groupe | Nom | Nb entités |
|--------|-----|------------|
| `group.ikea_devices` | IKEA Devices | 12 capteurs battery |
| `group.hue_devices` | HUE Devices | 11 capteurs battery |
| `group.sonoff_devices` | SONOFF Devices | 11 capteurs battery |

**Total surveillé : 34 capteurs de batteries.**

### Entités incluses dans `group.ikea_devices`

`contact_fenetre_bureau`, `contact_fenetre_chambre`, `contact_fenetre_cuisine`, `contact_fenetre_salon`, `detecteur_de_fuite`, `inter_salon_4`, `detecteur_vallhorn`, `inter_tv_chambre_rodret`, `inter_somrig`, `inter_bureau_rodret`, `poussoir_tradfri`, `inter_radiateur_sdb_rodret`

### Entités incluses dans `group.hue_devices`

Boutons HUE Smart Button : `entree_1`, `entree_2`, `eco`, `table`, `cuisine`, `couloir`, `bureau` + `boutton_sdb` + `chambre`, `chambre_gege`, `chambre_eric`

### Entités incluses dans `group.sonoff_devices`

Thermostats SNZB-02 (7 pièces) + contacts fenêtres SNZB-04 (salon, cuisine, bureau, chambre)

### Vignette dashboard

- **L5C1** Surveillance Batteries / Piles — `docs/L5C1_PILES_BATTERIES/`

---

## 5. `shell_command.yaml`

**Rôle :** Expose 3 commandes shell appelables depuis HA (via automation ou bouton) pour exécuter le script de backup Git.

### Commandes

| Clé | Argument passé | Déclencheur typique |
|-----|---------------|---------------------|
| `shell_command.git_backup_push` | *(aucun)* | Automatique — horaire/daily |
| `shell_command.git_backup_push_manual` | `"Manuel"` | `input_button.git_push_manuel` |
| `shell_command.git_backup_push_weekly` | `"weekly"` | `input_button.git_push_weekly_manuel` |

### Script et log

| Fichier | Rôle |
|---------|------|
| `/config/.scripts/ha_git_backup.sh` | Script bash : `git add`, `git commit`, `git push` |
| `/config/.logs/ha_git_backup.log` | Journal de toutes les exécutions (`>>` = append) |

> L'argument passé (`"Manuel"`, `"weekly"`) est utilisé dans le script pour formater le message de commit et éventuellement créer un tag ISO.

---

## 6. `sql.yaml`

**Rôle :** Déclare 1 capteur SQL qui interroge MariaDB pour retourner la taille de la base de données `homeassistant` en MiB.

### Entité

| Entité | unique_id | Unité | device_class |
|--------|-----------|-------|--------------|
| `sensor.taille_db_home_assistant` | `taille_db_home_assistant` | `MiB` | `data_size` |

### Requête

```sql
SELECT ROUND(SUM(data_length + index_length) / POWER(1024, 2), 1) AS value
FROM information_schema.tables
WHERE table_schema = 'homeassistant';
```

> `db_url: !secret mariadb_url` — credentials non versionnés dans `secrets.yaml`.
> `device_class: data_size` → HA affiche automatiquement en MiB/GiB selon la valeur.

### Vignette dashboard

- **L5C3** Taille de la DB MariaDB — `docs/L5C3_MARIADB/`

---

## 7. Dépendances croisées

```
configuration.yaml
  ├── !include camera.yaml         → camera.mf_alerte_today / _tomorrow
  │     └── dépend de command_line/meteo/carte_meteo_france.yaml
  ├── !include input_button.yaml   → git_push_manuel / git_push_weekly_manuel
  │     └── déclenchent shell_command.yaml
  ├── !include groups.yaml         → ikea_devices / hue_devices / sonoff_devices
  │     └── utilisés par L5C1 Batteries (auto-entities)
  ├── !include shell_command.yaml  → git_backup_push*
  │     └── appellent /config/.scripts/ha_git_backup.sh
  └── !include sql.yaml            → sensor.taille_db_home_assistant
        └── affiché dans L5C3 MariaDB
```

---

## 🐛 Dépannage

### `sensor.taille_db_home_assistant` indisponible
1. Vérifier que `secrets.yaml` contient `mariadb_url: mysql://...`
2. Vérifier que le service MariaDB est actif dans les add-ons HA
3. Tester la connexion : `Outils de développement > Modèles > {{ states('sensor.taille_db_home_assistant') }}`

### Caméras Météo France vides / indisponibles
1. Vérifier que les PNG existent dans `/config/www/weather/`
2. Forcer la MAJ : `Outils de développement > Actions > homeassistant.update_entity` sur `sensor.meteo_france_alertes_image_today`
3. Consulter les logs de l'automation (ID `1771872569647`)

### `shell_command` n'exécute rien
1. Vérifier que le script est exécutable : `chmod +x /config/.scripts/ha_git_backup.sh`
2. Consulter le log : `/config/.logs/ha_git_backup.log`
3. Tester manuellement : `Outils de développement > Actions > shell_command.git_backup_push`

---

## 🔗 Fichiers liés

- `command_line/meteo/carte_meteo_france.yaml` — génère les PNG pour `camera.yaml`
- `/config/.scripts/ha_git_backup.sh` — script appelé par `shell_command.yaml`
- `secrets.yaml` — `mariadb_url` (non versionné)
- `docs/L5C1_PILES_BATTERIES/` — dashboard batteries (utilise `groups.yaml`)
- `docs/L5C3_MARIADB/` — dashboard MariaDB (utilise `sql.yaml`)

---

← Retour : `docs/IA/IA_CONTEXT_BASE.md`
