# (A) SDB SOUFFLANT - BOUTON IKEA RODRET (MQTT vers interrupteur)

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

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_03_Chauffage_Salle_de_Bain/a_soufflant_sdb_bouton_rodret/a_soufflant_sdb_bouton_rodret.yaml`
> **ID HA :** `1790623332290`
> **Mode HA :** `single`
> **MàJ :** 2026-10-10 (fiche écrite à partir du YAML, identique à H:\automations.yaml)

---

## Description

Le bouton IKEA Rodret de la salle de bain pilote l'interrupteur virtuel du soufflant. C'est l'interrupteur qui déclenche ensuite les séquences (voir B).

---

## Déclencheurs

| ID | Type | Détail |
|:---|:---|:---|
| `rodret_on` | `mqtt` | topic `zigbee2mqtt2/Inter Soufflant Salle de Bain (IKEA RODRET)/action`, payload `on` (appui I) |
| `rodret_off` | `mqtt` | même topic, payload `off` (appui O) |

---

## Actions

| Déclencheur | Action |
|:---|:---|
| `rodret_on` | `switch.turn_on` sur `switch.inter_soufflant_salle_de_bain` |
| `rodret_off` | `switch.turn_off` sur `switch.inter_soufflant_salle_de_bain` |

---

## Dépendances

| Entité / topic | Rôle |
|:---|:---|
| `zigbee2mqtt2/Inter Soufflant Salle de Bain (IKEA RODRET)/action` | Appuis du bouton |
| `switch.inter_soufflant_salle_de_bain` | Interrupteur virtuel, entrée unique du soufflant |

Pas de notification, pas de condition.

---

## Chaîne

Bouton Rodret (A) -> interrupteur virtuel -> routage (B) -> scripts `sdb_soufflant_demarrer` / `sdb_soufflant_arreter`.
