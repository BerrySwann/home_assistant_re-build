# (F) NOTIFICATION FERMETURE DES FENÊTRES

> **Fichier :** `automations_corrige/P1_clim_chauffage/F_notif_fermeture_fenetres.yaml`
> **Mode HA :** `queued`

---

## 📝 Description

Notifie la fermeture d'une fenêtre. Précise la pièce concernée et indique
si toutes les fenêtres sont maintenant fermées (via `sensor.nbre_de_fenetres_fermees`).

---

## ⚡ Déclencheurs

| Type | Entité | Transition |
|:---|:---|:---|
| `state` | 4 capteurs fenêtres | `on → off` |

---

## ⚙️ Actions

1. Pause 2s
2. Notification avec pièce identifiée depuis `trigger.entity_id`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | Fenêtre salon |
| `binary_sensor.contact_fenetre_cuisine_sonoff_contact` | Fenêtre cuisine |
| `binary_sensor.contact_fenetre_bureau_sonoff_contact` | Fenêtre bureau |
| `binary_sensor.contact_fenetre_chambre_sonoff_contact` | Fenêtre chambre |
| `sensor.nbre_de_fenetres_fermees` | Compteur (message "toutes fermées") |

### Notifications

| Titre | Message |
|:---|:---|
| `Fermeture en cours` | Pièce identifiée + état global |
