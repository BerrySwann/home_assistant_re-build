# (H) SDB SECHE-SERVIETTES - RATTRAPAGE AU DEMARRAGE DE HA (timer 10 min)

> **Fichier :** `docs/03_docs_automations/docs_automations_YAML/P1_03_Chauffage Salle de Bain/h_sdb_seche_serviettes_rattrapage_demarrage_ha_timer/h_sdb_seche_serviettes_rattrapage_demarrage_ha_timer.yaml`
> **ID HA :** `1791402001955`
> **Mode HA :** `single`
> **MàJ :** 2026-10-10 (fiche écrite à partir du YAML, identique à H:\automations.yaml)

---

## Description

Au démarrage de Home Assistant : si la prise du sèche-serviettes est en marche et qu'aucun des deux timers n'est actif (2 h non restauré ou fini pendant l'arrêt), lance `timer.seche_serviettes_sdb_10mn`. L'automation G coupe la prise à la fin du timer, ou annule ce timer et lance le 2 h si la puissance dépasse 50 W. Décision Eric 2026-10-07.

---

## Déclencheur

| Type | Détail |
|:---|:---|
| `homeassistant` | événement `start` (HA démarre) |

---

## Actions

1. Attente de 30 s (laisser aux timers le temps d'être restaurés).
2. Si `switch.prise_seche_serviette_salle_de_bain_nous` est `on` ET `timer.seche_serviettes_sdb_2h` est `idle` ET `timer.seche_serviettes_sdb_10mn` est `idle` : `timer.start` sur `timer.seche_serviettes_sdb_10mn`.

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `switch.prise_seche_serviette_salle_de_bain_nous` | Prise du sèche-serviettes |
| `timer.seche_serviettes_sdb_2h` / `timer.seche_serviettes_sdb_10mn` | Timers de durée |

Pas de notification. La coupure est faite par G.
