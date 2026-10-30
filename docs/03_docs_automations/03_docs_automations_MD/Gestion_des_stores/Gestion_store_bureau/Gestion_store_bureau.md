# GESTION OPTIMISÉE DU STORE BUREAU

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Gestion_des_Stores/gestion_optimisee_du_store_bureau/gestion_optimisee_du_store_bureau.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Pilotage automatique du store bureau selon 3 scénarios : ouverture travail
(T° ext 18–25°C), fermeture chaleur (> 25°C), fermeture nuit (coucher soleil).
Sécurité absolue : aucun mouvement si fenêtre ouverte.

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| `reveil` | `time` | 07:00:00 |
| - | `state` | `sensor.th_balcon_nord_temperature` |
| - | `sun` | sunset |
| `fenetre` | `state` | `binary_sensor.contact_fenetre_bureau_sonoff_contact → off` |

---

## 🔒 Conditions globales

- `binary_sensor.contact_fenetre_bureau_sonoff_contact == off` (fenêtre fermée)

---

## ⚙️ Scénarios - Choose

| Scénario | Condition | Action |
|:---|:---|:---|
| A - Ouverture travail | Après 07:00, avant sunset, T° 18–25°C, store fermé | `cover.open_cover` |
| B - Fermeture chaleur | T° > 25°C, avant sunset | `cover.close_cover` |
| C - Fermeture nuit | Après sunset | `cover.close_cover` |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.th_balcon_nord_temperature` | T° ext pour scénarios A et B |
| `binary_sensor.contact_fenetre_bureau_sonoff_contact` | Sécurité fenêtre |
| `cover.store_bureau` | Volet motorisé bureau |
| `sun.sun` | Lever/coucher soleil |
