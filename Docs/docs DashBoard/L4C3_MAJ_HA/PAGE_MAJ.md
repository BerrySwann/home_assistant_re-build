<div align="center">

[![Statut](https://img.shields.io/badge/Statut-VERROUILLÉ-44739e?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-INTERDITES-f44336?style=flat-square)](.)&nbsp;

[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--18-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page%20D%C3%A9taill%C3%A9e-ff9800?style=flat-square)](.)

</div>

> **🔒 DOC VERROUILLÉE — VERSION FINALE**
> Ce fichier est considéré comme terminé. Aucune modification ne doit être apportée sans décision explicite.
>
> ⚠️ **2 bugs esthétiques connus (à traiter ultérieurement) :**
> 1. Icône HA dans la vignette — positionnement à revoir (alignement vertical résiduel à peaufiner)
> 2. Page MAJ — mise en page des grilles à affiner sur petit écran (espacement entre Grille 1 et Grille 2)

| Champ | Valeur |
|:------|:-------|
| 📁 **Path dashboard** | `/dashboard-tablette/maj` |
| 🔗 **Accès depuis** | Vignette L4C3 (clic) |
| 🏗️ **Layout** | `type: grid` × 2 colonnes |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-18 |
| 🏠 **Version HA** | 2026.3 |

---

# 🔄 PAGE MAJ — `/dashboard-tablette/maj`

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Grille 1 — H.A. SERVER](#grille-1--ha-server)
3. [Grille 2 — H.A. UPDATE](#grille-2--ha-update)

---

## 🎯 VUE D'ENSEMBLE

La page MAJ est composée de **deux grilles côte à côte** (`type: grid`). Elle regroupe toutes les informations de mises à jour de Home Assistant, organisées par catégorie.

```
┌──────────────────────────┬──────────────────────────────────────┐
│   GRILLE 1               │   GRILLE 2                           │
│   H.A. SERVER            │   H.A. UPDATE                        │
│                          │                                      │
│ ■ HA Server (titre)      │ ■ Addons updates (titre + compteur)  │
│   Core / OS / Supervisor │   auto-entities hassio (sauf Core)   │
│   version + MAJ compteur │                                      │
│                          │ ■ HACS updates (titre + compteur)    │
│ ■ HA Core update-card    │   auto-entities hacs                 │
│   + template info        │                                      │
│ ■ HA OS update-card      │ ■ Redémarrage requis (markdown)      │
│   + template info        │                                      │
│ ■ HA Supervisor card     │ ■ ZigBee2MQTT (titre + compteur)     │
│   + template info        │   auto-entities mqtt                 │
│                          │                                      │
│ ■ HACS (titre + chips)   │ ■ H.A. ADD-ON                        │
│   auto-entities hacs     │   Core update-card + chips CPU/RAM   │
│   update.hacs_update     │   Supervisor card + chips CPU/RAM    │
└──────────────────────────┴──────────────────────────────────────┘
```

---

## GRILLE 1 — H.A. SERVER

```yaml
type: grid
cards:
  - type: heading
    icon: mdi:home-assistant
    heading: H.A. SERVER
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
              pointer-events: none;background: transparent !important;
              box-shadow: transparent !important;
            }
        styles:
          grid:
            - grid-template-areas: "\"card1 card2 card3\" "
            - grid-template-columns: 1fr 0.69fr 0.05fr
            - grid-template-rows: 0fr 0fr
          card:
            - margin-top: 1.5rem
            - padding: 5px 0px 5px 10px
            - background: rgba(0,0,0,0)
          custom_fields:
            card1: null
            card2:
              - align-self: top
              - height: 100%
        custom_fields:
          card1:
            card:
              type: custom:mushroom-title-card
              title: Home Assistant Server
              subtitle: >
                Core v{{ state_attr('update.home_assistant_core_update',
                'installed_version') }} - OS v{{
                  state_attr('update.home_assistant_operating_system_update',
                'installed_version') }} - Supervisor v{{
                state_attr('update.home_assistant_supervisor_update',
                'installed_version') }}
              alignment: start
              card_mod:
                style: |
                  .header {
                    padding: 0px !important;
                  }
                  ha-card {
                      margin-right: -15rem;
                   }
          card2:
            card:
              type: markdown
              content: >-
                {% set
                maj=integration_entities('hassio')|select('search','update.home')|select('is_state','on')|list|count|int(2)
                %}  {% set
                total=integration_entities('hassio')|select('search','update.home')|list|count|int(2)
                %}  {% if maj == 0 %} <ha-alert alert-type="success"
                title="{{maj}}  MàJ
                 sur {{total}}" > {% elif maj == 1 %} <ha-alert
                alert-type="warning" title="{{maj}} MàJ sur {{total}}" > {% elif
                maj > 1 %} <ha-alert alert-type="warning" title="{{maj}} mises a
                jour sur {{total}}" ></ha-alert> {% else %} {% endif %}
              card_mod:
                style: |
                  :host {
                    --ha-card-margin: 0px;
                    --ha-card-border-color: transparent !important;
                    --card-background-color: transparent !important;
                  }
                  ha-markdown.no-header {
                    margin: 0px !important;
                  }
                  ha-card {
                    margin-top: -1rem;
                    font-size: 1rem;
                    --mdc-icon-size: 1.3rem;
                   }
      - type: vertical-stack
        cards:
          - type: horizontal-stack
            cards:
              - type: custom:mushroom-update-card
                entity: update.home_assistant_core_update
                name: HA Core
                show_buttons_control: true
                icon_type: entity-picture
                fill_container: false
              - type: custom:mushroom-template-card
                primary: Version Information
                secondary: >-
                  Installed v{{ state_attr('update.home_assistant_core_update',
                  'installed_version')}}
                  Latest v{{ state_attr('update.home_assistant_core_update',
                  'latest_version')}}
                icon: mdi:package-variant-closed
                multiline_secondary: true
                fill_container: true
                entity: update.home_assistant_core_update
                tap_action:
                  action: more-info
                icon_color: |-
                  {% if is_state('update.home_assistant_core_update', 'on') %}
                    orange
                  {% else %}
                    green
                  {% endif %}
                badge_color: |-
                  {% if is_state('update.home_assistant_core_update', 'on') %}
                    red
                  {% else %}
                    blue
                  {% endif %}
                badge_icon: |-
                  {% if is_state('update.home_assistant_core_update', 'on') %}
                    mdi:help
                  {% else %}
                    mdi:check-bold
                  {% endif %}
                card_mod:
                  style: |
                    ha-card {
                      pointer-events: none;
                    }
          - type: horizontal-stack
            cards:
              - type: custom:mushroom-update-card
                entity: update.home_assistant_operating_system_update
                name: HA OS
                show_buttons_control: true
                icon_type: entity-picture
              - type: custom:mushroom-template-card
                primary: Version Information
                secondary: >-
                  Installed v{{
                  state_attr('update.home_assistant_operating_system_update',
                  'installed_version')}}
                  Latest v{{
                  state_attr('update.home_assistant_operating_system_update',
                  'latest_version')}}
                icon: mdi:package-variant-closed
                multiline_secondary: true
                fill_container: true
                entity: update.home_assistant_operating_system_update
                tap_action:
                  action: more-info
                icon_color: >-
                  {% if
                  is_state('update.home_assistant_operating_system_update',
                  'on') %}
                    orange
                  {% else %}
                    green
                  {% endif %}
                badge_color: >-
                  {% if
                  is_state('update.home_assistant_operating_system_update',
                  'on') %}
                    red
                  {% else %}
                    blue
                  {% endif %}
                badge_icon: >-
                  {% if
                  is_state('update.home_assistant_operating_system_update',
                  'on') %}
                    mdi:help
                  {% else %}
                    mdi:check-bold
                  {% endif %}
                card_mod:
                  style: |
                    ha-card {
                      pointer-events: none;
                    }
          - type: horizontal-stack
            cards:
              - type: custom:mushroom-update-card
                entity: update.home_assistant_supervisor_update
                name: HA Supervisor
                show_buttons_control: true
                icon_type: entity-picture
              - type: custom:mushroom-template-card
                primary: Version Information
                secondary: >-
                  Installed v{{
                  state_attr('update.home_assistant_supervisor_update',
                  'installed_version')}}
                  Latest v{{
                  state_attr('update.home_assistant_supervisor_update',
                  'latest_version')}}
                icon: mdi:package-variant-closed
                multiline_secondary: true
                fill_container: true
                entity: update.home_assistant_core_update
                tap_action:
                  action: more-info
                icon_color: >-
                  {% if is_state('update.home_assistant_supervisor_update',
                  'on') %}
                    orange
                  {% else %}
                    green
                  {% endif %}
                badge_color: >-
                  {% if is_state('update.home_assistant_supervisor_update',
                  'on') %}
                    red
                  {% else %}
                    blue
                  {% endif %}
                badge_icon: >-
                  {% if is_state('update.home_assistant_supervisor_update',
                  'on') %}
                    mdi:help
                  {% else %}
                    mdi:check-bold
                  {% endif %}
                card_mod:
                  style: |
                    ha-card {
                      pointer-events: none;
                    }
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
                - grid-template-areas: "\"card1 card2 card3\" "
                - grid-template-columns: 1fr 0.69fr 0.05fr
                - grid-template-rows: 0fr 0fr
              card:
                - padding: 5px 0px 5px 10px
                - background: rgba(0,0,0,0)
              custom_fields:
                card1: null
                card2:
                  - align-self: top
                  - height: 100%
            custom_fields:
              card1:
                card:
                  type: custom:mushroom-title-card
                  title: HACS
                  subtitle: >-
                    Installed v{{ state_attr('update.hacs_update',
                    'installed_version') }} - Latest v{{
                    state_attr('update.hacs_update', 'latest_version') }}
                  alignment: start
                  card_mod:
                    style: |
                      .header {
                        padding: 0px !important;
                      }
                      ha-card {
                          margin-right: -15rem;
                       }
              card2:
                card:
                  type: markdown
                  content: >-
                    {% set
                    need_update=integration_entities('hacs')|select('search','update.hacs_update')|select('is_state','of')|list|count|int(2)
                    %} {% if need_update == 0 %} <ha-alert alert-type="success"
                    title="HACS est à jour" > {% else %} <ha-alert
                    alert-type="error" title="1 mise a jour de HASC est
                    disponible" ></ha-alert> {% endif %}
                  card_mod:
                    style: |
                      :host {
                        --ha-card-margin: 0px;
                        --ha-card-border-color: transparent !important;
                        --card-background-color: transparent !important;
                      }
                      ha-markdown.no-header {
                        margin: 0px !important;
                      }
                      ha-card {
                        margin-top: -1.3rem;
                        margin-bottom: -1.3rem;
                        margin-left: -1rem;
                        font-size: 1rem;
                        --mdc-icon-size: 1.3rem;
                       }
          - type: custom:mushroom-chips-card
            chips:
              - type: template
                icon: mdi:web
                icon_color: blue
                content: Release Changelog
                tap_action:
                  action: url
                  url_path: https://github.com/hacs/integration/releases
              - type: template
                entity: update.hacs_update
                content: >-
                  Installed v{{ state_attr('update.hacs_update',
                  'installed_version') }}
                icon_color: green
                icon: mdi:package-variant-closed
                tap_action:
                  action: none
              - type: template
                entity: update.hacs_update
                content: >-
                  Latest v{{ state_attr('update.hacs_update', 'latest_version')
                  }}
                icon_color: orange
                icon: mdi:package-variant-closed
                tap_action:
                  action: none
            card_mod:
              style:
                mushroom-template-chip:nth-child(2):
                  $: |
                    mushroom-chip{
                    pointer-events: none;
                    }
                mushroom-template-chip:nth-child(3):
                  $: |
                    mushroom-chip{
                    pointer-events: none;
                    }
          - type: custom:auto-entities
            card:
              type: vertical-stack
            card_param: cards
            filter:
              include:
                - entity_id: update.hacs_update
                  state: "on"
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
                        - grid-template-areas: "\"i n n cardupload\" \"i s cardurl cardupload\""
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
                          - margin-right: "-2rem"
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
                              entity_id: "[[[return variables.sensor]]]"
              exclude: []
              card_param: cards
```

---

## GRILLE 2 — H.A. UPDATE

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
            - grid-template-areas: "\"card1 card2 card3\""
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
              state: "on"
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
                    - grid-template-areas: "\"i n n cardupload\" \"i s s cardupload\""
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
                          entity_id: "[[[return variables.sensor]]]"
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
            - grid-template-areas: "\"card1 card2 card3\""
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
              state: "on"
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
                    - grid-template-areas: "\"i n n cardupload\" \"i s cardurl cardupload\""
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
                      - margin-right: "-2rem"
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
                          entity_id: "[[[return variables.sensor]]]"
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
            - grid-template-areas: "\"card1 card2 card3\""
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
              state: "on"
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
                    - grid-template-areas: "\"i n n cardupload\" \"i s s cardupload\""
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
                          entity_id: "[[[return variables.sensor]]]"
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
              - type: entity
                entity: sensor.home_assistant_core_cpu_percent
                icon_color: blue
              - type: entity
                entity: sensor.home_assistant_core_memory_percent
                icon_color: orange
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
              - type: entity
                entity: sensor.home_assistant_supervisor_cpu_percent
                icon_color: blue
              - type: entity
                entity: sensor.home_assistant_supervisor_memory_percent
                icon_color: orange
```

---

## 🔗 FICHIERS LIÉS

- [`L4C3_VIGNETTE_MAJ.md`](./L4C3_VIGNETTE_MAJ.md) — vignette button-card + bug `margin-left`
- [`docs/DEPENDANCES_GLOBALES.md`](../DEPENDANCES_GLOBALES.md) — chaîne complète L4C3

---

← Retour : [`L4C3_VIGNETTE_MAJ.md`](./L4C3_VIGNETTE_MAJ.md)


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L4C3_VIGNETTE_MAJ]]*
