# Raspberry Pi4 - CPU Fan PWM 6 States

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Archive-9e9e9e?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--01-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-INTERDITES-f44336?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-4fc3f7?style=flat-square)](.)

</div>

> **Sauvegarde pour le Raspberry Pi 4 4 Go.** Modifications interdites : fichier conservé tel quel, ce n'est pas un fichier actif de la prod.

**Catégorie :** RASPI (sauvegarde du Raspberry, ce n'est pas une automation de Home Assistant)
**Alias HA :** `Raspberry CPU Fan PWM 6 States`

## Description

Règle la vitesse du ventilateur du Raspberry (`fan.rpi_cooling_fan`) en fonction de la température du CPU (`sensor.system_monitor_temperature_du_processeur`). Au démarrage de HA le ventilateur est mis à 100 %. Déclencheurs : démarrage, et franchissement à la hausse et à la baisse des seuils 30, 40, 50, 60 et 70. Sous 30 : 30 %. Les autres paliers sont dans le YAML.

## Déclencheurs

- `homeassistant`
- `numeric_state`

## Entités principales

- `sensor.system_monitor_temperature_du_processeur`
- `fan.rpi_cooling_fan`

## Fichier source

`docs/03_docs_automations/03_docs_automations_YAML/RASPI/A_RASPI_fan_pwm_6_states/A_RASPI_fan_pwm_6_states.yaml`

---
*Doc générée le 2026-05-30 ; relue et complétée le 2026-10-11 d'après le YAML (description, chemin source). Pas d'ID HA : l'automation tourne sur le Raspberry.*
<!-- [2026-11-01] Modifs INTERDITES et mention sauvegarde Raspberry Pi 4 4 Go, ordre d'Eric -->
