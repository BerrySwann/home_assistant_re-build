# DIAG - ENREGISTREMENT JOURNALIER (7 POSTES + DUT)

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

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P0_ENRIGE/diag_enregistrement_journalier/diag_enregistrement_journalier.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Log toutes les 15 min la consommation des 7 postes fonctionnels, la présence,
la température intérieure moyenne, la T° extérieure et les DUT des 4 équipements
de chauffage (Salon/Radiateur/Bureau/Chambre) dans un fichier de log.

---

## ⚡ Déclencheurs

| Type | Pattern |
|:---|:---|
| `time_pattern` | `minutes: /15` |

---

## ⚙️ Actions

- `notify.send_message → notify.file_diag_log_file` avec ligne formatée :
  `[pres] | DD/MM HH:MM | Hyg:X | Cuis:X | Froid:X | Chauff:X | Avg 4:X | Multi:X | Lum:X | Autres:X | Ti:X°C | Ext:X°C | DUT S/R/B/C:X/X/X/X`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.presence` | Présence groupe (groupe_1 à groupe_4) |
| `sensor.diag_poste_hygiene_quotidien` | Poste 1 kWh |
| `sensor.diag_poste_cuisine_quotidien` | Poste 2 kWh |
| `sensor.diag_poste_froid_quotidien` | Poste 3 kWh |
| `sensor.diag_poste_chauffage_quotidien` | Poste 4 kWh |
| `sensor.clim_rad_total_avg_watts_quotidien` | AVG watts P1 |
| `sensor.diag_poste_multimedia_quotidien` | Poste 5 kWh |
| `sensor.diag_poste_eclairage_quotidien` | Poste 6 kWh |
| `sensor.diag_poste_autre_quotidien` | Poste 7 kWh |
| `sensor.th_balcon_nord_temperature` | T° ext |
| `sensor.temperature_moyenne_interieure` | T° int moyenne |
| `sensor.dut_clim_salon` | DUT salon |
| `sensor.dut_radiateur_cuisine` | DUT cuisine |
| `sensor.dut_clim_bureau` | DUT bureau |
| `sensor.dut_clim_chambre` | DUT chambre |
| `notify.file_diag_log_file` | Service log fichier (intégration File UI) |
