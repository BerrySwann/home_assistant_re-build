<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--04--19-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script_Exécutant-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Fichier prod** | `scripts.yaml` (géré via UI HA) |
| 🔗 **Appelé depuis** | `script.j_1_1/j_1_2/j_1_3_*` (sur OFF uniquement) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-04-19 |
| 🏠 **Version HA** | 2026.3 |

---

# 🔒 Script J 2-0 SECU — ARRÊT CLIM PROTÉGÉ

Exécutant commun aux 3 pièces. Gère la **protection thermique** : attend que la clim descende sous 9W avant de couper la prise, avec un timeout de 10 minutes.

---

## 🏗️ ARCHITECTURE

```
script.j_1_x_<piece>_clim_on_off_intelligent  (sur OFF)
    │
    └── script.j_2_0_secu_arret_clim_protege  (mode: parallel, max: 3)
            │
            ├── 1. Activer verrou  input_boolean.clim_<piece>_arret_securise_en_cours → ON
            ├── 2. Thermostat OFF  climate.clim_<piece>_rm4_mini → hvac_mode: off
            ├── 3a. Si power_lock = off (déjà à l'arrêt) → coupure immédiate
            ├── 3b. Si power_lock = on  → attente max 10 min → coupure propre ou erreur
            └── 4. Désactiver verrou → OFF
```

### Pourquoi `mode: parallel, max: 3` ?
- Les 3 pièces peuvent être arrêtées **simultanément** sans se bloquer entre elles.
- `max: 3` = limite stricte à 3 instances (1 par pièce).

---

## 📍 J 2-0 — YAML COMPLET

**Script ID** : `j_2_0_secu_arret_clim_protege`

```yaml
j_2_0_secu_arret_clim_protege:
  alias: J 2-0 SECU - ARRÊT CLIM PROTÉGÉ
  description: '[EXÉCUTANT] Protection thermique et coupure sous 9W.'
  mode: parallel
  max: 3
  fields:
    piece:
      description: 'Pièce (ex: salon, bureau, chambre)'
      example: salon
      required: true
  variables:
    p: '{{ piece | lower }}'
    lock_entity: input_boolean.clim_{{ p }}_arret_securise_en_cours
    clim_entity: climate.clim_{{ p }}_rm4_mini
    switch_entity: switch.clim_{{ p }}_nous
    power_status_sensor: sensor.{{ p }}_power_status
    power_lock_sensor: sensor.{{ p }}_power_lock
    piece_nom: '{% if p == ''salon'' %} du Salon {% elif p == ''bureau'' %} du Bureau
      {% elif p == ''chambre'' %} de la Chambre {% else %} Inconnue {% endif %}'
  sequence:
  - alias: 1. ACTIVATION VERROU
    target:
      entity_id: '{{ lock_entity }}'
    action: input_boolean.turn_on
  - alias: 2. THERMOSTAT SUR OFF
    target:
      entity_id: '{{ clim_entity }}'
    action: climate.set_hvac_mode
    data:
      hvac_mode: 'off'
  - alias: 3. ANALYSE ET ATTENTE CONSOMMATION
    choose:
    - alias: 'CAS : DÉJÀ À L''ARRÊT COMPLET'
      conditions:
      - condition: template
        value_template: '{{ is_state(power_lock_sensor, "off") }}'
      sequence:
      - alias: 'ACTION : COUPURE PRISE IMMÉDIATE'
        target:
          entity_id: '{{ switch_entity }}'
        action: switch.turn_off
      - alias: 'NOTIFICATION : REPOS COMPLET'
        action: notify.mobile_app_eric
        data:
          title: Prise clim {{ p | upper }}
          message: La Clim {{ piece_nom }} est coupée (Repos complet).
    - alias: 'CAS : CLIM EN CYCLE D''ARRÊT (ATTENTE)'
      conditions:
      - condition: template
        value_template: '{{ is_state(power_lock_sensor, "on") }}'
      sequence:
      - alias: 'NOTIFICATION : ATTENTE DESCENTE WATTS'
        action: notify.mobile_app_eric
        data:
          title: ARRÊT CLIM EN COURS
          message: La Clim {{ piece_nom }} est active. Attente de descente sous 9W
            (max 10 min).
      - alias: 'WAIT : DÉTECTION SOUS 9W'
        wait_for_trigger:
        - trigger: template
          value_template: '{{ is_state(power_lock_sensor, "off") }}'
        timeout: 00:10:00
        continue_on_timeout: true
      - alias: 'CHECK FINAL : COUPURE OU ERREUR'
        if:
        - condition: template
          value_template: '{{ is_state(power_lock_sensor, "off") }}'
        then:
        - alias: 'ACTION : COUPURE PRISE PROPRE'
          target:
            entity_id: '{{ switch_entity }}'
          action: switch.turn_off
        - alias: 'NOTIFICATION : ARRÊT RÉUSSI'
          action: notify.mobile_app_eric
          data:
            title: CLIM À L'ARRÊT
            message: La prise de la Clim {{ piece_nom }} a été coupée proprement (<
              9W).
        else:
        - alias: 'NOTIFICATION : ÉCHEC SÉCURITÉ'
          action: notify.mobile_app_eric
          data:
            title: ERREUR ARRÊT CLIM
            message: 'ÉCHEC : La Clim {{ piece_nom }} consomme toujours > 9W après
              10 min. Prise maintenue.'
  - alias: 4. DÉSACTIVATION VERROU
    target:
      entity_id: '{{ lock_entity }}'
    action: input_boolean.turn_off
```

---

## 🔌 ENTITÉS UTILISÉES

| Entité | Type | Rôle |
|--------|------|------|
| `input_boolean.clim_<piece>_arret_securise_en_cours` | Helper | Verrou anti-double exécution |
| `climate.clim_<piece>_rm4_mini` | Climate Broadlink | Mise en mode off du thermostat |
| `switch.clim_<piece>_nous` | Switch NOUS | Coupure alimentation physique |
| `sensor.<piece>_power_lock` | Template | Détecteur seuil 9W (on = > 9W) |

> `sensor.<piece>_power_lock` est défini dans `P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml`

---

## ⚠️ PIÈGES CONNUS

- **Ne jamais appeler J 2-0 directement depuis le dashboard** — toujours passer par J 1-x.
- **`mode: parallel`** est obligatoire : sans ça, l'arrêt d'une pièce bloque les autres.
- **Timeout 10 min** : si la clim consomme toujours > 9W après 10 min, la prise EST MAINTENUE (pas de coupure forcée) — notification `ERREUR ARRÊT CLIM` envoyée.
- **Le verrou** (`input_boolean`) est toujours désactivé en étape 4, même en cas d'échec.

---

<!-- obsidian-wikilinks -->
---
*Liens : [[INDEX_SCRIPTS]]  [[SCRIPTS_CLIM_ON_OFF]]*
