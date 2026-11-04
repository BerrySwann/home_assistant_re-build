# [00-Backup] Alerte si KO 15 min

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MaJ](https://img.shields.io/badge/MaJ-2026--11--04-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-4fc3f7?style=flat-square)](.)

</div>

> **Catégorie :** Backup_ha_GitHub
> **Alias HA :** `[00-Backup] Alerte si KO 15 min`
> **ID HA :** `1772275440416`
> **Fichier :** `Backup_ha_GitHub/00_Backup_alerte_si_ko_15_min/00_Backup_alerte_si_ko_15_min.yaml`
> **Empreinte relevée le 2026-11-04 :** MD5 `6eaacb3c`, 721 octets

---

## Description

Notification si le backup reste en KO pendant 15 minutes

## Déclencheurs

- `state` entity_id=sensor.backup_github_status · to=KO

## Actions

- `action`
- `action`
- `action`

## Entités citées

- `notify.mobile_app_eric`
- `sensor.backup_github_status`

## Points d'attention

Fiche produite le 2026-11-04 à partir du YAML local, pour combler l absence de fiche signalée par R63.4. Les sections Déclencheurs, Actions et Entités sont extraites du fichier, pas rédigées : à enrichir à la main si le comportement mérite une explication.
