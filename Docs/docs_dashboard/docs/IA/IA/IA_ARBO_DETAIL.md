# 🌳 ARBORESCENCES COMPLÈTES & INDEX GITHUB
*Dernière mise à jour : 2026-06-19*
*Lire ce fichier si : audit fichiers, sync GitHub, recherche d'un fichier prod, vérification arbo locale.*

---

## 🌳 ARBORESCENCE — DOSSIER LOCAL ReBuild/ (DÉTAILLÉE)

```text
ReBuild/                                         (C:\Users\Berry Swann\Documents\HA\ReBuild\)
├── CLAUDE.md
├── README.md / SYNC_REPORT.md
├── INDEX_NAVIGATION.md                          (index 18 vignettes dashboard — accordéon GitHub)
├── INDEX_AUTOMATIONS.md                         (index 48 automations — accordéon GitHub)
├── secrets.yaml                                 (NE JAMAIS synchroniser)
├── Analyse énergétique/                         (analyses ad-hoc conso électrique)
├── HTML/                                        (export dashboard HTML)
├── IA/                                          (contexte IA — tous les IA_*.md)
│   ├── IA_CONTEXT_BASE.md
│   ├── IA_INTEGRATIONS_CARTES.md
│   ├── IA_AUTOMATIONS_NOTIFS.md
│   ├── IA_P4_PRESENCE.md
│   ├── IA_ARBO_DETAIL.md
│   ├── IA_INDEX_NAVIGATION.md                   (compétence index dashboard — régénération)
│   └── IA_INDEX_AUTOMATIONS.md                  (compétence index automations — régénération)
├── Infra/                                       (réseau — Proxmox.crt, reseau.md)
├── Orphelin/                                    (fichiers non rattachés)
├── historique/                                  (journal sessions — histo_*.txt, SESSION_LOG)
│
├── Dashboard/
│   ├── Dashboard_COMPLET/                       (dashboards complets — conservation illimitée)
│   ├── L1C1_01_Meteo/
│   ├── L1C2_02_Temperatures/
│   ├── L1C3_03_Commandes_Clim/
│   ├── L2C1_04_Energie_Generale/
│   ├── L2C2_05_Energie_Clim/
│   ├── L2C3_06_Energie_Eclairage/
│   ├── L3C1_07_Commandes_Eclairage/
│   ├── L3C2_08_Commandes_Prises/
│   ├── L3C3_09_Stores_Fenetres/
│   ├── L4C1_10_Proxmox/
│   ├── L4C2_11_Mini_PC/
│   ├── L4C3_12_MAJ_HA/
│   ├── L5C1_13_Batteries_Piles/
│   ├── L5C2_14_Batteries_Portables/
│   ├── L5C3_15_MariaDB/
│   ├── L6C1_16_Air_Qualite/
│   ├── L6C2_17_Pollution_Pollen/
│   ├── L6C3_18_VigiEau/
│   ├── PAGE_ENERGIE_ECLAIRAGE/
│   └── PAGE_RASPI/
│
├── docs_dashboard/
│   ├── TREE_CORRIGE/
│   │   ├── sensors/
│   │   ├── templates/                           (⚠️ Mini-PC/ présent mais vide — supprimé prod)
│   │   ├── utility_meter/
│   │   ├── command_line/
│   │   │   ├── audit/audit_logs.yaml            (sensor.audit_md5_journal — créé 2026-06-14)
│   │   │   ├── github_maintenance/github_maintenance.yaml
│   │   │   ├── ip_externe/ip_externe.yaml       (sensor.ip_externe — créé 2026-06-13)
│   │   │   └── meteo/carte_meteo_france.yaml
│   │   ├── packages/                            (nouveau — créé 2026-06-17)
│   │   │   ├── cssmeteo.yaml                    (REST sensor Moon API / ipgeolocation)
│   │   │   └── demometeo.yaml                   (input_select démo météo — non inclus config)
│   │   ├── shell_command/                       (monolithique shell_command.yaml → découpé 2026-06-17)
│   │   │   ├── Ghithub/backup_github.yaml
│   │   │   └── P4/P4_log_eric_zone.yaml
│   │   ├── input_booleans/
│   │   ├── input_number/
│   │   ├── groups/                              (GRP_01_batteries_hue / GRP_02_ikea / GRP_03_sonoff)
│   │   └── [root]                               (configuration.yaml, scripts.yaml, sql.yaml, scenes.yaml, input_button.yaml, input_datetime.yaml, input_select.yaml, automations.yaml)
│   ├── TREE_ORIGINE/
│   └── docs/
│       ├── IA/
│       │   ├── IA_CONTEXT_BASE.md
│       │   └── analyse_energetique_appart.md
│       ├── CONFIG_ROOT/CONFIG_ROOT.md
│       ├── MOC_DASHBOARD.md
│       ├── INDEX_PAGES.md
│       ├── L1C1_METEO/ … L6C3_VIGIEAU/         (voir arbo CLAUDE.md)
│       ├── L4C1_FREEBOX/                        (SUPPRIMÉ 2026-06-18 — Freebox retirée du setup)
│       ├── L4C1_PROXMOX/                        (vignette + page finalisées — PVE/HA/Z2M/MariaDB/MED — déploiement #10)
│       ├── HOME PAGE/PAGE_HOME.md + VIGNETTE_WIFI_PRESENCE.md
│       ├── DEPENDANCES_GLOBALES.md
│       ├── WORKFLOW_REBUILD.md
│       └── _TEMPLATE_DOC.md
│
├── docs_automations/
│   ├── TREE_CORRIGE/
│   │   ├── P1_clim_chauffage/                   (11 fichiers A0→L + old/)
│   │   ├── P1_cuisine/                          (2 fichiers)
│   │   ├── P1_sdb/                              (3 fichiers : A_soufflant, D_watchdog, E_minuterie)
│   │   ├── P2_prises/                           (3 fichiers actifs : eco_prises_dynamique / gestion_pc_bureau / gestion_tv_chambre)
│   │   ├── P3_eclairage/                        (5 fichiers : entree + rodret + 3×bureau watchdog/play/ecran)
│   │   ├── raspi/                               (1 fichier — Raspberry Pi4 archivé, conservé)
│   │   ├── P2_bouton_rodret_soufflant_sdb.yaml  (⚠️ mal placé à la racine — à ranger)
│   │   ├── P3_salon_bouton_inter_ikea_4.yaml
│   │   ├── P3_salon_bouton_inter_somrig.yaml
│   │   ├── backup/                              (6 fichiers : hourly/weekly/daily/alerte/push_manuel/push_weekly_manuel)
│   │   ├── energie/                             (3 fichiers : basculement_hphc/log_ecart_linky/surveillance_electro)
│   │   ├── meteo/                               (5 fichiers)
│   │   ├── stores/                              (2 fichiers)
│   │   └── systeme/                             (6 fichiers : db/vscode/veille_github/watchdog_piles/z2m/diag)
│   ├── TREE_ORIGINE/
│   └── docs/
│       ├── INDEX_AUTOMATIONS.md                 (index accordéon 48 automations)
│       ├── AUTOMATIONS/ BACKUP/ ENERGIE/ METEO/ (docs par catégorie)
│       ├── P1_CLIM_CHAUFFAGE/ P1_CUISINE/ P1_SDB/
│       ├── P2_PRISES/ P3_ECLAIRAGE/ RASPI/
│       ├── STORES/ SYSTEME/
│       └── AUTOMATIONS_IDS_REF.md / TRIAGE / PROD_vs_REBUILD_DIFF
│
└── docs_scripts/
    ├── TREE_CORRIGE/
    │   ├── .scripts/audit_md5.sh               (copie versionnée depuis prod — synchro GitHub 2026-06-19)
    │   └── A_rpi_fan_pwm_6_states.yaml
    ├── TREE_ORIGINE/
    └── docs/                                    (INDEX_SCRIPTS.md, SCRIPTS_CLIM_ON_OFF.md, SCRIPT_J2_0_SECU_ARRET_CLIM.md)
```

---

## 🌳 ARBORESCENCE — PRODUCTION /homeassistant/ (DÉTAILLÉE)

```text
/homeassistant/
├── configuration.yaml
├── automations.yaml
├── scripts.yaml
├── scenes.yaml
├── camera.yaml
├── input_button.yaml
├── sql.yaml
├── shell_command/                               (découpé 2026-06-17 — plus de shell_command.yaml monolithique)
│   ├── Ghithub/backup_github.yaml
│   └── P4/P4_log_eric_zone.yaml
├── packages/                                    (nouveau 2026-06-17)
│   └── cssmeteo.yaml                            (REST sensor Moon API / ipgeolocation)
├── groups/                                      (répertoire — !include_dir_merge_named)
│   ├── GRP_01_batteries_hue.yaml               (hue_devices — 11 sensors)
│   ├── GRP_02_batteries_ikea.yaml              (ikea_devices — 12 sensors)
│   └── GRP_03_batteries_sonoff.yaml            (sonoff_devices — 11 sensors)
├── #sensors.yaml   #templates.yaml   #utility_meter.yaml  (désactivés)
│
/homeassistant/ [INTÉGRATION FILE — UI UNIQUEMENT — notify.file interdit en YAML]
├── Notify [/homeassistant/.logs/zone_eric.txt]        → shell_command/P4/P4_log_eric_zone.yaml
├── Notify [/homeassistant/notifs/diag_conso_elec.txt]
└── Notify [/homeassistant/notifs/ecart_liky_vs_nodon.txt]
│
/homeassistant/command_line/
├── audit/audit_logs.yaml                        (sensor.audit_md5_journal — créé 2026-06-14)
├── github_maintenance/github_maintenance.yaml
├── ip_externe/ip_externe.yaml                   (sensor.ip_externe — curl ipify.org — créé 2026-06-13)
└── meteo/carte_meteo_france.yaml
│
/homeassistant/input_booleans/
├── P1/P1_ACS_IB_01_arret_clim_securises.yaml
├── P1/P1_BV_BI_02_inter_soufflant_sdb.yaml
├── P3/P3_BV_01_IB_inter_smorig_salon.yaml
├── P3/P3_BV_02_IB_inter_rodret_salon.yaml
└── P4/P4_presence_wifi.yaml
│
/homeassistant/utility_meter/
├── P0_Energie_total/Genelec_appart/
│   ├── 01_UM_AMHQ.yaml                        (Nodon — compteurs AMHQ globaux)
│   └── 02_UM_genelec_appart_HPHC_AMHQ.yaml   (HP/HC AMHQ)
├── P1_clim_chauffage/P1_UM_AMHQ.yaml
├── P2_prise/
│   ├── P2_UM_AMHQ_mini_pc.yaml               (✅ actif)
│   ├── P2_UM_AMHQ_prises.yaml                (✅ actif)
│   └── P2_UM_AMHQ_veilles.yaml               (✅ actif)
├── P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml      (seul actif — 2_ZONE et 3_TOTAL absents de prod)
└── meteo/M_03_meteo_UM_blitzortung.yaml
│
/homeassistant/templates/
├── P0_Energie_total_diag/
│   ├── Diag/ × 3 yaml (jour/mois/hebdo)
│   ├── Genelec_appart/ × 3 yaml (cost/ratio/avg)
│   ├── Linky/MyElectricalData.yaml
│   └── total_pour_les_7_postes/total_pour_les_7_postes.yaml
├── P1_clim_chauffage/ P1_01_MASTER + P1_AVG + P1_TOTAL + P1_DUT_TOTAL + P1_ui_dashboard
├── P2_prise/ P2_AVG + P2_I_all_standby_power + P2_ui_dashboard + P2_éCO_prises/P2_eco_prises_config.yaml
├── P3_eclairage/
│   ├── P3_ENERGIE_TPL/                        (⚠️ nom prod — pas P3_POWER, pas P3_ENERGIE_TLP)
│   │   ├── P3_TPL_AMHQ_1_UNITE.yaml           (76 sensors — 19 ampoules × 4 cycles)
│   │   ├── P3_TPL_AMHQ_2_ZONE.yaml            (40 sensors — 10 zones × 4 cycles)
│   │   └── P3_TPL_AMHQ_3_TOTAL.yaml           (4 sensors)
│   ├── P3_POWER_TPL/
│   │   └── P3_POWER_3_TOTAL_ZONE.yaml         (puissance totale zone — présent prod + TREE_CORRIGE)
│   ├── P3_AVG/ × 3 yaml
│   └── ui_dashboard/etats_status.yaml
├── P4_groupe_presence/ × 2 yaml
├── Air_quality/A_01_AIR_QUALITY.yaml
├── Stores/S_01_STORES.yaml
├── meteo/ × 5 yaml (M_01 → M_05)
├── Inter_BP_Virtuel/ P1 + P3
└── utilitaires/ × 3 yaml
                                               (⚠️ Mini-PC/ supprimé — capteurs proxmox_* pris à la source directemen