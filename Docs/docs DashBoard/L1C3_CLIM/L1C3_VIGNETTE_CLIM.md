<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--22-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📍 **Position** | Dashboard HOME — Ligne 1, Colonne 3 |
| 🔗 **Navigation** | `/dashboard-tablette/clim` |
| 🃏 **Type de carte** | `custom:button-card` |
| 🌡️ **Entités** | 18 sensors/climates (5 pièces × état + consigne + mode global) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-22 |
| 🏠 **Version HA** | 2025.2.x → 2.0 |

---

# ❄️ VIGNETTE L1C3 : COMMANDES CLIM

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Rendu visuel](#rendu-visuel)
3. [Code source complet](#code-source-complet)
4. [Entités utilisées](#entités-utilisées)
5. [Logique JS — Colonne PIÈCE](#logique-js--colonne-pièce)
6. [Logique JS — Colonne MODE](#logique-js--colonne-mode)
7. [Logique JS — Colonne CONSIGNE](#logique-js--colonne-consigne)
8. [Paramètres clés](#paramètres-clés)
9. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Vignette récapitulative affichant l'état de **5 équipements de chauffage/clim** sur une grille 3 colonnes compacte. Chaque ligne montre le nom de la pièce (coloré selon la puissance), le mode actif (Cool/Heat/Fan/Off) et la consigne de température réglée.

Les 3 premières lignes sont des informations globales : T° moyenne appartement, Δ ADEME et le mode saison (été/hiver). Les 5 lignes suivantes correspondent à chaque pièce.

### Caractéristiques
- Grille 3 colonnes : `piece` | `mode` | `consigne`
- Ligne 1 titre : "Commande Clim."
- Lignes 2-4 : indicateurs globaux (T̄ Appart. / Δ Ademe / Mode →)
- Lignes 5-9 : 5 pièces (Salon / Cuisine / Bureau / SdB / Chambre)
- Couleurs dynamiques sur les noms : vert si actif / blanc si éteint / gris si indisponible
- Modes colorés : skyblue (Cool) / orange (Heat) / turquoise (Fan) / rouge (Off)
- Consignes en `°C` depuis les entités `climate.*`

---

## 🖼️ RENDU VISUEL

```
┌──────────────────────────────────────┐
│          Commande Clim.              │ ← titre (centré, bold)
│                                      │
│  T̄ Appart. ------   .     22.1°C    │
│  Δ Ademe --------   .     -6.5°C    │ ← vert si optimal, rouge si hors plage
│  Mode ->            Cool      .      │
│  Salon            Cool    22.0°C     │ ← skyblue (Cool)
│  Cuisine          Off     17.5°C     │ ← rouge (Off)
│  Bureau           Heat    21.0°C     │ ← orange (Heat)
│  SdB              Heat    22.0°C     │ ← orange (Heat)
│  Chambre          Off     20.0°C     │ ← rouge (Off)
└──────────────────────────────────────┘
  Bordure: 3px double white | aspect-ratio: 1/1 | font-size: 11px
```

### Structure CSS grid
```
grid-template-areas:
  "titre  titre   titre"
  "piece  mode    consigne"
grid-template-columns: 1fr  1fr  1fr
```

---

## 🔧 CODE SOURCE COMPLET

```yaml
type: custom:button-card
entities:
  - sensor.temperature_moyenne_interieure
  - sensor.delta_ademe_recommande
  - sensor.mode_ete_hiver_etat
  - sensor.clim_salon_etat
  - sensor.radiateur_cuisine_etat
  - sensor.clim_bureau_etat
  - sensor.sdb_soufflant_etat
  - sensor.clim_chambre_etat
  - sensor.salon_power_status
  - sensor.cuisine_power_status
  - sensor.bureau_power_status
  - sensor.sdb_soufflant_power_status
  - sensor.chambre_power_status
  - climate.clim_salon_rm4_mini
  - climate.radiateur_cuisine
  - climate.clim_bureau_rm4_mini
  - climate.soufflant_salle_de_bain
  - climate.clim_chambre_rm4_mini
triggers_update:
  - sensor.temperature_moyenne_interieure
  - sensor.delta_ademe_recommande
  - sensor.mode_ete_hiver_etat
  - sensor.clim_salon_etat
  - sensor.radiateur_cuisine_etat
  - sensor.clim_bureau_etat
  - sensor.sdb_soufflant_etat
  - sensor.clim_chambre_etat
  - sensor.salon_power_status
  - sensor.cuisine_power_status
  - sensor.bureau_power_status
  - sensor.sdb_soufflant_power_status
  - sensor.chambre_power_status
  - climate.clim_salon_rm4_mini
  - climate.radiateur_cuisine
  - climate.clim_bureau_rm4_mini
  - climate.soufflant_salle_de_bain
  - climate.clim_chambre_rm4_mini
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/clim
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
        "piece mode consigne"
    - grid-template-columns: 1fr 1fr 1fr
    - grid-template-rows: auto auto auto
    - margin-top: 3px
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
    mode:
      - justify-self: start
      - margin-left: 15px
      - text-align: left
    consigne:
      - justify-self: end
      - margin-right: 6px
      - text-align: right
custom_fields:
  titre: Commande Clim.
  piece: |
    [[[
      const colorMap = {
        'Fan': '#00FF00',
        'on': 'lightgreen',
        'off': 'white',
        'default': '#aaaaaa'
      };
      function safeState(entityId, defaultValue = 'on') {
        return states[entityId]?.state || defaultValue;
      }
      function getColorForPowerStatus(powerStatus, mode) {
        if (mode === 'Fan') return colorMap['Fan'];
        if (powerStatus === 'on') return colorMap['on'];
        if (powerStatus === 'off') return colorMap['off'];
        return colorMap['default'];
      }
      const pieces = [
        { name: 'T̄ Appart. --------------', color: 'white' },
        { name: 'Δ Ademe --------------', color: 'white' },
        { name: 'Mode ->', color: 'white' },
        { name: 'Salon', power: safeState('sensor.salon_power_status'), mode: safeState('sensor.clim_salon_etat') },
        { name: 'Cuisine', power: safeState('sensor.cuisine_power_status'), mode: safeState('sensor.radiateur_cuisine_etat') },
        { name: 'Bureau', power: safeState('sensor.bureau_power_status'), mode: safeState('sensor.clim_bureau_etat') },
        { name: 'SdB', power: safeState('sensor.sdb_soufflant_power_status'), mode: safeState('sensor.sdb_soufflant_etat') },
        { name: 'Chambre', power: safeState('sensor.chambre_power_status'), mode: safeState('sensor.clim_chambre_etat') }
      ];
      return pieces.map(piece =>
        `<span style="display: block; text-align: left; line-height: 1.2; color: ${piece.color || getColorForPowerStatus(piece.power, piece.mode)};">${piece.name}</span>`
      ).join('');
    ]]]
  mode: |
    [[[
      const colorMap = {
        'cool': 'skyblue',
        'heat': '#FFA500',
        'fan': 'turquoise',
        'off': '#F44336',
        'N/A': '#aaaaaa',
        'default': '#aaaaaa'
      };
      function safeState(entityId, defaultValue = 'off') {
        const state = states[entityId]?.state?.trim()?.toLowerCase() || defaultValue;
        if (state === 'unknown' || state === 'unavailable') return 'N/A';
        return state === 'fan_only' ? 'fan' : state;
      }
      function getColorForMode(mode) {
        return colorMap[mode] || colorMap['default'];
      }
      function formatMode(mode) {
        const color = getColorForMode(mode);
        const formattedMode = mode.charAt(0).toUpperCase() + mode.slice(1);
        return `<span style="display: block; text-align: left; line-height: 1.2; color: ${color};">${formattedMode}</span>`;
      }
      const modes = [
        { entity: 'sensor.mode_ete_hiver_etat' },
        { entity: 'sensor.clim_salon_etat' },
        { entity: 'sensor.radiateur_cuisine_etat' },
        { entity: 'sensor.clim_bureau_etat' },
        { entity: 'sensor.sdb_soufflant_etat' },
        { entity: 'sensor.clim_chambre_etat' }
      ];
      return [
        '<span style="display: block; text-align: left; line-height: 1.2; color: transparent;">.</span>',
        '<span style="display: block; text-align: left; line-height: 1.2; color: transparent;">.</span>',
        ...modes.map(mode => formatMode(safeState(mode.entity)))
      ].join('');
    ]]]
  consigne: |
    [[[
      function safeState(entityId, attribute = 'temperature') {
        const entity = states[entityId];
        if (!entity) return 'N/A';
        if (entity.state && !isNaN(parseFloat(entity.state))) {
          return parseFloat(entity.state).toFixed(1);
        }
        if (entity.attributes && entity.attributes[attribute] !== undefined) {
          return parseFloat(entity.attributes[attribute]).toFixed(1);
        }
        return 'N/A';
      }
      function formatDisplay(value) {
        const color = value === 'N/A' ? '#aaaaaa' : 'inherit';
        const text = value === 'N/A' ? 'N/A' : value + '°C';
        return `<span style="display: block; text-align: right; line-height: 1.2; color: ${color};">${text}</span>`;
      }
      const deltaADEME = parseFloat(states['sensor.delta_ademe_recommande']?.state);
      const isCooling = states['sensor.mode_ete_hiver']?.state === 'cool';
      const deltaColor =
        !isNaN(deltaADEME) && isCooling && deltaADEME >= -8 && deltaADEME <= -4
          ? 'lightgreen'
          : !isNaN(deltaADEME) && isCooling
            ? '#FF0000'
            : 'white';
      const ademeDisplayValue = !isNaN(deltaADEME) ? `${deltaADEME.toFixed(1)}°C` : 'N/A';
      const tempMoyenne = safeState('sensor.temperature_moyenne_interieure');
      const consigneSalon = safeState('climate.clim_salon_rm4_mini');
      const consigneCuisine = safeState('climate.radiateur_cuisine');
      const consigneBureau = safeState('climate.clim_bureau_rm4_mini');
      const consigneSdB = safeState('climate.soufflant_salle_de_bain');
      const consigneChambre = safeState('climate.clim_chambre_rm4_mini');
      return [
        `<span style="display: block; text-align: right; line-height: 1.2; color: lightgreen;">${tempMoyenne}°C</span>`,
        `<span style="display: block; text-align: right; line-height: 1.2; color: ${deltaColor};">${ademeDisplayValue}</span>`,
        '<span style="display: block; text-align: right; line-height: 1.2;">.</span>',
        formatDisplay(consigneSalon),
        formatDisplay(consigneCuisine),
        formatDisplay(consigneBureau),
        formatDisplay(consigneSdB),
        formatDisplay(consigneChambre)
      ].join('');
    ]]]
```

---

## 📊 ENTITÉS UTILISÉES

| Entité | Source | Rôle |
|--------|--------|------|
| `sensor.temperature_moyenne_interieure` | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | T° moyenne appartement |
| `sensor.delta_ademe_recommande` | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | Delta T° int/ext (recommandation ADEME) |
| `sensor.mode_ete_hiver_etat` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Mode saison global (Cool/Heat/Fan/Off) |
| `sensor.clim_salon_etat` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | État clim salon |
| `sensor.radiateur_cuisine_etat` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | État radiateur cuisine |
| `sensor.clim_bureau_etat` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | État clim bureau |
| `sensor.sdb_soufflant_etat` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | État sèche-serviette SdB |
| `sensor.clim_chambre_etat` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | État clim chambre |
| `sensor.salon_power_status` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Puissance salon > 50W → on |
| `sensor.cuisine_power_status` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Puissance cuisine > 50W → on |
| `sensor.bureau_power_status` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Puissance bureau > 50W → on |
| `sensor.sdb_soufflant_power_status` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Puissance soufflant > 20W → on |
| `sensor.chambre_power_status` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Puissance chambre > 50W → on |
| `climate.clim_salon_rm4_mini` | `[NAT]` SmartIR | Consigne T° salon (attr: temperature) |
| `climate.radiateur_cuisine` | `[NAT]` Meross | Consigne T° cuisine (attr: temperature) |
| `climate.clim_bureau_rm4_mini` | `[NAT]` SmartIR | Consigne T° bureau (attr: temperature) |
| `climate.soufflant_salle_de_bain` | `[NAT]` Meross | Consigne T° soufflant SdB (attr: temperature) |
| `climate.clim_chambre_rm4_mini` | `[NAT]` SmartIR | Consigne T° chambre (attr: temperature) |

> Les 18 entités sont identiques dans `entities:` et `triggers_update:` — recalcul instantané à chaque changement.

> **Note `sensor.sdb_soufflant_etat`** : utilisé dans le JS colonne `mode` mais **absent de la liste `entities:`** — cela signifie qu'il ne déclenche pas de rafraîchissement automatique. Si nécessaire, l'ajouter à `triggers_update:`.

---

## 🎨 LOGIQUE JS — COLONNE PIÈCE

### Structure des 8 lignes
```
Ligne 1 : T̄ Appart. -------------- → blanc (fixe)
Ligne 2 : Δ Ademe -------------- → blanc (fixe)
Ligne 3 : Mode ->              → blanc (fixe)
Ligne 4 : Salon                → couleur selon power_status
Ligne 5 : Cuisine              → couleur selon power_status
Ligne 6 : Bureau               → couleur selon power_status
Ligne 7 : SdB                  → couleur selon power_status
Ligne 8 : Chambre              → couleur selon power_status
```

### `getColorForPowerStatus(powerStatus, mode)`

| Condition | Couleur | Signification |
|-----------|---------|---------------|
| `mode === 'Fan'` | `#00FF00` vert vif | Ventilation active |
| `powerStatus === 'on'` | `lightgreen` | Appareil consomme |
| `powerStatus === 'off'` | `white` | Éteint |
| autre | `#aaaaaa` | Indisponible |

---

## 🎨 LOGIQUE JS — COLONNE MODE

### Rendu des 8 lignes
```
Ligne 1 : transparent "."  (alignement T̄)
Ligne 2 : transparent "."  (alignement Δ)
Ligne 3 : Mode global      ← sensor.mode_ete_hiver_etat
Ligne 4 : Mode Salon       ← sensor.clim_salon_etat
Ligne 5 : Mode Cuisine     ← sensor.radiateur_cuisine_etat
Ligne 6 : Mode Bureau      ← sensor.clim_bureau_etat
Ligne 7 : Mode SdB         ← sensor.sdb_soufflant_etat
Ligne 8 : Mode Chambre     ← sensor.clim_chambre_etat
```

### Palette des modes

| Valeur HA | Valeur JS | Couleur | HEX |
|-----------|-----------|---------|-----|
| `cool` | `cool` | Bleu ciel | `skyblue` |
| `heat` | `heat` | Orange | `#FFA500` |
| `fan_only` | `fan` | Turquoise | `turquoise` |
| `off` | `off` | Rouge | `#F44336` |
| `unknown`/`unavailable` | `N/A` | Gris | `#aaaaaa` |

> `fan_only` → `fan` : normalisation réalisée dans `safeState()` avant formatage.

---

## 🎨 LOGIQUE JS — COLONNE CONSIGNE

### Rendu des 8 lignes
```
Ligne 1 : T° moyenne appart  → lightgreen (toujours)
Ligne 2 : Δ ADEME            → couleur conditionnelle (vert/rouge/blanc)
Ligne 3 : "."                → spacer (invisible)
Ligne 4 : Consigne Salon     → inherit ou #aaaaaa si N/A
Ligne 5 : Consigne Cuisine   → inherit ou #aaaaaa si N/A
Ligne 6 : Consigne Bureau    → inherit ou #aaaaaa si N/A
Ligne 7 : Consigne SdB       → inherit ou #aaaaaa si N/A
Ligne 8 : Consigne Chambre   → inherit ou #aaaaaa si N/A
```

### Logique Δ ADEME

| Condition | Couleur | Signification |
|-----------|---------|---------------|
| Mode `cool` ET delta ∈ [-8, -4] | `lightgreen` | Plage optimale ADEME |
| Mode `cool` ET delta hors [-8, -4] | `#FF0000` | Hors recommandation |
| Mode `heat` ou autre | `white` | Neutre (non applicable en hiver) |

> La recommandation ADEME préconise un écart de 4°C à 8°C entre T° intérieure et extérieure en climatisation.

### `safeState()` pour les consignes climate
```javascript
// Priorité 1 : state numérique direct
if (entity.state && !isNaN(parseFloat(entity.state))) → toFixed(1)
// Priorité 2 : attribut temperature
if (entity.attributes.temperature !== undefined) → toFixed(1)
// Fallback
return 'N/A'
```

---

## ⚙️ PARAMÈTRES CLÉS

| Paramètre | Valeur | Rôle |
|-----------|--------|------|
| `aspect-ratio` | `1/1` | Carré parfait |
| `border-style` | `double` | Bordure double blanche (3px) |
| `font-size` | `11px` | Compact pour tenir 8 lignes dans le carré |
| `line-height` | `1.2` | Espacement serré |
| `grid-template-columns` | `1fr 1fr 1fr` | 3 colonnes égales |
| `margin-top` | `3px` | Alignement vertical global |
| `margin-left` (piece) | `8px` | Marge gauche noms |
| `margin-left` (mode) | `15px` | Décalage centrage modes |
| `margin-right` (consigne) | `6px` | Marge droite consignes |

---

## 🐛 DÉPANNAGE

### La vignette affiche "N/A" partout
1. Vérifier que les templates P1 sont chargés : `Configuration → Vérifier la config`
2. `sensor.temperature_moyenne_interieure` doit être `numeric` — vérifier dans `Outils de développement → États`
3. Si `sensor.mode_ete_hiver_etat` est `unknown` : le template `ui_dashboard.yaml` n'est pas chargé

### Les modes ne changent pas après modification
1. `triggers_update` contient bien les 18 entités — la carte se recalcule automatiquement
2. `sensor.sdb_soufflant_etat` absent de `triggers_update` → ajouter si le SdB ne se rafraîchit pas

### Le Δ ADEME est toujours rouge en été
- Vérifier `sensor.delta_ademe_recommande` : il doit retourner une valeur négative (T° int < T° ext)
- Vérifier que `sensor.mode_ete_hiver` (sans `_etat`) retourne bien `cool` — ce sensor est différent de `sensor.mode_ete_hiver_etat`

### Les consignes affichent N/A
- Les entités `climate.*` doivent être disponibles (SmartIR connecté, Meross connecté)
- Si `climate.clim_*_rm4_mini` est `unavailable` → vérifier l'IR bridge (RM4 Mini)

---

## 📚 FICHIERS LIÉS

- Page destination : `docs/L1C3_CLIM/PAGE_CLIM.md`
- Templates P1 : `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml`
- Templates P1 Master : `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_CLIM]]  [[L1C1_VIGNETTE_METEO]]  [[L1C2_VIGNETTE_TEMPERATURES]]  [[L2C2_VIGNETTE_ENERGIE_CLIM]]*
