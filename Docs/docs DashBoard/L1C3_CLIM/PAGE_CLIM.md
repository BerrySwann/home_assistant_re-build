<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--04--17-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/dashboard-tablette/clim` |
| 🔗 **Accès depuis** | Vignette L1C3 (tap) |
| 🏗️ **Layout** | `type: grid` (colonne unique) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-04-17 |
| 🏠 **Version HA** | 2026.3 |

---

# ❄️ PAGE CLIM / RADIATEUR

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Section BILAN GLOBAL](#section-bilan-global)
4. [Section SALON](#section-salon)
5. [Section CUISINE](#section-cuisine)
6. [Section BUREAU](#section-bureau)
7. [Section SDB](#section-sdb)
8. [Section CHAMBRE](#section-chambre)
9. [Pop-up #calcul](#pop-up-calcul)
10. [Entités utilisées — Provenance complète](#entités-utilisées--provenance-complète)
11. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page de contrôle complet du **Pôle 1 Chauffage & Climatisation**. Elle regroupe sur une seule colonne scrollable les 5 équipements (3 clims, 1 radiateur, 1 soufflant SdB) avec pour chacun : un séparateur contextuel, un heading avec badges de contrôle rapide, un thermostat HA natif, et une barre de consommation instantanée conditionnelle.

En tête de page : un bloc bilan global (consommation totale, chips conditionnels par pièce active). En bas : popup `#calcul` avec le détail du calcul delta T° intérieur/extérieur.

---

## 🏗️ ARCHITECTURE

```
/dashboard-tablette/clim
│
├── HEADING  "CLIM. / RADIATEUR"
│       badge: sensor.temperature_delta_affichage → popup #calcul
│
├── [CONDITIONAL] Bloc bilan (si au moins 1 pièce active)
│       ├── text-divider "Consomation TOTAL Climatisations & Radiateurs"
│       ├── mushroom-chips-card (6 chips conditionnels — 1 par pièce active)
│       └── bar-card auto-entities → sensor.conso_clim_rad_total (si > 0.1W)
│
├── ── SALON ──
│       ├── text-divider "Climatiseur du SALON"
│       ├── [CONDITIONAL] Warning arrêt sécurisé en cours
│       ├── [CONDITIONAL] Warning prise coupée
│       ├── heading badges (remote / schedules / power W / power switch)
│       ├── thermostat climate.clim_salon_rm4_mini
│       └── bar-card sensor.clim_salon_nous_power (si > 0.1W)
│
├── ── CUISINE ──
│       ├── text-divider "Radiateur électrique de la CUISINE"
│       ├── heading badges (switch / schedules / power W)
│       ├── thermostat climate.radiateur_cuisine
│       └── bar-card sensor.radiateur_elec_cuisine_power (si > 0.1W)
│
├── ── BUREAU ──
│       ├── text-divider "Climatiseur du BUREAU"
│       ├── [CONDITIONAL] Warning arrêt sécurisé en cours
│       ├── [CONDITIONAL] Warning prise coupée
│       ├── heading badges (remote / schedules / power W / power switch)
│       ├── thermostat climate.clim_bureau_rm4_mini
│       └── bar-card sensor.clim_bureau_nous_power (si > 0.1W)
│
├── ── SDB ──
│       ├── text-divider "Chauffage Salle de Bain"
│       ├── heading badges (remote / schedules / power W / power switch)
│       ├── thermostat climate.soufflant_salle_de_bain
│       ├── button-card soufflant_sdb (état résistance + delta T°) — si inter ON
│       └── bar-card sensor.prise_soufflant_salle_de_bain_nous_power (si > 0.1W)
│
├── ── CHAMBRE ──
│       ├── text-divider "Climatiseur de la CHAMBRE"
│       ├── [CONDITIONAL] Warning arrêt sécurisé en cours
│       ├── [CONDITIONAL] Warning prise coupée
│       ├── heading badges (remote / schedules / power W / power switch)
│       ├── thermostat climate.clim_chambre_rm4_mini
│       └── bar-card sensor.clim_chambre_nous_power (si > 0.1W)
│
├── Pop-up #calcul
│       ├── bubble-card header
│       └── streamline-card template: calcule_temp_cible
│
└── streamline-card template: nav_bar
```

---

## 📊 SECTION BILAN GLOBAL

### Heading principal
```yaml
type: heading
icon: mdi:sun-snowflake
heading: CLIM.  / RADIATEUR
heading_style: title
badges:
  - type: entity
    entity: sensor.temperature_delta_affichage   # → popup #calcul
```

### Conditional bilan (au moins 1 pièce active)
Affiché si `au moins 1` des entités `*_power_status_affichage ≠ "off"` :
- `sensor.salon_power_status_affichage`
- `sensor.cuisine_power_status_affichage`
- `sensor.bureau_power_status_affichage`
- `sensor.sdb_power_status_affichage`
- `sensor.sdb_seche_serviettes_power_status_affichage`
- `sensor.chambre_power_status_affichage`

Seuil `_affichage` = puissance > **1W** (contre > 50W pour `_power_status`). Permet d'afficher le bloc même en veille.

### mushroom-chips-card — 6 chips conditionnels

| Chip | Condition d'affichage | Source état | Icône |
|------|----------------------|-------------|-------|
| Salon | `sensor.salon_power_status ≠ off` | `sensor.clim_salon_etat` | `mdi:air-conditioner` |
| Cuisine | `sensor.cuisine_power_status ≠ off` | `sensor.radiateur_cuisine_etat` | `mdi:heating-coil` |
| Bureau | `sensor.bureau_power_status ≠ off` | `sensor.clim_bureau_etat` | `mdi:air-conditioner` |
| SdB Soufflant | `sensor.sdb_soufflant_power_status ≠ off` | `sensor.sdb_soufflant_power_etat` | `mdi:heat-wave` |
| SdB Serviette | `sensor.sdb_seche_serviette_power_status ≠ off` | `sensor.sdb_seche_serviette_etat` | `mdi:heating-coil` |
| Chambre | `sensor.chambre_power_status ≠ off` | `sensor.clim_chambre_etat` | `mdi:air-conditioner` |

#### Couleurs icônes chips

| État | Couleur | HEX |
|------|---------|-----|
| `Cool` | Bleu ciel | `#87CEEB` |
| `Heat` | Orange | `#ff6100` |
| `Fan` | Turquoise | `#40E0D0` |
| `Off` | Rouge | `#FF0000` |

### bar-card total (conditionnel visibility > 0.1W)
```yaml
entity_id: sensor.conso_clim_rad_total
unit_of_measurement: W
# source: templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml
```

#### Graduation sévérité bar-card (commune à toutes les sections)

| Plage (W) | Couleur |
|-----------|---------|
| 0 – 5 | `gainsboro` (éteint) |
| 5 – 49 | `rgb(102, 255, 102)` vert clair (veille/ventil) |
| 50 – 249 | `rgb(0, 102, 0)` vert foncé (basse conso) |
| 250 – 499 | `orange` |
| 500 – 749 | `darkorange` |
| 750 – 999 | `red` |
| 1000 – 6000 | `darkred` (forte charge) |

---

## 🛋️ SECTION SALON

### Warnings conditionnels (2 states mutuellement exclusifs)

**Warning ROUGE** — arrêt sécurisé en cours :
```yaml
conditions:
  - entity: input_boolean.clim_salon_arret_securise_en_cours  state: "on"
  - entity: sensor.salon_power_lock                          state: "on"
# text-divider-color: rgb(234, 67, 53)
# text: "⚠️ Clim SALON en cours d'arrêt ⚠️"
```

**Warning AMBER** — prise coupée :
```yaml
conditions:
  - entity: input_boolean.clim_salon_arret_securise_en_cours  state: "off"
  - entity: switch.clim_salon_nous                            state: "off"
  - entity: sensor.salon_power_status_affichage               state: "off"
# text-divider-color: #FFA000
# text: 'La prise extérieur "CLIM SALON" est coupée'
```

### Heading Clim. Salon — badges

| Badge | Entité | Rôle |
|-------|--------|------|
| Remote | `remote.clim_salon` | État IR |
| Sem. | `switch.schedule_clim_du_salon_week` | Programme semaine |
| Week-End | `switch.schedule_clim_du_salon_week_end` | Programme week-end |
| Power W | `sensor.clim_salon_nous_power` | Conso instantanée |
| Power ON/OFF | `switch.clim_salon_nous` → `script.j_1_1_salon_clim_on_off_intelligent` | Coupe/allume la prise |

> Tap heading → `/dashboard-tablette/prog-clim-salon`

> **Note schedules** : `switch.schedule_clim_du_salon_week/week_end` sont gérés par l'intégration **Scheduler** (HACS). La configuration des plages horaires est à définir séparément.

### Thermostat
```yaml
entity: climate.clim_salon_rm4_mini
name: Clim SALON (+1°)   ← +1° = correction de décalage calibré
features:
  - hvac_modes: [off, fan_only, heat, cool]
  - fan_modes:  [auto, quiet, high, med, low]
```

### bar-card puissance (conditionnel > 0.1W)
```
sensor.clim_salon_nous_power
```

---

## 🍳 SECTION CUISINE

> Pas de warning prise coupée (le radiateur cuisine n'a pas de logique arrêt sécurisé).

### Heading Rad. Cuisine — badges

| Badge | Entité | Rôle |
|-------|--------|------|
| ON/OFF | `switch.radiateur_elec_cuisine` | Toggle direct |
| Sem. | `switch.schedule_radiateur_cuisine_week` | Programme semaine |
| Week-End | `switch.schedule_radiateur_cuisine_week_end` | Programme week-end |
| Power W | `sensor.radiateur_elec_cuisine_power` | Conso instantanée |
| Power (dupliqué) | `switch.radiateur_elec_cuisine` | Visuel état |

> Tap heading → `/dashboard-tablette/prog-radiateur-cuisine`

### Thermostat
```yaml
entity: climate.radiateur_cuisine
features:
  - type: climate-hvac-modes   ← modes réduits (off / heat uniquement)
show_current_as_primary: false
```

### bar-card puissance (conditionnel > 0.1W)
```
sensor.radiateur_elec_cuisine_power
```

---

## 🖥️ SECTION BUREAU

### Warnings conditionnels (identiques à Salon)

**Warning ROUGE** — arrêt sécurisé :
```yaml
entity: input_boolean.clim_bureau_arret_securise_en_cours + sensor.bureau_power_lock
```

**Warning AMBER** — prise coupée :
```yaml
entity: input_boolean.clim_bureau_arret_securise_en_cours (off) + switch.clim_bureau_nous (off) + sensor.bureau_power_status_affichage (off)
```

### Heading clim. Bureau — badges

| Badge | Entité | Rôle |
|-------|--------|------|
| Remote | `remote.clim_bureau` | État IR |
| Sem. | `switch.schedule_clim_du_bureau_week` | Programme semaine |
| Week-End | `switch.schedule_clim_du_bureau_week_end` | Programme week-end |
| Power W | `sensor.clim_bureau_nous_power` | Conso instantanée |
| Power ON/OFF | `switch.clim_bureau_nous` → `script.j_1_2_bureau_clim_on_off_intelligent` | Coupe/allume prise |

> Tap heading → `/dashboard-tablette/prog-clim-bureau`

### Thermostat
```yaml
entity: climate.clim_bureau_rm4_mini
name: Clim du BUREAU (-1°)   ← -1° = correction de décalage calibré
features:
  - hvac_modes: [off, fan_only, heat, cool]
  - fan_modes:  [auto, comfort, breeze, level1..5, powerful]
```

### bar-card puissance (conditionnel > 0.1W)
```
sensor.clim_bureau_nous_power
```

---

## 🛁 SECTION SDB

> Pas de warning arrêt sécurisé ni prise coupée pour le soufflant.

### Heading Radiateur SdB — badges

| Badge | Entité | Rôle |
|-------|--------|------|
| Remote | `remote.soufflant_sdb` | État IR |
| Sem. | `switch.schedule_soufflant_salle_de_bain_week` | Programme semaine |
| Week-End | `switch.schedule_soufflant_salle_de_bain_week_end` | Programme week-end |
| Power W | `sensor.prise_soufflant_salle_de_bain_nous_power` | Conso instantanée |
| Power ON/OFF | `switch.prise_soufflant_salle_de_bain_nous` → toggle | Coupe/allume prise |

> Tap heading → `/dashboard-tablette/prog-soufflant-sdb`

### Thermostat
```yaml
entity: climate.soufflant_salle_de_bain
features:
  - type: climate-hvac-modes   hvac_modes: [off, heat]
show_current_as_primary: false
```

### button-card soufflant_sdb (état résistance)
Affiché uniquement si `switch.inter_soufflant_salle_de_bain = on`.

| Élément | Source | Détail |
|---------|--------|--------|
| Visibilité | `switch.inter_soufflant_salle_de_bain` | Masqué si inter OFF |
| Icône | `input_select.etat_resistance_soufflant_sdb` | radiator (2000W/1000W) / fan (0W) / radiator-off |
| Couleur icône | `input_select.etat_resistance_soufflant_sdb` | `#ff9800` 2000W / `#fdd835` 1000W / `#2196f3` 0W / `#44739e` off |
| Animation | `input_select.etat_resistance_soufflant_sdb` | blink 2s si résistance active |
| State display | `input_select.etat_resistance_soufflant_sdb` | Valeur directe (2000W / 1000W / 0W) |
| Label | `sensor.th_salle_de_bain_temperature` + `climate.soufflant_salle_de_bain.temperature` | `T°réelle (±ΔT°)` |
| Entité principale | `sensor.statut_soufflant_sdb` | État narratif du soufflant |

```javascript
// Label calculé :
const temp   = parseFloat(states['sensor.th_salle_de_bain_temperature'].state).toFixed(1);
const target = parseFloat(states['climate.soufflant_salle_de_bain'].attributes.temperature).toFixed(1);
const delta  = (temp - target).toFixed(1);
// → "23.2°C (+1.2°C)"
```

Sources pour ce bloc :
- `templates/Inter_BP_Virtuel/BI_02_switch_inter_sdb.yaml` → `switch.inter_soufflant_salle_de_bain`
- `[NAT]` input_select.yaml → `input_select.etat_resistance_soufflant_sdb`

### bar-card puissance (conditionnel > 0.1W)
```
sensor.prise_soufflant_salle_de_bain_nous_power
```

---

## 🛏️ SECTION CHAMBRE

### Warnings conditionnels (identiques à Salon)

**Warning ROUGE** — arrêt sécurisé :
```yaml
entity: input_boolean.clim_chambre_arret_securise_en_cours + sensor.chambre_power_lock
```

**Warning AMBER** — prise coupée :
```yaml
entity: input_boolean.clim_chambre_arret_securise_en_cours (off) + switch.clim_chambre_nous (off) + sensor.chambre_power_status_affichage (off)
```

### Heading clim. Chambre — badges

| Badge | Entité | Rôle |
|-------|--------|------|
| Remote | `remote.clim_chambre` | État IR |
| Sem. | `switch.schedule_clim_de_la_chambre_week` | Programme semaine |
| Week-End | `switch.schedule_clim_de_la_chambre_week_end` | Programme week-end |
| Power W | `sensor.clim_chambre_nous_power` | Conso instantanée |
| Power ON/OFF | `switch.clim_chambre_nous` → `script.j_1_3_chambre_clim_on_off_intelligent` | Coupe/allume prise |

> Tap heading → `/dashboard-tablette/prog-clim-chambre`

### Thermostat
```yaml
entity: climate.clim_chambre_rm4_mini
name: Clim de la CHAMBRE
show_current_as_primary: false
features:
  - hvac_modes: [off, fan_only, heat, cool]
  - fan_modes:  [auto, breeze, powerful, level1..5]
```

### bar-card puissance (conditionnel > 0.1W)
```
sensor.clim_chambre_nous_power
```

---

## 🔲 POP-UP #calcul

```yaml
type: custom:bubble-card
card_type: pop-up
hash: "#calcul"
name: CALCUL DU DELTA Intérieur <-> Extérieur
icon: mdi:delta
```

Contenu : `streamline-card template: calcule_temp_cible`

Ce template affiche le détail du calcul du delta T° utilisé pour la recommandation ADEME. Source : streamline templates (non documenté ici — voir template `calcule_temp_cible`).

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### Templates P1 (TREE_CORRIGE)

| Entité | Fichier | Rôle sur la page |
|--------|---------|-----------------|
| `sensor.temperature_delta_affichage` | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | Badge heading principal |
| `sensor.salon_power_status_affichage` | `ui_dashboard/ui_dashboard.yaml` | Condition bloc bilan |
| `sensor.cuisine_power_status_affichage` | `ui_dashboard/ui_dashboard.yaml` | Condition bloc bilan |
| `sensor.bureau_power_status_affichage` | `ui_dashboard/ui_dashboard.yaml` | Condition bloc bilan |
| `sensor.sdb_power_status_affichage` | `ui_dashboard/ui_dashboard.yaml` | Condition bloc bilan |
| `sensor.sdb_seche_serviettes_power_status_affichage` | `ui_dashboard/ui_dashboard.yaml` | Condition bloc bilan |
| `sensor.chambre_power_status_affichage` | `ui_dashboard/ui_dashboard.yaml` | Condition bloc bilan |
| `sensor.salon_power_status` | `ui_dashboard/ui_dashboard.yaml` | Chips mushroom |
| `sensor.cuisine_power_status` | `ui_dashboard/ui_dashboard.yaml` | Chips mushroom |
| `sensor.bureau_power_status` | `ui_dashboard/ui_dashboard.yaml` | Chips mushroom |
| `sensor.sdb_soufflant_power_status` | `ui_dashboard/ui_dashboard.yaml` | Chips mushroom |
| `sensor.sdb_seche_serviette_power_status` | `ui_dashboard/ui_dashboard.yaml` | Chips mushroom |
| `sensor.chambre_power_status` | `ui_dashboard/ui_dashboard.yaml` | Chips mushroom |
| `sensor.clim_salon_etat` | `ui_dashboard/ui_dashboard.yaml` | Chip Salon (contenu) |
| `sensor.radiateur_cuisine_etat` | `ui_dashboard/ui_dashboard.yaml` | Chip Cuisine (contenu) |
| `sensor.clim_bureau_etat` | `ui_dashboard/ui_dashboard.yaml` | Chip Bureau (contenu) |
| `sensor.sdb_soufflant_power_etat` | `ui_dashboard/ui_dashboard.yaml` | Chip SdB Soufflant |
| `sensor.sdb_seche_serviette_etat` | `ui_dashboard/ui_dashboard.yaml` | Chip SdB Serviette |
| `sensor.clim_chambre_etat` | `ui_dashboard/ui_dashboard.yaml` | Chip Chambre |
| `sensor.salon_power_lock` | `ui_dashboard/ui_dashboard.yaml` | Warning arrêt sécurisé salon |
| `sensor.bureau_power_lock` | `ui_dashboard/ui_dashboard.yaml` | Warning arrêt sécurisé bureau |
| `sensor.chambre_power_lock` | `ui_dashboard/ui_dashboard.yaml` | Warning arrêt sécurisé chambre |
| `sensor.conso_clim_rad_total` | `P1_TOTAL/P1_TOTAL_AMHQ.yaml` | bar-card total W |

### Templates Inter_BP_Virtuel

| Entité | Fichier | Rôle |
|--------|---------|------|
| `switch.inter_soufflant_salle_de_bain` | `Inter_BP_Virtuel/BI_02_switch_inter_sdb.yaml` | Visibilité button-card soufflant SdB |

### Natif HA — climate (SmartIR / Meross)

| Entité | Intégration | Section |
|--------|------------|---------|
| `climate.clim_salon_rm4_mini` | SmartIR | Salon |
| `climate.radiateur_cuisine` | Meross | Cuisine |
| `climate.clim_bureau_rm4_mini` | SmartIR | Bureau |
| `climate.soufflant_salle_de_bain` | Meross | SdB |
| `climate.clim_chambre_rm4_mini` | SmartIR | Chambre |

### Natif HA — power sensors (prises NOUS / Meross)

| Entité | Section |
|--------|---------|
| `sensor.clim_salon_nous_power` | Salon |
| `sensor.radiateur_elec_cuisine_power` | Cuisine |
| `sensor.clim_bureau_nous_power` | Bureau |
| `sensor.prise_soufflant_salle_de_bain_nous_power` | SdB |
| `sensor.clim_chambre_nous_power` | Chambre |

### Natif HA — switches / remotes

| Entité | Rôle |
|--------|------|
| `switch.clim_salon_nous` | Prise NOUS Salon |
| `switch.clim_bureau_nous` | Prise NOUS Bureau |
| `switch.clim_chambre_nous` | Prise NOUS Chambre |
| `switch.radiateur_elec_cuisine` | Switch Meross Cuisine |
| `switch.prise_soufflant_salle_de_bain_nous` | Prise NOUS SdB |
| `remote.clim_salon` | SmartIR remote Salon |
| `remote.clim_bureau` | SmartIR remote Bureau |
| `remote.clim_chambre` | SmartIR remote Chambre |
| `remote.soufflant_sdb` | SmartIR remote SdB |

### Natif HA — input_boolean / input_select

| Entité | Rôle | Fichier source |
|--------|------|----------------|
| `input_boolean.clim_salon_arret_securise_en_cours` | Verrou arrêt sécurisé Salon | `input_booleans/arret_clim_securises.yaml` |
| `input_boolean.clim_bureau_arret_securise_en_cours` | Verrou arrêt sécurisé Bureau | `input_booleans/arret_clim_securises.yaml` |
| `input_boolean.clim_chambre_arret_securise_en_cours` | Verrou arrêt sécurisé Chambre | `input_booleans/arret_clim_securises.yaml` |
| `input_select.etat_resistance_soufflant_sdb` | État résistance 0W/1000W/2000W | — |

### Natif HA — Schedules (HACS Scheduler)

> ⚠️ **À configurer** — Les `switch.schedule_*` sont créés par l'intégration **Scheduler** (HACS). Les plages horaires sont définies dans l'UI Scheduler, pas en YAML.

| Switch | Pièce | Fréquence |
|--------|-------|-----------|
| `switch.schedule_clim_du_salon_week` | Salon | Semaine |
| `switch.schedule_clim_du_salon_week_end` | Salon | Week-end |
| `switch.schedule_radiateur_cuisine_week` | Cuisine | Semaine |
| `switch.schedule_radiateur_cuisine_week_end` | Cuisine | Week-end |
| `switch.schedule_clim_du_bureau_week` | Bureau | Semaine |
| `switch.schedule_clim_du_bureau_week_end` | Bureau | Week-end |
| `switch.schedule_soufflant_salle_de_bain_week` | SdB | Semaine |
| `switch.schedule_soufflant_salle_de_bain_week_end` | SdB | Week-end |
| `switch.schedule_clim_de_la_chambre_week` | Chambre | Semaine |
| `switch.schedule_clim_de_la_chambre_week_end` | Chambre | Week-end |

### Scripts intelligents

> Les J-1 sont appelés depuis le dashboard. Chaque J-1 appelle J 2-0 (commun). Architecture 3+1 : un routeur par pièce + un exécuteur commun.

| Entité | Alias | Rôle | Mode |
|--------|-------|------|------|
| `script.j_1_1_salon_clim_on_off_intelligent` | J 1-1 SALON | **ROUTEUR SALON** — anti-tremblote + route ON/OFF | `single` |
| `script.j_1_2_bureau_clim_on_off_intelligent` | J 1-2 BUREAU | **ROUTEUR BUREAU** — anti-tremblote + route ON/OFF | `single` |
| `script.j_1_3_chambre_clim_on_off_intelligent` | J 1-3 CHAMBRE | **ROUTEUR CHAMBRE** — anti-tremblote + route ON/OFF | `single` |
| `script.j_2_0_secu_arret_clim_protege` | J 2-0 SECU | **EXÉCUTANT commun** — (1) active verrou → (2) coupe thermostat → (3) vérifie état → (4) attend descente sous 9W (timeout 10 min) → (5) coupe prise NOUS → (6) libère verrou | `parallel` (max 3) |

> **Pourquoi 3 routeurs ?** Chaque `mode: single` est isolé par pièce. Avec un routeur unique, arrêter salon bloquait silencieusement bureau pendant 10 min (J-1 attendait la fin de J-2).

**Fichier source** : `scripts.yaml` (racine) — voir aussi `docs Scripts/SCRIPTS_CLIM_ON_OFF.md`

---

## 🐛 DÉPANNAGE

### Les chips de bilan ne s'affichent pas
1. Vérifier que les templates `ui_dashboard.yaml` sont chargés : `Outils de développement → États → sensor.salon_power_status_affichage`
2. Tous les `_power_status_affichage` doivent être à `off` quand tous les appareils sont éteints → le bloc conditionnel est masqué. C'est normal.

### Le thermostat affiche "Unavailable"
- Pour les clims SmartIR (`climate.clim_*_rm4_mini`) : vérifier que le RM4 Mini est connecté au Wi-Fi et accessible
- Pour le radiateur cuisine (`climate.radiateur_cuisine`) : vérifier l'intégration Meross dans HA

### Les warnings rouge/amber ne s'affichent jamais
- Le warning ROUGE nécessite simultanément `input_boolean.clim_*_arret_securise_en_cours = on` ET `sensor.*_power_lock = on` — les deux conditions doivent être vraies
- Le warning AMBER nécessite `arret_securise = off` ET `switch.*_nous = off` ET `*_affichage = off` — les trois simultanément

### La bar-card bilan reste masquée
- `sensor.conso_clim_rad_total` doit retourner une valeur > 0.1W
- Source : `templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml`
- Vérifier que les sources NOUS power sont disponibles : `sensor.clim_salon_nous_power`, etc.

### Le button-card soufflant SdB n'apparaît pas
- `switch.inter_soufflant_salle_de_bain` doit être `on`
- Source : `templates/Inter_BP_Virtuel/BI_02_switch_inter_sdb.yaml`
- Vérifier que `input_boolean.inter_soufflant_salle_de_bain` est bien créé dans `input_boolean.yaml`

### Les schedules montrent "unavailable"
- L'intégration **Scheduler** (HACS) doit être installée et active
- Les `switch.schedule_*` sont créés depuis l'UI Scheduler — ils n'existent pas sans planification définie

---

## 📚 FICHIERS LIÉS

- Vignette : `docs/L1C3_CLIM/L1C3_VIGNETTE_CLIM.md`
- Templates P1 ui : `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml`
- Templates P1 total : `templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml`
- Templates P1 master : `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml`
- Templates Inter SdB : `templates/Inter_BP_Virtuel/BI_02_switch_inter_sdb.yaml`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L1C3_VIGNETTE_CLIM]]  [[L2C2_VIGNETTE_ENERGIE_CLIM]]*
