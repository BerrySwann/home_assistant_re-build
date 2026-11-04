# (D) Notification température Up ou Down de (21h00 -> 7h30)

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

> **Catégorie :** P1_01_Clim_chauffage
> **Alias HA :** `(D) Notification température Up ou Down de (21h00 -> 7h30)`
> **ID HA :** `1775243679316`
> **Fichier :** `P1_01_Clim_chauffage/D_notification_temperature_up_ou_down_21h00_7h30/D_notification_temperature_up_ou_down_21h00_7h30.yaml`
> **Empreinte relevée le 2026-11-04 :** MD5 `250a022d`, 1552 octets

---

## Description

Envoie le message personnalisé de clim si le texte change, OU au début de la nuit à 21h00.

## Déclencheurs

- `state` entity_id=sensor.th_balcon_nord_temperature
- `time` at=21:00:00

## Actions

- CONDITION : PÉRIODE NOCTURNE · `?`
- ACTION : PAUSE 2 SECONDES · `delay`
- LOGIQUE : VÉRIFICATION CAPTEURS · `if`

## Entités citées

- `notify.mobile_app_eric`
- `sensor.eric_wi_fi_connection`
- `sensor.mamour_wi_fi_connection`
- `sensor.message_clim_personnalise_21h00_7h30`
- `sensor.th_balcon_nord_temperature`

## Points d'attention

Fiche produite le 2026-11-04 à partir du YAML local, pour combler l absence de fiche signalée par R63.4. Les sections Déclencheurs, Actions et Entités sont extraites du fichier, pas rédigées : à enrichir à la main si le comportement mérite une explication.
