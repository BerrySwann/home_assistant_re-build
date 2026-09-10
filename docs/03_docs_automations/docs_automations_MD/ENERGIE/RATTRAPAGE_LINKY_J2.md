# Rattrapage Linky J-2 + Ecart

**Catégorie :** energie
**Alias HA :** `[P0] Rattrapage Linky J-2 + Ecart`
**ID HA :** `1788118327851`
**Mode HA :** `single`

## Description

Tourne à 23h59:00 (juste après les 2 automatisations histo du soir). Si `day_2` > 0 : appelle le script Python `/config/.scripts/correct_linky.py` avec la date J-2 et la valeur `day_2`.

Le script corrige la ligne `(MANQUANT)` de `linky_histo.txt` si elle existe :
- Lit `nodon_histo.txt` pour trouver la valeur Nodon correspondante
- Calcule l'écart et l'ajoute dans `ecart_histo.txt` avec la mention `(RATTRAPÉ)`
- Si la ligne J-2 n'est pas MANQUANT (cas normal), le script ne fait rien

Différence avec `RATTRAPAGE_LINKY_ECART.md` : celle-ci traite **J-2 uniquement** à 23h59, l'autre traite **jusqu'à 7 jours** de retard à 01h00. Les deux peuvent corriger la même ligne — le script ne retraite jamais une ligne déjà corrigée.

## Déclencheurs

- `time` 23:59:00 (alias : HORAIRE : EXECUTION 23H59)

## Conditions

- Template : `{{ state_attr('sensor.linky_25481620821301_consumption', 'day_2') | float(0) > 0 }}` (données J-2 arrivées)

## Entités principales

- `sensor.linky_25481620821301_consumption` (attr `day_2`)
- `shell_command.correct_linky_log` -> `/config/.scripts/correct_linky.py`
  - Lit : `/config/notifs/linky_histo.txt`
  - Lit : `/config/notifs/nodon_histo.txt`
  - Écrit : `/config/notifs/linky_histo.txt` (correction MANQUANT -> RATTRAPÉ)
  - Append : `/config/notifs/ecart_histo.txt`

Variables passées au script : `date_j2` (`now() - 2 jours` au format `JJ/MM`), `value_j2` (`day_2` arrondi à 2 décimales).

## Fichier source

`P0_energie/rattrapage_linky_j2_ecart.yaml` — **extrait du live le 2026-09-10** (version datée coexistante : `rattrapage_linky_j2_ecart_2026-09-10.yaml`).

## Scripts associés

- `shell_command/P0/P0_correct_linky.yaml` -> `shell_command.correct_linky_log`
- `/config/.scripts/correct_linky.py` (déployé en prod)

---
*Doc créée le 2026-09-10 (audit huissier : automation active dans HA sans fiche) — Discordance relevée : la description HA annonce "23h59:30" alors que le trigger est `23:59:00`.*
