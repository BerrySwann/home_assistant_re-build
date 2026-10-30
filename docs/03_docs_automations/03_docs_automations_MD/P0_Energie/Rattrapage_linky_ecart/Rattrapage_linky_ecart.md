# Rattrapage Linky MANQUANT + Ecart

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

**Catégorie :** energie
**Alias HA :** `D - [P0] Rattrapage Linky MANQUANT + Ecart`

## Description

Tourne à 01h00 (après arrivée des données Enedis). Construit un JSON avec `day_1` à `day_7` (valeurs > 0 uniquement, dates converties en JJ/MM depuis `dailyweek`) et appelle le script Python `/config/.scripts/correct_linky.py`.

Le script corrige TOUTES les lignes `(MANQUANT)` de `linky_histo.txt` correspondantes :
- Lit `nodon_histo.txt` pour trouver la valeur Nodon de chaque date corrigée
- Calcule l'écart et l'ajoute dans `ecart_histo.txt` avec la mention `(RATTRAPÉ)`
- Si aucune ligne MANQUANT : ne fait rien

Couvre jusqu'à 7 jours de retard Enedis en une seule exécution.

## Déclencheurs

- `time` 01:00:00 (alias : HORAIRE : EXECUTION 01H00)

## Entités principales

- `sensor.linky_25481620821301_consumption` (attrs `day_1` à `day_7`, `dailyweek`)
- `shell_command.correct_linky_log` -> `/config/.scripts/correct_linky.py`
  - Lit : `/config/notifs/linky_histo.txt`
  - Lit : `/config/notifs/nodon_histo.txt`
  - Écrit : `/config/notifs/linky_histo.txt` (correction MANQUANT -> RATTRAPÉ)
  - Append : `/config/notifs/ecart_histo.txt`

## Fichier source

`P0_energie/rattrapage_linky_ecart.yaml` (et `energie/rattrapage_linky_ecart.yaml` — synchro identique)

## Scripts associés

- `shell_command/P0/P0_correct_linky.yaml` -> `shell_command.correct_linky_log`
- `/config/.scripts/correct_linky.py` (déployé en prod)

---
*Doc créée le 2026-09-01 — Corrections 2026-09-03 : trigger 23:59:30 -> 01:00:00, template data.append() -> ns.namespace (SecurityError fix), energie/ synchro avec P0_energie/*
*Corrections 2026-10-23 : alias HA renomme avec une lettre d ordre d execution (A a D), aligne sur la prod.*
