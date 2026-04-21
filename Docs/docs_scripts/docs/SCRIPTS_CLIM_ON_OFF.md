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

# ⚙️ Scripts Clim ON/OFF — Routeurs J 1-1 / J 1-2 / J 1-3

> Script exécutant (protection thermique) → [[SCRIPT_J2_0_SECU_ARRET_CLIM]]

---

## 📋 TABLE DES MATIÈRES

1. [Architecture](#architecture)
2. [Problème résolu](#problème-résolu)
3. [J 1-1 SALON](#j-11--salon)
4. [J 1-2 BUREAU](#j-12--bureau)
5. [J 1-3 CHAMBRE](#j-13--chambre)
6. [Entités & helpers requis](#entités--helpers-requis)
7. [Dashboard — tap_action](#dashboard--tap_action)

---

## 🏗️ ARCHITECTURE

```
Dashboard tap_action
    │
    ├── script.j_1_1_salon_clim_on_off_intelligent    (J 1-1 SALON   — mode: single)
    ├── script.j_1_2_bureau_clim_on_off_intelligent   (J 1-2 BUREAU  — mode: single)
    └── script.j_1_3_chambre_clim_on_off_intelligent  (J 1-3 CHAMBRE — mode: single)
            │  ON  → switch.clim_<piece>_nous → ON
            └── OFF → script.j_2_0_secu_arret_clim_protege  ← voir [[SCRIPT_J2_0_SECU_ARRET_CLIM]]
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

## 🔌 ENTITÉS & HELPERS REQUIS (J 1-x)

| Entité | Type | Pièce(s) |
|--------|------|----------|
| `switch.clim_salon_nous` | Switch NOUS | Salon |
| `switch.clim_bureau_nous` | Switch NOUS | Bureau |
| `switch.clim_chambre_nous` | Switch NOUS | Chambre |
| `input_boolean.clim_salon_arret_securise_en_cours` | Helper (verrou anti-tremblote) | Salon |
| `input_boolean.clim_bureau_arret_securise_en_cours` | Helper (verrou anti-tremblote) | Bureau |
| `input_boolean.clim_chambre_arret_securise_en_cours` | Helper (verrou anti-tremblote) | Chambre |

> Entités utilisées par J 2-0 (climate, power_lock) → [[SCRIPT_J2_0_SECU_ARRET_CLIM]]

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
| `j_1_1_salon_clim_on_off_intelligent` | J 1-1 SALON | ✅ Actif |
| `j_1_2_bureau_clim_on_off_intelligent` | J 1-2 BUREAU | ✅ Actif |
| `j_1_3_chambre_clim_on_off_intelligent` | J 1-3 CHAMBRE | ✅ Actif |
| `j_2_0_secu_arret_clim_protege` | J 2-0 SECU | → [[SCRIPT_J2_0_SECU_ARRET_CLIM]] |
| `input_boolean.clim_*_arret_securise_en_cours` × 3 | Helpers | ✅ Essentiel |

---

<!-- obsidian-wikilinks -->
---
*Liens : [[INDEX_SCRIPTS]]  [[SCRIPT_J2_0_SECU_ARRET_CLIM]]*
