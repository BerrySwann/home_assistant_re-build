# SYSTÈME - ÉCONOMIE ÉNERGIE VS CODE

> **Fichier :** `docs/03_docs_automations/03_docs_automations_yaml/Mariadb_et_vscode_optimisation/systeme_economie_energie_vs_code/systeme_economie_energie_vs_code.yaml`
> **ID HA :** `1773253636237` (`automation.systeme_economie_energie_vs_code`)
> **Mode HA :** `single`
> **MàJ :** 2026-10-11 (fiche réécrite d'après le YAML, identique à H:\automations.yaml)

---

## Description

Coupe l'add-on VS Code (Studio Code Server) pour économiser l'énergie du mini-PC, après confirmation sur le téléphone d'Eric. Description HA : "Coupe VS Code si son CPU dépasse 10% ou s'il est inactif, avec confirmation (H24)". Les deux déclencheurs mesurent le CPU de VS Code lui-même (pas le CPU global du mini-PC).

---

## Déclencheurs

| ID | Type | Entité | Seuil | Durée |
|:---|:---|:---|:---|:---|
| `high_cpu` | `numeric_state` | `sensor.studio_code_server_pourcentage_du_processeur` | au-dessus de 10 % | 10 min |
| `inactive` | `numeric_state` | `sensor.studio_code_server_pourcentage_du_processeur` | en dessous de 0,8 % | 15 min |

---

## Conditions

- `binary_sensor.studio_code_server_en_cours_d_execution` est `on` (VS Code tourne).

---

## Actions

1. `choose` selon le déclencheur : notification à `notify.mobile_app_eric` avec deux boutons `STOP_VSC` ("Oui, couper") et `KEEP_VSC` ("Non, ignorer").
   - `high_cpu` : titre "ALERTE VSC CPU", message "CPU VSC >10% dps 10m. Le couper pour economiser ?"
   - `inactive` : titre "ALERTE VSC INAC", message "VSC inactif dps 15m. Le couper pour economiser ?"
2. `wait_for_trigger` : événement `mobile_app_notification_action` avec l'action `STOP_VSC` ou `KEEP_VSC`, délai 5 min, `continue_on_timeout: true`.
3. `choose` sur la réponse :
   - STOP ou délai dépassé (`wait.trigger == none`) : `hassio.addon_stop` sur `a0d7b954_vscode`, puis notification "VSC ARRETE" ("Arret auto VSC OK. (Economie energie).").
   - KEEP : `stop` ("L'utilisateur code encore, on laisse tourner.").

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `sensor.studio_code_server_pourcentage_du_processeur` | CPU de l'add-on VS Code (les deux déclencheurs) |
| `binary_sensor.studio_code_server_en_cours_d_execution` | VS Code tourne ? (condition) |
| `notify.mobile_app_eric` | Notifications avec boutons (seul Eric est notifié) |
| `hassio.addon_stop` (add-on `a0d7b954_vscode`) | Arrêt de VS Code |

---

## Notes

- Quand VS Code est arrêté, le capteur de CPU passe `unavailable` et la condition `en_cours_d_execution` est `off` : l'automation ne se déclenche pas.
- Cas "inactif" : l'automation se déclenche dès que le CPU reste sous 0,8 % pendant 15 min, ce qui est l'état normal d'un VS Code ouvert sans activité.
- Les anciens noms d'entités cités par l'ancienne fiche (`sensor.system_monitor_utilisation_du_processeur` comme déclencheur, `sensor.studio_code_server_cpu_percent`, `binary_sensor.studio_code_server_running`) ne sont pas ceux du YAML ; les deux derniers n'existent pas dans HA.