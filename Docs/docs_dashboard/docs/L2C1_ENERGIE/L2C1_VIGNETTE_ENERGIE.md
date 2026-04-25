<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--04--23-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord → Vue: Home → L2C1` |
| 🔗 **Accès depuis** | Vue principale Home → tap → `/dashboard-tablette/energie` |
| 🏗️ **Type carte** | `custom:button-card` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-04-23 |
| 🏠 **Version HA** | 2026.3.x |

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

**Bloc 1 — Énergie / Puissance** : titre `kWh -- Réel (W) -- kWh` — Mini (kWh) / Temps réel (W) / Maxi (kWh) avec code couleur dynamique sur Realtime et Maxi.

> - **Mini** = `value_min` sur 24h de l'UM quotidien → toujours 0 (l'UM part de 0 à minuit, ne peut que croître). Blanc fixe. Sert de marqueur de reset.
> - **Maxi** = `value_max` sur 24h → total kWh du jour. Seuils : rouge > 15 kWh / orange > 8 kWh.

**Bloc 2 — Coûts (€)** : Coût total **quotidien** + détail Heures Pleines / Heures Creuses, lus directement depuis 3 sensors pré-calculés : `sensor.genelec_appart_cout_total_quotidien`, `_cout_hp_quotidien`, `_cout_hc_quotidien`. Aucun calcul inline — pas de tarif EDF dans la vignette.

Tap → navigue vers la page détaillée `/dashboard-tablette/energie`.

### Intégrations requises

- ✅ **NODON** (smart plug général appartement) — `sensor.general_electric_appart_power`
- ✅ Sensors Genelec Appart — `sensor.genelec_appart_conso_mini_24h` / `sensor.genelec_appart_conso_maxi_24h` (via `P0_MINI_MAXI_AVG_Genelec_appart.yaml`)
- ✅ Sensors coûts quotidiens — `sensor.genelec_appart_cout_total/hp/hc_quotidien` (via `01_genelec_appart_AMHQ_cost.yaml`)

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

### mini — Énergie minimale du jour (kWh)

```javascript
const value = parseFloat(states['sensor.genelec_appart_conso_mini_24h']?.state) || 0;
return `<span style='color:white; font-weight:bold;'>${value.toFixed(0)} kWh</span>`;
```

> `genelec_appart_conso_mini_24h` = `value_min` sur 24h de `sensor.genelec_appart_quotidien_kwh_um`.
> **Valeur pratique : toujours 0** — l'UM repart de 0 à minuit. Blanc fixe, pas de seuil couleur.
> Source : `sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml`

---

### realtime — Puissance temps réel (W)

```javascript
const value = parseFloat(states['sensor.general_electric_appart_power']?.state || 0);
let color = 'white';
if (value > 4000)      { color = 'rgb(244,67,54)'; }  // rouge     > 4 kW
else if (value > 2000) { color = '#FFA500'; }          // orange    > 2 kW
else if (value > 1000) { color = 'lightgreen'; }       // vert      > 1 kW
return `<span style='color:${color}; font-weight:bold;'>${value} W</span>`;
```

> `general_electric_appart_power` = puissance instantanée du smart plug NODON général appartement.

---

### maxi — Énergie maximale du jour (kWh)

```javascript
const value = parseFloat(states['sensor.genelec_appart_conso_maxi_24h']?.state) || 0;
let color = 'white';
if (value > 15)     { color = 'rgb(244,67,54)'; }  // rouge  > 15 kWh
else if (value > 8) { color = '#FFA500'; }           // orange >  8 kWh
return `<span style='color:${color}; font-weight:bold;'>${value.toFixed(0)} kWh</span>`;
```

> `genelec_appart_conso_maxi_24h` = `value_max` sur 24h de `sensor.genelec_appart_quotidien_kwh_um`.
> Représente le **total journalier accumulé** (pic = valeur courante de l'UM en fin de journée).
> Source : `sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml`

---

### titre_2 — Séparateur + En-tête Bloc 2

```javascript
return '__________________________<br><br>Coûts Total = H.P. + H.C.';
```

La ligne de tirets joue le rôle de séparateur visuel entre les deux blocs.

---

### toto — Coût total quotidien (€)

```javascript
const total = parseFloat(states['sensor.genelec_appart_cout_total_quotidien']?.state) || 0;
return `<span style="display:block; text-align:right; line-height:1.2; color:lightgreen;">
  ${total.toFixed(2)}<span style="font-size:9px;"> €</span>
</span>`;
```

> Lecture directe du sensor pré-calculé `genelec_appart_cout_total_quotidien`.
> Couleur fixe : `lightgreen`.

---

### hp — Coût Heures Pleines quotidien (€)

```javascript
const hp_total = parseFloat(states['sensor.genelec_appart_cout_hp_quotidien']?.state) || 0;
return `<span style="display:block; text-align:right; line-height:1.2;">
  ${hp_total.toFixed(2)}<span style="font-size:9px;"> €</span>
</span>`;
```

> Lecture directe du sensor pré-calculé `genelec_appart_cout_hp_quotidien`.
> Couleur : blanc (hérité).

---

### hc — Coût Heures Creuses quotidien (€)

```javascript
const hc_total = parseFloat(states['sensor.genelec_appart_cout_hc_quotidien']?.state) || 0;
return `<span style="display:block; text-align:right; line-height:1.2;">
  ${hc_total.toFixed(2)}<span style="font-size:9px;"> €</span>
</span>`;
```

> Lecture directe du sensor pré-calculé `genelec_appart_cout_hc_quotidien`.
> Couleur : blanc (hérité).

---

## 🎨 LOGIQUE JS & PALETTES COULEURS

### Puissance instantanée (realtime) — en W

| Seuil | Couleur | Code | Signification |
|:------|:--------|:-----|:--------------|
| > 4 000 W | Rouge | `rgb(244,67,54)` | Forte consommation (clim + tout) |
| > 2 000 W | Orange | `#FFA500` | Consommation élevée |
| > 1 000 W | Vert clair | `lightgreen` | Consommation modérée |
| ≤ 1 000 W | Blanc | `white` | Consommation normale |

### Énergie minimale (mini) — en kWh

| Seuil | Couleur | Signification |
|:------|:--------|:--------------|
| Toujours | Blanc | Valeur pratiquement toujours 0 (reset minuit). Pas de seuil. |

### Énergie maximale (maxi) — en kWh — total journalier accumulé

| Seuil | Couleur | Signification |
|:------|:--------|:--------------|
| > 15 kWh | Rouge | Journée très élevée |
| > 8 kWh  | Orange | Journée élevée |
| ≤ 8 kWh  | Blanc  | Journée normale |

### Coûts (toto / hp / hc)

| Champ | Couleur | Code | Logique |
|:------|:--------|:-----|:--------|
| `toto` | Vert clair | `lightgreen` | Lecture sensor pré-calculé `genelec_appart_cout_total_quotidien` |
| `hp`   | Blanc      | (hérité)     | Lecture sensor pré-calculé `genelec_appart_cout_hp_quotidien` |
| `hc`   | Blanc      | (hérité)     | Lecture sensor pré-calculé `genelec_appart_cout_hc_quotidien` |

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### ⚡ NODON — Puissance temps réel

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.general_electric_appart_power` | Puissance instantanée (W) — champ `realtime` | Smart plug NODON [UI] |

---

### 📈 Statistiques P0 — Mini / Maxi journaliers (kWh)

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.genelec_appart_conso_mini_24h` | `value_min` 24h de l'UM quotidien — toujours 0 (reset minuit) | `sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml` |
| `sensor.genelec_appart_conso_maxi_24h` | `value_max` 24h de l'UM quotidien — total kWh journalier accumulé | idem |

---

### 💰 Coûts quotidiens pré-calculés HP/HC

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.genelec_appart_cout_total_quotidien` | Coût total du jour (€) — champ `toto` | `templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml` |
| `sensor.genelec_appart_cout_hp_quotidien`    | Coût HP du jour (€) — champ `hp`   | idem |
| `sensor.genelec_appart_cout_hc_quotidien`    | Coût HC du jour (€) — champ `hc`   | idem |

> Les coûts sont **pré-calculés** dans le template YAML côté HA — pas de calcul inline dans la vignette.

### 🔄 triggers_update

La carte se met à jour sur changement de l'une des 6 entités ci-dessus (event-driven, pas de polling).

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:button-card` | HACS | ✅ Essentiel |
| Smart plug NODON (appartement général) | Intégration HA [UI] | ✅ Essentiel — fournit `general_electric_appart_power` |
| `sensor.genelec_appart_quotidien_kwh_um` | Utility Meter (utility_meter/) | ✅ Requis — source des stats mini/maxi |
| `P0_MINI_MAXI_AVG_Genelec_appart.yaml` | platform: statistics | ✅ Requis — fournit mini/maxi kWh |
| `01_genelec_appart_AMHQ_cost.yaml` | Template coûts | ✅ Requis — fournit `cout_total/hp/hc_quotidien` |
| Automation basculement HP/HC | `automations_corrige/energie/basculement_tarif_hphc.yaml` | ✅ Requis — split HP/HC correct |

---

## 🔗 FICHIERS LIÉS

| Rôle | Chemin |
|------|--------|
| Dashboard principal | `dashbord_2026-03-20.yaml` |
| Riemann tampon NODON | `sensors/P0_Energie_total_diag/Genelec_appart/P0_kWh_genelec_appart.yaml` |
| UM quotidien kWh (total) | `utility_meter/P0_Energie_total/Genelec_appart/01_UM_AMHQ_cost.yaml` |
| UM HP/HC AMHQ | `utility_meter/P0_Energie_total/Genelec_appart/03_UM_genelec_appart_HPHC_AMHQ.yaml` |
| Statistiques mini/maxi (kWh) | `sensors/P0_Energie_total_diag/Genelec_appart/Genelec_appart_mini_maxi_avg.yaml` |
| Coûts HP/HC (4 périodes) | `templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml` |
| Ratios HC | `templates/P0_Energie_total_diag/Genelec_appart/02_ratio_hp_hc.yaml` |
| Page détail | `docs DashBoard/L2C1_ENERGIE/PAGE_ENERGIE.md` |

---

← Retour : `docs DashBoard/L1C2_TEMPERATURES/` | → Suivant : `docs DashBoard/L2C1_ENERGIE/PAGE_ENERGIE.md`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_ENERGIE]]  [[PAGE_ENERGIE_MENSUEL]]  [[PAGE_ENERGIE_TEMPS_REEL]]  [[COULEURS_PRISES_PAR_PIECE]]  [[L2C2_VIGNETTE_ENERGIE_CLIM]]  [[L2C3_VIGNETTE_ECLAIRAGE]]*
