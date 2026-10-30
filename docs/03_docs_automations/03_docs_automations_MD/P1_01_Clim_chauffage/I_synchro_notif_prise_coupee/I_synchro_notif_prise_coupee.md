# (I) SYNCHRO & NOTIF CLIM SI PRISE COUPÉE

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/i_synchro_notif_clim_si_prise_coupee/i_synchro_notif_clim_si_prise_coupee.yaml`
> **Mode HA :** `parallel`

---

## 📝 Description

Quand une prise clim est coupée manuellement (ON→OFF), force immédiatement
l'entité `climate` correspondante à `off` (synchro état HA) et notifie
si on est en période diurne.

---

## ⚡ Déclencheurs

| Type | Entité | Transition |
|:---|:---|:---|
| `state` | `switch.clim_salon_nous` | `on → off` |
| `state` | `switch.clim_bureau_nous` | `on → off` |
| `state` | `switch.clim_chambre_nous` | `on → off` |

---

## ⚙️ Actions

1. `climate.set_hvac_mode: off` sur la clim correspondante (résolu via `trigger.entity_id`)
2. Si 07:30–21:00 → notification `CLIM COUPÉE` avec pièce identifiée

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `switch.clim_salon/bureau/chambre_nous` | Déclencheurs |
| `climate.clim_salon/bureau_rm4_mini` + `clim_chambre_rm4_mini` | Ci