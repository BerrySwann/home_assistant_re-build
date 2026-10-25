<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page%20droite-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path dashboard** | `/dashboard-tablette/lumieres` (navigation de la vignette L3C1) |
| 🔗 **Accès depuis** | Vignette L3C1 (tap) |
| 🏗️ **Layout** | `type: grid` - 14 cartes de niveau 1 (titre, Bureau, Écran, Salle de Bain, Chambre, Têtes de Lit, 3 popups bubble-card, barre de navigation) |
| 📄 **Fichier YAML** | `L3C1_ECLAIRAGE/03_page_droite/page_L3C1_eclairage_droite.yaml` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 📅 **Modifié le** | 2026-10-11 (MD réécrit à partir du YAML et de l'ancien MD du 2026-03-21) |

---

# 💡 L3C1 - Page Commandes Lumières - DROITE (Bureau, Écran, Salle de Bain, Chambre, Têtes de Lit)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Sections](#sections)
4. [Bugs documentés](#bugs-documentés)
5. [Entités utilisées](#entités-utilisées)
6. [Dépendances critiques](#dépendances-critiques)
7. [Disparition de cartes](#disparition-de-cartes)
8. [Code YAML](#code-yaml)
9. [Points à vérifier](#points-à-vérifier)

---

## 🎯 VUE D'ENSEMBLE

Colonne de droite de la page `/dashboard-tablette/lumieres` : les pièces à **plusieurs circuits ou à condition d'affichage** (Bureau, Écran, Salle de Bain, Chambre, Têtes de Lit) et les **popups bubble-card** de réglage de luminosité (`#bureau`, `#ecranpc`, `#tete_de_lit`). Chaque pièce a un `mushroom-entity-card` avec animation **flame** CSS (`card_mod` + `mushroom-shape-icon$`) déclenchée selon l'état de la lumière.

Les pièces simples (Entrée, Salon, Cuisine, Couloir) sont dans [`PAGE_ECLAIRAGE_GAUCHE.md`](../02_page_gauche/PAGE_ECLAIRAGE_GAUCHE.md).

### Intégrations requises

- ✅ Philips Hue Bridge (natif HA)
- ✅ Sonoff (relais SdB `switch.relais_lumiere_sdb_sonoff`)
- ✅ Hue Play HDMI Sync Box (`switch.ecran_p_c_3_play_hue`)

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:mushroom-entity-card` | Bouton principal par pièce avec animation flame |
| `custom:mushroom-chips-card` | Pastille en overlay qui ouvre le popup de luminosité |
| `custom:mushroom-light-card` | Réglage de luminosité dans les popups |
| `custom:vertical-stack-in-card` | Groupement bouton + pastille sans bordure |
| `custom:bubble-card` | Popups `#bureau` / `#ecranpc` / `#tete_de_lit` |
| `custom:button-card` | Grilles de presets 25/50/75/100 % dans les popups |
| `custom:layout-card` | Grille de 4 colonnes dans les popups |
| `custom:streamline-card` | Barre de navigation (template `nav_bar`) |

---

## 🏗️ ARCHITECTURE

```
type: grid
│
├── [HEADING] LUMIERES - retour (tap → /dashboard-tablette/0)
│
├── [HEADING] Bureau   badges : sensor.th_bureau_temperature, sensor.lumiere_bureau_etat,
│                               sensor.lumiere_ecran_etat, cover.store_bureau
├── [vertical-stack-in-card] Bouton Bureau
│   ├── mushroom-entity-card sensor.lumiere_bureau_etat  → toggle light.hue_white_lamp_bureau_1 + _2
│   └── mushroom-chips-card  pastille → popup #bureau    (visible si Bureau | Allumé)
├── [conditional] switch.ecran_p_c_3_play_hue = on → Bouton Écran
│   ├── mushroom-entity-card sensor.lumiere_ecran_etat   → toggle light.hue_play_1/2/3_pc_bureau
│   └── mushroom-chips-card  pastille → popup #ecranpc   (visible si Écran | Allumé)
│
├── [HEADING] Salle de Bain  badges : sensor.th_salle_de_bain_temperature,
│                                     light.hue_white_lamp_salle_de_bain, switch.relais_lumiere_sdb_sonoff
├── [mushroom-entity-card] sensor.lumiere_salle_de_bain_etat → toggle lampe SdB + relais miroir (cols 12)
│
├── [HEADING] Chambre  badges : sensor.th_chambre_temperature, light.chambre, sensor.chambre_nb_allumes
├── [mushroom-entity-card] sensor.lumiere_chambre_etat → toggle light.chambre (cols 12)
│
├── [HEADING] Têtes de Lit  badges : light.zone_eric (zE), light.zone_gege (zG)
│   visibility : switch.prise_tete_de_lit_chambre = on   (heading masqué si prise coupée)
├── [conditional] switch.prise_tete_de_lit_chambre = on → Bouton Têtes de Lit
│   ├── mushroom-entity-card sensor.lumiere_tete_de_lit_etat → toggle light.lit (groupe)
│   └── mushroom-chips-card  pastille → popup #tete_de_lit
│
├── [bubble-card] Popup #tete_de_lit : mushroom-light-card candle gégé + candle eric, 4 presets chacune
├── [bubble-card] Popup #bureau      : mushroom-light-card light.bureau, 4 presets
├── [bubble-card] Popup #ecranpc     : mushroom-light-card light.moniteur_pc, 4 presets
│
└── [streamline-card] template nav_bar
```

---

## Sections

### Heading Bureau - 4 badges

| Badge | Entité | Couleur logique |
|-------|--------|-----------------|
| T° Bureau | `sensor.th_bureau_temperature` | `color: green` fixe |
| Lumière bureau | `sensor.lumiere_bureau_etat` | Ambre si `Bureau` ou `Allumé`, gris sinon |
| Écran Hue Sync | `sensor.lumiere_ecran_etat` | Vert si `Éco.` ; ambre pour l'icône si `Écran`, `Allumé`, `Allumé & Sync.`, `Synchro.` ; voir [B1] ci-dessous pour le fond du badge |
| Store bureau | `cover.store_bureau` | `color: state` natif HA |

### Bouton Bureau (vertical-stack-in-card)

`mushroom-entity-card` sur `sensor.lumiere_bureau_etat` : état texte du bureau. Flame animation si l'état est `Allumé` ou `Bureau`. La **pastille** (`mushroom-chips-card`, en overlay) navigue vers `#bureau`.

### Bouton Écran (conditional)

Affiché **uniquement** si `switch.ecran_p_c_3_play_hue = on`. Flame animation déclenchée par `light.moniteur_pc = on`. La pastille gradateur (navigate `#ecranpc`) est masquée par `display: none` sauf si `sensor.lumiere_ecran_etat` vaut `Écran` ou `Allumé`.

**Logique des états** (relue dans le template `P3_etats_status.yaml` le 2026-10-11) :

> `binary_sensor.moniteur_pc = on` = moniteur PC allumé = Hue Sync Box active.

| # | État (`sensor.lumiere_ecran_etat`) | Condition | Carte Écran | Pastille #ecranpc |
|---|-------------------------------------|-----------|-------------|-------------------|
| 1 | `Éco.` | `switch.ecran_p_c_3_play_hue = off` | **masquée** (conditional) | - |
| 2 | `Synchro.` | switch ON + Play bars ON + moniteur ON + lampes bureau OFF | visible | **masquée** |
| 3 | `Allumé & Sync.` | switch ON + Play bars ON + moniteur ON + lampes bureau ON | visible | **masquée** |
| 4 | `Écran` | switch ON + Play bars ON + moniteur OFF + lampes bureau OFF | visible | **visible** |
| 5 | `Allumé` | switch ON + Play bars ON + moniteur OFF + lampes bureau ON | visible | **visible** |
| 6 | `Éteint` | switch ON + Play bars OFF | visible | masquée |

("Play bars ON" = au moins une des `light.hue_play_1/2/3_pc_bureau` ; "lampes bureau ON" = `light.hue_white_lamp_bureau_1` ou `_2`.)

Pourquoi la pastille est masquée en `Synchro.` et `Allumé & Sync.` (explication de l'ancien MD) : la Hue Sync Box synchronise les Play bars en temps réel depuis l'écran, une luminosité envoyée par HA serait écrasée immédiatement.

### Salle de Bain, Chambre

- **Salle de Bain** : un seul bouton pour la lampe Hue et le relais miroir Sonoff (`light.hue_white_lamp_salle_de_bain` + `switch.relais_lumiere_sdb_sonoff`).
- **Chambre** : bouton sur `light.chambre`; le badge `sensor.chambre_nb_allumes` affiche `n/3` quand la prise des têtes de lit est ON, `1/1` ou `0/1` sinon (relu dans le template).

### Heading Têtes de Lit - condition de visibilité

Le heading entier (et ses badges `zone_eric` / `zone_gege`) est masqué si `switch.prise_tete_de_lit_chambre` n'est pas `on`. Comportement voulu : prise coupée = pas d'alimentation des lampes.

### Presets de luminosité (popups)

Même motif pour les 3 popups : 4 `custom:button-card` en grille 4 colonnes, chacun appelle `light.turn_on` avec `brightness_pct` 25, 50, 75, 100. Surbrillance ambre quand la luminosité courante est à ±1 de la cible.

| % | Plage brightness HA (0-255) | Cible |
|---|-----------------------------|-------|
| 25% | 63-65 | 64 |
| 50% | 127-129 | 128 |
| 75% | 190-192 | 191 |
| 100% | 255 | 255 |

---

## Bugs documentés

Etat de chaque bug de l'ancien MD, **comparé au YAML actuel** (relevé le 2026-10-11) :

| Bug | Description | Etat dans le YAML actuel |
|:--|:--|:--|
| [B1] | Badge `sensor.lumiere_ecran_etat` : le bloc `:host` ne listait que `['Écran','Allumé']`, donc badge gris pour `Synchro.` et `Allumé & Sync.` | **Non corrigé** : ligne 54, `{% elif etat in ['Écran', 'Allumé'] %}` ; seul le bloc `ha-state-icon` (ligne 67) contient les 4 états. Le même constat existe dans la sauvegarde `page_L3C1_eclairage_droite.bak_2026_05_13.yaml`. |
| [B2] | `{% set use_number = false %}` manquant dans le bloc USER CONFIG (SdB) | Corrigé : présent dans les 4 cartes qui en ont besoin (Écran, SdB, Chambre, Tête de Lit). La carte Bureau a un bloc flame plus simple, sans `use_number`. |
| [B3] | Pastille `#ecranpc` visible en mode sync | Corrigé : `display: none !important` quand l'état n'est pas `Écran` ou `Allumé` (ligne 427-428). |
| [B4] | Tap Tête de Lit : `light.toggle` sur 2 entités alternait gégé/eric | Corrigé : cible `light.lit` (groupe). |

Fix prévu pour [B1] : remplacer la ligne 54 par `{% elif etat in ['Écran', 'Allumé', 'Allumé & Sync.', 'Synchro.'] %}`. **Non appliqué** (le YAML est inchangé). Au moment du relevé `sensor.lumiere_ecran_etat` valait `Synchro.` : l'écart peut être constaté sur le dashboard (icône ambre, fond du badge gris).

---

## Entités utilisées

Toutes les entités ci-dessous existent dans HA (vérification en direct le 2026-10-11).

### Intégrations natives HA

| Entité | Source | Rôle |
|--------|--------|------|
| `light.bureau` | Philips Hue | Groupe lampes bureau (popup `#bureau`) |
| `light.hue_white_lamp_bureau_1`, `light.hue_white_lamp_bureau_2` | Philips Hue | Lampes bureau (toggle du bouton Bureau) |
| `light.hue_play_1_pc_bureau`, `light.hue_play_2_pc_bureau`, `light.hue_play_3_pc_bureau` | Philips Hue | Play bars (toggle du bouton Écran) |
| `light.moniteur_pc` | Philips Hue | Moniteur PC / Sync box (popup `#ecranpc`, trigger flame Écran) |
| `light.hue_white_lamp_salle_de_bain` | Philips Hue | Lampe SdB |
| `light.chambre` | Philips Hue | Groupe chambre |
| `light.hue_color_candle_chambre_gege`, `light.hue_color_candle_chambre_eric` | Philips Hue | Bougies têtes de lit (popup `#tete_de_lit`) |
| `light.lit` | groupe | Cible du tap Têtes de Lit |
| `light.zone_eric`, `light.zone_gege` | Philips Hue | Badges du heading Têtes de Lit |
| `switch.relais_lumiere_sdb_sonoff` | Sonoff | Relais miroir SdB |
| `switch.ecran_p_c_3_play_hue` | prise pilotant la Hue Play Sync box | condition d'affichage du bouton Écran |
| `switch.prise_tete_de_lit_chambre` | intégration native | condition d'affichage des Têtes de Lit |
| `binary_sensor.moniteur_pc` | intégration native | Détection moniteur allumé (utilisé par le template d'état) |
| `cover.store_bureau` | intégration native | Badge store bureau |
| `sensor.th_bureau_temperature`, `sensor.th_salle_de_bain_temperature`, `sensor.th_chambre_temperature` | capteurs de température | Badges des headings |

### Templates `templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml`

| Entité | Rôle |
|--------|------|
| `sensor.lumiere_bureau_etat` | `Allumé` / `Bureau` / `Éteint` |
| `sensor.lumiere_ecran_etat` | `Éco.` / `Écran` / `Allumé` / `Allumé & Sync.` / `Synchro.` / `Éteint` |
| `sensor.lumiere_salle_de_bain_etat` | état SdB |
| `sensor.lumiere_chambre_etat` | `Allumé` / `Éteint` |
| `sensor.lumiere_tete_de_lit_etat` | `Éco.` si la prise est coupée, sinon état des bougies |
| `sensor.chambre_nb_allumes` | compteur `n/3` ou `n/1` |

`light.toggle` et `light.turn_on` sont des **services** du YAML, pas des entités. `sensor.plug_power` apparaît dans la variable `number_entity` des blocs USER CONFIG (valeur `unknown` le 2026-10-11, non utilisée en mode état).

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `sensor.lumiere_*_etat` (bureau, écran, SdB, chambre, tête de lit) | template `P3_etats_status.yaml` | ✅ Essentiel |
| `light.*` natifs | Philips Hue | ✅ Essentiel |
| `switch.ecran_p_c_3_play_hue` | Hue Play Sync Box | ✅ Conditionnel (carte Écran masquée si OFF) |
| `switch.prise_tete_de_lit_chambre` | Intégration native | ✅ Conditionnel (Têtes de Lit masquées si OFF) |
| `binary_sensor.moniteur_pc` | Intégration native | ✅ Essentiel (état Écran) |
| `custom:mushroom-entity-card`, `mushroom-chips-card`, `mushroom-light-card` | HACS | ✅ Essentiel |
| `custom:bubble-card` | HACS | ✅ Essentiel (popups) |
| `custom:button-card`, `custom:layout-card` | HACS | ✅ Essentiel (presets) |
| `custom:vertical-stack-in-card`, `custom:streamline-card` | HACS | ✅ Essentiel |

---

## Disparition de cartes

Certaines cartes disparaissent selon l'état de deux prises :

| Carte | Switch pilotant | Quand il n'est pas `on` |
|-------|----------------|--------------------------|
| Bouton Écran | `switch.ecran_p_c_3_play_hue` | carte masquée (le badge Écran du heading Bureau reste, état `Éco.`) |
| Heading Têtes de Lit + badges | `switch.prise_tete_de_lit_chambre` | heading masqué |
| Bouton Têtes de Lit | `switch.prise_tete_de_lit_chambre` | carte masquée |
| Bureau, Salle de Bain, Chambre | aucun | toujours visibles |

L'ancien MD décrivait une chaîne d'absence (`templates/P4_groupe_presence/02_logique_wifi_cellular.yaml` → `binary_sensor.presence_maison` → automation de coupure des prises). **Cette description est obsolète** : ce fichier n'existe plus (le dossier contient `P4_groupe_presence.yaml` et `P4_wifi_detection.yaml`), `binary_sensor.presence_maison` n'est défini dans aucun YAML de config et vaut `unknown` dans HA, et la détection WiFi passe par le routeur Beryl (voir `CARD_PRESENCE_HOME.md`). L'automation qui coupe les prises n'a pas été retrouvée ; la seule automation du dossier des automations qui cite l'un de ces deux switches est `p3_bureau_activation_ecran_synchro`.

---

## Code YAML

> Copie du fichier `page_L3C1_eclairage_droite.yaml` (le fichier YAML fait foi).

```yaml
type: grid
cards:
- type: heading
  icon: hue:bulb-group-classic-3-alt
  heading: LUMIERES
  heading_style: title
  badges: []
  tap_action:
    action: navigate
    navigation_path: /dashboard-tablette/0
  layout_options:
    grid_columns: full
    grid_rows: 1
- type: heading
  icon: mdi:desktop-tower-monitor
  heading_style: title
  heading: Bureau
  badges:
  - type: entity
    entity: sensor.th_bureau_temperature
    color: green
    show_state: true
  - type: entity
    entity: sensor.lumiere_bureau_etat
    icon: hue:flourish-alt
    card_mod:
      style: |
        :host {
          {% set etat = states('sensor.lumiere_bureau_etat') %}
          {% if etat in ['Bureau', 'Allumé'] %}
            --label-badge-red: #FFBF00 !important;
            --ha-label-badge-color: #FFBF00 !important;
            color: #FFBF00 !important;
          {% else %}
            --ha-label-badge-color: grey !important;
            color: grey !important;
          {% endif %}
        }
        ha-state-icon {
          color: {% if states('sensor.lumiere_bureau_etat') in ['Bureau', 'Allumé'] %} #FFBF00 {% else %} grey {% endif %} !important;
        }
  - type: entity
    entity: sensor.lumiere_ecran_etat
    icon: mdi:monitor-dashboard
    card_mod:
      style: |
        :host {
          {% set etat = states('sensor.lumiere_ecran_etat') %}
          {% if etat == 'Éco.' %}
            /* Couleur Verte quand Éco. */
            --label-badge-red: var(--green-color) !important;
            --ha-label-badge-color: var(--green-color) !important;
            color: var(--green-color) !important;
          {% elif etat in ['Écran', 'Allumé'] %}
            /* Couleur Ambre pour le reste */
            --label-badge-red: #FFBF00 !important;
            --ha-label-badge-color: #FFBF00 !important;
            color: #FFBF00 !important;
          {% else %}
            /* Gris par défaut */
            --ha-label-badge-color: grey !important;
            color: grey !important;
          {% endif %}
        }
        ha-state-icon {
          {% set etat = states('sensor.lumiere_ecran_etat') %}
          color: {% if etat == 'Éco.' %} var(--green-color) {% elif etat in ['Allumé & Sync.','Synchro.','Écran', 'Allumé'] %} #FFBF00 {% else %} grey {% endif %} !important;
        }
  - type: entity
    entity: cover.store_bureau
    color: state
- type: custom:vertical-stack-in-card
  cards:
  - type: custom:mushroom-entity-card
    entity: sensor.lumiere_bureau_etat
    secondary_info: state
    icon_color: deep-orange
    name: Bureau
    tap_action:
      action: call-service
      service: light.toggle
      target:
        entity_id:
        - light.hue_white_lamp_bureau_1
        - light.hue_white_lamp_bureau_2
    layout: horizontal
    card_mod:
      style:
        mushroom-shape-icon$: |
          .shape {
            {% set trigger_active = states('sensor.lumiere_bureau_etat') in ['Allumé', 'Bureau'] %}
            
            {% if trigger_active %}
              --shape-animation: flame-core 1.4s infinite;
              --flame-layer1: flame-layers 1.8s infinite;
              --flame-layer2: ember-pulse 2.4s infinite;
              opacity: 1;
            {% else %}
              --shape-animation: none;
              --flame-layer1: none;
              --flame-layer2: none;
              opacity: 0.6;
            {% endif %}
            position: relative;
            transform-origin: 50% 75%;
            animation: var(--shape-animation);
          }
          .shape::before, .shape::after {
            content: "";
            position: absolute;
            inset: -8px;
            border-radius: inherit;
            pointer-events: none;
            filter: blur(3px);
          }
          .shape::before { animation: var(--flame-layer1); }
          .shape::after { animation: var(--flame-layer2); }
          /* Core flame motion: chaotic vertical flicker + heat ripple */
            @keyframes flame-core {
              0%   { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
              12%  { transform: translateY(-2px) scale(1.05);  filter: brightness(1.4) hue-rotate(-10deg); }
              25%  { transform: translateY(1px)  scale(0.98);  filter: brightness(0.9) hue-rotate(8deg); }
              40%  { transform: translateY(-3px) scale(1.07);  filter: brightness(1.5) hue-rotate(-18deg); }
              55%  { transform: translateY(0)    scale(1.02);  filter: brightness(1.2) hue-rotate(10deg); }
              70%  { transform: translateY(-1px) scale(1.04);  filter: brightness(1.35) hue-rotate(-6deg); }
              85%  { transform: translateY(2px)  scale(0.97);  filter: brightness(0.95) hue-rotate(6deg); }
              100% { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
            }
            /* Outer flame shape: shifting blurred glow */
            @keyframes flame-layers {
              0% {
                box-shadow:
                  0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                  0 -12px 24px -6px rgba(255, 200, 0, 0.4);
              }
              33% {
                box-shadow:
                  0 0 20px 10px rgba(var(--rgb-{{ config.icon_color }}), 1),
                  0 -16px 30px -8px rgba(255, 160, 0, 0.5);
              }
              66% {
                box-shadow:
                  0 0 18px 9px rgba(var(--rgb-{{ config.icon_color }}), 0.9),
                  0 -8px 20px -6px rgba(255, 220, 0, 0.35);
              }
              100% {
                box-shadow:
                  0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                  0 -12px 24px -6px rgba(255, 200, 0, 0.4);
              }
            }
            /* Ember pulse: slow breathing glow */
            @keyframes ember-pulse {
              0% {
                box-shadow:
                  0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                  0 0 60px 20px rgba(255, 120, 0, 0.15);
              }
              50% {
                box-shadow:
                  0 0 50px 18px rgba(var(--rgb-{{ config.icon_color }}), 0.5),
                  0 0 90px 35px rgba(255, 150, 0, 0.25);
              }
              100% {
                box-shadow:
                  0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                  0 0 60px 20px rgba(255, 120, 0, 0.15);
              }
            }
        .: |
          mushroom-shape-icon {
            {% set active = states('sensor.lumiere_bureau_etat') in ['Allumé', 'Bureau'] %}
            --shape-color: {% if active %} rgba(var(--rgb-deep-orange), 0.2) {% else %} rgba(var(--rgb-disabled), 0.1) {% endif %} !important;
            --icon-color: {% if active %} rgb(var(--rgb-deep-orange)) {% else %} rgb(var(--rgb-disabled)) {% endif %} !important;
            --icon-size: 65px;
            display: flex;
            margin: -18px 30px -20px !important;
            padding-right: 20px;
          }
          mushroom-state-info {
            position: absolute !important;
            top: 27px !important;  
            left: 137px !important; 
            text-align: left !important;
          }
          ha-card {
            border: 1px solid {% if states('sensor.lumiere_bureau_etat') in ['Allumé', 'Bureau'] %} transparent {% else %} grey {% endif %} !important;
            background-color: {% if states('sensor.lumiere_bureau_etat') in ['Allumé', 'Bureau'] %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %} !important;
            height: 120px !important;
          }
  - type: custom:mushroom-chips-card
    chips:
    - type: template
      entity: sensor.lumiere_bureau_etat
      tap_action:
        action: navigate
        navigation_path: "#bureau"
      icon: >
        {{ 'hue:flourish-alt' if states('sensor.lumiere_bureau_etat') in
        ['Allumé', 'Bureau'] else 'hue:flourish' }}
      icon_color: >
        {{ '#FFA000A9' if states('sensor.lumiere_bureau_etat') in
        ['Allumé', 'Bureau'] else 'grey' }}
    card_mod:
      style: |
        ha-card {
          --chip-border-color: {% if states('sensor.lumiere_bureau_etat') in ['Allumé', 'Bureau'] %} rgb(255, 160, 0) {% else %} rgba(var(--rgb-disabled), 0.1) {% endif %};
          background: transparent !important;
          border: none !important;
          box-shadow: none !important;
          margin-left: 180px;
          bottom: 47px;
          height: 0px !important;
        }
  grid_options:
    columns: 6
    rows: 2
  card_mod:
    style: |
      ha-card {
        background: transparent !important;
        border: 1px solid {% if states('sensor.lumiere_bureau_etat') in ['Allumé', 'Bureau'] %} transparent {% else %} grey {% endif %};
        box-shadow: none !important;
      }
- type: conditional
  conditions:
  - entity: switch.ecran_p_c_3_play_hue
    state: "on"
  card:
    type: custom:vertical-stack-in-card
    card_mod:
      style: |
        ha-card {
          background: transparent !important;
          border: 1px solid {% if is_state('light.moniteur_pc', 'on') %} transparent {% else %} grey {% endif %};
          box-shadow: transparent !important;
        }
    cards:
    - type: custom:mushroom-entity-card
      entity: sensor.lumiere_ecran_etat
      secondary_info: state
      icon_color: deep-orange
      name: Ecran
      tap_action:
        action: call-service
        service: light.toggle
        target:
          entity_id:
          - light.hue_play_1_pc_bureau
          - light.hue_play_2_pc_bureau
          - light.hue_play_3_pc_bureau
      layout: horizontal
      card_mod:
        style:
          mushroom-shape-icon$: |
            .shape {
              {# ========== USER CONFIG ========== #}
              {# true = number mode, false = state mode #}
              {% set use_number      = false %}
              {# STATE MODE SETTINGS #}
              {% set state_entity    = 'light.moniteur_pc' %}
              {% set active_value    = 'on' %}
              {# OPTIONAL: NUMBER MODE SETTINGS #}
              {% set number_entity   = 'sensor.plug_power' %}
              
              {# '>' '<' '=' '>=' '<=' #}
              {% set number_operator = '>' %}
              
              {% set threshold       = 0.0 %}
              {# ========== END USER CONFIG ====== #}
              {# ----------- TRIGGER LOGIC ----------- #}
              {% if use_number %}
                {% set num = states(number_entity) | float(0) %}
                {% if number_operator == '>' %}
                  {% set trigger_active = (num > threshold) %}
                {% elif number_operator == '<' %}
                  {% set trigger_active = (num < threshold) %}
                {% elif number_operator == '=' %}
                  {% set trigger_active = (num == threshold) %}
                {% elif number_operator == '>=' %}
                  {% set trigger_active = (num >= threshold) %}
                {% elif number_operator == '<=' %}
                  {% set trigger_active = (num <= threshold) %}
                {% else %}
                  {% set trigger_active = false %}
                {% endif %}
              {% else %}
                {% set trigger_active = (states(state_entity) == active_value) %}
              {% endif %}
              {# --------- END TRIGGER LOGIC --------- #}
              {% if trigger_active %}
                --shape-animation: flame-core 1.4s infinite;
                --flame-layer1: flame-layers 1.8s infinite;
                --flame-layer2: ember-pulse 2.4s infinite;
                opacity: 1;
              {% else %}
                --shape-animation: none;
                --flame-layer1: none;
                --flame-layer2: none;
                opacity: 0.6;
              {% endif %}
              position: relative;
              transform-origin: 50% 75%;
            }
            /* Flame layers */
            .shape::before,
            .shape::after {
              content: "";
              position: absolute;
              inset: -8px;
              border-radius: inherit;
              pointer-events: none;
              filter: blur(3px);
            }
            .shape::before {
              animation: var(--flame-layer1);
            }
            .shape::after {
              animation: var(--flame-layer2);
            }
            /* Core flame motion: chaotic vertical flicker + heat ripple */
            @keyframes flame-core {
              0%   { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
              12%  { transform: translateY(-2px) scale(1.05);  filter: brightness(1.4) hue-rotate(-10deg); }
              25%  { transform: translateY(1px)  scale(0.98);  filter: brightness(0.9) hue-rotate(8deg); }
              40%  { transform: translateY(-3px) scale(1.07);  filter: brightness(1.5) hue-rotate(-18deg); }
              55%  { transform: translateY(0)    scale(1.02);  filter: brightness(1.2) hue-rotate(10deg); }
              70%  { transform: translateY(-1px) scale(1.04);  filter: brightness(1.35) hue-rotate(-6deg); }
              85%  { transform: translateY(2px)  scale(0.97);  filter: brightness(0.95) hue-rotate(6deg); }
              100% { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
            }
            /* Outer flame shape: shifting blurred glow */
            @keyframes flame-layers {
              0% {
                box-shadow:
                  0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                  0 -12px 24px -6px rgba(255, 200, 0, 0.4);
              }
              33% {
                box-shadow:
                  0 0 20px 10px rgba(var(--rgb-{{ config.icon_color }}), 1),
                  0 -16px 30px -8px rgba(255, 160, 0, 0.5);
              }
              66% {
                box-shadow:
                  0 0 18px 9px rgba(var(--rgb-{{ config.icon_color }}), 0.9),
                  0 -8px 20px -6px rgba(255, 220, 0, 0.35);
              }
              100% {
                box-shadow:
                  0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                  0 -12px 24px -6px rgba(255, 200, 0, 0.4);
              }
            }
            /* Ember pulse: slow breathing glow */
            @keyframes ember-pulse {
              0% {
                box-shadow:
                  0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                  0 0 60px 20px rgba(255, 120, 0, 0.15);
              }
              50% {
                box-shadow:
                  0 0 50px 18px rgba(var(--rgb-{{ config.icon_color }}), 0.5),
                  0 0 90px 35px rgba(255, 150, 0, 0.25);
              }
              100% {
                box-shadow:
                  0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                  0 0 60px 20px rgba(255, 120, 0, 0.15);
              }
            }
          .: |
            mushroom-shape-icon {
              /* On définit les variables directment sur le composant */
              {% if is_state('light.moniteur_pc', 'on') %}
                --shape-color: rgba(var(--rgb-deep-orange), 0.2) !important;
                --icon-color: rgb(var(--rgb-deep-orange)) !important;
              {% else %}
                --shape-color: rgba(var(--rgb-disabled), 0.1) !important;
                --icon-color: rgb(var(--rgb-disabled)) !important;
              {% endif %}
              
              --icon-size: 65px;
              display: flex;
              margin: -18px 30px -20px !important;
              padding-right: 20px;
            }
            mushroom-state-info {
              position: absolute !important;
              top: 27px !important;  
              left: 137px !important; 
              text-align: left !important;
            }
            ha-card {
              clip-path: inset(0 0 0 0 round var(--ha-card-border-radius, 12px));
              border: 1px solid {% if is_state('light.moniteur_pc', 'on') %} transparent {% else %} grey {% endif %};
              background-color: {% if is_state('light.moniteur_pc', 'on') %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
              height: 120px !important;
              width: auto !important;
            }
    - type: custom:mushroom-chips-card
      chips:
      - type: template
        entity: sensor.lumiere_ecran_etat
        tap_action:
          action: navigate
          navigation_path: "#ecranpc"
        icon: >
          {% set actif = states('sensor.lumiere_ecran_etat') in ['Écran',
          'Allumé', 'Allumé & Sync.', 'Synchro.'] %} {{
          'mdi:monitor-dashboard' if actif else 'mdi:monitor' }}
        icon_color: >
          {% set actif = states('sensor.lumiere_ecran_etat') in ['Écran',
          'Allumé', 'Allumé & Sync.', 'Synchro.'] %} {{ '#FFA000A9' if
          actif else 'grey' }}
      card_mod:
        style: |
          ha-card {
            --chip-border-color: {{ '#FFA000A9' if is_state('light.moniteur_pc', 'on') else 'grey' }};
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            margin-left: 180px;
            bottom: 47px;
            height: 0px !important;
            {% if states('sensor.lumiere_ecran_etat') not in ['Écran', 'Allumé'] %}
            display: none !important;                                    {# [L1] modif — pastille masquée si état ≠ Écran/Allumé #}
            {% endif %}
          }
  grid_options:
    columns: 6
    rows: 2
- type: heading
  icon: mdi:bathtub
  heading: Salle de Bain
  heading_style: title
  badges:
  - type: entity
    show_state: true
    show_icon: true
    entity: sensor.th_salle_de_bain_temperature
    color: green
  - type: entity
    show_state: true
    show_icon: true
    entity: light.hue_white_lamp_salle_de_bain
    icon: mdi:ceiling-light
    color: state
    state_content: state
  - type: entity
    show_state: true
    show_icon: true
    entity: switch.relais_lumiere_sdb_sonoff
    color: state
    icon: mdi:mirror-rectangle
- type: custom:mushroom-entity-card
  entity: sensor.lumiere_salle_de_bain_etat
  secondary_info: state
  icon_color: deep-orange
  name: Salle de Bain
  tap_action:
    action: call-service
    service: light.toggle
    target:
      entity_id:
      - light.hue_white_lamp_salle_de_bain
      - switch.relais_lumiere_sdb_sonoff
  layout: horizontal
  card_mod:
    style:
      mushroom-shape-icon$: |
        .shape {
          {# ========== USER CONFIG ========== #}
          {# true = number mode, false = state mode #}
          {% set use_number      = false %}
          {# STATE MODE SETTINGS #}
          {% set state_entity    = 'light.hue_white_lamp_salle_de_bain' %}
          {% set active_value    = 'on' %}
          {# OPTIONAL: NUMBER MODE SETTINGS #}
          {% set number_entity   = 'sensor.plug_power' %}
          
          {# '>' '<' '=' '>=' '<=' #}
          {% set number_operator = '>' %}
          
          {% set threshold       = 0.0 %}
          {# ========== END USER CONFIG ====== #}
          {# ----------- TRIGGER LOGIC ----------- #}
          {% if use_number %}
            {% set num = states(number_entity) | float(0) %}
            {% if number_operator == '>' %}
              {% set trigger_active = (num > threshold) %}
            {% elif number_operator == '<' %}
              {% set trigger_active = (num < threshold) %}
            {% elif number_operator == '=' %}
              {% set trigger_active = (num == threshold) %}
            {% elif number_operator == '>=' %}
              {% set trigger_active = (num >= threshold) %}
            {% elif number_operator == '<=' %}
              {% set trigger_active = (num <= threshold) %}
            {% else %}
              {% set trigger_active = false %}
            {% endif %}
          {% else %}
            {% set trigger_active = (states(state_entity) == active_value) %}
          {% endif %}
          {# --------- END TRIGGER LOGIC --------- #}
          {% if trigger_active %}
            --shape-animation: flame-core 1.4s infinite;
            --flame-layer1: flame-layers 1.8s infinite;
            --flame-layer2: ember-pulse 2.4s infinite;
            opacity: 1;
          {% else %}
            --shape-animation: none;
            --flame-layer1: none;
            --flame-layer2: none;
            opacity: 0.6;
          {% endif %}
          position: relative;
          transform-origin: 50% 75%;
        }
        /* Flame layers */
        .shape::before,
        .shape::after {
          content: "";
          position: absolute;
          inset: -8px;
          border-radius: inherit;
          pointer-events: none;
          filter: blur(3px);
        }
        .shape::before {
          animation: var(--flame-layer1);
        }
        .shape::after {
          animation: var(--flame-layer2);
        }
        /* Core flame motion: chaotic vertical flicker + heat ripple */
        @keyframes flame-core {
          0%   { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
          12%  { transform: translateY(-2px) scale(1.05);  filter: brightness(1.4) hue-rotate(-10deg); }
          25%  { transform: translateY(1px)  scale(0.98);  filter: brightness(0.9) hue-rotate(8deg); }
          40%  { transform: translateY(-3px) scale(1.07);  filter: brightness(1.5) hue-rotate(-18deg); }
          55%  { transform: translateY(0)    scale(1.02);  filter: brightness(1.2) hue-rotate(10deg); }
          70%  { transform: translateY(-1px) scale(1.04);  filter: brightness(1.35) hue-rotate(-6deg); }
          85%  { transform: translateY(2px)  scale(0.97);  filter: brightness(0.95) hue-rotate(6deg); }
          100% { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
        }
        /* Outer flame shape: shifting blurred glow */
        @keyframes flame-layers {
          0% {
            box-shadow:
              0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
              0 -12px 24px -6px rgba(255, 200, 0, 0.4);
          }
          33% {
            box-shadow:
              0 0 20px 10px rgba(var(--rgb-{{ config.icon_color }}), 1),
              0 -16px 30px -8px rgba(255, 160, 0, 0.5);
          }
          66% {
            box-shadow:
              0 0 18px 9px rgba(var(--rgb-{{ config.icon_color }}), 0.9),
              0 -8px 20px -6px rgba(255, 220, 0, 0.35);
          }
          100% {
            box-shadow:
              0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
              0 -12px 24px -6px rgba(255, 200, 0, 0.4);
          }
        }
        /* Ember pulse: slow breathing glow */
        @keyframes ember-pulse {
          0% {
            box-shadow:
              0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
              0 0 60px 20px rgba(255, 120, 0, 0.15);
          }
          50% {
            box-shadow:
              0 0 50px 18px rgba(var(--rgb-{{ config.icon_color }}), 0.5),
              0 0 90px 35px rgba(255, 150, 0, 0.25);
          }
          100% {
            box-shadow:
              0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
              0 0 60px 20px rgba(255, 120, 0, 0.15);
          }
        }
      .: |
        mushroom-shape-icon {
          /* On définit les variables directment sur le composant */
          {% if is_state('light.hue_white_lamp_salle_de_bain', 'on') %}
            --shape-color: rgba(var(--rgb-deep-orange), 0.2) !important;
            --icon-color: rgb(var(--rgb-deep-orange)) !important;
          {% else %}
            --shape-color: rgba(var(--rgb-disabled), 0.1) !important;
            --icon-color: rgb(var(--rgb-disabled)) !important;
          {% endif %}
          
          --icon-size: 65px;
          display: flex;
          margin: -18px 30px -20px !important;
          padding-right: 20px;
        }
        ha-card {
          clip-path: inset(0 0 0 0 round var(--ha-card-border-radius, 12px));
          border: 1px solid {% if is_state('light.hue_white_lamp_salle_de_bain', 'on') %} transparent {% else %} grey {% endif %};
          background-color: {% if is_state('light.hue_white_lamp_salle_de_bain', 'on') %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
          height: 120px !important;
          width: auto !important;
        }
  grid_options:
    columns: 12
    rows: 2
- type: heading
  icon: mdi:bed
  heading: Chambre
  heading_style: title
  badges:
  - type: entity
    show_state: true
    show_icon: true
    entity: sensor.th_chambre_temperature
    color: green
  - type: entity
    show_state: true
    show_icon: true
    entity: light.chambre
    icon: hue:flourish-alt
    color: state
    state_content: state
  - type: entity                    # [L3C1 modif] badge x/x lumières chambre coloré
    show_state: true
    show_icon: false
    entity: sensor.chambre_nb_allumes
    card_mod:
      style: |
        :host {
          {% set s = states('sensor.chambre_nb_allumes') %}
          --badge-color:
            {% if s in ['3/3', '1/1'] %}lightgreen
            {% elif s == '0/3' %}rgb(244,67,54)
            {% else %}#FFA500
            {% endif %};
        }
- type: custom:mushroom-entity-card
  entity: sensor.lumiere_chambre_etat
  secondary_info: state
  icon_color: deep-orange
  name: Chambre
  tap_action:
    action: call-service
    service: light.toggle
    target:
      entity_id:
      - light.chambre
  layout: horizontal
  grid_options:
    columns: 12
    rows: 2
  card_mod:
    style:
      mushroom-shape-icon$: |
        .shape {
          {# ========== USER CONFIG ========== #}
          {# true = number mode, false = state mode #}
          {% set use_number      = false %}
          {# STATE MODE SETTINGS #}
          {% set state_entity    = 'light.chambre' %}
          {% set active_value    = 'on' %}
          {# OPTIONAL: NUMBER MODE SETTINGS #}
          {% set number_entity   = 'sensor.plug_power' %}
          
          {# '>' '<' '=' '>=' '<=' #}
          {% set number_operator = '>' %}
          
          {% set threshold       = 0.0 %}
          {# ========== END USER CONFIG ====== #}
          {# ----------- TRIGGER LOGIC ----------- #}
          {% if use_number %}
            {% set num = states(number_entity) | float(0) %}
            {% if number_operator == '>' %}
              {% set trigger_active = (num > threshold) %}
            {% elif number_operator == '<' %}
              {% set trigger_active = (num < threshold) %}
            {% elif number_operator == '=' %}
              {% set trigger_active = (num == threshold) %}
            {% elif number_operator == '>=' %}
              {% set trigger_active = (num >= threshold) %}
            {% elif number_operator == '<=' %}
              {% set trigger_active = (num <= threshold) %}
            {% else %}
              {% set trigger_active = false %}
            {% endif %}
          {% else %}
            {% set trigger_active = (states(state_entity) == active_value) %}
          {% endif %}
          {# --------- END TRIGGER LOGIC --------- #}
          {% if trigger_active %}
            --shape-animation: flame-core 1.4s infinite;
            --flame-layer1: flame-layers 1.8s infinite;
            --flame-layer2: ember-pulse 2.4s infinite;
            opacity: 1;
          {% else %}
            --shape-animation: none;
            --flame-layer1: none;
            --flame-layer2: none;
            opacity: 0.6;
          {% endif %}
          position: relative;
          transform-origin: 50% 75%;
        }
        /* Flame layers */
        .shape::before,
        .shape::after {
          content: "";
          position: absolute;
          inset: -8px;
          border-radius: inherit;
          pointer-events: none;
          filter: blur(3px);
        }
        .shape::before {
          animation: var(--flame-layer1);
        }
        .shape::after {
          animation: var(--flame-layer2);
        }
        /* Core flame motion: chaotic vertical flicker + heat ripple */
        @keyframes flame-core {
          0%   { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
          12%  { transform: translateY(-2px) scale(1.05);  filter: brightness(1.4) hue-rotate(-10deg); }
          25%  { transform: translateY(1px)  scale(0.98);  filter: brightness(0.9) hue-rotate(8deg); }
          40%  { transform: translateY(-3px) scale(1.07);  filter: brightness(1.5) hue-rotate(-18deg); }
          55%  { transform: translateY(0)    scale(1.02);  filter: brightness(1.2) hue-rotate(10deg); }
          70%  { transform: translateY(-1px) scale(1.04);  filter: brightness(1.35) hue-rotate(-6deg); }
          85%  { transform: translateY(2px)  scale(0.97);  filter: brightness(0.95) hue-rotate(6deg); }
          100% { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
        }
        /* Outer flame shape: shifting blurred glow */
        @keyframes flame-layers {
          0% {
            box-shadow:
              0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
              0 -12px 24px -6px rgba(255, 200, 0, 0.4);
          }
          33% {
            box-shadow:
              0 0 20px 10px rgba(var(--rgb-{{ config.icon_color }}), 1),
              0 -16px 30px -8px rgba(255, 160, 0, 0.5);
          }
          66% {
            box-shadow:
              0 0 18px 9px rgba(var(--rgb-{{ config.icon_color }}), 0.9),
              0 -8px 20px -6px rgba(255, 220, 0, 0.35);
          }
          100% {
            box-shadow:
              0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
              0 -12px 24px -6px rgba(255, 200, 0, 0.4);
          }
        }
        /* Ember pulse: slow breathing glow */
        @keyframes ember-pulse {
          0% {
            box-shadow:
              0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
              0 0 60px 20px rgba(255, 120, 0, 0.15);
          }
          50% {
            box-shadow:
              0 0 50px 18px rgba(var(--rgb-{{ config.icon_color }}), 0.5),
              0 0 90px 35px rgba(255, 150, 0, 0.25);
          }
          100% {
            box-shadow:
              0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
              0 0 60px 20px rgba(255, 120, 0, 0.15);
          }
        }
      .: |
        mushroom-shape-icon {
          /* On définit les variables directment sur le composant */
          {% if is_state('light.chambre', 'on') %}
            --shape-color: rgba(var(--rgb-deep-orange), 0.2) !important;
            --icon-color: rgb(var(--rgb-deep-orange)) !important;
          {% else %}
            --shape-color: rgba(var(--rgb-disabled), 0.1) !important;
            --icon-color: rgb(var(--rgb-disabled)) !important;
          {% endif %}
          
          --icon-size: 65px;
          display: flex;
          margin: -18px 30px -20px !important;
          padding-right: 20px;
        }
        ha-card {
          clip-path: inset(0 0 0 0 round var(--ha-card-border-radius, 12px));
          border: 1px solid {% if is_state('light.chambre', 'on') %} transparent {% else %} grey {% endif %};
          background-color: {% if is_state('light.chambre', 'on') %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
          height: 120px !important;
          width: auto !important;
        }
- type: heading
  icon: mdi:bed
  heading: Têtes de Lit
  heading_style: title
  badges:
  - type: entity
    show_state: true
    show_icon: true
    entity: light.zone_eric
    color: state
    icon: hue:wall-impress-narrow
    name: zE
    state_content:
    - name
    - state
    - brightness
  - type: entity
    show_state: true
    show_icon: true
    entity: light.zone_gege
    name: zG
    icon: hue:wall-impress-narrow
    state_content:
    - name
    - state
    - brightness
    color: state
  visibility:
  - condition: state
    entity: switch.prise_tete_de_lit_chambre
    state: "on"
- type: conditional
  conditions:
  - entity: switch.prise_tete_de_lit_chambre
    state: "on"
  card:
    type: custom:vertical-stack-in-card
    card_mod:
      style: |
        ha-card {
          background: transparent !important;
          border: 1px solid {% if is_state('light.lit', 'on') %} transparent {% else %} grey {% endif %};
          box-shadow: transparent !important;
        }
    cards:
    - type: custom:mushroom-entity-card
      entity: sensor.lumiere_tete_de_lit_etat
      secondary_info: state
      icon_color: deep-orange
      name: Tête de Lit
      tap_action:
        action: call-service
        service: light.toggle
        target:
          entity_id: light.lit     # [L841 modif] cible le groupe — évite l'alternance gege/eric
      layout: horizontal
      card_mod:
        style:
          mushroom-shape-icon$: |
            .shape {
              {# ========== USER CONFIG ========== #}
              {# true = number mode, false = state mode #}
              {% set use_number      = false %}
              {# STATE MODE SETTINGS #}
              {% set state_entity    = 'light.lit' %}
              {% set active_value    = 'on' %}
              {# OPTIONAL: NUMBER MODE SETTINGS #}
              {% set number_entity   = 'sensor.plug_power' %}
              
              {# '>' '<' '=' '>=' '<=' #}
              {% set number_operator = '>' %}
              
              {% set threshold       = 0.0 %}
              {# ========== END USER CONFIG ====== #}
              {# ----------- TRIGGER LOGIC ----------- #}
              {% if use_number %}
                {% set num = states(number_entity) | float(0) %}
                {% if number_operator == '>' %}
                  {% set trigger_active = (num > threshold) %}
                {% elif number_operator == '<' %}
                  {% set trigger_active = (num < threshold) %}
                {% elif number_operator == '=' %}
                  {% set trigger_active = (num == threshold) %}
                {% elif number_operator == '>=' %}
                  {% set trigger_active = (num >= threshold) %}
                {% elif number_operator == '<=' %}
                  {% set trigger_active = (num <= threshold) %}
                {% else %}
                  {% set trigger_active = false %}
                {% endif %}
              {% else %}
                {% set trigger_active = (states(state_entity) == active_value) %}
              {% endif %}
              {# --------- END TRIGGER LOGIC --------- #}
              {% if trigger_active %}
                --shape-animation: flame-core 1.4s infinite;
                --flame-layer1: flame-layers 1.8s infinite;
                --flame-layer2: ember-pulse 2.4s infinite;
                opacity: 1;
              {% else %}
                --shape-animation: none;
                --flame-layer1: none;
                --flame-layer2: none;
                opacity: 0.6;
              {% endif %}
              position: relative;
              transform-origin: 50% 75%;
            }
            /* Flame layers */
            .shape::before,
            .shape::after {
              content: "";
              position: absolute;
              inset: -8px;
              border-radius: inherit;
              pointer-events: none;
              filter: blur(3px);
            }
            .shape::before {
              animation: var(--flame-layer1);
            }
            .shape::after {
              animation: var(--flame-layer2);
            }
            /* Core flame motion: chaotic vertical flicker + heat ripple */
            @keyframes flame-core {
              0%   { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
              12%  { transform: translateY(-2px) scale(1.05);  filter: brightness(1.4) hue-rotate(-10deg); }
              25%  { transform: translateY(1px)  scale(0.98);  filter: brightness(0.9) hue-rotate(8deg); }
              40%  { transform: translateY(-3px) scale(1.07);  filter: brightness(1.5) hue-rotate(-18deg); }
              55%  { transform: translateY(0)    scale(1.02);  filter: brightness(1.2) hue-rotate(10deg); }
              70%  { transform: translateY(-1px) scale(1.04);  filter: brightness(1.35) hue-rotate(-6deg); }
              85%  { transform: translateY(2px)  scale(0.97);  filter: brightness(0.95) hue-rotate(6deg); }
              100% { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
            }
            /* Outer flame shape: shifting blurred glow */
            @keyframes flame-layers {
              0% {
                box-shadow:
                  0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                  0 -12px 24px -6px rgba(255, 200, 0, 0.4);
              }
              33% {
                box-shadow:
                  0 0 20px 10px rgba(var(--rgb-{{ config.icon_color }}), 1),
                  0 -16px 30px -8px rgba(255, 160, 0, 0.5);
              }
              66% {
                box-shadow:
                  0 0 18px 9px rgba(var(--rgb-{{ config.icon_color }}), 0.9),
                  0 -8px 20px -6px rgba(255, 220, 0, 0.35);
              }
              100% {
                box-shadow:
                  0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                  0 -12px 24px -6px rgba(255, 200, 0, 0.4);
              }
            }
            /* Ember pulse: slow breathing glow */
            @keyframes ember-pulse {
              0% {
                box-shadow:
                  0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                  0 0 60px 20px rgba(255, 120, 0, 0.15);
              }
              50% {
                box-shadow:
                  0 0 50px 18px rgba(var(--rgb-{{ config.icon_color }}), 0.5),
                  0 0 90px 35px rgba(255, 150, 0, 0.25);
              }
              100% {
                box-shadow:
                  0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                  0 0 60px 20px rgba(255, 120, 0, 0.15);
              }
            }
          .: |
            mushroom-shape-icon {
              /* On définit les variables directment sur le composant */
              {% if is_state('light.lit', 'on') %}
                --shape-color: rgba(var(--rgb-deep-orange), 0.2) !important;
                --icon-color: rgb(var(--rgb-deep-orange)) !important;
              {% else %}
                --shape-color: rgba(var(--rgb-disabled), 0.1) !important;
                --icon-color: rgb(var(--rgb-disabled)) !important;
              {% endif %}
              
              --icon-size: 65px;
              display: flex;
              margin: -18px 30px -20px !important;
              padding-right: 20px;
            }
            ha-card {
              clip-path: inset(0 0 0 0 round var(--ha-card-border-radius, 12px));
              border: 1px solid {% if is_state('light.lit', 'on') %} transparent {% else %} grey {% endif %};
              background-color: {% if is_state('light.lit', 'on') %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
              height: 120px !important;
              width: auto !important;
            }
    - type: custom:mushroom-chips-card
      chips:
      - type: template
        entity: light.lit
        tap_action:
          action: navigate
          navigation_path: "#tete_de_lit"
        icon: >-
          {{ 'mdi:floor-lamp' if is_state('light.lit', 'on') else
          'mdi:floor-lamp-outline' }}
        icon_color: "{{ '#FFA000A9' if is_state('light.lit', 'on') else 'grey' }}"
      card_mod:
        style: |
          ha-card {
            --chip-border-color: {{ '#FFA000A9' if is_state('light.lit', 'on') else 'grey' }};
            background: transparent !important;
            border: transparent !important;
            box-shadow: transparent !important;
            margin-left: 400px;
            bottom: 80px;
            height: 0px !important;
          }
  grid_options:
    columns: 12
    rows: 2
- type: custom:bubble-card
  card_type: pop-up
  hash: "#tete_de_lit"
  show_header: true
  force_icon: false
  show_state: false
  show_last_changed: false
  show_attribute: false
  button_type: name
  name: Têtes de Lit
  icon: mdi:floor-lamp
  show_icon: true
  show_name: true
  card_layout: normal
  hide_backdrop: false
  close_on_click: false
  bg_opacity: "0"
  sub_button:
    main: []
    bottom: []
  cards:
  - type: vertical-stack
    cards:
    - type: custom:mushroom-light-card
      entity: light.hue_color_candle_chambre_gege
      name: Tête de Lit Gégé
      icon: mdi:floor-lamp
      icon_color:
      layout: normal
      use_light_color: false
      show_brightness_control: true
      show_color_temp_control: false
      show_color_control: false
      collapsible_controls: false
      card_mod:
        style: |
          ha-card {
            border: 2px solid {% if is_state('light.hue_color_candle_chambre_gege', 'on') %} #FFA000A9 {% else %} grey {% endif %};
            background-color: {% if is_state('light.hue_color_candle_chambre_gege', 'on') %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
          }
    - type: custom:layout-card
      layout_type: custom:grid-layout
      layout:
        grid-template-columns: 25% 25% 25% 25%
        grid-template-rows: 100%
        grid-template-areas: |
          "zone1 zone2 zone3 zone4"
      cards:
      - type: custom:button-card
        view_layout:
          grid-area: zone1
        label: 25%
        show_label: true
        tap_action:
          action: call-service
          service: light.turn_on
          service_data:
            entity_id: light.hue_color_candle_chambre_gege
            brightness_pct: 25
        styles:
          grid:
          - grid-template-areas: "\"i\" \"n\" \"l\""
          - grid-template-rows: min-content min-content 1fr
          card:
          - aspect-ratio: 1/1
          - background-color: |
              [[[
                var brightness = states['light.hue_color_candle_chambre_gege'].attributes.brightness;
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && brightness >= 63 && brightness <= 65)
                  return "rgba(255, 160, 0, 0.1)";
                else
                  return "transparent";
              ]]]
          - border-width: 1px
          - border-color: |
              [[[
                var brightness = states['light.hue_color_candle_chambre_gege'].attributes.brightness;
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && brightness >= 63 && brightness <= 65)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          icon:
          - color: |
              [[[
                var brightness = states['light.hue_color_candle_chambre_gege'].attributes.brightness;
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && brightness >= 63 && brightness <= 65)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          label:
          - font-weight: bold
          - color: |
              [[[
                var brightness = states['light.hue_color_candle_chambre_gege'].attributes.brightness;
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && brightness >= 63 && brightness <= 65)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
      - type: custom:button-card
        view_layout:
          grid-area: zone2
        label: 50%
        show_label: true
        tap_action:
          action: call-service
          service: light.turn_on
          service_data:
            entity_id: light.hue_color_candle_chambre_gege
            brightness_pct: 50
        styles:
          grid:
          - grid-template-areas: "\"i\" \"n\" \"l\""
          - grid-template-rows: min-content min-content 1fr
          card:
          - aspect-ratio: 1/1
          - background-color: |
              [[[
                var brightness = states['light.hue_color_candle_chambre_gege'].attributes.brightness;
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && brightness >= 127 && brightness <= 129)
                  return "rgba(255, 160, 0, 0.1)";
                else
                  return "transparent";
              ]]]
          - border-width: 1px
          - border-color: |
              [[[
                var brightness = states['light.hue_color_candle_chambre_gege'].attributes.brightness;
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && brightness >= 127 && brightness <= 129)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          icon:
          - color: |
              [[[
                var brightness = states['light.hue_color_candle_chambre_gege'].attributes.brightness;
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && brightness >= 127 && brightness <= 129)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          label:
          - font-weight: bold
          - color: |
              [[[
                var brightness = states['light.hue_color_candle_chambre_gege'].attributes.brightness;
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && brightness >= 127 && brightness <= 129)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
      - type: custom:button-card
        view_layout:
          grid-area: zone3
        label: 75%
        show_label: true
        tap_action:
          action: call-service
          service: light.turn_on
          service_data:
            entity_id: light.hue_color_candle_chambre_gege
            brightness_pct: 75
        styles:
          grid:
          - grid-template-areas: "\"i\" \"n\" \"l\""
          - grid-template-rows: min-content min-content 1fr
          card:
          - aspect-ratio: 1/1
          - background-color: |
              [[[
                var brightness = states['light.hue_color_candle_chambre_gege'].attributes.brightness;
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && brightness >= 190 && brightness <= 192)
                  return "rgba(255, 160, 0, 0.1)";
                else
                  return "transparent";
              ]]]
          - border-width: 1px
          - border-color: |
              [[[
                var brightness = states['light.hue_color_candle_chambre_gege'].attributes.brightness;
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && brightness >= 190 && brightness <= 192)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          icon:
          - color: |
              [[[
                var brightness = states['light.hue_color_candle_chambre_gege'].attributes.brightness;
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && brightness >= 190 && brightness <= 192)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          label:
          - font-weight: bold
          - color: |
              [[[
                var brightness = states['light.hue_color_candle_chambre_gege'].attributes.brightness;
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && brightness >= 190 && brightness <= 192)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
      - type: custom:button-card
        view_layout:
          grid-area: zone4
        label: 100%
        show_label: true
        tap_action:
          action: call-service
          service: light.turn_on
          service_data:
            entity_id: light.hue_color_candle_chambre_gege
            brightness_pct: 100
        styles:
          grid:
          - grid-template-areas: "\"i\" \"n\" \"l\""
          - grid-template-rows: min-content min-content 1fr
          card:
          - aspect-ratio: 1/1
          - background-color: |
              [[[
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && states['light.hue_color_candle_chambre_gege'].attributes.brightness == 255)
                  return "rgba(255, 160, 0, 0.1)";
                else
                  return "transparent";
              ]]]
          - border-width: 1px
          - border-color: |
              [[[
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && states['light.hue_color_candle_chambre_gege'].attributes.brightness == 255)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          icon:
          - color: |
              [[[
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && states['light.hue_color_candle_chambre_gege'].attributes.brightness == 255)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          label:
          - font-weight: bold
          - color: |
              [[[
                if (states['light.hue_color_candle_chambre_gege'].state == "on" && states['light.hue_color_candle_chambre_gege'].attributes.brightness == 255)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
  - type: custom:mushroom-light-card
    entity: light.hue_color_candle_chambre_eric
    name: Tête de Lit Eric
    icon: mdi:floor-lamp
    icon_color:
    layout: normal
    use_light_color: false
    show_brightness_control: true
    show_color_temp_control: false
    show_color_control: false
    collapsible_controls: false
    card_mod:
      style: |
        ha-card {
          border: 2px solid {% if is_state('light.hue_color_candle_chambre_eric', 'on') %} #FFA000A9 {% else %} grey {% endif %};
          background-color: {% if is_state('light.hue_color_candle_chambre_eric', 'on') %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
        }
  - type: custom:layout-card
    layout_type: custom:grid-layout
    layout:
      grid-template-columns: 25% 25% 25% 25%
      grid-template-rows: 100%
      grid-template-areas: |
        "zone1 zone2 zone3 zone4"
    cards:
    - type: custom:button-card
      view_layout:
        grid-area: zone1
      label: 25%
      show_label: true
      tap_action:
        action: call-service
        service: light.turn_on
        service_data:
          entity_id: light.hue_color_candle_chambre_eric
          brightness_pct: 25
      styles:
        grid:
        - grid-template-areas: "\"i\" \"n\" \"l\""
        - grid-template-rows: min-content min-content 1fr
        card:
        - aspect-ratio: 1/1
        - background-color: |
            [[[
              var brightness = states['light.hue_color_candle_chambre_eric'].attributes.brightness;
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && brightness >= 63 && brightness <= 65)
                return "rgba(255, 160, 0, 0.1)";
              else
                return "transparent";
            ]]]
        - border-width: 1px
        - border-color: |
            [[[
              var brightness = states['light.hue_color_candle_chambre_eric'].attributes.brightness;
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && brightness >= 63 && brightness <= 65)
                return "#FFA000A9";
              else
                return "grey";
            ]]]
        icon:
        - color: |
            [[[
              var brightness = states['light.hue_color_candle_chambre_eric'].attributes.brightness;
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && brightness >= 63 && brightness <= 65)
                return "#FFA000A9";
              else
                return "grey";
            ]]]
        label:
        - font-weight: bold
        - color: |
            [[[
              var brightness = states['light.hue_color_candle_chambre_eric'].attributes.brightness;
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && brightness >= 63 && brightness <= 65)
                return "#FFA000A9";
              else
                return "grey";
            ]]]
    - type: custom:button-card
      view_layout:
        grid-area: zone2
      label: 50%
      show_label: true
      tap_action:
        action: call-service
        service: light.turn_on
        service_data:
          entity_id: light.hue_color_candle_chambre_eric
          brightness_pct: 50
      styles:
        grid:
        - grid-template-areas: "\"i\" \"n\" \"l\""
        - grid-template-rows: min-content min-content 1fr
        card:
        - aspect-ratio: 1/1
        - background-color: |
            [[[
              var brightness = states['light.hue_color_candle_chambre_eric'].attributes.brightness;
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && brightness >= 127 && brightness <= 129)
                return "rgba(255, 160, 0, 0.1)";
              else
                return "transparent";
            ]]]
        - border-width: 1px
        - border-color: |
            [[[
              var brightness = states['light.hue_color_candle_chambre_eric'].attributes.brightness;
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && brightness >= 127 && brightness <= 129)
                return "#FFA000A9";
              else
                return "grey";
            ]]]
        icon:
        - color: |
            [[[
              var brightness = states['light.hue_color_candle_chambre_eric'].attributes.brightness;
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && brightness >= 127 && brightness <= 129)
                return "#FFA000A9";
              else
                return "grey";
            ]]]
        label:
        - font-weight: bold
        - color: |
            [[[
              var brightness = states['light.hue_color_candle_chambre_eric'].attributes.brightness;
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && brightness >= 127 && brightness <= 129)
                return "#FFA000A9";
              else
                return "grey";
            ]]]
    - type: custom:button-card
      view_layout:
        grid-area: zone3
      label: 75%
      show_label: true
      tap_action:
        action: call-service
        service: light.turn_on
        service_data:
          entity_id: light.hue_color_candle_chambre_eric
          brightness_pct: 75
      styles:
        grid:
        - grid-template-areas: "\"i\" \"n\" \"l\""
        - grid-template-rows: min-content min-content 1fr
        card:
        - aspect-ratio: 1/1
        - background-color: |
            [[[
              var brightness = states['light.hue_color_candle_chambre_eric'].attributes.brightness;
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && brightness >= 190 && brightness <= 192)
                return "rgba(255, 160, 0, 0.1)";
              else
                return "transparent";
            ]]]
        - border-width: 1px
        - border-color: |
            [[[
              var brightness = states['light.hue_color_candle_chambre_eric'].attributes.brightness;
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && brightness >= 190 && brightness <= 192)
                return "#FFA000A9";
              else
                return "grey";
            ]]]
        icon:
        - color: |
            [[[
              var brightness = states['light.hue_color_candle_chambre_eric'].attributes.brightness;
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && brightness >= 190 && brightness <= 192)
                return "#FFA000A9";
              else
                return "grey";
            ]]]
        label:
        - font-weight: bold
        - color: |
            [[[
              var brightness = states['light.hue_color_candle_chambre_eric'].attributes.brightness;
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && brightness >= 190 && brightness <= 192)
                return "#FFA000A9";
              else
                return "grey";
            ]]]
    - type: custom:button-card
      view_layout:
        grid-area: zone4
      label: 100%
      show_label: true
      tap_action:
        action: call-service
        service: light.turn_on
        service_data:
          entity_id: light.hue_color_candle_chambre_eric
          brightness_pct: 100
      styles:
        grid:
        - grid-template-areas: "\"i\" \"n\" \"l\""
        - grid-template-rows: min-content min-content 1fr
        card:
        - aspect-ratio: 1/1
        - background-color: |
            [[[
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && states['light.hue_color_candle_chambre_eric'].attributes.brightness == 255)
                return "rgba(255, 160, 0, 0.1)";
              else
                return "transparent";
            ]]]
        - border-width: 1px
        - border-color: |
            [[[
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && states['light.hue_color_candle_chambre_eric'].attributes.brightness == 255)
                return "#FFA000A9";
              else
                return "grey";
            ]]]
        icon:
        - color: |
            [[[
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && states['light.hue_color_candle_chambre_eric'].attributes.brightness == 255)
                return "#FFA000A9";
              else
                return "grey";
            ]]]
        label:
        - font-weight: bold
        - color: |
            [[[
              if (states['light.hue_color_candle_chambre_eric'].state == "on" && states['light.hue_color_candle_chambre_eric'].attributes.brightness == 255)
                return "#FFA000A9";
              else
                return "grey";
            ]]]
- type: custom:bubble-card
  card_type: pop-up
  hash: "#bureau"
  show_header: true
  force_icon: false
  show_state: false
  show_last_changed: false
  show_attribute: false
  button_type: name
  name: Lampes Bureau
  icon: hue:flourish-alt
  show_icon: true
  show_name: true
  card_layout: normal
  hide_backdrop: false
  close_on_click: false
  bg_opacity: "0"
  sub_button:
    main: []
    bottom: []
  cards:
  - type: vertical-stack
    cards:
    - type: custom:mushroom-light-card
      entity: light.bureau
      name: Lampes Bureau
      icon: hue:flourish-alt
      icon_color:
      layout: normal
      use_light_color: false
      show_brightness_control: true
      show_color_temp_control: false
      show_color_control: false
      collapsible_controls: false
      card_mod:
        style: |
          ha-card {
            border: 2px solid {% if is_state('light.bureau', 'on') %} #FFA000A9 {% else %} grey {% endif %};
            background-color: {% if is_state('light.bureau', 'on') %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
          }
    - type: custom:layout-card
      layout_type: custom:grid-layout
      layout:
        grid-template-columns: 25% 25% 25% 25%
        grid-template-rows: 100%
        grid-template-areas: |
          "zone1 zone2 zone3 zone4"
      cards:
      - type: custom:button-card
        view_layout:
          grid-area: zone1
        label: 25%
        show_label: true
        tap_action:
          action: call-service
          service: light.turn_on
          service_data:
            entity_id: light.bureau
            brightness_pct: 25
        styles:
          grid:
          - grid-template-areas: "\"i\" \"n\" \"l\""
          - grid-template-rows: min-content min-content 1fr
          card:
          - aspect-ratio: 1/1
          - background-color: |
              [[[
                var brightness = states['light.bureau'].attributes.brightness;
                if (states['light.bureau'].state == "on" && brightness >= 63 && brightness <= 65)
                  return "rgba(255, 160, 0, 0.1)";
                else
                  return "transparent";
              ]]]
          - border-width: 1px
          - border-color: |
              [[[
                var brightness = states['light.bureau'].attributes.brightness;
                if (states['light.bureau'].state == "on" && brightness >= 63 && brightness <= 65)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          icon:
          - color: |
              [[[
                var brightness = states['light.bureau'].attributes.brightness;
                if (states['light.bureau'].state == "on" && brightness >= 63 && brightness <= 65)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          label:
          - font-weight: bold
          - color: |
              [[[
                var brightness = states['light.bureau'].attributes.brightness;
                if (states['light.bureau'].state == "on" && brightness >= 63 && brightness <= 65)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
      - type: custom:button-card
        view_layout:
          grid-area: zone2
        label: 50%
        show_label: true
        tap_action:
          action: call-service
          service: light.turn_on
          service_data:
            entity_id: light.bureau
            brightness_pct: 50
        styles:
          grid:
          - grid-template-areas: "\"i\" \"n\" \"l\""
          - grid-template-rows: min-content min-content 1fr
          card:
          - aspect-ratio: 1/1
          - background-color: |
              [[[
                var brightness = states['light.bureau'].attributes.brightness;
                if (states['light.bureau'].state == "on" && brightness >= 127 && brightness <= 129)
                  return "rgba(255, 160, 0, 0.1)";
                else
                  return "transparent";
              ]]]
          - border-width: 1px
          - border-color: |
              [[[
                var brightness = states['light.bureau'].attributes.brightness;
                if (states['light.bureau'].state == "on" && brightness >= 127 && brightness <= 129)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          icon:
          - color: |
              [[[
                var brightness = states['light.bureau'].attributes.brightness;
                if (states['light.bureau'].state == "on" && brightness >= 127 && brightness <= 129)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          label:
          - font-weight: bold
          - color: |
              [[[
                var brightness = states['light.bureau'].attributes.brightness;
                if (states['light.bureau'].state == "on" && brightness >= 127 && brightness <= 129)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
      - type: custom:button-card
        view_layout:
          grid-area: zone3
        label: 75%
        show_label: true
        tap_action:
          action: call-service
          service: light.turn_on
          service_data:
            entity_id: light.bureau
            brightness_pct: 75
        styles:
          grid:
          - grid-template-areas: "\"i\" \"n\" \"l\""
          - grid-template-rows: min-content min-content 1fr
          card:
          - aspect-ratio: 1/1
          - background-color: |
              [[[
                var brightness = states['light.bureau'].attributes.brightness;
                if (states['light.bureau'].state == "on" && brightness >= 190 && brightness <= 192)
                  return "rgba(255, 160, 0, 0.1)";
                else
                  return "transparent";
              ]]]
          - border-width: 1px
          - border-color: |
              [[[
                var brightness = states['light.bureau'].attributes.brightness;
                if (states['light.bureau'].state == "on" && brightness >= 190 && brightness <= 192)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          icon:
          - color: |
              [[[
                var brightness = states['light.bureau'].attributes.brightness;
                if (states['light.bureau'].state == "on" && brightness >= 190 && brightness <= 192)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          label:
          - font-weight: bold
          - color: |
              [[[
                var brightness = states['light.bureau'].attributes.brightness;
                if (states['light.bureau'].state == "on" && brightness >= 190 && brightness <= 192)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
      - type: custom:button-card
        view_layout:
          grid-area: zone4
        label: 100%
        show_label: true
        tap_action:
          action: call-service
          service: light.turn_on
          service_data:
            entity_id: light.bureau
            brightness_pct: 100
        styles:
          grid:
          - grid-template-areas: "\"i\" \"n\" \"l\""
          - grid-template-rows: min-content min-content 1fr
          card:
          - aspect-ratio: 1/1
          - background-color: |
              [[[
                if (states['light.bureau'].state == "on" && states['light.bureau'].attributes.brightness == 255)
                  return "rgba(255, 160, 0, 0.1)";
                else
                  return "transparent";
              ]]]
          - border-width: 1px
          - border-color: |
              [[[
                if (states['light.bureau'].state == "on" && states['light.bureau'].attributes.brightness == 255)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          icon:
          - color: |
              [[[
                if (states['light.bureau'].state == "on" && states['light.bureau'].attributes.brightness == 255)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          label:
          - font-weight: bold
          - color: |
              [[[
                if (states['light.bureau'].state == "on" && states['light.bureau'].attributes.brightness == 255)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
- type: custom:bubble-card
  card_type: pop-up
  hash: "#ecranpc"
  show_header: true
  force_icon: false
  show_state: false
  show_last_changed: false
  show_attribute: false
  button_type: name
  name: Ecrans P.C.
  icon: mdi:television
  show_icon: true
  show_name: true
  card_layout: normal
  hide_backdrop: false
  close_on_click: false
  bg_opacity: "0"
  sub_button:
    main: []
    bottom: []
  cards:
  - type: vertical-stack
    cards:
    - type: custom:mushroom-light-card
      entity: light.moniteur_pc
      name: Ecrans P.C.
      icon: mdi:television
      icon_color:
      layout: normal
      use_light_color: false
      show_brightness_control: true
      show_color_temp_control: false
      show_color_control: false
      collapsible_controls: false
      card_mod:
        style: |
          ha-card {
            border: 2px solid {% if is_state('light.moniteur_pc', 'on') %} #FFA000A9 {% else %} grey {% endif %};
            background-color: {% if is_state('light.moniteur_pc', 'on') %}  rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
          }
    - type: custom:layout-card
      layout_type: custom:grid-layout
      layout:
        grid-template-columns: 25% 25% 25% 25%
        grid-template-rows: 100%
        grid-template-areas: |
          "zone1 zone2 zone3 zone4"
      cards:
      - type: custom:button-card
        view_layout:
          grid-area: zone1
        label: 25%
        show_label: true
        tap_action:
          action: call-service
          service: light.turn_on
          service_data:
            entity_id: light.moniteur_pc
            brightness_pct: 25
        styles:
          grid:
          - grid-template-areas: "\"i\" \"n\" \"l\""
          - grid-template-rows: min-content min-content 1fr
          card:
          - aspect-ratio: 1/1
          - background-color: |
              [[[
                var brightness = states['light.moniteur_pc'].attributes.brightness;
                if (states['light.moniteur_pc'].state == "on" && brightness >= 63 && brightness <= 65)
                  return " rgba(255, 160, 0, 0.1)";
                else
                  return "transparent";
              ]]]
          - border-width: 1px
          - border-color: |
              [[[
                var brightness = states['light.moniteur_pc'].attributes.brightness;
                if (states['light.moniteur_pc'].state == "on" && brightness >= 63 && brightness <= 65)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          icon:
          - color: |
              [[[
                var brightness = states['light.moniteur_pc'].attributes.brightness;
                if (states['light.moniteur_pc'].state == "on" && brightness >= 63 && brightness <= 65)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          label:
          - font-weight: bold
          - color: |
              [[[
                var brightness = states['light.moniteur_pc'].attributes.brightness;
                if (states['light.moniteur_pc'].state == "on" && brightness >= 63 && brightness <= 65)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
      - type: custom:button-card
        view_layout:
          grid-area: zone2
        label: 50%
        show_label: true
        tap_action:
          action: call-service
          service: light.turn_on
          service_data:
            entity_id: light.moniteur_pc
            brightness_pct: 50
        styles:
          grid:
          - grid-template-areas: "\"i\" \"n\" \"l\""
          - grid-template-rows: min-content min-content 1fr
          card:
          - aspect-ratio: 1/1
          - background-color: |
              [[[
                var brightness = states['light.moniteur_pc'].attributes.brightness;
                if (states['light.moniteur_pc'].state == "on" && brightness >= 127 && brightness <= 129)
                  return " rgba(255, 160, 0, 0.1)";
                else
                  return "transparent";
              ]]]
          - border-width: 1px
          - border-color: |
              [[[
                var brightness = states['light.moniteur_pc'].attributes.brightness;
                if (states['light.moniteur_pc'].state == "on" && brightness >= 127 && brightness <= 129)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          icon:
          - color: |
              [[[
                var brightness = states['light.moniteur_pc'].attributes.brightness;
                if (states['light.moniteur_pc'].state == "on" && brightness >= 127 && brightness <= 129)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          label:
          - font-weight: bold
          - color: |
              [[[
                var brightness = states['light.moniteur_pc'].attributes.brightness;
                if (states['light.moniteur_pc'].state == "on" && brightness >= 127 && brightness <= 129)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
      - type: custom:button-card
        view_layout:
          grid-area: zone3
        label: 75%
        show_label: true
        tap_action:
          action: call-service
          service: light.turn_on
          service_data:
            entity_id: light.moniteur_pc
            brightness_pct: 75
        styles:
          grid:
          - grid-template-areas: "\"i\" \"n\" \"l\""
          - grid-template-rows: min-content min-content 1fr
          card:
          - aspect-ratio: 1/1
          - background-color: |
              [[[
                var brightness = states['light.moniteur_pc'].attributes.brightness;
                if (states['light.moniteur_pc'].state == "on" && brightness >= 190 && brightness <= 192)
                  return " rgba(255, 160, 0, 0.1)";
                else
                  return "transparent";
              ]]]
          - border-width: 1px
          - border-color: |
              [[[
                var brightness = states['light.moniteur_pc'].attributes.brightness;
                if (states['light.moniteur_pc'].state == "on" && brightness >= 190 && brightness <= 192)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          icon:
          - color: |
              [[[
                var brightness = states['light.moniteur_pc'].attributes.brightness;
                if (states['light.moniteur_pc'].state == "on" && brightness >= 190 && brightness <= 192)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          label:
          - font-weight: bold
          - color: |
              [[[
                var brightness = states['light.moniteur_pc'].attributes.brightness;
                if (states['light.moniteur_pc'].state == "on" && brightness >= 190 && brightness <= 192)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
      - type: custom:button-card
        view_layout:
          grid-area: zone4
        label: 100%
        show_label: true
        tap_action:
          action: call-service
          service: light.turn_on
          service_data:
            entity_id: light.moniteur_pc
            brightness_pct: 100
        styles:
          grid:
          - grid-template-areas: "\"i\" \"n\" \"l\""
          - grid-template-rows: min-content min-content 1fr
          card:
          - aspect-ratio: 1/1
          - background-color: |
              [[[
                if (states['light.moniteur_pc'].state == "on" && states['light.moniteur_pc'].attributes.brightness == 255)
                  return " rgba(255, 160, 0, 0.1)";
                else
                  return "transparent";
              ]]]
          - border-width: 1px
          - border-color: |
              [[[
                if (states['light.moniteur_pc'].state == "on" && states['light.moniteur_pc'].attributes.brightness == 255)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          icon:
          - color: |
              [[[
                if (states['light.moniteur_pc'].state == "on" && states['light.moniteur_pc'].attributes.brightness == 255)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
          label:
          - font-weight: bold
          - color: |
              [[[
                if (states['light.moniteur_pc'].state == "on" && states['light.moniteur_pc'].attributes.brightness == 255)
                  return "#FFA000A9";
                else
                  return "grey";
              ]]]
- type: custom:streamline-card
  template: nav_bar
```

---

## Points à vérifier

- [B1] non corrigé dans le YAML (voir plus haut).
- La chaîne d'absence (qui coupe les deux prises, et quand) n'est pas documentée à jour.
- Le dossier YAML contient une sauvegarde ancienne `page_L3C1_eclairage_droite.bak_2026_05_13.yaml`.
- Les positions exactes des pastilles en overlay (marges en px dans le `card_mod`) et l'animation flame n'ont pas été vérifiées visuellement.

---

## 🔗 FICHIERS LIÉS

- [`PAGE_ECLAIRAGE_GAUCHE.md`](../02_page_gauche/PAGE_ECLAIRAGE_GAUCHE.md) - page gauche (Entrée, Salon, Cuisine, Couloir)
- [`L3C1_Vignette_ECLAIRAGE.md`](../01_vignette/L3C1_Vignette_ECLAIRAGE.md) - vignette d'accès à cette page
- [`PAGE_PRISES.md`](../../L3C2_PRISES/02_page/PAGE_PRISES.md) - page prises (même structure)
- [`CARD_PRESENCE_HOME.md`](../../L0C0_PAGE_Home/11_Carte%20Pr%C3%A9sence/CARD_PRESENCE_HOME.md) - détection de présence (carte de la page d'accueil)

---

← Retour : [`L3C1_Vignette_ECLAIRAGE.md`](../01_vignette/L3C1_Vignette_ECLAIRAGE.md) | → Suite : [`L3C2_PRISES/`](../../L3C2_PRISES/)


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L3C1_Vignette_ECLAIRAGE]]  [[PAGE_ECLAIRAGE_GAUCHE]]*
