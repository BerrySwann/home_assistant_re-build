# (D) SDB SOUFFLANT - DECOMPTE 60 MIN (timer)

> **Fichier :** `docs/03_docs_automations/docs_automations_YAML/P1_03_Chauffage Salle de Bain/d_sdb_soufflant_decompte_60min_timer/d_sdb_soufflant_decompte_60min_timer.yaml`
> **ID HA :** `1791401485072`
> **Mode HA :** `queued` (`max: 5`)
> **MàJ :** 2026-10-10 (fiche écrite à partir du YAML, identique à H:\automations.yaml)

---

## Description

Sécurité de durée du soufflant de la salle de bain. `timer.soufflant_sdb_60mn` est lancé quand l'interrupteur passe vraiment de arrêt à marche, annulé quand il passe sur arrêt, et l'automation coupe l'interrupteur à la fin du timer (60 min, ou 10 min de rattrapage). Le timer survit à un redémarrage de Home Assistant (restore). Décision Eric 2026-10-07 : remplace à terme le compte d'une heure du script de démarrage (SDB-60MIN-FRAGILE).

---

## Déclencheurs

| ID | Type | Détail |
|:---|:---|:---|
| `marche` | `state` | `switch.inter_soufflant_salle_de_bain` de `off` vers `on` |
| `arret` | `state` | `switch.inter_soufflant_salle_de_bain` vers `off` |
| `fin` | `timer.finished` | `timer.soufflant_sdb_60mn` ou `timer.soufflant_sdb_10mn` |

---

## Actions

| Déclencheur | Action |
|:---|:---|
| `marche` | `timer.start` sur `timer.soufflant_sdb_60mn` |
| `arret` | `timer.cancel` sur les deux timers (60mn et 10mn) |
| `fin` | si l'interrupteur est encore `on` : `switch.turn_off` |

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `switch.inter_soufflant_salle_de_bain` | Interrupteur du soufflant |
| `timer.soufflant_sdb_60mn` | Décompte principal |
| `timer.soufflant_sdb_10mn` | Rattrapage (lancé par E) |

Pas de notification. Voir aussi `TIMERS_SDB_SOUFFLANT_ET_SECHE_SERVIETTES.md`.
