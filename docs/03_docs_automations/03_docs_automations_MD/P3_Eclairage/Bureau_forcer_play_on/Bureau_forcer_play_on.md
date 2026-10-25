# Bureau - Forcer Play ON si PC tourne

**Catégorie :** P3_eclairage
**Alias HA :** `P3_BUREAU - Forcer Play ON si PC tourne`
**Entité :** `automation.bureau_forcer_play_on_si_pc_tourne` (id `1775331547996`), mode `parallel`

## Description

Gère les 3 Hue Play du bureau. Si une Hue Play passe à `off` (éteinte à la main) alors que `binary_sensor.moniteur_pc` est `on`, elle est rallumée à 25 %.

La prise écran `switch.ecran_p_c_3_play_hue` est gérée par une autre automation : `P3_BUREAU_ACTIVATION_ECRAN_SYNCHRO` (fiche `BUREAU_ACTIVATION_ECRAN_SYNCHRO`). Une automation pour la prise, une pour les Play.

## Déclencheurs

- `off_hue_play_1_pc_bureau`, `off_hue_play_2_pc_bureau`, `off_hue_play_3_pc_bureau` : `light.hue_play_1_pc_bureau`, `light.hue_play_2_pc_bureau`, `light.hue_play_3_pc_bureau` passent à `off`

## Condition

- `binary_sensor.moniteur_pc` est `on`

## Actions

Un cas par lampe : `light.turn_on` sur la lampe déclenchante, `brightness_pct: 25`.

## Entités principales

- `light.hue_play_1_pc_bureau`, `light.hue_play_2_pc_bureau`, `light.hue_play_3_pc_bureau`
- `binary_sensor.moniteur_pc`

## Limites connues

- Quand la prise est coupée, les Hue Play passent à `unavailable` et non à `off` (relevé HA du 2026-10-11) : cette automation ne se déclenche pas dans ce cas, c'est le rôle de `P3_BUREAU_ACTIVATION_ECRAN_SYNCHRO`.

## Historique

- 2026-10-11 : une modification manuelle (13h41) avait remplacé la branche Play 3 par un `switch.turn_on` (Play 3 n'était plus rallumée) ; corrigée, puis la logique de la prise remise dans `P3_BUREAU_ACTIVATION_ECRAN_SYNCHRO`. Contenu identique à l'original. Export YAML local réaligné sur la prod.

## Fichier source

`docs/03_docs_automations/03_docs_automations_YAML/P3_Eclairage/p3_bureau_forcer_play_on_si_pc_tourne/p3_bureau_forcer_play_on_si_pc_tourne.yaml`

---
*Doc mise à jour le 2026-10-11*