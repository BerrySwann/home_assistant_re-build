# PAGE — Énergie Clim / Radiateur / Soufflant
*Dernière mise à jour : 2026-03-24*
*Path : `/dashboard-tablette/energie-clim`*

---

## 📋 TABLE DES MATIÈRES

- [Architecture de la page](#architecture-de-la-page)
- [Détail des sections](#détail-des-sections)
  - [En-tête](#1-en-tête)
  - [Bloc bilan conditionnel](#2-bloc-bilan-conditionnel)
  - [Chips DUT (durées)](#3-chips-dut--durées-de-fonctionnement)
  - [Chips état (modes actifs)](#4-chips-état--modes-actifs)
  - [Bar-card total instantané](#5-bar-card-total-instantané)
  - [Donut journalier](#6-donut-journalier)
  - [Donut mensuel](#7-donut-mensuel)
  - [Section Tendances](#8-section-tendances)
  - [ApexCharts multi-yaxis](#9-apexcharts-multi-yaxis-24h)
  - [ApexCharts DUT global](#10-apexcharts-dut-global-5-pièces)
  - [Salon](#11-section-salon)
  - [Cuisine](#12-section-cuisine)
  - [Bureau](#13-section-bureau)
  - [SdB Soufflant](#14-section-sdb-soufflant)
  - [SdB Sèche-Serviettes](#15-section-sdb-sèche-serviettes)
  - [Chambre](#16-section-chambre)
  - [Pop-up #tendances](#17-pop-up-tendances)
- [Entités utilisées](#entités-utilisées--provenance-complète)
- [Streamline templates](#streamline-templates-utilisés)
- [Palette de couleurs](#palette-de-couleurs-p1)
- [Dépannage](#dépannage)

---

## Architecture de la page

```
/dashboard-tablette/energie-clim
│
├── [Heading] ENERGIE (C)LIM / (R)ADIATEUR  ← badge: Δ T° → popup #tendances
│
├── [Conditional] Bilan total
│   └── si au moins 1 clim active (*_power_status_affichage ≠ 'off')
│       └── text-divider "Consomation TOTAL Climatisations & Radiateurs"
│
├── [Horizontal-stack] Chips DUT × 4 (Salon / Cuisine / Bureau / Chambre)
│
├── [mushroom-chips-card] Chips état conditionnels × 6
│   └── affichés seulement si power_status ≠ 'off'
│
├── [auto-entities + bar-card] Puissance totale instantanée (sensor.conso_clim_rad_total)
│
├── [text-divider] Consomation Total Journalière
├── [apexcharts donut] kWh jour × 6 appareils
│
├── [text-divider] Consomation Total Mensuel
├── [apexcharts donut] kWh mois × 6 appareils
│
├── [text-divider] Tendance
├── [Heading] Tendances
├── [Horizontal-stack] Mini-graph T° Balcon Nord (24h)
├── [apexcharts multi-yaxis] T̄ Appart / T° Bal.Nrd / Conso W / Moy.Minuit / Total kWh
├── [apexcharts] D.U.T. Pièces vs Performance Totale (5 pièces + T° ext)
│
├── ── SECTION SALON ──────────────────────────────────────────
│   ├── [text-divider] SALON
│   ├── [heading] SALON  (badges: climate consigne + T° sensor)
│   ├── [bubble-card climate] climate.clim_salon_rm4_mini
│   ├── [streamline] clim_voltage_ring-tile  (sensor.clim_salon_nous_voltage)
│   ├── [streamline] clim_ampere_ring-tile   (sensor.clim_salon_nous_current)
│   ├── [tabbed-card] 3 onglets:
│   │   ├── INSTANTANÉ → streamline conso_temps_reel_clim_rad
│   │   ├── MENSUEL    → streamline conso_mensuelle_clim
│   │   └── PERF / DUT → apexcharts (DUT Salon + T° ext)
│   └── [heading subtitle] Badges Q / H / M / A kWh
│
├── ── SECTION CUISINE ─────────────────────────────────────────
│   ├── [text-divider] CUISINE
│   ├── [heading] CUISINE (RADIATEUR)  (badges: climate consigne + T° sensor)
│   ├── [bubble-card climate] climate.radiateur_cuisine
│   ├── [streamline] clim_voltage_ring-tile  (sensor.radiateur_elec_cuisine_voltage)
│   ├── [streamline] clim_ampere_ring-tile   (sensor.radiateur_elec_cuisine_current)
│   ├── [tabbed-card] 3 onglets
│   └── [heading subtitle] Badges Q / H / M / A kWh
│
├── ── SECTION BUREAU ──────────────────────────────────────────
│   ├── [text-divider] BUREAU
│   ├── [heading] BUREAU  (badges: climate consigne + T° sensor)
│   ├── [bubble-card climate] climate.clim_bureau_rm4_mini
│   ├── [streamline] clim_voltage_ring-tile  (sensor.clim_bureau_nous_voltage)
│   ├── [streamline] clim_ampere_ring-tile   (sensor.clim_bureau_nous_current)
│   ├── [tabbed-card] 3 onglets
│   └── [heading subtitle] Badges Q / H / M / A kWh
│
├── ── SECTION SALLE DE BAIN ───────────────────────────────────
│   ├── [text-divider] SALLE DE BAIN
│   ├── [heading] SALLE DE BAIN  (badges: climate soufflant + T° sdb)
│   ├── [stack-in-card] text-divider "Soufflant de la Salle de Bain"
│   ├── [bubble-card climate] climate.soufflant_salle_de_bain
│   ├── [streamline] clim_voltage_ring-tile  (sensor.prise_soufflant_salle_de_bain_nous_voltage)
│   ├── [streamline] clim_ampere_ring-tile   (sensor.prise_soufflant_salle_de_bain_nous_current)
│   ├── [tabbed-card] 3 onglets  (DUT: sensor.dut_sdb_total, color: magenta)
│   ├── [heading subtitle] Badges Q / H / M / A kWh (soufflant)
│   │
│   ├── [stack-in-card] text-divider "Sèche-Serviettes Salle de Bain"
│   ├── [streamline] clim_voltage_ring-tile  (sensor.prise_seche_serviette_salle_de_bain_nous_voltage)
│   ├── [streamline] clim_ampere_ring-tile   (sensor.prise_seche_serviette_salle_de_bain_nous_current)
│   ├── [tabbed-card] 3 onglets  (DUT: sensor.dut_sdb_total, color: rgb(218,112,214))
│   └── [heading subtitle] Badges Q / H / M / A kWh (sèche-serv)
│
├── ── SECTION CHAMBRE ─────────────────────────────────────────
│   ├── [text-divider] CHAMBRE
│   ├── [heading] CHAMBRE  (badges: climate consigne + T° sensor)
│   ├── [bubble-card climate] climate.clim_chambre_rm4_mini
│   ├── [streamline] clim_voltage_ring-tile  (sensor.clim_chambre_nous_voltage)
│   ├── [streamline] clim_ampere_ring-tile   (sensor.clim_chambre_nous_current)
│   ├── [tabbed-card] 3 onglets
│   └── [heading subtitle] Badges Q / H / M / A kWh
│
└── [Pop-up #tendances]
    ├── bubble-card pop-up  (hash: "#tendances", name: "CALCUL DU DELTA Intérieur <-> Extérieur")
    └── streamline calcule_temp_cible
```

---

## Détail des sections

### 1. En-tête

```yaml
type: heading
icon: mdi:transmission-tower
heading: ENERGIE (C)LIM / (R)ADIATEUR
heading_style: title
badges:
  - type: entity
    entity: sensor.temperature_delta_affichage
    tap_action:
      action: navigate
      navigation_path: "#tendances"
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/home   # ← retour Home
```

Le badge `sensor.temperature_delta_affichage` (Δ T° intérieur/extérieur) ouvre la pop-up `#tendances` au clic.

---

### 2. Bloc bilan conditionnel

Affiché **uniquement si au moins une clim/chauffage est active**. Vérifie 6 entités `*_power_status_affichage` :

| Entité | Pièce |
|--------|-------|
| `sensor.salon_power_status_affichage` | Salon |
| `sensor.cuisine_power_status_affichage` | Cuisine |
| `sensor.bureau_power_status_affichage` | Bureau |
| `sensor.sdb_power_status_affichage` | SdB Soufflant |
| `sensor.sdb_seche_serviettes_power_status_affichage` | SdB Sèche-Serv |
| `sensor.chambre_power_status_affichage` | Chambre |

Si `state_not: "off"` pour au moins une → affiche `text-divider "Consomation TOTAL Climatisations & Radiateurs"`.

**Source :** `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml`

---

### 3. Chips DUT — Durées de fonctionnement

4 chips `mushroom-chips-card` en ligne horizontale, format `Xh MM` :

```jinja
Salon: {% set t = states(entity) | float(0) %}
{% set h = t | int %}{% set m = ((t - h) * 60) | int %}
{{ h }}h{{ '{:02d}'.format(m) }}
```

| Chip | Entité | Icône dynamique |
|------|--------|-----------------|
| Salon | `sensor.dut_clim_salon` | `mdi:snowflake` (Été) / `mdi:fire` (Hiver) |
| Cuisine | `sensor.dut_radiateur_cuisine` | `mdi:radiator` (fixe, rouge) |
| Bureau | `sensor.dut_clim_bureau` | `mdi:snowflake` / `mdi:fire` |
| Chambre | `sensor.dut_clim_chambre` | `mdi:snowflake` / `mdi:fire` |

Icône/couleur conditionnelle sur `sensor.ete_hiver` : Été = `#03a9f4`, Hiver = `#ff9800`.

> Note : La SdB n'a **pas** de chip DUT dédié ici (le DUT SdB est visible dans la section dédiée).

---

### 4. Chips état — Modes actifs

6 chips `conditional` affichés seulement si la prise correspondante est ON :

| Condition | Chip | Icône | Couleurs modes |
|-----------|------|-------|----------------|
| `sensor.salon_power_status ≠ off` | Salon: Cool/Heat/Fan/Off | `mdi:air-conditioner` | Cool=#87CEEB / Heat=#ff6100 / Fan=#40E0D0 / Off=#FF0000 |
| `sensor.cuisine_power_status ≠ off` | Cuisine: Heat/Off | `mdi:heating-coil` | Heat=#ff6100 / Off=#FF0000 |
| `sensor.bureau_power_status ≠ off` | Bureau: Cool/Heat/Fan/Off | `mdi:air-conditioner` | idem Salon |
| `sensor.sdb_soufflant_power_status ≠ off` | SdB: Heat/Off | `mdi:heat-wave` | Heat=#ff6100 / Off=#FF0000 |
| `sensor.sdb_seche_serviette_power_status ≠ off` | SdB SèS: Heat/Off | `mdi:heating-coil` | Heat=#ff6100 / Off=#FF0000 |
| `sensor.chambre_power_status ≠ off` | Chambre: Cool/Heat/Fan/Off | `mdi:air-conditioner` | idem Salon |

Content affiche le mode actif via `sensor.clim_*_etat` / `sensor.radiateur_cuisine_etat` / `sensor.soufflant_sdb_etat` / `sensor.sdb_seche_serviette_etat`.

---

### 5. Bar-card total instantané

`custom:auto-entities` + `custom:bar-card` sur `sensor.conso_clim_rad_total` (W) :

| Seuil (W) | Couleur |
|-----------|---------|
| 0 – 5 | gainsboro |
| 5 – 49 | rgb(102,255,102) |
| 50 – 249 | rgb(0,102,0) |
| 250 – 499 | orange |
| 500 – 749 | darkorange |
| 750 – 999 | red |
| 1000 – 6000 | darkred |

Visibilité : affiché uniquement si `sensor.conso_clim_rad_total > 0.1`.

---

### 6. Donut journalier

`custom:apexcharts-card`, `chart_type: donut`, `span.start: day`

6 séries × couleur pièce :

| Série | Entité | Couleur |
|-------|--------|---------|
| SALON (C) | `sensor.clim_salon_quotidien_kwh_um` | `rgb(174,68,90)` |
| CUISINE (R) | `sensor.radiateur_elec_cuisine_quotidien_kwh_um` | `rgb(168,136,181)` |
| BUREAU (C) | `sensor.clim_bureau_quotidien_kwh_um` | `orange` |
| Souff. SdB (R) | `sensor.soufflant_sdb_quotidien_kwh_um` | `magenta` |
| Sèche-Serv. SdB (R) | `sensor.seche_serviette_sdb_quotidien_kwh_um` | `purple` |
| CHAMBRE (C) | `sensor.clim_chambre_quotidien_kwh_um` | `rgb(30,81,40)` |

---

### 7. Donut mensuel

`custom:apexcharts-card`, `chart_type: donut`, `span.start: month`

Même 6 séries que le journalier, mais avec les entités `*_mensuel_kwh_um` :

| Série | Entité | Couleur |
|-------|--------|---------|
| SALON (C) | `sensor.clim_salon_mensuel_kwh_um` | `rgb(174,68,90)` |
| CUISINE (R) | `sensor.radiateur_elec_cuisine_mensuel_kwh_um` | `rgb(168,136,181)` |
| BUREAU (C) | `sensor.clim_bureau_mensuel_kwh_um` | `orange` |
| Souff. SdB (R) | `sensor.soufflant_sdb_mensuel_kwh_um` | `magenta` |
| Sèche-Serv. SdB (R) | `sensor.seche_serviette_sdb_mensuel_kwh_um` | `purple` |
| CHAMBRE (C) | `sensor.clim_chambre_mensuel_kwh_um` | `rgb(30,81,40)` |

---

### 8. Section Tendances

- **Mini-graph** `custom:vertical-stack-in-card` contenant :
  - `mushroom-template-card` sur `sensor.th_balcon_nord_temperature` avec icône directionnelle (`increasing` → flèche montante rouge / `decreasing` → flèche descendante bleue / stable → flèche droite)
  - `mini-graph-card` : 24h, 6 points/heure, couleur `#df6366`, hauteur 200px

---

### 9. ApexCharts multi-yaxis 24h

**Titre :** affiché vide (`" "`) — les valeurs sont dans `show_states`

**Axes Y :**
- `temperature` (gauche) : min ~5, max ~32, 10 ticks
- `conso_clim` (droite) : min ~150, max auto, 10 ticks

**6 séries :**

| Série | Entité | Yaxis | Type | Couleur |
|-------|--------|-------|------|---------|
| T̄ Appart. | `sensor.temperature_moyenne_interieure` | temperature | line | orange |
| T° Bal.Nrd | `sensor.th_balcon_nord_temperature` | temperature | line | green |
| Conso. Instan. | `sensor.conso_clim_rad_total` | conso_clim | column | rgb(68,115,158) |
| Conso. Total (header only) | `sensor.conso_clim_rad_total_quotidien` | – | hidden | rgb(68,115,158) |
| Moy.depuis Minuit | `sensor.clim_rad_total_avg_watts_daily` | conso_clim | line | #F44336 |
| Mois en cours (header only) | `sensor.conso_clim_rad_total_mensuel` | – | hidden | red |

Les 2 séries `in_chart: false` servent uniquement à afficher leur valeur dans le header (`show_states: true`).

---

### 10. ApexCharts DUT global (5 pièces)

**Titre :** `D.U.T. Pièces vs Performance Totale`
**Span :** 24h depuis début du jour

**Axes Y :**
- `temp` (gauche) : T° extérieure (fond area bleu-gris, opacity 0.2)
- `hours` (droite) : 0–6h par défaut, 12 ticks
- `perf` : masqué

**6 séries :**

| Série | Entité | Couleur |
|-------|--------|---------|
| Temp. Ext. (fond) | `sensor.th_balcon_nord_temperature` | `#44739e` (area 0.2) |
| Salon | `sensor.dut_clim_salon` | `rgb(174,68,90)` |
| Cuisine | `sensor.dut_radiateur_cuisine` | `rgb(168,136,181)` |
| Bureau | `sensor.dut_clim_bureau` | `orange` |
| SdB | `sensor.dut_sdb_total` | `magenta` |
| Chambre | `sensor.dut_clim_chambre` | `rgb(30,81,40)` |

---

### 11. Section SALON

**Heading** : icon `mdi:sofa`, badges :
- `climate.clim_salon_rm4_mini` → state_content: name + temperature (consigne)
- `sensor.th_salon_temperature` → T° mesurée (couleur green)

**Bubble-card climate** : `climate.clim_salon_rm4_mini`, 2 sub_buttons : HVAC modes + fan modes

**Ring-tiles streamline** :
- Voltage : `sensor.clim_salon_nous_voltage`
- Ampère : `sensor.clim_salon_nous_current`

**Tabbed-card** (couleur accent `rgb(174,68,90)`) :
- `INSTANTANÉ` → `conso_temps_reel_clim_rad` : energy=`sensor.clim_salon_nous_power` (rgb(174,68,90)), avg=`sensor.clim_salon_avg_watts_quotidien`, kwh=`sensor.clim_salon_quotidien_kwh_um`
- `MENSUEL` → `conso_mensuelle_clim` : energy=`sensor.clim_salon_nous_energy`, avg_monthly=`sensor.clim_salon_avg_watts_mensuel`, kwh_monthly=`sensor.clim_salon_mensuel_kwh_um`
- `PERF / DUT` → apexcharts DUT Salon (`sensor.dut_clim_salon`) + T° ext, color_threshold: 0→vert / 4→jaune / 6→orange / 10→rouge, annotation zone critique [5–50h]

**Heading subtitle kWh** :
- Q : `sensor.clim_salon_quotidien_kwh_um` (amber)
- H : `sensor.clim_salon_hebdomadaire_kwh_um` (orange)
- M : `sensor.clim_salon_mensuel_kwh_um` (deep-orange)
- A : `sensor.clim_salon_annuel_kwh_um` (red)

---

### 12. Section CUISINE

**Heading** : icon `mdi:fridge`, heading `CUISINE (RADIATEUR)`, badges :
- `climate.radiateur_cuisine` (consigne)
- `sensor.th_cuisine_temperature`

**Bubble-card climate** : `climate.radiateur_cuisine`, 1 sub_button HVAC modes

**Ring-tiles streamline** :
- Voltage : `sensor.radiateur_elec_cuisine_voltage`
- Ampère : `sensor.radiateur_elec_cuisine_current`

**Tabbed-card** :
- `INSTANTANÉ` → energy=`sensor.radiateur_elec_cuisine_power` (rgb(168,136,181)), avg=`sensor.radiateur_elec_cuisine_avg_watts_quotidien`, kwh=`sensor.radiateur_elec_cuisine_quotidien_kwh_um`
- `MENSUEL` → energy=`sensor.radiateur_elec_cuisine_energy`, avg_monthly=`sensor.radiateur_elec_cuisine_avg_watts_mensuel`, kwh_monthly=`sensor.radiateur_elec_cuisine_mensuel_kwh_um`
- `PERF / DUT` → `sensor.dut_radiateur_cuisine` (rgb(168,136,181)), annotation "Performance Faible"

**Heading subtitle kWh** :
- Q/H/M/A : `sensor.radiateur_elec_cuisine_*_kwh_um`

---

### 13. Section BUREAU

**Heading** : icon `mdi:desktop-tower-monitor`, badges :
- `climate.clim_bureau_rm4_mini` (consigne)
- `sensor.th_bureau_temperature`

**Bubble-card climate** : `climate.clim_bureau_rm4_mini`, 2 sub_buttons : HVAC + fan modes

**Ring-tiles streamline** :
- Voltage : `sensor.clim_bureau_nous_voltage`
- Ampère : `sensor.clim_bureau_nous_current`

**Tabbed-card** :
- `INSTANTANÉ` → energy=`sensor.clim_bureau_nous_power` (orange), avg=`sensor.clim_bureau_avg_watts_quotidien`, kwh=`sensor.clim_bureau_quotidien_kwh_um`
- `MENSUEL` → energy=`sensor.clim_bureau_nous_energy`, avg_monthly=`sensor.clim_bureau_avg_watts_mensuel`, kwh_monthly=`sensor.clim_bureau_mensuel_kwh_um`
- `PERF / DUT` → `sensor.dut_clim_bureau` (orange), annotation "Zone Critique"

**Heading subtitle kWh** :
- Q/H/M/A : `sensor.clim_bureau_*_kwh_um`

---

### 14. Section SdB Soufflant

**Heading** : icon `hue:room-bathroom`, heading `SALLE DE BAIN`, badges :
- `climate.soufflant_salle_de_bain` (consigne)
- `sensor.th_salle_de_bain_temperature`

**Sub-section Soufflant** (`text-divider "Soufflant de la Salle de Bain"`) :

**Bubble-card climate** : `climate.soufflant_salle_de_bain`, min_temp: 21, max_temp: 23, step: 1

**Ring-tiles streamline** :
- Voltage : `sensor.prise_soufflant_salle_de_bain_nous_voltage`
- Ampère : `sensor.prise_soufflant_salle_de_bain_nous_current`

**Tabbed-card** :
- `INSTANTANÉ` → energy=`sensor.prise_soufflant_salle_de_bain_nous_power` (magenta), avg=`sensor.soufflant_sdb_avg_watts_quotidien`, kwh=`sensor.soufflant_sdb_quotidien_kwh_um`
- `MENSUEL` → energy=`sensor.prise_soufflant_salle_de_bain_nous_energy` (magenta), avg_monthly=`sensor.soufflant_sdb_avg_watts_mensuel`
- `PERF / DUT` → `sensor.dut_sdb_total` (rgb(218,112,214)), annotation "Pic de conso", dashArray pour distinguer les tracés

**Heading subtitle kWh** :
- Q/H/M/A : `sensor.soufflant_sdb_*_kwh_um`

---

### 15. Section SdB Sèche-Serviettes

**Sub-section** (`text-divider "Sèche-Serviettes Salle de Bain"`) — pas de bubble-card climate, pas de heading dédié.

**Ring-tiles streamline** :
- Voltage : `sensor.prise_seche_serviette_salle_de_bain_nous_voltage`
- Ampère : `sensor.prise_seche_serviette_salle_de_bain_nous_current`

**Tabbed-card** :
- `INSTANTANÉ` → energy=`sensor.prise_seche_serviette_salle_de_bain_nous_power` (rgb(218,112,214)), avg=`sensor.seche_serviette_sdb_avg_watts_quotidien`, kwh=`sensor.seche_serviette_sdb_quotidien_kwh_um`, power_entity=`sensor.prise_radiateur_salle_de_bain_inspelning_ikea_power` (rgb(255,215,0) — IKEA Inspelning)
- `MENSUEL` → energy=`sensor.prise_seche_serviette_salle_de_bain_nous_energy` (rgb(218,112,214)), avg_monthly=`sensor.seche_serviette_sdb_avg_watts_mensuel`
- `PERF / DUT` → `sensor.dut_sdb_total` (rgb(218,112,214)), annotation "Pic de conso"

**Heading subtitle kWh** :
- Q/H/M/A : `sensor.seche_serviette_sdb_*_kwh_um`

---

### 16. Section CHAMBRE

**Heading** : icon `mdi:bed`, badges :
- `climate.clim_chambre_rm4_mini` (consigne)
- `sensor.th_chambre_temperature`

**Bubble-card climate** : `climate.clim_chambre_rm4_mini`, 2 sub_buttons : HVAC + fan modes

**Ring-tiles streamline** :
- Voltage : `sensor.clim_chambre_nous_voltage`
- Ampère : `sensor.clim_chambre_nous_current`

**Tabbed-card** :
- `INSTANTANÉ` → energy=`sensor.clim_chambre_nous_power` (rgb(30,81,40)), avg=`sensor.clim_chambre_avg_watts_quotidien`, kwh=`sensor.clim_chambre_quotidien_kwh_um`
- `MENSUEL` → energy=`sensor.clim_chambre_nous_energy`, avg_monthly=`sensor.clim_chambre_avg_watts_mensuel`, kwh_monthly=`sensor.clim_chambre_mensuel_kwh_um`
- `PERF / DUT` → `sensor.dut_clim_chambre` (rgb(30,81,40)), annotation "Zone de déperdition" (opacity 0.7 — chambre = forte déperdition thermique attendue)

**Heading subtitle kWh** :
- Q/H/M/A : `sensor.clim_chambre_*_kwh_um`

---

### 17. Pop-up #tendances

```yaml
type: vertical-stack
cards:
  - type: custom:bubble-card
    card_type: pop-up
    hash: "#tendances"
    name: CALCUL DU DELTA Intérieur <-> Extérieur
    icon: mdi:delta
  - type: custom:streamline-card
    template: calcule_temp_cible
```

Affiche le calcul du delta entre T° intérieure moyenne et T° extérieure, avec la T° cible confort calculée par la logique ADEME.

---

## Entités utilisées — Provenance complète

### Catégorie A — Climate (thermostats natifs)

| Entité | Source |
|--------|--------|
| `climate.clim_salon_rm4_mini` | SmartIR |
| `climate.radiateur_cuisine` | Meross |
| `climate.clim_bureau_rm4_mini` | SmartIR |
| `climate.soufflant_salle_de_bain` | Meross |
| `climate.clim_chambre_rm4_mini` | SmartIR |

### Catégorie B — Utility Meters kWh (P1_UM_AMHQ)

**Source :** `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml`

| Entité | Période |
|--------|---------|
| `sensor.clim_salon_quotidien_kwh_um` | Quotidien |
| `sensor.clim_salon_hebdomadaire_kwh_um` | Hebdomadaire |
| `sensor.clim_salon_mensuel_kwh_um` | Mensuel |
| `sensor.clim_salon_annuel_kwh_um` | Annuel |
| `sensor.radiateur_elec_cuisine_quotidien_kwh_um` | Quotidien |
| `sensor.radiateur_elec_cuisine_hebdomadaire_kwh_um` | Hebdomadaire |
| `sensor.radiateur_elec_cuisine_mensuel_kwh_um` | Mensuel |
| `sensor.radiateur_elec_cuisine_annuel_kwh_um` | Annuel |
| `sensor.clim_bureau_quotidien_kwh_um` | Quotidien |
| `sensor.clim_bureau_hebdomadaire_kwh_um` | Hebdomadaire |
| `sensor.clim_bureau_mensuel_kwh_um` | Mensuel |
| `sensor.clim_bureau_annuel_kwh_um` | Annuel |
| `sensor.soufflant_sdb_quotidien_kwh_um` | Quotidien |
| `sensor.soufflant_sdb_hebdomadaire_kwh_um` | Hebdomadaire |
| `sensor.soufflant_sdb_mensuel_kwh_um` | Mensuel |
| `sensor.soufflant_sdb_annuel_kwh_um` | Annuel |
| `sensor.seche_serviette_sdb_quotidien_kwh_um` | Quotidien |
| `sensor.seche_serviette_sdb_mensuel_kwh_um` | Mensuel |
| `sensor.clim_chambre_quotidien_kwh_um` | Quotidien |
| `sensor.clim_chambre_hebdomadaire_kwh_um` | Hebdomadaire |
| `sensor.clim_chambre_mensuel_kwh_um` | Mensuel |
| `sensor.clim_chambre_annuel_kwh_um` | Annuel |

### Catégorie C — Templates P1 TOTAL (agrégats)

**Source :** `templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml`

| Entité | Description |
|--------|-------------|
| `sensor.conso_clim_rad_total` | Puissance instantanée totale (W) |
| `sensor.conso_clim_rad_total_quotidien` | kWh jour (somme des 6) |
| `sensor.conso_clim_rad_total_mensuel` | kWh mois (somme des 6) |

### Catégorie D — Templates P1 ui_dashboard

**Source :** `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml`

| Entité | Description |
|--------|-------------|
| `sensor.salon_power_status` | ON/OFF Salon |
| `sensor.cuisine_power_status` | ON/OFF Cuisine |
| `sensor.bureau_power_status` | ON/OFF Bureau |
| `sensor.sdb_soufflant_power_status` | ON/OFF SdB Soufflant |
| `sensor.sdb_seche_serviette_power_status` | ON/OFF SdB Sèche-Serv |
| `sensor.chambre_power_status` | ON/OFF Chambre |
| `sensor.salon_power_status_affichage` | État affichage Salon (pour conditional) |
| `sensor.cuisine_power_status_affichage` | État affichage Cuisine |
| `sensor.bureau_power_status_affichage` | État affichage Bureau |
| `sensor.sdb_power_status_affichage` | État affichage SdB Soufflant |
| `sensor.sdb_seche_serviettes_power_status_affichage` | État affichage SdB SèS |
| `sensor.chambre_power_status_affichage` | État affichage Chambre |
| `sensor.clim_salon_etat` | Mode Salon (Cool/Heat/Fan/Off) |
| `sensor.radiateur_cuisine_etat` | Mode Cuisine (Heat/Off) |
| `sensor.clim_bureau_etat` | Mode Bureau |
| `sensor.soufflant_sdb_etat` | Mode Soufflant SdB |
| `sensor.sdb_seche_serviette_etat` | Mode Sèche-Serv SdB |
| `sensor.clim_chambre_etat` | Mode Chambre |

### Catégorie E — Sensors natifs puissance (W) — prises NOUS/Meross

| Entité | Appareil |
|--------|----------|
| `sensor.clim_salon_nous_power` | Clim Salon |
| `sensor.clim_salon_nous_voltage` | Clim Salon (V) |
| `sensor.clim_salon_nous_current` | Clim Salon (A) |
| `sensor.clim_salon_nous_energy` | Clim Salon (kWh natif) |
| `sensor.radiateur_elec_cuisine_power` | Radiateur Cuisine |
| `sensor.radiateur_elec_cuisine_voltage` | Radiateur Cuisine (V) |
| `sensor.radiateur_elec_cuisine_current` | Radiateur Cuisine (A) |
| `sensor.radiateur_elec_cuisine_energy` | Radiateur Cuisine (kWh natif) |
| `sensor.clim_bureau_nous_power` | Clim Bureau |
| `sensor.clim_bureau_nous_voltage` | Clim Bureau (V) |
| `sensor.clim_bureau_nous_current` | Clim Bureau (A) |
| `sensor.clim_bureau_nous_energy` | Clim Bureau (kWh natif) |
| `sensor.prise_soufflant_salle_de_bain_nous_power` | Soufflant SdB |
| `sensor.prise_soufflant_salle_de_bain_nous_voltage` | Soufflant SdB (V) |
| `sensor.prise_soufflant_salle_de_bain_nous_current` | Soufflant SdB (A) |
| `sensor.prise_soufflant_salle_de_bain_nous_energy` | Soufflant SdB (kWh natif) |
| `sensor.prise_seche_serviette_salle_de_bain_nous_power` | Sèche-Serv SdB |
| `sensor.prise_seche_serviette_salle_de_bain_nous_voltage` | Sèche-Serv SdB (V) |
| `sensor.prise_seche_serviette_salle_de_bain_nous_current` | Sèche-Serv SdB (A) |
| `sensor.prise_seche_serviette_salle_de_bain_nous_energy` | Sèche-Serv SdB (kWh natif) |
| `sensor.prise_radiateur_salle_de_bain_inspelning_ikea_power` | IKEA Inspelning SdB (W) |
| `sensor.clim_chambre_nous_power` | Clim Chambre |
| `sensor.clim_chambre_nous_voltage` | Clim Chambre (V) |
| `sensor.clim_chambre_nous_current` | Clim Chambre (A) |
| `sensor.clim_chambre_nous_energy` | Clim Chambre (kWh natif) |

### Catégorie F — Templates P1 AVG (moyennes)

**Source :** `templates/P1_clim_chauffage/P1_AVG/P1_avg.yaml`

| Entité | Description |
|--------|-------------|
| `sensor.clim_salon_avg_watts_quotidien` | Moy. W depuis minuit (Salon) |
| `sensor.clim_salon_avg_watts_mensuel` | Moy. W depuis 1er du mois (Salon) |
| `sensor.clim_rad_total_avg_watts_daily` | Moy. W total depuis minuit |
| `sensor.radiateur_elec_cuisine_avg_watts_quotidien` | Moy. W depuis minuit (Cuisine) |
| `sensor.radiateur_elec_cuisine_avg_watts_mensuel` | Moy. W depuis 1er du mois (Cuisine) |
| `sensor.clim_bureau_avg_watts_quotidien` | Moy. W depuis minuit (Bureau) |
| `sensor.clim_bureau_avg_watts_mensuel` | Moy. W depuis 1er du mois (Bureau) |
| `sensor.soufflant_sdb_avg_watts_quotidien` | Moy. W depuis minuit (SdB Sft) |
| `sensor.soufflant_sdb_avg_watts_mensuel` | Moy. W depuis 1er du mois (SdB Sft) |
| `sensor.seche_serviette_sdb_avg_watts_quotidien` | Moy. W depuis minuit (SdB SèS) |
| `sensor.seche_serviette_sdb_avg_watts_mensuel` | Moy. W depuis 1er du mois (SdB SèS) |
| `sensor.clim_chambre_avg_watts_quotidien` | Moy. W depuis minuit (Chambre) |
| `sensor.clim_chambre_avg_watts_mensuel` | Moy. W depuis 1er du mois (Chambre) |

### Catégorie G — DUT (Durée d'Utilisation Totale)

**Source :** `sensors/P1_clim_chauffage/P1_DUT_clim_chauffage.yaml`

| Entité | Description |
|--------|-------------|
| `sensor.dut_clim_salon` | Heures de fonctionnement Salon (aujourd'hui) |
| `sensor.dut_radiateur_cuisine` | Heures de fonctionnement Cuisine (aujourd'hui) |
| `sensor.dut_clim_bureau` | Heures de fonctionnement Bureau (aujourd'hui) |
| `sensor.dut_sdb_total` | Heures de fonctionnement SdB total (soufflant + sèche-serv) |
| `sensor.dut_clim_chambre` | Heures de fonctionnement Chambre (aujourd'hui) |

### Catégorie H — Températures intérieures + logique système

| Entité | Description |
|--------|-------------|
| `sensor.th_salon_temperature` | T° Salon |
| `sensor.th_cuisine_temperature` | T° Cuisine |
| `sensor.th_bureau_temperature` | T° Bureau |
| `sensor.th_salle_de_bain_temperature` | T° SdB |
| `sensor.th_chambre_temperature` | T° Chambre |
| `sensor.th_balcon_nord_temperature` | T° Extérieure |
| `sensor.th_balcon_nord_temperature_trend` | Tendance T° (increasing/decreasing/flat) |
| `sensor.temperature_moyenne_interieure` | T° moyenne intérieure |
| `sensor.temperature_delta_affichage` | Δ T° intérieur/extérieur (badge en-tête) |
| `sensor.ete_hiver` | Saison (Été / Hiver) — pour icônes DUT chips |

---

## Streamline templates utilisés

| Template | Utilisation | Variables clés |
|----------|-------------|----------------|
| `conso_temps_reel_clim_rad` | Onglet INSTANTANÉ × 5 pièces | `card_title`, `energy_entity`, `energy_color`, `current_entity`, `avg_daily_entity`, `conso_daily_kwh_entity`, `span_offset`, `group_duration` |
| `conso_mensuelle_clim` | Onglet MENSUEL × 5 pièces | `title`, `energy_entity`, `energy_name`, `energy_color`, `avg_monthly_entity`, `temp_entity`, `conso_monthly_kwh_entity` |
| `clim_voltage_ring-tile` | Voltage (V) × 5 pièces | `card_name`, `entity` |
| `clim_ampere_ring-tile` | Ampère (A) × 5 pièces | `card_name`, `entity` |
| `calcule_temp_cible` | Pop-up #tendances | _(aucune variable)_ |

---

## Palette de couleurs P1

| Pièce/Équipement | Couleur | Code |
|-----------------|---------|------|
| Salon | Rose foncé | `rgb(174,68,90)` |
| Cuisine | Mauve clair | `rgb(168,136,181)` |
| Bureau | Orange | `orange` |
| SdB Soufflant | Magenta | `magenta` / `rgb(218,112,214)` |
| SdB Sèche-Serv | Orchidée | `rgb(218,112,214)` / `purple` |
| Chambre | Vert foncé | `rgb(30,81,40)` |
| Température ext. | Bleu-gris | `#44739e` |
| Moy. depuis minuit | Rouge | `#F44336` |

---

## Dépannage

**Donuts vides / à 0 :**
Les UM `*_kwh_um` mettent un peu de temps à s'alimenter au démarrage. Si vide plus longtemps, vérifier que `P1_UM_AMHQ.yaml` référence bien les bons sensors sources (intégration Riemann dans `P1_DUT_clim_chauffage.yaml`).

**DUT chips bloqués à 0h00 :**
Les `sensor.dut_*` viennent de `platform: history_stats`. Vérifier que les entités source (`climate.*`, `switch.*`) sont bien suivies dans l'historique MariaDB.

**Ring-tiles V/A : `unavailable` :**
Les prises NOUS doivent être connectées (Wi-Fi). Si offline, `sensor.*_nous_voltage/current` restent en `unavailable`.

**Tabbed-card onglet PERF/DUT vide :**
`sensor.dut_sdb_total` pour la SdB cumule soufflant + sèche-serviettes. Si les deux sont éteints toute la journée, le graphique reste vide (c'est normal).

**Pop-up #tendances ne s'ouvre pas :**
Le hash `#tendances` doit être déclaré dans la page. Vérifier que la `bubble-card pop-up` avec `hash: "#tendances"` est bien présente dans la page.

---

## Fichiers liés

| Fichier | Rôle |
|---------|------|
| `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml` | Compteurs UM Q/H/M/A (6 appareils) |
| `templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml` | Totaux agrégés |
| `templates/P1_clim_chauffage/P1_AVG/P1_avg.yaml` | Moyennes W (quotidien/mensuel) |
| `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | power_status + etat + affichage |
| `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | Logique T° cible + delta ADEME |
| `sensors/P1_clim_chauffage/P1_DUT_clim_chauffage.yaml` | DUT history_stats + intégration kWh |
