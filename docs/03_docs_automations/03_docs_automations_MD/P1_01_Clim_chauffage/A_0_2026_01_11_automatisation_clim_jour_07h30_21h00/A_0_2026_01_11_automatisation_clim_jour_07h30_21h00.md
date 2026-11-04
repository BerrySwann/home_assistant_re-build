# (A - 0) 2026-01-11 AUTOMATISATION CLIM JOUR (07H30 <-> 21H00)

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
> **Alias HA :** `(A - 0) 2026-01-11 AUTOMATISATION CLIM JOUR (07H30 <-> 21H00)`
> **ID HA :** `1767373340706`
> **Fichier :** `P1_01_Clim_chauffage/A_0_2026_01_11_automatisation_clim_jour_07h30_21h00/A_0_2026_01_11_automatisation_clim_jour_07h30_21h00.yaml`
> **Empreinte relevée le 2026-11-04 :** MD5 `e0f6b40e`, 2021 octets

---

## Description

Pilotage clims jour - délègue au script P1_MASTER_gestion_clim

## Déclencheurs

- `homeassistant` event=start
- `time` at=07:30:00
- `state` entity_id=sensor.mamour_network_type, sensor.eric_network_type
- `state` entity_id=switch.clim_salon_nous, switch.clim_bureau_nous, switch.clim_chambre_nous
- `state` entity_id=binary_sensor.contact_fenetre_salon_sonoff_contact, binary_sensor.contact_fenetre_cuisine_sonoff_contact, binary_sensor.contact_fenetre_bureau_sonoff_contact, binary_sensor.contact_fenetre_chambre_sonoff_contact · to=on · from=off
- `state` entity_id=binary_sensor.contact_fenetre_salon_sonoff_contact, binary_sensor.contact_fenetre_cuisine_sonoff_contact, binary_sensor.contact_fenetre_bureau_sonoff_contact, binary_sensor.contact_fenetre_chambre_sonoff_contact · to=off · from=on
- `state` entity_id=sensor.groupe, sensor.th_balcon_nord_temperature, sensor.temperature_cible, sensor.mode_ete_hiver, sensor.temperature_confort_jour

## Actions

- `action`

## Entités citées

- `binary_sensor.contact_fenetre_bureau_sonoff_contact`
- `binary_sensor.contact_fenetre_chambre_sonoff_contact`
- `binary_sensor.contact_fenetre_cuisine_sonoff_contact`
- `binary_sensor.contact_fenetre_salon_sonoff_contact`
- `script.p1_master_gestion_clim`
- `sensor.eric_network_type`
- `sensor.groupe`
- `sensor.mamour_network_type`
- `sensor.mode_ete_hiver`
- `sensor.temperature_cible`
- `sensor.temperature_confort_jour`
- `sensor.th_balcon_nord_temperature`
- `switch.clim_bureau_nous`
- `switch.clim_chambre_nous`
- `switch.clim_salon_nous`

## Points d'attention

Fiche produite le 2026-11-04 à partir du YAML local, pour combler l absence de fiche signalée par R63.4. Les sections Déclencheurs, Actions et Entités sont extraites du fichier, pas rédigées : à enrichir à la main si le comportement mérite une explication.
