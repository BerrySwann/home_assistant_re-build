# SDB - Soufflant - Routage (interrupteur vers séquences)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

**Catégorie :** P1_SDB
**Alias HA :** `SDB - SOUFFLANT - ROUTAGE (interrupteur vers sequences)` (dans `automations.yaml` de la prod : `B - SDB - SOUFFLANT - ROUTAGE (interrupteur vers sequences)`, ligne 2582 relevée le 2026-10-28)
**Mode :** `single`. **Déployée en prod le 2026-09-28** (d'après l'en-tête du YAML), rechargée sans redémarrer Home Assistant.

## Description

Entrée unique du soufflant de la salle de bain : l'interrupteur virtuel `switch.inter_soufflant_salle_de_bain` (bouton du tableau de bord ou bouton Rodret) déclenche le démarrage ou l'arrêt. Le verrou anti-rebond est tenu par les scripts, pas par cette automation. Aucun automatisme de température dans cette automation.

## Déclencheurs

| Alias du déclencheur | Entité | État | id |
|:---|:---|:---|:---|
| Interrupteur SDB sur ON | `switch.inter_soufflant_salle_de_bain` | `on` | `marche` |
| Interrupteur SDB sur OFF | `switch.inter_soufflant_salle_de_bain` | `off` | `arret` |

## Actions

- `marche` : `script.turn_on` sur `script.sdb_soufflant_demarrer`
- `arret` : `script.turn_on` sur `script.sdb_soufflant_arreter`

Aucune condition.

## Entités principales

- `switch.inter_soufflant_salle_de_bain`
- `script.sdb_soufflant_demarrer` et `script.sdb_soufflant_arreter` (présents dans `scripts.yaml` de la prod, lignes 527 et 612 relevées le 2026-10-28)

## Limites connues

- Écart dans le YAML : le commentaire d'en-tête parle d'un verrou de trente secondes, la description de l'automation d'un verrou de deux minutes. À vérifier dans les scripts avant de corriger l'un des deux textes.

## Historique

- 2026-09-28 : déployée en prod (version finale 2026/2027 du soufflant de la salle de bain).
- 2026-10-28 : fiche créée d'après le YAML local, rangée avec son YAML dans `P1_SDB`. Le bouton Rodret qui commande l'interrupteur est décrit dans `i_soufflant_SDB_bouton_rodret.md`.

## Fichier source

`docs/03_docs_automations/03_docs_automations_YAML/P1_SDB/h_soufflant_SDB_routage.yaml`

---
*Doc créée le 2026-10-28*