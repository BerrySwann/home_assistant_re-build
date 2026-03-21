# 🔗 DÉPENDANCES GLOBALES — TOUTES LES VIGNETTES
*Dernière mise à jour : 2026-03-21 (session 5 — s11)*

> **RÈGLE :** Ce fichier est mis à jour obligatoirement à chaque création ou modification d'une doc de vignette (`docs/L*`).
> Format : Vignette → Carte → Template/Sensor → Utility Meter → Source native HA

---

## 📖 LÉGENDE

| Symbole | Signification |
|---------|---------------|
| ✅ | Doc vignette existante dans `docs/` |
| 🔲 | Doc vignette à créer |
| `→` | Dépend de |
| `[UM]` | Utility Meter |
| `[TPL]` | Template |
| `[SNS]` | Sensor (intégration kWh) |
| `[NAT]` | Entité native HA (intégration UI) |

---

## LIGNE 1 — ENVIRONNEMENT & THERMIQUE

### ✅ L1C1 — Météo
`docs/L1C1_METEO/`

```
L1C1 Météo
  ├── Alertes vigilance
  │     └── [TPL] M_01_meteo_alertes_card.yaml
  │           └── camera.mf_alerte_today / _tomorrow  [NAT camera.yaml]
  │                 └── command_line/meteo/carte_meteo_france.yaml
  │                       └── API Météo France (wget)
  ├── Vent / Windrose
  │     └── [TPL] M_02_meteo_vent_vence_card.yaml
  │           └── [NAT] sensor.openweathermap_wind_* / wind_bearing
  ├── Foudre Blitzortung
  │     └── [TPL] M_03_meteo_templates_blitzortung.yaml
  │           └── [SNS] sensors/meteo/M_03_meteo_sensors_blitzortung.yaml
  │                 └── [UM] utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml
  │                       └── [NAT] intégration Blitzortung (HACS)
  └── Tendances T° ext
        └── [TPL] M_04_tendances_th_ext_card.yaml
              └── [NAT] sensor.th_ext_temperature (SONOFF SNZB-02 balcon)
```

---

### ✅ L1C2 — Températures
`docs/L1C2_TEMPERATURES/`

```
L1C2 Températures
  ├── T° + Humidité (6 pièces + extérieur)
  │     └── [NAT] sensor.th_*_temperature / *_humidity (SONOFF SNZB-02 x7)
  └── Cycle solaire (lever/coucher)
        └── [TPL] templates/meteo/M_05_cycle_solaire.yaml
              └── [NAT] sun.sun
```

---

### 🔲 L1C3 — Commandes Clim

```
L1C3 Commandes Clim
  ├── Clim Salon / Bureau / Chambre
  │     └── [NAT] climate.clim_*_rm4_mini (SmartIR — configuration.yaml)
  ├── Radiateur Cuisine
  │     └── [NAT] switch.radiateur_cuisine (Meross)
  ├── Soufflant SDB
  │     └── [NAT] switch.soufflant_sdb (Sonoff)
  └── Logique système clim
        └── [TPL] P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml
```

---

## LIGNE 2 — CONSOMMATION ÉNERGÉTIQUE

### ✅ L2C1 — Énergie Générale
`docs/L2C1_ENERGIE/`

```
L2C1 Énergie Générale
  ├── Vignette (ring-tile Mini/Réel/Maxi + badges coût J/M/A)
  │     ├── [NAT] sensor.ecojoko_conso_mini_24h / ecojoko_conso_maxi_24h (Ecojoko natif)
  │     ├── [NAT] sensor.ecojoko_puissance_apparente_w (live W)
  │     ├── [TPL] P0_Energie_total_diag/Ecojoko/01_ecojoko_AMHQ_cost.yaml
  │     │     └── [UM] P0_Energie_total/Ecojoko/01_UM_AMHQ_cost.yaml
  │     │           └── [NAT] sensor.ecojoko_hp/hc_reseau_* (Ecojoko HACS)
  │     └── [TPL] P0_Energie_total_diag/Ecojoko/03_AVG_ecojoko.yaml
  ├── Page principale /energie (tabbed-card 3 onglets JOURNALIER/HEBDO/MENSUEL)
  │     ├── Coûts HP/HC (quotidien, hebdo, mensuel, annuel)
  │     │     └── [TPL] 01_ecojoko_AMHQ_cost.yaml → [UM] 01_UM_AMHQ_cost.yaml
  │     ├── Ratio HC/HP
  │     │     └── [TPL] 02_ratio_hp_hc.yaml
  │     ├── Diag conso (jour / semaine / mois)
  │     │     └── [TPL] Diag/diag_conso_*.yaml (x3)
  │     │           └── sensor.diag_poste_*_quotidien / hebdomadaire / mensuel
  │     │           └── sensor.diag_max_poste_quotidien_dynamique / hebdo / mensuel
  │     ├── Entités HEBDO : sensor.ecojoko_reseau_hebdomadaire_um
  │     │     sensor.ecojoko_hp/hc_reseau_hebdomadaire_um
  │     │     sensor.ecojoko_cout_total/hp/hc_hebdomadaire
  │     │     sensor.ecojoko_ratio_hc_hebdomadaire
  │     └── Linky MyElectricalData
  │           └── [TPL] P0_Energie_total_diag/Linky/MyElectricalData.yaml
  │                 └── [NAT] intégration MyElectricalData (HACS)
  ├── Page temps réel /energie-temps-reel (4 colonnes)
  │     ├── Col 1 : 7 sections conditionnelles par catégorie
  │     │     └── [NAT] sensor.total_poste_*_puissance (W) — condition ≠ "0"
  │     ├── Col 2 : Donut journalier (18 prises × _quotidien_kwh_um)
  │     │     └── [UM] P2_prise/P2_AVG/P2_UM_AMHQ_prises.yaml + veilles
  │     ├── Col 3 : ApexCharts ligne instantanée
  │     │     └── [NAT] sensor.ecojoko_puissance_apparente_w
  │     └── Col 4 : tabbed-card 6 onglets pièces (1/4/5/7/9/Veilles)
  │           └── [NAT] sensor.*_power (W) par prise connectée
  └── Page mensuelle /energie-mensuel (streamline par appareil)
        ├── Donut mensuel (18 séries × _mensuel_kwh_um)
        │     └── [UM] P2_prise/P2_AVG/P2_UM_AMHQ_prises.yaml + veilles
        └── Streamline cards (18 appareils — template conso_mensuelle_appareil)
              ├── [SNS] P2_prise/P2_kWh_prises.yaml (_energie_totale_kwh)
              └── [TPL] P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml (_avg_watts_mensuel)
```

---

### 🔲 L2C2 — Énergie Clim / Radiateur / Soufflant

```
L2C2 Énergie Clim
  ├── kWh par appareil (clim x3 + radiateur + soufflant + sèche-serviette)
  │     └── [UM] utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml
  │           └── [NAT] sensor.*_energy (Meross / Sonoff power sensors)
  └── Moyennes puissance [AVG]
        └── [TPL] P1_clim_chauffage/P1_AVG/P1_avg.yaml
              └── [UM] P1_UM_AMHQ.yaml
```

---

### ✅ L2C3 — Énergie Éclairage
`docs/L2C3_ENERGIE_ECLAIRAGE/`

```
L2C3 Éclairage kWh
  ├── Vignette (button-card 3 colonnes pièce/quotidien/mensuel)
  │     └── sensor.lumiere_*_etat  [TPL] P3_eclairage/ui_dashboard/etats_status.yaml
  │     └── sensor.eclairage_*_quotidien/mensuel_kwh_um
  │           └── [UM] P3_eclairage/P3_UM_AMHQ_2_ZONE.yaml + P3_UM_AMHQ_3_TOTAL.yaml
  ├── Page /dashboard-tablette/energie-lampes
  │     ├── Donuts JOUR/MOIS par ampoule (19 lampes × 5 pièces)
  │     │     └── sensor.hue_*/sonoff_*_quotidien/mensuel_kwh_um
  │     │           └── [UM] P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
  │     ├── Graphique 30 JOURS par zone + ligne AVG
  │     │     └── sensor.eclairage_*_mensuel_kwh_um  [UM 2_ZONE]
  │     │     └── sensor.eclairage_*_avg_watts_mensuel  [TPL] P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml
  │     └── Badges Q/H/M/A par zone (subtitle heading)
  │           └── [UM] P3_eclairage/P3_UM_AMHQ_2_ZONE.yaml
  ├── kWh par ampoule
  │     └── [SNS] P3_eclairage/P3_kWh_1_UNITE.yaml
  │           └── intégration Riemann sur P3_POWER_1
  ├── kWh par zone
  │     └── [SNS] P3_eclairage/P3_kWh_2_ZONE.yaml
  │           └── [UM] P3_eclairage/P3_UM_AMHQ_2_ZONE.yaml
  └── Moyennes [AVG]
        └── [TPL] P3_AVG/P3_AVG_AMHQ_*.yaml (x3)
```

---

## LIGNE 3 — COMMANDES & ACTIONNEURS

### 🔲 L3C1 — Commandes Éclairage

```
L3C1 Éclairage
  └── [NAT] light.* (Hue Bridge + Sonoff ZBMINIL2 miroir SDB)
        └── États UI → [TPL] P3_eclairage/ui_dashboard/etats_status.yaml
```

---

### 🔲 L3C2 — Commandes Éco (Prises)

```
L3C2 Prises
  ├── Consommation en cours (W)
  │     └── [NAT] sensor.*_power (Meross / Sonoff)
  ├── Standby global
  │     └── [TPL] P2_prise/P2_I_all_standby_power/P2_ current_all_standby.yaml
  └── kWh prises
        └── [SNS] P2_prise/P2_kWh_prises.yaml
              └── [UM] P2_prise/P2_AVG/P2_UM_AMHQ_prises.yaml
```

---

### ✅ L3C3 — Fenêtres + Stores
`docs/L3C3_STORES/`

```
L3C3 Fenêtres / Stores
  ├── Vignette (button-card 3 colonnes Pièce / Fenêtres / Stores)
  │     ├── [NAT] binary_sensor.contact_fenetre_* × 4 (SONOFF SNZB-04)
  │     └── [TPL] sensor.store_salon_status / sensor.store_bureau_status
  └── Page /stores (2 sections — Salon + Bureau)
        ├── enhanced-shutter-card
        │     └── [NAT] cover.store_salon / cover.store_bureau (Zigbee2MQTT)
        │     └── [NAT] sensor.store_*_signal_strength
        ├── Boutons position rapide (5 × cover.set_cover_position)
        │     └── Mapping non-linéaire calibré (Salon: 100/85/70/49/20, Bureau: 100/90/60/45/25)
        ├── Conditions affichées
        │     └── [NAT] sensor.th_balcon_nord_temperature (SONOFF SNZB-02 balcon)
        ├── Batteries contacts
        │     └── [NAT] sensor.contact_fenetre_salon/bureau_sonoff_battery
        └── DnD voyants commandes
              └── [NAT] light.store_salon_dnd / light.store_bureau_dnd (helpers UI)
```

---

## LIGNE 4 — RÉSEAU & SYSTÈME

### ✅ L4C1 — Freebox Pop
`docs/L4C1_FREEBOX/`

```
L4C1 Freebox
  ├── Vignette (custom:button-card — navigation pure, pas d'entité live)
  ├── Page /systeme-freebox
  │     ├── Bloc Speedtest
  │     │     ├── Déclencheur manuel → homeassistant.update_entity
  │     │     │     └── [NAT] sensor.speedtest_cli_data (Speedtest CLI)
  │     │     │     └── [NAT] sensor.speedtest_download (Speedtest CLI)
  │     │     └── Bouton popup → #speedtest_details
  │     └── Bloc Freebox info (stack-in-card)
  │           ├── [NAT] device_tracker.freebox_v8_r1 (attr: IPv4, IPv6, uptime, connection_type, firmware_version)
  │           ├── [NAT] sensor.freebox_download_speed
  │           ├── [NAT] sensor.freebox_upload_speed
  │           ├── [NAT] sensor.freebox_temperature_1
  │           └── [NAT] sensor.freebox_temperature_cpu_b
  └── Pop-up #speedtest_details (Historique 24h Download/Upload/Ping)
        ├── [NAT] sensor.speedtest_cli_data (attr: isp, server.name/location/country)
        ├── [TPL] sensor.speedtest_cli_download  → templates/SpeedTest/ST_01_speedTest.yaml
        ├── [TPL] sensor.speedtest_cli_upload    → templates/SpeedTest/ST_01_speedTest.yaml
        └── [TPL] sensor.speedtest_cli_ping      → templates/SpeedTest/ST_01_speedTest.yaml

⚠️ Page originellement optimisée pour Raspberry Pi — ajustements possibles sur x86-64
```

---

### 🔲 L4C2 — Mini PC

```
L4C2 Mini PC
  └── [NAT] command_line/sante_systeme_mini_pc/sante_systeme_mini_pc.yaml
        sensor.mini_pc_* (CPU, RAM, temp sondes)
```

---

### ✅ L4C3 — Mises à jour HA
`docs/L4C3_MAJ_HA/`

```
L4C3 MAJ HA
  ├── Vignette (button-card)
  │     └── [TPL] templates/utilitaires/Mise_a_jour_home_assistant.yaml
  │           └── sensor.available_updates
  │                 └── [NAT] update.* (domaine natif HA — state == 'on')
  └── Page /dashboard-tablette/maj
        ├── Grille 1 — H.A. SERVER
        │     ├── [NAT] update.home_assistant_core_update
        │     ├── [NAT] update.home_assistant_operating_system_update
        │     ├── [NAT] update.home_assistant_supervisor_update
        │     └── [NAT] update.hacs_update (HACS)
        └── Grille 2 — H.A. UPDATE
              ├── [NAT] update.* filtrés par intégration (hassio / hacs / mqtt)
              └── [NAT] sensor.processor_use + sensor.memory_use_percent
```

---

## LIGNE 5 — MAINTENANCE MATÉRIELLE

### ✅ L5C1 — Batteries / Piles
`docs/L5C1_PILES_BATTERIES/`

```
L5C1 Batteries
  └── [NAT] sensor.*_battery (%) — 34 capteurs
        └── groups.yaml
              ├── group.ikea_devices  (12 capteurs)
              ├── group.hue_devices   (11 capteurs)
              └── group.sonoff_devices (11 capteurs)
```

---

### 🔲 L5C2 — Batterie Portail

```
L5C2 Batterie Portail
  └── [NAT] sensor.portail_battery (%) — à préciser
```

---

### ✅ L5C3 — MariaDB
`docs/L5C3_MARIADB/`

```
L5C3 MariaDB
  └── [NAT] sensor.taille_db_home_assistant
        └── sql.yaml → MariaDB (secrets.yaml: mariadb_url)
```

---

## LIGNE 6 — QUALITÉ & ALERTES

### ✅ L6C1 — Qualité de l'air (Appartement)
`docs/L6C1_AIR_QUALITE/`

```
L6C1 Air intérieur
  ├── Vignette (custom:button-card 9 lignes × 3 cols — PM2.5 + tCOV × 3 pièces)
  │     ├── [NAT] sensor.qualite_air_salon_ikea_pm25         (IKEA Vindstyrka)
  │     ├── [NAT] sensor.qualite_air_salon_ikea_voc_index    (IKEA Vindstyrka)
  │     ├── [NAT] sensor.qualite_air_bureau_ikea_pm25        (IKEA Vindstyrka)
  │     ├── [NAT] sensor.qualite_air_bureau_ikea_voc_index   (IKEA Vindstyrka)
  │     ├── [NAT] sensor.qualite_air_chambre_ikea_pm25       (IKEA Vindstyrka)
  │     └── [NAT] sensor.qualite_air_chambre_ikea_voc_index  (IKEA Vindstyrka)
  └── Page /air-quality (3 sections Salon / Bureau / Chambre)
        ├── Ring-tile PM2.5 (custom:streamline-card — template: pm25_ring-tile)
        │     ├── entity   → [NAT] sensor.qualite_air_*_ikea_pm25
        │     └── marker2  → [SNS] sensor.pm2_5_*_moy_24h
        │                         sensors/air_qualite/pm25_tcov_moy_24h.yaml
        │                         platform: statistics — mean — max_age: 24h
        ├── Ring-tile tCOV (custom:streamline-card — template: cov_ring-tile)
        │     ├── entity   → [TPL] sensor.tcov_*_ppb
        │     │                    templates/air_qualite/tcov_ppb.yaml
        │     │                    device_class: volatile_organic_compounds_parts
        │     │                    source → [NAT] sensor.qualite_air_*_ikea_voc_index
        │     └── marker2  → [SNS] sensor.tcov_*_moy_24h
        │                         sensors/air_qualite/pm25_tcov_moy_24h.yaml
        ├── Boutons pop-up PM2.5 / tCOV (custom:bubble-card button — hash #*pm25 / #*cov)
        └── Pop-ups graphiques (vertical-stack — bubble-card pop-up + streamline-card)
              ├── template: pm25 — entity_sensor: [NAT] sensor.qualite_air_*_ikea_pm25
              │                    mean_24h_entity: [SNS] sensor.pm2_5_*_moy_24h
              └── template: cov  — entity_sensor: [NAT] sensor.qualite_air_*_ikea_voc_index
                                   mean_24h_entity: [SNS] sensor.tcov_*_moy_24h
```

---

### 🔲 L6C2 — Pollution / Pollen (Extérieur)

```
L6C2 Pollution ext.
  └── [NAT] intégration AtmoFrance (HACS custom_components/atmofrance)
        sensor.atmofrance_*
```

---

### 🔲 L6C3 — Vigilance Eau

```
L6C3 Vigieau
  └── [NAT] intégration Vigieau (HACS custom_components/vigieau)
        sensor.vigieau_*
```

---

## PAGE HOME (Racine du dashboard)

> 📄 Doc complète : [`docs/WIFI_PRESENCE (Home Page)/PAGE_HOME.md`](./WIFI_PRESENCE%20(Home%20Page)/PAGE_HOME.md)

### ✅ WIFI / Présence
`docs/WIFI_PRESENCE (Home Page)/`

```
Présence
  ├── Détection Wi-Fi
  │     └── [TPL] P4_groupe_presence/02_logique_wifi_cellular.yaml
  │           └── [NAT] device_tracker.* (intégration router / nmap)
  └── Carte état téléphones
        └── [TPL] P4_groupe_presence/01_phones_wifi_cellular_card_autom.yaml
```

---

## 📋 STATUT DOCS VIGNETTES

| Vignette | Doc existante | Dépendances complètes |
|----------|---------------|-----------------------|
| L1C1 Météo | ✅ | ✅ |
| L1C2 Températures | ✅ | ✅ |
| L1C3 Commandes Clim | 🔲 | 🔲 |
| L2C1 Énergie Générale | ✅ | ✅ |
| L2C2 Énergie Clim | 🔲 | 🔲 |
| L2C3 Énergie Éclairage | ✅ | ✅ |
| L3C1 Commandes Éclairage | 🔲 | 🔲 |
| L3C2 Commandes Prises | 🔲 | 🔲 |
| L3C3 Fenêtres + Stores | ✅ | ✅ |
| L4C1 Freebox | ✅ | ✅ |
| L4C2 Mini PC | 🔲 | 🔲 |
| L4C3 MAJ HA | ✅ | ✅ |
| L5C1 Batteries | ✅ | ✅ |
| L5C2 Batterie Portail | 🔲 | 🔲 |
| L5C3 MariaDB | ✅ | ✅ |
| L6C1 Air intérieur | ✅ | ✅ |
| L6C2 Pollution ext. | 🔲 | 🔲 |
| L6C3 Vigieau | 🔲 | 🔲 |
| **PAGE HOME** | | |
| Wifi / Présence | ✅ | ✅ |
