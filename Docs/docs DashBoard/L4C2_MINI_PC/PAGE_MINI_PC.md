# PAGE MINI PC — Documentation complète

> ⚠️ **STATUT : PAGE DÉFINITIVE MINI PC — À DÉPLOYER après migration RPi4 → Mini PC**
> Cette page remplacera `PAGE_RASPI.md` une fois le Mini PC opérationnel en production HA.

---

![Badge](https://img.shields.io/badge/HA-2026.3-blue)
![Badge](https://img.shields.io/badge/Modifié_le-2026--03--25-lightgrey)
![Badge](https://img.shields.io/badge/Statut-PRÊT_migration-orange)

---

## 📋 MÉTADONNÉES

| Champ | Valeur |
|-------|--------|
| **Path dashboard** | `/dashboard-tablette/raspberry-pi4` ← chemin actuel (conservé, aucun impact) |
| **Heading** | `Mini - P.C.` |
| **Icône heading** | `phu:intel-nuc` |
| **Retour (tap heading)** | `/dashboard-tablette/0` |
| **Image** | `/local/images/mini pc.png` |
| **Type layout** | `type: grid` + `type: vertical-stack` (colonne principale + 5 pop-ups) |
| **Doc vignette associée** | `L4C2_VIGNETTE_MINI_PC.md` |
| **Vignette tableau de bord** | L4C2 |

---

## 🏗️ ARCHITECTURE GLOBALE

```
PAGE MINI PC (type: grid)
│
├── 🗃️ COL PRINCIPALE (vertical-stack — grid_columns: 12)
│   ├── BLOC 1 — Image + IP + Uptime
│   ├── BLOC 2 — Bar-cards CPU (USED + Temp)
│   ├── BLOC 3 — Bar-cards RAM (% + USED MB + FREE MB)
│   ├── BLOC 4 — Bar-card SSD SATA 512 Go
│   ├── BLOC 5 — Bar-cards Réseau (DL + UL via enp1s0)
│   ├── BLOC 6 — ring-tile + mini-graph : Utilisation CPU (24h)
│   ├── BLOC 7 — Bar-card CPU SPEED (GHz)
│   ├── BLOC 8 — Bar-cards Charges système (1m / 5m / 15m)
│   ├── BLOC 9 — ring-tile + mini-graph : Température CPU (24h)
│   ├── BLOC 10 — Bar-cards Températures cores (Core 0/1/2/3)
│   ├── BLOC 11 — Bar-card Température CPU package (résumé mini)
│   ├── BLOC 12 — Bar-card Température Carte Mère (résumé mini)
│   └── BLOC 13 — ring-tile + mini-graph : Conso. W (24h)
│       + Bar-card POWER (résumé mini)
│
└── 🔲 5 POP-UPS (bubble-card + contenu)
    ├── #speed  → apexcharts CPU% 24h (3 séries : instantané / moy.1h / moy.730h)
    ├── #temp   → apexcharts T° CPU 24h (3 séries : instantané / moy.1h / moy.730h)
    ├── #conso  → streamline: conso temps réel + conso mensuelle (prise IKEA)
    ├── #disk   → apexcharts espace disque 24h (SSD SATA 512 Go)
    └── #memory → apexcharts mémoire utilisée 24h (16 Go)
```

---

## 📦 BLOC 1 — Image + IP + Uptime

### Image
- **Type** : `type: picture`
- **Source** : `/local/images/mini pc.png`
- CSS : fond transparent, pas de bordure

### IP Interne / IP Externe
| Carte | Entité | Tap action |
|-------|--------|-----------|
| IP Int. (label) | — | `action: none` |
| IP locale | `sensor.local_ip` | navigate `#temp` |
| IP publique | `sensor.myip` | `action: none` |

### Uptime
| Carte | Source | Format |
|-------|--------|--------|
| Uptime (label) | — | — |
| Durée formatée | `sensor.system_monitor_dernier_demarrage` | template Jinja2 : `Xd Xh Xm` |

> Template Uptime :
> ```jinja2
> {% set uptime = (now()|as_timestamp - states('sensor.system_monitor_dernier_demarrage')|as_timestamp) %}
> {% set jours = (uptime / 86400) | int(0) %}
> {%- if jours > 0 -%} {{ jours }}d {{ (uptime - (jours * 86400)) | int(0) | timestamp_custom('%Hh %Mm', false) }}
> {%- else -%} {{ uptime | int(0) | timestamp_custom('%Hh %Mm', false) }}
> {%- endif -%}
> ```

---

## 📦 BLOC 2 — CPU : Utilisation + Température

### `bar-card` CPU USED
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_utilisation_du_processeur` |
| Min/Max | 0 – 100 % |
| Target | 82 % |
| Tap | `action: none` |

**Severity** :
- 0–74 % → `rgb(68,115,158)` (bleu Inactive)
- 75–79 % → `rgb(255,193,7)` (jaune)
- 90–100 % → `rgb(244,67,54)` (rouge Error)

### `bar-card` CPU Temp.
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_temperature_du_processeur` |
| Min/Max | 0 – 100 °C |
| Target | 75 °C |
| Tap | `action: none` |

**Severity** :
- 0–64 °C → `rgb(255,193,7)` (jaune Warning)
- 65–74 °C → `rgb(255,152,1)` (orange)
- 75–100 °C → `rgb(244,67,54)` (rouge Error)

---

## 📦 BLOC 3 — RAM

### `bar-card` Mem. (%)
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_utilisation_de_la_memoire` |
| Min/Max | 0 – 100 % |
| Target | 65 % |
| Max RAM | 16 Go |
| Tap | navigate `#memory` |

**Severity** :
- 0–74 % → `rgb(81,140,67)` (vert)
- 75–79 % → `rgb(255,152,1)` (orange)
- 80–100 % → `rgb(244,67,54)` (rouge)

### `bar-card` USED (Mo)
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_memoire_utilisee` |
| Min/Max | 0 – **16 384 Mo** |
| Target | 7 500 Mo |
| Tap | navigate `#memory` |

### `bar-card` FREE (Mo)
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_memoire_libre` |
| Min/Max | 0 – **16 384 Mo** |
| Target | 7 500 Mo |
| Tap | navigate `#memory` |

---

## 📦 BLOC 4 — SSD SATA 512 Go

### `bar-card` SSD SATA 512 Go
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_utilisation_du_disque` |
| Min/Max | 0 – **524 Go** |
| Target | 470 Go |
| Tap | navigate `#disk` |

> Pas de severity intégrée (couleur fixe `rgb(142,142,142)` — gris).

---

## 📦 BLOC 5 — Réseau (interface `enp1s0`)

> ⚠️ **Interface réseau Mini PC = `enp1s0`** (≠ RPi4 qui utilisait `end0`)

### `bar-card` Download
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_debit_du_reseau_entrant_via_enp1s0` |
| Min/Max | 0 – 130 MB/s |
| Target | 20 MB/s |
| Couleur | `rgb(81,140,67)` vert |

### `bar-card` Upload
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_debit_du_reseau_sortant_via_enp1s0` |
| Min/Max | 0 – 130 MB/s |
| Target | 20 MB/s |
| Couleur | `rgb(244,67,54)` rouge |

---

## 📦 BLOC 6 — ring-tile + mini-graph : CPU Utilisation (24h)

### `custom:ring-tile` CPU Utilisation
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_utilisation_du_processeur` |
| Min/Max | 0 – 100 % |
| Tap | navigate `#speed` |
| Ring type | `open` |

**Couleurs ring** :
- 0–69 % → `ha_green`
- 70–79 % → `ha_orange`
- 80–100 % → `ha_red`

### `custom:mini-graph-card` CPU 24h
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_utilisation_du_processeur` |
| Couleur | `rgb(68,115,158)` |
| Durée | 24h |
| Tap | navigate `#speed` |

---

## 📦 BLOC 7 — CPU SPEED (GHz)

> ⚠️ **`sensor.cpu_speed`** — Entité NON native `system_monitor`.
> Provenance probable : `command_line` sensor (lecture `/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq` ÷ 1 000 000).
> **À VÉRIFIER** que ce sensor remonte bien sur le Mini PC.

### `bar-card` CPU SPEED
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.cpu_speed` |
| Min/Max | 0 – **4 GHz** |
| Target | **3.125 GHz** |
| Tap | navigate `#speed` (via `icon_tap_action`) |

**Severity** :
- 0–2.9 GHz → `rgb(81,140,67)` vert (fréquence normale basse)
- 3.0–3.3 GHz → `rgb(255,152,1)` orange (charge modérée)
- 3.4–4.0 GHz → `rgb(244,67,54)` rouge (pic / boost actif)

---

## 📦 BLOC 8 — Charges système (Load average)

> ⚠️ **`sensor.system_monitor_charge_1m/5m/15m`** — Native `system_monitor` (load average Linux).
> **À VÉRIFIER** : activer dans `configuration.yaml` → `monitor_conditions: [processor_use, disk_use, disk_free, memory_use, memory_free, memory_use_percent, network_in, network_out, last_boot, processor_temperature, load_1m, load_5m, load_15m]`

### 3 `bar-card` : Charge 1m / 5m / 15m
| Entité | Target | Severity |
|--------|--------|----------|
| `sensor.system_monitor_charge_1m` | 75 | 0–2 vert / 2–3 orange / 3–6 rouge |
| `sensor.system_monitor_charge_5m` | 75 | 0–2 vert / 2–3 orange / 3–6 rouge |
| `sensor.system_monitor_charge_15m` | 75 | 0–2 vert / 2–3 orange / 3–6 rouge |

> Min/Max : 0 – 100 (échelle relative au nb de CPUs).

---

## 📦 BLOC 9 — ring-tile + mini-graph : Température CPU (24h)

> ⚠️ **`sensor.temperature_cpu_package_sys`** — Sensor NON natif `system_monitor`.
> Provenance : template `command_line` (lecture `/sys/class/thermal/thermal_zone*/temp` ÷ 1000).
> Voir section **SENSORS SPÉCIAUX** ci-dessous.

### `custom:ring-tile` Température CPU
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.temperature_cpu_package_sys` |
| Min/Max | 0 – 100 °C |
| Tap | navigate `#temp` |

**Couleurs ring** :
- 0–60 °C → `ha_green`
- 65–70 °C → `ha_orange`
- 75–100 °C → `ha_red`

### `custom:mini-graph-card` T° CPU 24h
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.temperature_cpu_package_sys` |
| Couleur | `rgb(255,193,7)` |
| Durée | 24h |
| Tap | navigate `#temp` |

---

## 📦 BLOC 10 — Températures cores (Core 0/1/2/3)

> ⚠️ **`sensor.temperature_core_X_sys`** — Sensors NON natifs `system_monitor`.
> Voir section **SENSORS SPÉCIAUX** ci-dessous.
> Note : Core 3 porte l'ID `sensor.temperature_core_3_sys_2` (suffixe `_2` = doublon automatique HA).

### 4 `bar-card` : Core 0 / 1 / 2 / 3
| Entité | Min/Max | Target |
|--------|---------|--------|
| `sensor.temperature_core_0_sys` | 0–100 °C | 75 °C |
| `sensor.temperature_core_1_sys` | 0–100 °C | 75 °C |
| `sensor.temperature_core_2_sys` | 0–100 °C | 75 °C |
| `sensor.temperature_core_3_sys_2` | 0–100 °C | 75 °C |

**Severity identique pour tous** :
- 0–64 °C → `rgb(81,140,67)` vert
- 65–74 °C → `rgb(255,152,1)` orange
- 75–100 °C → `rgb(244,67,54)` rouge

---

## 📦 BLOC 11 — Température CPU Package (résumé mini)

> ⚠️ Même entité que BLOC 9 — `sensor.temperature_cpu_package_sys`.

### `bar-card` Température CPU (mini)
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.temperature_cpu_package_sys` |
| Min/Max | 0 – 100 °C |
| Target | 88 °C |
| Tap | navigate `#temp` |

---

## 📦 BLOC 12 — Température Carte Mère

> ⚠️ **`sensor.temperature_carte_mere_sys`** — Sensor NON natif `system_monitor`.
> Voir section **SENSORS SPÉCIAUX** ci-dessous.

### `bar-card` Température Carte Mère
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.temperature_carte_mere_sys` |
| Min/Max | 0 – 100 °C |
| Target | 88 °C |
| Tap | navigate `#temp` |

**Severity** :
- 0–64 °C → vert / 65–74 °C → orange / 75–100 °C → rouge

---

## 📦 BLOC 13 — ring-tile + mini-graph : Consommation W (24h) + Bar-card Power

### `custom:ring-tile` Conso. CPU
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.prise_mini_pc_ikea_power` |
| Min/Max | 0 – 30 W |
| Tap | navigate `#conso` |

**Couleurs ring** :
- 0–13 W → `ha_green`
- 14–18 W → `ha_orange`
- 19–30 W → `ha_red`

### `custom:mini-graph-card` Conso 24h
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.prise_mini_pc_ikea_power` |
| Couleur | `gainsboro` |
| Durée | 24h |
| Tap | navigate `#conso` |

### `bar-card` POWER (mini)
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.prise_mini_pc_ikea_power` |
| Min/Max | 0 – 25 W |
| Target | 22 W |
| Tap | navigate `#conso` |

**Severity** :
- 0–13 W → vert / 14–18 W → orange / 19–30 W → rouge

---

## 🔲 POP-UP `#speed` — Utilisation CPU (apexcharts 24h)

| Paramètre | Valeur |
|-----------|--------|
| Hash | `#speed` |
| Titre bubble | `Utilisation du CPU` |
| Icône | `mdi:cpu-64-bit` |
| `graph_span` | 24h |
| `experimental` | `color_threshold: true`, `brush: true` |

**3 séries** :
| Série | Entité | Type | Description |
|-------|--------|------|-------------|
| Instantané | `sensor.system_monitor_utilisation_du_processeur` | area / stepline | color_threshold : bleu → jaune (65%) → rouge (85%) |
| Moy.(24h) | même entité | line / smooth | `group_by avg 1h` — couleur rouge |
| Moy.(730hrs) | même entité | — | `group_by avg 730h` — affiché hors graphique (référence long terme) |

---

## 🔲 POP-UP `#temp` — Température CPU (apexcharts 24h)

| Paramètre | Valeur |
|-----------|--------|
| Hash | `#temp` |
| Titre bubble | `Température du processeur` |
| Icône | `mdi:thermometer` |

**3 séries** :
| Série | Entité | Type | Description |
|-------|--------|------|-------------|
| Instantané | `sensor.system_monitor_temperature_du_processeur` | area | color_threshold : vert → jaune (55°C) → rouge (70°C) |
| Moy.(24h) | même entité | line | `group_by avg 1h` — rouge |
| Moy.(730hrs) | même entité | — | hors graphique |

---

## 🔲 POP-UP `#conso` — Consommation Prise Mini PC (streamline)

| Paramètre | Valeur |
|-----------|--------|
| Hash | `#conso` |
| Titre bubble | `Consommation Mini-PC` |
| Icône | `mdi:lightning-bolt-circle` |

### Carte 1 : `custom:streamline-card` template `conso_temps_reel_appareil`
| Variable | Valeur |
|----------|--------|
| `card_title` | `Prise Mini P.C.` |
| `energy_entity` | `sensor.prise_mini_pc_ikea_power` |
| `energy_color` | `gainsboro` |
| `current_entity` | `sensor.prise_mini_pc_ikea_current` |
| `avg_daily_entity` | `sensor.mini_pc_avg_watts_quotidien` |
| `conso_daily_kwh_entity` | `sensor.prise_mini_pc_ikea_quotidien_wh_um` |

### Carte 2 : `custom:streamline-card` template `conso_mensuelle_appareil`
| Variable | Valeur |
|----------|--------|
| `title` | `Conso. mensuelle Mini P.C.` |
| `energy_entity` | `sensor.prise_mini_pc_ikea_energy` |
| `color` | `gainsboro` |
| `avg_monthly_entity` | `sensor.mini_pc_avg_watts_mensuel` |
| `conso_monthly_kwh_entity` | `sensor.prise_mini_pc_ikea_mensuel_wh_um` |

---

## 🔲 POP-UP `#disk` — Espace disque SSD (apexcharts 24h)

| Paramètre | Valeur |
|-----------|--------|
| Hash | `#disk` |
| Titre bubble | `Espace disque utilisé (SSD SATA)` |
| Icône | `mdi:harddisk` |
| Titre graphique | `Disque (512Go)` |
| `brush: selection_span` | 6h |

**Série** : `sensor.system_monitor_espace_utilise`
- color_threshold : vert → orange (7 500) → rouge (10 000)

---

## 🔲 POP-UP `#memory` — Mémoire utilisée (apexcharts 24h)

| Paramètre | Valeur |
|-----------|--------|
| Hash | `#memory` |
| Titre bubble | `Mémoire utilisée` |
| Icône | `mdi:memory` |
| Titre graphique | `MEMOIRE (16Go)` |
| `brush: selection_span` | 3h |

**Série** : `sensor.system_monitor_memoire_utilisee`
- color_threshold : vert → orange (14 000 Mo) → rouge (15 000 Mo)

---

## 🔍 SENSORS SPÉCIAUX — PROVENANCE & STATUT

Ces entités ne font **pas** partie de l'intégration `system_monitor` native de HA.

### Groupe A : Températures via `command_line` / fichiers `/sys/`

> **Provenance probable** : template `command_line` dans l'ancienne config (`12_1_sonde_température_mini-pc.yaml` → TREE_ORIGINE). Ces sensors lisent les fichiers de température Linux (thermal zones, hwmon) en millidegrees Kelvin / Celsius et divisent par 1000.

| Entité | Source hardware | Fichier probable |
|--------|-----------------|-----------------|
| `sensor.temperature_cpu_package_sys` | CPU Package global | `/sys/class/hwmon/hwmon*/temp1_input` ÷ 1000 |
| `sensor.temperature_core_0_sys` | Core 0 | `/sys/class/hwmon/hwmon*/temp2_input` ÷ 1000 |
| `sensor.temperature_core_1_sys` | Core 1 | `/sys/class/hwmon/hwmon*/temp3_input` ÷ 1000 |
| `sensor.temperature_core_2_sys` | Core 2 | `/sys/class/hwmon/hwmon*/temp4_input` ÷ 1000 |
| `sensor.temperature_core_3_sys_2` | Core 3 | `/sys/class/hwmon/hwmon*/temp5_input` ÷ 1000 |
| `sensor.temperature_carte_mere_sys` | Carte mère (Acpi / Board) | `/sys/class/thermal/thermal_zone0/temp` ÷ 1000 |

> ⚠️ Le suffixe `_sys` provient du `unique_id` de l'entité dans HA. Le `_2` de `temperature_core_3_sys_2` indique une collision de nom corrigée automatiquement par HA.

> ⚠️ **Action requise lors de la migration** : vérifier que ces sensors remontent bien les bonnes valeurs sur le Mini PC (les chemins `/sys/class/hwmon/` peuvent varier selon le chipset `x86_64` vs RPi ARM).

### Groupe B : CPU Speed

| Entité | Source hardware | Notes |
|--------|-----------------|-------|
| `sensor.cpu_speed` | Fréquence CPU courante | Probable `command_line` → `/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq` ÷ 1 000 000 (Hz → GHz) |

> ⚠️ **À VÉRIFIER** : ce sensor n'est pas référencé dans TREE_CORRIGE. Peut être un sensor natif de l'intégration `system_monitor` v2026 ou un `command_line` à migrer.

### Groupe C : Charges système (Load average)

| Entité | Source | Notes |
|--------|--------|-------|
| `sensor.system_monitor_charge_1m` | `system_monitor` natif | `monitor_condition: load_1m` |
| `sensor.system_monitor_charge_5m` | `system_monitor` natif | `monitor_condition: load_5m` |
| `sensor.system_monitor_charge_15m` | `system_monitor` natif | `monitor_condition: load_15m` |

> ⚠️ **À VÉRIFIER** dans `configuration.yaml` : activer les conditions `load_1m`, `load_5m`, `load_15m` dans le bloc `system_monitor:`.

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### Intégration `system_monitor` (natif HA)
| Entité | Usage dans la page |
|--------|-------------------|
| `sensor.system_monitor_utilisation_du_processeur` | BLOCS 2, 6 + pop-up `#speed` |
| `sensor.system_monitor_temperature_du_processeur` | BLOC 2 + pop-up `#temp` |
| `sensor.system_monitor_utilisation_de_la_memoire` | BLOC 3 |
| `sensor.system_monitor_memoire_utilisee` | BLOC 3 + pop-up `#memory` |
| `sensor.system_monitor_memoire_libre` | BLOC 3 |
| `sensor.system_monitor_utilisation_du_disque` | BLOC 4 |
| `sensor.system_monitor_espace_utilise` | pop-up `#disk` |
| `sensor.system_monitor_debit_du_reseau_entrant_via_enp1s0` | BLOC 5 |
| `sensor.system_monitor_debit_du_reseau_sortant_via_enp1s0` | BLOC 5 |
| `sensor.system_monitor_dernier_demarrage` | BLOC 1 (Uptime template) |
| `sensor.system_monitor_charge_1m` | BLOC 8 ⚠️ à activer |
| `sensor.system_monitor_charge_5m` | BLOC 8 ⚠️ à activer |
| `sensor.system_monitor_charge_15m` | BLOC 8 ⚠️ à activer |

### Prise IKEA Inspelning (Zigbee2MQTT — Pôle 2)
| Entité | Usage |
|--------|-------|
| `sensor.prise_mini_pc_ikea_power` | BLOCS 13 + pop-up `#conso` |
| `sensor.prise_mini_pc_ikea_current` | pop-up `#conso` (streamline) |
| `sensor.prise_mini_pc_ikea_energy` | pop-up `#conso` (streamline mensuel) |

### Sensors spéciaux (command_line / thermal zones) ⚠️
| Entité | Usage |
|--------|-------|
| `sensor.temperature_cpu_package_sys` | BLOCS 9, 11 + pop-up (ring/mini-graph) |
| `sensor.temperature_core_0_sys` | BLOC 10 |
| `sensor.temperature_core_1_sys` | BLOC 10 |
| `sensor.temperature_core_2_sys` | BLOC 10 |
| `sensor.temperature_core_3_sys_2` | BLOC 10 ⚠️ ID avec `_2` |
| `sensor.temperature_carte_mere_sys` | BLOC 12 |
| `sensor.cpu_speed` | BLOC 7 ⚠️ à vérifier dans config |

### Réseau / IP
| Entité | Usage |
|--------|-------|
| `sensor.local_ip` | BLOC 1 (IP interne) |
| `sensor.myip` | BLOC 1 (IP externe) |

### Utility Meter & AVG (Pôle 2 — ✅ dans re-build / ⚠️ à déployer en live)

**Chaîne complète (unité Wh — intentionnel, pas kWh) :**
```
sensor.prise_mini_pc_ikea_power (W natif NOUS)
    ↓  sensors/P2_prise/P2_Wh_mini_pc.yaml  (Riemann left, 3 déc., PAS unit_prefix:k → Wh)
sensor.prise_mini_pc_ikea_energie_totale_wh
    ↓  utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml
sensor.prise_mini_pc_ikea_annuel_wh_um
sensor.prise_mini_pc_ikea_mensuel_wh_um
sensor.prise_mini_pc_ikea_hebdomadaire_wh_um
sensor.prise_mini_pc_ikea_quotidien_wh_um
    ↓  templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml  (formule: conso / h → W)
sensor.mini_pc_avg_watts_annuel
sensor.mini_pc_avg_watts_mensuel
sensor.mini_pc_avg_watts_hebdomadaire
sensor.mini_pc_avg_watts_quotidien
```

| Entité | Fichier source |
|--------|----------------|
| `sensor.prise_mini_pc_ikea_energie_totale_wh` | `sensors/P2_prise/P2_Wh_mini_pc.yaml` |
| `sensor.prise_mini_pc_ikea_annuel_wh_um` | `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml` |
| `sensor.prise_mini_pc_ikea_mensuel_wh_um` | `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml` |
| `sensor.prise_mini_pc_ikea_hebdomadaire_wh_um` | `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml` |
| `sensor.prise_mini_pc_ikea_quotidien_wh_um` | `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml` |
| `sensor.mini_pc_avg_watts_annuel` | `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml` |
| `sensor.mini_pc_avg_watts_mensuel` | `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml` |
| `sensor.mini_pc_avg_watts_hebdomadaire` | `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml` |
| `sensor.mini_pc_avg_watts_quotidien` | `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml` |

---

## 🔧 CARTE HACS REQUISES

| Carte | Usage |
|-------|-------|
| `custom:bar-card` | Blocs 2 à 5, 7, 8, 10, 11, 12, 13 |
| `custom:ring-tile` | Blocs 6, 9, 13 |
| `custom:mini-graph-card` | Blocs 6, 9, 13 |
| `custom:bubble-card` | 5 pop-ups |
| `custom:apexcharts-card` | Pop-ups #speed, #temp, #disk, #memory |
| `custom:streamline-card` | Pop-up #conso |
| `custom:mushroom-template-card` | Bloc 1 (IP, Uptime) |
| `custom:stack-in-card` | Structure générale |
| `custom:mod-card` (card-mod) | CSS partout |

---

## ⚠️ LISTE DES POINTS À VÉRIFIER LORS DE LA MIGRATION

1. **`sensor.temperature_cpu_package_sys`** et les `sensor.temperature_core_X_sys` : vérifier que les chemins `/sys/class/hwmon/` sont corrects sur le Mini PC (Intel NUC / x86-64).
2. **`sensor.temperature_carte_mere_sys`** : idem, le chemin thermal_zone peut différer.
3. **`sensor.cpu_speed`** : localiser le sensor dans la config HA (TREE_ORIGINE / `command_line` ?) et vérifier qu'il fonctionne sur le Mini PC.
4. **`sensor.system_monitor_charge_1m/5m/15m`** : activer les conditions load dans `configuration.yaml`.
5. **Interface réseau `enp1s0`** : confirmée pour le Mini PC (remplace `end0` du RPi4).
6. **RAM max 16 384 Mo** : confirmé (16 Go) — les bar-cards sont déjà configurées en conséquence.
7. **SSD max 524 Go** : confirmé (SSD SATA 512 Go formaté ≈ 512 Go utilisables).
8. **Entités UM + AVG prise Mini PC** : ⚠️ Fichiers créés dans le repo `home_assistant_re-build` (TREE_CORRIGE) — **pas encore copiés dans la config live**. À déployer :
   - `sensors/P2_prise/P2_Wh_mini_pc.yaml` (Riemann kWh)
   - `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml`
   - `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml`
   - Redémarrer HA → les entités `prise_mini_pc_ikea_quotidien/mensuel_kwh_um` et `mini_pc_avg_watts_quotidien/mensuel` seront créées.
9. **Image** `/local/images/mini pc.png` : à copier sur le serveur HA.

---

## 🔗 FICHIERS LIÉS

| Fichier | Rôle |
|---------|------|
| `docs/L4C2_MINI_PC/L4C2_VIGNETTE_MINI_PC.md` | Doc vignette tableau de bord |
| `docs/L4C2_MINI_PC/PAGE_RASPI.md` | Page transitoire (ancienne page RPi4) |
| `docs/DEPENDANCES_GLOBALES.md` | Tableau récap vignettes |
| `utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml` | UM prise Mini PC (à compléter) |
| `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml` | AVG watts prise Mini PC (à compléter) |
| `sensors/P2_prise/P2_kWh_prises.yaml` | kWh intégration prise IKEA |


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L4C2_VIGNETTE_MINI_PC]]  [[PAGE_RASPI]]*
