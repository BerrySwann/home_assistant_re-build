# Mettre à jour le temps du dernier impact de foudre

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

> **Catégorie :** Meteo
> **Alias HA :** `Mettre à jour le temps du dernier impact de foudre`
> **ID HA :** `1775243312985`
> **Fichier :** `Meteo/Mettre_a_jour_le_temps_du_dernier_impact_de_foudre/Mettre_a_jour_le_temps_du_dernier_impact_de_foudre.yaml`
> **Empreinte relevée le 2026-11-04 :** MD5 `87005db5`, 536 octets

---

## Description

Met à jour le temps du dernier impact de foudre lorsque le capteur change.

## Déclencheurs

- `state` entity_id=sensor.maison_lightning_counter

## Actions

- `action`

## Entités citées

- `input_datetime.dernier_eclair`
- `input_datetime.set_datetime`
- `sensor.maison_lightning_counter`

## Points d'attention

Fiche produite le 2026-11-04 à partir du YAML local, pour combler l absence de fiche signalée par R63.4. Les sections Déclencheurs, Actions et Entités sont extraites du fichier, pas rédigées : à enrichir à la main si le comportement mérite une explication.
