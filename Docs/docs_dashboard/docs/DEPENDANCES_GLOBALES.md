# 🔗 DÉPENDANCES GLOBALES — TABLEAU DE BORD HA
*Dernière mise à jour : 2026-05-01*

---

## LÉGENDE

| Symbole | Signification |
|:-------:|:-------------|
| ✅ | Chaîne validée et opérationnelle |
| 🔲 | À documenter |
| ⚠️ | Rupture de chaîne ou entité obsolète |
| NAT | Entité native HA (intégration directe) |
| TPL | Template (`templates/`) |
| UM | Utility Meter (`utility_meter/`) |
| SEN | Sensor (`sensors/`) |

---

## MATRICE DES 18 VIGNETTES — STATUT DÉPENDANCES

| ID | Vignette | Statut |
|:---|:---------|:------:|
| L1C1 | Météo | 🔲 |
| L1C2 | Températures | 🔲 |
| L1C3 | Commandes Clim | 🔲 |
| L2C1 | Énergie Générale | ⚠️ |
| **L2C2** | **Énergie Clim / Rad / Soufflant** | ✅ |
| **L2C3** | **Énergie Éclairage** | ✅ |
| L3C1 | Commandes Éclairage | 🔲 |
| L3C2 | Commandes Prises | 🔲 |
| L3C3 | Stores / Fenêtres | 🔲 |
| L4C1 | *(Freebox — supprimé)* | — |
| L4C2 | Mini-PC | 🔲 |
| L4C3 | Mises à jour HA | 🔲 |
| L5C1 | Batteries / Piles | 🔲 |
| L5C2 | Batteries portables | 🔲 |
| L5C3 | MariaDB | 🔲 |
| L6C1 | Qualité de l'air | 🔲 |
| L6C2 | Pollution / Pollen | 🔲 |
| L6C3 | Vigilance Eau | 🔲 |

---

## ✅ L2C2 — ÉNERGIE CLIM / RAD / SOUFFLANT
*Validée le 2026-04-25*

### Chaîne de dépendances

```
MATÉRIEL (NOUS SP via Z2M)
  └─→ sensor.*_power / climate.*   (HA natif)
        └─→ SEN: P1_kWh_clim_chauffage.yaml   (Riemann → _energy_totale_kwh)
              └─→ UM: P1_UM_AMHQ.yaml          (6 appareils × 4 cycles AMHQ)
                    └─→ TPL: P1_TOTAL_AMHQ.yaml (conso_clim_rad_total_Q/M)
                          └─→ TPL: P1_ui_dashboard.yaml (*_power_status / *_etat)
                                └─→ VIGNETTE L2C2 (button-card 3 colonnes)
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `climate.clim_salon_rm4_mini` | NAT | SmartIR |
| `climate.radiateur_cuisine` | NAT | Meross |
| `climate.clim_bureau_rm4_mini` | NAT | SmartIR |
| `climate.soufflant_salle_de_bain` | NAT | Meross |
| `climate.clim_chambre_rm4_mini` | NAT | SmartIR |
| `sensor.salon_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.cuisine_power_status` | TPL | idem |
| `sensor.bureau_power_status` | TPL | idem |
| `sensor.sdb_soufflant_etat` | TPL | idem |
| `sensor.sdb_seche_serviette_etat` | TPL | idem |
| `sensor.chambre_power_status` | TPL | idem |
| `sensor.clim_salon_quotidien_kwh_um` | UM | `P1_clim_chauffage/P1_UM_AMHQ.yaml` |
| `sensor.radiateur_elec_cuisine_quotidien_kwh_um` | UM | idem |
| `sensor.clim_bureau_quotidien_kwh_um` | UM | idem |
| `sensor.soufflant_sdb_quotidien_kwh_um` | UM | idem |
| `sensor.seche_serviette_sdb_quotidien_kwh_um` | UM | idem |
| `sensor.clim_chambre_quotidien_kwh_um` | UM | idem |
| `sensor.conso_clim_rad_total_quotidien` | TPL | `P1_TOTAL/P1_TOTAL_AMHQ.yaml` |
| `sensor.clim_salon_mensuel_kwh_um` | UM | `P1_clim_chauffage/P1_UM_AMHQ.yaml` |
| `sensor.radiateur_elec_cuisine_mensuel_kwh_um` | UM | idem |
| `sensor.clim_bureau_mensuel_kwh_um` | UM | idem |
| `sensor.soufflant_sdb_mensuel_kwh_um` | UM | idem |
| `sensor.seche_serviette_sdb_mensuel_kwh_um` | UM | idem |
| `sensor.clim_chambre_mensuel_kwh_um` | UM | idem |
| `sensor.conso_clim_rad_total_mensuel` | TPL | `P1_TOTAL/P1_TOTAL_AMHQ.yaml` |

### Entités JS uniquement (non dans `entities:`)

| Entité | Source |
|:-------|:-------|
| `sensor.clim_salon_etat` | `P1_ui_dashboard.yaml` |
| `sensor.radiateur_cuisine_etat` | idem |
| `sensor.clim_bureau_etat` | idem |
| `sensor.sdb_soufflant_power_status` | idem |
| `sensor.sdb_seche_serviette_power_status` | idem |
| `sensor.clim_chambre_etat` | idem |

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `sensors/P1_clim_chauffage/P1_kWh/P1_kWh_clim_chauffage.yaml` | ✅ |
| `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml` | ✅ |
| `templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml` | ✅ |
| `templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml` | ✅ |

---

## ✅ L2C3 — ÉNERGIE ÉCLAIRAGE (LAMPES)
*Validée le 2026-04-29 — Migration TPL kWh complète (_um → _um_kwh_tpl)*

### Chaîne de dépendances

```
MATÉRIEL (Hue Bridge / Sonoff via Z2M)
  └─→ _energy (firmware direct, kWh cumulatif)
        └─→ UM: P3_UM_AMHQ_1_UNITE.yaml  (19 ampoules × 4 cycles = 76 _um)
              └─→ TPL: P3_ENERGIE_TLP/P3_TPL_AMHQ_1_UNITE.yaml  (76 _um_kwh_tpl)
                    └─→ TPL: P3_ENERGIE_TLP/P3_TPL_AMHQ_2_ZONE.yaml  (zones → 40 _um_kwh_tpl)
                    └─→ TPL: P3_ENERGIE_TLP/P3_TPL_AMHQ_3_TOTAL.yaml (4 total _kwh_tpl)
                    └─→ TPL: P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml (AVG W/ampoule, src _um_kwh_tpl)
                    └─→ TPL: P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml  (AVG W/zone, src _um_kwh_tpl)
                    └─→ TPL: P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml (AVG W total, src _um_kwh_tpl)
                    └─→ TPL: ui_dashboard/etats_status.yaml   (lumiere_*_etat)
                          └─→ VIGNETTE L2C3 (button-card 3 colonnes)
                          └─→ PAGE energie-lampes (tabbed-card 5 pièces)
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.lumiere_appartement_etat` | TPL | `P3_eclairage/ui_dashboard/etats_status.yaml` |
| `sensor.lumiere_salon_etat` | TPL | idem |
| `sensor.lumiere_cuisine_etat` | TPL | idem |
| `sensor.lumiere_bureau_etat` | TPL | idem |
| `sensor.lumiere_salle_de_bain_etat` | TPL | idem |
| `sensor.lumiere_chambre_etat` | TPL | idem |
| `sensor.eclairage_appart_2_quotidien_um_kwh_tpl` | TPL | `P3_ENERGIE_TLP/P3_TPL_AMHQ_2_ZONE.yaml` |
| `sensor.eclairage_salon_5_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_cuisine_1_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_bureau_5_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_sdb_2_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_chambre_4_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_total_unit_quotidien_kwh_tpl` | TPL | `P3_ENERGIE_TLP/P3_TPL_AMHQ_3_TOTAL.yaml` |
| `sensor.eclairage_appart_2_mensuel_um_kwh_tpl` | TPL | `P3_ENERGIE_TLP/P3_TPL_AMHQ_2_ZONE.yaml` |
| `sensor.eclairage_salon_5_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_cuisine_1_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_bureau_5_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_sdb_2_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_chambre_4_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_total_unit_mensuel_kwh_tpl` | TPL | `P3_ENERGIE_TLP/P3_TPL_AMHQ_3_TOTAL.yaml` |

### TPL ENERGIE — Détail des 3 fichiers P3_ENERGIE_TLP

| Fichier TPL | Contenu | Nb sensors | Statut |
|:------------|:--------|:----------:|:------:|
| `P3_TPL_AMHQ_1_UNITE.yaml` | 19 ampoules × 4 cycles | 76 | ✅ |
| `P3_TPL_AMHQ_2_ZONE.yaml` | 10 zones × 4 cycles | 40 | ✅ |
| `P3_TPL_AMHQ_3_TOTAL.yaml` | 1 total × 4 cycles | 4 | ✅ |

### Zones couvertes par P3_TPL_AMHQ_2_ZONE

| Zone (unique_id prefix) | Ampoules |
|:------------------------|:--------:|
| `eclairage_entree_1` | 1 |
| `eclairage_salon_5` | 5 |
| `eclairage_cuisine_1` | 1 |
| `eclairage_couloir_1` | 1 |
| `eclairage_bureau_5` | 5 |
| `eclairage_sdb_2` | 2 |
| `eclairage_chambre_4` | 4 |
| `eclairage_appart_3` | 3 (entrée+cuisine+couloir) |
| `eclairage_appart_2` | 2 (entrée+couloir) |

### Entité puissance temps réel (W)

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.eclairage_total_group_puissance_tpl` | TPL | `P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml` |

> Somme des 19 `{slug}_power` (PowerCalc). Consommé par `total_pour_les_7_postes.yaml` (Pôle 6) → L2C1.

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml` | ✅ |
| `templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_1_UNITE.yaml` | ✅ |
| `templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_2_ZONE.yaml` | ✅ |
| `templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_3_TOTAL.yaml` | ✅ |
| `templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml` | ✅ |
| `templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml` | ✅ |
| `templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml` | ✅ |
| `templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml` | ✅ |
| `templates/P3_eclairage/ui_dashboard/etats_status.yaml` | ✅ |

---

## ⚠️ L2C1 — ÉNERGIE GÉNÉRALE
*Corrections validées le 2026-05-01 — Documentation partielle (vignette complète à finaliser)*

### Fichiers corrigés cette session

| Fichier | Correction | Statut |
|:--------|:-----------|:------:|
| `templates/P0_Energie_total_diag/total_pour_les_7_postes/total_pour_les_7_postes.yaml` | Pôle 6 : `eclairage_total_group_puissance` → `eclairage_total_group_puissance_tpl` | ✅ |
| `templates/P0_Energie_total_diag/Diag/diag_conso_jour_en_cours.yaml` | Pôle 6 éclairage : `eclairage_total_group_quotidien_um` → `eclairage_total_unit_quotidien_kwh_tpl` | ✅ |
| `templates/P0_Energie_total_diag/Diag/diag_conso_mois_en_cours.yaml` | Pôle 6 éclairage : `eclairage_total_group_mensuel_um` → `eclairage_total_unit_mensuel_kwh_tpl` | ✅ |
| `templates/P0_Energie_total_diag/Diag/diag_conso_hebdomadaire_en_cours.yaml` | Pôle 6 éclairage : `eclairage_total_group_hebdomadaire_um` → `eclairage_total_unit_hebdomadaire_kwh_tpl` | ✅ |

### Entités Pôle 6 (Éclairage) alimentant L2C1

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.eclairage_total_group_puissance_tpl` | TPL | `P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml` |
| `sensor.eclairage_total_unit_quotidien_kwh_tpl` | TPL | `P3_ENERGIE_TLP/P3_TPL_AMHQ_3_TOTAL.yaml` |
| `sensor.eclairage_total_unit_mensuel_kwh_tpl` | TPL | idem |
| `sensor.eclairage_total_unit_hebdomadaire_kwh_tpl` | TPL | idem |

### Automation log (hors dashboard)

| Fichier | Correction | Statut |
|:--------|:-----------|:------:|
| `docs_automations/TREE_CORRIGE/systeme/diag_enregistrement_journalier.yaml` | `notify.file` → `notify.file_diag_log_file` + artefact Markdown `sensor.th_balcon_nord_temperature` | ✅ |

---

## 🔲 VIGNETTES À DOCUMENTER

Les vignettes suivantes n'ont pas encore leur chaîne de dépendances renseignée.
Remplir lors de la validation ou modification du fichier YAML correspondant.

| ID | Vignette | Fichiers source clés (estimation) |
|:---|:---------|:----------------------------------|
| L1C1 | Météo | `command_line/meteo/`, `templates/meteo/M_01/02/04.yaml` |
| L1C2 | Températures | `climate.*` natif SONOFF, `templates/P1_ui_dashboard.yaml` |
| L1C3 | Commandes Clim | `climate.*`, `P1_ui_dashboard.yaml`, `P1_AVG.yaml` |
| L2C1 | Énergie Générale *(partiel)* | `total_pour_les_7_postes.yaml` ✅, `diag_conso_*.yaml` ✅, `P0_kWh_genelec_appart.yaml` 🔲 |
| L3C1 | Commandes Éclairage | `light.*` natif Hue, `ui_dashboard/etats_status.yaml` |
| L3C2 | Commandes Prises | `switch.*` natif Z2M, `P2_ui_dashboard.yaml` |
| L3C3 | Stores / Fenêtres | `Stores/S_01_STORES.yaml`, `binary_sensor.*` fenêtres |
| L4C2 | Mini-PC | `Mini-PC/MP_01_sonde_température_mini-pc.yaml`, `sql.yaml` |
| L4C3 | Mises à jour HA | `utilitaires/Mise_a_jour_home_assistant.yaml` |
| L5C1 | Batteries / Piles | `auto-entities` natif HA |
| L5C2 | Batteries portables | `sensor.battery_*` natif |
| L5C3 | MariaDB | `sql.yaml` |
| L6C1 | Qualité de l'air | `sensors/Air_quality/A_01_AIR_QUALITY.yaml`, `templates/Air_quality/` |
| L6C2 | Pollution / Pollen | API externe météo |
| L6C3 | Vigilance Eau | API VigiEau |

---

<!-- obsidian-wikilinks -->
*Liens : [[L2C2_VIGNETTE_ENERGIE_CLIM]] [[L2C3_VIGNETTE_ECLAIRAGE]] [[WORKFLOW_REBUILD]] [[INDEX_PAGES]]*
