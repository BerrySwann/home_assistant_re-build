# Histo Nodon Quotidien

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

**Catégorie :** energie
**Alias HA :** `B - [P0] Histo Nodon quotidien`

## Description

Enregistre chaque nuit à 23h59 la consommation Nodon J-1 (`last_period` du UM quotidien) dans `/config/notifs/nodon_histo.txt` via l'intégration File `notify.log_nodon_histo`.

Format de ligne : `JJ/MM | Nodon : X.XX kWh`

## Déclencheurs

- `time` 23:59:00

## Entités principales

- `sensor.genelec_appart_quotidien_um` (attr `last_period`)
- `notify.send_message` -> `notify.log_nodon_histo` -> `/config/notifs/nodon_histo.txt`

## Fichier source

`energie/histo_nodon_quotidien.yaml`

## Prérequis

Intégration File créée dans l'UI HA : Paramètres > Appareils > Ajouter intégration > File
- Nom : `log_nodon_histo` | Fichier : `/config/notifs/nodon_histo.txt`

---
*Doc créée le 2026-09-01*
*Corrections 2026-10-23 : alias HA renomme avec une lettre d ordre d execution (A a D), aligne sur la prod.*
