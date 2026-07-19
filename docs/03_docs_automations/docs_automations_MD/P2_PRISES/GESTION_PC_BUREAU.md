# GESTION PC BUREAU — SCÈNE DE FIN + NOTIF

> **Fichier :** `docs_automations/TREE_CORRIGE/P2_prises/gestion_pc_bureau_scene_de_fin_notif.yaml`
> **ID HA :** `1775245732227`
> **Mode HA :** `parallel`
> **MàJ :** 2026-06-02

---

## 📝 Description

Gestion du cycle PC bureau : allumage/extinction via bouton MQTT (Poussoir IKEA TRADFRI)
ou détection veille < 40W pendant 2 min. Pilote uniquement l'éclairage `light.hue_smart_eco_pc_bureau`.

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| `bouton_mqtt` | `mqtt` | `zigbee2mqtt2/Poussoir (IKEA TRADFRI)/action` |
| `extinction_conso` | `numeric_state` | `sensor.prise_bureau_pc_ikea_power` < 40W pendant 2 min |

---

## ⚙️ Actions — Choose

**ALLUMAGE (bouton ON) :**
- `trigger.payload_json.action == 'on'` OU `trigger.id == 'bouton_mqtt'`
- `light.turn_on → light.hue_smart_eco_pc_bureau`

**EXTINCTION (bouton OFF ou veille < 40W) :**
- `trigger.payload_json.action == 'off'` OU `trigger.id == 'extinction_conso'`
- `light.turn_off → light.hue_smart_eco_pc_bureau`
- Notification `Veille détectée` / `PC Bureau [OFF]`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt2/Poussoir (IKEA TRADFRI)/action` | Bouton physique |
| `sensor.prise_bureau_pc_ikea_power` | Puissance (détection veille) |
| `light.hue_smart_eco_pc_bureau` | Éclairage bureau PC |

### Notifications

| Titre | Message |
|:---|:---|
| `Veille détectée` | `PC Bureau [OFF]` (tag: notif_pc_bureau) |

---

## ⚠️ Notes techniques

- Topic : `zigbee2mqtt2` (LXC 200) — pas `zigbee2mqtt`.
- `trigger.payload_json.action` utilisé directement — fonctionne car le trigger MQTT fournit toujours du JSON.
- Le trigger `extinction_conso` est géré par `condition: trigger id: extinction_conso` (pas de payload_json).
- `mode: parallel` : permet allumage et extinction simultanés si besoin.
