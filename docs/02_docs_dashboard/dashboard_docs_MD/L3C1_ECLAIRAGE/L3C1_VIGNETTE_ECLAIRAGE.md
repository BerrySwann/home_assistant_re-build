<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--05--04-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashboard-tablette` → Ligne 3, Colonne 1 |
| 🔗 **Tap** | `/dashboard-tablette/lumieres` |
| 🏗️ **Layout** | `custom:button-card` — grid 3 cols (Pièce / État / Compteur) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-05-04 |
| 🏠 **Version HA** | 2026.5 |

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
  - light.hue_white_lamp_salle_de_bain
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
  - light.hue_white_lamp_salle_de_bain
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

      var sdbActive = states['light.hue_white_lamp_salle_de_bain']?.state === 'on' ? 1 : 0;

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

| État reçu | Couleur | Condition source |
|-----------|---------|-----------------|
| `Allumé` | `lightgreen` | Toutes entités ON (toutes pièces) |
| `Éteint` | `rgb(244,67,54)` | Toutes entités OFF |
| `AlluSync` / `Synchro` / `Éco.` | `#FFA500` | Bureau partiel / écran sync / prise coupée |
| `Entrée` / `Couloir` / `Salon` / `Table` / `Bureau` / `Écran` | `lightgreen` | Ce groupe seul allumé |
| `Chambre` / `Tête Lit` / `Ch.+zG` / `Ch.+zÉ` / `Zone G.` / `Zone É.` | `lightgreen` | État partiel chambre (prise ON ou OFF) |
| `N/A` / `erreur` | `#aaaaaa` | Entité indisponible / unknown |

#### Chambre — Tous les cas (couches 1+2+3)

| État `chambre_etat` | Prise | Actifs | Couleur `etat` | Couleur `active` |
|:--------------------|:-----:|:------:|:--------------:|:----------------:|
| `Allumé` | ON | 3/3 | vert | vert |
| `Ch.+zG` | ON | 2/3 | vert | orange |
| `Ch.+zÉ` | ON | 2/3 | vert | orange |
| `Tête Lit` | ON | 2/3 | vert | orange |
| `Chambre` | ON | 1/3 | vert | orange |
| `Zone G.` | ON | 1/3 | vert | orange |
| `Zone É.` | ON | 1/3 | vert | orange |
| `Éteint` | ON | 0/3 | rouge | rouge |
| `Chambre` | OFF | 1/1 | vert | vert |
| `Éco.` | OFF | 0/1 → override | orange | orange |

### Colonne `active` — Compteur X/N

| Pièce | Entités comptées | Total | Couleur logique |
|-------|-----------------|-------|-----------------|
| Appart. | `light.entree` + `light.couloir` | 2 | vert=2/2, rouge=0/2, orange=1/2 |
| Salon | `light.salon` + `light.table` | 2 | vert=2/2, rouge=0/2, orange=1/2 |
| Cuisine | `light.cuisine` | 1 | vert=1/1, rouge=0/1 |
| Bureau | Logique complexe *(voir ci-dessous)* | 1 ou 2 | — |
| SdB | `light.hue_white_lamp_salle_de_bain` | 1 | vert=1/1, rouge=0/1 |
| Chambre | `light.chambre` + bougies si prise ON | 1 ou 3 | vert=`Allumé` (3/3) ou chambre seule (1/1 prise OFF), orange=partiel (1/3 ou 2/3) ou `Éco.` (override) |

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

## ⚠️ ENTITÉS DISPONIBLES NON ENCORE INTÉGRÉES (etats_status.yaml)

Les sensors suivants existent dans `P3_eclairage/ui_dashboard/etats_status.yaml` mais ne sont pas encore
référencés dans le code de cette vignette. À intégrer lors d'une prochaine révision si la logique le justifie :

| Entité | Remplace / Complète | Note |
|:-------|:--------------------|:-----|
| `sensor.lumiere_bureau_etat` | `sensor.bureau_etat` | Nouveau slug unifié (préfixe `lumiere_`) |
| `sensor.lumiere_chambre_etat` | `sensor.chambre_etat` | Idem — slug harmonisé |
| `sensor.lumiere_tete_de_lit_etat` | *(absent)* | Nouvel état dédié tête de lit chambre |

> **Note :** Les anciens `sensor.bureau_etat` et `sensor.chambre_etat` sont toujours présents dans
> `etats_status.yaml` et fonctionnels — pas de migration urgente.

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
| `light.hue_white_lamp_salle_de_bain` | 8. SDB | Hue Bridge |
| `light.chambre` | 9. CHAMBRE | Hue Bridge |
| `light.hue_color_candle_chambre_gege` | 9. CHAMBRE | Hue Bridge |
| `light.hue_color_candle_chambre_eric` | 9. CHAMBRE | Hue Bridge |
| `switch.prise_tete_de_lit_chambre` | 9. CHAMBRE | Intégration native |

---

## 📁 YAML SOURCE — `etats_status.yaml`

> Fichier : `templates/P3_eclairage/ui_dashboard/etats_status.yaml`
> C'est lui qui génère **tous** les `sensor.lumiere_*_etat` lus par cette vignette.

### 🖥️ Setup Bureau — à lire avant le code

Le bureau a **3 couches** d'éclairage :
1. **Lumières blanches** : `light.hue_white_lamp_bureau_1` + `light.hue_white_lamp_bureau_2` (boules lumineuses)
2. **Play bars** : `light.hue_play_1/2/3_pc_bureau` (rétroéclairage moniteur — Hue Sync)
3. **Switch Sync** : `switch.ecran_p_c_3_play_hue` — coupe la prise Hue Sync Box (économie énergie)

Cela donne **3 sensors** distincts : `lumiere_bureau_etat` (boules lumineuses seuls), `lumiere_ecran_etat` (Play bars + Sync), `bureau_etat` (synthèse des deux).

```yaml
# ┌──────────────────────────────────────┐
# │ 0. APPARTEMENT (GLOBAL)              │
# └──────────────────────────────────────┘
- name: "Lumière Appartement État"
  unique_id: lumiere_appartement_etat
  state: >
    {% if is_state('light.entree', 'on') and is_state('light.couloir', 'on') %}
      Allumé
    {% elif is_state('light.entree', 'off') and is_state('light.couloir', 'off') %}
      Éteint
    {% elif is_state('light.entree', 'on') and is_state('light.couloir', 'off')%}
      Entrée
    {% elif is_state('light.couloir', 'on') and is_state('light.entree', 'off')%}
      Couloir
    {% else %}
      erreur
    {% endif %}

# ┌──────────────────────────────────────┐
# │ 4. SALON                             │
# └──────────────────────────────────────┘
- name: "Lumière Salon État"
  unique_id: lumiere_salon_etat
  state: >
    {% if is_state('light.salon', 'on') and is_state('light.table', 'on') %}
      Allumé
    {% elif is_state('light.salon', 'off') and is_state('light.table', 'off') %}
      Éteint
    {% elif is_state('light.salon', 'on') and is_state('light.table', 'off') %}
      Salon
    {% elif is_state('light.salon', 'off') and is_state('light.table', 'on') %}
      Table
    {% else %}
      erreur
    {% endif %}

# ┌──────────────────────────────────────┐
# │ 7. BUREAU — Plafonniers              │
# └──────────────────────────────────────┘
- name: "Lumière Bureau État"
  unique_id: lumiere_bureau_etat
  state: >
    {% set bureau_on = is_state('light.hue_white_lamp_bureau_1', 'on') or
                       is_state('light.hue_white_lamp_bureau_2', 'on') %}
    {% set ecran3_off = is_state('switch.ecran_p_c_3_play_hue', 'off') %}
    {% set ecrans_pc_on = is_state('light.hue_play_1_pc_bureau', 'on') or
                          is_state('light.hue_play_2_pc_bureau', 'on') or
                          is_state('light.hue_play_3_pc_bureau', 'on') %}
    {% if ecran3_off %}
      {{ 'Bureau' if bureau_on else 'Éteint' }}
    {% else %}
      {{ 'Allumé' if (bureau_on and ecrans_pc_on) else ('Bureau' if bureau_on else 'Éteint') }}
    {% endif %}

# ┌──────────────────────────────────────┐
# │ 7. BUREAU — Écran / Hue Sync         │
# └──────────────────────────────────────┘
# switch.ecran_p_c_3_play_hue = prise Hue Sync Box
# Éco. = prise coupée (économie)
# Synchro. = Play bars ON + PC actif, sans plafonnier
# Allumé & Sync. = plafonnier + Play bars + PC actif
- name: "Lumière Écran État"
  unique_id: lumiere_ecran_etat
  state: >
    {% set switch_on = is_state('switch.ecran_p_c_3_play_hue', 'on') %}
    {% set bureau_on = is_state('light.hue_white_lamp_bureau_1', 'on') or
                       is_state('light.hue_white_lamp_bureau_2', 'on') %}
    {% set play_on = is_state('light.hue_play_1_pc_bureau', 'on') or
                     is_state('light.hue_play_2_pc_bureau', 'on') or
                     is_state('light.hue_play_3_pc_bureau', 'on') %}
    {% set pc_running = is_state('binary_sensor.moniteur_pc', 'on') %}
    {% if not switch_on %}
      Éco.
    {% elif bureau_on and play_on and pc_running %}
      Allumé & Sync.
    {% elif not bureau_on and play_on and pc_running %}
      Synchro.
    {% elif bureau_on and play_on %}
      Allumé
    {% elif not bureau_on and play_on %}
      Écran
    {% else %}
      Éteint
    {% endif %}

# ┌──────────────────────────────────────┐
# │ 7. BUREAU — Synthèse (bureau_etat)   │
# └──────────────────────────────────────┘
# Agrège lumiere_bureau_etat + lumiere_ecran_etat
- name: "Bureau État"
  unique_id: bureau_etat
  state: >
    {% set bureau = states('sensor.lumiere_bureau_etat') %}
    {% set ecran  = states('sensor.lumiere_ecran_etat') %}
    {% if   bureau == 'Allumé' and ecran == 'Allumé' %}          Allumé
    {% elif bureau == 'Allumé' and ecran == 'Allumé & Sync.' %}  AlluSync
    {% elif bureau == 'Éteint' and ecran == 'Synchro.' %}        Synchro
    {% elif bureau == 'Bureau' and ecran == 'Éteint' %}          Bureau
    {% elif bureau == 'Éteint' and ecran == 'Écran' %}           Écran
    {% elif bureau in ['Bureau','Éteint'] and ecran == 'Éco.' %} {{ 'Bureau' if bureau == 'Bureau' else 'Éco.' }}
    {% elif bureau == 'Éteint' and ecran == 'Éteint' %}          Éteint
    {% else %}                                                    erreur
    {% endif %}

# ┌──────────────────────────────────────┐
# │ 9. CHAMBRE                           │
# └──────────────────────────────────────┘
# switch.prise_tete_de_lit_chambre = prise alimentant les bougies Hue Color
# Éco. (prise OFF) = bougies hors tension, seule light.chambre peut être ON
# Ch.+zG / Ch.+zÉ = chambre + zone Géraldine ou zone Éric (bougie individuelle)
- name: "Chambre État"
  unique_id: chambre_etat
  state: >
    {% if is_state('switch.prise_tete_de_lit_chambre', 'off') %}
      {{ 'Chambre' if is_state('light.chambre', 'on') else 'Éco.' }}
    {% else %}
      {% set ch = is_state('light.chambre', 'on') %}
      {% set zg = is_state('light.hue_color_candle_chambre_gege', 'on') %}
      {% set ze = is_state('light.hue_color_candle_chambre_eric', 'on') %}
      {% if ch and zg and ze %}     Allumé
      {% elif ch and zg %}          Ch.+zG
      {% elif ch and ze %}          Ch.+zÉ
      {% elif ch %}                 Chambre
      {% elif zg and ze %}          Tête Lit
      {% elif zg %}                 Zone G.
      {% elif ze %}                 Zone É.
      {% else %}                    Éteint
      {% endif %}
    {% endif %}
```

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


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_ECLAIRAGE]]  [[L2C3_VIGNETTE_ECLAIRAGE]]  [[L3C2_VIGNETTE_PRISES]]  [[L3C3_VIGNETTE_STORES]]*
