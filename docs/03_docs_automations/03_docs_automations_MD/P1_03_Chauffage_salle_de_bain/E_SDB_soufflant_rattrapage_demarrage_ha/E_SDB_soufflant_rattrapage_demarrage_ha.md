# (E) SDB SOUFFLANT - RATTRAPAGE AU DEMARRAGE DE HA (timer 10 min)

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_03_Chauffage_Salle_de_Bain/e_sdb_soufflant_rattrapage_demarrage_ha_timer/e_sdb_soufflant_rattrapage_demarrage_ha_timer.yaml`
> **ID HA :** `1791401487876`
> **Mode HA :** `single`
> **MàJ :** 2026-10-10 (fiche écrite à partir du YAML, identique à H:\automations.yaml)

---

## Description

Au démarrage de Home Assistant : lève le verrou (le script qui le tenait est mort), puis, si l'interrupteur du soufflant est en marche et qu'aucun timer n'est actif (60 min non restauré ou fini pendant l'arrêt), lance `timer.soufflant_sdb_10mn`. L'automation D coupe l'interrupteur à la fin du timer. Décision Eric 2026-10-07.

---

## Déclencheur

| Type | Détail |
|:---|:---|
| `homeassistant` | événement `start` (HA démarre) |

---

## Actions

1. Attente de 30 s (laisser aux timers le temps d'être restaurés).
2. `input_boolean.turn_off` sur `input_boolean.verrou_soufflant_salle_de_bain` (lever le verrou).
3. Si `switch.inter_soufflant_salle_de_bain` est `on` ET `timer.soufflant_sdb_60mn` est `idle` ET `timer.soufflant_sdb_10mn` est `idle` : `timer.start` sur `timer.soufflant_sdb_10mn`.

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `switch.inter_soufflant_salle_de_bain` | Interrupteur du soufflant |
| `input_boolean.verrou_soufflant_salle_de_bain` | Verrou tenu par les scripts |
| `timer.soufflant_sdb_60mn` / `timer.soufflant_sdb_10mn` | Timers de durée |

Pas de notification. La coupure est faite par D.
