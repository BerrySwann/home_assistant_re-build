<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--04--18-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord → Vue: Home → L2C1` |
| 🔗 **Accès depuis** | Vue principale Home → tap → `/dashboard-tablette/energie` |
| 🏗️ **Type carte** | `custom:button-card` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-04-18 |
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

**Bloc 1 — Énergie / Puissance** : Mini (kWh) / Temps réel (W) / Maxi (kWh) avec code couleur dynamique selon les seuils de consommation.

> ⚠️ **Changement vs version Ecojoko** : Mini et Maxi sont désormais en **kWh** (via `platform: statistics` sur l'UM quotidien NODON — remise à 0 à minuit), pas en W. Le champ Temps Réel reste en W (puissance instantanée NODON).
> - **Mini** = `value_min` sur 24h de l'UM quotidien → toujours 0 (l'UM part de 0 à minuit et ne fait qu'augmenter). Sert de marqueur de reset.
> - **Maxi** = `value_max` sur 24h de l'UM quotidien → total journalier accumulé (kWh du jour).

**Bloc 2 — Coûts (€)** : Coût total mensuel et détail Heures Pleines / Heures Creuses **calculés entièrement en JS inline** en multipliant `sensor.genelec_appart_hphc_mensuel_um_hp/hc` par `sensor.edf_tempo_price_blue_hp/hc`. Aucun sensor de coût pré-calculé n'est utilisé dans la vignette.

Tap → navigue vers la page détaillée `/dashboard-tablette/energie`.

### Intégrations requises

- ✅ **NODON** (smart plug général appartement) — `sensor.general_electric_appart_*`
- ✅ **tarif_edf** (custom component) — `sensor.edf_tempo_price_blue_hp` / `sensor.edf_tempo_price_blue_hc`
- ✅ Sensors Genelec Appart — `sensor.genelec_appart_conso_mini_24h` / `sensor.genelec_appart_conso_maxi_24h` (via `Genelec_appart_mini_maxi_avg.yaml`)

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
const value = parseFloat(states['sensor.genelec_appart_conso_mini_24h']?.state || 0);
let color = 'white';
if (value > 4)  { color = 'rgb(244,67,54)'; }    // rouge  > 4 kWh (anormal)
else if (value > 2) { color = '#FFA500'; }         // orange > 2 kWh (à surveiller)
return `<span style='color:${color}; font-weight:bold;'>${value.toFixed(3)} kWh</span>`;
```

> `genelec_appart_conso_mini_24h` = `value_min` sur 24h de `sensor.genelec_appart_quotidien_kwh_um` (UM quotidien NODON via Riemann).
> **Valeur pratique : toujours 0** — l'UM repart de 0 à minuit et ne peut que croître. Sert de marqueur visuel de reset.
> Source : `sensors/P0_Energie_total_diag/Genelec_appart/Genelec_appart_mini_maxi_avg.yaml`

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
const value = parseFloat(states['sensor.genelec_appart_conso_maxi_24h']?.state || 0);
let color = 'white';
if (value > 18)        { color = 'rgb(244,67,54)'; }  // rouge  > 18 kWh
else if (value > 15)   { color = '#FFA500'; }          // orange > 15 kWh
else if (value > 8)    { color = '#FFA500'; }          // orange >  8 kWh
return `<span style='color:${color}; font-weight:bold;'>${value.toFixed(3)} kWh</span>`;
```

> `genelec_appart_conso_maxi_24h` = `value_max` sur 24h de `sensor.genelec_appart_quotidien_kwh_um`.
> Représente le **total journalier accumulé** (pic = valeur courante de l'UM en fin de journée).
> Source : `sensors/P0_Energie_total_diag/Genelec_appart/Genelec_appart_mini_maxi_avg.yaml`

---

### titre_2 — Séparateur + En-tête Bloc 2

```javascript
return '__________________________<br><br>Coûts Total = H.P. + H.C.';
```

La ligne de tirets joue le rôle de séparateur visuel entre les deux blocs.

---

### toto — Coût total mensuel (€)

```javascript
const hp = parseFloat(states['sensor.genelec_appart_hphc_mensuel_um_hp']?.state || 0);
const hc = parseFloat(states['sensor.genelec_appart_hphc_mensuel_um_hc']?.state || 0);
const tarif_hp = parseFloat(states['sensor.edf_tempo_price_blue_hp']?.state || 0);
const tarif_hc = parseFloat(states['sensor.edf_tempo_price_blue_hc']?.state || 0);
const total = (hp * tarif_hp) + (hc * tarif_hc);
return `<span style="display:block; text-align:right; line-height:1.2; color:lightgreen;">
  ${total.toFixed(2)}<span style="font-size:9px;"> €</span>
</span>`;
```

> ⚠️ **Calcul inline** : le total est calculé à la volée — pas de sensor `genelec_appart_cout_total_mensuel` ici.
> Formule : `(HP_kWh × tarif_HP) + (HC_kWh × tarif_HC)`.
> Tarifs EDF Tempo Bleu : HP = 0.1494 €/kWh · HC = 0.1232 €/kWh.
> Couleur fixe : `lightgreen` (toujours — pas de seuil d'alerte sur le total).

---

### hp — Coût Heures Pleines (€)

```javascript
const hp_value = parseFloat(states['sensor.genelec_appart_hphc_mensuel_um_hp']?.state || 0);
const tarif_hp = parseFloat(states['sensor.edf_tempo_price_blue_hp']?.state || 0);
const hp_total = hp_value * tarif_hp;
return `<span style="display:block; text-align:right; line-height:1.2;">
  ${hp_total.toFixed(2)}<span style="font-size:9px;"> €</span>
</span>`;
```

> ⚠️ **Calcul inline** : `sensor.genelec_appart_hphc_mensuel_um_hp` × `sensor.edf_tempo_price_blue_hp`.
> Couleur : blanc (hérite de la couleur de la carte).

---

### hc — Coût Heures Creuses (€)

```javascript
const hc_value = parseFloat(states['sensor.genelec_appart_hphc_mensuel_um_hc']?.state || 0);
const tarif_hc = parseFloat(states['sensor.edf_tempo_price_blue_hc']?.state || 0);
const hc_total = hc_value * tarif_hc;
return `<span style="display:block; text-align:right; line-height:1.2;">
  ${hc_total.toFixed(2)}<span style="font-size:9px;"> €</span>
</span>`;
```

> ⚠️ **Calcul inline** : `sensor.genelec_appart_hphc_mensuel_um_hc` × `sensor.edf_tempo_price_blue_hc`.
> Couleur : blanc (hérite de la couleur de la carte).

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
| > 4 kWh | Rouge | Anormal (valeur min > 0 signale un problème de sensor) |
| > 2 kWh | Orange | À surveiller |
| ≤ 2 kWh | Blanc | Normal (pratiquement toujours 0 — reset minuit) |

### Énergie maximale (maxi) — en kWh — total journalier accumulé

| Seuil | Couleur | Signification |
|:------|:--------|:--------------|
| > 18 kWh | Rouge | Journée très élevée |
| > 15 kWh | Orange | Journée élevée |
| > 8 kWh | Orange | Journée modérée |
| ≤ 8 kWh | Blanc | Journée normale |

### Coûts (toto / hp / hc)

| Champ | Couleur | Code | Logique |
|:------|:--------|:-----|:--------|
| `toto` | Vert clair | `lightgreen` | Fixe — calcul inline `(HP×tarif_HP) + (HC×tarif_HC)` |
| `hp`   | Blanc      | (hérité)     | Calcul inline — `HP_kWh × tarif_HP` |
| `hc`   | Blanc      | (hérité)     | Calcul inline — `HC_kWh × tarif_HC` |

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### ⚡ NODON — Puissance & Énergie temps réel

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.general_electric_appart_power` | Puissance instantanée (W) — champ `realtime` | Smart plug NODON [UI] |
| `sensor.general_electric_appart_energy` | Énergie cumulée brute (kWh) — NODON brut | Smart plug NODON [UI] |

> ⚠️ `sensor.general_electric_appart_energy` n'est **pas** directement utilisé dans la vignette — il sert de source au capteur Riemann (`sensor.genelec_appart_totale_kwh`) qui alimente les UM.

---

### 📈 Statistiques P0 — Mini / Maxi journaliers (kWh)

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.genelec_appart_conso_mini_24h` | `value_min` 24h de l'UM quotidien — toujours 0 (reset minuit) | `sensors/P0_Energie_total_diag/Genelec_appart/Genelec_appart_mini_maxi_avg.yaml` |
| `sensor.genelec_appart_conso_maxi_24h` | `value_max` 24h de l'UM quotidien — total kWh journalier accumulé | idem |

> ⚠️ Ces sensors opèrent sur l'**énergie** (kWh), pas sur la puissance (W). Changement vs version Ecojoko qui fournissait des valeurs en W.

---

### 🔢 Utility Meters Mensuels HP/HC — base du calcul inline coûts

| Entité | Cycle | Source |
|--------|-------|--------|
| `sensor.genelec_appart_hphc_mensuel_um_hp` | monthly (HP) | `utility_meter/P0_Energie_total/Genelec_appart/03_UM_genelec_appart_HPHC_AMHQ.yaml` |
| `sensor.genelec_appart_hphc_mensuel_um_hc` | monthly (HC) | idem |

---

### 💰 Tarifs EDF Tempo Bleu

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.edf_tempo_price_blue_hp` | Tarif HP €/kWh TTC (0.1494 €) | `custom_components/tarif_edf` [UI] |
| `sensor.edf_tempo_price_blue_hc` | Tarif HC €/kWh TTC (0.1232 €) | `custom_components/tarif_edf` [UI] |

> ⚠️ Les coûts (champs `toto`, `hp`, `hc`) sont **calculés en JS inline** dans la vignette.
> Formule : `consommation_kWh × tarif_ttc` — les tarifs sont mis à jour automatiquement par `tarif_edf`.

### 🔄 triggers_update

La carte se met à jour sur changement de l'une des 5 entités fonctionnelles ci-dessus (pas de polling passif — uniquement event-driven).

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:button-card` | HACS | ✅ Essentiel |
| Smart plug NODON (appartement général) | Intégration HA [UI] | ✅ Essentiel — fournit `general_electric_appart_power` |
| `sensor.genelec_appart_totale_kwh` | Riemann integration (sensors/) | ✅ Requis — tampon NODON → UM |
| `sensor.genelec_appart_quotidien_kwh_um` | Utility Meter (utility_meter/) | ✅ Requis — source des stats mini/maxi |
| `sensors/.../Genelec_appart_mini_maxi_avg.yaml` | platform: statistics | ✅ Requis — fournit mini/maxi kWh |
| `03_UM_genelec_appart_HPHC_AMHQ.yaml` | Utility Meter HP/HC | ✅ Requis — base calcul coûts inline |
| `custom_components/tarif_edf` | Custom component | ✅ Requis — fournit `edf_tempo_price_blue_hp/hc` |
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
