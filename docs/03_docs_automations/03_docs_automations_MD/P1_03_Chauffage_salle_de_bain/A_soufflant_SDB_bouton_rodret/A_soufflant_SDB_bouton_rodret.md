# (A) SDB SOUFFLANT - BOUTON IKEA RODRET (MQTT vers interrupteur)

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_03_Chauffage_Salle_de_Bain/a_soufflant_sdb_bouton_rodret/a_soufflant_sdb_bouton_rodret.yaml`
> **ID HA :** `1790623332290`
> **Mode HA :** `single`
> **MàJ :** 2026-10-10 (fiche écrite à partir du YAML, identique à H:\automations.yaml)

---

## Description

Le bouton IKEA Rodret de la salle de bain pilote l'interrupteur virtuel du soufflant. C'est l'interrupteur qui déclenche ensuite les séquences (voir B).

---

## Déclencheurs

| ID | Type | Détail |
|:---|:---|:---|
| `rodret_on` | `mqtt` | topic `zigbee2mqtt2/Inter Soufflant Salle de Bain (IKEA RODRET)/action`, payload `on` (appui I) |
| `rodret_off` | `mqtt` | même topic, payload `off` (appui O) |

---

## Actions

| Déclencheur | Action |
|:---|:---|
| `rodret_on` | `switch.turn_on` sur `switch.inter_soufflant_salle_de_bain` |
| `rodret_off` | `switch.turn_off` sur `switch.inter_soufflant_salle_de_bain` |

---

## Dépendances

| Entité / topic | Rôle |
|:---|:---|
| `zigbee2mqtt2/Inter Soufflant Salle de Bain (IKEA RODRET)/action` | Appuis du bouton |
| `switch.inter_soufflant_salle_de_bain` | Interrupteur virtuel, entrée unique du soufflant |

Pas de notification, pas de condition.

---

## Chaîne

Bouton Rodret (A) -> interrupteur virtuel -> routage (B) -> scripts `sdb_soufflant_demarrer` / `sdb_soufflant_arreter`.
