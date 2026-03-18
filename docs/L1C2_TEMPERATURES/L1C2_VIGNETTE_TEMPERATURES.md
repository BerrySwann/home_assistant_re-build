<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--11-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📍 **Position** | Dashboard HOME — Ligne 1, Colonne 2 |
| 🔗 **Navigation** | `/dashboard-tablette/temperatures` |
| 🃏 **Type de carte** | `custom:button-card` |
| 🌡️ **Entités** | 14 sensors (7 pièces × temp + humidité) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-11 |
| 🏠 **Version HA** | 2025.2.x → 2.0 |

---

# 🌡️ VIGNETTE L1C2 : TEMPÉRATURES PAR PIÈCE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Rendu visuel](#rendu-visuel)
3. [Code source complet](#code-source-complet)
4. [Entités utilisées](#entités-utilisées)
5. [Logique JS — Températures](#logique-js--températures)
6. [Logique JS — Humidités](#logique-js--humidités)
7. [Paramètres clés](#paramètres-clés)
8. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Vignette de données en temps réel affichant les températures et humidités de **7 pièces** sur une grille 4 colonnes compacte. Contrairement à L1C1 (navigation pure), cette vignette est une **carte de données active** : elle se met à jour dès qu'un sensor change via `triggers_update`.

### Caractéristiques
- Grille 4 colonnes : `piece` | `temp` | `espace` | `humidite`
- Titre statique en ligne 1 : "Courbes Température"
- 7 lignes de données : Balcon N. / Salon / Cellier / Cuisine / Bureau / SdB / Chambre
- Températures colorées dynamiquement par gradient thermique (8 paliers)
- Humidités colorées selon seuils (>75% rouge, >55% orange, sinon blanc)
- Valeur `N/A` en gris (`#aaaaaa`) si sensor indisponible/inconnu

---

## 🖼️ RENDU VISUEL

```
┌─────────────────────────────────────────────┐
│           Courbes Température               │ ← titre (centré, bold)
│                                             │
│  Balcon N.   19.5°C   │    62.0%            │
│  Salon       22.3°C   │    55.8%            │
│  Cellier     18.1°C   │    48.2%            │
│  Cuisine     21.0°C   │    51.3%            │
│  Bureau      20.7°C   │    49.6%            │
│  SdB         24.2°C   │    78.1%            │ ← rouge (>75%)
│  Chambre     19.9°C   │    53.4%            │
└─────────────────────────────────────────────┘
  Bordure: 3px double white | Background: transparent | aspect-ratio: 1/1
```

### Structure CSS grid
```
grid-template-areas:
  "titre  titre  titre  titre"
  "piece  temp   espace humidite"
grid-template-columns: 1fr  1fr  0.5fr  1fr
```

---

## 🔧 CODE SOURCE COMPLET

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

## 📊 ENTITÉS UTILISÉES

| Entité | Source | Pièce |
|--------|--------|-------|
| `sensor.th_balcon_nord_temperature` | Zigbee - UI (Sonoff SNZB-02) | Balcon Nord (ext.) |
| `sensor.th_balcon_nord_humidity` | Zigbee - UI (Sonoff SNZB-02) | Balcon Nord (ext.) |
| `sensor.th_salon_temperature` | Zigbee - UI (Sonoff SNZB-02) | Salon |
| `sensor.th_salon_humidity` | Zigbee - UI (Sonoff SNZB-02) | Salon |
| `sensor.th_cellier_temperature` | Zigbee - UI (Sonoff SNZB-02) | Cellier |
| `sensor.th_cellier_humidity` | Zigbee - UI (Sonoff SNZB-02) | Cellier |
| `sensor.th_cuisine_temperature` | Zigbee - UI (Sonoff SNZB-02) | Cuisine |
| `sensor.th_cuisine_humidity` | Zigbee - UI (Sonoff SNZB-02) | Cuisine |
| `sensor.th_bureau_temperature` | Zigbee - UI (Sonoff SNZB-02) | Bureau |
| `sensor.th_bureau_humidity` | Zigbee - UI (Sonoff SNZB-02) | Bureau |
| `sensor.th_salle_de_bain_temperature` | Zigbee - UI (Sonoff SNZB-02) | Salle de Bain |
| `sensor.th_salle_de_bain_humidity` | Zigbee - UI (Sonoff SNZB-02) | Salle de Bain |
| `sensor.th_chambre_temperature` | Zigbee - UI (Sonoff SNZB-02) | Chambre |
| `sensor.th_chambre_humidity` | Zigbee - UI (Sonoff SNZB-02) | Chambre |

> Les 14 entités sont identiques dans `entities:` et `triggers_update:` — la vignette se recalcule instantanément à chaque changement de valeur.

---

## 🌡️ LOGIQUE JS — TEMPÉRATURES

### Gradient de couleurs (`getTemperatureColor`)

| Plage | Couleur | HEX | Signification |
|-------|---------|-----|---------------|
| `< 5°C` | Bleu foncé | `#3674B5` | Très froid |
| `5–13°C` | Bleu moyen | `#578FCA` | Froid |
| `13–19°C` | Bleu très clair | `#A1E3F9` | Frais |
| `19–25°C` | Vert clair | `lightgreen` | Confort |
| `25–32°C` | Or | `#FFD700` | Chaud |
| `32–36°C` | Orange | `#FFA500` | Très chaud |
| `36–40°C` | Rouge | `#F44336` | Critique |
| Indisponible | Gris | `#aaaaaa` | N/A |

### Logique défensive
```javascript
var s = states[entityId]?.state;
var val = (s && s !== 'unknown' && s !== 'unavailable') ? parseFloat(s).toFixed(1) : 'NaN';
```
Si le sensor est `unknown`, `unavailable` ou absent → affiche `N/A` en gris.

---

## 💧 LOGIQUE JS — HUMIDITÉS

### Seuils de couleurs (`getHumidityColor`)

| Seuil | Couleur | HEX | Signification |
|-------|---------|-----|---------------|
| `> 75%` | Rouge | `#F44336` | Excessif (risque condensation/moisissures) |
| `> 55%` | Orange | `#FFA500` | Élevé (attention) |
| `≤ 55%` | Blanc | `white` | Normal |
| Indisponible | Gris | `#aaaaaa` | N/A |

---

## ⚙️ PARAMÈTRES CLÉS

| Paramètre | Valeur | Rôle |
|-----------|--------|------|
| `aspect-ratio` | `1/1` | Carré parfait |
| `border-style` | `double` | Bordure double blanche (3px) |
| `font-size` | `11px` | Compact pour tenir 7 lignes dans le carré |
| `line-height` | `1.2` | Espacement serré entre les lignes |
| `grid-template-columns` | `1fr 1fr 0.5fr 1fr` | Colonne `espace` réduite à 0.5fr |
| `margin-top` | `4.5px` | Ajustement fin de l'alignement vertical global |
| `margin-left` (piece) | `8px` | Marge gauche noms de pièces |
| `margin-left` (temp) | `35px` | Décalage centrage températures |
| `margin-right` (humidite) | `6px` | Marge droite humidités |

---

## 🐛 DÉPANNAGE

### La vignette affiche "N/A" partout
1. Vérifier que les sensors Zigbee sont disponibles : `Outils de développement → États`
2. Vérifier que le coordinateur Zigbee est actif (intégrations HA)
3. Si un sensor est `unavailable` → vérifier la pile de la sonde Sonoff SNZB-02

### Les couleurs ne changent pas
1. `button-card` nécessite que les sensors soient dans `entities:` ET `triggers_update:`
2. Vérifier que les deux listes sont strictement identiques (14 entités chacune)
3. Vider le cache navigateur (`Ctrl+Shift+R`)

### La grille est désalignée
1. `font-size: 11px` est critique — ne pas augmenter sans tester visuellement
2. `line-height: 1.2` doit rester constant sur toute la carte
3. `margin-left: 35px` sur `temp` est un ajustement empirique — adapter si la police change

### Les valeurs se chevauchent
1. Vérifier que `grid-template-columns: 1fr 1fr 0.5fr 1fr` est bien appliqué
2. La colonne `espace` (0.5fr) sert de séparateur visuel — ne pas la supprimer

---

## 📚 FICHIERS LIÉS

- Page destination : `docs/L1C2_TEMPERATURES/PAGE_TEMPERATURES.md`

---

→ **Prochaine étape :** Consulter `PAGE_TEMPERATURES.md` pour la documentation complète de la page.
