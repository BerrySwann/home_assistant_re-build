# Script MPC_01_monitor_temp.sh - températures du mini PC (sauvegarde pour le Raspberry)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Archive-9e9e9e?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--01-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-INTERDITES-f44336?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-4fc3f7?style=flat-square)](.)

</div>

**Catégorie :** RASPI (sauvegarde pour le Raspberry Pi 4 4 Go, ce n'est pas un script actif de la prod)

## Ce que fait le script

Boucle infinie qui efface l'écran, affiche la date et l'heure, puis lit en direct les températures du mini PC et les affiche en °C (conversion des milli-degrés avec `bc`). Pause de 2 secondes entre deux relevés.

- Carte mère (`acpitz`) : `/sys/class/thermal/thermal_zone0/temp`
- CPU package (`x86_pkg_temp`) : `/sys/class/thermal/thermal_zone1/temp`
- 4 cœurs CPU : `/sys/devices/platform/coretemp.0/hwmon/hwmon1/temp2_input` à `temp5_input`

Il n'affiche aucun pourcentage d'utilisation (ni CPU, ni mémoire).

## Fichier source

`docs/04_docs_scripts/04_docs_scripts_SH/XX_MPC_01_monitor_temp_sh_RASPI (a ne pas jeter)/#MPC_01_monitor_temp.sh.#` (dossier miroir de celui-ci). C'est un fichier de sauvegarde automatique d'éditeur (1614 octets, MD5 6f853dca), la seule version du script retrouvée. La copie `.sh` a été supprimée le 2026-11-01.

---
*Fiche recréée le 2026-11-01 d'après le contenu du script. Aucune fiche d'origine n'a été retrouvée (recherche dans ReBuild, la prod, GitHub et la corbeille Windows).*
<!-- annotations_log: -->
<!-- [2026-11-01] Fiche créée avec le dossier (a ne pas jeter) sur demande d'Eric -->
<!-- [2026-11-01] Modifs INTERDITES et mention sauvegarde Raspberry Pi 4 4 Go, ordre d'Eric -->
<!-- [2026-11-01] Texte corrigé : caractères parasites et fautes, copie .sh supprimée, ordre d'Eric -->