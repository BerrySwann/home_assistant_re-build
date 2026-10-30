# TIMERS DE DUREE - SOUFFLANT ET SECHE-SERVIETTES SDB

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> Mis en place le 2026-10-07 au soir, decision Eric. **Non teste en conditions reelles.**

## 1. Pourquoi

Le compte de duree du soufflant (script `sdb_soufflant_demarrer`, 60 min) et celui du seche-serviettes (`delay` de 2 h dans l'automation F) vivent dans une execution en cours. Un redemarrage de Home Assistant efface le `delay` (ticket SDB-60MIN-FRAGILE). Un timer natif avec `restore: true` reprend avec le temps restant.

## 2. Helpers (dossier `timers/P1_timers/`, inclus par `timer: !include_dir_merge_named timers/`)

| Entite | Duree | Fichier |
|:--|:--|:--|
| `timer.soufflant_sdb_60mn` | 01:00:00 | `P1_timer_60mn_soufflant_SDB.yaml` |
| `timer.soufflant_sdb_10mn` (rattrapage) | 00:10:00 | `P1_timer_10mn_soufflant_SDB.yaml` |
| `timer.seche_serviettes_sdb_2h` | 02:00:00 | `P1_timer_2h_seche_serviettes_SDB.yaml` |
| `timer.seche_serviettes_sdb_10mn` (rattrapage) | 00:10:00 | `P1_timer_10mn_seche_serviettes_SDB.yaml` |

Un nouveau fichier timer se charge avec le service `timer.reload`. Le domaine `timer` a demande un redemarrage de HA la premiere fois (2026-10-07, 21h30).

## 3. Automations

| Lettre | Role |
|:--|:--|
| D | Soufflant : interrupteur de arret a marche (`from: off`) lance le 60 mn ; passage sur arret annule les deux timers ; fin d'un timer coupe l'interrupteur s'il est en marche (le routage lance alors le script d'arret). |
| E | Soufflant, demarrage de HA : attend 30 s, leve le verrou, lance le 10 mn si l'interrupteur est en marche et si aucun timer n'est actif. |
| G | Seche-serviettes : puissance > 50 W lance le 2 h (s'il est inactif) et annule le 10 mn ; prise sur arret annule les timers ; fin de timer : coupure, notification, attente 1 min, remise en veille. |
| H | Seche-serviettes, demarrage de HA : attend 30 s, lance le 10 mn si la prise est en marche et si aucun timer n'est actif. |

Exports YAML : `03_docs_automations_YAML/P1_03_Chauffage_Salle_de_Bain/` (d_, e_, g_, h_ ...). L'automation F (ancienne E puis G, `delay` de 2 h) reste active en doublon jusqu'au test de G.

## 4. Test a faire

1. Allumer le soufflant : `timer.soufflant_sdb_60mn` doit passer `active`. L'eteindre : retour a `idle`.
2. Redemarrer HA soufflant en marche : le 60 mn doit etre restaure avec le temps restant. A defaut, E lance le 10 mn.
3. Meme controle pour le seche-serviettes (G / H). Apres validation, desactiver F.

## 5. Limites connues

- Si la fin d'un timer tombe pendant l'arret de HA, `timer.finished` n'est pas emis au demarrage (doc officielle HA). D'ou le rattrapage de 10 min.
- Le delai de 30 s avant lecture des timers est une estimation, a verifier.
- Les deux dernieres etapes du script de demarrage (arret force a 60 min) restent en doublon.
- Risque ancien de l'automation B (routage, `to: on` sans `from`) au redemarrage de HA : voir TODO SDB-ROUTAGE-REDEMARRAGE.
