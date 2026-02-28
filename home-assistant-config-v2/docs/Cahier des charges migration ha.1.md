# 📋 CAHIER DES CHARGES
## MIGRATION HOME ASSISTANT v1.5 → v2.0
### Documentation de l'Existant & Préparation Migration

---

**Version :** 1.0  
**Date :** 2026-02-22  
**Auteur :** Eric (BerrySwann)  
**Statut :** 🟡 En cours de rédaction

---

## 📑 TABLE DES MATIÈRES

1. [Contexte & Objectifs](#1-contexte--objectifs)
2. [Périmètre du Projet](#2-périmètre-du-projet)
3. [Architecture Actuelle](#3-architecture-actuelle)
4. [Glossaire & Conventions](#4-glossaire--conventions)
5. [Inventaire des Équipements](#5-inventaire-des-équipements)
6. [Cartographie des Automations Critiques](#6-cartographie-des-automations-critiques)
7. [Points de Vigilance & Bugs Connus](#7-points-de-vigilance--bugs-connus)
8. [Procédures de Maintenance](#8-procédures-de-maintenance)
9. [Roadmap de Migration](#9-roadmap-de-migration)
10. [Annexes Techniques](#10-annexes-techniques)

---

## 1️⃣ CONTEXTE & OBJECTIFS

### 1.1 Historique

**Système actuel :**
- **Durée de vie :** 1 an et demi (depuis ~août 2024)
- **Évolution :** Organique, par ajouts successifs
- **État :** Fonctionnel mais nécessite refactoring

**Problèmes identifiés :**
- 🔴 Nommage incohérent (ex: `sensor.clim_rad_total_avg_watts_daily` → nom opaque)
- 🟡 Code legacy ("syndrome P4" : certaines parties obscures)
- 🟡 Documentation dispersée (GitHub + notes + mémoire)
- 🟢 Fonctionnalités éprouvées (chauffage, monitoring énergie)

### 1.2 Objectifs de la Documentation

**Objectif principal :**  
> Documenter exhaustivement l'installation actuelle pour permettre une migration maîtrisée vers un système v2.0 optimisé, sans perte de fonctionnalité.

**Objectifs secondaires :**
1. ✅ Créer un **référentiel technique** (schémas, conventions)
2. ✅ Identifier les **automations critiques** à conserver
3. ✅ Lister les **bugs connus** et leurs workarounds
4. ✅ Établir un **glossaire** pour futurs contributeurs
5. ✅ Préparer la **roadmap de migration**

### 1.3 Livrables Attendus

| Livrable | Format | Statut |
|:---------|:-------|:-------|
| **Schéma Architecture Actuelle** | Draw.io / Mermaid | 🔴 À faire |
| **Glossaire des Conventions** | Markdown | 🟡 En cours |
| **Inventaire Équipements** | Tableau Excel/CSV | 🔴 À faire |
| **Cartographie Automations** | Markdown + YAML | 🔴 À faire |
| **Procédures Maintenance** | Markdown | 🔴 À faire |
| **Plan de Migration** | Gantt / Roadmap | 🔴 À faire |

---

## 2️⃣ PÉRIMÈTRE DU PROJET

### 2.1 Inclus dans le Périmètre

**Équipements domotiques :**
- ✅ Climatiseurs (×3 : Salon, Bureau, Chambre)
- ✅ Chauffage électrique (Radiateur Cuisine, Soufflant SDB, Sèche-Serviette SDB)
- ✅ Volets motorisés (×2 : Salon, Bureau)
- ✅ Éclairage Philips Hue + Sonoff (30+ ampoules)
- ✅ Prises connectées (10+ équipements)
- ✅ Capteurs (Température ×6, Qualité d'air ×3, Ouverture fenêtres)

**Fonctionnalités logicielles :**
- ✅ Monitoring énergétique (Logs 15min, Ecojoko, Linky)
- ✅ Automations chauffage (Jour/Nuit, Présence, Saisons)
- ✅ Gestion volets (Isolation, Lumière, Protection solaire)
- ✅ Notifications (Poco X7 Pro + Xiaomi Watch Lite)
- ✅ Dashboards Lovelace (Bubble Card, ApexCharts, Mushroom)

**Infrastructure :**
- ✅ Raspberry Pi 4 (Home Assistant OS)
- ✅ Mini-PC (ancien serveur, à décommissionner)
- ✅ Intégrations externes (MyElectricalData, Météo France, Speedtest)

### 2.2 Exclus du Périmètre

**Non traité dans cette phase :**
- ❌ Caméras de surveillance (si existantes)
- ❌ Intégration domotique professionnelle (sites UCA/SNEF)
- ❌ Optimisation réseau Wi-Fi (couverture, mesh)
- ❌ Sauvegardes automatisées (sera traité en phase 2)

---

## 3️⃣ ARCHITECTURE ACTUELLE

### 3.1 Vue d'Ensemble

```
┌─────────────────────────────────────────────────────────────────┐
│                    HOME ASSISTANT (RPi4)                        │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  CHAUFFAGE   │  │  ÉCLAIRAGE   │  │   ÉNERGIE    │         │
│  │   (Pôle 1)   │  │   (Pôle 3)   │  │  (Monitoring)│         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│         │                  │                  │                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │    PRISES    │  │    VOLETS    │  │ NOTIFICATIONS│         │
│  │   (Pôle 2)   │  │  (Série 08)  │  │   (Série 03) │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└─────────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
   ┌─────────┐         ┌─────────┐        ┌─────────┐
   │ ECOJOKO │         │  LINKY  │        │  MÉTÉO  │
   │ (Local) │         │  (API)  │        │ FRANCE  │
   └─────────┘         └─────────┘        └─────────┘
```

### 3.2 Structure des Fichiers

**Organisation actuelle :**

```
/config/
├── configuration.yaml          # Config principale
├── automations.yaml            # Toutes les automations
├── scripts.yaml                # Scripts réutilisables
├── secrets.yaml                # Clés API, tokens
├── sensors/                    # Capteurs par pôle
│   ├── p1_0_sensors_clim_rad.yaml
│   ├── p1_1_sensors - dut.yaml
│   ├── p1_2_sensors - Perf.yaml
│   ├── p1_3_sensors_moy_24h.yaml
│   ├── p2_sensors_ prises.yaml
│   ├── p3_sensors_lumieres.yaml
│   └── sensors - pm25 et tcov.yaml
├── templates/                  # Templates sensors
│   ├── 01_1_meteo_alertes_card.yaml
│   ├── 03_05_clim_logique_system_autom.yaml
│   ├── 17_1_diag_conso_jour_en_cours.yaml
│   └── [18 séries au total]
├── utility_meter.yaml          # Compteurs journaliers/mensuels
└── [autres fichiers config]
```

**Points critiques :**
- ⚠️ `automations.yaml` monolithique (200+ lignes)
- ⚠️ Nommage des templates incohérent (numéros séries)
- ✅ Séparation sensors par pôle (bonne pratique)

### 3.3 Flux de Données Énergétiques

**Pipeline de monitoring :**

```
[Écojoko] ──┐
            │
[Prises]────┼──→ [Sensors kWh] ──→ [Utility Meters] ──→ [Templates]
            │         ↓                    ↓                  ↓
[Linky] ────┘    Daily/Monthly        Diag Conso      Notifications
                                       (15min log)      (Poco X7 Pro)
```

**Capteurs clés :**
- `sensor.diag_poste_X_quotidien` (X = 1 à 7)
- `sensor.clim_rad_total_avg_watts_daily` (le fameux "Avg P4")
- `sensor.dut_clim_salon/bureau/chambre`
- `sensor.dut_radiateur_cuisine`
- `sensor.dut_sdb_soufflant` ⚠️ (existe mais pas dans logs)
- `sensor.dut_sdb_seche_serviettes` ⚠️ (existe mais pas dans logs)

---

## 4️⃣ GLOSSAIRE & CONVENTIONS

### 4.1 Abréviations Standards

| Abréviation | Signification | Contexte |
|:------------|:--------------|:---------|
| **HA** | Home Assistant | Logiciel domotique |
| **DUT** | Durée d'Utilisation Totale | Temps de fonctionnement cumulé (heures) |
| **kWh** | Kilowatt-heure | Énergie consommée |
| **W** | Watt | Puissance instantanée |
| **Avg** | Average (Moyenne) | Puissance moyenne depuis minuit |
| **T̄i** | Température Intérieure moyenne | Moyenne des sondes pièces |
| **Ext** | Température Extérieure | Sonde balcon Nord |
| **SDB** | Salle de Bain | Pièce 8 |
| **Sf** | Soufflant | Chauffage SDB 2000W |
| **SS** | Sèche-Serviette | Chauffage SDB 150W |

### 4.2 Convention de Nommage "Pôles"

**Système actuel (logs `diag_conso_elec.txt`) :**

| Pôle | Nom complet | Équipements | Colonne log |
|:-----|:------------|:------------|:------------|
| **P1** | Hygiène & Linge | Lave-Linge, Lave-Vaisselle | `Hyg` |
| **P2** | Cuisson | Four, Micro-ondes, Air-Fryer, Plaques | `Cuis` |
| **P3** | Froid | Frigo, Congélateur | `Froid` |
| **P4** | Chauffage & Clim | Clims ×3, Radiateur, Soufflant, Sèche-Serviette | `Chauff` |
| **P5** | Multimédia | PC ×2, TV, Mini-PC HA | `Multi` |
| **P6** | Éclairage | Hue, Sonoff | `Lum` |
| **P7** | Autres | Standby, Ecojoko, Capteurs | `Autres` |

**P4 = Position 4 dans les logs** ✅  
(Origine du nom `sensor.clim_rad_total_avg_watts_daily` → "Avg P4")

### 4.3 Convention DUT (Durée d'Utilisation)

**Format actuel (logs avant 22/02/2026) :**
```
DUT S/R/B/C:3.8/0.2/11.2/14.9
```

**Format futur (à partir de 22/02/2026) :**
```
DUT S/R/B/Sf/SS/C:3.8/0.2/11.2/0.0/0.0/14.9
```

**Légende :**
- **S** = Salon (Clim Sud)
- **R** = Radiateur Cuisine
- **B** = Bureau (Clim Nord)
- **Sf** = Soufflant SDB ⚡ NOUVEAU
- **SS** = Sèche-Serviette SDB ⚡ NOUVEAU
- **C** = Chambre (Clim Nord)

### 4.4 Convention "Séries" (Templates)

**Système de numérotation actuel :**

| Série | Fonction | Exemples |
|:------|:---------|:---------|
| **01** | Météo | `01_1_meteo_alertes_card.yaml` |
| **02** | Réseau | `02_1_reseau_speedtest_card.yaml` |
| **03** | Climat/Chauffage | `03_05_clim_logique_system_autom.yaml` |
| **04** | Éclairage | `04_1_energie_eclairage_card.yaml` |
| **05** | Mises à jour | `05_1_updates_ha_system_vignette.yaml` |
| **06** | Wi-Fi/Cellular | `06_1_phones_wifi_cellular_card_autom.yaml` |
| **07** | Fenêtres | `07_1_nb_fenetre_ouvert_ferme_autom.yaml` |
| **08** | Stores/Volets | `08_1_stores_etats_vignette_card.yaml` |
| **09** | Standby | `09_1_sensor.all_standby_current.yaml` |
| **10** | Qualité Air | `10_1_air_quality_ppb.yaml` |
| **11** | Ecojoko/Linky | `11_1_ecojoko_kwh_jrs_moins_1.yaml` |
| **12** | Mini-PC | `12_1_sonde_température_mini-pc.yaml` |
| **13** | Temporel | `13_1_Capteur temporel.yaml` |
| **14** | Interrupteurs | `14_1_inter_sdb.yaml` |
| **15** | Jour/Nuit | `15_1_jour_on_7h30_21h.yaml` |
| **16** | Icônes Saisons | `16_1_icon ete_hivers.yaml` |
| **17** | Diagnostics | `17_1_diag_conso_jour_en_cours.yaml` |
| **18** | Moyennes | `18_1_Moyenne_daily_monthly.yaml` |

⚠️ **Problème identifié :** Pas de standard clair entre `_` et espace dans les noms.

### 4.5 Groupes de Présence (G1-G4)

**Logique des automations volets/chauffage :**

| Groupe | Présence | Comportement volets | Comportement chauffage |
|:-------|:---------|:--------------------|:-----------------------|
| **G1** | Absence (Wifi + Cell OFF) | Fermés (isolation) | Mode Absence (17-19°C) |
| **G2** | Mamour seule | Ouverts (lumière) | Mode Confort (20-21°C) |
| **G3** | Eric seul | Fermés si T<17°C | Mode Confort (20-21°C) |
| **G4** | Les deux | Ouverts (lumière) | Mode Confort (20-21°C) |

**Capteurs de détection :**
- `device_tracker.poco_x7_pro_wifi`
- `device_tracker.poco_x7_pro_cell`
- `device_tracker.mamour_phone_wifi` (à vérifier)
- `device_tracker.mamour_phone_cell` (à vérifier)

---

## 5️⃣ INVENTAIRE DES ÉQUIPEMENTS

### 5.1 Chauffage & Climatisation (Pôle 1)

#### Pièce 4. SALON (Sud, 25.88 m²)

| Équipement | Marque/Modèle | Puissance | Entité HA | DUT | État |
|:-----------|:--------------|:----------|:----------|:----|:-----|
| Split mural | [À documenter] | ~2000W | `climate.clim_salon_entree` | `sensor.dut_clim_salon` | ✅ Fonctionnel |
| Volet motorisé | [À documenter] | - | `cover.store_salon` | - | ✅ Fonctionnel |

**Automations liées :**
- Ouverture/Fermeture selon G1/G2/G3/G4
- Protection solaire (>34°C)
- Apports solaires (15h → coucher)

#### Pièce 5. CUISINE (Nord, 10.59 m²)

| Équipement | Marque/Modèle | Puissance | Entité HA | DUT | État |
|:-----------|:--------------|:----------|:----------|:----|:-----|
| Radiateur bain d'huile | [À documenter] | ~1500W | `switch.radiateur_cuisine` | `sensor.dut_radiateur_cuisine` | ✅ Fonctionnel |

**Automations liées :**
- Timer matin semaine : 04h45 → 07h00
- Timer matin week-end : 05h45 → 08h00
- Thermostat virtuel : <19.9°C ON / >20.5°C OFF

#### Pièce 7. BUREAU (Nord, 10.55 m²)

| Équipement | Marque/Modèle | Puissance | Entité HA | DUT | État |
|:-----------|:--------------|:----------|:----------|:----|:-----|
| Split mural | [À documenter] | ~2000W | `climate.clim_bureau` | `sensor.dut_clim_bureau` | ✅ Fonctionnel |
| Volet motorisé | [À documenter] | - | `cover.store_bureau` | - | ✅ Fonctionnel |

**Automations liées :**
- Ouverture uniquement si T° Ext [18-25°C]
- Fermé sinon (isolation)
- Rideaux épais installés (22/02/2026)

#### Pièce 8. SALLE DE BAIN (Interne, 3.13 m²)

| Équipement | Marque/Modèle | Puissance | Entité HA | DUT | État |
|:-----------|:--------------|:----------|:----------|:----|:-----|
| Soufflant | [À documenter] | 2×1000W | `climate.soufflant_sdb` | `sensor.dut_sdb_soufflant` | ✅ Fonctionnel |
| Sèche-serviette | [À documenter] | 150W | `climate.seche_serviette_sdb` | `sensor.dut_sdb_seche_serviettes` | ⚠️ Timer 2h à valider |

**Automations liées :**
- Soufflant : OFF si >23°C
- Sèche-serviette : Timer 2h après détection >50W

#### Pièce 9. CHAMBRE (Nord, 11.26 m²)

| Équipement | Marque/Modèle | Puissance | Entité HA | DUT | État |
|:-----------|:--------------|:----------|:----------|:----|:-----|
| Split mural | [À documenter] | ~2000W | `climate.clim_chambre` | `sensor.dut_clim_chambre` | ✅ Fonctionnel |
| Store manuel | - | - | - | - | ⚠️ Gestion manuelle (point faible) |

**Travaux réalisés :**
- Rideaux épais installés (07/02/2026, 26.52€)

**Problème identifié :**
- DUT Chambre élevé (3.9× vs Salon)
- Absence automation store (oublis de fermeture nocturne)

### 5.2 Prises Connectées (Pôle 2)

#### Pièce 1. ENTRÉE

| Équipement | Marque/Modèle | Entité HA | État |
|:-----------|:--------------|:----------|:-----|
| Box Internet | [À documenter] | `switch.box_internet_entree` | ✅ |
| Horloge | [À documenter] | `switch.horloge_entree` | ✅ |

#### Pièce 4. SALON

| Équipement | Marque/Modèle | Entité HA | État |
|:-----------|:--------------|:----------|:-----|
| PC Fixe Gégé | [À documenter] | `switch.pc_s_gege_salon` | ✅ |
| Chargeur | [À documenter] | `switch.salon_chargeur_salon` | ✅ |

#### Pièce 5. CUISINE

| Équipement | Marque/Modèle | Entité HA | État |
|:-----------|:--------------|:----------|:-----|
| Micro-ondes | [À documenter] | `switch.micro_ondes_cuisine` | ✅ |
| Lave-linge | [À documenter] | `switch.lave_linge_cuisine` | ✅ |
| Lave-vaisselle | [À documenter] | `switch.lave_vaisselle_cuisine` | ✅ |
| Air-fryer | [À documenter] | `switch.airfryer_cuisine` | ✅ |
| Four + Plaques | [À documenter] | `switch.four_plaque_cuisine` | ✅ |
| Frigo | [À documenter] | `switch.frigo_cuisine` | ✅ |
| Congélateur | [À documenter] | `switch.congel_cuisine` | ✅ |

#### Pièce 7. BUREAU

| Équipement | Marque/Modèle | Entité HA | État |
|:-----------|:--------------|:----------|:-----|
| PC Bureau | [À documenter] | `switch.bureau_pc` | ✅ |
| Fer à repasser | [À documenter] | `switch.fer_a_repasser_bureau` | ✅ |

#### Pièce 9. CHAMBRE

| Équipement | Marque/Modèle | Entité HA | État |
|:-----------|:--------------|:----------|:-----|
| Tête de lit | [À documenter] | `switch.tete_de_lit_chambre` | ✅ |
| TV | [À documenter] | `switch.tv_chambre` | ✅ |

### 5.3 Éclairage (Pôle 3)

**Total : ~30 ampoules Philips Hue + Sonoff**

#### Détail par pièce (à compléter)

| Pièce | Type | Quantité | Zones logiques |
|:------|:-----|:---------|:---------------|
| 1. ENTRÉE | Hue White | 1 | - |
| 4. SALON | Hue White, Ambiance, Color | 5 | Table (5×) |
| 5. CUISINE | Hue White | 1 | - |
| 6. COULOIR | Hue White | 1 | - |
| 7. BUREAU | Play, Hue White | 5 | Play (3×), White (2×) |
| 8. SDB | Sonoff Miroir, Hue White | 2 | - |
| 9. CHAMBRE | Hue White, Color Zone | 4 | White (2×), Color Zone (2×) |

**Zones logiques (Pôle 3 spécifique) :**
- `sensor.eclairage_salon_5_*` (5 ampoules)
- `sensor.eclairage_appart_3_*` (Entrée+Cuisine+Couloir)
- `sensor.eclairage_bureau_5_*` (5 ampoules)
- `sensor.eclairage_sdb_2_*` (2 ampoules)
- `sensor.eclairage_chambre_4_*` (4 ampoules)

### 5.4 Capteurs & Monitoring

#### Température & Humidité

| Capteur | Emplacement | Entité HA | État |
|:--------|:------------|:----------|:-----|
| TH Balcon Nord | Extérieur Nord | `sensor.th_balcon_nord_temperature` | ✅ |
| TH Salon | Pièce 4 | `sensor.th_salon_temperature` | ✅ |
| TH Cuisine | Pièce 5 | [À documenter] | ✅ |
| TH Bureau | Pièce 7 | [À documenter] | ✅ |
| TH SDB | Pièce 8 | [À documenter] | ✅ |
| TH Chambre | Pièce 9 | [À documenter] | ✅ |

**Capteur calculé :**
- `sensor.temperature_moyenne_interieure` (moyenne des 5 pièces)

#### Qualité de l'Air

| Capteur | Emplacement | Paramètres | Entité HA | État |
|:--------|:------------|:-----------|:----------|:-----|
| PM2.5 + tCOV | Salon | Particules fines, COV totaux | `sensor.pm25_salon`, `sensor.tcov_salon` | ✅ |
| PM2.5 + tCOV | Bureau | Particules fines, COV totaux | `sensor.pm25_bureau`, `sensor.tcov_bureau` | ✅ |
| PM2.5 + tCOV | Chambre | Particules fines, COV totaux | `sensor.pm25_chambre`, `sensor.tcov_chambre` | ✅ |

#### Énergie

| Capteur | Type | Entité HA | État |
|:--------|:-----|:----------|:-----|
| Ecojoko | Compteur temps réel | `sensor.ecojoko_*` | ✅ |
| Linky (MyElectricalData) | API Enedis | `sensor.linky_*` | ✅ |
| Prises connectées | Mesure individuelle | `sensor.*_power`, `sensor.*_energy` | ✅ |

#### Ouverture Fenêtres

| Capteur | Emplacement | Entité HA | État |
|:--------|:------------|:----------|:-----|
| Contact Salon | Fenêtre Sud | [À documenter] | ✅ |
| Contact Bureau | Fenêtre Nord | [À documenter] | ✅ |
| Contact Chambre | Fenêtre Nord | [À documenter] | ✅ |

**Capteur calculé :**
- `sensor.nb_fenetres_ouvertes` (compteur global)

---

## 6️⃣ CARTOGRAPHIE DES AUTOMATIONS CRITIQUES

### 6.1 Chauffage — Mode Jour (07h30-21h00)

**Fichier source :** `templates/03_07_automation_message_clim_7h30_21h.yaml`

**Déclencheur :**
- Timer : 07h30

**Conditions :**
- Jour de la semaine (L-D)

**Actions :**
1. Activation mode "Jour" sur toutes les clims
2. Logique de présence (G1/G2/G3/G4)
3. Vérification état fenêtres
4. Ajustement température selon T° ext

**Criticité :** 🔴 HAUTE (confort quotidien)

**Bugs connus :** Aucun

**Dépendances :**
- `sensor.temperature_moyenne_interieure`
- `sensor.th_balcon_nord_temperature`
- `input_boolean.mode_jour` (à vérifier si existe)

### 6.2 Chauffage — Mode Nuit (21h00-07h30)

**Fichier source :** `templates/03_08_automation message clim 21h 7h30.yaml`

**Déclencheur :**
- Timer : 21h00

**Conditions :**
- Jour de la semaine (L-D)

**Actions :**
1. Activation mode "Nuit" sur toutes les clims
2. Réduction température (consignes nuit)
3. Notification envoyée

**Criticité :** 🔴 HAUTE (économies d'énergie)

**Bugs connus :** Aucun

### 6.3 Radiateur Cuisine — Timer Matin

**Fichier source :** `automations.yaml` (à identifier ligne exacte)

**Déclencheur :**
- Semaine (L-J) : 04h45
- Week-end (V-D) : 05h45

**Conditions :**
- T° Cuisine < 19.9°C

**Actions :**
1. Activation radiateur
2. Thermostat virtuel actif
3. Arrêt forcé à 07h00 (semaine) / 08h00 (week-end)

**Criticité :** 🟡 MOYENNE (confort matinal)

**Bugs connus :** Aucun (validé dans audit 22/02)

**Statut validation :** ✅ CONFORME

### 6.4 Sèche-Serviette SDB — Timer 2h

**Fichier source :** `automations.yaml` (à identifier)

**Déclencheur :**
- Détection consommation >50W

**Conditions :**
- État sèche-serviette = "Heat"

**Actions :**
1. Démarrage timer 2h
2. Arrêt automatique après 2h
3. Notification (optionnelle)

**Criticité :** 🟢 BASSE (sécurité)

**Bugs connus :** ⚠️ **NON TESTÉ** (aucun cycle détecté dans logs)

**Statut validation :** 🟡 À VALIDER

**Action requise :** Test manuel un week-end matin

### 6.5 Volets Salon — Gestion Intelligente

**Fichier source :** `automations.yaml` (à identifier)

**Logique :**

#### Scénario "Isolation" (G1/G3)
```
SI T° Ext < 17°C
ET (Absence OU Eric seul)
ALORS Fermer volet (même en journée)
```

#### Scénario "Lumière" (G2/G4)
```
SI Mamour présente
ALORS Ouvrir volet OU Position 50% Mi-ombre
(Priorité confort visuel sur isolation)
```

#### Protection Solaire (Été)
```
SI T° Ext > 34°C
ALORS Fermer volet
```

**Criticité :** 🟡 MOYENNE (confort + économies)

**Bugs connus :** Impossible à valider sans tags G1/G2/G3/G4 dans logs

**Statut validation :** ⚠️ DONNÉES INSUFFISANTES

### 6.6 Volets Bureau — Gestion Thermique

**Fichier source :** `automations.yaml` (à identifier)

**Logique :**
```
SI T° Ext dans [18°C - 25°C]
ALORS Volet OUVERT
SINON Volet FERMÉ (isolation)
```

**Criticité :** 🟡 MOYENNE

**Bugs connus :** Aucun

### 6.7 Diagnostic Énergie — Log 15min

**Fichier source :** `automations.yaml`  
**Alias :** `DIAG - ENREGISTREMENT JOURNALIER (6 POSTES + DUT)`

**Déclencheur :**
- Time pattern : toutes les 15 minutes

**Actions :**
1. Collecte des 7 pôles (Hyg, Cuis, Froid, Chauff, Multi, Lum, Autres)
2. Collecte Avg P4
3. Collecte T° int/ext
4. Collecte DUT S/R/B/C (bientôt S/R/B/Sf/SS/C)
5. Écriture dans `notify.file` (fichier texte)

**Criticité :** 🔴 HAUTE (monitoring énergétique)

**Bugs connus :** 
- ⚠️ DUT Soufflant et Sèche-Serviette non inclus (correction en cours)

**Statut validation :** 🟡 EN COURS DE CORRECTION

**Fichier corrigé :** `/outputs/automation_diag_enregistrement_corrected.yaml`

---

## 7️⃣ POINTS DE VIGILANCE & BUGS CONNUS

### 7.1 Bugs Actifs

| ID | Sévérité | Description | Workaround | Résolution prévue |
|:---|:---------|:------------|:-----------|:------------------|
| **BUG-001** | 🟡 MOYENNE | DUT Soufflant/Sèche-Serviette absents des logs | Monitoring manuel | ✅ Corrigé (22/02/2026) |
| **BUG-002** | 🟢 BASSE | Timer 2h Sèche-Serviette non validé | - | 🔴 Test requis |
| **BUG-003** | 🟡 MOYENNE | Absence tags G1/G2/G3/G4 dans logs | Analyse manuelle calendrier | 🔴 À implémenter |

### 7.2 Points de Vigilance Thermique

#### Chambre Nord — Point Faible Identifié

**Problème :**
- DUT Chambre = **3.9× supérieur au Salon** (à T° ext identique)
- Orientation Nord (zéro apport solaire)
- Store manuel → risque d'oubli de fermeture nocturne

**Impact :**
- Surconsommation estimée : ~54 kWh/mois (~11€/mois à 0.20€/kWh)

**Actions correctives :**
- ✅ Rideaux épais installés (07/02/2026, 26.52€)
- 🟡 Protocole fermeture store strict à tester
- 🔴 Motorisation store envisagée (150-200€, ROI 18-24 mois)

#### Cuisine — Isolation Passive

**Problème :**
- Radiateur cycle 2h15/jour (0.2h DUT typique)
- Fenêtre Nord sans volet motorisé

**Actions correctives :**
- 🟡 Rideaux épais en cours d'installation (26.52€)

#### Seuil de Décrochage Système

**Observation :**
- À **T° ext < 8°C**, les clims Nord tournent quasi en continu
- DUT Chambre atteint 14.9h/jour (62% du temps)

**Recommandation :**
- Isolation renforcée prioritaire (rideaux thermiques, joints fenêtres)

### 7.3 Incohérences de Nommage

**Problème :** Conventions multiples coexistent

**Exemples :**
- ✅ Bon : `sensor.dut_clim_salon` (clair)
- ⚠️ Moyen : `sensor.clim_rad_total_avg_watts_daily` (opaque)
- ❌ Mauvais : `sensor.diag_poste_1_hygiene_quotidien` (verbeux)

**Action prévue :**
- Phase 2 : Refonte complète du nommage selon standard

### 7.4 Fichiers Monolithiques

**Problème :** `automations.yaml` contient toutes les automations

**Risques :**
- Difficile à maintenir (recherche, modifications)
- Risque de conflit lors des édits multiples
- Pas de séparation logique

**Action prévue :**
- Phase 2 : Découpage par domaine (`automations/chauffage/*.yaml`)

---

## 8️⃣ PROCÉDURES DE MAINTENANCE

### 8.1 Sauvegarde Système

**Fréquence :** Hebdomadaire (dimanche 03h00)

**Méthode actuelle :**
- 🔴 **AUCUNE SAUVEGARDE AUTOMATISÉE DÉTECTÉE**

**Procédure manuelle recommandée :**

1. **Sauvegarde complète Home Assistant**
   ```
   Supervisor → Sauvegardes → Créer sauvegarde complète
   ```

2. **Export vers GitHub** (déjà en place ✅)
   - Configuration sync automatique vers `BerrySwann/home-assistant-config`

3. **Sauvegarde locale additionnelle**
   - Copie sur clé USB mensuelle
   - Stockage hors site (cloud personnel)

**À implémenter en Phase 2 :**
- Automation sauvegarde hebdomadaire
- Upload automatique vers NAS/Cloud
- Rotation des sauvegardes (conserver 4 dernières)

### 8.2 Mise à Jour Home Assistant

**Fréquence :** Mensuelle (1er du mois)

**Procédure :**

1. **Vérification pré-mise à jour**
   ```
   - Créer sauvegarde complète
   - Lire changelog HA (breaking changes)
   - Vérifier compatibilité intégrations critiques
   ```

2. **Mise à jour**
   ```
   Supervisor → Tableau de bord → Mettre à jour Home Assistant
   ```

3. **Tests post-mise à jour**
   ```
   - Vérifier automations chauffage
   - Tester logs 15min (diag_conso)
   - Valider dashboards Lovelace
   - Contrôler intégrations Ecojoko/Linky
   ```

4. **Rollback si problème**
   ```
   Supervisor → Sauvegardes → Restaurer sauvegarde pré-MAJ
   ```

### 8.3 Vérification Mensuelle Capteurs

**Checklist :**

- [ ] Batteries capteurs TH (seuil alerte : <20%)
- [ ] Batteries capteurs ouverture (seuil alerte : <20%)
- [ ] Connectivité Ecojoko (vérifier dernière mise à jour)
- [ ] Connectivité Linky (MyElectricalData API)
- [ ] État prises connectées (ping test)

**Automation recommandée (à créer) :**
```yaml
# Notification si batterie capteur < 20%
trigger:
  - platform: numeric_state
    entity_id: sensor.*_battery
    below: 20
action:
  - service: notify.mobile_app_poco_x7_pro
    data:
      title: "BATTERIE FAIBLE"
      message: "Capteur {{ trigger.entity_id }} : {{ trigger.to_state.state }}%"
```

### 8.4 Maintenance Annuelle Physique

**Checklist :**

- [ ] Nettoyage filtres clims (×3)
- [ ] Nettoyage grilles VMC SDB
- [ ] Vérification étanchéité fenêtres (joints)
- [ ] Test volets motorisés (×2)
- [ ] Nettoyage capteurs température (poussière)

---

## 9️⃣ ROADMAP DE MIGRATION

### 9.1 Phase 0 : Documentation (EN COURS)

**Durée :** 2 semaines (22/02 → 08/03/2026)

**Livrables :**
- ✅ Cahier des charges v1.0 (ce document)
- 🟡 Schéma architecture actuelle (Draw.io)
- 🟡 Inventaire exhaustif équipements (Excel)
- 🟡 Cartographie complète automations (Markdown)

**Responsable :** Eric

**Statut :** 🟡 30% complété

### 9.2 Phase 1 : Stabilisation & Corrections (Mars 2026)

**Durée :** 2 semaines (09/03 → 22/03/2026)

**Objectifs :**
1. ✅ Corriger logs DUT (ajout Sf/SS) — **FAIT**
2. 🔴 Valider timer 2h Sèche-Serviette (test manuel)
3. 🔴 Ajouter tags G1/G2/G3/G4 dans logs
4. 🔴 Documenter toutes les entités HA (noms réels vs `[À documenter]`)
5. 🔴 Créer automation sauvegarde hebdomadaire

**Responsable :** Eric

**Statut :** 🔴 Non démarré

### 9.3 Phase 2 : Refactoring (Avril-Mai 2026)

**Durée :** 6 semaines (23/03 → 03/05/2026)

**Objectifs :**

#### 2.1 Restructuration Fichiers
- Découper `automations.yaml` par domaine
- Renommer templates (supprimer numéros séries)
- Créer `packages/` pour regrouper pôles

#### 2.2 Refonte Nommage
- Standard unique pour tous les capteurs
- Convention `domain_location_function_metric`
- Exemples :
  - `sensor.clim_rad_total_avg_watts_daily` → `sensor.heating_total_power_avg_daily`
  - `sensor.dut_clim_salon` → `sensor.heating_livingroom_runtime_daily`

#### 2.3 Amélioration Monitoring
- Créer dashboards par pièce (Bubble Card)
- Ajouter graphiques ApexCharts performance thermique
- Implémenter alertes anomalies (DUT anormal, T° dérive)

**Responsable :** Eric

**Statut :** 🔴 Non démarré

### 9.4 Phase 3 : Migration Matérielle (Juin 2026)

**Durée :** 1 semaine (04/06 → 10/06/2026)

**Objectifs :**
1. Décommissionner Mini-PC (ancien serveur)
2. Consolider tout sur Raspberry Pi 4
3. Optimiser performances HA (cleanup base de données)
4. Configurer sauvegarde NAS

**Responsable :** Eric

**Statut :** 🔴 Non démarré

### 9.5 Phase 4 : Optimisations Avancées (Juillet-Août 2026)

**Durée :** 6 semaines (11/06 → 22/08/2026)

**Objectifs :**

#### 4.1 Motorisation Store Chambre
- Achat moteur Somfy (~200€)
- Installation
- Intégration HA
- Automation isolation/lumière

#### 4.2 Amélioration Isolation Passive
- Joints fenêtres autocollants (15€)
- Film isolant fenêtres (optionnel, 50€)
- Mesure impact DUT (avant/après)

#### 4.3 Machine Learning
- Prédiction consommation (Prophet)
- Détection anomalies automatique
- Optimisation chauffage prédictif

**Responsable :** Eric

**Statut :** 🔴 Non démarré

### 9.6 Gantt Simplifié

```
Phase 0 : Documentation          [████████░░░░░░░░░░░░] 30% | 22/02-08/03
Phase 1 : Stabilisation          [░░░░░░░░░░░░░░░░░░░░]  0% | 09/03-22/03
Phase 2 : Refactoring            [░░░░░░░░░░░░░░░░░░░░]  0% | 23/03-03/05
Phase 3 : Migration Matérielle   [░░░░░░░░░░░░░░░░░░░░]  0% | 04/06-10/06
Phase 4 : Optimisations          [░░░░░░░░░░░░░░░░░░░░]  0% | 11/06-22/08
```

---

## 🔟 ANNEXES TECHNIQUES

### 10.1 Template Nommage v2.0 (Standard futur)

**Convention proposée :**

```
{domain}_{location}_{function}_{metric}_{cycle}
```

**Exemples :**

| Ancien nom | Nouveau nom v2.0 |
|:-----------|:-----------------|
| `sensor.clim_rad_total_avg_watts_daily` | `sensor.heating_total_power_avg_daily` |
| `sensor.dut_clim_salon` | `sensor.heating_livingroom_runtime_daily` |
| `sensor.diag_poste_1_hygiene_quotidien` | `sensor.energy_hygiene_total_daily` |
| `sensor.eclairage_salon_5_energie` | `sensor.lighting_livingroom_energy_total` |

**Domaines (domain) :**
- `heating` (chauffage/clim)
- `lighting` (éclairage)
- `energy` (monitoring global)
- `climate` (température/humidité)
- `air_quality` (qualité air)
- `cover` (volets/stores)

**Locations (location) :**
- `livingroom`, `kitchen`, `office`, `bathroom`, `bedroom`, `entrance`, `hallway`

**Functions (function) :**
- `total`, `average`, `runtime`, `status`, `power`, `temperature`

**Metrics (metric) :**
- `kwh`, `watts`, `hours`, `celsius`, `percent`, `count`

**Cycles (cycle) :**
- `daily`, `monthly`, `yearly`, `realtime`

### 10.2 Structure Fichiers Cible v2.0

**Organisation future recommandée :**

```
/config/
├── configuration.yaml              # Config minimale (includes)
├── secrets.yaml                    # Clés API
├── automations/                    # Automations par domaine
│   ├── heating/
│   │   ├── mode_day.yaml
│   │   ├── mode_night.yaml
│   │   └── kitchen_timer.yaml
│   ├── covers/
│   │   ├── livingroom_automation.yaml
│   │   └── office_automation.yaml
│   ├── monitoring/
│   │   └── energy_log_15min.yaml
│   └── notifications/
│       ├── battery_alerts.yaml
│       └── anomaly_detection.yaml
├── packages/                       # Regroupements fonctionnels
│   ├── heating.yaml                # Tout le chauffage ensemble
│   ├── lighting.yaml               # Tout l'éclairage ensemble
│   └── energy.yaml                 # Tout le monitoring énergie
├── sensors/
│   ├── heating/
│   │   ├── dut.yaml
│   │   ├── performance.yaml
│   │   └── averages.yaml
│   ├── energy/
│   │   └── diagnostics.yaml
│   └── climate/
│       └── temperature.yaml
└── dashboards/                     # Lovelace par pièce
    ├── main.yaml
    ├── livingroom.yaml
    ├── kitchen.yaml
    └── energy.yaml
```

### 10.3 Checklist Migration Complète

**Pré-migration :**
- [ ] Sauvegarde complète système
- [ ] Export config GitHub à jour
- [ ] Documentation inventaire exhaustive
- [ ] Tests validation automations critiques

**Migration :**
- [ ] Installation HA OS fresh sur carte SD neuve
- [ ] Restauration sélective (pas sauvegarde complète)
- [ ] Re-création config v2.0 avec nouvelle structure
- [ ] Import équipements par pôle (1 pôle/jour)
- [ ] Tests unitaires après chaque pôle

**Post-migration :**
- [ ] Validation 7 jours monitoring
- [ ] Comparaison conso v1 vs v2 (détection régressions)
- [ ] Ajustements automations
- [ ] Documentation v2.0 finalisée
- [ ] Archivage config v1.5

### 10.4 Outils Recommandés

**Développement :**
- Visual Studio Code + Extension Home Assistant
- YAML Lint (validation syntaxe)
- Jinja2 Tester (test templates)

**Schémas :**
- Draw.io (architecture réseau)
- Mermaid (diagrammes intégrés Markdown)

**Monitoring :**
- Grafana + InfluxDB (historiques long terme)
- Node-RED (flux visuels optionnel)

**Backup :**
- Restic (sauvegardes incrémentales)
- Rclone (sync cloud)

---

## ✅ VALIDATION & SIGNATURES

### Validation Technique

**Rédacteur :** Eric (BerrySwann)  
**Date :** 2026-02-22  
**Version :** 1.0 (Draft)

**Statut :** 🟡 **Document vivant** — À compléter au fur et à mesure

### Prochaines Étapes Immédiates

1. **Compléter Section 5 (Inventaire)** — Documenter marques/modèles équipements
2. **Créer schéma architecture** — Draw.io ou Mermaid
3. **Valider bugs actifs** — Test Sèche-Serviette SDB
4. **Implémenter Phase 1** — Corrections urgentes

---

**FIN DU CAHIER DES CHARGES v1.0**

---

## 📎 ANNEXE : LIENS UTILES

- **GitHub Config :** https://github.com/BerrySwann/home-assistant-config
- **Documentation HA :** https://www.home-assistant.io/docs/
- **Forum Communauté :** https://community.home-assistant.io/
- **HACS (Custom Components) :** https://hacs.xyz/

---

**Document généré le 2026-02-22 par Claude (Anthropic)**  
**Licence :** Usage personnel Eric (BerrySwann) uniquement