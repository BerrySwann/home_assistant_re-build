# UPDATE PREVIOUS TEMPERATURE - TENDANCE T° EXT

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

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Meteo/update_previous_temperature/update_previous_temperature.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Snapshot de la température extérieure toutes les 30 min dans un `input_number`.
Utilisé pour calculer la tendance (hausse/baisse/stable) dans les sensors templates.

---

## ⚡ Déclencheurs

| Type | Pattern |
|:---|:---|
| `time_pattern` | `minutes: /30` |

---

## ⚙️ Actions

- `input_number.set_value → input_number.th_balcon_nord_temperature_previous`
  valeur = `sensor.th_balcon_nord_temperature | float(0)`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.th_balcon_nord_temperature` | Source T° ext |
| `input_number.th_balcon_nord_temperature_previous` | Helper snapshot |
