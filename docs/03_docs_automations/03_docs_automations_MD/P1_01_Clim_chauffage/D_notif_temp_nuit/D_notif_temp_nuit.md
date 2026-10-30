# (D) NOTIFICATION TEMPÉRATURE - NUIT (21H00 → 07H30)

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

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/d_notification_temperature_up_ou_down_21h00_7h30/d_notification_temperature_up_ou_down_21h00_7h30.yaml`
> **Mode HA :** `queued`

---

## 📝 Description

Miroir nocturne de D. Même logique mais sur la plage 21h00–07h30 et
avec `sensor.message_clim_personnalise_21h00_7h30`.

---

## ⚡ Déclencheurs

| Type | Entité |
|:---|:---|
| `state` | `sensor.th_balcon_nord_temperature` |
| `time` | 21:00:00 |

---

## ⚙️ Actions

1. Pause 2s
2. Si capteurs KO → `[ANN] Erreur Capteurs`
3. Sinon → `[Automa. Notif. Nuit]` avec contenu du sensor nuit

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.th_balcon_nord_temperature` | Déclencheur |
| `sensor.message_clim_personnalise_21h00_7h30` | Message nuit |
| `sensor.mamour_wi_fi_connection` | Vérification |
| `sensor.eric_wi_fi_connection` | Vérification |
