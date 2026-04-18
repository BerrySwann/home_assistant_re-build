# GESTION OPTIMISÉE DU STORE BUREAU

> **Fichier :** `automations_corrige/stores/gestion_store_bureau.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Pilotage automatique du store bureau selon 3 scénarios : ouverture travail
(T° ext 18–25°C), fermeture chaleur (> 25°C), fermeture nuit (coucher soleil).
Sécurité absolue : aucun mouvement si fenêtre ouverte.

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| `reveil` | `time` | 07:00:00 |
| — | `state` | `sensor.th_balcon_nord_temperature` |
| — | `sun` | sunset |
| `fenetre` | `state` | `binary_sensor.contact_fenetre_bureau_sonoff_contact → off` |

---

## 🔒 Conditions globales

- `binary_sensor.contact_fenetre_bureau_sonoff_contact == off` (fenêtre fermée)

---

## ⚙️ Scénarios — Choose

| Scénario | Condition | Action |
|:---|:---|:---|
| A — Ouverture travail | Après 07:00, avant sunset, T° 18–25°C, store fermé | `cover.open_cover` |
| B — Fermeture chaleur | T° > 25°C, avant sunset | `cover.close_cover` |
| C — Fermeture nuit | Après sunset | `cover.close_cover` |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.th_balcon_nord_temperature` | T° ext pour scénarios A et B |
| `binary_sensor.contact_fenetre_bureau_sonoff_contact` | Sécurité fenêtre |
| `cover.store_bureau` | Volet motorisé bureau |
| `sun.sun` | Lever/coucher soleil |
