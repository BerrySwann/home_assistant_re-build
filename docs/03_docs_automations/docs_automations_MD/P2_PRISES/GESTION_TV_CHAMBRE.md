# GESTION TV CHAMBRE - SCÈNE DE FIN + NOTIF

> **Fichier :** `P2_prises/gestion_tv_chambre_scene_de_fin_notif.yaml`
> **ID HA :** `1775330762844`
> **Mode HA :** `single`
> **MàJ :** 2026-09-23 (refonte anti-raté)

---

## 📝 Description

Gestion du cycle TV chambre : allumage via bouton MQTT (Poussoir IKEA TRADFRI),
extinction sur veille CONFIRMÉE (puissance < 40W pendant 12 min via
`binary_sensor.veille_tv_chambre`). Pilote l'éclairage `light.hue_smart_eco_tv_chambre`
(la prise de mesure `switch.prise_tv_chambre_nous` reste allumée pour le suivi conso).

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| `bouton_mqtt` | `mqtt` | `zigbee2mqtt2/Poussoir TV (IKEA TRADFRI)/action` |
| `veille` | `state` | `binary_sensor.veille_tv_chambre` = on pendant 12 min |
| `rattrapage` | `time_pattern` | toutes les 15 min (filet si le trigger veille ne se réarme pas) |

---

## ⚙️ Actions - Choose

**ALLUMAGE (bouton ON) :**
- `trigger.payload == 'on'`
- `light.turn_on → light.hue_smart_eco_tv_chambre`
- `switch.turn_on → switch.prise_tv_chambre_nous` (prise de mesure)
- Notification `Allumage TV` / `Prise TV [ON]`

**EXTINCTION (veille confirmée) :**
- Déclencheur `veille` ou `rattrapage`, ET lumière allumée, ET veille ≥ 12 min
  (garde anti-fantôme + vérification sur durée réelle)
- `light.turn_off → light.hue_smart_eco_tv_chambre`
- Notification `Veille détectée` / `Prise TV [OFF]`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt2/Poussoir TV (IKEA TRADFRI)/action` | Bouton physique |
| `sensor.prise_tv_chambre_nous_power` | Puissance TV (NOUS) - source du binaire |
| `binary_sensor.veille_tv_chambre` | Veille confirmée (template : puissance < 40W) |
| `light.hue_smart_eco_tv_chambre` | Éclairage ambiance TV chambre (prise éco) |
| `switch.prise_tv_chambre_nous` | Prise de mesure (ON à l'allumage, laissée allumée) |
| `sensor.eco_prises_spy_pc_tv` | Spy de contrôle PC+TV (veille, coupures ratées) |

### Notifications

| Titre | Message |
|:---|:---|
| `Allumage TV` | `Prise TV [ON]` (tag: notif_tv_chambre, icône: mdi:television-off) |
| `Veille détectée` | `Prise TV [OFF]` (tag: notif_tv_chambre) |

---

## ⚠️ Notes techniques

- Topic : `zigbee2mqtt2` (LXC 200) - pas `zigbee2mqtt`.
- `mode: single` : une seule exécution à la fois.
- Le bouton IKEA : seule l'action `on` est écoutée (l'extinction passe par la veille,
  comme avant la refonte).
- **Refonte 2026-09-23** (cause : prise restée allumée jusqu'à ~19 h) : l'ancien trigger
  ne réagissait qu'au FRANCHISSEMENT du seuil (< 25W / 2 min) ; si la coupure était ratée
  (ou le seuil déjà franchi), plus rien ne déclenchait. Remplacé par : binaire dédié < 40W
  (au-dessus de la veille ~20W, sous l'actif ~70W+), confirmation 12 min sur durée RÉELLE,
  filet de rattrapage 15 min, garde anti-fantôme (n'agit que si la prise est allumée).
