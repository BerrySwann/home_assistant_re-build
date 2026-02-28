# CAHIER DES CHARGES - MIGRATION HOME ASSISTANT v1.5 → v2.0

**Version :** 1.2  
**Date :** 22 février 2026  
**Auteur :** Eric (Technicien maintenance SNEF)  
**Statut :** 🟡 EN COURS - Phase 0 (65% complété)

---

## 📊 RÉSUMÉ EXÉCUTIF

**Objectif :** Migration complète Home Assistant v1.5 (Raspberry Pi 4) vers v2.0 (nouvelle instance propre) sans perte de fonctionnalité ni interruption de service prolongée.

**Stratégie :** Migration progressive pôle par pôle avec système dual (v1.5 prod + v2.0 test) via écoute MQTT, permettant validation complète avant bascule finale.

**Avancement global :** 40% (Phase 0: 65%, Phase 1: 15%)

---

## 🎯 NOUVEAUTÉS VERSION 1.2

### **Travaux réalisés session 22/02/2026 :**

✅ **Infrastructure v2.0 complète installée**
- Home Assistant OS opérationnel
- 19 cartes HACS installées et validées
- Intégrations critiques configurées (8/17)
- MQTT client mode écoute fonctionnel

✅ **Configuration mode MQTT écoute validée**
- v2.0 connecté à Mosquitto v1.5 (192.168.1.96:1883)
- 54 équipements Zigbee visibles en temps réel
- ~150-200 entités découvertes automatiquement
- Zéro impact sur prod v1.5

✅ **Structure fichiers v2.0 organisée**
- Arborescence /config/ créée selon bonnes pratiques
- Dossiers sensors/, templates/, utility_meter/ structurés par pôles
- Fichiers P2 et P3 partiellement migrés

✅ **Documentation technique enrichie**
- Tree structure complète générée
- Dashboard v1.5 sauvegardé
- Configuration Z2M v1.5 documentée

---

## 📋 TABLE DES MATIÈRES

1. [Contexte & Objectifs](#1-contexte--objectifs)
2. [Périmètre Projet](#2-périmètre-projet)
3. [Architecture](#3-architecture)
4. [Glossaire & Conventions](#4-glossaire--conventions)
5. [Inventaire Équipements](#5-inventaire-équipements)
6. [Cartographie Automations](#6-cartographie-automations)
7. [Bugs & Points Vigilance](#7-bugs--points-vigilance)
8. [Procédures Maintenance](#8-procédures-maintenance)
9. [Roadmap Migration](#9-roadmap-migration)
10. [Annexes Techniques](#10-annexes-techniques)

---

## 1. CONTEXTE & OBJECTIFS

### 1.1 Situation Actuelle

**Système v1.5 (Production) :**
- **Plateforme :** Raspberry Pi 4 / Home Assistant OS
- **Durée vie :** 1.5 ans (depuis ~août 2024)
- **État :** ✅ Fonctionnel mais nécessite refactoring
- **Équipements :** 54 Zigbee + 30 Hue + 10+ autres
- **Surface :** 61m² (9 pièces)

**Problématiques identifiées :**
- ⚠️ Évolution organique → Nommage incohérent
- ⚠️ Fichiers monolithiques (automations.yaml)
- ⚠️ Templates séries 01-18 sans standard clair
- ⚠️ Documentation dispersée
- ⚠️ Code legacy non documenté ("syndrome P4")

### 1.2 Objectifs Migration

**Objectifs fonctionnels :**
1. ✅ Conserver 100% des fonctionnalités v1.5
2. ✅ Améliorer maintenabilité (nommage, structure)
3. ✅ Optimiser performances
4. ✅ Faciliter évolutions futures

**Objectifs techniques :**
1. ✅ Refactoring complet structure fichiers
2. ✅ Nommage cohérent v2.0
3. ✅ Documentation exhaustive
4. ✅ Tests validation 7j par pôle

**Objectifs opérationnels :**
1. ✅ Migration sans interruption service prolongée
2. ✅ Rollback instantané si problème
3. ✅ Validation progressive (P1/P2/P3)
4. ✅ Formation/documentation pour maintenance future

### 1.3 Livrables

- [x] Cahier des charges complet (v1.2) ✅
- [ ] Schémas architecture (Draw.io/Mermaid) 🔄
- [x] Inventaire exhaustif équipements ✅
- [x] Cartographie automations critiques ✅
- [ ] Procédures maintenance 🔄
- [x] Roadmap détaillée ✅
- [ ] Documentation technique v2.0 🔄

---

## 2. PÉRIMÈTRE PROJET

### 2.1 Inclus

**Équipements physiques :**
- ✅ Climatisation/Chauffage : 3 splits + 1 radiateur électrique + 2 chauffages SDB
- ✅ Volets motorisés : 2 (Salon, Bureau)
- ✅ Éclairage : ~30 ampoules (Hue White/Ambiance/Color + Sonoff)
- ✅ Prises connectées : 17 (IKEA, NOUS)
- ✅ Capteurs : T°/H° ×6, PM2.5+tCOV ×3, Fenêtres ×4
- ✅ Monitoring : Ecojoko, Linky (API)

**Fonctionnalités :**
- ✅ Monitoring énergétique (logs 15min, 3 pôles)
- ✅ Automations chauffage (jour/nuit, présence G1-G4)
- ✅ Gestion volets intelligente
- ✅ Notifications mobile (Poco X7 Pro + Xiaomi Watch)
- ✅ Dashboards Lovelace (19 cartes HACS)

**Infrastructure :**
- ✅ Raspberry Pi 4 (consolidation)
- ✅ Intégrations externes (10+)
- ✅ Custom components HACS

### 2.2 Exclus

**Phase initiale (à intégrer ultérieurement) :**
- ❌ Caméras surveillance
- ❌ Domotique professionnelle (UCA)
- ❌ Optimisation réseau avancée
- ❌ Sauvegardes automatisées cloud (Phase 2)
- ❌ Machine Learning prédictif (Phase 4)

### 2.3 Contraintes

**Techniques :**
- ✅ Compatibilité matériel existant
- ✅ Pas de re-pairage équipements avant Phase 6
- ✅ Conservation données historiques

**Opérationnelles :**
- ✅ Migration hors heures critiques chauffage
- ✅ Prod v1.5 jamais arrêtée >2h
- ✅ Tests validation 7j minimum par pôle

---

## 3. ARCHITECTURE

### 3.1 Architecture v1.5 (Actuelle)

**Infrastructure matérielle :**
```
Raspberry Pi 4 (v1.5)
├── Dongle Zigbee (SONOFF USB Plus V2)
│   └── 54 équipements appairés
├── Bridge Hue (Philips)
│   └── ~30 ampoules
└── Mosquitto Broker (port 1883)
    └── Zigbee2MQTT publish
```

**Structure fichiers :**
```yaml
/config/
├── configuration.yaml (includes)
├── automations.yaml ⚠️ (monolithique)
├── sensors/
│   ├── p1_0_sensors_clim_rad.yaml
│   ├── p1_1_sensors_dut.yaml
│   ├── p1_2_sensors_Perf.yaml
│   ├── p1_3_sensors_moy_24h.yaml
│   ├── p2_sensors_prises.yaml
│   ├── p3_sensors_lumieres.yaml
│   ├── sensors_blitzortung.yaml
│   ├── sensors_erodi_ha.yaml
│   ├── sensors_mini_pc.yaml
│   └── sensors_pm25_et_tcov.yaml
├── templates/ (18 séries) ⚠️
│   ├── 01_1_meteo_alertes_card.yaml
│   ├── 01_2_meteo_foudre_card.yaml
│   ├── [...série 01 à 18...]
│   └── 18_1_Moyenne_daily_monthly.yaml
├── utility_meter.yaml
└── scripts.yaml
```

### 3.2 Architecture v2.0 (Cible)

**Infrastructure matérielle (Phase 0-5) :**
```
┌─────────────────────────────────────────────────┐
│ Raspberry Pi 4 (v1.5) - PRODUCTION             │
├─────────────────────────────────────────────────┤
│ • Dongle Zigbee (contrôle 54 devices)          │
│ • Mosquitto Broker (192.168.1.96:1883)         │
│ • Zigbee2MQTT (publish topics)                 │
└─────────────────────────────────────────────────┘
                    │
                    │ MQTT Topics
                    │ zigbee2mqtt/#
                    ▼
┌─────────────────────────────────────────────────┐
│ Raspberry Pi 4 / VM (v2.0) - TEST              │
├─────────────────────────────────────────────────┤
│ • MQTT Client (subscribe mode écoute)          │
│ • Voit 54 équipements Zigbee temps réel        │
│ • PAS de contrôle (lecture seule)              │
│ • Migration progressive P1/P2/P3               │
└─────────────────────────────────────────────────┘
```

**Infrastructure matérielle (Phase 6 - Post-migration) :**
```
┌─────────────────────────────────────────────────┐
│ Raspberry Pi 4 (v2.0) - PRODUCTION UNIQUE      │
├─────────────────────────────────────────────────┤
│ • Dongle Zigbee (migré depuis v1.5)            │
│ • Mosquitto Broker                             │
│ • Zigbee2MQTT                                  │
│ • Bridge Hue                                   │
│ • Mini-PC décommissionné                       │
└─────────────────────────────────────────────────┘
```

**Structure fichiers v2.0 (Cible) :**
```yaml
/config/
├── configuration.yaml (minimaliste, includes)
├── secrets.yaml
├── automations/ (découpage par domaine)
│   ├── heating/
│   │   ├── mode_day.yaml
│   │   ├── mode_night.yaml
│   │   └── kitchen_timer.yaml
│   ├── covers/
│   │   └── livingroom_automation.yaml
│   ├── monitoring/
│   │   └── energy_log_15min.yaml
│   └── notifications/
│       └── battery_alerts.yaml
├── sensors/
│   ├── P1_clim_chauffage/
│   │   ├── p1_0_sensors_clim_rad.yaml (kWh)
│   │   ├── p1_1_sensors_dut.yaml (DUT)
│   │   ├── p1_2_sensors_Perf.yaml (Performance)
│   │   └── p1_3_sensors_moy_24h.yaml (Moyennes)
│   ├── P2_prise/
│   │   └── P2_kWh.yaml
│   └── P3_eclairage/
│       ├── P3_kWh_1_UNITE.yaml
│       ├── P3_kWh_2_ZONE.yaml
│       └── P3_kWh_3_TOTAL.yaml
├── templates/
│   ├── P1_/
│   │   └── P1_AVG/
│   │       └── P1_avg.yaml
│   ├── P2_prises/
│   │   ├── P2_AVG/
│   │   │   └── P2_avg.yaml
│   │   └── (P2_puissance.yaml - si nécessaire)
│   ├── P3_eclairage/
│   │   ├── P3_01_somme_par_piece.yaml (Puissance W)
│   │   ├── P3_02_energie.yaml (Énergie kWh) ⚠️ À CRÉER
│   │   └── ui_dashboard/
│   │       └── etats_status.yaml
│   └── generales/
│       └── 18_1_Moyenne_daily_monthly.yaml
├── utility_meter/
│   ├── P1_clim_chauffage/
│   │   └── P1_UM_AMHQ.yaml
│   ├── P2_prise/
│   │   └── P2_UM_AMHQ.yaml
│   └── P3_eclairage/
│       ├── P3_UM_AMHQ_1_UNITE.yaml
│       ├── P3_UM_AMHQ_2_ZONE.yaml
│       └── P3_UM_AMHQ_3_TOTAL.yaml
├── packages/ (optionnel Phase 2)
│   ├── heating.yaml
│   ├── lighting.yaml
│   └── energy.yaml
└── dashboards/
    ├── main.yaml
    ├── energy.yaml
    └── rooms/
        ├── livingroom.yaml
        └── kitchen.yaml
```

### 3.3 Flux Données Énergétiques

**v1.5 (Actuel) :**
```
Équipements physiques (Zigbee/Hue)
    ↓ Power (W)
Zigbee2MQTT / Hue Bridge
    ↓ MQTT Topics / API
Sensors integration (platform: integration)
    ↓ Energy (kWh)
Utility Meters (daily/monthly/yearly)
    ↓ Cycles temporels
Templates (calculs DUT/Avg/Perf)
    ↓ Métriques avancées
Dashboard + Automations
```

**v2.0 Mode écoute (Phase 0-5) :**
```
v1.5 Mosquitto Broker (192.168.1.96:1883)
    ↓ MQTT Topics zigbee2mqtt/#
v2.0 MQTT Client (subscribe only)
    ↓ Discovery automatique
v2.0 Entités Zigbee (lecture seule)
    ↓ Sensors integration (v2.0)
v2.0 Utility Meters (v2.0)
    ↓ Cycles temporels
v2.0 Templates (v2.0)
    ↓ Métriques avancées
v2.0 Dashboard (v2.0) - Validation comparative
```

### 3.4 Configuration MQTT Mode Écoute

**Mosquitto Broker v1.5 :**
```yaml
# Modules complémentaires > Mosquitto Broker > Configuration
logins:
  - username: homeassistant
    password: [mdp_principal]
  - username: mqtt
    password: mqtt
    
customize:
  active: false
  folder: mosquitto
  
certfile: fullchain.pem
keyfile: privkey.pem
require_certificate: false
anonymous: false
```

**MQTT Client v2.0 :**
```yaml
# Paramètres > Appareils et Services > MQTT
# Configuration via UI (PAS dans configuration.yaml)

Broker: 192.168.1.96
Port: 1883
Username: mqtt
Password: mqtt
Découverte: ✅ Activée
Préfixe découverte: homeassistant
```

**Résultat :**
- ✅ v2.0 voit 54 équipements Zigbee temps réel
- ✅ ~150-200 entités découvertes automatiquement
- ✅ Zéro contrôle possible (lecture seule)
- ✅ Zéro impact v1.5 (prod intacte)

---

## 4. GLOSSAIRE & CONVENTIONS

### 4.1 Pôles Énergétiques

**Classification système (P1-P7) :**

| Pôle | Nom | Équipements | Priorité Migration |
|:-----|:----|:------------|:-------------------|
| **P1** | Hygiène | Lave-Linge, Lave-Vaisselle | Moyenne |
| **P2** | Cuisson | Four, Micro-ondes, Air-Fryer, Plaques | Moyenne |
| **P3** | Froid | Frigo, Congélateur | Haute (24/7) |
| **P4** | Chauffage | Clims ×3, Radiateur, Soufflant, Sèche-Serviette | **Critique** |
| **P5** | Multimédia | PC ×2, TV, Mini-PC HA | Basse |
| **P6** | Luminaire | Hue ×25, Sonoff ×5 | Moyenne |
| **P7** | Autres | Standby, Ecojoko, Capteurs | Faible |

**Regroupement migration (simplifié) :**
- **P3 Éclairage** → Migration Semaine 1-2 (en cours 65%)
- **P2 Prises** → Migration Semaine 3 (préparé 30%)
- **P1 Chauffage** → Migration Semaine 4-5 (préparé 20%)

### 4.2 Nommage Entités v2.0

**Convention standard :**
```
{domain}_{location}_{function}_{metric}_{cycle}
```

**Exemples :**
```yaml
# v1.5 (ancien)
sensor.clim_rad_total_avg_watts_daily

# v2.0 (nouveau - optionnel)
sensor.heating_total_power_avg_daily

# v2.0 (conservé pour compatibilité)
sensor.clim_rad_total_avg_watts_daily
```

**Domaines :**
- heating, lighting, energy, climate, air_quality, cover, switch, sensor

**Locations :**
- livingroom, kitchen, office, bathroom, bedroom, entrance, hallway

**Functions :**
- total, average, runtime, status, power, temperature

**Metrics :**
- kwh, watts, hours, celsius, percent, count

**Cycles :**
- daily, monthly, yearly, realtime

### 4.3 DUT (Durée Utilisation Totale)

**Format actuel v1.5 :**
```
DUT S/R/B/C:3.8/0.2/11.2/14.9
```

**Format cible v2.0 :**
```
DUT S/R/B/Sf/SS/C:3.8/0.2/11.2/0.0/0.0/14.9
```

**Légende :**
- S = Salon
- R = Radiateur Cuisine
- B = Bureau
- Sf = Soufflant SDB (ajouté v2.0)
- SS = Sèche-Serviette SDB (ajouté v2.0)
- C = Chambre

### 4.4 Groupes Présence (G1-G4)

**États présence logement :**

| Groupe | Mamour | Eric | Volets | T° Cible Hiver | T° Cible Été |
|:-------|:-------|:-----|:-------|:---------------|:-------------|
| **G1** | Absente | Absent | Fermés | 17-19°C | - |
| **G2** | Présente | Absent | Ouverts | 20-21°C | 28°C |
| **G3** | Absente | Présent | Auto | 20-21°C | 28°C |
| **G4** | Présente | Présent | Ouverts | 20-21°C | 28°C |

**Logique volets :**
- G1/G3 : Fermer si T°ext <17°C (isolation)
- G2/G4 : Ouvrir si Mamour présente (lumière naturelle)
- Tous : Fermer si T°ext >34°C (protection solaire)

### 4.5 Séries Templates (01-18)

**Organisation v1.5 (à restructurer v2.0) :**

| Série | Nom | Fichiers | Migration v2.0 |
|:------|:----|:---------|:---------------|
| 01 | Météo | 4 cards | → templates/meteo/ |
| 02 | Réseau | 1 card | → templates/reseau/ |
| 03 | Climat/Chauffage | 8 cards | → templates/P1_/ |
| 04 | Éclairage | 3 cards | → templates/P3_/ |
| 05 | MAJ HA | 1 vignette | → templates/system/ |
| 06 | Wi-Fi | 1 card | → templates/reseau/ |
| 07 | Fenêtres | 1 automation | → automations/sensors/ |
| 08 | Stores/Volets | 1 vignette | → templates/covers/ |
| 09 | Standby | 1 sensor | → templates/P2_/ |
| 10 | Qualité Air | 1 ppb | → templates/air_quality/ |
| 11 | Ecojoko/Linky | 4 cards | → templates/energy/ |
| 12 | Mini-PC | 1 sensor | → templates/system/ |
| 13 | Temporel | 1 sensor | → templates/time/ |
| 14 | Interrupteurs | 2 cards | → templates/switches/ |
| 15 | Jour/Nuit | 2 sensors | → templates/time/ |
| 16 | Icônes | 1 icon | → templates/ui/ |
| 17 | Diagnostics | 2 cards | → templates/energy/ |
| 18 | Moyennes | 1 card | → templates/generales/ |

---

## 5. INVENTAIRE ÉQUIPEMENTS

### 5.1 Chauffage & Climatisation (Pôle P4)

#### **4. SALON (Sud, 25.88 m²)**
- **Split mural** : ~2000W
  - Entité v1.5 : `climate.clim_salon`, `sensor.clim_salon_nous_power`
  - Entité v2.0 : Identique (via MQTT)
- **Volet motorisé**
  - Automation : Ouvert 7h30 → Coucher soleil / Fermé si Absence / Fermé si >34°C
  - Apport solaire crucial dès 15h

#### **5. CUISINE (Nord, 10.59 m²)**
- **Radiateur bain d'huile** : ~1500W
  - Entité v1.5 : `sensor.radiateur_elec_cuisine_power`
  - Entité v2.0 : Identique (via MQTT)
  - Automation : L-Ma-Me-Je (4h45-7h), Ve-Sa-Di (5h45-8h)
  - Thermostat virtuel : <19.9°C ON / >20.5°C OFF

#### **7. BUREAU (Nord, 10.55 m²)**
- **Split mural** : ~2000W
  - Entité v1.5 : `climate.clim_bureau`, `sensor.clim_bureau_nous_power`
  - Entité v2.0 : Identique (via MQTT)
- **Volet motorisé**
  - Automation : Ouvert si T°ext [18-25°C]
- **Rideaux épais** : Installés 22/02/2026 (isolation thermique)

#### **8. SDB (Interne, 3.13 m²)**
- **Soufflant** : 2×1000W
  - Entité v1.5 : `sensor.prise_soufflant_salle_de_bain_nous_power`
  - Entité v2.0 : Identique (via MQTT)
  - Automation : OFF si >23°C
- **Sèche-serviette** : 150W
  - Entité v1.5 : `sensor.prise_seche_serviette_salle_de_bain_nous_power`
  - Entité v2.0 : Identique (via MQTT)
  - Automation : Timer 2h après douche (⚠️ Non testé)

#### **9. CHAMBRE (Nord, 11.26 m²)**
- **Split mural** : ~2000W
  - Entité v1.5 : `climate.clim_chambre`, `sensor.clim_chambre_nous_power`
  - Entité v2.0 : Identique (via MQTT)
- **Store manuel** : Non motorisé
- **Rideaux épais** : Installés 07/02/2026
- **Note** : Forte dissipation thermique (DUT 3.9× vs Salon)

### 5.2 Prises Connectées (Pôle P2/P5/P7)

#### **1. ENTRÉE**
- Box Internet (IKEA) : `sensor.prise_box_internet_ikea_power`
- Horloge (IKEA) : `sensor.prise_horloge_ikea_power`

#### **4. SALON**
- PC Salon (IKEA) : `sensor.prise_pc_s_gege_ikea_power`
- Chargeur (NOUS) : `sensor.prise_salon_chargeur_nous_power`

#### **5. CUISINE**
- Micro-ondes (NOUS) : `sensor.prise_four_micro_ondes_nous_power`
- Lave-linge (NOUS) : `sensor.prise_lave_linge_nous_power`
- Lave-vaisselle (NOUS) : `sensor.prise_lave_vaisselle_nous_power`
- Air-fryer (NOUS) : `sensor.prise_airfryer_ninja_nous_power`
- Four+Plaques : `sensor.four_et_plaque_de_cuisson_power`
- Frigo (NOUS) : `sensor.prise_frigo_cuisine_nous_power`
- Congélateur (NOUS) : `sensor.prise_congelateur_cuisine_nous_power`

#### **7. BUREAU**
- PC Bureau (IKEA) : `sensor.prise_bureau_pc_ikea_power`
- Fer à repasser (NOUS) : `sensor.prise_bureau_fer_a_repasser_nous_power`

#### **9. CHAMBRE**
- Tête de lit : `sensor.prise_tete_de_lit_chambre_power`
- TV (NOUS) : `sensor.prise_tv_chambre_nous_power`

#### **10. AUTRE**
- All Standby : `sensor.all_standby_power`
- Mini-PC : `sensor.prise_mini_pc_ikea_power` (à décommissionner Phase 3)

### 5.3 Éclairage (Pôle P6)

#### **Philips Hue (~25 ampoules)**

**1. ENTRÉE :**
- 1× Hue White

**4. SALON :**
- 1× Hue White (Table)
- 3× Hue Ambiance
- 1× Hue Color

**5. CUISINE :**
- 1× Hue White

**6. COULOIR :**
- 1× Hue White

**7. BUREAU :**
- 3× Play
- 2× Hue White

**8. SDB :**
- 1× Hue White

**9. CHAMBRE :**
- 2× Hue White
- 2× Hue Color Zone

#### **Sonoff (~5 ampoules)**

**8. SDB :**
- 1× Miroir Sonoff

### 5.4 Capteurs

#### **Température/Humidité (×6 SONOFF SNZB-02)**
- Balcon Nord (T° ext) : `sensor.th_balcon_nord_temperature`
- Salon : `sensor.th_salon_temperature/humidity`
- Cuisine : `sensor.th_cuisine_temperature/humidity`
- Bureau : `sensor.th_bureau_temperature/humidity`
- SDB : `sensor.th_salle_de_bain_temperature`
- Chambre : `sensor.th_chambre_temperature`

#### **Qualité Air PM2.5 + tCOV (×3 IKEA VINDSTYRKA)**
- Salon : `sensor.qualite_air_salon_ikea_pm25/voc_index`
- Bureau : `sensor.qualite_air_bureau_ikea_pm25/voc_index`
- Chambre : `sensor.qualite_air_chambre_ikea_pm25/voc_index`

#### **Ouverture Fenêtres (×4 IKEA VALLHORN + SONOFF)**
- Salon : `binary_sensor.contact_fenetre_salon_ikea_contact`
- Cuisine : `binary_sensor.contact_fenetre_cuisine_contact`
- Bureau : `binary_sensor.contact_fenetre_bureau_contact`
- Chambre : `binary_sensor.contact_fenetre_chambre_contact`

#### **Monitoring Énergie**
- Ecojoko : `sensor.ecojoko_power/energy_daily`
- Linky (API MyElectricalData) : `sensor.linky_25481620821301_*`

### 5.5 Dongle Zigbee

**Modèle :** SONOFF Zigbee 3.0 USB Dongle Plus V2  
**Port v1.5 :** `/dev/serial/by-id/usb-ITEAD_SONOFF_Zigbee_3.0_USB_Dongle_Plus_V2_20231121194208-if00`  
**Adapter :** ember  
**Équipements appairés :** 54

**Paramètres réseau Zigbee v1.5 (à conserver v2.0) :**
```yaml
network_key: [178, 172, 119, 211, 134, 153, 2, 27, 80, 242, 226, 246, 27, 214, 189, 209]
pan_id: 34933
ext_pan_id: [207, 75, 225, 233, 176, 165, 152, 116]
channel: 25
```

---

## 6. CARTOGRAPHIE AUTOMATIONS

### 6.1 Automations Critiques

#### **Chauffage Mode Jour (07h30-21h00)** 🔴 HAUTE
- **Fichier :** `templates/03_07_automation_message_clim_7h30_21h.yaml`
- **Déclencheur :** Time 07:30
- **Logique :**
  1. Activation mode Jour
  2. Vérification présence (G1-G4)
  3. Vérification fenêtres (arrêt si ouvert)
  4. Ajustement T° selon T° ext
- **Criticité :** 🔴 HAUTE (confort thermique)
- **Statut :** ✅ CONFORME
- **Migration v2.0 :** → `automations/heating/mode_day.yaml`

#### **Chauffage Mode Nuit (21h00-07h30)** 🔴 HAUTE
- **Fichier :** `templates/03_08_automation message clim 21h 7h30.yaml`
- **Déclencheur :** Time 21:00
- **Logique :**
  1. Activation mode Nuit
  2. Réduction température (-1°C)
  3. Notification mobile
- **Criticité :** 🔴 HAUTE
- **Statut :** ✅ CONFORME
- **Migration v2.0 :** → `automations/heating/mode_night.yaml`

#### **Radiateur Cuisine Timer** 🟡 MOYENNE
- **Déclencheurs :**
  - Time L-Ma-Me-Je 04:45
  - Time Ve-Sa-Di 05:45
- **Logique :**
  - Thermostat virtuel <19.9°C ON / >20.5°C OFF
  - Arrêt automatique 7h00 / 8h00
- **Criticité :** 🟡 MOYENNE
- **Statut :** ✅ CONFORME (validé audit 22/02)
- **Migration v2.0 :** → `automations/heating/kitchen_timer.yaml`

#### **Sèche-Serviette Timer 2h** 🟢 BASSE
- **Déclencheur :** Détection >50W
- **Action :** Timer 2h puis arrêt
- **Criticité :** 🟢 BASSE
- **Statut :** ⚠️ NON TESTÉ (aucun cycle détecté logs)
- **Migration v2.0 :** → `automations/heating/bathroom_dryer.yaml`

#### **Volets Salon Gestion Intelligente** 🟡 MOYENNE
- **Scénarios :**
  - **Isolation (G1/G3) :** Fermer si T°ext <17°C
  - **Lumière (G2/G4) :** Ouvrir si Mamour présente
  - **Protection solaire :** Fermer si T°ext >34°C
- **Criticité :** 🟡 MOYENNE
- **Statut :** ⚠️ Impossible valider sans tags G1-G4 dans logs
- **Migration v2.0 :** → `automations/covers/livingroom_automation.yaml`

#### **Volets Bureau Gestion Thermique** 🟡 MOYENNE
- **Logique :** Ouvert si T°ext [18-25°C], sinon fermé
- **Criticité :** 🟡 MOYENNE
- **Statut :** ✅ CONFORME
- **Migration v2.0 :** → `automations/covers/office_automation.yaml`

#### **Diagnostic Énergie Log 15min** 🔴 HAUTE
- **Alias :** `DIAG - ENREGISTREMENT JOURNALIER (6 POSTES + DUT)`
- **Déclencheur :** Time pattern */15 * * * *
- **Actions :** Collecte 7 pôles + Avg P4 + T° int/ext + DUT
- **Criticité :** 🔴 HAUTE (monitoring énergétique)
- **Statut :** 🟡 EN COURS CORRECTION (ajout DUT Sf/SS - fait 22/02)
- **Fichier corrigé :** `automation_diag_enregistrement_corrected.yaml`
- **Migration v2.0 :** → `automations/monitoring/energy_log_15min.yaml`

### 6.2 Automations Secondaires

**Notifications :**
- Batteries capteurs <20%
- Fenêtres ouvertes + chauffage ON
- Mise à jour HA disponible

**Éclairage :**
- Extinction automatique après absence
- Allumage progressif matin
- Scènes ambiance (soirée, film, lecture)

**Sécurité :**
- Détection fuite eau (IKEA Detector)
- Surveillance qualité air (seuils PM2.5/tCOV)

---

## 7. BUGS & POINTS VIGILANCE

### 7.1 Bugs Actifs

#### **BUG-001** 🟡 MOYEN (RÉSOLU)
- **Description :** DUT Soufflant/Sèche-Serviette absents logs 15min
- **Impact :** Monitoring incomplet DUT total
- **Statut :** ✅ **CORRIGÉ 22/02/2026**
- **Solution :** Automation `automation_diag_enregistrement_corrected.yaml`
- **Validation :** À tester cycle suivant

#### **BUG-002** 🟢 FAIBLE
- **Description :** Timer 2h Sèche-Serviette non validé
- **Impact :** Pas de coupure automatique après douche
- **Statut :** 🔴 **TEST REQUIS**
- **Action :** Tester cycle complet avec détection >50W

#### **BUG-003** 🟡 MOYEN
- **Description :** Absence tags G1-G4 dans logs
- **Impact :** Impossible valider automations volets contextuelles
- **Statut :** 🔴 **À IMPLÉMENTER**
- **Action :** Ajouter logging états présence dans automations

### 7.2 Points Vigilance Thermique

#### **Chambre Nord - Surconsommation**
- **Constat :** DUT 3.9× vs Salon (~54 kWh/mois, ~11€/mois)
- **Causes :**
  - Exposition Nord
  - Simple vitrage
  - Sous toiture (déperdition++)
- **Actions :**
  - ✅ Rideaux épais installés 07/02/2026
  - 🟡 Protocole fermeture strict (à tester)
  - 🔴 Motorisation store envisagée (150-200€, ROI 18-24 mois)

#### **Cuisine Nord**
- **Action en cours :** 🟡 Rideaux épais (26.52€)

#### **Seuil décrochage climatisation**
- **Observation :** T°ext <8°C → Clims Nord quasi-continu
- **Recommandation :** Surveillance accrue périodes grand froid

### 7.3 Incohérences Nommage v1.5

**Exemples à corriger v2.0 :**

| Type | v1.5 (Actuel) | v2.0 (Cible) | Statut |
|:-----|:-------------|:-------------|:-------|
| ✅ Bon | `sensor.dut_clim_salon` | Conservé | OK |
| ⚠️ Moyen | `sensor.clim_rad_total_avg_watts_daily` | `sensor.heating_total_power_avg_daily` | Optionnel |
| ❌ Mauvais | `sensor.diag_poste_1_hygiene_quotidien` | `sensor.hygiene_daily_energy` | À changer |

### 7.4 Fichiers Monolithiques

**Problème :**
- `automations.yaml` contient TOUTES les automations → Risque maintenance

**Solution v2.0 :**
- Découpage par domaine :
  - `automations/heating/`
  - `automations/covers/`
  - `automations/monitoring/`
  - `automations/notifications/`

---

## 8. PROCÉDURES MAINTENANCE

### 8.1 Sauvegarde

**Fréquence recommandée :** Hebdomadaire (dimanche 03h00)

**État actuel v1.5 :**
- 🔴 **AUCUNE SAUVEGARDE AUTOMATISÉE**
- ✅ Export GitHub manuel (configuration.yaml, sensors/, etc.)

**Recommandations v2.0 :**
- ✅ Automation sauvegarde hebdomadaire
- ✅ Upload NAS/Cloud (Google Drive, Nextcloud)
- ✅ Rotation 4 dernières sauvegardes
- ✅ Copie USB mensuelle (stockage physique)

**Éléments à sauvegarder :**
```
/config/
├── configuration.yaml
├── secrets.yaml (chiffré)
├── automations/
├── sensors/
├── templates/
├── utility_meter/
├── dashboards/
└── .storage/ (intégrations UI)
```

### 8.2 Mise à Jour Home Assistant

**Fréquence :** Mensuelle (1er du mois)

**Procédure :**
1. ✅ Sauvegarde pré-MAJ complète
2. ✅ Lecture changelog HA (breaking changes)
3. ✅ Vérification compatibilité custom components
4. ✅ MAJ en heures creuses (nuit)
5. ✅ Tests post-MAJ :
   - Automations chauffage fonctionnelles
   - Logs 15min OK
   - Dashboards affichés
   - Intégrations actives
6. ✅ Rollback si problème critique

### 8.3 Vérification Mensuelle Capteurs

**Checklist :**
- [ ] Batteries TH/ouverture (<20% alerte)
- [ ] Connectivité Ecojoko/Linky (API)
- [ ] État prises connectées (online/offline)
- [ ] Logs erreurs Zigbee2MQTT
- [ ] Qualité signal WiFi clims

**Automation recommandée v2.0 :**
```yaml
# Notification batterie <20%
automation:
  - alias: "ALERTE - Batteries Faibles"
    trigger:
      - platform: numeric_state
        entity_id:
          - sensor.th_*_battery
          - sensor.contact_*_battery
        below: 20
    action:
      - service: notify.mobile_app_poco_x7_pro
        data:
          title: "🔋 Batterie Faible"
          message: "{{ trigger.to_state.name }}: {{ trigger.to_state.state }}%"
```

### 8.4 Maintenance Annuelle Physique

**Checklist :**
- [ ] Nettoyage filtres clims ×3
- [ ] Nettoyage grilles VMC
- [ ] Vérification joints fenêtres
- [ ] Test volets motorisés (monter/descendre)
- [ ] Nettoyage capteurs T° (poussière)
- [ ] Vérification alimentation Raspberry Pi

---

## 9. ROADMAP MIGRATION

### 9.1 Vue d'Ensemble

```
┌─────────────────────────────────────────────────────────────┐
│ PHASE 0 : Documentation        │ 22/02 - 08/03 │ 65% ✅     │
│ PHASE 1 : Stabilisation        │ 09/03 - 22/03 │ 15% 🔄     │
│ PHASE 2 : Refactoring          │ 23/03 - 03/05 │  0% ⏸️     │
│ PHASE 3 : Migration Matérielle │ 04/06 - 10/06 │  0% ⏸️     │
│ PHASE 4 : Optimisations        │ 11/06 - 22/08 │  0% ⏸️     │
└─────────────────────────────────────────────────────────────┘
```

### 9.2 Phase 0 : Documentation (22/02-08/03) - 🟡 65% EN COURS

**Objectifs :**
- [x] Cahier charges v1.0 (87 pages)
- [x] Cahier charges v1.2 (mise à jour session 22/02)
- [x] Tree structure v2.0
- [x] Configuration MQTT écoute
- [ ] Schéma architecture complet
- [x] Inventaire exhaustif équipements
- [x] Cartographie automations

**Livrables complétés :**
- ✅ `CAHIER_DES_CHARGES_Migration_HA_v1.2.md`
- ✅ `tree.txt` (structure /config/)
- ✅ `DASHBOARD_2026_02_22.yaml` (sauvegarde)
- ✅ `config_z2m_v1.5.yaml` (documentation)
- ✅ MQTT écoute fonctionnel (54 équipements)

**Statut :** 🟡 **EN COURS** (65% complété)

### 9.3 Phase 1 : Stabilisation (09/03-22/03) - 🔄 15% EN COURS

#### **Objectifs :**
- [x] Corriger logs DUT (BUG-001) ✅ **FAIT 22/02**
- [ ] Valider timer Sèche-Serviette (BUG-002)
- [ ] Ajouter tags G1-G4 (BUG-003)
- [x] Documenter entités v2.0 (noms Zigbee identiques v1.5) ✅
- [ ] Automation sauvegarde hebdo

#### **Livrables :**
- [x] `automation_diag_enregistrement_corrected.yaml` ✅
- [ ] Tests validation BUG-002 (timer 2h)
- [ ] Logs G1-G4 implémentés
- [ ] Script sauvegarde automatique

**Statut :** 🔄 **EN COURS** (15% complété)

### 9.4 Phase 2 : Refactoring (23/03-03/05) - ⏸️ NON DÉMARRÉ

#### **2.1 Restructuration (2 sem)**
- [ ] Découper `automations.yaml` par domaine
- [ ] Renommer templates séries 01-18
- [ ] Créer `packages/` (heating, lighting, energy)
- [ ] Validation syntaxe YAML

#### **2.2 Refonte Nommage (2 sem)**
- [ ] Appliquer standard `domain_location_function_metric_cycle`
- [ ] Créer alias compatibilité v1.5
- [ ] Migration progressive P3 → P2 → P1
- [ ] Tests unitaires par pôle

#### **2.3 Amélioration Monitoring (2 sem)**
- [ ] Dashboards par pièce (Lovelace)
- [ ] Graphiques ApexCharts avancés
- [ ] Alertes anomalies consommation
- [ ] Rapports hebdomadaires automatiques

**Statut :** ⏸️ **NON DÉMARRÉ** (0%)

### 9.5 Phase 3 : Migration Matérielle (04/06-10/06) - ⏸️ NON DÉMARRÉ

**Objectifs :**
- [ ] Décommissionner Mini-PC
- [ ] Consolidation Raspberry Pi 4 unique
- [ ] Optimisation performances HA
- [ ] Configuration sauvegarde NAS

**Fenêtre maintenance :** 1 semaine (juin 2026)

**Statut :** ⏸️ **NON DÉMARRÉ** (0%)

### 9.6 Phase 4 : Optimisations (11/06-22/08) - ⏸️ NON DÉMARRÉ

#### **4.1 Isolation Passive (2 sem)**
- [ ] Motorisation store Chambre (~200€)
- [ ] Joints fenêtres additionnels (~15€)
- [ ] Film isolant fenêtres Nord (~50€)
- [ ] Mesure impact DUT

#### **4.2 Machine Learning (4 sem)**
- [ ] Prédiction consommation (Prophet)
- [ ] Détection anomalies automatique
- [ ] Chauffage prédictif (météo + habitudes)
- [ ] Optimisation heures creuses

**Statut :** ⏸️ **NON DÉMARRÉ** (0%)

### 9.7 Roadmap Détaillée - Semaines 1-6

#### **SEMAINE 1 (23/02-01/03) : P3 Éclairage - Finalisation**
**Objectif :** Migration complète Pôle 3

**Actions :**
- [ ] Génération fichiers manquants :
  - `p3_02_templates_energie.yaml` (W→kWh)
- [ ] Copie fichiers dans v2.0
- [ ] Tests 24h entités P3
- [ ] Comparaison v1.5 vs v2.0 (±5%)
- [ ] Validation dashboard éclairage

**Livrables :**
- [ ] P3 100% fonctionnel v2.0
- [ ] Documentation validation P3

**Statut estimé :** 🔄 80% → 100%

---

#### **SEMAINE 2 (02/03-08/03) : P3 Validation + P2 Préparation**
**Objectif :** Tests 7j P3 + Début P2

**Actions :**
- [ ] Monitoring continu P3 (7 jours)
- [ ] Vérification utility meters (reset daily/monthly)
- [ ] Début migration P2 (Prises) :
  - Fichiers déjà présents à valider
  - Tests entités Zigbee prises

**Livrables :**
- [ ] Rapport validation P3 (7j)
- [ ] P2 préparé (50%)

**Statut estimé :** P3 100% validé ✅ / P2 50%

---

#### **SEMAINE 3 (09/03-15/03) : P2 Prises - Migration Complète**
**Objectif :** Migration Pôle 2

**Actions :**
- [ ] Finalisation fichiers P2
- [ ] Tests 24h entités P2
- [ ] Validation automations prises
- [ ] Comparaison consommation v1.5 vs v2.0

**Livrables :**
- [ ] P2 100% fonctionnel v2.0
- [ ] Documentation validation P2

**Statut estimé :** P2 100%

---

#### **SEMAINE 4 (16/03-22/03) : P2 Validation + P1 Préparation**
**Objectif :** Tests 7j P2 + Début P1

**Actions :**
- [ ] Monitoring continu P2 (7 jours)
- [ ] Préparation P1 (Chauffage) :
  - Génération fichiers manquants
  - Adaptation entités Zigbee

**Livrables :**
- [ ] Rapport validation P2 (7j)
- [ ] P1 préparé (30%)

**Statut estimé :** P2 100% validé ✅ / P1 30%

---

#### **SEMAINE 5 (23/03-29/03) : P1 Chauffage - Migration Phase 1**
**Objectif :** Migration sensors P1

**Actions :**
- [ ] Copie fichiers P1 sensors/
- [ ] Tests capteurs DUT/Perf/Avg
- [ ] Validation calculs thermiques
- [ ] Monitoring 48h

**Livrables :**
- [ ] P1 sensors opérationnels
- [ ] DUT complet (S/R/B/Sf/SS/C)

**Statut estimé :** P1 50%

---

#### **SEMAINE 6 (30/03-05/04) : P1 Chauffage - Migration Phase 2**
**Objectif :** Migration automations P1

**Actions :**
- [ ] Migration automations chauffage :
  - mode_day.yaml
  - mode_night.yaml
  - kitchen_timer.yaml
  - bathroom_dryer.yaml
- [ ] Tests mode écoute (v2.0 voit états mais ne contrôle pas)
- [ ] Validation logique thermique
- [ ] Tests 7 jours monitoring

**Livrables :**
- [ ] P1 100% fonctionnel v2.0
- [ ] Rapport validation P1

**Statut estimé :** P1 100%

---

### 9.8 Planning Gantt Visuel

```
Février 2026          Mars 2026              Avril 2026
22|24|26|28|01|03|05|07|09|11|13|15|17|19|21|23|25|27|29|31|02|04|
══════════════════════════════════════════════════════════════════
Phase 0 ████████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 65%
P3 Éclairage ░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 80%
P2 Prises    ░░░░░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░  0%
P1 Chauffage ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████░░  0%
Phase 2      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  0%

Légende: █ Terminé  ▓ En cours  ░ À faire
```

---

## 10. ANNEXES TECHNIQUES

### 10.1 Template Nommage v2.0 (Optionnel)

**Convention :**
```
{domain}_{location}_{function}_{metric}_{cycle}
```

**Domaines :**
- heating, lighting, energy, climate, air_quality, cover, switch, sensor, binary_sensor

**Locations :**
- livingroom, kitchen, office, bathroom, bedroom, entrance, hallway, outdoor

**Functions :**
- total, average, runtime, status, power, temperature, humidity, contact

**Metrics :**
- kwh, watts, hours, celsius, percent, count, state

**Cycles :**
- daily, monthly, yearly, realtime

**Exemples :**
```yaml
# Chauffage
sensor.heating_total_power_avg_daily
sensor.heating_livingroom_runtime_hours_daily
sensor.heating_bedroom_energy_kwh_monthly

# Éclairage
sensor.lighting_kitchen_power_watts_realtime
sensor.lighting_office_energy_kwh_daily

# Climat
sensor.climate_office_temperature_celsius_realtime
sensor.climate_bathroom_humidity_percent_realtime

# Énergie
sensor.energy_plug_fridge_power_watts_realtime
sensor.energy_plug_fridge_total_kwh_yearly
```

### 10.2 Structure Fichiers Cible v2.0

```yaml
/config/
├── configuration.yaml (minimaliste)
│   # Includes uniquement
│   sensor: !include_dir_merge_list sensors/
│   template: !include_dir_merge_list templates/
│   utility_meter: !include_dir_merge_named utility_meter/
│   automation: !include_dir_merge_list automations/
│
├── automations/
│   ├── heating/
│   │   ├── mode_day.yaml
│   │   ├── mode_night.yaml
│   │   ├── kitchen_timer.yaml
│   │   └── bathroom_dryer.yaml
│   ├── covers/
│   │   ├── livingroom_automation.yaml
│   │   └── office_automation.yaml
│   ├── monitoring/
│   │   └── energy_log_15min.yaml
│   └── notifications/
│       ├── battery_alerts.yaml
│       └── window_open_heating.yaml
│
├── sensors/
│   ├── P1_clim_chauffage/
│   │   ├── p1_0_sensors_clim_rad.yaml
│   │   ├── p1_1_sensors_dut.yaml
│   │   ├── p1_2_sensors_Perf.yaml
│   │   └── p1_3_sensors_moy_24h.yaml
│   ├── P2_prise/
│   │   └── P2_kWh.yaml
│   ├── P3_eclairage/
│   │   ├── P3_kWh_1_UNITE.yaml
│   │   ├── P3_kWh_2_ZONE.yaml
│   │   └── P3_kWh_3_TOTAL.yaml
│   └── system/
│       ├── blitzortung.yaml
│       ├── mini_pc.yaml (à supprimer Phase 3)
│       └── pm25_tcov.yaml
│
├── templates/
│   ├── P1_/
│   │   └── P1_AVG/
│   │       └── P1_avg.yaml
│   ├── P2_prises/
│   │   └── P2_AVG/
│   │       └── P2_avg.yaml
│   ├── P3_eclairage/
│   │   ├── P3_01_somme_par_piece.yaml
│   │   └── P3_02_energie.yaml
│   ├── meteo/
│   │   ├── 01_1_alertes.yaml
│   │   ├── 01_2_foudre.yaml
│   │   ├── 01_3_vent.yaml
│   │   └── 01_4_tendances.yaml
│   ├── reseau/
│   │   ├── 02_1_speedtest.yaml
│   │   └── 06_1_wifi.yaml
│   ├── energy/
│   │   ├── 11_1_ecojoko.yaml
│   │   ├── 11_2_linky.yaml
│   │   ├── 17_1_diag_daily.yaml
│   │   └── 17_2_diag_monthly.yaml
│   ├── air_quality/
│   │   └── 10_1_ppb.yaml
│   ├── time/
│   │   ├── 13_1_temporel.yaml
│   │   └── 15_1_jour_nuit.yaml
│   └── generales/
│       └── 18_1_moyennes.yaml
│
├── utility_meter/
│   ├── P1_clim_chauffage/
│   │   └── P1_UM_AMHQ.yaml
│   ├── P2_prise/
│   │   └── P2_UM_AMHQ.yaml
│   └── P3_eclairage/
│       ├── P3_UM_AMHQ_1_UNITE.yaml
│       ├── P3_UM_AMHQ_2_ZONE.yaml
│       └── P3_UM_AMHQ_3_TOTAL.yaml
│
├── packages/ (Phase 2)
│   ├── heating.yaml
│   ├── lighting.yaml
│   └── energy.yaml
│
└── dashboards/
    ├── main.yaml
    ├── energy.yaml
    └── rooms/
        ├── livingroom.yaml
        ├── kitchen.yaml
        ├── office.yaml
        └── bedroom.yaml
```

### 10.3 Checklist Migration Complète

#### **Pré-migration :**
- [x] Sauvegarde complète v1.5 ✅
- [x] Export GitHub configuration ✅
- [x] Documentation inventaire ✅
- [ ] Tests automations critiques v1.5
- [x] Installation v2.0 propre ✅
- [x] MQTT écoute configuré ✅

#### **Migration (par pôle) :**
- [ ] P3 Éclairage (Semaine 1-2)
  - [x] Fichiers sensors/ ✅
  - [x] Fichiers templates/ (partiel) 🔄
  - [x] Fichiers utility_meter/ ✅
  - [ ] Tests unitaires
  - [ ] Validation 7j
- [ ] P2 Prises (Semaine 3)
  - [x] Fichiers sensors/ ✅
  - [x] Fichiers templates/ ✅
  - [x] Fichiers utility_meter/ ✅
  - [ ] Tests unitaires
  - [ ] Validation 7j
- [ ] P1 Chauffage (Semaine 4-6)
  - [ ] Fichiers sensors/
  - [ ] Fichiers templates/
  - [x] Fichiers utility_meter/ ✅
  - [ ] Automations/
  - [ ] Tests unitaires
  - [ ] Validation 7j

#### **Post-migration :**
- [ ] Validation complète v2.0 (7j tous pôles)
- [ ] Comparaison conso v1.5 vs v2.0 (±5%)
- [ ] Migration Zigbee physique (dongle)
- [ ] Arrêt v1.5
- [ ] Démarrage v2.0 production unique
- [ ] Tests 48h surveillance rapprochée
- [ ] Documentation v2.0 finale
- [ ] Archivage v1.5

### 10.4 Outils Recommandés

**Développement :**
- VS Code + Extension Home Assistant
- YAML Lint (validation syntaxe)
- Jinja2 Tester (templates)

**Schémas :**
- Draw.io (architecture)
- Mermaid (diagrammes)

**Monitoring :**
- Grafana + InfluxDB (graphiques avancés)
- Node-RED (optionnel, automations visuelles)

**Backup :**
- Restic (snapshots incrémentaux)
- Rclone (sync cloud)

### 10.5 Configuration MQTT Mode Écoute (Détail)

**Mosquitto Broker v1.5 - Configuration complète :**
```yaml
# Modules complémentaires > Mosquitto Broker > Configuration
logins:
  - username: homeassistant
    password: [mdp_principal_secret]
  - username: mqtt
    password: mqtt
    
customize:
  active: false
  folder: mosquitto
  
certfile: fullchain.pem
keyfile: privkey.pem
require_certificate: false
anonymous: false
```

**MQTT Client v2.0 - Configuration UI :**
```
Paramètres > Appareils et Services > MQTT
+ AJOUTER UNE INTÉGRATION > MQTT

Courtier: 192.168.1.96
Port: 1883
Nom d'utilisateur: mqtt
Mot de passe: mqtt
ID client: (vide - auto-généré)
Keep Alive: 60

Options avancées:
  Utiliser certificat client: ❌
  Validation certificat courtier: Désactivé
  Ignorer validation certificat: ✅
  Protocole MQTT: 3.1.1
  Transport MQTT: TCP

Découverte: ✅ Activée
Préfixe découverte: homeassistant
```

**Validation connexion :**
```yaml
# Outils développement > MQTT > Écouter un topic
Topic: zigbee2mqtt/#
QoS: 0

# Résultat attendu (temps réel):
# zigbee2mqtt/bridge/state {"state":"online"}
# zigbee2mqtt/Th Bureau {"battery":100,"temperature":20.8,...}
# zigbee2mqtt/prise bureau pc (IKEA) {"power":28.5,"energy":245.67,...}
# [... messages continus 54 équipements ...]
```

### 10.6 Fichiers Manquants à Générer

**Pôle 3 (Éclairage) :**
```
templates/P3_eclairage/
  └── P3_02_energie.yaml (conversion W→kWh) ⚠️ À CRÉER
```

**Pôle 1 (Chauffage) :**
```
sensors/P1_clim_chauffage/
  ├── p1_0_sensors_clim_rad.yaml (déjà uploadé, à copier)
  ├── p1_1_sensors_dut.yaml (déjà uploadé, à copier)
  ├── p1_2_sensors_Perf.yaml (déjà uploadé, à copier)
  └── p1_3_sensors_moy_24h.yaml (déjà uploadé, à copier)
```

**Templates généraux :**
```
templates/generales/
  └── 18_1_Moyenne_daily_monthly.yaml (déjà uploadé, à copier)
```

---

## 📊 MÉTRIQUES AVANCEMENT

### Avancement Global : 40%

**Par phase :**
- Phase 0 (Documentation) : 65% ✅
- Phase 1 (Stabilisation) : 15% 🔄
- Phase 2 (Refactoring) : 0% ⏸️
- Phase 3 (Migration Matérielle) : 0% ⏸️
- Phase 4 (Optimisations) : 0% ⏸️

**Par pôle (v2.0) :**
- P3 Éclairage : 80% 🔄 (structure OK, templates énergie manquants)
- P2 Prises : 30% 🔄 (fichiers présents, validation à faire)
- P1 Chauffage : 20% 🔄 (fichiers uploadés, à copier/valider)

**Infrastructure v2.0 :**
- Installation HA : 100% ✅
- Cartes HACS : 100% ✅ (19/19)
- Intégrations : 47% 🔄 (8/17)
- MQTT écoute : 100% ✅
- Structure fichiers : 75% ✅

---

## 📝 CHANGELOG

### Version 1.2 (22/02/2026)
- ✅ Ajout section 3.2 Architecture v2.0 mode MQTT écoute
- ✅ Ajout section 3.4 Configuration MQTT détaillée
- ✅ Mise à jour section 5 Inventaire (noms entités Zigbee v2.0 identiques v1.5)
- ✅ Mise à jour section 7.1 Bugs (BUG-001 résolu)
- ✅ Ajout section 9.7 Roadmap détaillée semaines 1-6
- ✅ Ajout section 10.5 Configuration MQTT mode écoute
- ✅ Ajout section 10.6 Fichiers manquants à générer
- ✅ Mise à jour métriques avancement (Phase 0: 65%, P3: 80%, Infrastructure: 75%)
- ✅ Ajout session 22/02/2026 dans résumé exécutif

### Version 1.1 (Non publiée)
- Ajout détails migration P3
- Structuration fichiers v2.0
- Cartographie automations

### Version 1.0 (22/02/2026)
- Création document initial
- 87 pages
- 10 sections complètes

---

## 🎯 PROCHAINES ACTIONS

### **Urgent (Cette semaine - 23-29/02) :**
1. ✅ Mettre à jour Cahier des Charges v1.2 ✅ **FAIT**
2. 🔄 Générer fichier `P3_02_energie.yaml` (conversion W→kWh)
3. 🔄 Copier fichiers P1 dans v2.0
4. 🔄 Tests validation P3 (24h)

### **Important (Semaine prochaine - 02-08/03) :**
5. Validation P3 complète (7 jours)
6. Début migration P2 (Prises)
7. Tests entités Zigbee prises
8. Schéma architecture complet (Draw.io)

### **Moyen terme (Mars 2026) :**
9. Finalisation P2 (Semaine 3)
10. Début P1 Chauffage (Semaine 4-5)
11. Tests 7j par pôle
12. Documentation technique enrichie

---

**FIN DU DOCUMENT**

*Cahier des Charges Migration Home Assistant v1.5 → v2.0*  
*Version 1.2 - 22 février 2026*  
*Eric - Technicien Maintenance SNEF*