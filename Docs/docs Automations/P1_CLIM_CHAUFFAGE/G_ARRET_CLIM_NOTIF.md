# (G) ARRÊT CLIM — NOTIFICATION MANUELLE

> **Fichier :** `automations_corrige/P1_clim_chauffage/G_arret_clim_notif.yaml`
> **Mode HA :** `queued`

---

## 📝 Description

Notifie quand une clim passe à `off` manuellement (via télécommande ou UI),
mais uniquement si les prises sont actives et toutes les fenêtres fermées —
pour éviter les faux positifs lors des coupures automatiques.

---

## ⚡ Déclencheurs

| Type | Entité | État cible |
|:---|:---|:---|
| `state` | `climate.clim_salon_rm4_mini` | `off` |
| `state` | `climate.clim_bureau_rm4_mini` | `off` |
| `state` | `climate.clim_chambre_rm4_mini` | `off` |

---

## 🔒 Conditions

- 3 prises clim NOUS à `on`
- 4 capteurs fenêtres à `off` (toutes fermées)

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `climate.clim_salon_rm4_mini` / `bureau` / `chambre` | Déclencheurs |
| `switch.clim_salon_nous` / `bureau` / `chambre` | Conditions |
| 4× `binary_sensor.contact_fenetre_*` | Conditions |

### Notifications

| Titre | Message |
|:---|:---|
| `ARRÊT CLIM` | Pièce identifiée depuis `trigger.entity_id` |
