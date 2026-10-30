# (G) SDB SECHE-SERVIETTES - DECOMPTE 2 H (timer)

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_03_Chauffage_Salle_de_Bain/g_sdb_seche_serviettes_decompte_2h_timer/g_sdb_seche_serviettes_decompte_2h_timer.yaml`
> **ID HA :** `1791401998919`
> **Mode HA :** `queued` (`max: 5`)
> **MàJ :** 2026-10-10 (fiche écrite à partir du YAML, identique à H:\automations.yaml)

---

## Description

Sécurité de durée du sèche-serviettes de la salle de bain. `timer.seche_serviettes_sdb_2h` est lancé quand la puissance de la prise dépasse 50 W (comme l'automation F), annulé quand la prise passe sur arrêt, et à la fin d'un timer (2 h, ou 10 min de rattrapage) coupe la prise, notifie, attend 1 min puis remet la prise en marche (veille). Le timer survit à un redémarrage de HA (restore). Décision Eric 2026-10-07. L'automation F reste active en doublon jusqu'à décision d'Eric.

---

## Déclencheurs

| ID | Type | Détail |
|:---|:---|:---|
| `chauffe` | `numeric_state` | `sensor.prise_seche_serviette_salle_de_bain_nous_power` > 50 W |
| `arret` | `state` | `switch.prise_seche_serviette_salle_de_bain_nous` vers `off` |
| `fin` | `timer.finished` | `timer.seche_serviettes_sdb_2h` ou `timer.seche_serviettes_sdb_10mn` |

---

## Actions

| Déclencheur | Condition | Action |
|:---|:---|:---|
| `chauffe` | `timer.seche_serviettes_sdb_2h` est `idle` | annuler `timer.seche_serviettes_sdb_10mn`, puis lancer `timer.seche_serviettes_sdb_2h` |
| `arret` | aucune | annuler les deux timers (2h et 10mn) |
| `fin` | la prise est `on` | `switch.turn_off` sur la prise, notification, attente 1 min, `switch.turn_on` (réarmement veille) |

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `sensor.prise_seche_serviette_salle_de_bain_nous_power` | Détection de chauffe (W) |
| `switch.prise_seche_serviette_salle_de_bain_nous` | Pilotage de la prise |
| `timer.seche_serviettes_sdb_2h` / `timer.seche_serviettes_sdb_10mn` | Timers de durée |

### Notifications

| Titre | Message | Cible |
|:---|:---|:---|
| `Seche-Serv. OFF` | `Duree maximale ecoulee. Arret automatique.` | `notify.mobile_app_eric` |

---

## Points d'attention

- Le réarmement en veille (`turn_on` à la fin) est nécessaire pour que la prise reste alimentée et que la consommation reste suivie (même logique que F).
- Doublon avec F (`F_MINUTERIE_SECHE_SERVIETTES`) tant que Eric n'a pas tranché.
