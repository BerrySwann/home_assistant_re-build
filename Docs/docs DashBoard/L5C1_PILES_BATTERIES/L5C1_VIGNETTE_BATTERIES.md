<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--07-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord/L5C1_vignette_batteries.yaml` |
| 🔗 **Accès depuis** | Vue Home |
| 🔗 **tap →** | `/dashboard-tablette/battery-bp` |
| 🏗️ **Layout** | `custom:button-card` — grille 6 colonnes |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-07 |
| 🏠 **Version HA** | 2025.2.x → v2.0 |

---

# 🔋 L5C1 — VIGNETTE PILES & BATTERIES

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Code](#code)
4. [Logique JS — plages](#logique-js--plages)
5. [Entités — groupes HA](#entités--groupes-ha)
6. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Vignette compacte affichant un tableau 3 marques × 4 plages de batterie. Si un équipement d'un groupe descend sous 10 %, le count et la marque passent en rouge avec ⚠️. Un tap navigue vers la page détail.

### Intégrations requises

- ✅ **Philips Hue** (bridge natif) — `sensor.hue_smart_button_*_batterie`
- ✅ **Zigbee2MQTT [Z2M]** — `sensor.*_battery`
- ✅ **group** (natif HA) — `group.hue_devices`, `group.ikea_devices`, `group.sonoff_devices`

### Cartes HACS

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Vignette résumé marque × plage |

---

## 🏗️ ARCHITECTURE

```
┌──────┬──────┬───────┬───────┬───────┬───────┐
│count │marque│100-75%│ 75-50%│ 50-25%│ 25-0% │
│  HUE │  HUE │   n   │   n   │   n   │   n   │
│ IKEA │ IKEA │   n   │   n   │   n   │   n   │
│SONFF │SONFF │   n   │   n   │   n   │   n   │
└──────┴──────┴───────┴───────┴───────┴───────┘
⚠️ rouge si batterie ≤ 10% dans le groupe
tap → /dashboard-tablette/battery-bp
```

---

## 📍 CODE

```yaml
type: custom:button-card
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/battery-bp
entities:
  - group.hue_devices
  - group.ikea_devices
  - group.sonoff_devices
triggers_update:
  - group.hue_devices
  - group.ikea_devices
  - group.sonoff_devices
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
    - grid-template-areas: >
        "title title title title title title"
        "espace_debut espace_debut espace_debut espace_debut espace_debut espace_debut"
        "count marque 100_75_battery 75_50_battery 50_25_battery 25_0_battery"
        "espace_fin espace_fin espace_fin espace_fin espace_fin espace_fin"
    - grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr
    - grid-template-rows: auto 10px auto 18px
    - margin-top: 4.5px
  custom_fields:
    title:
      - grid-area: title
      - justify-self: center
      - text-align: center
      - font-weight: bold
    espace_debut:
      - grid-area: espace_debut
      - height: 10px
    count:
      - grid-area: count
      - justify-self: start
      - margin-left: 5px
      - text-align: right
    marque:
      - grid-area: marque
      - margin-right: "-21px"
      - text-align: left
    100_75_battery:
      - grid-area: 100_75_battery
      - justify-self: end
      - margin-right: "-15px"
      - text-align: right
    75_50_battery:
      - grid-area: 75_50_battery
      - justify-self: end
      - margin-right: "-9px"
      - text-align: right
    50_25_battery:
      - grid-area: 50_25_battery
      - justify-self: end
      - margin-right: "-2px"
      - text-align: right
    25_0_battery:
      - grid-area: 25_0_battery
      - justify-self: end
      - margin-right: 5px
      - text-align: right
    espace_fin:
      - grid-area: espace_fin
      - height: 10px
custom_fields:
  title: |
    [[[
      return 'Etat des Piles & Batteries<br><br> 100%> 75%> 50%> 25%>';
    ]]]
  espace_debut: "[[[return ' ';]]]"
  count: |
    [[[
      function hasBatteryBelowThreshold(groupName, threshold) {
        var group = states[groupName];
        if (!group) return false;
        return group.attributes.entity_id.some(entityId => {
          var entity = states[entityId];
          return entity && entity.state && parseInt(entity.state) <= threshold;
        });
      }
      function getStyledCount(groupName) {
        if (hasBatteryBelowThreshold(groupName, 10)) {
          return '<span style="color: rgb(244,67,54); font-weight: bold;">⚠️</span>';
        }
        var group = states[groupName];
        return group ? group.attributes.entity_id.length : 0;
      }
      return `<div>
        <div>${getStyledCount('group.hue_devices')}</div>
        <div>${getStyledCount('group.ikea_devices')}</div>
        <div>${getStyledCount('group.sonoff_devices')}</div>
      </div>`;
    ]]]
  marque: |
    [[[
      function hasBatteryBelowThreshold(groupName, threshold) {
        var group = states[groupName];
        if (!group) return false;
        return group.attributes.entity_id.some(entityId => {
          var entity = states[entityId];
          return entity && entity.state && parseInt(entity.state) <= threshold;
        });
      }
      function getStyledMarque(name, groupName) {
        if (hasBatteryBelowThreshold(groupName, 10)) {
          return `<span style="color: rgb(244,67,54); font-weight: bold;">${name}</span>`;
        }
        return name;
      }
      return `<div>
        <div>${getStyledMarque('HUE',   'group.hue_devices')}</div>
        <div>${getStyledMarque('IKEA',  'group.ikea_devices')}</div>
        <div>${getStyledMarque('SONOFF','group.sonoff_devices')}</div>
      </div>`;
    ]]]
  100_75_battery: |
    [[[
      function countBatteriesInRange(groupName, lo, up) {
        var group = states[groupName];
        if (!group) return 0;
        return group.attributes.entity_id.filter(id => {
          var e = states[id];
          return e && e.state && parseInt(e.state) <= up && parseInt(e.state) > lo;
        }).length;
      }
      function styled(n) { return n > 0 ? `<span style="color:#FFA500;">${n}</span>` : n; }
      return `<div>
        <div>${styled(countBatteriesInRange('group.hue_devices',   74, 100))}</div>
        <div>${styled(countBatteriesInRange('group.ikea_devices',  74, 100))}</div>
        <div>${styled(countBatteriesInRange('group.sonoff_devices',74, 100))}</div>
      </div>`;
    ]]]
  75_50_battery: |
    [[[
      function countBatteriesInRange(groupName, lo, up) {
        var group = states[groupName];
        if (!group) return 0;
        return group.attributes.entity_id.filter(id => {
          var e = states[id];
          return e && e.state && parseInt(e.state) <= up && parseInt(e.state) > lo;
        }).length;
      }
      function styled(n) { return n > 0 ? `<span style="color:#FFA500;">${n}</span>` : n; }
      return `<div>
        <div>${styled(countBatteriesInRange('group.hue_devices',   49, 74))}</div>
        <div>${styled(countBatteriesInRange('group.ikea_devices',  49, 74))}</div>
        <div>${styled(countBatteriesInRange('group.sonoff_devices',49, 74))}</div>
      </div>`;
    ]]]
  50_25_battery: |
    [[[
      function countBatteriesInRange(groupName, lo, up) {
        var group = states[groupName];
        if (!group) return 0;
        return group.attributes.entity_id.filter(id => {
          var e = states[id];
          return e && e.state && parseInt(e.state) <= up && parseInt(e.state) > lo;
        }).length;
      }
      function styled(n) { return n > 0 ? `<span style="color:#FFA500;">${n}</span>` : n; }
      return `<div>
        <div>${styled(countBatteriesInRange('group.hue_devices',   24, 49))}</div>
        <div>${styled(countBatteriesInRange('group.ikea_devices',  24, 49))}</div>
        <div>${styled(countBatteriesInRange('group.sonoff_devices',24, 49))}</div>
      </div>`;
    ]]]
  25_0_battery: |
    [[[
      function countBatteriesInRange(groupName, lo, up) {
        var group = states[groupName];
        if (!group) return 0;
        return group.attributes.entity_id.filter(id => {
          var e = states[id];
          return e && e.state && parseInt(e.state) <= up && parseInt(e.state) > lo;
        }).length;
      }
      function styled(n) { return n > 0 ? `<span style="color:#FFA500;">${n}</span>` : n; }
      return `<div>
        <div>${styled(countBatteriesInRange('group.hue_devices',   -1, 24))}</div>
        <div>${styled(countBatteriesInRange('group.ikea_devices',  -1, 24))}</div>
        <div>${styled(countBatteriesInRange('group.sonoff_devices',-1, 24))}</div>
      </div>`;
    ]]]
  espace_fin: "[[[return '----------------------------------------';]]]"
```

---

## 🔢 LOGIQUE JS — PLAGES

`state > lo && state <= up` — couverture continue 0–100 % sans trou :

| Colonne | Plage | `lo` | `up` |
|---------|-------|------|------|
| `100_75_battery` | 75–100 % | 74 | 100 |
| `75_50_battery` | 50–74 % | 49 | 74 |
| `50_25_battery` | 25–49 % | 24 | 49 |
| `25_0_battery` | 0–24 % | -1 | 24 |

**Alerte** : `hasBatteryBelowThreshold(group, 10)` → rouge + ⚠️ si `state <= 10`.

---

## ⚙️ ENTITÉS — GROUPES HA (`group.yaml`)

> Contenir uniquement des `sensor.*` à état numérique (%). Un `light.*` ou `switch.*` retourne `NaN`.

| Groupe | Contenu | Total |
|--------|---------|-------|
| `group.hue_devices` | 11 boutons HUE | 11 |
| `group.ikea_devices` | 8 boutons/détect. + 4 contacts fenêtres IKEA | 12 |
| `group.sonoff_devices` | 4 contacts fenêtres + 7 thermostats SONOFF | 11 |

---

## 🐛 DÉPANNAGE

### Vignette affiche 0 partout
1. Vérifier les 3 groupes dans `group.yaml`
2. Leurs entités doivent être des `sensor.*` à état numérique
3. Tester : `{{ states.group.hue_devices.attributes.entity_id }}`

### Batterie absente de toutes les colonnes
État `unavailable` / `unknown` → `parseInt()` = `NaN` → aucune comparaison ne passe.

---

## 📝 DÉPENDANCES

| Élément | Type | Statut |
|---------|------|--------|
| `group.hue_devices` | HA group | ✅ Essentiel |
| `group.ikea_devices` | HA group | ✅ Essentiel |
| `group.sonoff_devices` | HA group | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

- `dashbord/L5C1_vignette_batteries.yaml`
- `docs/L5C1_PILES_BATTERIES/PAGE_BATTERIES.md`

---

← Retour : `docs/WIFI_PRESENCE/VIGNETTE_WIFI_PRESENCE.md` | → Suivant : `PAGE_BATTERIES.md`
