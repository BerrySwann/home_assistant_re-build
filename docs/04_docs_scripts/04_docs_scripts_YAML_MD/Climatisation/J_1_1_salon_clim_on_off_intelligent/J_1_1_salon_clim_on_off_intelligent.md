# J 1-1 SALON - Clim ON/OFF intelligent (Salon)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--01-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Scripts-4fc3f7?style=flat-square)](.)

</div>

> **Doublon (decide par Eric le 2026-11-01) :** fiches qui decrivent les routeurs clim : `04_docs_scripts_YAML_MD/Climatisation/Scripts_clim_on_off/Scripts_clim_on_off.md` (les trois ensemble), et une fiche par script : J_1_1 (salon), J_1_2 (bureau), J_1_3 (chambre).
> Toute modification se fait dans toutes les fiches listees.

| Champ | Valeur |
|:------|:-------|
| Source | `docs/04_docs_scripts/04_docs_scripts_YAML/J_1_1_salon_clim_on_off_intelligent/J_1_1_salon_clim_on_off_intelligent.yaml` |
| Entité HA | `script.j_1_1_salon_clim_on_off_intelligent` |
| Fichier prod | `scripts.yaml` (géré via l'UI HA) |
| Appelé depuis | `custom:button-card` tap_action du dashboard (tablette) |
| Rôle | routeur ON/OFF de la clim Salon : anti-tremblote, allume la prise ou appelle J 2-0 |

---

## 📝 Description

Routeur dédié à la pièce Salon (`mode: single` isolé par pièce, pour qu'un arrêt en cours sur une pièce ne bloque pas les deux autres). Si le verrou `input_boolean.clim_salon_arret_securise_en_cours` est à `on`, une notification est envoyée et le script s'arrête. Sinon : prise `off` -> allumée ; prise `on` -> appel du script de sécurité J 2-0 (voir la fiche `J_2_0_secu_arret_clim_protege.md`).

## 🔌 Entités et helpers

| Entité | Type |
|:-------|:-----|
| `switch.clim_salon_nous` | Prise NOUS de la clim |
| `input_boolean.clim_salon_arret_securise_en_cours` | Verrou anti-tremblote |

## 🖥️ Dashboard

`tap_action: call-service` avec `service: script.j_1_1_salon_clim_on_off_intelligent` ; la pièce est écrite en dur dans le script.

## 💻 Source (copie du fichier du dépôt local, relevée le 2026-11-01)

```yaml
# ╭──────────────────────────────────────────────────────────────────────────────╮
# │ J 1-1 SALON - CLIM ON/OFF INTELLIGENT
# ╰──────────────────────────────────────────────────────────────────────────────╯
#
# ## DESCRIPTION :
# [ROUTEUR SALON] Anti-tremblote et routage ON/OFF — Salon uniquement.
#
# ## ETAT :
# - Extrait le 2026-10-12 de la prod (scripts.yaml, fichier du 2026-10-07 20:20:29).
# - Aucune copie locale n'existait (verifie : local, archives, GitHub). Contenu repris tel quel, non modifie.


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
      action: script.j_2_0_secu_arret_clim_protege
      data:
        piece: '{{ p }}'
```

---

*Fiche créée le 2026-11-01 à la demande d'Eric (une fiche par script, même si elle fait doublon).*