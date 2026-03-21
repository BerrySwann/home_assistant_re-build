<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord/L3C3_vignette_stores.yaml` |
| 🔗 **Accès depuis** | Vue Home — L3C3 |
| 🔗 **tap →** | `/dashboard-tablette/stores` |
| 🏗️ **Layout** | `custom:button-card` — grille 3 colonnes (Pièce / Fenêtres / Stores) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3.x |

---

# 🪟 L3C3 — VIGNETTE FENÊTRES & STORES

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

Vignette affichant en un coup d'œil l'état de 4 fenêtres (ouvert/fermé) et de 2 stores motorisés (Salon + Bureau) pour les 4 pièces : Salon, Cuisine, Bureau, Chambre. Tap → page de commande détaillée `/dashboard-tablette/stores`.

Trois colonnes :
- **Pièce** : nom fixe (Salon / Cuisine / Bureau / Chambre)
- **Fenêtres** : état coloré — rouge `Ouvert` / vert `Fermé` / gris `N/A`
- **Stores** : état textuel brut du sensor de statut (ex: "Ouvert", "Fermé", "Arrêt")

### Intégrations requises

- ✅ **SONOFF SNZB-04** (Zigbee) — contacts fenêtres → `binary_sensor.contact_fenetre_*`
- ✅ **Zigbee2MQTT** (Zigbee) — stores motorisés → `cover.store_*`
- ✅ **Templates** — `sensor.store_*_status` (texte d'état volet)

### Cartes HACS

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Vignette — grille 3 colonnes avec JS |

---

## 🏗️ ARCHITECTURE

```
┌──────────────────────────────────────────┐
│  Commande Stores                         │
│  Pièces / Fenêtres / Stores              │  ← titre (row 1)
├────────────────┬─────────────┬───────────┤
│  Salon         │  Ouvert/    │  Ouvert/  │
│  Cuisine       │  Fermé/N/A  │  Fermé/   │  ← row 3 (grille 3 cols)
│  Bureau        │             │  Arrêt/…  │
│  Chambre       │             │           │
└────────────────┴─────────────┴───────────┘
tap → /dashboard-tablette/stores
```

**Grid-template-areas :**
```
"titre titre titre"
"espace espace espace"
"piece fenetres stores"
```

---

## 📍 CODE

```yaml
type: custom:button-card
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/stores
entities:
  - binary_sensor.contact_fenetre_salon_sonoff_contact
  - binary_sensor.contact_fenetre_cuisine_sonoff_contact
  - binary_sensor.contact_fenetre_bureau_sonoff_contact
  - binary_sensor.contact_fenetre_chambre_sonoff_contact
  - sensor.store_salon_status
  - sensor.store_bureau_status
triggers_update:
  - binary_sensor.contact_fenetre_salon_sonoff_contact
  - binary_sensor.contact_fenetre_cuisine_sonoff_contact
  - binary_sensor.contact_fenetre_bureau_sonoff_contact
  - binary_sensor.contact_fenetre_chambre_sonoff_contact
  - sensor.store_salon_status
  - sensor.store_bureau_status
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
        "espace espace espace"
        "piece fenetres stores"
    - grid-template-columns: 1fr 1fr 1fr
    - grid-template-rows: auto 14px auto
    - margin-top: 4.5px
  custom_fields:
    titre:
      - grid-area: titre
      - justify-self: center
      - text-align: center
      - font-weight: bold
    espace:
      - grid-area: espace
      - height: 10px
    piece:
      - grid-area: piece
      - justify-self: start
      - margin-left: 8px
      - text-align: left
    fenetres:
      - grid-area: fenetres
      - justify-self: end
      - text-align: center
    stores:
      - grid-area: stores
      - justify-self: end
      - margin-right: 7px
      - text-align: right
custom_fields:
  titre: |
    [[[
      return 'Commande Stores<BR>Pièces / Fenêtres / Stores';
    ]]]
  espace: |
    [[[ return ' '; ]]]
  piece: |
    [[[
      return `
      <div>
        <div>Salon</div>
        <div>Cuisine</div>
        <div>Bureau</div>
        <div>Chambre</div>
      </div>
      `;
    ]]]
  fenetres: |
    [[[
      function getColorForFenetreStatus(entityId) {
        const state = states[entityId]?.state;
        if (state === 'on') return '<span style="color: rgb(244,67,54);">Ouvert</span>';
        if (state === 'off') return '<span style="color: lightgreen;">Fermé</span>';
        return '<span style="color: #aaaaaa;">N/A</span>';
      }
      var salon = getColorForFenetreStatus('binary_sensor.contact_fenetre_salon_sonoff_contact');
      var cuisine = getColorForFenetreStatus('binary_sensor.contact_fenetre_cuisine_sonoff_contact');
      var bureau = getColorForFenetreStatus('binary_sensor.contact_fenetre_bureau_sonoff_contact');
      var chambre = getColorForFenetreStatus('binary_sensor.contact_fenetre_chambre_sonoff_contact');
      return `
      <div>
        <div>${salon}</div>
        <div>${cuisine}</div>
        <div>${bureau}</div>
        <div>${chambre}</div>
      </div>
      `;
    ]]]
  stores: |
    [[[
      function getStoreStatus(entityId) {
        const entity = states[entityId];
        if (!entity) return '-';
        const state = entity.state;
        if (state === 'unavailable' || state === 'unknown' || state === 'N/A') {
          return '<span style="color: #aaaaaa;">N/A</span>';
        }
        return state;
      }
      var salonStoreStatus = getStoreStatus('sensor.store_salon_status');
      var cuisineStoreStatus = getStoreStatus('sensor.store_cuisine_status');
      var bureauStoreStatus = getStoreStatus('sensor.store_bureau_status');
      var chambreStoreStatus = getStoreStatus('sensor.store_chambre_status');
      return `
      <div>
        <div>${salonStoreStatus}</div>
        <div>${cuisineStoreStatus}</div>
        <div>${bureauStoreStatus}</div>
        <div>${chambreStoreStatus}</div>
      </div>
      `;
    ]]]
```

---

## 🔢 LOGIQUE JS

### Colonne Fenêtres — `getColorForFenetreStatus(entityId)`

Lit l'état du `binary_sensor` :

| État HA | Signification physique | Rendu affiché |
|:--------|:----------------------|:--------------|
| `on` | Fenêtre ouverte (contact rompu) | `Ouvert` en rouge `rgb(244,67,54)` |
| `off` | Fenêtre fermée (contact établi) | `Fermé` en `lightgreen` |
| autre / absent | Indisponible | `N/A` en gris `#aaaaaa` |

### Colonne Stores — `getStoreStatus(entityId)`

Lit l'état textuel du `sensor.store_*_status` (template) et l'affiche brut. Les états `unavailable`, `unknown`, `N/A` sont remplacés par `N/A` gris.

> ⚠️ **Note** : `sensor.store_cuisine_status` et `sensor.store_chambre_status` sont lus dans le JS mais **absents de `entities:` et `triggers_update:`**. La vignette ne se rafraîchit pas automatiquement sur ces deux sensors. Si un store Cuisine ou Chambre est ajouté à l'avenir, les ajouter dans les deux listes.

---

## 📊 ENTITÉS UTILISÉES

### Contacts fenêtres (binary_sensor)

| Entité | Pièce | Matériel | `on` = |
|:-------|:------|:---------|:-------|
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | Salon | SONOFF SNZB-04 | Ouvert |
| `binary_sensor.contact_fenetre_cuisine_sonoff_contact` | Cuisine | SONOFF SNZB-04 | Ouvert |
| `binary_sensor.contact_fenetre_bureau_sonoff_contact` | Bureau | SONOFF SNZB-04 | Ouvert |
| `binary_sensor.contact_fenetre_chambre_sonoff_contact` | Chambre | SONOFF SNZB-04 | Ouvert |

### Statuts stores (sensor template)

| Entité | Store | Dans `entities:` | Dans `triggers_update:` |
|:-------|:------|:-----------------|:------------------------|
| `sensor.store_salon_status` | Salon | ✅ | ✅ |
| `sensor.store_bureau_status` | Bureau | ✅ | ✅ |
| `sensor.store_cuisine_status` | Cuisine | ⚠️ Non | ⚠️ Non |
| `sensor.store_chambre_status` | Chambre | ⚠️ Non | ⚠️ Non |

---

## 🐛 DÉPANNAGE

### Fenêtre affiche "N/A" en permanence
→ Vérifier que le `binary_sensor.contact_fenetre_*_sonoff_contact` est bien disponible (Zigbee2MQTT actif, capteur appairé).

### Colonne Stores ne se rafraîchit pas (Cuisine / Chambre)
→ Comportement attendu — `sensor.store_cuisine_status` et `sensor.store_chambre_status` ne sont pas dans `triggers_update:`. Ajouter ces entités si un store Cuisine/Chambre est installé.

### La carte reste blanche ou ne s'affiche pas
→ `custom:button-card` nécessite au moins une entité principale déclarée. Vérifier que la première entité de la liste est disponible.

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:button-card` | HACS | ✅ Essentiel |
| `binary_sensor.contact_fenetre_*` × 4 | SONOFF SNZB-04 / Zigbee | ✅ Essentiel |
| `sensor.store_salon_status` | Template (à documenter) | ✅ Requis |
| `sensor.store_bureau_status` | Template (à documenter) | ✅ Requis |

---

## 🔗 FICHIERS LIÉS

| Rôle | Chemin |
|------|--------|
| Page commande stores | `docs/L3C3_STORES/PAGE_STORES.md` |
| Config Zigbee2MQTT | Intégration UI |

---

← Retour : `docs/L3C2_*/` | → Suivant : `docs/L3C3_STORES/PAGE_STORES.md`
