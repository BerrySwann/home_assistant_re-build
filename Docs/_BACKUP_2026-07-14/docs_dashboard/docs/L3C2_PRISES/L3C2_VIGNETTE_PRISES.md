<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashboard-tablette` → Ligne 3, Colonne 2 |
| 🔗 **Tap** | `/dashboard-tablette/prises` |
| 🏗️ **Layout** | `custom:button-card` — grid 2 cols (Pièce / État) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3 |

---

# 🔌 L3C2 — Vignette Commandes Éco (Prises)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Code](#code--vignette)
3. [Entités utilisées](#entités-utilisées--provenance-complète)
4. [Logique JS](#logique-js)

---

## 🎯 VUE D'ENSEMBLE

Vignette affichant l'état ON/OFF de **6 prises/switches éco** clés de l'appartement. Disposition en grille 2 colonnes (Pièce | État coloré). Navigation vers la page prises au tap. Gestion des états `unavailable`/`unknown` → `N/A` grisé.

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Grille custom_fields — 2 colonnes Pièce / État |

---

## 📍 CODE — VIGNETTE

```yaml
type: custom:button-card
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/prises
entities:
  - switch.prise_horloge_ikea
  - switch.hue_smart_eco_pc_bureau
  - switch.prise_tete_de_lit_chambre
  - light.hue_smart_eco_salon
  - switch.prise_tv_salon_ikea
  - light.hue_smart_eco_tv_chambre
triggers_update:
  - switch.prise_horloge_ikea
  - switch.hue_smart_eco_pc_bureau
  - switch.prise_tete_de_lit_chambre
  - light.hue_smart_eco_salon
  - switch.prise_tv_salon_ikea
  - light.hue_smart_eco_tv_chambre
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
        "titre titre"
        "piece etat"
    - grid-template-columns: 1fr 1fr
    - grid-template-rows: auto
    - margin-top: 4.5px
  custom_fields:
    titre:
      - grid-area: titre
      - justify-self: center
      - text-align: center
      - font-weight: bold
    piece:
      - grid-area: piece
      - justify-self: start
      - margin-left: 8px
      - text-align: left
    etat:
      - grid-area: etat
      - justify-self: start
      - margin-left: 8px
      - text-align: left
custom_fields:
  titre: |
    [[[ return 'Commande éCO.' ]]]
  piece: |
    [[[
      return `
      <div>
        <div>Horloge</div>
        <div>Salon</div>
        <div>TV Salon</div>
        <div>PC Bureau</div>
        <div>TV Chambre</div>
        <div>Tête de Lit</div>
      </div>
      `;
    ]]]
  etat: |
    [[[
      function safeState(entityId) {
        const entity = states[entityId];
        if (!entity || entity.state === 'unavailable' || entity.state === 'unknown') {
          return 'N/A';
        }
        return entity.state;
      }
      function getColorForStatus(status) {
        if (status === 'N/A') return '#aaaaaa';
        return status === 'on' ? 'lightgreen' : 'rgb(244,67,54)';
      }
      function getStatusText(status) {
        if (status === 'N/A') return 'N/A';
        return status === 'on' ? 'Allumé' : 'Éteint';
      }
      const hStat  = safeState('switch.prise_horloge_ikea');
      const sStat  = safeState('light.hue_smart_eco_salon');
      const tsStat = safeState('switch.prise_tv_salon_ikea');
      const pStat  = safeState('switch.hue_smart_eco_pc_bureau');
      const tcStat = safeState('light.hue_smart_eco_tv_chambre');
      const tlStat = safeState('switch.prise_tete_de_lit_chambre');
      return `
      <div>
        <div style="color: ${getColorForStatus(hStat)};">${getStatusText(hStat)}</div>
        <div style="color: ${getColorForStatus(sStat)};">${getStatusText(sStat)}</div>
        <div style="color: ${getColorForStatus(tsStat)};">${getStatusText(tsStat)}</div>
        <div style="color: ${getColorForStatus(pStat)};">${getStatusText(pStat)}</div>
        <div style="color: ${getColorForStatus(tcStat)};">${getStatusText(tcStat)}</div>
        <div style="color: ${getColorForStatus(tlStat)};">${getStatusText(tlStat)}</div>
      </div>
      `;
    ]]]
```

---

## 🧠 LOGIQUE JS

### `safeState(entityId)`
Récupère l'état d'une entité avec protection contre `unavailable` / `unknown` → retourne `'N/A'`.

### `getColorForStatus(status)`
| Statut | Couleur |
|--------|---------|
| `'on'` | `lightgreen` |
| `'off'` | `rgb(244,67,54)` (rouge) |
| `'N/A'` | `#aaaaaa` (gris) |

### `getStatusText(status)`
| Statut | Texte affiché |
|--------|---------------|
| `'on'` | `Allumé` |
| `'off'` | `Éteint` |
| `'N/A'` | `N/A` |

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🔌 6 Prises / Switches surveillés

| Label vignette | Entité | Type | Pièce |
|----------------|--------|------|-------|
| Horloge | `switch.prise_horloge_ikea` | switch | 1. ENTRÉE |
| Salon | `light.hue_smart_eco_salon` | light | 4. SALON |
| TV Salon | `switch.prise_tv_salon_ikea` | switch | 4. SALON |
| PC Bureau | `switch.hue_smart_eco_pc_bureau` | switch | 7. BUREAU |
| TV Chambre | `light.hue_smart_eco_tv_chambre` | light | 9. CHAMBRE |
| Tête de Lit | `switch.prise_tete_de_lit_chambre` | switch | 9. CHAMBRE |

> ⚠️ **Mix switch / light :** 2 entités sont de type `light` (domaine `light.*`) et non `switch.*` — elles exposent tout de même un `.state` `on`/`off` compatible avec la logique JS.

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `switch.prise_horloge_ikea` | IKEA Dirigera (natif) | ✅ |
| `light.hue_smart_eco_salon` | Philips Hue (natif) | ✅ |
| `switch.prise_tv_salon_ikea` | IKEA Dirigera (natif) | ✅ |
| `switch.hue_smart_eco_pc_bureau` | Philips Hue (natif) | ✅ |
| `light.hue_smart_eco_tv_chambre` | Philips Hue (natif) | ✅ |
| `switch.prise_tete_de_lit_chambre` | Intégration native | ✅ |
| `custom:button-card` | HACS | ✅ |

---

## 🔗 FICHIERS LIÉS

- [`PAGE_PRISES.md`](./PAGE_PRISES.md) — page détaillée des prises *(à créer)*

---

← Retour : `L3C1_ECLAIRAGE/` | → Suite : `L3C3_STORES/`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_PRISES]]  [[COULEURS_PRISES_PAR_PIECE]]  [[L3C1_VIGNETTE_ECLAIRAGE]]  [[L3C3_VIGNETTE_STORES]]*
