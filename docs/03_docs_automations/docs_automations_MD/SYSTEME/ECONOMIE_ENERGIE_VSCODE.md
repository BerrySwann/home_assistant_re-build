# SYSTÈME — ÉCONOMIE ÉNERGIE VS CODE

> **Fichier :** `automations_corrige/systeme/economie_energie_vscode.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Coupe VS Code si le CPU global dépasse 10% pendant 10 min OU si VS Code
est inactif (< 0,8% CPU) depuis 15 min. Demande confirmation via notification
interactive avec boutons `Oui/Non`. Timeout 5 min → coupe auto.

---

## ⚡ Déclencheurs

| Type | Entité | Seuil | Durée |
|:---|:---|:---|:---|
| `numeric_state` | `sensor.system_monitor_utilisation_du_processeur` | > 10% | 10 min |
| `numeric_state` | `sensor.studio_code_server_cpu_percent` | < 0,8% | 15 min |

---

## 🔒 Conditions

- `binary_sensor.studio_code_server_running == on`

---

## ⚙️ Séquence

1. Notification `🔋 Alerte Énergie - Mini-PC` avec boutons `STOP_VSC` / `KEEP_VSC`
2. `wait_for_trigger` (actions mobiles ou timeout 5 min)
3. **STOP ou timeout** → `hassio.addon_stop (a0d7b954_vscode)` + notif confirmation
4. **KEEP** → `stop` (l'utilisateur travaille encore)

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.system_monitor_utilisation_du_processeur` | CPU global mini-PC |
| `sensor.studio_code_server_cpu_percent` | CPU VS Code addon |
| `binary_sensor.studio_code_server_running` | VS Code actif ? |
| `hassio.addon_stop` | Arrêt addon VS Code |
