# P3 SDB - Sync Miroir Lampe et Relais SDB

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

**Catégorie :** P3_eclairage
**Alias HA :** `P3_SDB - SYNC MIROIR LAMPE ET RELAIS SDB`
**ID HA :** `1780200461358`
**Mode HA :** `restart`

## Description

Aligne le relais Sonoff sur l'état de la lampe Hue SDB (ON/OFF) et sécurise l'allumage des deux.

Deux blocs d'action :
1. **Synchronisation du relais sur la lampe** : à chaque changement d'état de la lampe Hue, le relais Sonoff suit (`switch.turn_on` / `switch.turn_off`).
2. **Sécurité ON** : si la lampe est allumée, force AUSSI le relais et la lampe — évite un état désynchronisé où la lampe brille mais le relais est coupé.

## Déclencheurs

- `state` sur `light.hue_white_lamp_salle_de_bain` (alias : CHANGEMENT D'ÉTAT DE LA LAMPE SDB)

## Entités principales

- `light.hue_white_lamp_salle_de_bain` (lampe Hue SDB — chef de file)
- `switch.relais_lumiere_sdb_sonoff` (relais Sonoff piloté en miroir)

## Fichier source

`P3_eclairage/p3_sdb_sync_miroir_lampe_et_relais_sdb.yaml`

---
*Doc créée le 2026-09-10 (audit huissier : automation active dans HA sans fiche MD).*
