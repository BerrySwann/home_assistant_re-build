# TREE — FICHIERS ABSENTS / STATUT DE SYNCHRONISATION
*Dernière mise à jour : 2026-03-13*
*Référence live : `rebuild_tree.txt` (GitHub re-build, état HA fonctionnel)*

---

## ✅ ÉTAT GÉNÉRAL : 41 FICHIERS PRÉSENTS DANS TREE

La TREE est maintenant synchronisée avec `rebuild_tree.txt`.
Tous les fichiers présents sur l'instance HA live ont été intégrés.

---

## ❌ FICHIERS ABSENTS CONFIRMÉS

Ces fichiers sont référencés dans **CLAUDE.md** (arborescence cible)
mais sont **absents à la fois du workspace local ET de rebuild_tree.txt**.
Ils n'ont jamais été créés ou ont été supprimés/renommés sur HA.

| Fichier cible CLAUDE.md | Statut |
|-------------------------|--------|
| `utility_meter/P0_Energie_total/Linky/` | Dossier vide — aucun UM Linky déployé sur HA |
| `sensors/P1_/` | Dossier vide — aucun sensor P1 kWh déployé sur HA |

---

## 🆕 FICHIERS PRÉSENTS SUR HA MAIS HORS CLAUDE.md (2 fichiers)

Ces fichiers existent sur l'instance HA live (`rebuild_tree.txt`) mais
n'étaient pas documentés dans CLAUDE.md. Intégrés dans TREE le 2026-03-13.
**CLAUDE.md devra être mis à jour.**

| Fichier | Emplacement TREE | Note |
|---------|-----------------|------|
| `M_05_cycle_solaire.yaml` | `templates/meteo/` | Créé le 2026-03-11 par BerrySwann |
| `jour_nuit.yaml` | `templates/utilitaires/` | Nouveau dossier `utilitaires/` hors CLAUDE.md |

---

## 📋 INVENTAIRE COMPLET TREE (41 fichiers)

### `/utility_meter/` (8 fichiers)
```
P0_Energie_total/Ecojoko/
  ├── 01_UM_AMHQ_cost.yaml
  └── 02_UM_ecojoko_quotidien_live.yaml
P1_clim_chauffage/
  └── P1_UM_AMHQ.yaml
P2_prise/P2_AVG/
  ├── P2_UM_AMHQ_prises.yaml      ← AJOUTÉ 2026-03-13
  └── P2_UM_AMHQ_veilles.yaml
P3_eclairage/
  ├── P3_UM_AMHQ_1_UNITE.yaml
  ├── P3_UM_AMHQ_2_ZONE.yaml
  └── P3_UM_AMHQ_3_TOTAL.yaml
meteo/
  └── M_03_meteo_UM_blitzortung.yaml
```

### `/templates/` (24 fichiers)
```
P0_Energie_total_diag/Diag/
  ├── diag_conso_jour_en_cours.yaml    ← AJOUTÉ 2026-03-13
  └── diag_conso_mois_en_cours.yaml    ← AJOUTÉ 2026-03-13
P0_Energie_total_diag/Ecojoko/
  ├── 01_ecojoko_AMHQ_cost.yaml
  ├── 02_ratio_hp_hc.yaml
  └── 03_AVG_ecojoko.yaml              ← AJOUTÉ 2026-03-13
P0_Energie_total_diag/Linky/
  ├── MyElectricalData.yaml            ← AJOUTÉ 2026-03-13 (nom officiel HA)
  └── P0_linky_jour_J0_J7.yaml        ← ANCIEN (même contenu — à supprimer)
P1_clim_chauffage/P1_01_MASTER/
  └── P1_01_clim_logique_system_autom.yaml
P1_clim_chauffage/P1_AVG/
  └── P1_avg.yaml
P2_prise/P2_AVG/
  ├── P2_AVG_AMHQ_prises.yaml         ← AJOUTÉ 2026-03-13
  └── P2_AVG_AMHQ_veilles.yaml        ← AJOUTÉ 2026-03-13
P2_prise/P2_I_all_standby_power/
  └── P2_ current_all_standby.yaml    ← AJOUTÉ 2026-03-13
P3_eclairage/
  ├── P3_01_somme_par_piece.yaml
  ├── P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml
  ├── P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml
  └── P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml ← AJOUTÉ 2026-03-13
P3_eclairage/ui_dashboard/
  └── etats_status.yaml
P4_groupe_presence/
  ├── 01_phones_wifi_cellular_card_autom.yaml
  └── 02_logique_wifi_cellular.yaml
meteo/
  ├── M_01_meteo_alertes_card.yaml
  ├── M_02_meteo_vent_vence_card.yaml
  ├── M_03_meteo_templates_blitzortung.yaml
  ├── M_04_tendances_th_ext_card.yaml
  └── M_05_cycle_solaire.yaml          ← AJOUTÉ 2026-03-13 (hors CLAUDE.md)
utilitaires/                           ← NOUVEAU DOSSIER (hors CLAUDE.md)
  └── jour_nuit.yaml                   ← AJOUTÉ 2026-03-13
```

### `/sensors/` (9 fichiers)
```
P0_Energie_total_diag/Ecojoko_mini_maxi/
  └── Ecojoko_mini_maxi_avg_1h.yaml    ← AJOUTÉ 2026-03-13
P2_prise/
  ├── P2_kWh_prises.yaml
  └── P2_kWh_veilles.yaml
P3_eclairage/
  ├── P3_kWh_1_UNITE.yaml
  ├── P3_kWh_2_ZONE.yaml
  └── P3_kWh_3_TOTAL.yaml
meteo/
  └── M_03_meteo_sensors_blitzortung.yaml
```

---

## ⚠️ ACTIONS REQUISES

1. **Supprimer `P0_linky_jour_J0_J7.yaml`** dans `templates/P0_Energie_total_diag/Linky/`
   — remplacé par `MyElectricalData.yaml` (nom officiel sur HA).

2. **Mettre à jour CLAUDE.md** pour ajouter :
   - `templates/meteo/M_05_cycle_solaire.yaml`
   - `templates/utilitaires/` (nouveau dossier) et `jour_nuit.yaml`

3. **Valider les entités UM P2 prises** après `reload templates` sur HA — les noms
   générés suivent les conventions déduites des fichiers existants (vérification
   conseillée après prochain redémarrage ou `check_config`).
