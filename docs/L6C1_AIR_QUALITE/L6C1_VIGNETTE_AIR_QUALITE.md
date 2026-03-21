<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord/L6C1_vignette_air_qualite.yaml` |
| 🔗 **Accès depuis** | Vue Home — L6C1 |
| 🔗 **tap →** | `/dashboard-tablette/air-quality` |
| 🏗️ **Layout** | `custom:button-card` — grille 9 lignes × 3 colonnes (Pièce / Type / Valeur) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3.x |

---

# 🫧 L6C1 — VIGNETTE QUALITÉ DE L'AIR

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Code](#code)
4. [Logique JS — Seuils & couleurs](#logique-js--seuils--couleurs)
5. [Chaîne d'entités](#chaîne-dentités)
6. [Entités utilisées](#entités-utilisées)
7. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Vignette affichant en temps réel la qualité de l'air de 3 pièces (Salon, Bureau, Chambre) sur deux indicateurs : **PM2.5** (particules fines) et **tCOV** (composés organiques volatils totaux). Tap → page détaillée avec ring-tiles et graphiques pop-up.

**3 colonnes :** Pièce / Type (PM2.5 ou tCOV) / Valeur avec unité
**Colorisation dynamique** : chaque ligne change de couleur selon le niveau mesuré (blanc → orange → rouge).

### Intégrations requises

- ✅ **IKEA Vindstyrka** (Zigbee/Matter) — `sensor.qualite_air_*_ikea_pm25` + `*_voc_index`
- ✅ **Sensors statistics** — moyennes 24h (`platform: statistics`)
- ✅ **Templates** — conversion tCOV en ppb avec `device_class: volatile_organic_compounds_parts`

### Cartes HACS

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Vignette — grille 9 lignes × 3 colonnes avec JS |

---

## 🏗️ ARCHITECTURE

```
┌───────────────────────────────────────────────────┐
│         Qualité de l'Air ambiant                  │  ← titre (row 1)
├─────────────────┬───────────────┬─────────────────┤
│  Salon          │  PM2.5        │  x.x µg/m³      │  ← row 3
│  Bureau         │  PM2.5        │  x.x µg/m³      │  ← row 4
│  Chambre        │  PM2.5        │  x.x µg/m³      │  ← row 5
│  Salon          │  tCOV         │  xxx ppb         │  ← row 6
│  Bureau         │  tCOV         │  xxx ppb         │  ← row 7
│  Chambre        │  tCOV         │  xxx ppb         │  ← row 8
└─────────────────┴───────────────┴─────────────────┘
Couleur : blanc=OK / orange=Attention / rouge=Mauvais
tap → /dashboard-tablette/air-quality
```

**Grid-template-areas :**
```
"titre titre titre"
"espace_debut espace_debut espace_debut"
"piece_pm25_salon  type_pm25_salon  value_pm25_salon"
"piece_pm25_bureau type_pm25_bureau value_pm25_bureau"
"piece_pm25_chambre type_pm25_chambre value_pm25_chambre"
"piece_tcov_salon  type_tcov_salon  value_tcov_salon"
"piece_tcov_bureau type_tcov_bureau value_tcov_bureau"
"piece_tcov_chambre type_tcov_chambre value_tcov_chambre"
"espace_fin espace_fin espace_fin"
```

> ⚠️ **Bug connu** : le style du champ `titre` contient `grid-area: title` (anglais) alors que la `grid-template-areas` déclare `"titre titre titre"`. Le titre peut ne pas être positionné dans son area. À corriger en `grid-area: titre`.

---

## 📍 CODE

Le YAML complet de la vignette est volumineux (18 champs JS). Seuls les éléments structurants sont reproduits ici ; le code intégral est dans `dashbord/L6C1_vignette_air_qualite.yaml`.

```yaml
type: custom:button-card
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/air-quality
styles:
  card:
    - aspect-ratio: 1/1
    - border-radius: 10px
    - background: transparent
    - border-width: 3px
    - border-color: white
    - border-style: double
    - color: white
    - font-size: 11px
    - line-height: 1.2
  grid:
    - grid-template-areas: |
        "titre titre titre"
        "espace_debut espace_debut espace_debut"
        "piece_pm25_salon type_pm25_salon value_pm25_salon"
        "piece_pm25_bureau type_pm25_bureau value_pm25_bureau"
        "piece_pm25_chambre type_pm25_chambre value_pm25_chambre"
        "piece_tcov_salon type_tcov_salon value_tcov_salon"
        "piece_tcov_bureau type_tcov_bureau value_tcov_bureau"
        "piece_tcov_chambre type_tcov_chambre value_tcov_chambre"
        "espace_fin espace_fin espace_fin"
    - grid-template-columns: 1fr 1fr 1fr
    - grid-template-rows: auto
```

**Champ `titre` :**
```yaml
titre: |
  [[[
    return 'Qualité de l\'Air ambiant';
  ]]]
```

**Patron générique par champ** (répété × 6 pièces × 3 colonnes) :
```yaml
piece_pm25_salon: |   # → retourne la pièce colorée selon PM2.5
type_pm25_salon: |    # → retourne "PM2.5" coloré
value_pm25_salon: |   # → retourne la valeur + "µg/m³" colorée
```
*(idem pour bureau, chambre, et pour tCOV)*

---

## 🔢 LOGIQUE JS — SEUILS & COULEURS

Deux fonctions de colorisation sont appliquées en ligne dans chaque champ JS.

### PM2.5 (`sensor.qualite_air_*_ikea_pm25`)

| Seuil | Couleur | Signification |
|:------|:--------|:-------------|
| `> 35 µg/m³` | `rgb(244, 67, 54)` — rouge | Mauvais (norme OMS 24h) |
| `> 11 µg/m³` | `orange` | Attention (norme OMS annuelle) |
| `≤ 11 µg/m³` | `white` | Bon |
| `unavailable` / `unknown` | `#808080` — gris | Capteur indisponible |

**Unité affichée :** `µg/m³`

### tCOV (`sensor.qualite_air_*_ikea_voc_index`)

| Seuil | Couleur | Signification |
|:------|:--------|:-------------|
| `> 1000 ppb` | `rgb(244, 67, 54)` — rouge | Très mauvais |
| `> 250 ppb` | `orange` | Attention |
| `≤ 250 ppb` | `white` | Bon |
| `unavailable` / `unknown` | `#808080` — gris | Capteur indisponible |

**Unité affichée :** `ppb`

> **Note :** Pour les tCOV, la vignette lit directement `sensor.qualite_air_*_ikea_voc_index` (index brut), pas `sensor.tcov_*_ppb` (le template ppb est réservé à la page détaillée).

---

## 🔗 CHAÎNE D'ENTITÉS

```
IKEA Vindstyrka (Zigbee/Matter)
  ├── sensor.qualite_air_*_ikea_pm25        [NAT] → valeur brute PM2.5 (µg/m³)
  │     └── sensor.pm2_5_*_moy_24h         [SNS] platform: statistics (mean 24h)
  │           └── utilisé comme marker2 dans ring-tile page
  └── sensor.qualite_air_*_ikea_voc_index   [NAT] → index VOC brut
        ├── sensor.tcov_*_ppb              [TPL] conversion ppb + device_class
        │     └── utilisé dans ring-tile page
        └── sensor.tcov_*_moy_24h         [SNS] platform: statistics (mean 24h)
              └── utilisé comme marker2 dans ring-tile page
```

---

## 📊 ENTITÉS UTILISÉES

### Entités natives IKEA (source)

| Entité | Pièce | Mesure | Source |
|:-------|:------|:-------|:-------|
| `sensor.qualite_air_salon_ikea_pm25` | Salon | PM2.5 (µg/m³) | IKEA Vindstyrka [NAT] |
| `sensor.qualite_air_salon_ikea_voc_index` | Salon | VOC index | IKEA Vindstyrka [NAT] |
| `sensor.qualite_air_bureau_ikea_pm25` | Bureau | PM2.5 (µg/m³) | IKEA Vindstyrka [NAT] |
| `sensor.qualite_air_bureau_ikea_voc_index` | Bureau | VOC index | IKEA Vindstyrka [NAT] |
| `sensor.qualite_air_chambre_ikea_pm25` | Chambre | PM2.5 (µg/m³) | IKEA Vindstyrka [NAT] |
| `sensor.qualite_air_chambre_ikea_voc_index` | Chambre | VOC index | IKEA Vindstyrka [NAT] |

### Sensors moyennes 24h (platform: statistics)

Source : `sensors/air_qualite/pm25_tcov_moy_24h.yaml`

| Entité (entity_id généré) | unique_id | Source → |
|:--------------------------|:----------|:---------|
| `sensor.pm2_5_salon_moy_24h` | `pm25_salon_mean_24h` | `*_salon_ikea_pm25` |
| `sensor.tcov_salon_moy_24h` | `tcov_salon_mean_24h` | `*_salon_ikea_voc_index` |
| `sensor.pm2_5_bureau_moy_24h` | `pm25_bureau_mean_24h` | `*_bureau_ikea_pm25` |
| `sensor.tcov_bureau_moy_24h` | `tcov_bureau_mean_24h` | `*_bureau_ikea_voc_index` |
| `sensor.pm2_5_chambre_moy_24h` | `pm25_chambre_mean_24h` | `*_chambre_ikea_pm25` |
| `sensor.tcov_chambre_moy_24h` | `tcov_chambre_mean_24h` | `*_chambre_ikea_voc_index` |

### Templates ppb (conversion device_class)

Source : `templates/air_qualite/tcov_ppb.yaml`

| Entité | unique_id | Source → |
|:-------|:----------|:---------|
| `sensor.tcov_salon_ppb` | `tcov_salon_ppb` | `*_salon_ikea_voc_index` |
| `sensor.tcov_bureau_ppb` | `tcov_bureau_ppb` | `*_bureau_ikea_voc_index` |
| `sensor.tcov_chambre_ppb` | `tcov_chambre_ppb` | `*_chambre_ikea_voc_index` |

---

## 🐛 DÉPANNAGE

### Toutes les valeurs affichent "N/A" en gris
→ Les capteurs IKEA Vindstyrka sont indisponibles. Vérifier Zigbee2MQTT / intégration Matter.

### Le titre "Qualité de l'Air ambiant" n'apparaît pas dans la bonne position
→ Bug connu — le style contient `grid-area: title` au lieu de `grid-area: titre`. Corriger dans le YAML.

### Les valeurs tCOV affichent l'index VOC (ex: "150") au lieu de ppb
→ Normal pour la vignette — elle lit `sensor.qualite_air_*_ikea_voc_index` directement. Les `sensor.tcov_*_ppb` ne sont utilisés que dans la page détaillée.

### Les moyennes 24h ne se calculent pas
→ Vérifier que les sensors `platform: statistics` sont bien chargés (`sensors/air_qualite/pm25_tcov_moy_24h.yaml` inclus dans `configuration.yaml`). Il faut 24h de données pour que la moyenne soit stable.

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:button-card` | HACS | ✅ Essentiel |
| IKEA Vindstyrka × 3 | Zigbee/Matter [NAT] | ✅ Essentiel |
| `sensor.pm2_5_*_moy_24h` × 3 | `platform: statistics` | ✅ Requis (page) |
| `sensor.tcov_*_ppb` × 3 | Template | ✅ Requis (page) |

---

## 🔗 FICHIERS LIÉS

| Rôle | Chemin |
|------|--------|
| Sensors statistics 24h | `sensors/air_qualite/pm25_tcov_moy_24h.yaml` |
| Templates ppb | `templates/air_qualite/tcov_ppb.yaml` |
| Page détaillée | `docs/L6C1_AIR_QUALITE/PAGE_AIR_QUALITE.md` |

---

← Retour : `docs/L5C3_MARIADB/` | → Suivant : `docs/L6C1_AIR_QUALITE/PAGE_AIR_QUALITE.md`
