# (P) TRACK_CLIM - JOURNAL DES CONSIGNES

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--23-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-4fc3f7?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_01_Clim_chauffage/P_Track_Clim_journal_des_consignes/P_Track_Clim_journal_des_consignes.yaml`
> **ID HA :** `1795272726443` (entite `automation.m_clim_track_clim_journal_des_consignes`)
> **Mode HA :** `queued` (max 5)

---

## Description

Journal des consignes de la clim. Ecrit dans `notifs/Track_Clim.txt` (integration File `notify.track_clim`), par piece (salon, bureau, chambre) : température réelle, groupe, CNC (consigne non corrigée, sans anti-dérive), CT (correction), CAD (consigne anti-dérive, `input_number` jour ou nuit), CRE (consigne réelle envoyée à la clim).

L'automation a été créée directement dans HA (21 et 22 novembre 2026). Cet export local a été fait le 2026-11-23 par l'histo-final, en reprenant la prod telle quelle (le local s'aligne sur la prod).

---

## Déclencheurs

| Type | Détail |
|:---|:---|
| `time_pattern` | toutes les 15 minutes (`quinze_minutes`) |
| `state` | `sensor.groupe` (`changement_groupe`) |

## Conditions

- `sensor.groupe` différent de `unknown` et `unavailable`

## Actions

1. Entre 21h00 et 07h30 : message de nuit (CNC = consigne nuit) envoyé à `notify.track_clim`.
2. Sinon : message de jour (CNC = température corrigée) envoyé à `notify.track_clim`.

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `sensor.groupe` | groupe courant (déclencheur et condition) |
| `sensor.correction_temperature_<pièce>` | CT |
| `sensor.temperature_eco_hiver_corrige` | CNC en groupe_1 |
| `sensor.temperature_consigne_nuit_<pièce>` | CNC de nuit |
| `sensor.temperature_corrige_<pièce>` | CNC de jour |
| `input_number.clim_consigne_nuit_<pièce>` et `clim_consigne_jour_<pièce>` | CAD |
| `sensor.th_<pièce>_temperature` | température réelle |
| `climate.clim_<pièce>_rm4_mini` | CRE (attribut `temperature`) |
| `notify.track_clim` | écriture du journal |

Fiche de l'intégration File : `docs/01_docs_config_system/01_config_system_MD/integrations_file/integrations_file.md`.

---

<!-- annotations_log:
[2026-11-23] Fiche créée par l'histo-final (export local de l'automation prod, palier 1 du contrôle prod fonctionnelle) -->