# (E) NOTIFICATION FERMETURE DES FENÊTRES

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-ff9800?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/e_clim_notification_de_fermeture_des_fenetres/e_clim_notification_de_fermeture_des_fenetres.yaml`
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
