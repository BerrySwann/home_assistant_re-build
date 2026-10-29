# CORRECT_LINKY - Rattrapage des jours MANQUANT dans l'historique Linky

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Script :** `correct_linky.py` (Python 3)
> **Emplacement prod :** `/config/.scripts/correct_linky.py`
> **Emplacement local :** `docs/01_docs_config_system/01_config_system_SH_PY_YAML/.scripts/02_scripts.py/correct_linky.py` (copie identique dans `docs/04_docs_scripts/04_docs_scripts_YAML/Correct_linky/Correct_linky.py`)
> **Empreinte relevée le 2026-10-18 :** MD5 `a32d90f9`, 4911 octets, copies identiques à la prod
> **Appelé par :** `shell_command.correct_linky_log` (fichier `shell_command/P0/P0_correct_linky.yaml`), lui-même appelé par l'automation de rattrapage Linky de `automations.yaml` (action `shell_command.correct_linky_log`, vers la ligne 2468)
> **Dernière modification :** 2026-08-30 (date du fichier)

---

## Description

Quand Linky n'avait pas encore publié la consommation d'un jour, la ligne de cet historique contient `MANQUANT`. Le script remplace ces lignes par la valeur réelle quand elle est disponible, et enregistre l'écart avec la mesure Nodon du même jour.

## Fonctionnement

- Argument unique : un texte JSON, une liste de `{"date": "JJ/MM", "val": kWh}`. Exemple : `[{"date": "28/08", "val": 14.37}]`. Seuls les jours avec `val` supérieur à 0 sont passés par l'automation (jours day_1 à day_7 de l'entité Linky).
- Pour chaque entrée, cherche dans `linky_histo.txt` la ligne exacte `JJ/MM | Linky : 0.00 kWh (MANQUANT)` et la remplace par `JJ/MM | Linky : <valeur> kWh (RATTRAPÉ)`. Si la ligne n'existe pas, il passe au jour suivant (Linky était déjà disponible).
- Lit `nodon_histo.txt` pour la valeur Nodon du même jour. Si elle manque, avertit et ne calcule pas d'écart.
- Calcule l'écart (Linky moins Nodon, arrondi à 2 décimales) et son pourcentage de la valeur Linky (1 décimale), et ajoute une ligne `JJ/MM | Linky: ... kWh | Nodon: ... kWh | Ecart: ... (...%) (RATTRAPÉ)` à `ecart_histo.txt`.
- Code de sortie 1 si l'argument manque, si le JSON est invalide, si ce n'est pas une liste, ou si `linky_histo.txt` est introuvable.

## Fichiers touchés

- `/config/notifs/linky_histo.txt` : lecture et réécriture.
- `/config/notifs/nodon_histo.txt` : lecture seule.
- `/config/notifs/ecart_histo.txt` : ajout en fin de fichier.

Ces trois fichiers sont dans le dossier `notifs` de la prod. Ils ne sont pas dans le local (décision d'Eric du 2026-10-18 : une copie existe dans GitHub). `notifs` n'est pas inclus par `configuration.yaml`.

## Points d'attention

- Le texte exact `Linky : 0.00 kWh (MANQUANT)` doit être celui qu'écrit l'automation qui alimente `linky_histo.txt` (non relu pour cette fiche : inconnu).
- Le script réécrit `linky_histo.txt` en entier quand au moins un jour est corrigé.

## Dépendances

- `shell_command.correct_linky_log` (`python3 /config/.scripts/correct_linky.py '<json>'`).
- Le dossier `/config/.scripts/` doit exister en prod (commentaire du shell_command).