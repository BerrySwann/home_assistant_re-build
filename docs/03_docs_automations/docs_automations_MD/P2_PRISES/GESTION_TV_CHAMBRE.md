# GESTION TV CHAMBRE — SCÈNE DE FIN + NOTIF

> **Fichier :** `docs_automations/TREE_CORRIGE/P2_prises/gestion_tv_chambre_scene_de_fin_notif.yaml`
> **ID HA :** `1775330762844`
> **Mode HA :** `single`
> **MàJ :** 2026-06-02

---

## 📝 Description

Gestion du cycle TV chambre : allumage/extinction via bouton MQTT (Poussoir IKEA TRADFRI)
ou détection veille < 20W pendant 2 min. Pilote l'éclairage `light.hue_smart_eco_tv_chambre`
et la prise `switch.prise_tv_chambre_nous`.

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| `bouton_mqtt` | `mqtt` | `zigbee2mqtt2/Poussoir TV (IKEA TRADFRI)/action` |
| `extinction_conso` | `numeric_state` | `sensor.prise_tv_chambre_nous_power` < 20W pendant 2 min |

---

## ⚙️ Actions — Choose

**ALLUMAGE (bouton ON) :**
- `trigger.payload == 'on'` ET `switch.prise_tv_chambre_nous` est `off` (garde-fou anti-doublon)
- `light.turn_on → light.hue_smart_eco_tv_chambre`
- `switch.turn_on → switch.prise_tv_chambre_nous`

**EXTINCTION (bouton OFF ou veille < 20W) :**
- `trigger.payload == 'off'` OU `trigger.id == 'extinction_conso'`
- `light.turn_off → light.hue_smart_eco_tv_chambre`
- Notification `Veille détectée` / `Prise TV [OFF]`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt2/Poussoir TV (IKEA TRADFRI)/action` | Bouton physique |
| `sensor.prise_tv_chambre_nous_power` | Puissance TV (détection veille) |
| `light.hue_smart_eco_tv_chambre` | Éclairage ambiance TV chambre |
| `switch.prise_tv_chambre_nous` | Prise TV (ON/OFF) |

### Notifications

| Titre | Message |
|:---|:---|
| `Veille détectée` | `Prise TV [OFF]` (tag: notif_tv_chambre) |

---

## ⚠️ Notes techniques

- Topic : `zigbee2mqtt2` (LXC 200) — pas `zigbee2mqtt`.
- `trigger.payload` utilisé (pas `payload_json`) : le topic `/action` sur IKEA envoie une string directe.
- Garde-fou allumage : `switch.prise_tv_chambre_nous == off` évite le double-allumage.
- `mode: single` : une seule instance à la fois — pas de chevauchement allumage/extinction.
