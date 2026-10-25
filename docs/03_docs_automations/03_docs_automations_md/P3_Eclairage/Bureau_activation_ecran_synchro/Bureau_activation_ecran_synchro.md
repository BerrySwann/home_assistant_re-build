# Bureau - Activation Écran Synchronisation

**Catégorie :** P3_eclairage
**Alias HA :** `P3_BUREAU_ACTIVATION_ECRAN_SYNCHRO`
**Entité :** `automation.bureau_activation_ecran_synchro` (id `1775331623943`), mode `restart`

## Description

Gère la prise écran `switch.ecran_p_c_3_play_hue` (alimentation de l'écran et des Hue Play). Les Hue Play sont gérées par une autre automation : `P3_BUREAU - Forcer Play ON si PC tourne`.

- Quand `binary_sensor.moniteur_pc` passe à `on`, la prise est allumée.
- Quand la prise reste à `off` plus de 7 minutes alors que `moniteur_pc` est `on`, la prise est rallumée. Le délai de 7 minutes laisse l'arrêt programmé du PC (skill histo-final : prise coupée, puis arrêt du PC 5 minutes plus tard) se terminer : `moniteur_pc` passe à `off` avant, la condition est alors fausse et rien n'est rallumé.

## Déclencheurs

- `pc_on` : `binary_sensor.moniteur_pc` passe à `on`
- `pc_off` : `binary_sensor.moniteur_pc` passe à `off` depuis 2 minutes (aucune action associée pour l'instant : le déclencheur ne fait rien)
- `prise_off` : `switch.ecran_p_c_3_play_hue` passe à `off` depuis 7 minutes

## Actions

- cas `pc_on` : `switch.turn_on` sur `switch.ecran_p_c_3_play_hue`
- cas `prise_off`, si `moniteur_pc` est `on` : `switch.turn_on` sur `switch.ecran_p_c_3_play_hue`

## Entités principales

- `binary_sensor.moniteur_pc`
- `switch.ecran_p_c_3_play_hue`

## Limites connues

- `moniteur_pc` est affiché comme appartenant au Hue Bridge (espace de loisirs Moniteur PC, device_class `running`) : il semble indiquer que la synchro tourne, pas que le PC est allumé (déduit, source non vérifiée). Entre le démarrage du PC et le démarrage de la synchro, la prise reste coupée (13h15 à 13h20 le 2026-10-11).

## Historique

- 2026-10-11 : ajout du déclencheur `prise_off` (7 min) et de son cas.

## Fichier source

`docs/03_docs_automations/03_docs_automations_yaml/P3_Eclairage/p3_bureau_activation_ecran_synchro/p3_bureau_activation_ecran_synchro.yaml`

---
*Doc mise à jour le 2026-10-11*