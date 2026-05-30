# 🌳 ARBORESCENCES COMPLÈTES & INDEX GITHUB
*Lire ce fichier si : audit fichiers, sync GitHub, recherche d'un fichier prod, vérification arbo locale.*

---

## 🌳 ARBORESCENCE — DOSSIER LOCAL ReBuild/ (DÉTAILLÉE)

```text
ReBuild/                                         (C:\Users\Berry Swann\Documents\HA\ReBuild\)
├── CLAUDE.md
├── README.md / SYNC_REPORT.md
├── secrets.yaml                                 (NE JAMAIS synchroniser)
├── Analyse énergétique/                         (analyses ad-hoc conso électrique)
├── HTML/                                        (export dashboard HTML)
├── IA/                                          (contexte IA — tous les IA_*.md)
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
│   │   ├── templates/
│   │   ├── utility_meter/
│   │   ├── command_line/
│   │   ├── input_booleans/
│   │   ├── input_number/
│   │   ├── groups/                              (GRP_01_batteries_hue / GRP_02_ikea / GRP_03_sonoff)
│   │   └── [root]                               (configuration.yaml, scripts.yaml, shell_command.yaml, sql.yaml, scenes.yaml, input_button.yaml, input_datetime.yaml, input_select.yaml, automations.yaml)
│   ├── TREE_ORIGINE/
│   └── docs/
│       ├── IA/
│       │   ├── IA_CONTEXT_BASE.md
│       │   └── analyse_energetique_appart.md
│       ├── CONFIG_ROOT/CONFIG_ROOT.md
│       ├── MOC_DASHBOARD.md
│       ├── INDEX_PAGES.md
│       ├── L1C1_METEO/ … L6C3_VIGIEAU/         (voir arbo CLAUDE.md)
│       ├── L4C1_PROXMOX/L4C1_VIGNETTE_PROXMOX.md
│       ├── HOME PAGE/PAGE_HOME.md + VIGNETTE_WIFI_PRESENCE.md
│       ├── DEPENDANCES_GLOBALES.md
│       ├── WORKFLOW_REBUILD.md
│       └── _TEMPLATE_DOC.md
│
├── docs_automations/
│   ├── TREE_CORRIGE/
│   │   ├── P1_clim_chauffage/                   (11 fichiers A0→L + old/)
│   │   ├── P1_cuisine/                          (2 fichiers)
│   │   ├── P1_sdb/                              (1 fichier)
│   │   ├── P2_prises/                           (6 fichiers)
│   │   ├── P3_eclairage/                        (1 fichier)
│   │   ├── raspi/                               (automations RPi4 — conservées migration)
│   │   ├── P2_bouton_rodret_soufflant_sdb.yaml
│   │   ├── P3_salon_bouton_inter_ikea_4.yaml
│   │   ├── P3_salon_bouton_inter_somrig.yaml
│   │   ├── backup/                              (4 fichiers)
│   │   ├── energie/                             (2 fichiers)
│   │   ├── meteo/                               (5 fichiers)
│   │   ├── stores/                              (2 fichiers)
│   │   └── systeme/                             (6 fichiers)
│   ├── TREE_ORIGINE/
│   └── docs/                                    (INDEX_AUTOMATIONS, TRIAGE, PROD_vs_REBUILD_DIFF, IDs REF)
│
└── docs_scripts/
    ├── TREE_CORRIGE/                            (A_rpi_fan_pwm_6_states.yaml)
    ├── TREE_ORIGINE/
    └── docs/                                    (INDEX_SCRIPTS.md, SCRIPTS_CLIM_ON_OFF.md, SCRIPT_J2_0_SECU_ARRET_CLIM.md)
```

---

## 🌳 ARBORESCENCE — PRODUCTION /config/ (DÉTAILLÉE)

```text
/config/
├── configuration.yaml
├── automations.yaml
├── scripts.yaml
├── scenes.yaml
├── camera.yaml
├── input_button.yaml
├── shell_command.yaml
├── sql.yaml
├── groups/                                      (répertoire — !include_dir_merge_named)
│   ├── GRP_01_batteries_hue.yaml               (hue_devices — 11 sensors)
│   ├── GRP_02_batteries_ikea.yaml              (ikea_devices — 12 sensors)
│   └── GRP_03_batteries_sonoff.yaml            (sonoff_devices — 11 sensors)
├── #sensors.yaml   #templates.yaml   #utility_meter.yaml  (désactivés)
│
/config/input_booleans/
├── P1/P1_ACS_IB_01_arret_clim_securises.yaml
├── P1/P1_BV_BI_02_inter_soufflant_sdb.yaml
├── P3/P3_BV_01_IB_inter_smorig_salon.yaml
├── P3/P3_BV_02_IB_inter_rodret_salon.yaml
└── P4/P4_presence_wifi.yaml
│
/config/utility_meter/
├── P0_Energie_total/Genelec_appart/
│   ├── 01_kWh_UM_AMHQ.yaml                    (Riemann — A/B test vs 02)
│   ├── 02_UM_AMHQ.yaml                        (direct Ecojoko — A/B test vs 01)
│   └── 03_UM_genelec_appart_HPHC_AMHQ.yaml   (HP/HC AMHQ)
├── P1_clim_chauffage/P1_UM_AMHQ.yaml
├── P2_prise/
│   ├── #P2_UM_AMHQ_prises.yaml.#                (désactivé — intentionnel, conservé pour référence)
│   ├── #P2_UM_AMHQ_veilles.yaml.#               (désactivé — intentionnel)
│   └── #P2_UM_AMHQ_mini_pc.yaml.#              (désactivé — intentionnel)
│   ⚠️ Prod /config/ a encore les fichiers ACTIFS → à nettoyer côté prod
├── P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml      (zones + total → calculés en TPL layer)
└── meteo/M_03_meteo_UM_blitzortung.yaml
│
/config/templates/
├── P0_Energie_total_diag/
│   ├── Diag/ × 3 yaml (jour/mois/hebdo)
│   ├── Genelec_appart/ × 3 yaml (cost/ratio/avg)
│   ├── Linky/MyElectricalData.yaml
│   └── total_pour_les_7_postes/total_pour_les_7_postes.yaml
├── P1_clim_chauffage/ P1_01_MASTER + P1_AVG + P1_TOTAL + P1_DUT_TOTAL + P1_ui_dashboard
├── P2_prise/ P2_AVG + P2_I_all_standby_power + P2_ui_dashboard + P2_éCO_prises/P2_eco_prises_config.yaml
├── P3_eclairage/
│   ├── P3_ENERGIE_TLP/                        (⚠️ nom prod — pas P3_POWER)
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
├── Mini-PC/
│   ├── #MP_01_sonde_température_mini-pc.yaml.#  (désactivé)
│   └── MP_02_sonde_température_mini-pc.yaml     (actif — remplace MP_01)
└── utilitaires/ × 3 yaml
│
/config/sensors/
├── Air_quality/A_01_AIR_QUALITY.yaml
├── P0_Energie_total_min_maxi_diag/
│   ├── P0_Genelec_appart/#P0_kWh_genelec_appart.yaml.#  (désactivé)
│   └── P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml
├── P1_clim_chauffage/
│   ├── P1_DUT/P1_DUT_clim_chauffage.yaml
│   └── P1_kWh/#P1_kWh_clim_chauffage.yaml.#  (désactivé)
├── P2_prise/
│   ├── #P2_kWh_prises.yaml.#   #P2_kWh_veilles.yaml.#   #P2_Wh_mini_pc.yaml.#  (désactivés — Riemann)
├── P3_eclairage/ (tous désactivés — remplacés par P3_ENERGIE_TLP)
└── meteo/M_03_meteo_sensors_blitzortung.yaml
```

---

## 🔗 INDEX GITHUB — URLS RAW (TREE_CORRIGE ↔ GITHUB)

> Dépôt : https://github.com/BerrySwann/home_assistant_re-build

### UTILITY METER

```
P0 — 01_kWh_UM_AMHQ.yaml       → .../utility_meter/P0_Energie_total/Genelec_appart/01_kWh_UM_AMHQ.yaml
P0 — 02_UM_AMHQ.yaml           → .../utility_meter/P0_Energie_total/Genelec_appart/02_UM_AMHQ.yaml
P0 — 03_UM_genelec_HPHC.yaml   → .../utility_meter/P0_Energie_total/Genelec_appart/03_UM_genelec_appart_HPHC_AMHQ.yaml
P1 — P1_UM_AMHQ.yaml           → .../utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml
P2 — prises/veilles/mini_pc    → .../utility_meter/P2_prise/P2_UM_AMHQ_{prises|veilles|mini_pc}.yaml
P3 — P3_UM_AMHQ_1_UNITE.yaml   → .../utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
M  — blitzortung               → .../utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml
```

### TEMPLATES P3 (⚠️ dossier = P3_ENERGIE_TLP, pas P3_POWER)

```
P3_TPL_AMHQ_1_UNITE.yaml  → .../templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_1_UNITE.yaml
P3_TPL_AMHQ_2_ZONE.yaml   → .../templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_2_ZONE.yaml
P3_TPL_AMHQ_3_TOTAL.yaml  → .../templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_3_TOTAL.yaml
```

### COMMAND_LINE

```
meteo         → .../command_line/meteo/carte_meteo_france.yaml
github        → .../command_line/github_maintenance/github_maintenance.yaml
```

> URLs complètes sur demande. Base : `https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/`
