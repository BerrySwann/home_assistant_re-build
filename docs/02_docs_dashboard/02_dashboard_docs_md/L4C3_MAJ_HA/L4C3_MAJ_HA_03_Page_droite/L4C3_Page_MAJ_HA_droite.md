<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page%20droite-ff9800?style=flat-square)](.)

</div>

> **Ancienne mention "DOC VERROUILLÉE - Modifs interdites" (PAGE_MAJ.md du 2026-03-18) retirée** : le YAML a été ré-exporté depuis l'éditeur HA le 2026-10-11 à la demande d'Eric et ce MD a été réécrit en conséquence.

| Champ | Valeur |
|:------|:-------|
| 📁 **Path dashboard** | `/dashboard-tablette/maj` |
| 🔗 **Accès depuis** | Vignette L4C3 (clic) |
| 🏗️ **Layout** | `type: grid` - 4 cartes de niveau 1 (2 headings + 2 vertical-stack) |
| 📄 **Fichier YAML** | `L4C3_MAJ_HA/03_page_droite/page_L4C3_maj_ha_droite.yaml` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 📅 **Modifié le** | 2026-10-11 |

---

# 🔄 PAGE MAJ - DROITE : H.A. UPDATE et H.A. ADD-ON

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Contenu de la page](#contenu-de-la-page)
3. [Entités utilisées](#entités-utilisées)
4. [Code YAML](#code-yaml)
5. [Points à vérifier](#points-à-vérifier)

---

## 🎯 VUE D'ENSEMBLE

Colonne de droite de la page `/dashboard-tablette/maj`. Elle liste les mises à jour **en attente** par catégorie (add-ons, HACS, Zigbee2MQTT), signale les intégrations qui demandent un redémarrage, puis affiche les cartes de mise à jour de Core et Supervisor avec leur lien de notes de version. Deux titres : `H.A. UPDATE` et `H.A. ADD-ON` (heading, icône `mdi:home-assistant`, tap = retour `/dashboard-tablette/0`).

La colonne de gauche (versions Core, OS, Supervisor et HACS) est documentée dans [`PAGE_MAJ_GAUCHE.md`](../02_page_gauche/PAGE_MAJ_GAUCHE.md).

```
┌──────────────────────────────────────────────────────────────┐
│ H.A. UPDATE                                                  │
│ ■ Addons updates   titre + alerte "N MàJ sur total"          │
│                    auto-entities : domaine update, état on,  │
│                    hors Home*, hors hacs, hors mqtt          │
│ ■ HACS updates     titre + alerte "N MàJ sur total"          │
│                    auto-entities : intégration hacs, état on │
│ ■ Redémarrage      alerte si une MàJ demande un redémarrage  │
│ ■ ZigBee2MQTT      titre + alerte "N MàJ sur total"          │
│                    auto-entities : intégration mqtt, état on │
│                                                              │
│ H.A. ADD-ON                                                  │
│ ■ Home Assistant Core        update-card + chip Changelog    │
│ ■ Home Assistant Supervisor  update-card + chip Changelog    │
└──────────────────────────────────────────────────────────────┘
```

---

## Contenu de la page

| Bloc | Carte | Rôle |
|:--|:--|:--|
| Addons updates | `button-card` titre + `markdown` (compteur) + `auto-entities` | Compte les `update.*` de l'intégration `hassio` hors Core, OS et Supervisor ; liste en boutons les mises à jour à `on` (hors `Home*`, `hacs`, `mqtt`). Bouton = `update.install` sur l'entité |
| HACS updates | idem | Compteur et liste des `update.*` de l'intégration `hacs` à `on` |
| Redémarrage requis | `markdown` | Liste les entités `update` dont l'attribut `release_summary` est exactement `<ha-alert alert-type='error'>Restart of Home Assistant required</ha-alert>` ; n'affiche rien s'il n'y en a aucune |
| ZigBee2MQTT | idem | Compteur et liste des `update.*` de l'intégration `mqtt` à `on` |
| H.A. ADD-ON | `mushroom-update-card` x2 + `mushroom-chips-card` x2 | Core et Supervisor : carte de mise à jour sans boutons de contrôle (`show_buttons_control: false`), lien "Release Changelog" (Core : notes de version du site Home Assistant ; Supervisor : releases GitHub du Supervisor) ; les puces CPU et mémoire ont été retirées le 2026-10-25 (capteurs hassio désactivés par défaut, non utilisés sur le mini PC) |

Chaque ligne de liste (auto-entities) est un `custom:button-card` : nom, versions installée et dernière, lien vers les notes de version, icône `mdi:upload-circle` (devient `mdi:rotate-right` animée pendant l'installation) et tap = `update.install`.

---

## Entités utilisées

| Entité | Source | Usage |
|:--|:--|:--|
| `update.*` (domaine `update`, état `on`) | HA natif / intégrations | listes auto-entities (add-ons, HACS, mqtt) |
| `update.install` | service HA | action du bouton d'installation (service, pas une entité) |
| `update.home_assistant_core_update` | HA natif | carte Core (H.A. ADD-ON) |
| `update.home_assistant_supervisor_update` | HA natif | carte Supervisor (H.A. ADD-ON) |
| `update.home_assistant_operating_system_update` | HA natif | exclue du compteur Add-ons |

Les 4 capteurs CPU/RAM de Core et Supervisor (plateforme hassio, désactivés par défaut) ne sont plus utilisés par la page depuis le 2026-10-25. Le domaine `update` compte 126 entités dans HA le 2026-10-11, aucune n'est à `on`.

---

## Code YAML

> Copie du fichier `page_L4C3_maj_ha_droite.yaml` (le fichier YAML fait foi).

```yaml
type: grid
cards:
  - type: heading
    icon: mdi:home-assistant
    heading: H.A. UPDATE
    heading_style: title
    badges: []
    tap_action:
      action: navigate
      navigation_path: /dashboard-tablette/0
    layout_options:
      grid_columns: full
      grid_rows: 1
  - type: vertical-stack
    cards:
      - type: custom:button-card
        show_name: false
        show_icon: false
        show_state: false
        card_mod:
          style: |
            ha-card {
              pointer-events: none;
            }
        styles:
          grid:
            - grid-template-areas: '"card1 card2 card3"'
            - grid-template-columns: 1fr 0.63fr 0.1fr
            - grid-template-rows: 1fr
          card:
            - margin-top: 1.5rem
            - padding: 5px 0px 5px 10px
            - background: rgba(0,0,0,0)
          custom_fields:
            card1:
              - width: 90%
            card2:
              - align-self: top
              - height: 100%
        custom_fields:
          card1:
            card:
              type: custom:mushroom-title-card
              title: Addons updates
              alignment: start
              card_mod:
                style: |
                  .header {
                    padding: 0px !important;
                  }
                  .header div {
                    margin: 0px !important
                  }
          card2:
            card:
              type: markdown
              content: >-
                {% set
                rejet=['update.home_assistant_core_update','update.home_assistant_operating_system_update','update.home_assistant_supervisor_update']
                %}  {% set
                maj=integration_entities('hassio')|select('search','update.')|select('is_state','on')|reject('in',rejet)|list|count|int(2)
                %}  {% set
                total=integration_entities('hassio')|select('search','update.')|reject('in',rejet)|list|count|int(2)
                %}  {% if maj == 0 %} <ha-alert alert-type="success"
                title="{{maj}} MàJ sur {{total}}" > {% elif maj == 1 %}
                <ha-alert alert-type="warning" title="{{maj}} MàJ sur {{total}}"
                > {% elif maj > 1 %} <ha-alert alert-type="warning"
                title="{{maj}} Màj sur {{total}}" ></ha-alert> {% else %} {%
                endif %}
              card_mod:
                style: |
                  :host {
                    --ha-card-margin: 0px;
                    --ha-card-background: #00000000 !important;
                    --ha-card-border-color: #00000000 !important;
                    }
                  ha-markdown.no-header {
                    padding: 0px !important;
                    margin: 0px !important;
                    margin-right: 3em !important;
                    margin-left: -3em !important;
                  }
                  ha-card {
                    font-size: 1rem;
                    --mdc-icon-size: 1.3rem;
                   }
      - type: custom:auto-entities
        card:
          type: vertical-stack
        card_param: cards
        filter:
          include:
            - domain: update
              state: 'on'
              options:
                type: custom:button-card
                show_name: true
                show_icon: true
                show_state: true
                show_entity_picture: true
                variables:
                  sensor: |
                    [[[
                      let name = Object.values(entity)
                     return name[0]
                      ]]]
                name: |
                  [[[
                    return entity.attributes.friendly_name.replace('Home Assistant','HA').replace('Update','')
                  ]]]
                state_display: |
                  [[[ if(entity.state== "on")
                   return 'v' + entity.attributes.installed_version +' - v' + entity.attributes.latest_version
                  else if(entity.state== "off")
                   return helpers.localize(entity) +' - v'+ entity.attributes.installed_version
                  else
                   return "instal - "+entity.attributes.in_progress+"%"
                  ]]]
                styles:
                  grid:
                    - grid-template-areas: '"i n n cardupload" "i s s cardupload"'
                    - grid-template-columns: 0.6fr 1fr 1.6fr 1fr;
                    - grid-template-rows: repeat(2, 50%);
                    - gap: 0px 0px;
                  card:
                    - padding: 0px
                    - height: 100%
                    - width: 100%
                  icon:
                    - align-self: center
                    - left: 25%
                    - width: 55%
                  name:
                    - justify-self: start
                    - font-size: 0.9em
                    - font-weight: 450
                    - padding-top: 8px
                  state:
                    - justify-self: start
                    - font-size: 0.75em
                    - padding-bottom: 0.7em
                custom_fields:
                  cardupload:
                    card:
                      show_icon: true
                      type: custom:button-card
                      icon: |
                        [[[
                         if(entity.state == "off")
                         return ""
                         if(entity.attributes.in_progress == false)
                         return 'mdi:upload-circle'
                         else return 'mdi:rotate-right'
                        ]]]
                      styles:
                        card:
                          - background: none
                          - border: none
                        icon:
                          - animation: |
                              [[[
                               if(entity.attributes.in_progress == false)
                                return '' 
                               else return 'rotating 1s linear infinite'
                              ]]]
                          - color: |
                              [[[
                               if(entity.state == 'on' & entity.attributes.in_progress != false)
                               return 'green'
                               else return 'rgba(85,252,252, 1)'
                              ]]]
                          - left: 17%
                      tap_action:
                        action: perform-action
                        perform_action: update.install
                        target:
                          entity_id: '[[[return variables.sensor]]]'
          exclude:
            - name: Home*
            - integration: hacs
            - integration: mqtt
          card_param: cards
      - type: custom:button-card
        show_name: false
        show_icon: false
        show_state: false
        card_mod:
          style: |
            ha-card {
              pointer-events: none;
            }
        styles:
          grid:
            - grid-template-areas: '"card1 card2 card3"'
            - grid-template-columns: 1fr 0.63fr 0.1fr
            - grid-template-rows: 1fr
          card:
            - padding: 5px 0px 5px 10px
            - background: rgba(0,0,0,0)
          custom_fields:
            card1:
              - width: 90%
            card2:
              - align-self: top
              - height: 100%
        custom_fields:
          card1:
            card:
              type: custom:mushroom-title-card
              title: HACS updates
              alignment: start
              card_mod:
                style: |
                  .header {
                    padding: 0px !important;
                  }
                  .header div {
                    margin: 0px !important
                  }
          card2:
            card:
              type: markdown
              content: >-
                {% set
                maj=integration_entities('hacs')|select('search','update.')|select('is_state','on')|reject('in','update.hacs_update')|list|count|int(2)
                %}  {% set
                total=integration_entities('hacs')|select('search','update.')|reject('in','update.hacs_update')|list|count|int(2)
                %}  {% if maj == 0 %} <ha-alert alert-type="success"
                title="{{maj}} MàJ sur {{total}}" > {% elif maj == 1 %}
                <ha-alert alert-type="warning" title="{{maj}} MàJ sur {{total}}"
                > {% elif maj > 1 %} <ha-alert alert-type="warning"
                title="{{maj}}  màj sur {{total}}" ></ha-alert> {% else %} {%
                endif %}
              card_mod:
                style: |
                  :host {
                    --ha-card-margin: 0px;
                    --ha-card-background: #00000000 !important;
                    --ha-card-border-color: #00000000 !important;
                    }
                  ha-markdown.no-header {
                    padding: 0px !important;
                    margin: 0px !important;
                    margin-right: 3em !important;
                    margin-left: -3em !important;
                  }
                  ha-card {
                    font-size: 1rem;
                    --mdc-icon-size: 1.3rem;
                   }
      - type: markdown
        content: >-
          {% set maj = states.update |
          selectattr('attributes.release_summary','defined') |
          selectattr('attributes.release_summary','eq','<ha-alert
          alert-type=\'error\'>Restart of Home Assistant required</ha-alert>')
          |map(attribute='name') |list %}

          {% set maj_count = maj|count|int(2) %}

          {% if maj_count >= 1 %} <ha-alert alert-type="error"
          title="{{maj_count}} intégrations nécessitent un redémarrage">

          <hr>

          <ul>{% for i in maj%}

          <li>{{i}}</li>

          {% endfor%}</ul>

          {% else %}

          {% endif %}</ha-alert>
        card_mod:
          style: |
            :host {
              --ha-card-margin: 0px;
              --ha-card-background: #00000000 !important;
              --ha-card-border-color: #00000000 !important;
              }
            ha-markdown.no-header {
              padding: 4rem !important;
              padding-top: 0rem !important;
              padding-bottom: 0rem !important;
            }
      - type: custom:auto-entities
        card:
          type: vertical-stack
        card_param: cards
        filter:
          include:
            - domain: update
              state: 'on'
              integration: hacs
              options:
                type: custom:button-card
                show_name: true
                show_icon: true
                show_state: true
                show_entity_picture: true
                variables:
                  url: |
                    [[[
                      return entity.attributes.release_url
                    ]]]
                  sensor: |
                    [[[
                      let name = Object.values(entity)
                     return name[0]
                      ]]]
                name: |
                  [[[
                    return entity.attributes.friendly_name.replace('update','')
                  ]]]
                state_display: >
                  [[[ 

                  if(entity.state== "on" & entity.attributes.in_progress ==
                  false)
                     return  entity.attributes.installed_version +' - ' + entity.attributes.latest_version
                  else if(entity.state== "off")
                   return helpers.localize(entity) +' - '+ entity.attributes.installed_version
                  else
                    return "instal - "+entity.attributes.in_progress+"%"
                  ]]]
                styles:
                  grid:
                    - grid-template-areas: '"i n n cardupload" "i s cardurl cardupload"'
                    - grid-template-columns: 1fr 1fr 1fr 1.5fr;
                    - grid-template-rows: repeat(2, 50%);
                    - gap: 0px 0px;
                  card:
                    - padding: 0px
                    - height: 100%
                    - width: 100%
                  icon:
                    - align-self: center
                    - left: 25%
                    - width: 55%
                  name:
                    - justify-self: start
                    - font-size: 0.9em
                    - font-weight: 450
                    - padding-top: 8px
                  state:
                    - justify-self: start
                    - font-size: 0.75em
                    - padding-bottom: 0.7em
                    - padding-right: 8rem
                  custom_fields:
                    cardurl:
                      - justify-self: center
                      - margin-bottom: 0.7em
                      - margin-left: 2rem
                      - margin-right: -2rem
                custom_fields:
                  cardurl:
                    card:
                      type: custom:button-card
                      show_icon: false
                      name: |
                        [[[
                         if (variables.url == null)return ""
                         else
                          {return '<a style="color:white" href="'+[variables.url]+'">'+[variables.url.substr(8,18).toLowerCase()]+'</a>'}
                         endif
                        ]]]
                      tap_action:
                        action: url
                        url_path: |
                          [[[
                           return variables.url
                          ]]]
                      styles:
                        card:
                          - background: rgba(100,150,255,0.5)
                          - width: 13rem
                          - box-sizing: border-box
                          - padding: 0px
                        name:
                          - font-size: 1.2rem
                          - font-weight: bold
                          - font-style: italic
                  cardupload:
                    card:
                      show_icon: true
                      type: custom:button-card
                      icon: |
                        [[[
                         if(entity.state == "off")
                         return ""
                         if(entity.attributes.in_progress == false)
                         return 'mdi:upload-circle'
                         else return 'mdi:rotate-right'
                        ]]]
                      styles:
                        card:
                          - background: none
                          - border: none
                        icon:
                          - animation: |
                              [[[
                               if(entity.attributes.in_progress == false)
                                return '' 
                               else return 'rotating 1s linear infinite'
                              ]]]
                          - color: |
                              [[[
                               if(entity.state == 'on' & entity.attributes.in_progress != false)
                               return 'green'
                               else return 'rgba(85,252,252, 1)'
                              ]]]
                          - left: 18%
                          - width: 40%
                      tap_action:
                        action: perform-action
                        perform_action: update.install
                        target:
                          entity_id: '[[[return variables.sensor]]]'
          exclude:
            - entity_id: update.hacs_update
          card_param: cards
        sort:
          method: friendly_name
      - type: custom:button-card
        show_name: false
        show_icon: false
        show_state: false
        card_mod:
          style: |
            ha-card {
              pointer-events: none;
            }
        styles:
          grid:
            - grid-template-areas: '"card1 card2 card3"'
            - grid-template-columns: 1fr 0.63fr 0.1fr
            - grid-template-rows: 1fr
          card:
            - padding: 5px 0px 5px 10px
            - background: rgba(0,0,0,0)
          custom_fields:
            card1:
              - width: 90%
            card2:
              - align-self: top
              - height: 100%
        custom_fields:
          card1:
            card:
              type: custom:mushroom-title-card
              title: ZigBee2MQTT
              alignment: start
              card_mod:
                style: |
                  .header {
                    padding: 0px !important;
                  }
                  .header div {
                    margin: 0px !important
                  }
          card2:
            card:
              type: markdown
              content: >-
                {% set
                maj=integration_entities('mqtt')|select('search','update.')|select('is_state','on')|list|count|int(2)
                %}  {% set
                total=integration_entities('mqtt')|select('search','update.')|list|count|int(2)
                %}  {% if maj == 0 %} <ha-alert alert-type="success"
                title="{{maj}} MàJ sur {{total}}" > {% elif maj == 1 %}
                <ha-alert alert-type="warning" title="{{maj}} Màj sur {{total}}"
                > {% elif maj > 1 %} <ha-alert alert-type="warning"
                title="{{maj}} mises a jour sur {{total}}" ></ha-alert> {% else
                %} {% endif %}
              card_mod:
                style: |
                  :host {
                    --ha-card-margin: 0px;
                    --ha-card-background: #00000000 !important;
                    --ha-card-border-color: #00000000 !important;
                    }
                  ha-markdown.no-header {
                    padding: 0px !important;
                    margin: 0px !important;
                    margin-right: 3em !important;
                    margin-left: -3em !important;
                  }
                  ha-card {
                    font-size: 1rem;
                    --mdc-icon-size: 1.3rem;
                   }
      - type: custom:auto-entities
        card:
          type: vertical-stack
        card_param: cards
        filter:
          include:
            - domain: update
              state: 'on'
              integration: mqtt
              options:
                type: custom:button-card
                show_name: true
                show_icon: true
                show_state: true
                show_entity_picture: true
                variables:
                  sensor: |
                    [[[
                      let name = Object.values(entity)
                     return name[0]
                      ]]]
                name: |
                  [[[
                    return entity.attributes.friendly_name.replace('Home Assistant','HA').replace('Update','')
                  ]]]
                state_display: >
                  [[[ if(entity.state== "on" & entity.attributes.in_progress ==
                  false)
                   return 'v' + entity.attributes.installed_version +' - v' + entity.attributes.latest_version
                  else if(entity.state== "off")
                   return helpers.localize(entity) +' - v'+ entity.attributes.installed_version
                  else
                   return "instal - "+entity.attributes.in_progress+"%"
                  ]]]
                styles:
                  grid:
                    - grid-template-areas: '"i n n cardupload" "i s s cardupload"'
                    - grid-template-columns: 0.6fr 1fr 1.6fr 1fr;
                    - grid-template-rows: repeat(2, 50%);
                    - gap: 0px 0px;
                  card:
                    - padding: 0px
                    - height: 100%
                    - width: 100%
                  icon:
                    - align-self: center
                    - left: 25%
                    - width: 55%
                  name:
                    - justify-self: start
                    - font-size: 0.9em
                    - font-weight: 450
                    - padding-top: 8px
                  state:
                    - justify-self: start
                    - font-size: 0.75em
                    - padding-bottom: 0.7em
                custom_fields:
                  cardupload:
                    card:
                      show_icon: true
                      type: custom:button-card
                      icon: |
                        [[[
                         if(entity.state == "off")
                         return ""
                         if(entity.attributes.in_progress == false)
                         return 'mdi:upload-circle'
                         else return 'mdi:rotate-right'
                        ]]]
                      styles:
                        card:
                          - background: none
                          - border: none
                        icon:
                          - animation: |
                              [[[
                               if(entity.attributes.in_progress == false)
                                return '' 
                               else return 'rotating 1s linear infinite'
                              ]]]
                          - color: |
                              [[[
                               if(entity.state == 'on' & entity.attributes.in_progress != false)
                               return 'green'
                               else return 'rgba(85,252,252, 1)' 
                              ]]]
                          - left: 17%
                      tap_action:
                        action: perform-action
                        perform_action: update.install
                        target:
                          entity_id: '[[[return variables.sensor]]]'
          exclude: []
          card_param: cards
        sort:
          method: friendly_name
  - type: heading
    icon: mdi:home-assistant
    heading: H.A. ADD-ON
    heading_style: title
    badges: []
    tap_action:
      action: navigate
      navigation_path: /dashboard-tablette/0
    layout_options:
      grid_columns: full
      grid_rows: 1
  - type: vertical-stack
    cards:
      - type: vertical-stack
        cards:
          - type: custom:mushroom-update-card
            entity: update.home_assistant_core_update
            show_buttons_control: false
            icon_type: entity-picture
            layout: horizontal
            secondary_info: none
            name: Home Assistant Core
            card_mod:
              style: |
                ha-card {
                    --card-primary-line-height: 2.5rem;
                    --card-primary-font-size: 1.7rem;
                    --card-primary-font-weight: normal;
                    border: none !important;
                    box-shadow: none !important;
                    background: rgba(0,0,0,0);
                    margin-top: 1rem;
                 }
          - type: custom:mushroom-chips-card
            chips:
              - type: template
                icon: mdi:web
                icon_color: blue
                content: Release Changelog
                tap_action:
                  action: url
                  url_path: https://www.home-assistant.io/latest-release-notes/
      - type: vertical-stack
        cards:
          - type: custom:mushroom-update-card
            entity: update.home_assistant_supervisor_update
            show_buttons_control: false
            icon_type: entity-picture
            layout: horizontal
            secondary_info: none
            name: Home Assistant Supervisor
            card_mod:
              style: |
                ha-card {
                    --card-primary-line-height: 2.5rem;
                    --card-primary-font-size: 1.7rem;
                    --card-primary-font-weight: normal;
                    border: none !important;
                    box-shadow: none !important;
                    background: rgba(0,0,0,0);
                    margin-top: 1.2rem;
                 }
          - type: custom:mushroom-chips-card
            chips:
              - type: template
                icon: mdi:web
                icon_color: blue
                content: Release Changelog
                tap_action:
                  action: url
                  url_path: https://github.com/home-assistant/supervisor/releases/latest
```

---

## Points à vérifier

- Le compteur "Addons updates" repose sur `integration_entities('hassio')` : il ne compte que les entités de l'intégration `hassio`. Les listes auto-entities, elles, prennent tout le domaine `update` à `on` (hors exclusions). Les deux peuvent donc différer.
- Les textes d'alerte sont écrits en trois formes différentes selon les blocs ("MàJ", "Màj", "màj", "mises a jour") : cosmétique.
- La copie supprimée `page_L4C3_maj_ha.yaml` (page "principale", à la corbeille) contenait 4 lignes de commentaires du 2026-06-15 : sauvegarde de la page complète (Addons + HACS + Z2M + Core + Supervisor) et notes sur l'animation `mdi:rotate-right` de `cardupload` (l'icône passe de `mdi:upload-circle` à `mdi:rotate-right` quand `in_progress` est différent de `false`). Ces notes ne sont plus dans les YAML actuels.

---

## 🔗 FICHIERS LIÉS

- [`PAGE_MAJ_GAUCHE.md`](../02_page_gauche/PAGE_MAJ_GAUCHE.md) - page gauche (H.A. SERVER)
- [`L4C3_Vignette_MAJ_HA.md`](../01_vignette/L4C3_Vignette_MAJ_HA.md) - vignette
- [`DEPENDANCES_GLOBALES.md`](../../../../XX_docs_MD_system/DEPENDANCES_GLOBALES/DEPENDANCES_GLOBALES.md) - chaîne complète L4C3

---

← Retour : [`L4C3_Vignette_MAJ_HA.md`](../01_vignette/L4C3_Vignette_MAJ_HA.md)


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L4C3_Vignette_MAJ_HA]]  [[PAGE_MAJ_GAUCHE]]*
