<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--04--17-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Scripts-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Fichier prod** | `scripts.yaml` (géré via UI HA) |
| 🔗 **Appelé depuis** | `custom:button-card` tap_action (dashboard tablette) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-04-17 |
| 🏠 **Version HA** | 2026.3 |

---

# ⚙️ Scripts Clim ON/OFF — J 1-1 / J 1-2 / J 1-3 + J 2-0

---

## 📋 TABLE DES MATIÈRES

1. [Architecture](#architecture)
2. [Problème résolu](#problème-résolu)
3. [J 1-1 SALON](#j-11--salon)
4. [J 1-2 BUREAU](#j-12--bureau)
5. [J 1-3 CHAMBRE](#j-13--chambre)
6. [J 2-0 SECU (commun)](#j-20--secu--arrêt-clim-protégé)
7. [Entités & helpers requis](#entités--helpers-requis)
8. [Dashboard — tap_action](#dashboard--tap_action)

---

## 🏗️ ARCHITECTURE

```
Dashboard tap_action
    │
    ├── script.j_1_1_salon_clim_on_off_intelligent    (J 1-1 SALON   — mode: single)
    ├── script.j_1_2_bureau_clim_on_off_intelligent   (J 1-2 BUREAU  — mode: single)
    └── script.j_1_3_chambre_clim_on_off_intelligent  (J 1-3 CHAMBRE — mode: single)
            │
            └── script.j_2_0_secu_arret_clim_protege  (J 2-0 SECU — mode: parallel, max:3)
                    │
                    ├── input_boolean.clim_<piece>_arret_securise_en_cours  (verrou)
                    ├── climate.clim_<piece>_rm4_mini → hvac_mode: off
                    └── wait sensor.<piece>_power_lock = off  (max 10 min)
                            └── switch.clim_<piece>_nous → OFF
```

### Tableau des IDs

| N° | Alias HA | Script ID (slug) | Pièce |
|----|----------|-----------------|-------|
| J 1-1 | `J 1-1 SALON - CLIM ON/OFF INTELLIGENT` | `j_1_1_salon_clim_on_off_intelligent` | Salon |
| J 1-2 | `J 1-2 BUREAU - CLIM ON/OFF INTELLIGENT` | `j_1_2_bureau_clim_on_off_intelligent` | Bureau |
| J 1-3 | `J 1-3 CHAMBRE - CLIM ON/OFF INTELLIGENT` | `j_1_3_chambre_clim_on_off_intelligent` | Chambre |
| J 2-0 | `J 2-0 SECU - ARRÊT CLIM PROTÉGÉ` | `j_2_0_secu_arret_clim_protege` | Commun |

---

## ⚠️ PROBLÈME RÉSOLU

**Avant (J-1 unique `mode: single`)** : L'appel à J-2 est bloquant dans HA (`action: script.NOM`
attend la fin du script). J-1 restait actif jusqu'à 10 min. Avec `mode: single`, tout tap
sur une autre pièce pendant ce délai était **silencieusement ignoré** — aucune notification,
aucune action.

**Après (3 × J-1 dédiés)** : chaque script a son propre `mode: single` isolé par pièce.
Arrêter salon ne bloque plus bureau ni chambre.

---

## 📍 J 1-1 — SALON

**Script ID** : `j_1_1_salon_clim_on_off_intelligent`

```yaml
j_1_1_salon_clim_on_off_intelligent:
  alias: J 1-1 SALON - CLIM ON/OFF INTELLIGENT
  description: '[ROUTEUR SALON] Anti-tremblote et routage ON/OFF — Salon uniquement.'
  mode: single
  variables:
    p: salon
    switch_entity: switch.clim_salon_nous
    lock_entity: input_boolean.clim_salon_arret_securise_en_cours
  sequence:
  - alias: 1. SÉCURITÉ ANTI-TREMBLOTE
    if:
    - condition: template
      value_template: '{{ is_state(lock_entity, ''on'') }}'
    then:
    - alias: 'NOTIFICATION : VERROU ACTIF'
      action: notify.mobile_app_eric
      data:
        title: OULA DOUCEMENT !
        message: Une procédure d'arrêt est déjà en cours sur SALON.
    - stop: Arrêt sécurisé déjà en cours - Double clic ignoré
  - alias: 2. DÉCISION ON/OFF
    if:
    - condition: template
      value_template: '{{ is_state(switch_entity, ''off'') }}'
    then:
    - alias: 'ACTION : ALLUMER LA PRISE'
      action: switch.turn_on
      target:
        entity_id: '{{ switch_entity }}'
    else:
    - alias: 'ACTION : APPELER J-2 (SÉCURITÉ)'
      action: script.j_2_secu_arret_clim_protege
      data:
        piece: '{{ p }}'
```

---

## 📍 J 1-2 — BUREAU

**Script ID** : `j_1_2_bureau_clim_on_off_intelligent`

```yaml
j_1_2_bureau_clim_on_off_intelligent:
  alias: J 1-2 BUREAU - CLIM ON/OFF INTELLIGENT
  description: '[ROUTEUR BUREAU] Anti-tremblote et routage ON/OFF — Bureau uniquement.'
  mode: single
  variables:
    p: bureau
    switch_entity: switch.clim_bureau_nous
    lock_entity: input_boolean.clim_bureau_arret_securise_en_cours
  sequence:
  - alias: 1. SÉCURITÉ ANTI-TREMBLOTE
    if:
    - condition: template
      value_template: '{{ is_state(lock_entity, ''on'') }}'
    then:
    - alias: 'NOTIFICATION : VERROU ACTIF'
      action: notify.mobile_app_eric
      data:
        title: OULA DOUCEMENT !
        message: Une procédure d'arrêt est déjà en cours sur BUREAU.
    - stop: Arrêt sécurisé déjà en cours - Double clic ignoré
  - alias: 2. DÉCISION ON/OFF
    if:
    - condition: template
      value_template: '{{ is_state(switch_entity, ''off'') }}'
    then:
    - alias: 'ACTION : ALLUMER LA PRISE'
      action: switch.turn_on
      target:
        entity_id: '{{ switch_entity }}'
    else:
    - alias: 'ACTION : APPELER J-2 (SÉCURITÉ)'
      action: script.j_2_secu_arret_clim_protege
      data:
        piece: '{{ p }}'
```

---

## 📍 J 1-3 — CHAMBRE

**Script ID** : `j_1_3_chambre_clim_on_off_intelligent`

```yaml
j_1_3_chambre_clim_on_off_intelligent:
  alias: J 1-3 CHAMBRE - CLIM ON/OFF INTELLIGENT
  description: '[ROUTEUR CHAMBRE] Anti-tremblote et routage ON/OFF — Chambre uniquement.'
  mode: single
  variables:
    p: chambre
    switch_entity: switch.clim_chambre_nous
    lock_entity: input_boolean.clim_chambre_arret_securise_en_cours
  sequence:
  - alias: 1. SÉCURITÉ ANTI-TREMBLOTE
    if:
    - condition: template
      value_template: '{{ is_state(lock_entity, ''on'') }}'
    then:
    - alias: 'NOTIFICATION : VERROU ACTIF'
      action: notify.mobile_app_eric
      data:
        title: OULA DOUCEMENT !
        message: Une procédure d'arrêt est déjà en cours sur CHAMBRE.
    - stop: Arrêt sécurisé déjà en cours - Double clic ignoré
  - alias: 2. DÉCISION ON/OFF
    if:
    - condition: template
      value_template: '{{ is_state(switch_entity, ''off'') }}'
    then:
    - alias: 'ACTION : ALLUMER LA PRISE'
      action: switch.turn_on
      target:
        entity_id: '{{ switch_entity }}'
    else:
    - alias: 'ACTION : APPELER J-2 (SÉCURITÉ)'
      action: script.j_2_secu_arret_clim_protege
      data:
        piece: '{{ p }}'
```

---

## 📍 J 2-0 — SECU — ARRÊT CLIM PROTÉGÉ

**Script ID** : `j_2_secu_arret_clim_protege` — commun aux 3 pièces, aucune modification.

```yaml
j_2_secu_arret_clim_protege:
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

## 🔌 ENTITÉS & HELPERS REQUIS

| Entité | Type | Pièce(s) |
|--------|------|----------|
| `switch.clim_salon_nous` | Switch NOUS | Salon |
| `switch.clim_bureau_nous` | Switch NOUS | Bureau |
| `switch.clim_chambre_nous` | Switch NOUS | Chambre |
| `climate.clim_salon_rm4_mini` | Climate Broadlink | Salon |
| `climate.clim_bureau_rm4_mini` | Climate Broadlink | Bureau |
| `climate.clim_chambre_rm4_mini` | Climate Broadlink | Chambre |
| `input_boolean.clim_salon_arret_securise_en_cours` | Helper | Salon |
| `input_boolean.clim_bureau_arret_securise_en_cours` | Helper | Bureau |
| `input_boolean.clim_chambre_arret_securise_en_cours` | Helper | Chambre |
| `sensor.salon_power_lock` | Template | Salon |
| `sensor.bureau_power_lock` | Template | Bureau |
| `sensor.chambre_power_lock` | Template | Chambre |

> `sensor.<piece>_power_lock` : template renvoyant `on` si la clim consomme > 9W, `off` sinon.

---

## 🖥️ DASHBOARD — TAP_ACTION

```yaml
# SALON
entity: switch.clim_salon_nous
tap_action:
  action: call-service
  service: script.j_1_1_salon_clim_on_off_intelligent

# BUREAU
entity: switch.clim_bureau_nous
tap_action:
  action: call-service
  service: script.j_1_2_bureau_clim_on_off_intelligent

# CHAMBRE
entity: switch.clim_chambre_nous
tap_action:
  action: call-service
  service: script.j_1_3_chambre_clim_on_off_intelligent
```

> Plus de `service_data: piece:` — chaque script hardcode sa propre pièce.

---

## 📝 DÉPENDANCES CRITIQUES

| Script ID | Alias | Statut |
|-----------|-------|--------|
| `j_1_routeur_clim_on_off_intelligent` | J 1-1 SALON | ✅ Actif |
| `j_1_routeur_clim_on_off_intelligent_dupliquer_2` | J 1-2 BUREAU | ✅ Actif |
| `j_1_routeur_clim_on_off_intelligent_dupliquer` | J 1-3 CHAMBRE | ✅ Actif |
| `j_2_secu_arret_clim_protege` | J 2-0 SECU | ✅ Actif |
| `input_boolean.clim_*_arret_securise_en_cours` × 3 | Helpers | ✅ Essentiel |
| `sensor.*_power_lock` × 3 | Templates | ✅ Essentiel |

---

← Retour : `docs DashBoard/` | Dossier : `docs Scripts/`
