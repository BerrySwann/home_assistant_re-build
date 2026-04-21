<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--04--17-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashboard-tablette` → Ligne 5, Colonne 2 |
| 🔗 **Tap** | `/dashboard-tablette/phone` |
| 🏗️ **Layout** | `custom:button-card` — grid 3 colonnes (nom / batterie / état) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-04-17 |
| 🏠 **Version HA** | 2026.3 |

> 📝 **Note** : L5C2 était initialement documenté comme "Batterie Portail" dans CLAUDE.md — le contenu réel est "Batterie Portables" (7 téléphones + tablette). CLAUDE.md mis à jour en conséquence.

---

# 📱 L5C2 — Vignette État Batterie Portables

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Logique d'affichage](#logique-daffichage)
3. [Code](#code)
4. [Entités utilisées](#entités-utilisées--provenance-complète)

---

## 🎯 VUE D'ENSEMBLE

Vignette-tableau affichant en temps réel le niveau de batterie et l'état de charge de **7 appareils mobiles** (4 téléphones Eric, 2 téléphones Mamour + 1 tablette). Layout CSS Grid 3 colonnes : Appareil / Niveau % coloré / Icône état.

### Intégrations requises
- ✅ Home Assistant Companion App (Android) — 7 appareils

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Vignette grid multi-entités avec JavaScript custom_fields |

---

## 🎨 LOGIQUE D'AFFICHAGE

### Colonne batterie (niveau %)

| Niveau | Couleur | Code |
|--------|---------|------|
| ≥ 80% | Vert | `lightgreen` |
| ≥ 50% | Orange clair | `orange` |
| ≥ 20% | Orange vif | `rgb(255,152,0)` |
| < 20% | Rouge | `rgb(244,67,54)` |
| unavailable / unknown | Gris | `"Éteint"` |

### Colonne état (icône)

| État `battery_state` | Icône |
|----------------------|-------|
| `discharging` | 🟢 |
| `charging_wireless` | 🟡 |
| `wireless` | 🟡 |
| `charging` | 🟠 |
| `full` | `Full` |
| unavailable / unknown | ⚫ |

---

## 📍 CODE — VIGNETTE

```yaml
type: custom:button-card
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/phone
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
        "nom batterie reserve"
    - grid-template-columns: 1fr 1fr 1fr
    - grid-template-rows: auto auto
    - margin-top: 4.5px
  custom_fields:
    titre:
      - grid-area: titre
      - justify-self: center
      - text-align: center
      - font-weight: bold
      - margin-top: 3px
    nom:
      - grid-area: nom
      - justify-self: start
      - margin-left: 4px
      - text-align: left
    batterie:
      - grid-area: batterie
      - justify-self: center
      - text-align: right
    reserve:
      - grid-area: reserve
      - justify-self: end
      - margin-right: 8px
      - text-align: right
custom_fields:
  titre: |
    [[[
      return 'État Batterie Portables';
    ]]]
  nom: |
    [[[
      return `
      <div>
        <div>POCO_E</div>
        <div>POCO_G</div>
        <div>1+10P_E</div>
        <div>1+10P_G</div>
        <div>GM1901</div>
        <div>SM-A53</div>
        <div>Tablette</div>
      </div>
      `;
    ]]]
  batterie: |
    [[[
      function getColorForBatteryLevel(batteryLevel) {
        const lvl = Number(batteryLevel);
        if (Number.isNaN(lvl)) return 'gray';
        if (lvl >= 80) return 'lightgreen';
        if (lvl >= 50) return 'orange';
        if (lvl >= 20) return 'rgb(255,152,0)';
        return 'rgb(244,67,54)';
      }
      function getDeviceStatus(entityId) {
        const st = states[entityId];
        if (!st || st.state === 'unavailable' || st.state === 'unknown') {
          return '<span style="color: gray;">Éteint</span>';
        }
        const lvl = Number(st.state);
        const color = getColorForBatteryLevel(lvl);
        const safe = Number.isNaN(lvl) ? '—' : `${lvl}%`;
        return `<span style="color: ${color};">${safe}</span>`;
      }
      const pocox7_e_Status   = getDeviceStatus('sensor.poco_x7_pro_battery_level');
      const pocox7_g_Status   = getDeviceStatus('sensor.poco_x7_pro_mamour_battery_level');
      const ne2213_e_Status   = getDeviceStatus('sensor.ne2213_eric_battery_level');
      const ne2213_g_Status   = getDeviceStatus('sensor.ne2213_mamour_battery_level');
      const gm1901Status      = getDeviceStatus('sensor.gm1901_battery_level');
      const smA530FStatus     = getDeviceStatus('sensor.sm_a530f_battery_level');
      const tabletteStatus    = getDeviceStatus('sensor.tablette_battery_level');
      return `
      <div>
        <div>${pocox7_e_Status}</div>
        <div>${pocox7_g_Status}</div>
        <div>${ne2213_e_Status}</div>
        <div>${ne2213_g_Status}</div>
        <div>${gm1901Status}</div>
        <div>${smA530FStatus}</div>
        <div>${tabletteStatus}</div>
      </div>
      `;
    ]]]
  reserve: |
    [[[
      function getBatteryStateIcon(entityId) {
        const state = states[entityId]?.state;
        if (!state || state === 'unknown' || state === 'unavailable') return '⚫';
        if (state === 'discharging')        return '🟢';
        if (state === 'charging_wireless')  return '🟡';
        if (state === 'wireless')           return '🟡';
        if (state === 'charging')           return '🟠';
        if (state === 'full')               return 'Full';
        return state;
      }
      const pocox7_e_BatteryState  = getBatteryStateIcon('sensor.poco_x7_pro_battery_state');
      const pocox7_g_BatteryState  = getBatteryStateIcon('sensor.poco_x7_pro_mamour_battery_state');
      const ne2213_e_BatteryState  = getBatteryStateIcon('sensor.ne2213_eric_battery_state');
      const ne2213_g_BatteryState  = getBatteryStateIcon('sensor.ne2213_mamour_battery_state');
      const gm1901BatteryState     = getBatteryStateIcon('sensor.gm1901_battery_state');
      const smA530FBatteryState    = getBatteryStateIcon('sensor.sm_a530f_battery_state');
      const tabletteBatteryState   = getBatteryStateIcon('sensor.tablette_battery_state');
      return `
      <div>
        <div>${pocox7_e_BatteryState}</div>
        <div>${pocox7_g_BatteryState}</div>
        <div>${ne2213_e_BatteryState}</div>
        <div>${ne2213_g_BatteryState}</div>
        <div>${gm1901BatteryState}</div>
        <div>${smA530FBatteryState}</div>
        <div>${tabletteBatteryState}</div>
      </div>
      `;
    ]]]
```

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🌐 Intégrations natives HA (Android Companion App)

| Appareil | Entité niveau | Entité état |
|----------|--------------|-------------|
| POCO X7 Pro (Eric) | `sensor.poco_x7_pro_battery_level` | `sensor.poco_x7_pro_battery_state` |
| POCO X7 Pro (Mamour) | `sensor.poco_x7_pro_mamour_battery_level` | `sensor.poco_x7_pro_mamour_battery_state` |
| OnePlus 10 Pro NE2213 (Eric) | `sensor.ne2213_eric_battery_level` | `sensor.ne2213_eric_battery_state` |
| OnePlus 10 Pro NE2213 (Mamour) | `sensor.ne2213_mamour_battery_level` | `sensor.ne2213_mamour_battery_state` |
| OnePlus 7 GM1901 | `sensor.gm1901_battery_level` | `sensor.gm1901_battery_state` |
| Samsung A8 SM-A530F | `sensor.sm_a530f_battery_level` | `sensor.sm_a530f_battery_state` |
| Tablette | `sensor.tablette_battery_level` | `sensor.tablette_battery_state` |

> Toutes ces entités sont natives — aucun fichier YAML à créer. Configurées automatiquement par l'app Companion HA (Android).

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| HA Companion App — 7 appareils (NE2213 Mamour actif 2026-04-17) | Intégration native | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

### Documentation
- [`PAGE_BATTERIES_PORTABLES.md`](./PAGE_BATTERIES_PORTABLES.md) — page détaillée par appareil

---

← Retour : `L5C1_PILES_BATTERIES/` | → Suivant : `L5C3_MARIADB/`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_BATTERIES_PORTABLES]]  [[L5C1_VIGNETTE_BATTERIES]]  [[L5C3_VIGNETTE_MARIADB]]*
