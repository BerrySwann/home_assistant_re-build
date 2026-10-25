# (G) NOTIFICATION CHANGEMENT DE MODE ÉTÉ/FAN/HIVER

> **Fichier :** `docs/03_docs_automations/03_docs_automations_yaml/P1_01_CLIM_CHAUFFAGE/g_clim_notification_de_changement_de_mode_ete_fan_hiver/g_clim_notification_de_changement_de_mode_ete_fan_hiver.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Simple notification lors d'un changement de saison (heat / cool / fan_only).
Lit `sensor.mode_ete_hiver_etat` pour un texte lisible.

---

## ⚡ Déclencheurs

| Type | Entité |
|:---|:---|
| `state` | `sensor.mode_ete_hiver` |

---

## ⚙️ Actions

1. Pause 3s
2. Notification `CHANGEMENT DE MODE` avec `sensor.mode_ete_hiver_etat | upper`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.mode_ete_hiver` | Déclencheur |
| `sensor.mode_ete_hiver_etat` | Texte lisible du mode |
