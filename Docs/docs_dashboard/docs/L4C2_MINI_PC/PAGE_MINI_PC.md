# PAGE MINI PC — Documentation complète

> ✅ **STATUT : PAGE DÉPLOYÉE — Mini PC Intel NUC en production (2026-05-03)**

---

![Badge](https://img.shields.io/badge/HA-2026.4-blue)
![Badge](https://img.shields.io/badge/Modifié_le-2026--05--03-lightgrey)
![Badge](https://img.shields.io/badge/Statut-PROD-green)

---

## 📋 MÉTADONNÉES

| Champ | Valeur |
|-------|--------|
| **Path dashboard** | `/dashboard-tablette/systeme-mini-pc` |
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
│   ├── BLOC 5 — Bar-cards Réseau (DL + UL via enp6s18)
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
| IP publique | `sensor.ip_externe` | `action: none` |

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
| Entité | `sensor.temperature_cpu_package` |
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
| Min/Max | 0 – **8 192 MiB** (VM = 8 Go alloués) |
| Target | 5 000 MiB |
| Tap | navigate `#memory` |

### `bar-card` FREE (Mo)
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_memoire_libre` |
| Min/Max | 0 – **8 192 MiB** (VM = 8 Go alloués) |
| Target | 3 000 MiB |
| Tap | navigate `#memory` |

---

## 📦 BLOC 4 — SSD SATA 512 Go

### `bar-card` VM Disk (~30 GiB)
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_utilisation_du_disque` |
| Min/Max | 0 – **30 GiB** (disque virtuel VM ≈ 29.5 GiB) |
| Target | 24 GiB |
| Tap | navigate `#disk` |

> Pas de severity intégrée (couleur fixe `rgb(142,142,142)` — gris).
> Note : le disque physique du NUC est 512 Go (SSD SATA), mais Proxmox alloue ~30 GiB à la VM HA.

---

## 📦 BLOC 5 — Réseau (interface `enp6s18`)

> ⚠️ **Interface réseau Mini PC = `enp6s18`** (≠ RPi4 qui utilisait `end0`)

### `bar-card` Download
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_debit_du_reseau_entrant_via_enp6s18` |
| Min/Max | 0 – 130 MB/s |
| Target | 20 MB/s |
| Couleur | `rgb(81,140,67)` vert |

### `bar-card` Upload
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.system_monitor_debit_du_reseau_sortant_via_enp6s18` |
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

> Entité : `sensor.temperature_cpu_package` — Provenance : `command_line` / `sensors` Linux (`MP_01_sonde_température_mini-pc.yaml`).

### `custom:ring-tile` Température CPU
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.temperature_cpu_package` |
| Min/Max | 0 – 100 °C |
| Tap | navigate `#temp` |

**Couleurs ring** :
- 0–60 °C → `ha_green`
- 65–70 °C → `ha_orange`
- 75–100 °C → `ha_red`

### `custom:mini-graph-card` T° CPU 24h
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.temperature_cpu_package` |
| Couleur | `rgb(255,193,7)` |
| Durée | 24h |
| Tap | navigate `#temp` |

---

## 📦 BLOC 10 — Températures cores (Core 0/1/2/3)

> Entités `sensor.temperature_core_X` — Provenance : `command_line` / `sensors` Linux (`MP_01_sonde_température_mini-pc.yaml`).

### 4 `bar-card` : Core 0 / 1 / 2 / 3
| Entité | Min/Max | Target |
|--------|---------|--------|
| `sensor.temperature_core_0` | 0–100 °C | 75 °C |
| `sensor.temperature_core_1` | 0–100 °C | 75 °C |
| `sensor.temperature_core_2` | 0–100 °C | 75 °C |
| `sensor.temperature_core_3` | 0–100 °C | 75 °C |

**Severity identique pour tous** :
- 0–64 °C → `rgb(81,140,67)` vert
- 65–74 °C → `rgb(255,152,1)` orange
- 75–100 °C → `rgb(244,67,54)` rouge

---

## 📦 BLOC 11 — Température CPU Package (résumé mini)

> Même entité que BLOC 9 — `sensor.temperature_cpu_package`.

### `bar-card` Température CPU (mini)
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.temperature_cpu_package` |
| Min/Max | 0 – 100 °C |
| Target | 88 °C |
| Tap | navigate `#temp` |

---

## 📦 BLOC 12 — Température Carte Mère

> Entité `sensor.temperature_carte_mere` — Provenance : `command_line` / `sensors` Linux (`MP_01_sonde_température_mini-pc.yaml`).

### `bar-card` Température Carte Mère
| Paramètre | Valeur |
|-----------|--------|
| Entité | `sensor.temperature_carte_mere` |
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
| Instantané | `sensor.temperature_cpu_package` | area | color_threshold : vert → jaune (55°C) → rouge (70°C) |
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
| `conso_daily_kwh_entity` | `sensor.prise_mini_pc_ikea_quotidien_um` |

### Carte 2 : `custom:streamline-card` template `conso_mensuelle_appareil`
| Variable | Valeur |
|----------|--------|
| `title` | `Conso. mensuelle Mini P.C.` |
| `energy_entity` | `sensor.prise_mini_pc_ikea_energy` |
| `color` | `gainsboro` |
| `avg_monthly_entity` | `sensor.mini_pc_avg_watts_mensuel` |
| `conso_monthly_kwh_entity` | `sensor.prise_mini_pc_ikea_mensuel_um` |

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

### Groupe A : Températures via script MQTT (dans la VM)

> **Provenance** : `lm-sensors` (paquet Linux) tourne dans la VM HA via un script shell.
> La chaîne complète : `sensors` (VM) → **script** → **MQTT broker** → `sensor.temperature_*` dans HA.
> 
> ⚠️ `system_monitor` ne remonte **aucune** température dans un contexte VM Proxmox — les capteurs hwmon physiques ne sont pas accessibles depuis le guest. Cette solution MQTT contourne la limitation.

| Entité | Source hardware | Chaîne |
|--------|-----------------|--------|
| `sensor.temperature_cpu_package` | CPU Package global | `sensors` (VM) → script → MQTT |
| `sensor.temperature_core_0` | Core 0 | `sensors` (VM) → script → MQTT |
| `sensor.temperature_core_1` | Core 1 | `sensors` (VM) → script → MQTT |
| `sensor.temperature_core_2` | Core 2 | `sensors` (VM) → script → MQTT |
| `sensor.temperature_core_3` | Core 3 | `sensors` (VM) → script → MQTT |
| `sensor.temperature_carte_mere` | Carte mère (Acpi / Board) | `sensors` (VM) → script → MQTT |

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
| `sensor.system_monitor_utilisation_de_la_memoire` | BLOC 3 |
| `sensor.system_monitor_memoire_utilisee` | BLOC 3 + pop-up `#memory` |
| `sensor.system_monitor_memoire_libre` | BLOC 3 |
| `sensor.system_monitor_utilisation_du_disque` | BLOC 4 |
| `sensor.system_monitor_espace_utilise` | pop-up `#disk` |
| `sensor.system_monitor_debit_du_reseau_entrant_via_enp6s18` | BLOC 5 |
| `sensor.system_monitor_debit_du_reseau_sortant_via_enp6s18` | BLOC 5 |
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

### Sensors spéciaux (script MQTT / lm-sensors dans la VM)
| Entité | Usage |
|--------|-------|
| `sensor.temperature_cpu_package` | BLOCS 2, 9, 11 + pop-up `#temp` (ring/mini-graph/apexcharts) |
| `sensor.temperature_core_0` | BLOC 10 |
| `sensor.temperature_core_1` | BLOC 10 |
| `sensor.temperature_core_2` | BLOC 10 |
| `sensor.temperature_core_3` | BLOC 10 |
| `sensor.temperature_carte_mere` | BLOC 12 |
| `sensor.cpu_speed` | BLOC 7 ⚠️ à vérifier dans config |

### Réseau / IP
| Entité | Usage |
|--------|-------|
| `sensor.local_ip` | BLOC 1 (IP interne) |
| `sensor.ip_externe` | BLOC 1 (IP externe) |

### Utility Meter & AVG (Pôle 2 — ✅ dans re-build / ⚠️ à déployer en live)

**Chaîne complète (unité Wh — intentionnel, pas kWh) :**
```
sensor.prise_mini_pc_ikea_power (W natif IKEA Inspelning)
    ↓  sensors/P2_prise/P2_Wh_mini_pc.yaml  (Riemann left, 3 déc., PAS unit_prefix:k → Wh)
sensor.prise_mini_pc_ikea_energie_totale_wh
    ↓  utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml
sensor.prise_mini_pc_ikea_annuel_um
sensor.prise_mini_pc_ikea_mensuel_um
sensor.prise_mini_pc_ikea_hebdomadaire_um
sensor.prise_mini_pc_ikea_quotidien_um
    ↓  templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml  (formule: conso / h → W)
sensor.mini_pc_avg_watts_annuel
sensor.mini_pc_avg_watts_mensuel
sensor.mini_pc_avg_watts_hebdomadaire
sensor.mini_pc_avg_watts_quotidien
```

| Entité | Fichier source |
|--------|----------------|
| `sensor.prise_mini_pc_ikea_energie_totale_wh` | `sensors/P2_prise/P2_Wh_mini_pc.yaml` |
| `sensor.prise_mini_pc_ikea_annuel_um` | `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml` |
| `sensor.prise_mini_pc_ikea_mensuel_um` | `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml` |
| `sensor.prise_mini_pc_ikea_hebdomadaire_um` | `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml` |
| `sensor.prise_mini_pc_ikea_quotidien_um` | `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml` |
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

## ⚠️ LISTE DES POINTS À VÉRIFIER

1. **`sensor.temperature_cpu_package`** et `sensor.temperature_core_X` : entités actives via `MP_01_sonde_température_mini-pc.yaml` — confirmer que `sensors` (lm-sensors) retourne bien les valeurs sur le NUC.
2. **`sensor.temperature_carte_mere`** : idem — vérifier la ligne correspondante dans la sortie `sensors`.
3. **`sensor.cpu_speed`** : localiser le sensor dans la config HA (TREE_ORIGINE / `command_line` ?) et vérifier qu'il fonctionne sur le Mini PC.
4. **`sensor.system_monitor_charge_1m/5m/15m`** : activer les conditions load dans `configuration.yaml`.
5. **Interface réseau `enp6s18`** : confirmée pour le Mini PC Intel NUC (remplace `end0` du RPi4).
6. **RAM VM = 8 Go** : max bar-cards calé sur 8 192 MiB (RAM allouée à la VM Proxmox). NUC physique = 16 Go.
7. **Disk VM ≈ 30 GiB** : disque virtuel Proxmox alloué à la VM HA (~29.5 GiB). NUC physique = 512 Go SSD.
8. **Entités UM + AVG prise Mini PC** : ⚠️ Fichiers créés dans TREE_CORRIGE — **à déployer en live si pas encore fait** :
   - `sensors/P2_prise/P2_Wh_mini_pc.yaml` (Riemann Wh)
   - `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml`
   - `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml`
   - Redémarrer HA → entités `prise_mini_pc_ikea_quotidien/mensuel_um` et `mini_pc_avg_watts_*` créées.
9. **Image** `/local/images/mini pc.png` : à copier sur le serveur HA si absente.

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
