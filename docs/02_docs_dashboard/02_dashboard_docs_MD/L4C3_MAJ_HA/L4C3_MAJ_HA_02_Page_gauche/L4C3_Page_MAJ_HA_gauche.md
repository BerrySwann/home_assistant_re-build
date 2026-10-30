<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page%20gauche-ff9800?style=flat-square)](.)

</div>

> **Ancienne mention "DOC VERROUILLÉE - Modifs interdites" (PAGE_MAJ.md du 2026-03-18) retirée** : le YAML a été ré-exporté depuis l'éditeur HA le 2026-10-11 à la demande d'Eric et ce MD a été réécrit en conséquence.
>
> ⚠️ **2 bugs esthétiques connus (repris de l'ancien MD, non retestés) :**
> 1. Icône HA dans la vignette - positionnement à revoir (alignement vertical résiduel)
> 2. Mise en page des grilles à affiner sur petit écran (espacement entre les deux grilles)

| Champ | Valeur |
|:------|:-------|
| 📁 **Path dashboard** | `/dashboard-tablette/maj` |
| 🔗 **Accès depuis** | Vignette L4C3 (clic) |
| 🏗️ **Layout** | `type: grid` - 2 cartes de niveau 1 (heading + vertical-stack) |
| 📄 **Fichier YAML** | `L4C3_MAJ_HA/02_page_gauche/page_L4C3_maj_ha_gauche.yaml` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 📅 **Modifié le** | 2026-10-11 |

---

# 🔄 PAGE MAJ - GAUCHE : H.A. SERVER

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Contenu de la page](#contenu-de-la-page)
3. [Entités utilisées](#entités-utilisées)
4. [Code YAML](#code-yaml)
5. [Points à vérifier](#points-à-vérifier)

---

## 🎯 VUE D'ENSEMBLE

Colonne de gauche de la page `/dashboard-tablette/maj`. Elle montre les versions et l'état de mise à jour du **serveur Home Assistant** (Core, OS, Supervisor) puis de **HACS**. Titre de la grille : `H.A. SERVER` (heading, icône `mdi:home-assistant`, tap = retour `/dashboard-tablette/0`).

La colonne de droite (add-ons, HACS, Zigbee2MQTT, redémarrage) est documentée dans [`PAGE_MAJ_DROITE.md`](../03_page_droite/PAGE_MAJ_DROITE.md).

```
┌──────────────────────────────────────────────────────────────┐
│ H.A. SERVER                                                  │
│                                                              │
│ ■ Titre "Home Assistant Server"                              │
│   Core vX - OS vX - Supervisor vX  + alerte "N MàJ sur 3"    │
│                                                              │
│ ■ HA Core        update-card + "Version Information"         │
│ ■ HA OS          update-card + "Version Information"         │
│ ■ HA Supervisor  update-card + "Version Information"         │
│                                                              │
│ ■ HACS           titre + alerte "HACS est à jour"            │
│                  chips (changelog, installée, dernière)      │
│                  auto-entities : update.hacs_update si "on"  │
└──────────────────────────────────────────────────────────────┘
```

---

## Contenu de la page

| Bloc | Carte | Rôle |
|:--|:--|:--|
| Titre serveur | `custom:button-card` + `mushroom-title-card` + `markdown` | Versions installées (Core, OS, Supervisor) et alerte du nombre de MàJ sur les entités `update.home*` de l'intégration `hassio` |
| HA Core | `mushroom-update-card` + `mushroom-template-card` | Bouton de mise à jour et texte "Installed / Latest" (entité `update.home_assistant_core_update`) |
| HA OS | idem | Entité `update.home_assistant_operating_system_update` |
| HA Supervisor | idem | Entité `update.home_assistant_supervisor_update` |
| HACS | `button-card` + `mushroom-chips-card` + `auto-entities` | Versions HACS, lien vers les releases GitHub, ligne de mise à jour si `update.hacs_update` est à `on` |

---

## Entités utilisées

| Entité | Source | Usage |
|:--|:--|:--|
| `update.home_assistant_core_update` | HA natif | carte Core |
| `update.home_assistant_operating_system_update` | HA natif | carte OS |
| `update.home_assistant_supervisor_update` | HA natif | carte Supervisor |
| `update.hacs_update` | HACS | bloc HACS |
| `update.home*` (3 entités de l'intégration `hassio`) | HA natif | compteur "N MàJ sur 3" (via `integration_entities('hassio')`) |

Valeurs relevées dans HA le 2026-10-11 : `update.hacs_update` est à `off` (à jour) ; aucune des 3 entités `hassio` n'est à `on` (le compteur de la page donne 0 MàJ sur 3).

---

## Code YAML

> Copie du fichier `page_L4C3_maj_ha_gauche.yaml` (le fichier YAML fait foi).

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
            - grid-template-areas: '"card1 card2 card3" '
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
                - grid-template-areas: '"card1 card2 card3" '
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
                  state: 'on'
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
              exclude: []
              card_param: cards
```

---

## Points à vérifier

Constatés dans le YAML tel qu'exporté le 2026-10-11, **non corrigés** (le fichier reste identique à l'export d'Eric) :

- **Carte Supervisor** : la carte `mushroom-template-card` "Version Information" du Supervisor a pour `entity` `update.home_assistant_core_update` (au lieu de `update.home_assistant_supervisor_update`). Le texte affiché utilise bien les attributs du Supervisor, mais un clic ouvre la fiche du Core. Les cartes Core et OS pointent la bonne entité. (La carte a `tap_action: more-info`, mais le `card_mod` met `pointer-events: none`, donc le clic est probablement désactivé : non testé.)
- **Test HACS** : le gabarit utilise `select('is_state','of')`. L'état `of` n'existe pas, le résultat est toujours 0 et la carte affiche toujours "HACS est à jour". Test en direct du 2026-10-11 : `'of'` donne 0, `'off'` donne 1 (affichage faux), `'on'` donne 0. Décision d'Eric le 2026-10-11 : laissé tel quel, "on verra à l'usage".
- **Faute de frappe** dans le message d'erreur HACS : "HASC" au lieu de "HACS".
- **Écart de comptage avec la vignette** : la vignette L4C3 affiche `sensor.available_updates` (toutes les entités `update.*` à `on`, 126 entités au total), alors que cette page ne compte que les 3 entités de `hassio`. Les deux valent 0 aujourd'hui.

---

## 🔗 FICHIERS LIÉS

- [`PAGE_MAJ_DROITE.md`](../03_page_droite/PAGE_MAJ_DROITE.md) - page droite (H.A. UPDATE)
- [`L4C3_Vignette_MAJ_HA.md`](../01_vignette/L4C3_Vignette_MAJ_HA.md) - vignette
- [`DEPENDANCES_GLOBALES_CLAUDE_memoire.md`](../../../../00_IA/) - chaîne complète L4C3

---

← Retour : [`L4C3_Vignette_MAJ_HA.md`](../01_vignette/L4C3_Vignette_MAJ_HA.md)


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L4C3_Vignette_MAJ_HA]]  [[PAGE_MAJ_DROITE]]*
