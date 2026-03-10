# REBUILD — ÉTAT DE SYNCHRONISATION
*Mis à jour le 2026-03-08*

---

## LÉGENDE
- ✅ En sync (local = GitHub)
- ❌ Décalage local (à corriger)
- ➕ Manquant en local (existe sur GitHub)
- 🗑️ Obsolète local (absent sur GitHub = à supprimer)

---

## utility_meter/

```
utility_meter/
├── P0_Energie_total/
│   └── Ecojoko/
│       ├── ❌ 01_UM_AMHQ_cost.yaml              ← GitHub ✅ | Local: 03_P2_UM_ecojoko_hebdo_annuel.yaml (mauvais nom)
│       └── ❌ 02_UM_ecojoko_quotidien_live.yaml  ← GitHub ✅ | Local: absent (était dans P2_prise/)
│
├── P1_clim_chauffage/
│   └── ✅ P1_UM_AMHQ.yaml
│
├── P2_prise/
│   └── P2_AVG/
│       ├── ❌ P2_UM_AMHQ_prises.yaml            ← GitHub ✅ | Local: P2_UM_AMHQ.yaml (mauvais nom, plat)
│       └── ❌ P2_UM_AMHQ_veilles.yaml           ← GitHub ✅ | Local: absent
│
├── P3_eclairage/
│   ├── ✅ P3_UM_AMHQ_1_UNITE.yaml
│   ├── ✅ P3_UM_AMHQ_2_ZONE.yaml
│   └── ✅ P3_UM_AMHQ_3_TOTAL.yaml
│
└── meteo/
    └── ✅ M_03_meteo_UM_blitzortung.yaml
```

**Actions requises (local → GitHub) :**
1. Renommer `03_P2_UM_ecojoko_hebdo_annuel.yaml` → `01_UM_AMHQ_cost.yaml` (dans P0_Energie_total/Ecojoko/)
2. Déplacer + renommer `P2_prise/P2_UM_ecojoko_quotidien.yaml` → `P0_Energie_total/Ecojoko/02_UM_ecojoko_quotidien_live.yaml`
3. Créer `P2_prise/P2_AVG/` et y placer `P2_UM_AMHQ_prises.yaml` + `P2_UM_AMHQ_veilles.yaml` (supprimer `P2_UM_AMHQ.yaml` plat)

---

## templates/

```
templates/
├── P0_Energie_total_diag/
│   ├── Diag/
│   │   ├── ✅ diag_conso_jour_en_cours.yaml
│   │   └── ✅ diag_conso_mois_en_cours.yaml
│   ├── Ecojoko/
│   │   ├── ✅ 01_ecojoko_AMHQ_cost.yaml
│   │   ├── ✅ 02_ratio_hp_hc.yaml
│   │   └── ❌ 03_AVG_ecojoko.yaml               ← GitHub ✅ | Local: absent
│   └── Linky/
│       └── ✅ P0_linky_jour_J0_J7.yaml
│
├── P1_clim_chauffage/                            ← GitHub ✅ | Local: dossier nommé P1_/ (tronqué)
│   ├── P1_01_MASTER/
│   │   └── ✅ P1_01_clim_logique_system_autom.yaml
│   └── P1_AVG/
│       └── ✅ P1_avg.yaml
│
├── P2_prise/
│   ├── P2_AVG/
│   │   ├── ❌ P2_AVG_AMHQ_prises.yaml           ← GitHub ✅ | Local: P2_AGV_AMHQ.yaml (mauvais nom, dossier P2_prises/)
│   │   └── ❌ P2_AVG_AMHQ_veilles.yaml          ← GitHub ✅ | Local: absent
│   └── P2_I_all_standby_power/
│       └── ✅ P2_ current_all_standby.yaml
│
├── P3_eclairage/
│   ├── ✅ P3_01_somme_par_piece.yaml
│   ├── P3_AVG/
│   │   ├── ✅ P3_AVG_AMHQ_1_UNITE.yaml
│   │   ├── ✅ P3_AVG_AMHQ_2_ZONE.yaml
│   │   └── ✅ P3_AVG_AMHQ_3_TOTAL.yaml
│   └── ui_dashboard/
│       └── ✅ etats_status.yaml
│
├── P4_groupe_presence/
│   ├── ✅ 01_phones_wifi_cellular_card_autom.yaml
│   └── ✅ 02_logique_wifi_cellular.yaml
│
└── meteo/
    ├── ✅ M_01_meteo_alertes_card.yaml
    ├── ✅ M_02_meteo_vent_vence_card.yaml
    ├── ✅ M_03_meteo_templates_blitzortung.yaml
    └── ✅ M_04_tendances_th_ext_card.yaml
```

**Actions requises (local → GitHub) :**
1. Renommer dossier `templates/P1_/` → `templates/P1_clim_chauffage/`
2. Supprimer `templates/P2_prises/` (fichiers obsolètes déjà sur GitHub dans P2_prise/)
3. Supprimer `templates/P2_prises_NRJ_ TOTAL/` (doublons obsolètes)
4. Créer `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml` + `P2_AVG_AMHQ_veilles.yaml`
5. Ajouter `templates/P0_Energie_total_diag/Ecojoko/03_AVG_ecojoko.yaml`

---

## sensors/

```
sensors/
├── P0_Energie_total_diag/
│   └── Ecojoko_mini_maxi/
│       └── ✅ Ecojojoko_mini_maxi_avg_1h.yaml
│
├── P2_prise/
│   ├── ❌ P2_kWh_prises.yaml                    ← GitHub ✅ | Local: P2_kWh.yaml (mauvais nom)
│   ├── ❌ P2_kWh_veilles.yaml                   ← GitHub ✅ | Local: absent
│   └── 🗑️ P2_stats_ecojoko.yaml                 ← absent sur GitHub (à supprimer)
│
├── P3_eclairage/
│   ├── ✅ P3_kWh_1_UNITE.yaml
│   ├── ✅ P3_kWh_2_ZONE.yaml
│   └── ✅ P3_kWh_3_TOTAL.yaml
│
└── meteo/
    └── ✅ M_03_meteo_sensors_blitzortung.yaml
```

**Actions requises (local → GitHub) :**
1. Renommer `sensors/P2_prise/P2_kWh.yaml` → `P2_kWh_prises.yaml`
2. Ajouter `sensors/P2_prise/P2_kWh_veilles.yaml` (depuis GitHub)
3. Supprimer `sensors/P2_prise/P2_stats_ecojoko.yaml` (obsolète)

---

## docs/

```
docs/
├── ✅ IA/IA_CONTEXT_BASE.md
├── ✅ L1C1_METEO/ (3 fichiers)
├── ✅ L1C2_TEMPERATURES/ (2 fichiers)
├── ✅ L2C1_ENERGIE/ (5 fichiers + COULEURS_PRISES_PAR_PIECE.md)
├── ✅ L2C3_ENERGIE_ECLAIRAGE/L2C3_VIGNETTE_ECLAIRAGE.md
├── 🗑️ L5C1/État des Batteries.md               ← doublon de L5C1_PILES_BATTERIES/ (à supprimer)
├── ✅ L5C1_PILES_BATTERIES/ (2 fichiers)
├── ✅ WIFI_PRESENCE/VIGNETTE_WIFI_PRESENCE.md
└── ✅ REBUILD_SYNC_STATUS.md
```

**Actions requises :**
1. Supprimer `docs/L5C1/État des Batteries.md` (doublon)

---

## RÉCAPITULATIF DES ACTIONS LOCALES RESTANTES

| # | Action | Dossier | Détail |
|---|--------|---------|--------|
| 1 | Renommer | utility_meter/P0 | `03_P2_UM_ecojoko_hebdo_annuel.yaml` → `01_UM_AMHQ_cost.yaml` |
| 2 | Déplacer+renommer | utility_meter/P2→P0 | `P2_UM_ecojoko_quotidien.yaml` → P0/.../`02_UM_ecojoko_quotidien_live.yaml` |
| 3 | Restructurer | utility_meter/P2 | `P2_UM_AMHQ.yaml` plat → `P2_AVG/P2_UM_AMHQ_prises.yaml` + `P2_UM_AMHQ_veilles.yaml` |
| 4 | Renommer dossier | templates/ | `P1_/` → `P1_clim_chauffage/` |
| 5 | Supprimer | templates/ | `P2_prises/` (obsolète) + `P2_prises_NRJ_ TOTAL/` (doublons) |
| 6 | Ajouter | templates/P2_prise | `P2_AVG_AMHQ_prises.yaml` + `P2_AVG_AMHQ_veilles.yaml` depuis GitHub |
| 7 | Ajouter | templates/P0/Ecojoko | `03_AVG_ecojoko.yaml` depuis GitHub |
| 8 | Renommer | sensors/P2 | `P2_kWh.yaml` → `P2_kWh_prises.yaml` |
| 9 | Ajouter | sensors/P2 | `P2_kWh_veilles.yaml` depuis GitHub |
| 10 | Supprimer | sensors/P2 | `P2_stats_ecojoko.yaml` (obsolète) |
| 11 | Supprimer | docs/ | `L5C1/État des Batteries.md` (doublon) |
