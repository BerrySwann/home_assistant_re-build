# (C) GARDIEN ÉCO — COUPURE CLIM SI DELTA T < -1°C

> **Fichier :** `automations_corrige/P1_clim_chauffage/C_gardien_eco.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Module de sécurité écologique. Coupe automatiquement les clims si la température
extérieure est déjà plus haute que le seuil de non-chauffage ET que le Delta T
intérieur/extérieur est négatif depuis 10 minutes. Évite de chauffer inutilement
quand la météo fait le travail.

---

## ⚡ Déclencheurs

| Type | Entité | Condition |
|:---|:---|:---|
| `numeric_state` | `sensor.temperature_delta_valeur` | `< -1` pendant 10 min |

---

## 🔒 Conditions

- Plage horaire : `07:30–21:00`
- `sensor.th_balcon_nord_temperature > sensor.seuil_non_chauffage_bas`
- `sensor.th_balcon_nord_temperature < 25`
- Au moins une clim dans un état actif (cool/heat/fan_only/dry/auto)

---

## ⚙️ Actions

- Pour chaque clim active : `climate.set_hvac_mode → off`
- Notification : titre `Delta T° < -1°C`, message avec valeurs delta, T° ext et seuil réglé

---

## 🔌 DÉPENDANCES

### Entités lues

| Entité                              | Rôle               |
| :---------------------------------- | :----------------- |
| `sensor.temperature_delta_valeur`   | Delta T° int/ext   |
| `sensor.th_balcon_nord_temperature` | T° extérieure      |
| `sensor.seuil_non_chauffage_bas`    | Seuil paramétrable |
| `climate.clim_salon_rm4_mini`       | État clim salon    |
| `climate.clim_bureau_rm4_mini`      | État clim bureau   |
| `climate.clim_chambre_rm4_mini`     | État clim chambre  |

### Entités pilotées

| Entité | Action |
|:---|:---|
| `climate.clim_salon_rm4_mini` | `set_hvac_mode: off` (si active) |
| `climate.clim_bureau_rm4_mini` | `set_hvac_mode: off` (si active) |
| `climate.clim_chambre_rm4_mini` | `set_hvac_mode: off` (si active) |

### Notifications

| Titre | Message |
|:---|:---|
| `Delta T° < -1°C` | Valeurs delta, T° ext, seuil |
