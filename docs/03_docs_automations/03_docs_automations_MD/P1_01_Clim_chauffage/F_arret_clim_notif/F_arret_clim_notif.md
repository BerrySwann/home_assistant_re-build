# (F) ARRÊT CLIM - NOTIFICATION MANUELLE

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/f_clim_automatisation_arret_clim_notification/f_clim_automatisation_arret_clim_notification.yaml`
> **ID HA :** `1775243733692` (en prod dans automations.yaml)
> **Mode HA :** `queued`
> **MàJ :** 2026-10-11 (fiche complétée d'après le YAML, identique à H:\automations.yaml)

---

## Description

Notifie quand une clim passe à `off` (télécommande ou interface), mais seulement si les 3 prises clim sont actives et si les 4 fenêtres sont fermées, pour éviter les faux positifs lors des coupures automatiques (arrêt sur fenêtre ouverte, coupure de prise).

---

## Déclencheurs

| Type | Entités | État cible |
|:---|:---|:---|
| `state` | `climate.clim_salon_rm4_mini`, `climate.clim_bureau_rm4_mini`, `climate.clim_chambre_rm4_mini` | `off` |

---

## Conditions (toutes à la fois)

- `switch.clim_salon_nous`, `switch.clim_bureau_nous`, `switch.clim_chambre_nous` : `on`
- `binary_sensor.contact_fenetre_salon_sonoff_contact`, `binary_sensor.contact_fenetre_cuisine_sonoff_contact`, `binary_sensor.contact_fenetre_bureau_sonoff_contact`, `binary_sensor.contact_fenetre_chambre_sonoff_contact` : `off` (fermées)

---

## Actions

Notification `notify.mobile_app_eric`, titre "ARRÊT CLIM", message "La clim. du Salon / du Bureau / de la Chambre a été coupée." (pièce déduite de `trigger.entity_id`, "inconnue" si l'entité n'est pas dans la liste).

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `climate.clim_salon_rm4_mini`, `climate.clim_bureau_rm4_mini`, `climate.clim_chambre_rm4_mini` | Déclencheurs |
| `switch.clim_salon_nous`, `switch.clim_bureau_nous`, `switch.clim_chambre_nous` | Conditions (prises) |
| 4 capteurs `binary_sensor.contact_fenetre_*_sonoff_contact` (salon, cuisine, bureau, chambre) | Conditions (fenêtres) |
| `notify.mobile_app_eric` | Notification |

---

## Notes

- Fiche mise à jour : l'ancienne version s'arrêtait au milieu du tableau des notifications et ne nommait ni l'ID HA ni les 4 capteurs de fenêtre.
- Fichier YAML local : l'automation est écrite comme un élément de liste (`- id: ...`).