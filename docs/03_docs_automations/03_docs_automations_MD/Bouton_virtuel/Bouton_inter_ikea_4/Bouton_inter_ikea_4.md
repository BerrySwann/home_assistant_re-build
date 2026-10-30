# [P3-SALON] BOUTON IKEA INTER SALON (4 TOUCHES) - ON/OFF

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Bouton_Virtuel/p3_salon_bouton_ikea_inter_salon/p3_salon_bouton_ikea_inter_salon.yaml`
> **ID HA :** `1774183767864`
> **Mode HA :** `restart`
> **MàJ :** 2026-09-10

---

## 📝 Description

Pilotage direct de `light.salon` (le groupe des 4 lampes du salon) via le bouton
IKEA 4 touches. Un appui « on » allume le groupe, un appui « off » l'éteint.

Pas de helper intermédiaire : l'automation attaque directement l'entité `light.salon`
(l'ancien montage passait par `input_boolean.inter_lumiere_salon`, il n'existe plus).

---

## ⚡ Déclencheurs

| ID | Type | Topic MQTT | Payload |
|:---|:---|:---|:---|
| `bouton_on` | `mqtt` | `zigbee2mqtt2/Inter Salon (4) (IKEA)/action` | `on` |
| `bouton_off` | `mqtt` | `zigbee2mqtt2/Inter Salon (4) (IKEA)/action` | `off` |

---

## ⚙️ Actions - Choose

| Cas | Résultat |
|:---|:---|
| BOUTON ON PRESSÉ | `light.turn_on → light.salon` |
| BOUTON OFF PRESSÉ | `light.turn_off → light.salon` |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt2/Inter Salon (4) (IKEA)/action` | Bouton physique (4 touches) |
| `light.salon` | Groupe des 4 lampes du salon |

---

## ⚠️ Notes techniques

- Topic `zigbee2mqtt2` (LXC 200), pas `zigbee2mqtt`.
- Le bouton SOMRIG (2 touches) fait exactement la même chose en parallèle : cf. `BOUTON_INTER_SOMRIG.md`.
- `mode: restart` : un nouvel appui annule l'exécution en cours.

---
*MàJ 2026-09-10 — fiche réalignée sur l'automation live (cible `light.salon`, topic `zigbee2mqtt2`, plus de helper).*
