# 📦 ARCHIVE — FANTÔMES « ORPHELINS DE CONFIG » (2026-09-20)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Archive-9e9e9e?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-README-ff9800?style=flat-square)](.)

</div>

*Archivé le 2026-09-20 — purgés du registre HA le même jour (GO Berry).*

## Ce que c'est
9 entités restées au registre HA **sans plus aucune définition** dans la config (vérifiées une à une
par croisement registre ↔ fichiers YAML). Leurs fonctions vivent ailleurs, ou sont obsolètes :

| Entité | Plateforme | Créée | Statut |
|:-------|:-----------|:------|:-------|
| `sensor.genelec_appart_*_kwh_um` ×4 | utility_meter | 18/04 | Renommage d'avril `_kwh_um`→`_um` — les vivants = `sensor.genelec_appart_{quotidien,hebdomadaire,mensuel,annuel}_um` |
| `automation.energie_reset_complet_des_utility_meters` | automation | 28/04 | Outil **one-shot** de la migration d'avril — obsolète |
| `automation.diag_enregistrement_journalier_7_postes_dut` | automation | 29/04 | Remplacée par la version vivante `..._dut_2` (id 1780243175281, tourne) |
| `automation.sdb_watchdog_synchronisation_lumieres` | automation | 24/05 | **v1** de la sync SdB — remplacée par `P3_SDB - SYNC MIROIR LAMPE ET RELAIS SDB` (id 1780200461358, tourne) |
| `sensor.audit_md5_docs_journal` + `script.audit_md5_docs` | command_line / script | 07/08 | Remplacés le 09/08 par le système `audit_md5_md_yaml` |

## Contenu
- `registre_ha_2026-09-20.json` — entrées de registre complètes, telles qu'avant purge.

## Note
Les définitions YAML de certaines de ces entités avaient déjà disparu (30/05 & 09/08) — l'archive
conserve ce qui restait : les entrées de registre et l'historique ci-dessus.
