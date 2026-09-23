# GESTION PC BUREAU - SCÈNE DE FIN + NOTIF

> **Fichier :** `P2_prises/gestion_pc_bureau_scene_de_fin_notif.yaml`
> **ID HA :** `1775245732227`
> **Mode HA :** `single`
> **MàJ :** 2026-09-23 (refonte anti-raté)

---

## 📝 Description

Gestion du cycle PC bureau : allumage via bouton MQTT (Poussoir IKEA TRADFRI),
extinction sur veille CONFIRMÉE (puissance < 70W pendant 12 min via
`binary_sensor.veille_pc_bureau`). Pilote uniquement l'éclairage
`light.hue_smart_eco_pc_bureau` (la prise reste allumée pour le suivi conso).

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| `bouton_mqtt` | `mqtt` | `zigbee2mqtt2/Poussoir PC (IKEA TRADFRI)/action` |
| `veille` | `state` | `binary_sensor.veille_pc_bureau` = on pendant 12 min |
| `rattrapage` | `time_pattern` | toutes les 15 min (filet si le trigger veille ne se réarme pas) |

---

## ⚙️ Actions - Choose

**ALLUMAGE (bouton ON) :**
- `trigger.payload == 'on'`
- `light.turn_on → light.hue_smart_eco_pc_bureau`
- Notification `Allumage PC` / `PC Bureau [ON]`

**EXTINCTION (veille confirmée) :**
- Déclencheur `veille` ou `rattrapage`, ET lumière allumée, ET veille ≥ 12 min
  (garde anti-fantôme + vérification sur durée réelle)
- `light.turn_off → light.hue_smart_eco_pc_bureau`
- Notification `Veille détectée` / `PC Bureau [OFF]`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt2/Poussoir PC (IKEA TRADFRI)/action` | Bouton physique |
| `sensor.prise_bureau_pc_ikea_power` | Puissance PC (IKEA) - source du binaire |
| `binary_sensor.veille_pc_bureau` | Veille confirmée (template : puissance < 70W) |
| `light.hue_smart_eco_pc_bureau` | Éclairage bureau PC |
| `sensor.eco_prises_spy_pc_tv` | Spy de contrôle PC+TV (veille, coupures ratées) |

### Notifications

| Titre | Message |
|:---|:---|
| `Allumage PC` | `PC Bureau [ON]` (tag: notif_pc_bureau, icône: mdi:monitor-dashboard) |
| `Veille détectée` | `PC Bureau [OFF]` (tag: notif_pc_bureau) |

---

## ⚠️ Notes techniques

- Topic : `zigbee2mqtt2` (LXC 200) - pas `zigbee2mqtt`.
- `mode: single` : une seule exécution à la fois.
- Le bouton IKEA : seule l'action `on` est écoutée (l'extinction passe par la veille,
  comme avant la refonte).
- **Refonte 2026-09-23** (cause : coupures aléatoires) : les pics de veille réels du PC
  (43-44W) dépassaient l'ancien seuil 40W et annulaient la coupure ; la fenêtre d'attente
  de 10 min était réinitialisée par chaque micro-pic. Remplacé par : binaire dédié < 70W
  (au-dessus des pics ~45W, sous l'actif ~100W+), confirmation 12 min sur durée RÉELLE,
  filet de rattrapage 15 min, garde anti-fantôme (n'agit que si la prise est allumée).
