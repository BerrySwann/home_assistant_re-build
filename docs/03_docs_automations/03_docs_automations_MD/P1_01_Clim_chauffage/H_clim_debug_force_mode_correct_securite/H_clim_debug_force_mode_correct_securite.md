# (H) WATCHDOG CLIM - FORCE MODE CORRECT & SÉCURITÉ

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-4fc3f7?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/h_clim_debug_force_mode_correct_securite/h_clim_debug_force_mode_correct_securite.yaml`
> **ID HA :** `1774452171317` (en prod dans automations.yaml)
> **Mode HA :** `single`
> **MàJ :** 2026-10-11 (fiche complétée d'après le YAML, identique à H:\automations.yaml)

---

## Description

Watchdog en 2 couches, déclenché par tout changement d'état d'une clim ou du mode saison :
1. **Forcer OFF** : une clim n'est pas `off` alors que sa prise (`switch.clim_*_nous`) est coupée, ou qu'un arrêt sécurisé est en cours (`input_boolean.clim_*_arret_securise_en_cours` à `on`).
2. **Forcer le mode saison** : une clim est allumée dans un mode différent de `sensor.mode_ete_hiver` (exemple : `cool` au lieu de `heat`), à condition que sa prise soit `on` et qu'aucun arrêt sécurisé ne soit en cours.

---

## Déclencheurs

| Type | Entités | Remarque |
|:---|:---|:---|
| `state` | `climate.clim_salon_rm4_mini`, `climate.clim_bureau_rm4_mini`, `climate.clim_chambre_rm4_mini` | `to:` vide : tout changement d'état |
| `state` | `sensor.mode_ete_hiver` | `to:` vide : tout changement d'état |

---

## Conditions

Aucune (`conditions: []`).

---

## Actions

1. `delay: 00:00:02`
2. Variables :
   - `mode_saison` = état de `sensor.mode_ete_hiver`
   - `force_off_list` : clims dont l'état n'est pas `off` ET (prise `off` OU arrêt sécurisé `on`), pour salon, bureau, chambre
   - `force_mode_list` : clims dont l'état n'est pas dans `off`, `unavailable`, `unknown`, ni égal au mode saison, ET prise `on` ET arrêt sécurisé `off`, pour salon, bureau, chambre
3. Si `force_off_list` n'est pas vide : notification puis `climate.set_hvac_mode` à `off` sur la liste.
4. Si `force_mode_list` n'est pas vide : notification puis `climate.set_hvac_mode` au mode saison sur la liste.

---

## Dépendances

### Entités lues

| Entité | Rôle |
|:---|:---|
| `sensor.mode_ete_hiver` | Mode saison de référence |
| `climate.clim_salon_rm4_mini`, `climate.clim_bureau_rm4_mini`, `climate.clim_chambre_rm4_mini` | État courant des 3 clims |
| `switch.clim_salon_nous`, `switch.clim_bureau_nous`, `switch.clim_chambre_nous` | Prise active ? |
| `input_boolean.clim_salon_arret_securise_en_cours`, `input_boolean.clim_bureau_arret_securise_en_cours`, `input_boolean.clim_chambre_arret_securise_en_cours` | Arrêt sécurisé en cours ? |

### Entités pilotées

| Entité | Action |
|:---|:---|
| Liste dynamique de `climate.clim_*_rm4_mini` | `set_hvac_mode: off` ou mode saison |

### Notifications (`notify.mobile_app_eric`)

| Alias | Titre | Message | Condition |
|:---|:---|:---|:---|
| NOTIF : INTERDICTION DÉMARRAGE | SÉCURITÉ CLIM | "Tentative de démarrage interdite (Prise coupée ou Arrêt en cours). Retour forcé à OFF pour :" + liste des clims | `force_off_list` non vide |
| NOTIF : CORRECTION MODE | CORRECTION MODE | "Mauvais mode détecté. Correction vers <MODE SAISON> pour :" + liste des clims | `force_mode_list` non vide |

---

## Notes

- Fiche mise à jour : l'ancienne version s'arrêtait au milieu du tableau des notifications et ne citait ni l'ID HA ni les conditions des deux listes.
- Fichier YAML local : l'automation est écrite comme un élément de liste (`- id: ...`).