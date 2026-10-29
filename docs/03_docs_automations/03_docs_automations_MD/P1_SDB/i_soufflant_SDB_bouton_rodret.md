# SDB - Soufflant - Bouton IKEA Rodret (MQTT vers interrupteur)

**Catégorie :** P1_SDB
**Alias HA :** `SDB - SOUFFLANT - BOUTON IKEA RODRET (MQTT vers interrupteur)` (dans `automations.yaml` de la prod : `A - SDB - SOUFFLANT - BOUTON IKEA RODRET (MQTT vers interrupteur)`, ligne 2616 relevée le 2026-10-28)
**Mode :** `single`. **Déployée en prod le 2026-09-28** (d'après l'en-tête du YAML).

## Description

Le bouton IKEA Rodret de la salle de bain pilote l'interrupteur virtuel `switch.inter_soufflant_salle_de_bain`. C'est cet interrupteur qui déclenche ensuite les séquences de démarrage et d'arrêt du soufflant, par l'automation `h_soufflant_SDB_routage`.

Cette fiche remplace l'ancienne fiche `RODRET_SOUFFLANT_SDB.md` (rangée avant dans `P2_Prises`), qui décrivait la version précédente de cette automation : pilotage de `input_boolean.inter_soufflant_salle_de_bain` et topic `zigbee2mqtt/Inter Radiateur Salle de Bain (IKEA RODRET)`. L'ancien contenu est conservé dans la sauvegarde `.bak` de ce dossier.

## Déclencheurs

| Alias du déclencheur | Topic MQTT | Payload | id |
|:---|:---|:---|:---|
| Appui bouton I (marche) | `zigbee2mqtt2/Inter Soufflant Salle de Bain (IKEA RODRET)/action` | `on` | `rodret_on` |
| Appui bouton O (arrêt) | `zigbee2mqtt2/Inter Soufflant Salle de Bain (IKEA RODRET)/action` | `off` | `rodret_off` |

## Actions

- `rodret_on` : `switch.turn_on` sur `switch.inter_soufflant_salle_de_bain`
- `rodret_off` : `switch.turn_off` sur `switch.inter_soufflant_salle_de_bain`

Aucune condition.

## Chaîne

Bouton Rodret (MQTT) -> cette automation -> `switch.inter_soufflant_salle_de_bain` -> automation `SDB - SOUFFLANT - ROUTAGE` (`h_soufflant_SDB_routage`) -> `script.sdb_soufflant_demarrer` ou `script.sdb_soufflant_arreter`.

## Entités principales

- `switch.inter_soufflant_salle_de_bain` (interrupteur virtuel, cible)
- MQTT `zigbee2mqtt2/Inter Soufflant Salle de Bain (IKEA RODRET)/action` (déclencheur physique)

## Historique

- Avant 2026-09-28 : version sur `input_boolean.inter_soufflant_salle_de_bain` (ancienne fiche `RODRET_SOUFFLANT_SDB.md`, qui signalait un doublon de fichier à nettoyer).
- 2026-10-28 : fiche renommée et réécrite d'après le YAML local, rangée avec son YAML dans `P1_SDB`.

## Fichier source

`docs/03_docs_automations/03_docs_automations_YAML/P1_SDB/i_soufflant_SDB_bouton_rodret.yaml`

---
*Doc mise à jour le 2026-10-28*