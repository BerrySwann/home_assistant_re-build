# METTRE À JOUR LE TEMPS DU DERNIER IMPACT FOUDRE

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Meteo/mettre_a_jour_le_temps_du_dernier_impact_de_foudre/mettre_a_jour_le_temps_du_dernier_impact_de_foudre.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Enregistre l'heure exacte du dernier impact de foudre dans `input_datetime.dernier_eclair`
à chaque changement du compteur Blitzortung.

---

## ⚡ Déclencheurs

| Type | Entité |
|:---|:---|
| `state` | `sensor.maison_lightning_counter` |

---

## 🔒 Conditions

- `sensor.maison_lightning_counter | int > 0`

---

## ⚙️ Actions

- `input_datetime.set_datetime` → `input_datetime.dernier_eclair` = `now().isoformat()`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.maison_lightning_counter` | Compteur impacts Blitzortung |
| `input_datetime.dernier_eclair` | Helper datetime dernier éclair |
