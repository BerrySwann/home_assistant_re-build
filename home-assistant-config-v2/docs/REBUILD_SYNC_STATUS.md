# REBUILD — ÉTAT DE SYNCHRONISATION
*Généré le 2026-03-02*

---

## LÉGENDE
- ✅ En sync (local = GitHub)
- ❌ Décalage (à corriger)
- ➕ Manquant sur GitHub (existe local)
- 🗑️ Obsolète local (absent sur GitHub = à supprimer)

---

## utility_meter/

```
utility_meter/
├── P0_Energie_total/
│   └── Ecojoko/
│       ├── ❌ 01_UM_AMHQ_cost.yaml              ← GitHub ✅ | Local: 03_P2_UM_ecojoko_hebdo_annuel.yaml (mauvais nom)
│       └── ❌ 02_UM_ecojoko_quotidien_live.yaml  ← GitHub ✅ | Local: absent ici (à déplacer depuis P2_prise/)
│
├── P1_clim_chauffage/
│   └── ✅ P1_UM_AMHQ.yaml
│
├── P2_prise/
│   ├── ❌ P2_AVG/
│   │   └── P2_UM_AMHQ.yaml                      ← GitHub: P2_AVG/P2_UM_AMHQ.yaml | Local: pas de sous-dossier P2_AVG
│   └── 🗑️ P2_UM_ecojoko_quotidien.yaml          ← à déplacer → P0_Energie_total/Ecojoko/02_UM_ecojoko_quotidien_live.yaml
│
├── P3_eclairage/
│   ├── ✅ P3_UM_AMHQ_1_UNITE.yaml
│   ├── ✅ P3_UM_AMHQ_2_ZONE.yaml
│   └── ✅ P3_UM_AMHQ_3_TOTAL.yaml
│
└── meteo/
    └── ✅ M_03_meteo_UM_blitzortung.yaml
```

**Actions requises :**
1. Renommer `03_P2_UM_ecojoko_hebdo_annuel.yaml` → `01_UM_AMHQ_cost.yaml`
2. Déplacer `P2_prise/P2_UM_ecojoko_quotidien.yaml` → `P0_Energie_total/Ecojoko/02_UM_ecojoko_quotidien_live.yaml`
3. Créer sous-dossier `P2_prise/P2_AVG/` et y déplacer `P2_UM_AMHQ.yaml`

---

## templates/

```
templates/
├── P0_Energie_total_diag/
│   ├── Diag/
│   │   ├── ✅ diag_conso_jour_en_cours.yaml
│   │   └── ✅ diag_conso_mois_en_cours.yaml
│   └── Ecojoko/
│       ├── ❌ 01_ecojoko_AMHQ_cost.yaml          ← GitHub ✅ | Local: P2_prises/P2_ecojoko_cout_hp_hc.yaml (mauvais endroit)
│       └── ❌ 02_ecojoko_7jrs_historique.yaml     ← GitHub ✅ | Local: P2_prises/P2_ecojoko_snapshot_j2_j7.yaml (mauvais endroit)
│
├── P1_/                                           ← ⚠️ Nom tronqué (P1_ seul) — à renommer P1_clim_chauffage ?
│   ├── P1_01_MASTER/
│   │   └── ✅ P1_01_clim_logique_system_autom.yaml
│   └── P1_AVG/
│       └── ✅ P1_avg.yaml
│
├── P2_prises/
│   ├── P2_AVG/
│   │   └── ✅ P2_AGV_AMHQ.yaml
│   ├── 🗑️ P2_ecojoko_cout_hp_hc.yaml             ← à déplacer → P0_.../Ecojoko/01_ecojoko_AMHQ_cost.yaml
│   └── 🗑️ P2_ecojoko_snapshot_j2_j7.yaml         ← à déplacer → P0_.../Ecojoko/02_ecojoko_7jrs_historique.yaml
│
├── P2_prises_NRJ_ TOTAL/                          ← ❌ ESPACE dans le nom → à fusionner dans P2_prises/
│   ├── P2_AVG/
│   │   └── 🗑️ P2_AGV_AMHQ.yaml                  ← doublon de P2_prises/P2_AVG/ (identique)
│   ├── ➕ P2_ecojoko_avg_watts.yaml               ← manquant sur GitHub
│   └── 🗑️ P2_ecojoko_snapshot_j2_j7.yaml         ← doublon de P2_prises/ (identique)
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

**Actions requises :**
1. Déplacer `P2_prises/P2_ecojoko_cout_hp_hc.yaml` → `P0_Energie_total_diag/Ecojoko/01_ecojoko_AMHQ_cost.yaml`
2. Déplacer `P2_prises/P2_ecojoko_snapshot_j2_j7.yaml` → `P0_Energie_total_diag/Ecojoko/02_ecojoko_7jrs_historique.yaml`
3. Supprimer `P2_prises_NRJ_ TOTAL/P2_AGV_AMHQ.yaml` (doublon)
4. Supprimer `P2_prises_NRJ_ TOTAL/P2_ecojoko_snapshot_j2_j7.yaml` (doublon)
5. Déplacer `P2_prises_NRJ_ TOTAL/P2_ecojoko_avg_watts.yaml` → `P2_prises/P2_ecojoko_avg_watts.yaml`
6. Supprimer dossier `P2_prises_NRJ_ TOTAL/` (vide après)

---

## sensors/

```
sensors/
├── P0_Energie_total_diag/
│   └── Ecojoko_mini_maxi/
│       └── ✅ Ecojojoko_mini_maxi_avg_1h.yaml
│
├── P2_prise/
│   ├── ✅ P2_kWh.yaml
│   └── 🗑️ P2_stats_ecojoko.yaml                  ← obsolète (remplacé par Ecojoko_mini_maxi_avg_1h.yaml)
│
├── P3_eclairage/
│   ├── ✅ P3_kWh_1_UNITE.yaml
│   ├── ✅ P3_kWh_2_ZONE.yaml
│   └── ✅ P3_kWh_3_TOTAL.yaml
│
└── meteo/
    └── ✅ M_03_meteo_sensors_blitzortung.yaml
```

**Actions requises :**
1. Supprimer `sensors/P2_prise/P2_stats_ecojoko.yaml` (obsolète)

---

## RÉCAPITULATIF DES ACTIONS

| # | Action | Type | Fichier |
|---|--------|------|---------|
| 1 | Renommer | utility_meter | `P0_.../Ecojoko/03_P2_UM_ecojoko_hebdo_annuel.yaml` → `01_UM_AMHQ_cost.yaml` |
| 2 | Déplacer | utility_meter | `P2_prise/P2_UM_ecojoko_quotidien.yaml` → `P0_.../Ecojoko/02_UM_ecojoko_quotidien_live.yaml` |
| 3 | Créer dossier + déplacer | utility_meter | `P2_prise/P2_UM_AMHQ.yaml` → `P2_prise/P2_AVG/P2_UM_AMHQ.yaml` |
| 4 | Déplacer | templates | `P2_prises/P2_ecojoko_cout_hp_hc.yaml` → `P0_.../Ecojoko/01_ecojoko_AMHQ_cost.yaml` |
| 5 | Déplacer | templates | `P2_prises/P2_ecojoko_snapshot_j2_j7.yaml` → `P0_.../Ecojoko/02_ecojoko_7jrs_historique.yaml` |
| 6 | Déplacer | templates | `P2_prises_NRJ_ TOTAL/P2_ecojoko_avg_watts.yaml` → `P2_prises/P2_ecojoko_avg_watts.yaml` |
| 7 | Supprimer | templates | `P2_prises_NRJ_ TOTAL/` (dossier entier — doublons) |
| 8 | Supprimer | sensors | `P2_prise/P2_stats_ecojoko.yaml` (obsolète) |
