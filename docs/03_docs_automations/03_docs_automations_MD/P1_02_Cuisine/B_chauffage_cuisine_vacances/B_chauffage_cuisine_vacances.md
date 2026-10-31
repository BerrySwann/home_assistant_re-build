# (B) CHAUFFAGE CUISINE VACANCES

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-4fc3f7?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_02_Cuisine/b_chauffage_cuisine_vacances/b_chauffage_cuisine_vacances.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Version vacances du chauffage cuisine. Plage unique 06:00–08:30,
7 jours/7. Requiert la présence d'au moins Eric OU Mamour pour le démarrage et l'arrêt par température. Arrêt forcé à 08:30.

---

## ⚡ Déclencheurs

| Type | Entité / Horaire |
|:---|:---|
| `time` | 06:00:00 (id `demarrage`) |
| `time` | 08:30:00 (id `arret_force`, arrêt forcé) |
| `numeric_state` | `sensor.th_cuisine_temperature` < 19.9 |
| `numeric_state` | `sensor.th_cuisine_temperature` > 20.5 |

---

## 🔒 Conditions (dans choose)

- Arrêt forcé (08:30) : déclenché par l'id `arret_force`, sans condition de présence ni de température
- Démarrage et arrêt par température : Eric OU Mamour dans `zone.home`
- `06:00 < heure < 08:30`
- T° < 19,9° ou > 20,5°

---

## Actions - Choose

| Cas | Action |
|:---|:---|
| Arrêt forcé 08:30 | `climate.set_hvac_mode: off` + notif `/!\ RADIATEUR CUISINE est 'OFF' FORCE (Fin Vacances 8h30) /!\` |
| Température < 19,9 (06:00-08:30, présence) | `climate.set_hvac_mode: heat` + notif `/!\ Chauffage Cuisine 'ON' /!\` |
| Température > 20,5 (06:00-08:30, présence) | `climate.set_hvac_mode: off` + notif `/!\ Chauffage Cuisine 'OFF' /!\` |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.th_cuisine_temperature` | T° cuisine |
| `climate.radiateur_cuisine` | Radiateur |
| `person.eric` / `person.mamour` | Présence (au moins un des deux, OU) |
| `notify.mobile_app_eric` | Notifications |
