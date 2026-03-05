<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--01-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord_2026-03-01.yalm → Vue: Home → L2C1` |
| 🔗 **Accès depuis** | Vue principale Home → tap → `/dashboard-tablette/energie` |
| 🏗️ **Type carte** | `custom:button-card` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-01 |
| 🏠 **Version HA** | 2025.2.x → v2.0 |

---

# ⚡ L2C1 — Vignette : Consommation Électrique Temps Réel

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Layout CSS Grid](#layout-css-grid)
3. [Style de la carte](#style-de-la-carte)
4. [Champs custom_fields](#champs-custom_fields)
5. [Logique JS & palettes couleurs](#logique-js--palettes-couleurs)
6. [Entités utilisées](#entités-utilisées--provenance-complète)

---

## 🎯 VUE D'ENSEMBLE

Vignette carrée (`aspect-ratio: 1/1`) affichant en temps réel la consommation électrique du logement en deux blocs :

**Bloc 1 — Puissance (W)** : Mini / Temps réel / Maxi avec code couleur dynamique selon les seuils de consommation.

**Bloc 2 — Coûts (€)** : Coût total mensuel et détail Heures Pleines / Heures Creuses calculés à la volée en JS en multipliant la consommation (kWh) par le tarif TTC en vigueur.

Tap → navigue vers la page détaillée `/dashboard-tablette/energie`.

### Intégrations requises

- ✅ **Ecojoko** (`ecojoko` ou `little_monkey`) — `sensor.ecojoko_*`
- ✅ **tarif_edf** (custom component) — `sensor.tarif_heures_*_ttc`
- ✅ Sensors calculés — `sensor.conso_mini` / `sensor.conso_maxi`

---

## 🏗️ LAYOUT CSS GRID

```
┌───────────────────────────────────────────────────┐
│         titre_1 : "Home Consumption               │  ← row 1 (full width)
│                   Mini -- Realtime -- Maxi"       │
├───────────┬───────────────────┬───────────────────┤
│   mini    │     realtime      │       maxi        │  ← row 2
│  (1fr)   │      (1fr)       │      (1fr)        │
├───────────┴───────────────────┴───────────────────┤
│    titre_2 : "Coûts Total = H.P. + H.C."          │  ← row 3 (full width)
├───────────┬───────────────────┬───────────────────┤
│   toto    │       hp          │        hc         │  ← row 4
│  (total)  │  (Heures Pleines) │ (Heures Creuses)  │
└───────────┴───────────────────┴───────────────────┘
```

```yaml
grid-template-areas: |
  "titre_1 titre_1 titre_1"
  "mini realtime maxi"
  "titre_2 titre_2 titre_2"
  "toto hp hc"
grid-template-columns: 1fr 1fr 1fr
grid-template-rows: auto auto auto auto
```

---

## 🎨 STYLE DE LA CARTE

```yaml
styles:
  card:
    - aspect-ratio: 1/1
    - border-radius: 10px
    - background: transparent
    - border-width: 3px
    - border-color: white
    - border-style: double    # ← double trait blanc encadrant la vignette
    - color: white
    - font-size: 11px
    - line-height: 1.2
```

> La bordure `double` crée un effet de cadre à double trait blanc, caractéristique de cette vignette sur le dashboard Home.

---

## 📐 CHAMPS CUSTOM_FIELDS

### titre_1 — En-tête Bloc 1

```javascript
return 'Conso. Appart.<br><br>Mini -- Realtime -- Maxi';
```

Texte statique HTML, centré en gras. Le `<br><br>` espace visuellement le titre des valeurs.

---

### mini — Puissance minimale du jour

```javascript
const value = parseFloat(states['sensor.conso_mini']?.state || 0);
let color = 'white';
if (value > 75)  { color = 'rgb(244,67,54)'; }   // rouge  > 75 W
else if (value > 50) { color = '#FFA500'; }        // orange > 50 W
return `<span style='color:${color}; font-weight:bold;'>${value} W</span>`;
```

> `conso_mini` représente la puissance de base minimale du logement (standby + base irréductible). Les seuils faibles (50/75 W) reflètent l'ordre de grandeur d'une consommation standby.

---

### realtime — Puissance temps réel (Ecojoko)

```javascript
const value = parseFloat(states['sensor.ecojoko_consommation_temps_reel']?.state || 0);
let color = 'white';
if (value > 4000)      { color = 'rgb(244,67,54)'; }  // rouge     > 4 kW
else if (value > 2000) { color = '#FFA500'; }          // orange    > 2 kW
else if (value > 1000) { color = 'lightgreen'; }       // vert      > 1 kW
return `<span style='color:${color}; font-weight:bold;'>${value} W</span>`;
```

---

### maxi — Puissance maximale du jour

```javascript
const value = parseFloat(states['sensor.conso_maxi']?.state || 0);
let color = 'white';
if (value > 4000)      { color = 'rgb(244,67,54)'; }  // rouge  > 4 kW
else if (value > 2000) { color = '#FFA500'; }          // orange > 2 kW
return `<span style='color:${color}; font-weight:bold;'>${value} W</span>`;
```

---

### titre_2 — Séparateur + En-tête Bloc 2

```javascript
return '__________________________<br><br>Coûts Total = H.P. + H.C.';
```

La ligne de tirets joue le rôle de séparateur visuel entre les deux blocs.

---

### toto — Coût total mensuel (€)

```javascript
const total = parseFloat(states['sensor.ecojoko_cout_total_mensuel']?.state || 0);
return `<span style='color:lightgreen; font-weight:bold;'>${total.toFixed(2)}<span style='font-size:9px'> €</span></span>`;
```

> Source : `sensor.ecojoko_cout_total_mensuel` (template = cost_hp + cost_hc).
> Couleur fixe : `lightgreen` (toujours — pas de seuil d'alerte sur le total).

---

### hp — Coût Heures Pleines (€)

```javascript
const hp_cost = parseFloat(states['sensor.ecojoko_cout_hp_mensuel']?.state || 0);
return `<span style='color:#ff9800; font-weight:bold;'>${hp_cost.toFixed(2)}<span style='font-size:9px'> €</span></span>`;
```

> Source : `sensor.ecojoko_cout_hp_mensuel` — calcul `ecojoko_hp_kWh × tarif_heures_pleines_ttc`.
> Couleur orange (`#ff9800`) — Heures Pleines = tarif plein.

---

### hc — Coût Heures Creuses (€)

```javascript
const hc_cost = parseFloat(states['sensor.ecojoko_cout_hc_mensuel']?.state || 0);
return `<span style='color:#03a9f4; font-weight:bold;'>${hc_cost.toFixed(2)}<span style='font-size:9px'> €</span></span>`;
```

> Source : `sensor.ecojoko_cout_hc_mensuel` — calcul `ecojoko_hc_kWh × tarif_heures_creuses_ttc`.
> Couleur bleu (`#03a9f4`) — Heures Creuses = tarif réduit.

---

## 🎨 LOGIQUE JS & PALETTES COULEURS

### Puissance instantanée (realtime)

| Seuil | Couleur | Code | Signification |
|:------|:--------|:-----|:--------------|
| > 4 000 W | Rouge | `rgb(244,67,54)` | Forte consommation (clim + tout) |
| > 2 000 W | Orange | `#FFA500` | Consommation élevée |
| > 1 000 W | Vert clair | `lightgreen` | Consommation modérée |
| ≤ 1 000 W | Blanc | `white` | Consommation normale |

### Puissance minimale (mini)

| Seuil | Couleur | Signification |
|:------|:--------|:--------------|
| > 75 W | Rouge | Standby anormalement élevé |
| > 50 W | Orange | Standby à surveiller |
| ≤ 50 W | Blanc | Normal |

### Puissance maximale (maxi)

| Seuil | Couleur | Signification |
|:------|:--------|:--------------|
| > 4 000 W | Rouge | Pic de conso exceptionnel |
| > 2 000 W | Orange | Pic notable |
| ≤ 2 000 W | Blanc | Normal |

### Coûts (toto / hp / hc)

| Champ | Couleur | Code | Logique |
|:------|:--------|:-----|:--------|
| `toto` | Vert clair | `lightgreen` | Fixe — total mensuel (cost_hp + cost_hc natifs Ecojoko) |
| `hp`   | Orange     | `#ff9800`    | Fixe — Heures Pleines (tarif plein) |
| `hc`   | Bleu       | `#03a9f4`    | Fixe — Heures Creuses (tarif réduit) |

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### ⚡ Ecojoko — Consommation & Coûts réseau

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.ecojoko_consommation_temps_reel` | Puissance instantanée (W) | Intégration Ecojoko [UI] |
| `sensor.ecojoko_consommation_hp_reseau` | Consommation HP du mois (kWh) | Intégration Ecojoko [UI] |
| `sensor.ecojoko_consommation_hc_reseau` | Consommation HC du mois (kWh) | Intégration Ecojoko [UI] |
| `sensor.ecojoko_cout_hp_mensuel` | Coût HP du mois (€) | `templates/P0_Energie_total_diag/Ecojoko/02_ecojoko_cost_AMHQ.yaml` |
| `sensor.ecojoko_cout_hc_mensuel` | Coût HC du mois (€) | idem |
| `sensor.ecojoko_cout_total_mensuel` | Coût total du mois (€) | idem |
| `sensor.tarif_heures_pleines_ttc` | Tarif HP €/kWh TTC (temps réel) | `custom_components/tarif_edf` [UI] |
| `sensor.tarif_heures_creuses_ttc` | Tarif HC €/kWh TTC (temps réel) | `custom_components/tarif_edf` [UI] |

> Calcul : `consommation_kWh × tarif_ttc` — les tarifs sont mis à jour automatiquement par `tarif_edf`.

### 📈 Puissances Min/Max journalières + Moyenne 1h

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.conso_mini` | Puissance minimale du jour (W) — talon/standby | `sensors/P0_Energie_total_diag/Ecojoko_mini_maxi/Ecojojoko_mini_maxi_avg_1h.yaml` |
| `sensor.conso_maxi` | Puissance maximale du jour (W) — pic | idem |
| `sensor.conso_moyenne_1h` | Puissance moyenne glissante 1h (W) | idem |

> `platform: statistics` sur `sensor.ecojoko_consommation_temps_reel` — fenêtre 24h, sampling 8640 points.

### 🔄 triggers_update

La carte se met à jour sur changement de l'une des 7 entités ci-dessus (pas de polling passif — uniquement event-driven).

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:button-card` | HACS | ✅ Essentiel |
| Intégration Ecojoko (`little_monkey`) | Custom component | ✅ Essentiel |
| `sensor.conso_mini` / `sensor.conso_maxi` | Sensor calculé (`platform: statistics`) | ✅ `sensors/P0_Energie_total_diag/Ecojoko_mini_maxi/` |
| `custom_components/tarif_edf` | Custom component | ✅ Requis — fournit `tarif_heures_*_ttc` |

---

## 🔗 FICHIERS LIÉS

| Rôle | Chemin GitHub |
|------|--------------|
| Dashboard principal | `dashbord_2026-03-01.yalm` |
| Coûts HP/HC (4 périodes) | `templates/P0_Energie_total_diag/Ecojoko/01_ecojoko_AMHQ_cost.yaml` |
| UM quotidien HP/HC | `utility_meter/P0_Energie_total/Ecojoko/02_UM_ecojoko_quotidien_live.yaml` |
| UM hebdo + annuel HP/HC | `utility_meter/P0_Energie_total/Ecojoko/01_UM_AMHQ_cost.yaml` |
| Mini / Maxi / Moy 1h (W) | `sensors/P0_Energie_total_diag/Ecojoko_mini_maxi/Ecojojoko_mini_maxi_avg_1h.yaml` |
| Page détail | `docs/L2C1_ENERGIE/PAGE_ENERGIE.md` *(à créer)* |

---

← Retour : `docs/L1C3_TEMPERATURES/` | → Suivant : `docs/L2C2_*/`
