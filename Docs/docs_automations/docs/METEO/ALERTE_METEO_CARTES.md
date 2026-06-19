# ALERTE MÉTÉO FRANCE — ACTUALISATION DES CARTES

> **Fichier :** `automations_corrige/meteo/alerte_meteo_cartes.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Force la mise à jour des images d'alerte Météo France (aujourd'hui + demain).
Déclenché au démarrage, à 06:32 et 16:32, et toutes les 5 min si les capteurs
sont indisponibles (mécanisme de retry). Rafraîchit aussi les entités caméra finales.

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| `Start` | `homeassistant` | start |
| `Heure632` | `time` | 06:32:00 |
| `Heure1632` | `time` | 16:32:00 |
| `Toutesles5minutes` | `time_pattern` | `minutes: /5` |

---

## 🔒 Conditions

- `Start` ou `Heure632` ou `Heure1632` → toujours exécuter
- `Toutesles5minutes` → seulement si `sensor.meteo_france_alertes_image_today` ou `tomorrow` = `unavailable`

---

## ⚙️ Actions

1. `homeassistant.update_entity` (today + tomorrow images)
2. Pause 5s
3. Retry ×1 si today encore indisponible
4. Retry ×1 si tomorrow encore indisponible
5. `homeassistant.update_entity` → cameras `camera.mf_alerte_today` + `camera.mf_alerte_tomorrow`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.meteo_france_alertes_image_today` | Image alerte du jour |
| `sensor.meteo_france_alertes_image_tomorrow` | Image alerte demain |
| `camera.mf_alerte_today` | Caméra affichage aujourd'hui |
| `camera.mf_alerte_tomorrow` | Caméra affichage demain |
