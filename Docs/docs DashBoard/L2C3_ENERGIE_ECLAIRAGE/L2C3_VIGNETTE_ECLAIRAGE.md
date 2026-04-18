<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--18-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord/L2C3_vignette_eclairage.yaml` |
| 🔗 **Accès depuis** | Vue Home |
| 🔗 **tap →** | `/dashboard-tablette/energie-lampes` |
| 🏗️ **Layout** | `custom:button-card` — grille 3 colonnes |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-18 |
| 🏠 **Version HA** | 2026.3 |

---

# 💡 L2C3 — VIGNETTE CONSO ÉNERGIE ÉCLAIRAGE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Code](#code)
4. [Logique JS](#logique-js)
5. [Entités utilisées](#entités-utilisées)
6. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Vignette affichant la consommation kWh de l'éclairage par pièce, en colonnes Quotidien et Mensuel. La couleur du nom de pièce indique l'état d'allumage : **blanc** = éteint, **vert** = allumé. La ligne TOTAL est toujours en vert gras.

Les pièces Bureau et Chambre ont une logique `isEcoSensitive` : le mode `Éco.` n'allume pas la couleur verte (ampoules à faible consommation considérées comme éteintes).

### Intégrations requises

- ✅ **Philips Hue** (bridge natif) — états et puissance lampes
- ✅ **Utility Meters P3** — `sensor.eclairage_*_quotidien/mensuel_kwh_um`
- ✅ **Templates P3** — `sensor.lumiere_*_etat` (états par pièce)

### Cartes HACS

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Vignette 3 colonnes pièce / quotidien / mensuel |

---

## 🏗️ ARCHITECTURE

```
┌──────────────────────────────────┐
│     Consommation LAMPES          │
├───────────┬──────────┬───────────┤
│  Pièce    │ Quotidien│  Mensuel  │
│  Appart.  │  x.xx kWh│  x.xx kWh│
│  Salon    │  x.xx kWh│  x.xx kWh│
│  Cuisine  │  x.xx kWh│  x.xx kWh│
│  Bureau   │  x.xx kWh│  x.xx kWh│
│  SdB      │  x.xx kWh│  x.xx kWh│
│  Chambre  │  x.xx kWh│  x.xx kWh│
│  TOTAL    │  x.xx kWh│  x.xx kWh│
└───────────┴──────────┴───────────┘
Couleur pièce : blanc=éteint / vert=allumé
tap → /dashboard-tablette/energie-lampes
         → voir PAGE_ENERGIE_ECLAIRAGE.md pour le YAML complet
```

---

## 📍 CODE

```yaml
type: custom:button-card
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/energie-lampes
entities:
  - sensor.lumiere_appartement_etat
  - sensor.lumiere_salon_etat
  - sensor.lumiere_cuisine_etat
  - sensor.lumiere_bureau_etat
  - sensor.lumiere_salle_de_bain_etat
  - sensor.lumiere_chambre_etat
  - sensor.eclairage_appart_2_quotidien_kwh_um
  - sensor.eclairage_salon_5_quotidien_kwh_um
  - sensor.eclairage_cuisine_1_quotidien_kwh_um
  - sensor.eclairage_bureau_5_quotidien_kwh_um
  - sensor.eclairage_sdb_2_quotidien_kwh_um
  - sensor.eclairage_chambre_4_quotidien_kwh_um
  - sensor.eclairage_total_unit_quotidien_kwh_um
  - sensor.eclairage_appart_2_mensuel_kwh_um
  - sensor.eclairage_salon_5_mensuel_kwh_um
  - sensor.eclairage_cuisine_1_mensuel_kwh_um
  - sensor.eclairage_bureau_5_mensuel_kwh_um
  - sensor.eclairage_sdb_2_mensuel_kwh_um
  - sensor.eclairage_chambre_4_mensuel_kwh_um
  - sensor.eclairage_total_unit_mensuel_kwh_um
triggers_update:
  - sensor.lumiere_appartement_etat
  - sensor.lumiere_salon_etat
  - sensor.lumiere_cuisine_etat
  - sensor.lumiere_bureau_etat
  - sensor.lumiere_salle_de_bain_etat
  - sensor.lumiere_chambre_etat
  - sensor.eclairage_appart_2_quotidien_kwh_um
  - sensor.eclairage_salon_5_quotidien_kwh_um
  - sensor.eclairage_cuisine_1_quotidien_kwh_um
  - sensor.eclairage_bureau_5_quotidien_kwh_um
  - sensor.eclairage_sdb_2_quotidien_kwh_um
  - sensor.eclairage_chambre_4_quotidien_kwh_um
  - sensor.eclairage_total_unit_quotidien_kwh_um
  - sensor.eclairage_appart_2_mensuel_kwh_um
  - sensor.eclairage_salon_5_mensuel_kwh_um
  - sensor.eclairage_cuisine_1_mensuel_kwh_um
  - sensor.eclairage_bureau_5_mensuel_kwh_um
  - sensor.eclairage_sdb_2_mensuel_kwh_um
  - sensor.eclairage_chambre_4_mensuel_kwh_um
  - sensor.eclairage_total_unit_mensuel_kwh_um
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
        "piece quotidien mensuel"
    - grid-template-columns: 1fr 1fr 1fr
    - grid-template-rows: auto
    - margin-top: 4.5px
  custom_fields:
    titre:
      - grid-area: titre
      - justify-self: center
      - text-align: center
      - font-weight: bold
    piece:
      - justify-self: start
      - margin-left: 8px
      - text-align: left
    quotidien:
      - justify-self: start
      - margin-left: 15px
      - text-align: left
    mensuel:
      - justify-self: end
      - margin-right: 6px
      - text-align: right
custom_fields:
  titre: |
    [[[ return 'Consommation LAMPES' ]]]
  piece: |
    [[[
      function getCol(entityId, isEcoSensitive = false) {
        const s = states[entityId]?.state;
        if (!s || s === 'Éteint') return 'white';
        if (isEcoSensitive && s === 'Éco.') return 'white';
        return 'lightgreen';
      }
      const pieces = [
        { name: 'Appart.', color: getCol('sensor.lumiere_appartement_etat') },
        { name: 'Salon',   color: getCol('sensor.lumiere_salon_etat') },
        { name: 'Cuisine', color: getCol('sensor.lumiere_cuisine_etat') },
        { name: 'Bureau',  color: getCol('sensor.lumiere_bureau_etat', true) },
        { name: 'SdB',     color: getCol('sensor.lumiere_salle_de_bain_etat') },
        { name: 'Chambre', color: getCol('sensor.lumiere_chambre_etat', true) },
        { name: 'TOTAL',   color: 'lightgreen', bold: true }
      ];
      return pieces.map(p =>
        `<span style="display: block; text-align: left; line-height: 1.2; color: ${p.color}; ${p.bold ? 'font-weight: bold;' : ''}">${p.name}</span>`
      ).join('');
    ]]]
  quotidien: |
    [[[
      function safeState(entityId) {
        const entity = states[entityId];
        if (!entity || ['unavailable', 'unknown'].includes(entity.state)) return '<span style="color: #aaaaaa;">N/A</span>';
        var val = parseFloat(entity.state);
        if (isNaN(val)) return '<span style="color: #aaaaaa;">N/A</span>';
        if (val < 1) return (val * 1000).toFixed(0) + ' <span style="font-size: 5px;">Wh</span>';
        return val.toFixed(2) + ' <span style="font-size: 5px;">kWh</span>';
      }
      const sensors = [
        'sensor.eclairage_appart_2_quotidien_kwh_um',
        'sensor.eclairage_salon_5_quotidien_kwh_um',
        'sensor.eclairage_cuisine_1_quotidien_kwh_um',
        'sensor.eclairage_bureau_5_quotidien_kwh_um',
        'sensor.eclairage_sdb_2_quotidien_kwh_um',
        'sensor.eclairage_chambre_4_quotidien_kwh_um',
        'sensor.eclairage_total_unit_quotidien_kwh_um'
      ];
      return sensors.map((s, i) => {
        const isLast = i === sensors.length - 1;
        return `<span style="display: block; text-align: right; line-height: 1.2; ${isLast ? 'color: lightgreen; font-weight: bold;' : ''}">${safeState(s)}</span>`;
      }).join('');
    ]]]
  mensuel: |
    [[[
      function safeState(entityId) {
        const entity = states[entityId];
        if (!entity || ['unavailable', 'unknown'].includes(entity.state)) return '<span style="color: #aaaaaa;">N/A</span>';
        var val = parseFloat(entity.state);
        if (isNaN(val)) return '<span style="color: #aaaaaa;">N/A</span>';
        if (val < 1) return (val * 1000).toFixed(0) + ' <span style="font-size: 5px;">Wh</span>';
        return val.toFixed(2) + ' <span style="font-size: 5px;">kWh</span>';
      }
      const sensors = [
        'sensor.eclairage_appart_2_mensuel_kwh_um',
        'sensor.eclairage_salon_5_mensuel_kwh_um',
        'sensor.eclairage_cuisine_1_mensuel_kwh_um',
        'sensor.eclairage_bureau_5_mensuel_kwh_um',
        'sensor.eclairage_sdb_2_mensuel_kwh_um',
        'sensor.eclairage_chambre_4_mensuel_kwh_um',
        'sensor.eclairage_total_unit_mensuel_kwh_um'
      ];
      return sensors.map((s, i) => {
        const isLast = i === sensors.length - 1;
        return `<span style="display: block; text-align: right; line-height: 1.2; ${isLast ? 'color: lightgreen; font-weight: bold;' : ''}">${safeState(s)}</span>`;
      }).join('');
    ]]]
```

---

## 🔢 LOGIQUE JS

### Couleur des pièces — `getCol(entityId, isEcoSensitive)`

| État sensor | `isEcoSensitive` | Couleur |
|-------------|-----------------|---------|
| `Éteint` | — | `white` |
| `Éco.` | `true` | `white` |
| `Éco.` | `false` | `lightgreen` |
| Tout autre | — | `lightgreen` |

Bureau et Chambre passent `isEcoSensitive = true` : le mode Éco ne colore pas la pièce en vert.

### Affichage des valeurs — `safeState(entityId)`

- `unavailable` / `unknown` / `NaN` → `N/A` en gris
- `< 1 kWh` → converti en Wh (ex : `345 Wh`)
- `≥ 1 kWh` → affiché en kWh avec 2 décimales (ex : `1.23 kWh`)
- Dernière ligne (index 6 = TOTAL) → `lightgreen` + gras

---

## 📊 ENTITÉS UTILISÉES

### États d'allumage — `sensor.lumiere_*_etat`

> Définis dans `templates/P3_eclairage/ui_dashboard/etats_status.yaml`

| Entité | Pièce | isEcoSensitive |
|--------|-------|---------------|
| `sensor.lumiere_appartement_etat` | Appart. (agrégat) | non |
| `sensor.lumiere_salon_etat` | Salon | non |
| `sensor.lumiere_cuisine_etat` | Cuisine | non |
| `sensor.lumiere_bureau_etat` | Bureau | **oui** |
| `sensor.lumiere_salle_de_bain_etat` | SDB | non |
| `sensor.lumiere_chambre_etat` | Chambre | **oui** |

### Utility Meters quotidiens — `sensor.eclairage_*_quotidien_kwh_um`

> Définis dans `utility_meter/P3_eclairage/P3_UM_AMHQ_*.yaml`

| Entité | Zone / Pièce |
|--------|-------------|
| `sensor.eclairage_appart_2_quotidien_kwh_um` | Entrée + couloir (2 lampes) |
| `sensor.eclairage_salon_5_quotidien_kwh_um` | Salon (5 lampes) |
| `sensor.eclairage_cuisine_1_quotidien_kwh_um` | Cuisine (1 lampe) |
| `sensor.eclairage_bureau_5_quotidien_kwh_um` | Bureau (5 lampes) |
| `sensor.eclairage_sdb_2_quotidien_kwh_um` | SDB (2 lampes) |
| `sensor.eclairage_chambre_4_quotidien_kwh_um` | Chambre (4 lampes) |
| `sensor.eclairage_total_unit_quotidien_kwh_um` | **TOTAL appartement** |

### Utility Meters mensuels — `sensor.eclairage_*_mensuel_kwh_um`

> Mêmes zones, cycle mensuel — `utility_meter/P3_eclairage/P3_UM_AMHQ_*.yaml`

| Entité | Zone / Pièce |
|--------|-------------|
| `sensor.eclairage_appart_2_mensuel_kwh_um` | Entrée + couloir |
| `sensor.eclairage_salon_5_mensuel_kwh_um` | Salon |
| `sensor.eclairage_cuisine_1_mensuel_kwh_um` | Cuisine |
| `sensor.eclairage_bureau_5_mensuel_kwh_um` | Bureau |
| `sensor.eclairage_sdb_2_mensuel_kwh_um` | SDB |
| `sensor.eclairage_chambre_4_mensuel_kwh_um` | Chambre |
| `sensor.eclairage_total_unit_mensuel_kwh_um` | **TOTAL appartement** |

---

## 🐛 DÉPANNAGE

### Toutes les valeurs affichent N/A
Vérifier que les UM `P3_UM_AMHQ_*.yaml` sont bien chargés dans HA (`utility_meter/P3_eclairage/`).

### Une pièce reste blanche alors que la lumière est allumée
L'état du `sensor.lumiere_*_etat` n'est pas `Éteint` mais pas non plus reconnu comme allumé. Vérifier les valeurs possibles dans `etats_status.yaml`.

### Bureau/Chambre toujours blancs en mode Éco
Comportement voulu — `isEcoSensitive = true` maintient la couleur blanche en mode Éco.

---

## 📝 DÉPENDANCES

| Élément | Fichier source | Statut |
|---------|---------------|--------|
| `sensor.lumiere_*_etat` | `templates/P3_eclairage/ui_dashboard/etats_status.yaml` | ✅ Essentiel |
| `sensor.eclairage_*_quotidien_kwh_um` | `utility_meter/P3_eclairage/P3_UM_AMHQ_*.yaml` | ✅ Essentiel |
| `sensor.eclairage_*_mensuel_kwh_um` | `utility_meter/P3_eclairage/P3_UM_AMHQ_*.yaml` | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

### Configuration YAML (sources HA — ReBuild)

- `templates/P3_eclairage/ui_dashboard/etats_status.yaml` — `sensor.lumiere_*_etat`
- `utility_meter/P3_eclairage/P3_UM_AMHQ_2_ZONE.yaml` — UM quotidien/mensuel par zone
- `utility_meter/P3_eclairage/P3_UM_AMHQ_3_TOTAL.yaml` — UM TOTAL appartement

### Documentation

- [`PAGE_ENERGIE_ECLAIRAGE.md`](./PAGE_ENERGIE_ECLAIRAGE.md) — YAML complet de la page `/dashboard-tablette/energie-lampes` (5 sections pièces, tabbed-card)
- [`docs/WIFI_PRESENCE (Home Page)/PAGE_HOME.md`](../WIFI_PRESENCE%20(Home%20Page)/PAGE_HOME.md) — vue d'ensemble des 18 vignettes
- [`docs/DEPENDANCES_GLOBALES.md`](../DEPENDANCES_GLOBALES.md) — chaîne de dépendances L2C3

---

← Retour : [`PAGE_HOME.md`](../WIFI_PRESENCE%20(Home%20Page)/PAGE_HOME.md) | → Suite : [`PAGE_ENERGIE_ECLAIRAGE.md`](./PAGE_ENERGIE_ECLAIRAGE.md)


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_ENERGIE_ECLAIRAGE]]  [[COULEURS_ECLAIRAGE_PAR_PIECE]]  [[L2C1_VIGNETTE_ENERGIE]]  [[L2C2_VIGNETTE_ENERGIE_CLIM]]  [[L3C1_VIGNETTE_ECLAIRAGE]]*
