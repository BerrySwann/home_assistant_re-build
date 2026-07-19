# 🔗 MOC — DÉPENDANCES
*Map of Content — Chaîne de dépendances du projet HA ReBuild*
*Dernière mise à jour : 2026-04-19*

---

## 📖 Document maître

→ [[DEPENDANCES_GLOBALES]] — Chaîne complète (18 vignettes, toutes sources)

---

## 🏗️ Par Pôle technique

### Pôle 0 — Énergie Globale (Linky / NODON / Ecojoko)
Entités clés : `genelec_appart_totale_kwh` · `genelec_appart_*_um_hp/hc`
Fichiers YAML :
- `sensors/P0_Energie_total_min_maxi_diag/`
- `templates/P0_Energie_total_diag/`
- `utility_meter/P0_Energie_total/`

### Pôle 1 — Chauffage & Clim
Entités clés : `clim_*_energie_totale_kwh` · `p1_dut_*` · `p1_avg_*`
Fichiers YAML :
- `sensors/P1_clim_chauffage/P1_kWh/` · `P1_DUT/`
- `templates/P1_clim_chauffage/P1_AVG/` · `P1_TOTAL/` · `P1_ui_dashboard/`
- `utility_meter/P1_clim_chauffage/`

### Pôle 2 — Prises Connectées
Entités clés : `*_kwh_quotidien` · `mini_pc_avg_watts_*`
Fichiers YAML :
- `sensors/P2_prise/`
- `templates/P2_prise/P2_AVG/` · `P2_ui_dashboard/`
- `utility_meter/P2_prise/`

### Pôle 3 — Éclairage
Entités clés : `eclairage_*_energie_*` · `eclairage_*_power_*`
Fichiers YAML :
- `sensors/P3_eclairage/`
- `templates/P3_eclairage/P3_POWER/` · `P3_AVG/` · `ui_dashboard/`
- `utility_meter/P3_eclairage/`

### Pôle 4 — Groupe Présence
Entités clés : `presence_*` · `phone_*_status`
Fichiers YAML :
- `templates/P4_groupe_presence/`

### Catégories système
- **[ M ] Météo** : `templates/meteo/` · `sensors/meteo/` · `utility_meter/meteo/` · `command_line/meteo/`
- **[ A ] Air Quality** : `sensors/Air_quality/` · `templates/Air_quality/`
- **[ ST ] SpeedTest** : `templates/SpeedTest/` · `command_line/speedtest/`
- **[ S ] Stores** : `templates/Stores/`
- **[ B ] BP Virtuel** : `templates/Inter_BP_Virtuel/`
- **[ MP ] Mini-PC** : `templates/Mini-PC/`

---

## 📋 Workflows & Référence

→ [[WORKFLOW_REBUILD]] — Procédure création/modification doc vignette
→ [[CONFIG_ROOT/CONFIG_ROOT]] — configuration.yaml racine
→ [[_TEMPLATE_DOC]] — Modèle vierge pour nouvelle vignette
