<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--01-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📍 **Position** | Dashboard HOME — Ligne 1, Colonne 3 |
| 🔗 **Navigation** | `/dashboard-tablette/temperatures` |
| 🃏 **Type de carte** | `custom:button-card` |
| 🌡️ **Entités** | 14 sensors (7 pièces × temp + humidité) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-01 |
| 🏠 **Version HA** | 2025.1.x → 2.0 |

---

# 🌡️ VIGNETTE L1C3 : TEMPÉRATURES PAR PIÈCE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Rendu visuel](#rendu-visuel)
3. [Architecture de la grille](#architecture-de-la-grille)
4. [Code source complet](#code-source-complet)
5. [Anatomie des custom_fields](#anatomie-des-custom_fields)
6. [Logique JavaScript](#logique-javascript)
7. [Palettes de couleurs](#palettes-de-couleurs)
8. [Entités utilisées](#entités-utilisées)
9. [Modifications courantes](#modifications-courantes)
10. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Cette vignette affiche en **temps réel** la température et l'humidité de chaque pièce de l'appartement dans un format compact (carré 1:1). Elle sert de point d'entrée vers la page détaillée des courbes de température.

**Ce qu'elle fait :**
- Liste les 7 pièces surveillées (Balcon Nord, Salon, Cellier, Cuisine, Bureau, SdB, Chambre)
- Colore chaque température selon un gradient thermique (bleu froid → vert confort → rouge danger)
- Colore l'humidité en orange/rouge selon les seuils d'inconfort
- Affiche `N/A` si un sensor est indisponible (protection contre les états `unknown`/`unavailable`)
- Se rafraîchit en temps réel via `triggers_update` sur les 14 sensors

---

## 🖼️ RENDU VISUEL

```
┌─────────────────────────────┐
│    Courbes Température      │  ← titre (bold, centré)
├──────────┬──────┬───┬───────┤
│ Balcon N.│19.5°C│   │  62.0%│
│ Salon    │21.2°C│   │  58.3%│
│ Cellier  │17.8°C│   │  71.2%│  ← orange (>55%)
│ Cuisine  │20.1°C│   │  49.5%│
│ Bureau   │22.0°C│   │  55.0%│
│ SdB      │23.5°C│   │  78.4%│  ← rouge (>75%)
│ Chambre  │20.8°C│   │  52.1%│
└──────────┴──────┴───┴───────┘
  piece      temp  esp  humidite
```

> La colonne `espace` (0.5fr) est un séparateur visuel vide entre temp et humidité.

---

## 🏗️ ARCHITECTURE DE LA GRILLE

```
grid-template-areas:
  "titre   titre   titre   titre  "   ← ligne 1 : titre pleine largeur
  "piece   temp    espace  humidite"  ← ligne 2 : données
```

### Proportions des colonnes

| Zone | Taille | Alignement | Rôle |
|:-----|:-------|:-----------|:-----|
| `piece` | `1fr` | gauche + marge 8px | Noms des pièces |
| `temp` | `1fr` | centre + marge 35px | Températures colorées |
| `espace` | `0.5fr` | centre | Séparateur vide (`&nbsp;`) |
| `humidite` | `1fr` | droite + marge 6px | Humidités colorées |

> **Pourquoi `margin-left: 35px` sur temp ?**
> Compense le fait que la colonne `piece` (texte gauche) empiète visuellement — décale temp vers le centre réel de sa zone.

---

## 📄 CODE SOURCE COMPLET

```yaml
type: custom:button-card
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/temperatures
entities:
  - sensor.th_balcon_nord_temperature
  - sensor.th_balcon_nord_humidity
  - sensor.th_salon_temperature
  - sensor.th_salon_humidity
  - sensor.th_cellier_temperature
  - sensor.th_cellier_humidity
  - sensor.th_cuisine_temperature
  - sensor.th_cuisine_humidity
  - sensor.th_bureau_temperature
  - sensor.th_bureau_humidity
  - sensor.th_salle_de_bain_temperature
  - sensor.th_salle_de_bain_humidity
  - sensor.th_chambre_temperature
  - sensor.th_chambre_humidity
triggers_update:
  - sensor.th_balcon_nord_temperature
  - sensor.th_balcon_nord_humidity
  - sensor.th_salon_temperature
  - sensor.th_salon_humidity
  - sensor.th_cellier_temperature
  - sensor.th_cellier_humidity
  - sensor.th_cuisine_temperature
  - sensor.th_cuisine_humidity
  - sensor.th_bureau_temperature
  - sensor.th_bureau_humidity
  - sensor.th_salle_de_bain_temperature
  - sensor.th_salle_de_bain_humidity
  - sensor.th_chambre_temperature
  - sensor.th_chambre_humidity
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
        "titre titre titre titre"
        "piece temp espace humidite"
    - grid-template-columns: 1fr 1fr 0.5fr 1fr
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
    temp:
      - justify-self: center
      - margin-left: 35px
      - text-align: center
    espace:
      - justify-self: center
      - margin-left: 0px
      - text-align: center
    humidite:
      - justify-self: end
      - margin-right: 6px
      - text-align: right
custom_fields:
  titre: |
    [[[ return 'Courbes Température' ]]]
  piece: |
    [[[
      return '<span style="display: block; text-align: left; line-height: 1.2;">Balcon N.</span>' +
             '<span style="display: block; text-align: left; line-height: 1.2;">Salon</span>' +
             '<span style="display: block; text-align: left; line-height: 1.2;">Cellier</span>' +
             '<span style="display: block; text-align: left; line-height: 1.2;">Cuisine</span>' +
             '<span style="display: block; text-align: left; line-height: 1.2;">Bureau</span>' +
             '<span style="display: block; text-align: left; line-height: 1.2;">SdB</span>' +
             '<span style="display: block; text-align: left; line-height: 1.2;">Chambre</span>';
    ]]]
  temp: |
    [[[
      function getTemperatureColor(temp) {
        if (temp === 'NaN') return '#aaaaaa';
        var t = parseFloat(temp);
        if (t < 5)  return '#3674B5';
        if (t < 13) return '#578FCA';
        if (t < 19) return '#A1E3F9';
        if (t < 25) return 'lightgreen';
        if (t < 32) return '#FFD700';
        if (t < 36) return '#FFA500';
        if (t < 40) return '#F44336';
        return 'lightgreen';
      }
      function formatTemp(entityId) {
        var s = states[entityId]?.state;
        var val = (s && s !== 'unknown' && s !== 'unavailable') ? parseFloat(s).toFixed(1) : 'NaN';
        var color = getTemperatureColor(val);
        var text = val === 'NaN' ? 'N/A' : val + '°C';
        return `<span style="display: block; text-align: center; line-height: 1.2; color: ${color};">${text}</span>`;
      }
      return formatTemp('sensor.th_balcon_nord_temperature') +
             formatTemp('sensor.th_salon_temperature') +
             formatTemp('sensor.th_cellier_temperature') +
             formatTemp('sensor.th_cuisine_temperature') +
             formatTemp('sensor.th_bureau_temperature') +
             formatTemp('sensor.th_salle_de_bain_temperature') +
             formatTemp('sensor.th_chambre_temperature');
    ]]]
  espace: |
    [[[
      return Array(7).fill('<span style="display: block; text-align: center; line-height: 1.2;">&nbsp;&nbsp;</span>').join('');
    ]]]
  humidite: |
    [[[
      function getHumidityColor(h) {
        if (h === 'NaN') return '#aaaaaa';
        var val = parseFloat(h);
        if (val > 75) return '#F44336';
        if (val > 55) return '#FFA500';
        return 'white';
      }
      function formatHum(entityId) {
        var s = states[entityId]?.state;
        var val = (s && s !== 'unknown' && s !== 'unavailable') ? parseFloat(s).toFixed(1) : 'NaN';
        var color = getHumidityColor(val);
        var text = val === 'NaN' ? 'N/A' : val + '%';
        return `<span style="display: block; text-align: right; line-height: 1.2; color: ${color};">${text}</span>`;
      }
      return formatHum('sensor.th_balcon_nord_humidity') +
             formatHum('sensor.th_salon_humidity') +
             formatHum('sensor.th_cellier_humidity') +
             formatHum('sensor.th_cuisine_humidity') +
             formatHum('sensor.th_bureau_humidity') +
             formatHum('sensor.th_salle_de_bain_humidity') +
             formatHum('sensor.th_chambre_humidity');
    ]]]
```

---

## 🔬 ANATOMIE DES CUSTOM_FIELDS

### `titre`
Affiche simplement le texte statique "Courbes Température". Aucune donnée dynamique — juste un label de navigation.

```javascript
[[[ return 'Courbes Température' ]]]
```

---

### `piece`
Liste statique des 7 noms de pièces, chacun dans un `<span>` avec `display: block` pour créer les 7 lignes verticales.

```javascript
// Chaque pièce = un bloc indépendant
'<span style="display: block; text-align: left; line-height: 1.2;">Balcon N.</span>'
```

> **Pourquoi `display: block` ?**
> Sans `display: block`, les spans se placent côte à côte (inline). `block` force chaque span sur sa propre ligne, alignant visuellement les 7 lignes de pièces avec les 7 lignes de températures et d'humidités.

---

### `temp`
Deux fonctions JavaScript :

**`getTemperatureColor(temp)`** → retourne la couleur HEX/CSS selon la valeur.

**`formatTemp(entityId)`** → lit l'état HA, gère les cas erreur, formate le HTML.

```javascript
// Lecture sécurisée de l'état
var s = states[entityId]?.state;
// Protection : si absent / unknown / unavailable → 'NaN'
var val = (s && s !== 'unknown' && s !== 'unavailable')
  ? parseFloat(s).toFixed(1)
  : 'NaN';
```

> **L'opérateur `?.`** (optional chaining) évite un crash si `states[entityId]` est `undefined`.

---

### `espace`
Génère 7 spans vides (`&nbsp;&nbsp;`) — un par ligne — pour maintenir l'alignement de la grille entre les colonnes temp et humidité.

```javascript
Array(7).fill('<span ...>&nbsp;&nbsp;</span>').join('')
```

> Sans cette colonne, les colonnes temp et humidité se colleraient visuellement.

---

### `humidite`
Même logique que `temp` avec `getHumidityColor(h)` et `formatHum(entityId)`.

---

## 🎨 PALETTES DE COULEURS

### Température

| Seuil | Couleur | HEX | Signification |
|:------|:--------|:----|:--------------|
| < 5°C | Bleu foncé | `#3674B5` | Froid extrême / hors gel |
| < 13°C | Bleu moyen | `#578FCA` | Froid |
| < 19°C | Bleu clair | `#A1E3F9` | Frais |
| < 25°C | Vert | `lightgreen` | ✅ Confort |
| < 32°C | Or | `#FFD700` | Chaud |
| < 36°C | Orange | `#FFA500` | Très chaud |
| < 40°C | Rouge | `#F44336` | ⚠️ Danger |
| `NaN` | Gris | `#aaaaaa` | Indisponible |

> ⚠️ **Bug connu** : le cas `≥ 40°C` retourne `lightgreen` (identique au confort). C'est un oubli dans le code — à corriger si une telle température est jamais atteinte (peu probable en intérieur).

### Humidité

| Seuil | Couleur | HEX | Signification |
|:------|:--------|:----|:--------------|
| ≤ 55% | Blanc | `white` | ✅ Normal |
| > 55% | Orange | `#FFA500` | Humidité élevée |
| > 75% | Rouge | `#F44336` | ⚠️ Très humide (risque moisissures) |
| `NaN` | Gris | `#aaaaaa` | Indisponible |

---

## 📡 ENTITÉS UTILISÉES

Toutes ces entités sont créées automatiquement par l'**intégration Zigbee** (sondes Sonoff SNZB-02). Aucun fichier YAML à créer.

| Entité | Pièce | Type | Source |
|:-------|:------|:-----|:-------|
| `sensor.th_balcon_nord_temperature` | Balcon Nord | Température | Zigbee - UI |
| `sensor.th_balcon_nord_humidity` | Balcon Nord | Humidité | Zigbee - UI |
| `sensor.th_salon_temperature` | Salon | Température | Zigbee - UI |
| `sensor.th_salon_humidity` | Salon | Humidité | Zigbee - UI |
| `sensor.th_cellier_temperature` | Cellier | Température | Zigbee - UI |
| `sensor.th_cellier_humidity` | Cellier | Humidité | Zigbee - UI |
| `sensor.th_cuisine_temperature` | Cuisine | Température | Zigbee - UI |
| `sensor.th_cuisine_humidity` | Cuisine | Humidité | Zigbee - UI |
| `sensor.th_bureau_temperature` | Bureau | Température | Zigbee - UI |
| `sensor.th_bureau_humidity` | Bureau | Humidité | Zigbee - UI |
| `sensor.th_salle_de_bain_temperature` | SdB | Température | Zigbee - UI |
| `sensor.th_salle_de_bain_humidity` | SdB | Humidité | Zigbee - UI |
| `sensor.th_chambre_temperature` | Chambre | Température | Zigbee - UI |
| `sensor.th_chambre_humidity` | Chambre | Humidité | Zigbee - UI |

> **`triggers_update`** : les 14 entités sont listées deux fois — une fois dans `entities` (pour l'accès via `states[]` en JS) et une fois dans `triggers_update` (pour déclencher le re-rendu de la carte à chaque changement de valeur).

---

## 🛠️ MODIFICATIONS COURANTES

### Ajouter une pièce

3 endroits à modifier en synchronisation :

**1. `entities` + `triggers_update`** — ajouter les 2 sensors :
```yaml
entities:
  - sensor.th_NOUVELLE_PIECE_temperature
  - sensor.th_NOUVELLE_PIECE_humidity
triggers_update:
  - sensor.th_NOUVELLE_PIECE_temperature
  - sensor.th_NOUVELLE_PIECE_humidity
```

**2. `custom_fields.piece`** — ajouter le span :
```javascript
'<span style="display: block; text-align: left; line-height: 1.2;">NomPiece</span>'
```

**3. `custom_fields.temp` + `custom_fields.humidite`** — ajouter les appels :
```javascript
formatTemp('sensor.th_NOUVELLE_PIECE_temperature')
formatHum('sensor.th_NOUVELLE_PIECE_humidity')
```

**4. `custom_fields.espace`** — mettre à jour le `Array(7)` → `Array(8)` :
```javascript
Array(8).fill('<span ...>&nbsp;&nbsp;</span>').join('')
```

---

### Changer les seuils de température

Dans `getTemperatureColor()`, modifier les valeurs `if (t < X)` :

```javascript
// Exemple : abaisser le seuil confort à 22°C au lieu de 25°C
if (t < 22) return 'lightgreen';  // était 25
if (t < 32) return '#FFD700';
```

---

### Corriger le bug ≥ 40°C

Remplacer le dernier `return` de `getTemperatureColor()` :

```javascript
// Avant (bug)
return 'lightgreen';

// Après (correct)
return '#8B0000';  // Rouge très foncé = température critique
```

---

### Changer le titre

```javascript
// custom_fields.titre
[[[ return 'Mon nouveau titre' ]]]
```

---

## 🐛 DÉPANNAGE

### Une pièce affiche `N/A`

La sonde Zigbee de cette pièce est hors ligne ou a perdu la connexion. Vérifier dans **Outils de développement → États** que le sensor existe et a une valeur numérique.

### Toutes les pièces affichent `N/A`

L'intégration Zigbee est coupée. Vérifier le coordinateur Zigbee (USB ou réseau) dans **Paramètres → Appareils et services → Zigbee**.

### Les températures ne se mettent pas à jour

Vérifier que `triggers_update` contient bien tous les sensors. Sans `triggers_update`, la carte ne se rafraîchit qu'au rechargement complet du dashboard.

### La grille est mal alignée

Problème de font-size ou de zoom navigateur. La vignette est calibrée pour `font-size: 11px`. Si tu changes la police, recalibrer `margin-left: 35px` sur la colonne `temp`.

### Les couleurs ne correspondent pas

Vérifier la version de `custom:button-card` (HACS). Les templates JS `[[[...]]]` nécessitent button-card v4.x minimum.

---

## 🔗 FICHIERS LIÉS

### Documentation
- Page détaillée : `docs/L1C3_TEMPERATURES/PAGE_TEMPERATURES.md` *(à créer)*

### Configuration YAML
- Aucun fichier sensor à créer — entités 100% Zigbee natif

---

← Retour : `docs/L1C1_METEO/L1C1_VIGNETTE_METEO.md` | → Suivant : `docs/L1C3_TEMPERATURES/PAGE_TEMPERATURES.md` *(à venir)*
