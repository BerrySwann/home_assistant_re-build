# [P3-SALON] BOUTON IKEA SOMRIG (2 TOUCHES) - ON/OFF

> **Fichier :** `P3_eclairage/p3_salon_bouton_ikea_somrig.yaml`
> **ID HA :** `1775387618751`
> **Mode HA :** `restart`
> **MàJ :** 2026-09-10

---

## 📝 Description

Même rôle que l'Inter IKEA 4 touches (`BOUTON_INTER_IKEA_4.md`) : pilotage direct de
`light.salon`, le groupe des 4 lampes du salon.

Différence : le SOMRIG est plus permissif — il réagit à **tous** les types d'appui,
sur chaque touche :
- **Touche 1** (clic simple, double clic, appui long) → allumage
- **Touche 2** (clic simple, double clic, appui long) → extinction

Comme l'autre bouton, il attaque directement `light.salon` (plus de helper
`input_boolean.inter_lumiere_salon` — montage disparu).

---

## ⚡ Déclencheurs

| ID | Type | Topic MQTT | Payload |
|:---|:---|:---|:---|
| `bouton_on` | `mqtt` | `zigbee2mqtt2/Inter (SOMRIG)/action` | `1_short_release` |
| `bouton_on` | `mqtt` | `zigbee2mqtt2/Inter (SOMRIG)/action` | `1_double_press` |
| `bouton_on` | `mqtt` | `zigbee2mqtt2/Inter (SOMRIG)/action` | `1_long_press` |
| `bouton_off` | `mqtt` | `zigbee2mqtt2/Inter (SOMRIG)/action` | `2_short_release` |
| `bouton_off` | `mqtt` | `zigbee2mqtt2/Inter (SOMRIG)/action` | `2_double_press` |
| `bouton_off` | `mqtt` | `zigbee2mqtt2/Inter (SOMRIG)/action` | `2_long_press` |

---

## ⚙️ Actions - Choose

| Cas | Résultat |
|:---|:---|
| N'IMPORTE QUEL APPUI BOUTON 1 → ALLUMER | `light.turn_on → light.salon` |
| N'IMPORTE QUEL APPUI BOUTON 2 → ÉTEINDRE | `light.turn_off → light.salon` |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt2/Inter (SOMRIG)/action` | Bouton physique (2 touches) |
| `light.salon` | Groupe des 4 lampes du salon |

---

## ⚠️ Notes techniques

- Topic `zigbee2mqtt2` (LXC 200), pas `zigbee2mqtt`.
- Les 6 payloads (3 types d'appui × 2 touches) déclenchent tous la même action binaire.
- Doublon fonctionnel assumé avec `BOUTON_INTER_IKEA_4.md` : deux boutons physiques
  pour la même lumière du salon.
- `mode: restart` : un nouvel appui annule l'exécution en cours.

---
*MàJ 2026-09-10 — fiche réalignée sur l'automation live (cible `light.salon`, topic `zigbee2mqtt2`, 6 payloads, plus de helper).*
