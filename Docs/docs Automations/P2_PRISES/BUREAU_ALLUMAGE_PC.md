# BUREAU — ALLUMAGE MANUEL PC (MQTT POUSSOIR IKEA)

> **Fichier :** `automations_corrige/P2_prises/bureau_allumage_pc.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Simple automation MQTT : dès qu'un appui `on` est détecté sur le poussoir
IKEA TRADFRI, allume la prise PC bureau.

---

## ⚡ Déclencheurs

| Type | Topic MQTT | Payload |
|:---|:---|:---|
| `mqtt` | `zigbee2mqtt/Poussoir (IKEA TRADFRI)/action` | `on` |

---

## ⚙️ Action

- `switch.turn_on` → `switch.hue_smart_eco_pc_bureau`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt/Poussoir (IKEA TRADFRI)/action` | Déclencheur physique |
| `switch.hue_smart_eco_pc_bureau` | Prise alim PC |

---

## ⚠️ Note

Le pilotage complet (ON + OFF + veille) est géré par `gestion_pc_bureau.yaml`.
Cette automation ne gère que l'allumage via le bouton physique.
