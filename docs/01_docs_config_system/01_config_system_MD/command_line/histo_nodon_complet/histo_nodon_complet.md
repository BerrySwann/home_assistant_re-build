# histo_nodon_complet - Lecture de nodon_complet_histo.txt

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-System-ffeb3b?style=flat-square)](.)

</div>

> **Fichier :** `histo_nodon_complet.yaml`
> **Emplacement prod :** `/config/command_line/Energie/histo_nodon_complet.yaml` (et miroir `/config/docs/01_docs_config_system/01_config_system_SH_PY_YAML/...`)
> **Emplacement local :** `docs/01_docs_config_system/01_config_system_SH_PY_YAML/command_line/Energie/histo_nodon_complet.yaml`
> **Empreinte relevée le 2026-10-23 :** MD5 `ed10f126`, 3372 octets, copie locale identique à la prod après le push du 2026-10-23
> **Inclus par :** `configuration.yaml` (`command_line: !include_dir_merge_list command_line/`)
> **Dernière modification :** 2026-10-23 (fichier créé)

---

## Description

Un capteur `command_line` : `Histo Energie Nodon Complet` (`unique_id: histo_energie_nodon_complet`, `scan_interval: 900`). Il lit `/config/notifs/nodon_complet_histo.txt` avec un court script Python et expose l'attribut `data` : un dictionnaire indexé par date `JJ/MM` avec `total` (kWh), `hp` (kWh), `hc` (kWh) et `cout` (EUR), sur les 14 dernières lignes valides. L'attribut `count` donne le nombre de dates lues. L'état du capteur est toujours `OK`.

Format d'une ligne du fichier : `22/10 | Total: 5.0 kWh | HP: 3.7 | HC: 1.3 | Cout: 1.0`. Les lignes `(MANQUANT)` et les lignes illisibles sont ignorées sans bloquer les autres.

## Automation rattachée

- **E - [P0] Histo Nodon complet quotidien** (id `1792780906393`, 23:59:10) écrit le fichier via `notify.nodon_complet_histo` (intégration File, chemin `/config/notifs/nodon_complet_histo.txt`, horodatage désactivé). Elle y consigne chaque nuit le total, le HP, le HC et le coût de la veille (coût aux tarifs `sensor.tarif_heures_pleines_ttc` / `sensor.tarif_heures_creuses_ttc`).

## Utilisé par

- `P0_MyElectricalData.yaml` : les capteurs `linky_jour_1` à `linky_jour_7` lisent `data[JJ/MM]` quand le relevé Linky d'une date vaut 0 (voir sa fiche). Le nom du jour reçoit alors une `*`.

## Points d'attention

- Le fichier n'existe pas avant la première écriture (23:59:10 le 2026-10-23, ligne du 22/10). Tant qu'il est absent, l'attribut `data` n'existe pas et les templates passent à leur repli suivant (`last_period` pour hier, sinon `nodon_histo.txt`).
- `scan_interval` 900 : une ligne écrite à 23:59:10 est visible dans le capteur au plus tard 15 minutes plus tard. Mise à jour immédiate possible avec `homeassistant.update_entity`.
- Aucun guillemet double dans le script Python : la commande est encadrée par des guillemets doubles dans le YAML.
- Prérequis côté HA : l'intégration File `nodon_complet_histo` (créée dans l'UI), sinon l'automation E ne peut pas écrire.