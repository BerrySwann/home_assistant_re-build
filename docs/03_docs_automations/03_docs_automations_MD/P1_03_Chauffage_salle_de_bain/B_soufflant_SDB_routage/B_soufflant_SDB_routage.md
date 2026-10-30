# (B) SDB SOUFFLANT - ROUTAGE (interrupteur vers séquences)

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_03_Chauffage_Salle_de_Bain/b_soufflant_sdb_routage/b_soufflant_sdb_routage.yaml`
> **ID HA :** `1790623332289`
> **Mode HA :** `single`
> **MàJ :** 2026-10-10 (fiche écrite à partir du YAML, identique à H:\automations.yaml)

---

## Description

Entrée unique du soufflant de la salle de bain : l'interrupteur virtuel (bouton du tableau de bord ou bouton Rodret via A) déclenche le démarrage ou l'arrêt. Le verrou de deux minutes est tenu par les scripts. Aucun automatisme de température.

---

## Déclencheurs

| ID | Type | Détail |
|:---|:---|:---|
| `marche` | `state` | `switch.inter_soufflant_salle_de_bain` passe à `on` |
| `arret` | `state` | `switch.inter_soufflant_salle_de_bain` passe à `off` |

---

## Actions

| Déclencheur | Action |
|:---|:---|
| `marche` | `script.turn_on` sur `script.sdb_soufflant_demarrer` |
| `arret` | `script.turn_on` sur `script.sdb_soufflant_arreter` |

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `switch.inter_soufflant_salle_de_bain` | Interrupteur virtuel |
| `script.sdb_soufflant_demarrer` | Séquence de démarrage |
| `script.sdb_soufflant_arreter` | Séquence d'arrêt |

Pas de condition, pas de notification.
