<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashboard-tablette` → vue `lumieres` |
| 🔗 **Accès depuis** | Tap vignette L3C1 → `/dashboard-tablette/lumieres` |
| 🏗️ **Layout** | `type: grid` — sections heading + mushroom-entity-card + popups bubble-card |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3 |

---

# 💡 L3C1 — Page Commandes Lumieres

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Sections](#sections)
4. [Popups](#popups)
5. [Bugs corrigés](#bugs-corrigés)
6. [Entités utilisées](#entités-utilisées--provenance-complète)
7. [Dépendances critiques](#dépendances-critiques)

---

## 🎯 VUE D'ENSEMBLE

Page de commande complète de l'éclairage par pièce. Chaque pièce dispose d'un `mushroom-entity-card` avec animation **flame** CSS (via `card_mod` + `mushroom-shape-icon$`) déclenchée selon l'état de la lumière. Les pièces avec plusieurs circuits (Bureau, Chambre, Têtes de Lit) ont des cartes dédiées conditionnelles et des **popups bubble-card** avec grilles de preset brightness (25/50/75/100%).

### Intégrations requises

- ✅ Philips Hue Bridge (natif HA)
- ✅ Sonoff (via intégration Sonoff ou eWeLink)
- ✅ Hue Play HDMI Sync Box (`switch.ecran_p_c_3_play_hue`)

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:mushroom-entity-card` | Bouton principal par pièce avec flame animation |
| `custom:mushroom-chips-card` | Pastille overlay → ouvre popup brightness |
| `custom:mushroom-light-card` | Contrôle brightness dans les popups |
| `custom:vertical-stack-in-card` | Groupement bouton + pastille sans bordure |
| `custom:bubble-card` | Popups #bureau / #ecranpc / #tete_de_lit |
| `custom:button-card` | Grilles preset 25/50/75/100% dans les popups |
| `custom:layout-card` | Grid 4 colonnes dans les popups |

---

## 🏗️ ARCHITECTURE

```
type: grid
│
├── [HEADING] LUMIERES — nav retour dashboard (tap → /dashboard-tablette/0)
│
├── [HEADING] Entrée
├── [mushroom-entity-card] light.entree (cols 12)
│
├── [HEADING] Salon
├── [mushroom-entity-card] light.salon (cols 6)
├── [mushroom-entity-card] light.table (cols 6)
│
├── [HEADING] Cuisine
├── [mushroom-entity-card] light.cuisine (cols 12)
│
├── [HEADING] Couloir
├── [mushroom-entity-card] light.couloir (cols 12)
│
├── [HEADING] Bureau   [badges: T°, lumiere_bureau_etat, lumiere_ecran_etat, store_bureau]
├── [vertical-stack-in-card] Bouton Bureau (cols 6)
│   ├── mushroom-entity-card sensor.lumiere_bureau_etat  ← toggle light.hue_white_lamp_bureau_1+2
│   └── mushroom-chips-card pastille → popup #bureau     ← visible si Bureau|Allumé
├── [conditional] switch.ecran_p_c_3_play_hue = ON → Bouton Ecran (cols 6)
│   ├── mushroom-entity-card sensor.lumiere_ecran_etat   ← toggle hue_play_1/2/3_pc_bureau
│   └── mushroom-chips-card pastille → popup #ecranpc    ← visible si Écran|Allumé uniquement
│
├── [HEADING] Salle de Bain   [badges: T°, light.lampe_salle_de_bain_hue, switch.relais_lumiere_sdb_sonoff]
├── [mushroom-entity-card] sensor.lumiere_salle_de_bain_etat (cols 12)
│
├── [HEADING] Chambre   [badges: T°, light.chambre]
├── [mushroom-entity-card] sensor.lumiere_chambre_etat (cols 12)
│
├── [HEADING] Têtes de Lit   [badges: light.zone_eric, light.zone_gege]
│   visibility: switch.prise_tete_de_lit_chambre = ON   ← heading masqué si prise coupée
├── [conditional] switch.prise_tete_de_lit_chambre = ON → Bouton Têtes de Lit (cols 12)
│   ├── mushroom-entity-card sensor.lumiere_tete_de_lit_etat  ← toggle hue_color_candle ×2
│   └── mushroom-chips-card pastille → popup #tete_de_lit
│
├── [vertical-stack] Popup #tete_de_lit
│   ├── bubble-card hash="#tete_de_lit"
│   ├── mushroom-light-card light.hue_color_candle_chambre_gege + grille 4 presets
│   └── mushroom-light-card light.hue_color_candle_chambre_eric + grille 4 presets
│
├── [vertical-stack] Popup #bureau
│   ├── bubble-card hash="#bureau"
│   └── mushroom-light-card light.bureau + grille 4 presets
│
├── [vertical-stack] Popup #ecranpc
│   ├── bubble-card hash="#ecranpc"
│   └── mushroom-light-card light.moniteur_pc + grille 4 presets
│
└── [streamline-card] nav_bar
```

---

## 📍 SECTIONS

### Heading Bureau — 4 badges

| Badge | Entité | Couleur logique |
|-------|--------|-----------------|
| T° Bureau | `sensor.th_bureau_temperature` | `color: green` fixe |
| Lumière bureau | `sensor.lumiere_bureau_etat` | Ambre si `Bureau`\|`Allumé`, gris sinon |
| Écran Hue Sync | `sensor.lumiere_ecran_etat` | Vert si `Éco.`, ambre si `Écran`\|`Allumé`\|`Allumé & Sync.`\|`Synchro.`, gris sinon |
| Store bureau | `cover.store_bureau` | `color: state` natif HA |

### Bouton Bureau (vertical-stack-in-card, cols 6)

`mushroom-entity-card` sur `sensor.lumiere_bureau_etat` — affiche l'état textuel du bureau. Flame animation déclenchée si état `in ['Allumé', 'Bureau']`. Bordure et fond ambre si actif, transparent+gris sinon.

**Pastille** (`mushroom-chips-card`) positionnée en overlay (margin-left: 180px, bottom: 47px) → navigate `#bureau`. Visible **uniquement** si `sensor.lumiere_bureau_etat in ['Allumé', 'Bureau']`.

### Bouton Ecran (conditional, cols 6)

Affiché **uniquement** si `switch.ecran_p_c_3_play_hue = "on"`. La Hue Play Sync box pilote les Play bars — quand elle est OFF, la carte entière est masquée.

Flame animation déclenchée par `light.moniteur_pc = "on"`.

**Pastille** → navigate `#ecranpc`. Visible **uniquement** si `sensor.lumiere_ecran_etat in ['Écran', 'Allumé']`. Masquée si `Synchro.`, `Allumé & Sync.`, `Éco.`, `Éteint` (contrôle manuel sans sens en mode sync).

### Heading Têtes de Lit — visibility condition

Le heading entier (et ses badges `zone_eric` / `zone_gege`) est masqué si `switch.prise_tete_de_lit_chambre = "off"`. Comportement **intentionnel** : prise coupée = pas d'alimentation = pas de lampes → inutile d'afficher les badges.

### Grilles presets brightness (dans les popups)

Pattern identique pour toutes les grilles (bureau, écranpc, tête de lit Gégé/Eric) : 4 `custom:button-card` en grid 25%×4. Chaque bouton applique `brightness_pct` via `light.turn_on`. Mise en surbrillance ambre si la brightness courante correspond à la plage ±1 autour de la valeur cible (ex: 25% → 63-65/255).

| % | Plage brightness HA (0–255) | Cible |
|---|-----------------------------|-------|
| 25% | 63–65 | 64 |
| 50% | 127–129 | 128 |
| 75% | 190–192 | 191 |
| 100% | 255 | 255 |

---

## 🪲 BUGS CORRIGÉS

### [B1] Badge `sensor.lumiere_ecran_etat` — `:host` incomplet

**Symptôme** : badge ambre pour `Écran`/`Allumé` mais gris pour `Synchro.` et `Allumé & Sync.` — incohérence entre `:host` et `ha-state-icon`.

**Cause** : la condition `elif` du bloc `:host` ne listait que `['Écran', 'Allumé']`. Le bloc `ha-state-icon` avait déjà le fix (`'Allumé & Sync.','Synchro.'`) mais pas `:host`.

**Fix** :
```yaml
# AVANT
{% elif etat in ['Écran', 'Allumé'] %}

# APRÈS
{% elif etat in ['Écran', 'Allumé', 'Allumé & Sync.', 'Synchro.'] %}
```

### [B2] SDB — `use_number` non défini → UndefinedError Jinja2

**Symptôme** : animation flame absente sur la carte Salle de Bain.

**Cause** : `{% set use_number = false %}` manquant dans le bloc `USER CONFIG` de la SDB — toutes les autres cartes (Bureau, Chambre, Tête de Lit) l'ont. Sans cette ligne, `{% if use_number %}` lève un `UndefinedError` en Jinja2 → CSS `.shape` vide → pas d'animation.

**Fix** : ajouter en tête du bloc `USER CONFIG` de la SDB :
```yaml
{# true = number mode, false = state mode #}
{% set use_number = false %}
```

### [B3] Pastille Ecran — visible en mode sync (design)

**Symptôme** : pastille `#ecranpc` visible même quand les Play bars sont en sync avec le PC — ouvrir le popup brightness n'a pas de sens en mode sync.

**Fix** : `display: none` conditionnel sur le `mushroom-chips-card` :
```yaml
{% if states('sensor.lumiere_ecran_etat') not in ['Écran', 'Allumé'] %}
display: none !important;
{% endif %}
```

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🌐 Intégrations natives HA

| Entité | Intégration | Rôle |
|--------|-------------|------|
| `light.entree` | Philips Hue Bridge | Lumière entrée |
| `light.couloir` | Philips Hue Bridge | Lumière couloir |
| `light.salon` | Philips Hue Bridge | Groupe salon |
| `light.table` | Philips Hue Bridge | Groupe table salon |
| `light.cuisine` | Philips Hue Bridge | Lumière cuisine |
| `light.bureau` | Philips Hue Bridge | Groupe lampes bureau |
| `light.hue_white_lamp_bureau_1` | Philips Hue Bridge | Lampe bureau 1 |
| `light.hue_white_lamp_bureau_2` | Philips Hue Bridge | Lampe bureau 2 |
| `light.hue_play_1_pc_bureau` | Philips Hue Bridge | Play bar 1 (sync PC) |
| `light.hue_play_2_pc_bureau` | Philips Hue Bridge | Play bar 2 (sync PC) |
| `light.hue_play_3_pc_bureau` | Philips Hue Bridge | Play bar 3 (sync PC) |
| `light.moniteur_pc` | Philips Hue Bridge | Moniteur PC (Sync box) |
| `light.lampe_salle_de_bain_hue` | Philips Hue Bridge | Lampe SdB |
| `light.chambre` | Philips Hue Bridge | Groupe chambre |
| `light.hue_color_candle_chambre_gege` | Philips Hue Bridge | Tête de lit Gégé |
| `light.hue_color_candle_chambre_eric` | Philips Hue Bridge | Tête de lit Eric |
| `light.lit` | Philips Hue Bridge | Groupe tête de lit (trigger flame) |
| `light.zone_eric` | Philips Hue Bridge | Zone ambiante Eric |
| `light.zone_gege` | Philips Hue Bridge | Zone ambiante Gégé |
| `switch.relais_lumiere_sdb_sonoff` | Sonoff / eWeLink | Miroir SdB |
| `switch.ecran_p_c_3_play_hue` | Philips Hue Bridge | Hue Play Sync box ON/OFF |
| `switch.prise_tete_de_lit_chambre` | Intégration native | Prise têtes de lit |
| `binary_sensor.moniteur_pc` | Intégration native | Détection moniteur allumé |
| `cover.store_bureau` | Intégration native | Store bureau (badge état) |
| `sensor.th_bureau_temperature` | SONOFF TH | T° bureau (badge heading) |
| `sensor.th_salle_de_bain_temperature` | SONOFF TH | T° SdB (badge heading) |
| `sensor.th_chambre_temperature` | SONOFF TH | T° chambre (badge heading) |

---

### 📁 `templates/P3_eclairage/ui_dashboard/etats_status.yaml`

> Templates d'état synthétique par pièce — alimentation des `mushroom-entity-card` et des badges heading.

| Entité | Rôle |
|--------|------|
| `sensor.lumiere_bureau_etat` | État bureau : `Allumé`/`Bureau`/`AlluSync`/`Synchro`/`Éteint` |
| `sensor.lumiere_ecran_etat` | État écran : `Éco.`/`Écran`/`Allumé`/`Allumé & Sync.`/`Synchro.`/`Éteint` |
| `sensor.lumiere_salle_de_bain_etat` | État SdB : `Allumé`/`Éteint` |
| `sensor.lumiere_chambre_etat` | État chambre |
| `sensor.lumiere_tete_de_lit_etat` | État têtes de lit |

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `sensor.lumiere_*_etat` (×5) | [TPL] `etats_status.yaml` | ✅ Essentiel |
| `light.*` natifs (×19) | Philips Hue Bridge | ✅ Essentiel |
| `switch.ecran_p_c_3_play_hue` | Hue Play Sync Box | ✅ Conditionnel (carte Ecran masquée si absent) |
| `switch.prise_tete_de_lit_chambre` | Intégration native | ✅ Conditionnel (heading Têtes de Lit masqué si OFF) |
| `binary_sensor.moniteur_pc` | Intégration native | ✅ Essentiel (trigger flame Ecran) |
| `custom:mushroom-entity-card` | HACS | ✅ Essentiel |
| `custom:mushroom-chips-card` | HACS | ✅ Essentiel (pastilles) |
| `custom:mushroom-light-card` | HACS | ✅ Essentiel (popups brightness) |
| `custom:bubble-card` | HACS | ✅ Essentiel (popups) |
| `custom:button-card` | HACS | ✅ Essentiel (grilles presets) |
| `custom:layout-card` | HACS | ✅ Essentiel (grilles 4 cols) |
| `custom:vertical-stack-in-card` | HACS | ✅ Essentiel |

---

## ⚡ LOGIQUE ABSENCE — CHAÎNE COMPLÈTE

Certaines cartes de cette page disparaissent automatiquement en mode absence. Ce n'est pas un bug — c'est le résultat d'une **chaîne de dépendances** entre la détection de présence (P4), les automations d'absence et les switches éco qui conditionnent l'affichage.

```
[P4] WiFi / Réseau Mobile
  └── templates/P4_groupe_presence/02_logique_wifi_cellular.yaml
        └── binary_sensor.presence_maison (Présent / Absent)
              └── Automation absence → coupe les prises éco
                    │
                    ├── switch.ecran_p_c_3_play_hue = OFF
                    │     └── PAGE LUMIERES : carte Ecran (cols 6) DISPARAIT
                    │           (conditional: state: "on")
                    │
                    └── switch.prise_tete_de_lit_chambre = OFF
                          └── PAGE LUMIERES : heading Têtes de Lit + carte DISPARAISSENT
                                (visibility + conditional: state: "on")
```

### Comportement attendu par carte

| Carte | Switch pilotant | Groupes requis | Absent → |
|-------|----------------|----------------|----------|
| Bouton Ecran (cols 6) | `switch.ecran_p_c_3_play_hue` | Groupes 2+3+4 OK | ❌ Carte masquée |
| Heading Têtes de Lit + badges | `switch.prise_tete_de_lit_chambre` | Groupes 3+4 OK | ❌ Heading masqué |
| Bouton Têtes de Lit (cols 12) | `switch.prise_tete_de_lit_chambre` | Groupes 3+4 OK | ❌ Carte masquée |
| Bureau (cols 6) | *(pas de switch éco)* | — | ✅ Toujours visible¹ |
| SdB (cols 12) | *(pas de switch éco)* | — | ✅ Toujours visible |
| Chambre (cols 12) | *(pas de switch éco)* | — | ✅ Toujours visible |

> ¹ **Bureau toujours visible** mais quand les groupes 2+3+4 sont OFF (absence) → `switch.ecran_p_c_3_play_hue` est coupé → `sensor.lumiere_ecran_etat` passe à `Éco.` → **badge écran vert** dans le heading Bureau. Comportement attendu et correct.

> **Note séparation des responsabilités :** La logique de coupure (Absent → switch OFF) est gérée dans les automations et `P4_groupe_presence` — pas dans cette page. Cette page se contente de réagir à l'état des switches. Voir `docs/WIFI_PRESENCE (Home Page)/` pour la logique amont.

---

## 🔗 FICHIERS LIÉS

### Documentation
- [`L3C1_VIGNETTE_ECLAIRAGE.md`](./L3C1_VIGNETTE_ECLAIRAGE.md) — vignette d'accès à cette page
- [`L3C2_PRISES/PAGE_PRISES.md`](../L3C2_PRISES/PAGE_PRISES.md) — page prises (même structure)
- [`../WIFI_PRESENCE (Home Page)/PAGE_HOME.md`](../WIFI_PRESENCE%20(Home%20Page)/PAGE_HOME.md) — logique présence amont (P4)

---

← Retour : [`L3C1_VIGNETTE_ECLAIRAGE.md`](./L3C1_VIGNETTE_ECLAIRAGE.md) | → Suite : [`L3C2_PRISES/`](../L3C2_PRISES/)
