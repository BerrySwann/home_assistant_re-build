# Rattrapage Linky MANQUANT + Ecart

**Catégorie :** energie
**Alias HA :** `[P0] Rattrapage Linky MANQUANT + Ecart`

## Description

Tourne à 23h59:30 (30s après les 2 autos histo). Construit un JSON avec `day_1` à `day_7` (valeurs > 0 uniquement, dates converties en JJ/MM depuis `dailyweek`) et appelle le script Python `/config/.scripts/correct_linky.py`.

Le script corrige TOUTES les lignes `(MANQUANT)` de `linky_histo.txt` correspondantes :
- Lit `nodon_histo.txt` pour trouver la valeur Nodon de chaque date corrigée
- Calcule l'écart et l'ajoute dans `ecart_histo.txt` avec la mention `(RATTRAPÉ)`
- Si aucune ligne MANQUANT : ne fait rien

Couvre jusqu'à 7 jours de retard Enedis en une seule exécution.

## Déclencheurs

- `time` 23:59:30

## Entités principales

- `sensor.linky_25481620821301_consumption` (attrs `day_1` à `day_7`, `dailyweek`)
- `shell_command.correct_linky_log` -> `/config/.scripts/correct_linky.py`
  - Lit : `/config/notifs/linky_histo.txt`
  - Lit : `/config/notifs/nodon_histo.txt`
  - Écrit : `/config/notifs/linky_histo.txt` (correction MANQUANT -> RATTRAPÉ)
  - Append : `/config/notifs/ecart_histo.txt`

## Fichier source

`energie/rattrapage_linky_ecart.yaml`

## Scripts associés

- `shell_command/P0/P0_correct_linky.yaml` -> `shell_command.correct_linky_log`
- `/config/.scripts/correct_linky.py` (déployé en prod)

---
*Doc créée le 2026-09-01*
