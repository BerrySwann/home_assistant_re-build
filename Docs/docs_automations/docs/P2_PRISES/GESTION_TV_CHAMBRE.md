# GESTION TV CHAMBRE — SCÈNE DE FIN + NOTIF

> **Fichier :** `docs_automations/TREE_CORRIGE/P2_prises/gestion_tv_chambre.yaml`
> **Mode HA :** `parallel`
> **MàJ :** 2026-05-17

---

## 📝 Description

Gestion du cycle TV chambre : allumage/extinction via bouton MQTT (Poussoir IKEA TRADFRI)
ou détection veille < 20W pendant 2 min. Pilote uniquement l'éclairage `light.hue_smart_eco_tv_chambre`.

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| `bouton_mqtt` | `mqtt` | `zigbee2mqtt/Poussoir TV (IKEA TRADFRI)/action` |
| `extinction_conso` | `numeric_state` | `sensor.prise_tv_chambre_nous_power` < 20W pendant 2 min |

---

## ⚙️ Actions — Choose

**ALLUMAGE (bouton ON) :**
- `light.turn_on → light.hue_smart_eco_tv_chambre`

**EXTINCTION (bouton OFF ou veille < 20W) :**
- `light.turn_off → light.hue_smart_eco_tv_chambre`
- Notification `Veille détectée` / `TV Chambre [OFF]`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt/Poussoir TV (IKEA TRADFRI)/action` | Bouton physique |
| `sensor.prise_tv_chambre_nous_power` | Puissance TV (détection veille) |
| `light.hue_smart_eco_tv_chambre` | Éclairage ambiance TV chambre |

### Notifications

| Titre | Message |
|:---|:---|
| `Veille détectée` | `TV Chambre [OFF]` (tag: notif_tv_chambre) |

---

## ⚠️ Notes techniques

- Guard `trigger.payload_json is defined` obligatoire : le trigger `extinction_conso`
  (numeric_state) ne possède pas `payload_json` — sans le guard, UndefinedError au runtime.
- Suppression du trigger `allumage_auto` (21h00) et de `switch.prise_tv_chambre_nous` :
  logique simplifiée — bouton physique uniquement.
