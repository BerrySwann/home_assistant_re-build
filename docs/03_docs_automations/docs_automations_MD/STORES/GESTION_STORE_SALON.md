# GESTION OPTIMISÉE DU STORE SALON (ANTI-REFLET PC)

> **Fichier :** `automations_corrige/stores/gestion_store_salon.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Gestion multi-scénarios du store salon : canicule, anti-reflet PC (calcul
azimut/élévation solaire paramétrable), froid + absence, nuit.
Mode `default` → ouverture si aucun scénario ne correspond.

---

## ⚡ Déclencheurs

| ID | Type | Entités |
|:---|:---|:---|
| `re-evaluation` | `state` | `sensor.th_balcon_nord_temperature`, `sensor.groupe`, `sun.sun` |
| `fenetre` | `state` | `binary_sensor.contact_fenetre_salon_sonoff_contact` |
| `matin_soir` | `sun` | `sunrise` + `sunset` |

---

## 🔒 Conditions globales

- `binary_sensor.contact_fenetre_salon_sonoff_contact == off`

---

## ⚙️ Scénarios — Choose

| Scénario | Condition | Action |
|:---|:---|:---|
| 1 — Canicule > 34°C | T° > 34°C | G2/G4 → position 50% / sinon → fermeture totale |
| 2 — Anti-reflet PC | G2/G4 + azimut ∈ `input_number.soleil_azimut_*` + élévation ∈ `input_number.soleil_elevation_*` | position 30% |
| 3 — Froid < 17°C + sans Mamour | T° < 17°C + G1/G3 | `cover.close_cover` |
| 4 — Nuit | Après sunset | `cover.close_cover` |
| default | Tout autre cas | `cover.open_cover` |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.th_balcon_nord_temperature` | T° ext |
| `sensor.groupe` | Présence (G2/G4 = Mamour) |
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | Sécurité fenêtre |
| `cover.store_salon` | Volet motorisé salon |
| `sun.sun` | Azimut + élévation + lever/coucher |
| `input_number.soleil_azimut_debut` / `soleil_azimut_fin` | Fenêtre anti-reflet |
| `input_number.soleil_elevation_min` / `soleil_elevation_max` | Fenêtre anti-reflet |
