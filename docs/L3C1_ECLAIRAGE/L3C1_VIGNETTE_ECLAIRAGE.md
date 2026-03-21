<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashboard-tablette` → Ligne 3, Colonne 1 |
| 🔗 **Tap** | `/dashboard-tablette/lumieres` |
| 🏗️ **Layout** | `custom:button-card` — grid 3 cols (Pièce / État / Compteur) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3 |

---

# 💡 L3C1 — Vignette Commandes Éclairage

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Code](#code--vignette)
3. [Logique des colonnes](#logique-des-colonnes)
4. [Entités utilisées](#entités-utilisées--provenance-complète)

---

## 🎯 VUE D'ENSEMBLE

Vignette affichant l'état de l'éclairage par pièce sur **3 colonnes** : nom de pièce / état textuel coloré (depuis les templates `sensor.lumiere_*_etat`) / compteur de lumières actives (X/N). Navigation vers la page lampes au tap.

**6 lignes affichées :** Appart. · Salon · Cuisine · Bureau · SdB · Chambre

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Grille 3 colonnes avec `custom_fields` JS |

---

## 📍 CODE — VIGNETTE

```yaml
type: custom:button-card
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/lumieres
entities:
  - sensor.lumiere_appartement_etat
  - sensor.lumiere_salon_etat
  - sensor.lumiere_cuisine_etat
  - sensor.bureau_etat
  - sensor.lumiere_salle_de_bain_etat
  - sensor.chambre_etat
  - sensor.lumiere_ecran_etat
  - light.entree
  - light.couloir
  - light.salon
  - light.table
  - light.cuisine
  - light.lampe_salle_de_bain_hue
  - light.chambre
  - light.hue_color_candle_chambre_gege
  - light.hue_color_candle_chambre_eric
  - switch.prise_tete_de_lit_chambre
triggers_update:
  - sensor.lumiere_appartement_etat
  - sensor.lumiere_salon_etat
  - sensor.lumiere_cuisine_etat
  - sensor.bureau_etat
  - sensor.lumiere_salle_de_bain_etat
  - sensor.chambre_etat
  - sensor.lumiere_ecran_etat
  - light.entree
  - light.couloir
  - light.salon
  - light.table
  - light.cuisine
  - light.lampe_salle_de_bain_hue
  - light.chambre
  - light.hue_color_candle_chambre_gege
  - light.hue_color_candle_chambre_eric
  - switch.prise_tete_de_lit_chambre
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
        "piece etat active"
    - grid-template-columns: 1fr 1fr 1fr
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
      - justify-self: end
      - text-align: start
      - margin-right: "-11px"
    active:
      - grid-area: active
      - justify-self: end
      - margin-right: 8px
      - text-align: right
custom_fields:
  titre: |
    [[[ return 'Commande LAMPES' ]]]
  piece: >
    [[[ return
    `<div><div>Appart.</div><div>Salon</div><div>Cuisine</div><div>Bureau</div><div>SdB</div><div>Chambre</div></div>`;
    ]]]
  etat: |
    [[[
      function getColorForStatus(status) {
        if (status === 'N/A' || status === 'erreur') return '#aaaaaa';
        if (status === 'Allumé') return 'lightgreen';
        if (status === 'Éteint') return 'rgb(244,67,54)';
        if (status === 'AlluSync' || status === 'Synchro' || status === 'Éco.') return '#FFA500';
        const greenStates = [
          'Entrée', 'Couloir', 'Salon', 'Table', 'Bureau',
          'Écran', 'Chambre', 'Zone G.', 'Zone É.',
          'Tête Lit', 'Ch.+zG', 'Ch.+zÉ'
        ];
        if (greenStates.includes(status)) return 'lightgreen';
        return 'white';
      }
      function safeState(entityId) {
        const state = states[entityId]?.state;
        return (!state || state === 'unavailable' || state === 'unknown') ? 'N/A' : state;
      }
      var appStat = safeState('sensor.lumiere_appartement_etat');
      var salStat = safeState('sensor.lumiere_salon_etat');
      var cuiStat = safeState('sensor.lumiere_cuisine_etat');
      var burStat = safeState('sensor.bureau_etat');
      var sdbStat = safeState('sensor.lumiere_salle_de_bain_etat');
      var chaStat = safeState('sensor.chambre_etat');
      return `<div>
        <div style="color: ${getColorForStatus(appStat)};">${appStat}</div>
        <div style="color: ${getColorForStatus(salStat)};">${salStat}</div>
        <div style="color: ${getColorForStatus(cuiStat)};">${cuiStat}</div>
        <div style="color: ${getColorForStatus(burStat)};">${burStat}</div>
        <div style="color: ${getColorForStatus(sdbStat)};">${sdbStat}</div>
        <div style="color: ${getColorForStatus(chaStat)};">${chaStat}</div>
      </div>`;
    ]]]
  active: |
    [[[
      function countActiveEntities(entities) {
        return entities.filter(entity => states[entity]?.state === 'on').length;
      }
      function getColorForCount(activeCount, totalCount) {
        if (activeCount === totalCount && totalCount > 0) return 'lightgreen';
        if (activeCount === 0) return 'rgb(244,67,54)';
        return '#FFA500';
      }
      var appartement = { activeCount: countActiveEntities(['light.entree', 'light.couloir']), totalCount: 2 };
      var salon = { activeCount: countActiveEntities(['light.salon', 'light.table']), totalCount: 2 };
      var cuisine = { activeCount: countActiveEntities(['light.cuisine']), totalCount: 1 };

      var statusB = states['sensor.bureau_etat']?.state;
      var ecranS = states['sensor.lumiere_ecran_etat']?.state;
      var bTxt = "0/2";
      var bCol = "rgb(244,67,54)";
      if (statusB === 'AlluSync') { bTxt = "2/2"; bCol = "#FFA500"; }
      else if (statusB === 'Synchro') { bTxt = "1/2"; bCol = "#FFA500"; }
      else if (statusB === 'Allumé') { bTxt = "2/2"; bCol = "lightgreen"; }
      else if (statusB === 'Bureau') {
        if (ecranS === 'Éco.') { bTxt = "1/1"; bCol = "lightgreen"; }
        else { bTxt = "1/2"; bCol = "#FFA500"; }
      }
      else if (statusB === 'Écran') { bTxt = "1/2"; bCol = "#FFA500"; }
      else if (statusB === 'Éco.') { bTxt = "0/1"; bCol = "#FFA500"; }
      else { bTxt = "0/2"; bCol = "rgb(244,67,54)"; }

      var sdbActive = states['light.lampe_salle_de_bain_hue']?.state === 'on' ? 1 : 0;

      var statusCh = states['sensor.chambre_etat']?.state;
      var chEnt = ['light.chambre'];
      if (states['switch.prise_tete_de_lit_chambre']?.state === 'on') {
        chEnt.push('light.hue_color_candle_chambre_gege', 'light.hue_color_candle_chambre_eric');
      }
      var chActive = countActiveEntities(chEnt);
      var chTxt = `${chActive}/${chEnt.length}`;
      var chCol = getColorForCount(chActive, chEnt.length);
      if (statusCh === 'Éco.' && chActive === 0 && chEnt.length === 1) {
        chCol = '#FFA500';
      }
      return `<div>
        <div style="color: ${getColorForCount(appartement.activeCount, 2)};">${appartement.activeCount}/2</div>
        <div style="color: ${getColorForCount(salon.activeCount, 2)};">${salon.activeCount}/2</div>
        <div style="color: ${getColorForCount(cuisine.activeCount, 1)};">${cuisine.activeCount}/1</div>
        <div style="color: ${bCol};">${bTxt}</div>
        <div style="color: ${getColorForCount(sdbActive, 1)};">${sdbActive}/1</div>
        <div style="color: ${chCol};">${chTxt}</div>
      </div>`;
    ]]]
```

---

## 🧠 LOGIQUE DES COLONNES

### Colonne `etat` — État textuel (depuis templates)

Source : `sensor.lumiere_*_etat` → `[TPL] P3_eclairage/ui_dashboard/etats_status.yaml`

| État reçu | Couleur | Signification |
|-----------|---------|---------------|
| `Allumé` | `lightgreen` | Toutes les lumières de la pièce ON |
| `Éteint` | `rgb(244,67,54)` | Toutes éteintes |
| `AlluSync` / `Synchro` / `Éco.` | `#FFA500` | État partiel ou économie |
| `Entrée`, `Couloir`, `Salon`… | `lightgreen` | Seul ce groupe allumé |
| `Ch.+zG` / `Ch.+zÉ` | `lightgreen` | Chambre + zone ambiance |
| `N/A` / `erreur` | `#aaaaaa` | Entité indisponible |

### Colonne `active` — Compteur X/N

| Pièce | Entités comptées | Total | Couleur logique |
|-------|-----------------|-------|-----------------|
| Appart. | `light.entree` + `light.couloir` | 2 | vert=2/2, rouge=0/2, orange=1/2 |
| Salon | `light.salon` + `light.table` | 2 | vert=2/2, rouge=0/2, orange=1/2 |
| Cuisine | `light.cuisine` | 1 | vert=1/1, rouge=0/1 |
| Bureau | Logique complexe *(voir ci-dessous)* | 1 ou 2 | — |
| SdB | `light.lampe_salle_de_bain_hue` | 1 | vert=1/1, rouge=0/1 |
| Chambre | `light.chambre` + bougies si prise ON | 1 ou 3 | — |

#### Bureau — Logique spécifique

Le bureau compte 2 sources : la lumière principale (`light.bureau_*`) et l'écran Hue Sync (`sensor.lumiere_ecran_etat`). Le total affiché varie selon l'état :

| `sensor.bureau_etat` | `sensor.lumiere_ecran_etat` | Affiché | Couleur |
|----------------------|-----------------------------|---------|---------|
| `Allumé` | — | `2/2` | vert |
| `AlluSync` | — | `2/2` | orange |
| `Synchro` | — | `1/2` | orange |
| `Bureau` | `Éco.` | `1/1` | vert |
| `Bureau` | autre | `1/2` | orange |
| `Écran` | — | `1/2` | orange |
| `Éco.` | — | `0/1` | orange |
| *(autre)* | — | `0/2` | rouge |

#### Chambre — Logique dynamique (totalCount variable)

Le total de la chambre dépend de l'état de `switch.prise_tete_de_lit_chambre` :
- **Prise OFF** → 1 entité (`light.chambre`) → total = 1
- **Prise ON** → 3 entités (chambre + `hue_color_candle_chambre_gege` + `hue_color_candle_chambre_eric`) → total = 3

**Cas spécial `Éco.`** : si `chambre_etat === 'Éco.'` et prise OFF et 0 lampes allumées → forcer orange (signale l'état éco de la prise même sans lampe active).

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### Templates d'état (colonne `etat`)

| Entité | Fichier source | Rôle |
|--------|---------------|------|
| `sensor.lumiere_appartement_etat` | [TPL] `P3_eclairage/ui_dashboard/etats_status.yaml` | État global appartement |
| `sensor.lumiere_salon_etat` | [TPL] idem | État salon |
| `sensor.lumiere_cuisine_etat` | [TPL] idem | État cuisine |
| `sensor.bureau_etat` | [TPL] idem | État bureau (principal) |
| `sensor.lumiere_ecran_etat` | [TPL] idem | État écran Hue Sync bureau |
| `sensor.lumiere_salle_de_bain_etat` | [TPL] idem | État SdB |
| `sensor.chambre_etat` | [TPL] idem | État chambre |

### Lumières natives (colonne `active`)

| Entité | Pièce | Intégration |
|--------|-------|-------------|
| `light.entree` | 1. ENTRÉE | Hue Bridge |
| `light.couloir` | 6. COULOIR | Hue Bridge |
| `light.salon` | 4. SALON | Hue Bridge |
| `light.table` | 4. SALON | Hue Bridge |
| `light.cuisine` | 5. CUISINE | Hue Bridge |
| `light.lampe_salle_de_bain_hue` | 8. SDB | Hue Bridge |
| `light.chambre` | 9. CHAMBRE | Hue Bridge |
| `light.hue_color_candle_chambre_gege` | 9. CHAMBRE | Hue Bridge |
| `light.hue_color_candle_chambre_eric` | 9. CHAMBRE | Hue Bridge |
| `switch.prise_tete_de_lit_chambre` | 9. CHAMBRE | Intégration native |

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `sensor.lumiere_*_etat` (×7) | [TPL] `etats_status.yaml` | ✅ Essentiel |
| `light.*` (×9) | Hue Bridge (natif) | ✅ Essentiel |
| `switch.prise_tete_de_lit_chambre` | Intégration native | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

- [`PAGE_ECLAIRAGE.md`](./PAGE_ECLAIRAGE.md) — page détaillée lampes *(à créer)*
- Fichier source templates : `templates/P3_eclairage/ui_dashboard/etats_status.yaml`

---

← Retour : Ligne 3 | → Suite : `L3C2_PRISES/`
