# P4 - Log Zones Eric

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-ff9800?style=flat-square)](.)

</div>

**Catégorie :** P4_presence
**Alias HA :** `[P4] Eric — Log Zones`
**ID HA :** `1781715097077`
**Mode HA :** `queued` (max 10)

## Description

Enregistre chaque changement de zone d'Eric dans `/config/.logs/zone_eric.txt` (via `notify.zone_eric`).

Format de chaque ligne : `AAAA-MM-JJ HH:MM:SS | <zone précédente> → <zone courante>`.

Garde-fous : les transitions depuis/vers `unavailable` ou `unknown` sont ignorées au niveau du trigger (`not_from` / `not_to`), et une condition d'action vérifie que la zone courante n'est ni vide, ni `unavailable`, ni `unknown`.

## Déclencheurs

- `state` sur `device_tracker.poco` (alias : CHANGEMENT ZONE ERIC)

## Entités principales

- `device_tracker.poco` (téléphone d'Eric)
- `notify.zone_eric` (écriture dans `/config/.logs/zone_eric.txt`)

## Fichier source

`P4_presence/P4_log_zones_eric.yaml`

---
*Doc créée le 2026-09-10 (audit huissier : automation active dans HA sans fiche MD).*
