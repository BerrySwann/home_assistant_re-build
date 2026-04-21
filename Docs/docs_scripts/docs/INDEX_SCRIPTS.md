<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--04--19-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Index_Scripts-ff9800?style=flat-square)](.)

</div>

# ⚙️ INDEX SCRIPTS — NŒUD MASTER

> Fichier source : `scripts.yaml` (géré via UI HA, ne pas éditer directement)

---

## 📋 INVENTAIRE

| N° | Alias HA | Script ID | Doc |
|----|----------|-----------|-----|
| J 1-1 | `J 1-1 SALON - CLIM ON/OFF INTELLIGENT` | `j_1_1_salon_clim_on_off_intelligent` | [[SCRIPTS_CLIM_ON_OFF]] |
| J 1-2 | `J 1-2 BUREAU - CLIM ON/OFF INTELLIGENT` | `j_1_2_bureau_clim_on_off_intelligent` | [[SCRIPTS_CLIM_ON_OFF]] |
| J 1-3 | `J 1-3 CHAMBRE - CLIM ON/OFF INTELLIGENT` | `j_1_3_chambre_clim_on_off_intelligent` | [[SCRIPTS_CLIM_ON_OFF]] |
| J 2-0 | `J 2-0 SECU - ARRÊT CLIM PROTÉGÉ` | `j_2_0_secu_arret_clim_protege` | [[SCRIPT_J2_0_SECU_ARRET_CLIM]] |

---

## 🏗️ ARCHITECTURE GLOBALE

```
Dashboard tap_action
    │
    ├── J 1-1  script.j_1_1_salon_clim_on_off_intelligent   (Salon — mode: single)
    ├── J 1-2  script.j_1_2_bureau_clim_on_off_intelligent  (Bureau — mode: single)
    └── J 1-3  script.j_1_3_chambre_clim_on_off_intelligent (Chambre — mode: single)
            │
            ON  → switch.clim_<piece>_nous → ON  (direct)
            OFF → J 2-0  script.j_2_0_secu_arret_clim_protege  (mode: parallel, max: 3)
                        → protection thermique, attente < 9W, timeout 10 min
```

---

## 📁 DOCS DÉTAILLÉES

- [[SCRIPTS_CLIM_ON_OFF]] — Routeurs J 1-1 / J 1-2 / J 1-3 (anti-tremblote, tap_action)
- [[SCRIPT_J2_0_SECU_ARRET_CLIM]] — Exécutant J 2-0 (protection thermique, coupure propre)

---

<!-- obsidian-wikilinks -->
---
*Liens : [[SCRIPTS_CLIM_ON_OFF]]  [[SCRIPT_J2_0_SECU_ARRET_CLIM]]*
