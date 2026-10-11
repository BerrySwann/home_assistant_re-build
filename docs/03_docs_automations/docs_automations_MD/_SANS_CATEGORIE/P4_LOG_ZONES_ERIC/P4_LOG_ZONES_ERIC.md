# P4 - Log Zones Eric

**Catégorie :** P4_presence
**Alias HA :** `[P4] Eric — Log Zones`
**ID HA :** `1781715097077`
**Mode HA :** `queued` (max 10)

## Description

Enregistre chaque changement de zone d'Eric dans `/config/.logs/zone_eric.txt` (via `notify.zone_eric`).

Format de chaque ligne : `AAAA-MM-JJ HH:MM:SS | <zone précédente> → <zone courante>`.

Garde-fous : les transitions depuis/vers `unavailable` ou `unknown` sont ignorées au niveau du trigger (`not_from` / `not_to`), et une condition d'action vérifie que la zone courante n'est ni vide, ni `unavailable`, ni `unknown`.

## Déclencheurs

- `state` sur `device_tracker.poco` (alias : CHANGEMENT ZONE ERIC)

## Entités principales

- `device_tracker.poco` (téléphone d'Eric)
- `notify.zone_eric` (écriture dans `/config/.logs/zone_eric.txt`)

## Fichier source

`P4_presence/P4_log_zones_eric.yaml`

---
*Doc créée le 2026-09-10 (audit huissier : automation active dans HA sans fiche MD).*
