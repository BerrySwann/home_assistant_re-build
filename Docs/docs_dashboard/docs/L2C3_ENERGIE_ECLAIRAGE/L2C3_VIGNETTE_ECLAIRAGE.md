<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026-04-29-44739e?style=flat-square)](.)&nbsp;
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
| 📅 **Modifié le** | 2026-04-29 |
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

### Chaîne TPL (depuis 2026-04-29)

Les entités kWh proviennent désormais de la chaîne template P3_ENERGIE_TLP — plus des Utility Meters bruts :

```
P3_UM_AMHQ_1_UNITE  →  {slug}_{cycle}_um
P3_TPL_AMHQ_1_UNITE →  {slug}_{cycle}_um_kwh_tpl
P3_TPL_AMHQ_2_ZONE  →  eclairage_{zone}_{cycle}_um_kwh_tpl   ← vignette
P3_TPL_AMHQ_3_TOTAL →  eclairage_total_unit_{cycle}_kwh_tpl  ← vignette
```

### Intégrations requises

- ✅ **Philips Hue** (bridge natif) — états et puissance lampes
- ✅ **Utility Meters P3** — `P3_UM_AMHQ_1_UNITE.yaml` (source de base)
- ✅ **Templates P3_ENERGIE_TLP** — `_um_kwh_tpl` (relais kWh)
- ✅ **Templates P3_eclairage/ui_dashboard** — `sensor.lumiere_*_etat`

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
  - sensor.eclairage_appart_2_quotidien_um_kwh_tpl
  - sensor.eclairage_salon_5_quotidien_um_kwh_tpl
  - sensor.eclairage_cuisine_1_quotidien_um_kwh_tpl
  - sensor.eclairage_bureau_5_quotidien_um_kwh_tpl
  - sensor.eclairage_sdb_2_quotidien_um_kwh_tpl
  - sensor.eclairage_chambre_4_quotidien_um_kwh_tpl
  - sensor.eclairage_total_unit_quotidien_kwh_tpl
  - sensor.eclairage_appart_2_mensuel_um_kwh_tpl
  - sensor.eclairage_salon_5_mensuel_um_kwh_tpl
  - sensor.eclairage_cuisine_1_mensuel_um_kwh_tpl
  - sensor.eclairage_bureau_5_mensuel_um_kwh_tpl
  - sensor.eclairage_sdb_2_mensuel_um_kwh_tpl
  - sensor.eclairage_chambre_4_mensuel_um_kwh_tpl
  - sensor.eclairage_total_unit_mensuel_kwh_tpl
triggers_update:
  - sensor.lumiere_appartement_etat
  - sensor.lumiere_salon_etat
  - sensor.lumiere_cuisine_etat
  - sensor.lumiere_bureau_etat
  - sensor.lumiere_salle_de_bain_etat
  - sensor.lumiere_chambre_etat
  - sensor.eclairage_appart_2_quotidien_um_kwh_tpl
  - sensor.eclairage_salon_5_quotidien_um_kwh_tpl
  - sensor.eclairage_cuisine_1_quotidien_um_kwh_tpl
  - sensor.eclairage_bureau_5_quotidien_um_kwh_tpl
  - sensor.eclairage_sdb_2_quotidien_um_kwh_tpl
  - sensor.eclairage_chambre_4_quotidien_um_kwh_tpl
  - sensor.eclairage_total_unit_quotidien_kwh_tpl
  - sensor.eclairage_appart_2_mensuel_um_kwh_tpl
  - sensor.eclairage_salon_5_mensuel_um_kwh_tpl
  - sensor.eclairage_cuisine_1_mensuel_um_kwh_tpl
  - sensor.eclairage_bureau_5_mensuel_um_kwh_tpl
  - sensor.eclairage_sdb_2_mensuel_um_kwh_tpl
  - sensor.eclairage_chambre_4_mensuel_um_kwh_tpl
  - sensor.eclairage_total_unit_mensuel_kwh_tpl
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
        'sensor.eclairage_appart_2_quotidien_um_kwh_tpl',
        'sensor.eclairage_salon_5_quotidien_um_kwh_tpl',
        'sensor.eclairage_cuisine_1_quotidien_um_kwh_tpl',
        'sensor.eclairage_bureau_5_quotidien_um_kwh_tpl',
        'sensor.eclairage_sdb_2_quotidien_um_kwh_tpl',
        'sensor.eclairage_chambre_4_quotidien_um_kwh_tpl',
        'sensor.eclairage_total_unit_quotidien_kwh_tpl'
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
        'sensor.eclairage_appart_2_mensuel_um_kwh_tpl',
        'sensor.eclairage_salon_5_mensuel_um_kwh_tpl',
        'sensor.eclairage_cuisine_1_mensuel_um_kwh_tpl',
        'sensor.eclairage_bureau_5_mensuel_um_kwh_tpl',
        'sensor.eclairage_sdb_2_mensuel_um_kwh_tpl',
        'sensor.eclairage_chambre_4_mensuel_um_kwh_tpl',
        'sensor.eclairage_total_unit_mensuel_kwh_tpl'
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

### kWh quotidiens — `sensor.eclairage_*_quotidien_um_kwh_tpl`

> Source : `P3_UM_AMHQ_1_UNITE` → `P3_TPL_AMHQ_1_UNITE` → `P3_TPL_AMHQ_2_ZONE` / `P3_TPL_AMHQ_3_TOTAL`

| Entité | Zone / Pièce | Fichier source |
|--------|-------------|----------------|
| `sensor.eclairage_appart_2_quotidien_um_kwh_tpl` | Entrée + Couloir (2 lampes) | `P3_TPL_AMHQ_2_ZONE` |
| `sensor.eclairage_salon_5_quotidien_um_kwh_tpl` | Salon (5 lampes) | `P3_TPL_AMHQ_2_ZONE` |
| `sensor.eclairage_cuisine_1_quotidien_um_kwh_tpl` | Cuisine (1 lampe) | `P3_TPL_AMHQ_2_ZONE` |
| `sensor.eclairage_bureau_5_quotidien_um_kwh_tpl` | Bureau (5 lampes) | `P3_TPL_AMHQ_2_ZONE` |
| `sensor.eclairage_sdb_2_quotidien_um_kwh_tpl` | SDB (2 lampes) | `P3_TPL_AMHQ_2_ZONE` |
| `sensor.eclairage_chambre_4_quotidien_um_kwh_tpl` | Chambre (4 lampes) | `P3_TPL_AMHQ_2_ZONE` |
| `sensor.eclairage_total_unit_quotidien_kwh_tpl` | **TOTAL appartement (19)** | `P3_TPL_AMHQ_3_TOTAL` |

### kWh mensuels — `sensor.eclairage_*_mensuel_um_kwh_tpl`

> Mêmes zones, cycle mensuel

| Entité | Zone / Pièce | Fichier source |
|--------|-------------|----------------|
| `sensor.eclairage_appart_2_mensuel_um_kwh_tpl` | Entrée + Couloir | `P3_TPL_AMHQ_2_ZONE` |
| `sensor.eclairage_salon_5_mensuel_um_kwh_tpl` | Salon | `P3_TPL_AMHQ_2_ZONE` |
| `sensor.eclairage_cuisine_1_mensuel_um_kwh_tpl` | Cuisine | `P3_TPL_AMHQ_2_ZONE` |
| `sensor.eclairage_bureau_5_mensuel_um_kwh_tpl` | Bureau | `P3_TPL_AMHQ_2_ZONE` |
| `sensor.eclairage_sdb_2_mensuel_um_kwh_tpl` | SDB | `P3_TPL_AMHQ_2_ZONE` |
| `sensor.eclairage_chambre_4_mensuel_um_kwh_tpl` | Chambre | `P3_TPL_AMHQ_2_ZONE` |
| `sensor.eclairage_total_unit_mensuel_kwh_tpl` | **TOTAL appartement** | `P3_TPL_AMHQ_3_TOTAL` |

---

## 🐛 DÉPANNAGE

### Toutes les valeurs affichent N/A
Vérifier la chaîne en ordre : `P3_UM_AMHQ_1_UNITE` → `P3_TPL_AMHQ_1_UNITE` → `P3_TPL_AMHQ_2_ZONE`.
Les `_um_kwh_tpl` dépendent des `_um` qui dépendent eux-mêmes du Hue Bridge.

### Une pièce reste blanche alors que la lumière est allumée
L'état du `sensor.lumiere_*_etat` n'est pas `Éteint` mais pas non plus reconnu comme allumé. Vérifier les valeurs possibles dans `etats_status.yaml`.

### Bureau/Chambre toujours blancs en mode Éco
Comportement voulu — `isEcoSensitive = true` maintient la couleur blanche en mode Éco.

---

## 📝 DÉPENDANCES

| Élément | Fichier source | Statut |
|---------|---------------|--------|
| `sensor.lumiere_*_etat` | `templates/P3_eclairage/ui_dashboard/etats_status.yaml` | ✅ Essentiel |
| `sensor.{slug}_{cycle}_um` | `utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml` | ✅ Base |
| `sensor.{slug}_{cycle}_um_kwh_tpl` | `templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_1_UNITE.yaml` | ✅ Relais |
| `sensor.eclairage_{zone}_{cycle}_um_kwh_tpl` | `templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_2_ZONE.yaml` | ✅ Essentiel |
| `sensor.eclairage_total_unit_{cycle}_kwh_tpl` | `templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_3_TOTAL.yaml` | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

### Configuration YAML (sources HA — ReBuild)

- `templates/P3_eclairage/ui_dashboard/etats_status.yaml` — `sensor.lumiere_*_etat`
- `utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml` — UM source (19 ampoules)
- `templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_1_UNITE.yaml` — relais kWh unité
- `templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_2_ZONE.yaml` — agrégat par zone
- `templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_3_TOTAL.yaml` — total appartement

### Documentation

- [`PAGE_ENERGIE_ECLAIRAGE.md`](./PAGE_ENERGIE_ECLAIRAGE.md) — YAML complet de la page `/dashboard-tablette/energie-lampes`
- [`docs/DEPENDANCES_GLOBALES.md`](../DEPENDANCES_GLOBALES.md) — chaîne de dépendances L2C3

---

← Retour : [`PAGE_HOME.md`](../HOME%20PAGE/PAGE_HOME.md) | → Suite : [`PAGE_ENERGIE_ECLAIRAGE.md`](./PAGE_ENERGIE_ECLAIRAGE.md)


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_ENERGIE_ECLAIRAGE]]  [[COULEURS_ECLAIRAGE_PAR_PIECE]]  [[L2C1_VIGNETTE_ENERGIE]]  [[L2C2_VIGNETTE_ENERGIE_CLIM]]  [[L3C1_VIGNETTE_ECLAIRAGE]]*
