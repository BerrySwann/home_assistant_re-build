# C - SALLE DE BAIN : WATCHDOG SÉCURITÉ SOUFFLANT

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

> **Catégorie :** P1_03_Chauffage_salle_de_bain
> **Alias HA :** `C - SALLE DE BAIN : WATCHDOG SÉCURITÉ SOUFFLANT`
> **ID HA :** `1775331166275`
> **Fichier :** `P1_03_Chauffage_salle_de_bain/C_salle_de_bain_watchdog_securite_soufflant/C_salle_de_bain_watchdog_securite_soufflant.yaml`
> **Empreinte relevée le 2026-11-04 :** MD5 `93b6af8a`, 1975 octets

---

## Description

Reset physique si T > 25°C, uniquement si la prise est alimentée

## Déclencheurs

- `state` entity_id=sensor.th_salle_de_bain_temperature

## Actions

- ACTION : ATTENTE STABILISATION (1 MIN) · `delay`
- ACTION : ENVOI COMMANDE IR RESET · `action`
- ETAT : PASSAGE DU BOOLEAN SUR OFF (SÉCURITÉ) · `action`
- ACTION : ATTENTE AVANT COUPURE (1 MIN) SÉCURITÉ · `delay`
- MATÉRIEL : COUPURE PHYSIQUE DE LA PRISE · `action`
- NOTIFIER : ALERTE MOBILE DÉRIVE THERMIQUE · `action`

## Entités citées

- `input_boolean.inter_soufflant_salle_de_bain`
- `input_boolean.turn_off`
- `notify.mobile_app_eric`
- `sensor.th_salle_de_bain_temperature`
- `switch.prise_soufflant_salle_de_bain_nous`
- `switch.turn_off`

## Points d'attention

Fiche produite le 2026-11-04 à partir du YAML local, pour combler l absence de fiche signalée par R63.4. Les sections Déclencheurs, Actions et Entités sont extraites du fichier, pas rédigées : à enrichir à la main si le comportement mérite une explication.
