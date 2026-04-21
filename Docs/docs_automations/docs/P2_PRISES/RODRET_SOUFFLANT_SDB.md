# BOUTON IKEA RODRET — SOUFFLANT SDB

> **Fichiers :**
> - `automations_corrige/P2_prises/rodret_soufflant_sdb.yaml`
> - `automations_corrige/P2_bouton_rodret_soufflant_sdb.yaml` (doublon à nettoyer)
> **Mode HA :** `restart`

---

## 📝 Description

Pilotage du soufflant SDB via le bouton RODRET physique. Traduit les actions
MQTT `on`/`off` en changements de `input_boolean.inter_soufflant_salle_de_bain`,
lequel déclenche la logique de chauffage SDB.

---

## ⚡ Déclencheurs

| Type | Topic MQTT |
|:---|:---|
| `mqtt` | `zigbee2mqtt/Inter Radiateur Salle de Bain (IKEA RODRET)` |

---

## ⚙️ Actions — Choose

| Action MQTT | Résultat |
|:---|:---|
| `on` | `input_boolean.turn_on → input_boolean.inter_soufflant_salle_de_bain` |
| `off` | `input_boolean.turn_off → input_boolean.inter_soufflant_salle_de_bain` |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt/Inter Radiateur Salle de Bain (IKEA RODRET)` | Déclencheur physique |
| `input_boolean.inter_soufflant_salle_de_bain` | Helper cible |

---

## ⚠️ Note doublon

`P2_bouton_rodret_soufflant_sdb.yaml` (racine) et `P2_prises/rodret_soufflant_sdb.yaml`
sont identiques. L'un des deux est à supprimer.
