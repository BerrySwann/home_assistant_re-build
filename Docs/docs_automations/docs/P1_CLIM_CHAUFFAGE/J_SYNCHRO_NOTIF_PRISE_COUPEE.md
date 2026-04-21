# (J) SYNCHRO & NOTIF CLIM SI PRISE COUPÉE

> **Fichier :** `automations_corrige/P1_clim_chauffage/J_synchro_notif_prise_coupee.yaml`
> **Mode HA :** `parallel`

---

## 📝 Description

Quand une prise clim est coupée manuellement (ON→OFF), force immédiatement
l'entité `climate` correspondante à `off` (synchro état HA) et notifie
si on est en période diurne.

---

## ⚡ Déclencheurs

| Type | Entité | Transition |
|:---|:---|:---|
| `state` | `switch.clim_salon_nous` | `on → off` |
| `state` | `switch.clim_bureau_nous` | `on → off` |
| `state` | `switch.clim_chambre_nous` | `on → off` |

---

## ⚙️ Actions

1. `climate.set_hvac_mode: off` sur la clim correspondante (résolu via `trigger.entity_id`)
2. Si 07:30–21:00 → notification `CLIM COUPÉE` avec pièce identifiée

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `switch.clim_salon/bureau/chambre_nous` | Déclencheurs |
| `climate.clim_salon/bureau/chambre_rm4_mini` | Cibles synchro |
