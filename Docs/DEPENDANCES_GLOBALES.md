# 🔗 DÉPENDANCES GLOBALES — TOUTES LES VIGNETTES
*Dernière mise à jour : 2026-04-19 — Audit conformité TREE_CORRIGE (71 fichiers ✅ — 0 N1 — 0 N2)*

> **RÈGLE :** Ce fichier est mis à jour obligatoirement à chaque création ou modification d'une doc de vignette (`docs/L*`).
> Format : Vignette → Carte → Template/Sensor → Utility Meter → Source native HA

---

## 📖 LÉGENDE

| Symbole | Signification |
|---------|---------------|
| ✅ | Doc vignette existante dans `docs/` |
| 🔲 | Doc vignette à créer |
| `→` | Dépend de |
| `[UM]` | Utility Meter |
| `[TPL]` | Template |
| `[SNS]` | Sensor (intégration kWh) |
| `[NAT]` | Entité native HA (intégration UI) |

---

## LIGNE 1 — ENVIRONNEMENT & THERMIQUE

### ✅ L1C1 — Météo
`docs/L1C1_METEO/`

```
L1C1 Météo
  ├── Alertes vigilance
  │     └── [TPL] M_01_meteo_alertes_card.yaml
  │           └── camera.mf_alerte_today / _tomorrow  [NAT camera.yaml]
  │                 └── command_line/meteo/carte_meteo_france.yaml
  │                       └── API Météo France (wget)
  ├── Vent / Windrose
  │     └── [TPL] M_02_meteo_vent_vence_card.yaml
  │           └── [NAT] sensor.openweathermap_wind_* / wind_bearing
  ├── Foudre Blitzortung
  │     └── [TPL] M_03_meteo_templates_blitzortung.yaml
  │           └── [SNS] sensors/meteo/M_03_meteo_sensors_blitzortung.yaml
  │                 └── [UM] utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml
  │                       └── [NAT] intégration Blitzortung (HACS)
  └── Tendances T° ext
        └── [TPL] M_04_tendances_th_ext_card.yaml
              └── [NAT] sensor.th_ext_temperature (SONOFF SNZB-02 balcon)
```

---

### ✅ L1C2 — Températures
`docs/L1C2_TEMPERATURES/`

```
L1C2 Températures
  ├── T° + Humidité (6 pièces + extérieur)
  │     └── [NAT] sensor.th_*_temperature / *_humidity (SONOFF SNZB-02 x7)
  ├── Tendances T° / Humidité (extérieur)
  │     └── [TPL] templates/meteo/M_04_tendances_th_ext_card.yaml
  │           └── [NAT] sensor.th_balcon_nord_temperature / _humidity
  ├── Cycle solaire (lever/coucher)
  │     └── [TPL] templates/meteo/M_05_cycle_solaire.yaml
  │           └── [NAT] sun.sun
  ├── Section Consommation — statuts et états clim
  │     └── [TPL] templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml
  │           └── [NAT] sensor.*_nous_power / sensor.radiateur_elec_cuisine_power
  │                 └── [NAT] climate.clim_*_rm4_mini (SmartIR)
  ├── Section Consommation — totaux kWh + puissance W
  │     └── [TPL] templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml
  │           └── [UM] utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml
  │                 └── [SNS] sensors/P1_clim_chauffage/ (*_energie_totale_kwh Riemann)
  ├── Section Consommation — moyennes watts
  │     └── [TPL] templates/P1_clim_chauffage/P1_AVG/P1_avg.yaml
  │           └── [UM] P1_UM_AMHQ.yaml
  └── Section Consommation + pop-up #tendances — logique groupe / T° cible
        └── [TPL] templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml
              └── [NAT] climate.* / sensor.th_*_temperature / input_number.*
```

---

### ✅ L1C3 — Commandes Clim
`docs/L1C3_CLIM/`

```
L1C3 Commandes Clim (Vignette)
  ├── Statuts ON/OFF + modes + consignes × 5 pièces
  │     └── [TPL] P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml
  │           └── [NAT] sensor.*_nous_power / climate.*_rm4_mini / climate.radiateur_cuisine
  ├── T° moyenne appartement + Δ ADEME
  │     └── [TPL] P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml
  │           └── [NAT] sensor.th_*_temperature / input_number.*
  └── Consignes climate
        └── [NAT] climate.clim_*_rm4_mini (SmartIR) / climate.radiateur_cuisine (Meross)
              └── climate.soufflant_salle_de_bain (Meross)

L1C3 Commandes Clim (Page /clim)
  ├── Bilan total + chips conditionnels
  │     ├── [TPL] P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml
  │     │     → sensor.*_power_status / sensor.*_power_status_affichage / sensor.*_etat
  │     └── [TPL] P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml
  │           → sensor.conso_clim_rad_total (W)
  ├── Sections Salon / Bureau / Chambre — warnings arrêt sécurisé
  │     ├── [NAT] input_boolean.clim_*_arret_securise_en_cours
  │     │     └── fichier source : input_booleans/arret_clim_securises.yaml (ajouté 2026-03-27)
  │     ├── [TPL] sensor.*_power_lock (ui_dashboard.yaml)
  │     └── [NAT] switch.clim_*_nous (prises NOUS)
  ├── Thermostats + bar-cards puissance
  │     └── [NAT] climate.* + sensor.*_nous_power + sensor.radiateur_elec_cuisine_power
  ├── Section SdB — button-card soufflant (état résistance)
  │     ├── [TPL] Inter_BP_Virtuel/BI_02_switch_inter_sdb.yaml
  │     │     → switch.inter_soufflant_salle_de_bain
  │     └── [NAT] input_select.etat_resistance_soufflant_sdb / sensor.statut_soufflant_sdb
  ├── Badges schedules × 5 pièces
  │     └── [NAT] switch.schedule_* (intégration Scheduler HACS — ⚠️ à configurer)
  ├── Scripts arrêt intelligent (tandem J-1 → J-2)
  │     ├── [NAT] script.j_1_routeur_clim_on_off_intelligent — ROUTEUR (anti-tremblote + routage ON/OFF)
  │     └── [NAT] script.j_2_secu_arret_clim_protege — EXÉCUTANT (attend <9W → coupe NOUS → libère verrou)
  │           └── fichier source : scripts.yaml (racine repo)
  └── Pop-up #calcul
        └── streamline template: calcule_temp_cible
```

---

## LIGNE 2 — CONSOMMATION ÉNERGÉTIQUE

### ✅ L2C1 — Énergie Générale
`docs/L2C1_ENERGIE/`

> ⚠️ **[2026-04-18] Migration Ecojoko → NODON** : Ecojoko retiré de l'installation. Toutes les entités `ecojoko_*` remplacées par NODON + capteurs Genelec Appart.

```
L2C1 Énergie Générale
  ├── Vignette (button-card — Mini kWh / Réel W / Maxi kWh + coûts HP/HC inline)
  │     ├── [SNS] sensor.genelec_appart_conso_mini_24h  (value_min 24h sur UM quotidien — toujours 0)
  │     │     └── sensors/P0_Energie_total_diag/Genelec_appart/Genelec_appart_mini_maxi_avg.yaml
  │     │           └── [UM] sensor.genelec_appart_quotidien_um
  │     │                 └── utility_meter/P0_Energie_total/Genelec_appart/01_UM_AMHQ_cost.yaml
  │     │                       └── [SNS] sensor.genelec_appart_totale_kwh (Riemann tampon)
  │     │                             └── [NAT] sensor.general_electric_appart_energy (NODON)
  │     ├── [SNS] sensor.genelec_appart_conso_maxi_24h  (value_max 24h — total journalier kWh)
  │     │     └── (même source que mini ci-dessus)
  │     ├── [NAT] sensor.general_electric_appart_power  (live W — NODON)
  │     ├── [UM]  sensor.genelec_appart_hphc_mensuel_um_hp / *_hc  (base calcul coûts inline)
  │     │     └── utility_meter/P0_Energie_total/Genelec_appart/03_UM_genelec_appart_HPHC_AMHQ.yaml
  │     │           └── [SNS] sensor.genelec_appart_totale_kwh (Riemann tampon)
  │     └── [NAT] sensor.edf_tempo_price_blue_hp / _hc  (tarifs EDF Tempo Bleu)
  ├── Page principale /energie (tabbed-card 3 onglets JOURNALIER/HEBDO/MENSUEL)
  │     ├── Ring-tiles Mini(kWh) / Réel(W) / Maxi(kWh)
  │     │     ├── [SNS] sensor.genelec_appart_conso_mini_24h (max: 20 kWh)
  │     │     ├── [NAT] sensor.general_electric_appart_power (max: 6000 W)
  │     │     └── [SNS] sensor.genelec_appart_conso_maxi_24h (max: 20 kWh)
  │     ├── Energy overview card
  │     │     ├── [NAT] sensor.general_electric_appart_energy (champ power)
  │     │     └── [NAT] sensor.general_electric_appart_power  (champ current)
  │     ├── Coûts HP/HC (quotidien, hebdo, mensuel)
  │     │     ├── [TPL] P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml
  │     │     │     └── [UM] 03_UM_genelec_appart_HPHC_AMHQ.yaml → *_um_hp / *_um_hc
  │     │     │           └── [SNS] sensor.genelec_appart_totale_kwh (Riemann)
  │     │     └── [NAT] sensor.edf_tempo_price_blue_hp / _hc
  │     ├── Ratio HC/HP
  │     │     └── [TPL] P0_Energie_total_diag/Genelec_appart/02_ratio_hp_hc.yaml
  │     ├── Moyennes AVG Watts (AMHQ)
  │     │     └── [TPL] P0_Energie_total_diag/Genelec_appart/03_AVG_genelec_appart.yaml
  │     │           └── [UM] sensor.genelec_appart_*_um (01_UM_AMHQ_cost.yaml)
  │     ├── Historique 7j offset (ApexCharts)
  │     │     └── [UM] sensor.genelec_appart_quotidien_um (×8 séries offset J0→J-7)
  │     ├── Diag conso (jour / semaine / mois)
  │     │     └── [TPL] Diag/diag_conso_*.yaml (x3)
  │     │           └── sensor.diag_poste_*_quotidien / hebdomadaire / mensuel
  │     │           └── sensor.diag_max_poste_quotidien_dynamique / hebdo / mensuel
  │     └── Linky MyElectricalData
  │           └── [TPL] P0_Energie_total_diag/Linky/MyElectricalData.yaml
  │                 └── [NAT] intégration MyElectricalData (HACS)
  ├── Page temps réel /energie-temps-reel (4 colonnes)
  │     ├── Col 1 : 7 sections conditionnelles par catégorie
  │     │     └── [NAT] sensor.total_poste_*_puissance (W) — condition ≠ "0"
  │     ├── Col 2 : Donut journalier (18 prises × _quotidien_um)
  │     │     └── [UM] P2_prise/P2_AVG/P2_UM_AMHQ_prises.yaml + veilles
  │     ├── Col 3 : ApexCharts ligne instantanée
  │     │     └── [NAT] sensor.general_electric_appart_power (NODON)
  │     └── Col 4 : tabbed-card 6 onglets pièces (1/4/5/7/9/Veilles)
  │           └── [NAT] sensor.*_power (W) par prise connectée
  └── Page mensuelle /energie-mensuel (streamline par appareil)
        ├── Donut mensuel (18 séries × _mensuel_um)
        │     └── [UM] P2_prise/P2_AVG/P2_UM_AMHQ_prises.yaml + veilles
        └── Streamline cards (18 appareils — template conso_mensuelle_appareil)
              ├── [SNS] P2_prise/P2_kWh_prises.yaml (_energie_totale_kwh)
              └── [TPL] P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml (_avg_watts_mensuel)
```

---

### ✅ L2C2 — Énergie Clim / Radiateur / Soufflant
`docs/L2C2_ENERGIE_CLIM/`

```
L2C2 Énergie Clim (Vignette)
  ├── Noms pièces + couleur ON/OFF/mode (colorMap JS)
  │     └── [TPL] P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml
  │           → sensor.*_power_status / sensor.*_etat
  │                 └── [NAT] climate.* (SmartIR / Meross) + sensor.*_nous_power
  ├── kWh quotidien × 6 appareils + TOTAL
  │     ├── [UM] utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml
  │     │     → sensor.*_quotidien_um (6)
  │     └── [TPL] P1_TOTAL/P1_TOTAL_AMHQ.yaml
  │           → sensor.conso_clim_rad_total_quotidien
  └── kWh mensuel × 6 appareils + TOTAL
        ├── [UM] P1_UM_AMHQ.yaml → sensor.*_mensuel_um (6)
        └── [TPL] P1_TOTAL/P1_TOTAL_AMHQ.yaml → sensor.conso_clim_rad_total_mensuel

L2C2 Énergie Clim (Page /energie-clim)
  ├── En-tête + Δ T° badge → popup #tendances
  │     └── [TPL] P1_01_MASTER/P1_01_clim_logique_system_autom.yaml
  │           → sensor.temperature_delta_affichage
  ├── Bloc bilan conditionnel (6 *_affichage)
  │     └── [TPL] ui_dashboard.yaml → sensor.*_power_status_affichage
  ├── Chips DUT × 4 (Salon/Cuisine/Bureau/Chambre)
  │     └── [SNS] sensors/P1_clim_chauffage/P1_DUT_clim_chauffage.yaml
  │           → sensor.dut_clim_salon / dut_radiateur_cuisine / dut_clim_bureau / dut_clim_chambre
  ├── Chips état conditionnels × 6
  │     └── [TPL] ui_dashboard.yaml → sensor.*_power_status + sensor.*_etat
  ├── Bar-card puissance totale
  │     └── [TPL] P1_TOTAL/P1_TOTAL_AMHQ.yaml → sensor.conso_clim_rad_total (W)
  ├── Donuts Q + M (6 séries × _um)
  │     └── [UM] P1_UM_AMHQ.yaml
  ├── Graphique multi-yaxis 24h
  │     ├── sensor.temperature_moyenne_interieure [TPL P1_01_MASTER]
  │     ├── sensor.th_balcon_nord_temperature [NAT SONOFF]
  │     ├── sensor.conso_clim_rad_total [TPL P1_TOTAL]
  │     └── sensor.clim_rad_total_avg_watts_quotidien [TPL P1_AVG/P1_avg.yaml]
  ├── Graphique DUT global (5 pièces + T° ext)
  │     └── [SNS] P1_DUT_clim_chauffage.yaml → sensor.dut_* (5) + dut_sdb_total
  ├── × 5 pièces (Salon/Cuisine/Bureau/SdB×2/Chambre) :
  │     ├── bubble-card climate → [NAT] climate.*
  │     ├── ring-tiles V/A → [NAT] sensor.*_nous_voltage / *_nous_current
  │     ├── Onglet INSTANTANÉ → streamline conso_temps_reel_clim_rad
  │     │     → sensor.*_nous_power [NAT] + sensor.*_avg_watts_quotidien [TPL P1_AVG]
  │     ├── Onglet MENSUEL → streamline conso_mensuelle_clim
  │     │     → sensor.*_nous_energy [NAT] + sensor.*_avg_watts_mensuel [TPL P1_AVG]
  │     │       + sensor.*_mensuel_um [UM P1_UM_AMHQ]
  │     ├── Onglet PERF/DUT → apexcharts DUT par pièce (color_threshold)
  │     │     → sensor.dut_* [SNS P1_DUT]
  │     └── Badges Q/H/M/A kWh → [UM] P1_UM_AMHQ.yaml
  └── Pop-up #tendances
        └── streamline calcule_temp_cible [TPL P1_01_MASTER]
```

---

### ✅ L2C3 — Énergie Éclairage
`docs/L2C3_ENERGIE_ECLAIRAGE/`

```
L2C3 Éclairage kWh
  ├── Vignette (button-card 3 colonnes pièce/quotidien/mensuel)
  │     └── sensor.lumiere_*_etat  [TPL] P3_eclairage/ui_dashboard/etats_status.yaml
  │     └── sensor.eclairage_*_quotidien/mensuel_um
  │           └── [UM] P3_eclairage/P3_UM_AMHQ_2_ZONE.yaml + P3_UM_AMHQ_3_TOTAL.yaml
  ├── Page /dashboard-tablette/energie-lampes
  │     ├── Donuts JOUR/MOIS par ampoule (19 lampes × 5 pièces)
  │     │     └── sensor.hue_*/sonoff_*_quotidien/mensuel_um
  │     │           └── [UM] P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
  │     ├── Graphique 30 JOURS par zone + ligne AVG
  │     │     └── sensor.eclairage_*_mensuel_um  [UM 2_ZONE]
  │     │     └── sensor.eclairage_*_avg_watts_mensuel  [TPL] P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml
  │     └── Badges Q/H/M/A par zone (subtitle heading)
  │           └── [UM] P3_eclairage/P3_UM_AMHQ_2_ZONE.yaml
  ├── kWh par ampoule
  │     └── [SNS] P3_eclairage/P3_kWh_1_UNITE.yaml
  │           └── intégration Riemann sur P3_POWER_1
  ├── kWh par zone
  │     └── [SNS] P3_eclairage/P3_kWh_2_ZONE.yaml
  │           └── [UM] P3_eclairage/P3_UM_AMHQ_2_ZONE.yaml
  └── Moyennes [AVG]
        └── [TPL] P3_AVG/P3_AVG_AMHQ_*.yaml (x3)
```

---

## LIGNE 3 — COMMANDES & ACTIONNEURS

### ✅ L3C1 — Commandes Éclairage
`docs/L3C1_ECLAIRAGE/`

```
L3C1 Éclairage
  ├── Vignette (custom:button-card — grid 3 cols Pièce / État / Compteur)
  │     ├── [TPL] sensor.lumiere_appartement_etat  → etats_status.yaml
  │     ├── [TPL] sensor.lumiere_salon_etat         → etats_status.yaml
  │     ├── [TPL] sensor.lumiere_cuisine_etat       → etats_status.yaml
  │     ├── [TPL] sensor.bureau_etat                → etats_status.yaml
  │     ├── [TPL] sensor.lumiere_ecran_etat         → etats_status.yaml
  │     ├── [TPL] sensor.lumiere_salle_de_bain_etat → etats_status.yaml
  │     ├── [TPL] sensor.chambre_etat               → etats_status.yaml
  │     ├── [NAT] light.entree / couloir / salon / table / cuisine
  │     ├── [NAT] light.lampe_salle_de_bain_hue
  │     ├── [NAT] light.chambre / hue_color_candle_chambre_gege / _eric
  │     └── [NAT] switch.prise_tete_de_lit_chambre
  └── Page /dashboard-tablette/lumieres ✅ documentée [s16]
        ├── mushroom-entity-card × 7 pièces (Entrée/Salon/Table/Cuisine/Couloir/SdB/Chambre)
        │     └── flame animation card_mod — trigger état natif light.*
        ├── vertical-stack-in-card Bureau (cols 6) + conditional Ecran (cols 6)
        │     ├── [TPL] sensor.lumiere_bureau_etat / sensor.lumiere_ecran_etat → etats_status.yaml
        │     ├── [NAT] light.bureau / hue_white_lamp_bureau_1+2
        │     ├── [NAT] light.hue_play_1/2/3_pc_bureau + light.moniteur_pc
        │     ├── [NAT] switch.ecran_p_c_3_play_hue (conditional Ecran)
        │     └── mushroom-chips-card pastilles → popups #bureau / #ecranpc
        ├── conditional Têtes de Lit (cols 12) — [NAT] switch.prise_tete_de_lit_chambre
        │     └── mushroom-chips-card pastille → popup #tete_de_lit
        ├── Popups bubble-card × 3 (#bureau / #ecranpc / #tete_de_lit)
        │     └── mushroom-light-card + custom:button-card grilles 25/50/75/100%
        ├── [NAT] light.hue_color_candle_chambre_gege / _eric (têtes de lit)
        ├── [NAT] switch.relais_lumiere_sdb_sonoff + light.lampe_salle_de_bain_hue
        └── streamline-card template: nav_bar

  ✅ [B1] Badge lumiere_ecran_etat `:host` — ajout 'Allumé & Sync.'/'Synchro.' [s16]
  ✅ [B2] SDB use_number undefined — {% set use_number = false %} ajouté [s16]
  ✅ [B3] Pastille Ecran — display:none si état ≠ Écran|Allumé [s16]
  ℹ️ Compteur Chambre dynamique : total 1 si prise OFF / 3 si prise ON (bougies)
  ℹ️ Compteur Bureau : logique 6 états depuis sensor.bureau_etat + sensor.lumiere_ecran_etat
  ℹ️ Heading Têtes de Lit masqué si prise OFF — comportement intentionnel (pas d'alim = pas de lampes)
  ⚡ CHAÎNE ABSENCE : WiFi/Cell OFF → binary_sensor.presence_maison → automation coupe prises éco
       → Groupes 2+3+4 OFF : switch.ecran_p_c_3_play_hue OFF → carte Ecran disparaît
            ↳ Bureau (cols 6) reste visible mais badge lumiere_ecran_etat = Éco. (vert)
       → Groupes 3+4 OFF   : switch.prise_tete_de_lit_chambre OFF → heading + carte Têtes de Lit disparaissent
       (logique amont : P4_groupe_presence / docs/WIFI_PRESENCE)
```

---

### ✅ L3C2 — Commandes Éco (Prises)
`docs/L3C2_PRISES/`

```
L3C2 Prises
  ├── Vignette (custom:button-card — grid 2 cols Pièce / État)
  │     ├── [NAT] switch.prise_horloge_ikea          (IKEA — 1. ENTRÉE)
  │     ├── [NAT] light.hue_smart_eco_salon           (Hue — 4. SALON)
  │     ├── [NAT] switch.prise_tv_salon_ikea          (IKEA — 4. SALON)
  │     ├── [NAT] switch.hue_smart_eco_pc_bureau      (Hue — 7. BUREAU)
  │     ├── [NAT] light.hue_smart_eco_tv_chambre      (Hue — 9. CHAMBRE)
  │     └── [NAT] switch.prise_tete_de_lit_chambre    (9. CHAMBRE)
  └── Page /dashboard-tablette/prises ✅ documentée [s14]
        ├── mushroom-entity-card × 6 (toggle W/A/V badges + animation)
        │     ├── [NAT] switch.prise_horloge_ikea → sensor.prise_horloge_ikea_*
        │     ├── [NAT] light.hue_smart_eco_salon → sensor.prise_salon_chargeur_nous_*
        │     ├── [NAT] switch.prise_tv_salon_ikea → sensor.prise_tv_salon_ikea_* (🐛 corr. L2)
        │     ├── [NAT] switch.hue_smart_eco_pc_bureau → sensor.prise_bureau_pc_ikea_*
        │     ├── [NAT] light.hue_smart_eco_tv_chambre → sensor.prise_tv_chambre_nous_*
        │     └── [NAT] switch.prise_tete_de_lit_chambre → sensor.prise_tete_de_lit_chambre_*
        └── streamline-card template: nav_bar

  ⚠️ Mix domaines : 2 entités light.* + 4 switch.* — état on/off compatible JS
  ✅ [L1] TV Salon : show_ma = ture → voulu (affichage mA — confirmé s14)
  🐛 [L2] TV Salon : sensor.light.hue_smart_tv_salon_* → entity_id invalide
  ⚠️ [L3] Salon : light.hue_smart_eco_salon togglee mais capteurs = prise_salon_chargeur_nous — à vérifier
```

---

### ✅ L3C3 — Fenêtres + Stores
`docs/L3C3_STORES/`

```
L3C3 Fenêtres / Stores
  ├── Vignette (button-card 3 colonnes Pièce / Fenêtres / Stores)
  │     ├── [NAT] binary_sensor.contact_fenetre_* × 4 (SONOFF SNZB-04)
  │     └── [TPL] sensor.store_salon_status / sensor.store_bureau_status
  └── Page /stores (2 sections — Salon + Bureau)
        ├── enhanced-shutter-card
        │     └── [NAT] cover.store_salon / cover.store_bureau (Zigbee2MQTT)
        │     └── [NAT] sensor.store_*_signal_strength
        ├── Boutons position rapide (5 × cover.set_cover_position)
        │     └── Mapping non-linéaire calibré (Salon: 100/85/70/49/20, Bureau: 100/90/60/45/25)
        ├── Conditions affichées
        │     └── [NAT] sensor.th_balcon_nord_temperature (SONOFF SNZB-02 balcon)
        ├── Batteries contacts
        │     └── [NAT] sensor.contact_fenetre_salon/bureau_sonoff_battery
        └── DnD voyants commandes
              └── [NAT] light.store_salon_dnd / light.store_bureau_dnd (helpers UI)
```

---

## LIGNE 4 — RÉSEAU & SYSTÈME

### ✅ L4C1 — Freebox Pop
`docs/L4C1_FREEBOX/`

```
L4C1 Freebox
  ├── Vignette (custom:button-card — navigation pure, pas d'entité live)
  ├── Page /systeme-freebox
  │     ├── Bloc Speedtest
  │     │     ├── Déclencheur manuel → homeassistant.update_entity
  │     │     │     └── [NAT] sensor.speedtest_cli_data (Speedtest CLI)
  │     │     │     └── [NAT] sensor.speedtest_download (Speedtest CLI)
  │     │     └── Bouton popup → #speedtest_details
  │     └── Bloc Freebox info (stack-in-card)
  │           ├── [NAT] device_tracker.freebox_v8_r1 (attr: IPv4, IPv6, uptime, connection_type, firmware_version)
  │           ├── [NAT] sensor.freebox_download_speed
  │           ├── [NAT] sensor.freebox_upload_speed
  │           ├── [NAT] sensor.freebox_temperature_1
  │           └── [NAT] sensor.freebox_temperature_cpu_b
  └── Pop-up #speedtest_details (Historique 24h Download/Upload/Ping)
        ├── [NAT] sensor.speedtest_cli_data (attr: isp, server.name/location/country)
        ├── [TPL] sensor.speedtest_cli_download  → templates/SpeedTest/ST_01_speedTest.yaml
        ├── [TPL] sensor.speedtest_cli_upload    → templates/SpeedTest/ST_01_speedTest.yaml
        └── [TPL] sensor.speedtest_cli_ping      → templates/SpeedTest/ST_01_speedTest.yaml

✅ ST_01_speedTest.yaml présent sur GitHub [confirmé s13]
⚠️ Page originellement optimisée pour Raspberry Pi — ajustements possibles sur x86-64
```

---

### ✅ L4C2 — Mini PC
`docs/L4C2_MINI_PC/`

```
L4C2 Mini PC (Vignette — nom "Mini PC", icône phu:intel-nuc)
  ├── T° CPU + icône couleur (< 65 vert / 65-74 orange / ≥ 75 rouge)
  │     └── [NAT] sensor.system_monitor_temperature_du_processeur
  ├── CPU % / RAM % / Disk %
  │     └── [NAT] sensor.system_monitor_utilisation_du_processeur
  │     └── [NAT] sensor.system_monitor_utilisation_de_la_memoire
  │     └── [NAT] sensor.system_monitor_utilisation_du_disque
  └── Power W (prise IKEA Inspelning)
        └── [NAT] sensor.prise_mini_pc_ikea_power

L4C2 Mini PC (Page /raspberry-pi4 — TRANSITOIRE ancienne page RPi4)
  ├── Image RPi4B3.png [local/images/]
  ├── IP locale / publique
  │     └── [NAT] sensor.local_ip / sensor.myip
  ├── Uptime (depuis dernier boot)
  │     └── [NAT] sensor.system_monitor_dernier_demarrage
  ├── Ventilateur RPi (état + toggle + %)
  │     └── [NAT] fan.rpi_cooling_fan  ← ⚠️ RPi4 uniquement
  ├── Bar-cards (CPU%, T°, Mem USED/FREE MB, SSD Go, DL/UL MB/s)
  │     └── [NAT] system_monitor + sensor.system_monitor_*
  ├── Uptime-card 48h
  │     └── [NAT] binary_sensor.rpi_power_status  ← ⚠️ RPi4 uniquement
  ├── 6 boutons commandes ventilateur (30/40/50/65/85/100%)
  │     └── [NAT] fan.rpi_cooling_fan  ← ⚠️ RPi4 uniquement — à migrer
  └── Automation régulation ventilateur (DÉPENDANCE VISUELLE)
        └── [AUTO] automation.raspberry_cpu_fan_pwm_6_states
              ← alias : "Raspberry CPU Fan PWM 6 States"
              ← 6 paliers : ≥30°C→30% / ≥40°C→50% / ≥50°C→70% / ≥60°C→85% / ≥70°C→100%
              ← pilote fan.set_percentage selon T° CPU
              ← le % affiché + animation rotation = reflet de cette automation
              ← ⚠️ RPi4 uniquement — à ne pas migrer Mini PC

⚠️ PAGE_RASPI.md = page temporaire. Remplacée par PAGE_MINI_PC.md (créée s21).

L4C2 Mini PC (Page définitive — Mini PC Intel NUC)
  ├── Image /local/images/mini pc.png
  ├── IP locale / publique + Uptime
  │     └── [NAT] sensor.local_ip / sensor.myip
  │     └── [NAT] sensor.system_monitor_dernier_demarrage
  ├── Bar-cards CPU USED + Temp (system_monitor)
  │     └── [NAT] sensor.system_monitor_utilisation_du_processeur
  │     └── [NAT] sensor.system_monitor_temperature_du_processeur
  ├── Bar-cards RAM % + USED/FREE (16 Go max)
  │     └── [NAT] sensor.system_monitor_utilisation_de_la_memoire
  │     └── [NAT] sensor.system_monitor_memoire_utilisee / _libre
  ├── Bar-card SSD SATA 512 Go (524 Go max)
  │     └── [NAT] sensor.system_monitor_utilisation_du_disque
  ├── Bar-cards DL / UL via enp1s0
  │     └── [NAT] sensor.system_monitor_debit_du_reseau_entrant_via_enp1s0
  │     └── [NAT] sensor.system_monitor_debit_du_reseau_sortant_via_enp1s0
  ├── ring-tile + mini-graph : CPU Utilisation 24h
  │     └── [NAT] sensor.system_monitor_utilisation_du_processeur
  ├── Bar-card CPU SPEED (GHz)
  │     └── ⚠️ sensor.cpu_speed (provenance à confirmer — command_line probable)
  ├── Bar-cards Charges système 1m / 5m / 15m
  │     └── ⚠️ sensor.system_monitor_charge_1m/5m/15m (à activer config)
  ├── ring-tile + mini-graph : Température CPU 24h
  │     └── ⚠️ sensor.temperature_cpu_package_sys (command_line thermal zone)
  ├── Bar-cards Températures cores (Core 0/1/2/3)
  │     └── ⚠️ sensor.temperature_core_0/1/2_sys + sensor.temperature_core_3_sys_2
  ├── Bar-card Température Carte Mère
  │     └── ⚠️ sensor.temperature_carte_mere_sys (command_line thermal zone)
  ├── ring-tile + mini-graph : Conso. W 24h
  │     └── [NAT] sensor.prise_mini_pc_ikea_power (Zigbee2MQTT)
  └── 5 pop-ups : #speed / #temp / #conso / #disk / #memory
        ├── [NAT] sensor.system_monitor_* (apexcharts CPU, T°, disk, RAM)
        └── streamline conso_temps_reel + conso_mensuelle (prise IKEA)
              ├── ⚠️ sensor.mini_pc_quotidien/mensuel (UM à créer P2_UM_AMHQ_mini_pc)
              └── ⚠️ sensor.mini_pc_avg_watts_quotidien/mensuel (AVG à créer P2_AVG_AMHQ_mini_pc)

✅ PAGE_MINI_PC.md créée [s21 — 2026-03-25]
⚠️ Sensors spéciaux (temperature_*_sys, cpu_speed, charge_*) = à vérifier lors migration
⚠️ UM + AVG prise Mini PC = à ajouter dans fichiers P2
```

---

### ✅ L4C3 — Mises à jour HA
`docs/L4C3_MAJ_HA/`

```
L4C3 MAJ HA
  ├── Vignette (button-card)
  │     └── [TPL] templates/utilitaires/Mise_a_jour_home_assistant.yaml
  │           └── sensor.available_updates
  │                 └── [NAT] update.* (domaine natif HA — state == 'on')
  └── Page /dashboard-tablette/maj
        ├── Grille 1 — H.A. SERVER
        │     ├── [NAT] update.home_assistant_core_update
        │     ├── [NAT] update.home_assistant_operating_system_update
        │     ├── [NAT] update.home_assistant_supervisor_update
        │     └── [NAT] update.hacs_update (HACS)
        └── Grille 2 — H.A. UPDATE
              ├── [NAT] update.* filtrés par intégration (hassio / hacs / mqtt)
              └── [NAT] sensor.processor_use + sensor.memory_use_percent
```

---

## LIGNE 5 — MAINTENANCE MATÉRIELLE

### ✅ L5C1 — Batteries / Piles
`docs/L5C1_PILES_BATTERIES/`

```
L5C1 Batteries
  └── [NAT] sensor.*_battery (%) — 34 capteurs
        └── groups.yaml
              ├── group.ikea_devices  (12 capteurs)
              ├── group.hue_devices   (11 capteurs)
              └── group.sonoff_devices (11 capteurs)
```

---

### ✅ L5C2 — Batteries Portables
`docs/L5C2_BATTERIES_PORTABLES/`

> ⚠️ Label corrigé : "Batterie Portail" → "Batteries Portables" — le contenu réel est la surveillance des téléphones mobiles.

```
L5C2 Batteries Portables
  ├── Vignette (custom:button-card — grid 3 cols : Appareil / Niveau% / État)
  │     ├── [NAT] sensor.poco_x7_pro_battery_level / _state
  │     ├── [NAT] sensor.poco_x7_pro_mamour_battery_level / _state
  │     ├── [NAT] sensor.ne2213_eric_battery_level / _state
  │     ├── [NAT] sensor.ne2213_mamour_battery_level / _state
  │     ├── [NAT] sensor.gm1901_battery_level / _state
  │     ├── [NAT] sensor.sm_a530f_battery_level / _state
  │     └── [NAT] sensor.tablette_battery_level / _state
  └── Page /phone (2 grilles : Eric conditional / Mamour sans conditional)
        ├── Grille Eric (4 appareils — conditional si unavailable/unknown)
        │     ├── POCO X7 Pro (E)   : streamline portable + 7 entités
        │     ├── NE2213 Eric       : streamline portable + 7 entités
        │     ├── SM-A530F          : streamline portable + 5 entités (pas réseau)
        │     └── Tablette          : streamline portable + 5 entités (pas réseau)
        └── Grille Mamour (3 appareils — pas de conditional)
              ├── POCO X7 Pro (M)   : streamline portable + 7 entités
              ├── NE2213 Mamour     : streamline portable + 7 entités
              └── GM1901            : streamline portable + 7 entités

  → Toutes entités natives Android Companion App (aucun YAML)
  → custom:streamline-card template: portable requis
```

---

### ✅ L5C3 — MariaDB
`docs/L5C3_MARIADB/`

```
L5C3 MariaDB
  └── [NAT] sensor.taille_db_home_assistant
        └── sql.yaml → MariaDB (secrets.yaml: mariadb_url)
```

---

## LIGNE 6 — QUALITÉ & ALERTES

### ✅ L6C1 — Qualité de l'air (Appartement)
`docs/L6C1_AIR_QUALITE/`

```
L6C1 Air intérieur
  ├── Vignette (custom:button-card 9 lignes × 3 cols — PM2.5 + tCOV × 3 pièces)
  │     ├── [NAT] sensor.qualite_air_salon_ikea_pm25         (IKEA Vindstyrka)
  │     ├── [NAT] sensor.qualite_air_salon_ikea_voc_index    (IKEA Vindstyrka)
  │     ├── [NAT] sensor.qualite_air_bureau_ikea_pm25        (IKEA Vindstyrka)
  │     ├── [NAT] sensor.qualite_air_bureau_ikea_voc_index   (IKEA Vindstyrka)
  │     ├── [NAT] sensor.qualite_air_chambre_ikea_pm25       (IKEA Vindstyrka)
  │     └── [NAT] sensor.qualite_air_chambre_ikea_voc_index  (IKEA Vindstyrka)
  └── Page /air-quality (3 sections Salon / Bureau / Chambre)
        ├── Ring-tile PM2.5 (custom:streamline-card — template: pm25_ring-tile)
        │     ├── entity   → [NAT] sensor.qualite_air_*_ikea_pm25
        │     └── marker2  → [SNS] sensor.pm2_5_*_moy_24h
        │                         sensors/air_qualite/pm25_tcov_moy_24h.yaml
        │                         platform: statistics — mean — max_age: 24h
        ├── Ring-tile tCOV (custom:streamline-card — template: cov_ring-tile)
        │     ├── entity   → [TPL] sensor.tcov_*_ppb
        │     │                    templates/air_qualite/tcov_ppb.yaml
        │     │                    device_class: volatile_organic_compounds_parts
        │     │                    source → [NAT] sensor.qualite_air_*_ikea_voc_index
        │     └── marker2  → [SNS] sensor.tcov_*_moy_24h
        │                         sensors/air_qualite/pm25_tcov_moy_24h.yaml
        ├── Boutons pop-up PM2.5 / tCOV (custom:bubble-card button — hash #*pm25 / #*cov)
        └── Pop-ups graphiques (vertical-stack — bubble-card pop-up + streamline-card)
              ├── template: pm25 — entity_sensor: [NAT] sensor.qualite_air_*_ikea_pm25
              │                    mean_24h_entity: [SNS] sensor.pm2_5_*_moy_24h
              └── template: cov  — entity_sensor: [NAT] sensor.qualite_air_*_ikea_voc_index
                                   mean_24h_entity: [SNS] sensor.tcov_*_moy_24h
```

---

### ✅ L6C2 — Pollution / Pollen (Extérieur) — Pollulèn ©
`docs/L6C2_POLLUTION_POLLEN/`

```
L6C2 Pollulèn ©
  ├── Vignette (custom:button-card — name JS dynamique, échelle 0-7 bicolore)
  │     ├── [NAT] sensor.qualite_globale_vence        (indice air 0-7, attr: Libellé+Couleur)
  │     └── [NAT] sensor.qualite_globale_pollen_vence (indice pollen 0-7, attr: Libellé+Couleur)
  └── Page /pollen-pollution (column_span: 10)
        ├── Section POLLENS
        │     ├── entity-progress-card → sensor.qualite_globale_pollen_vence
        │     └── Grid 3 cols — 6 ring-tile espèces (concentration + niveau)
        │           Graminées / Ambroisie / Armoise / Aulne / Bouleau / Olivier
        │           sensor.concentration_*_vence + sensor.niveau_*_vence
        └── Section QUALITÉ DE L'AIR
              ├── entity-progress-card → sensor.qualite_globale_vence
              └── Grid 5 cols — 5 ring-tile polluants
                    sensor.ozone_vence / dioxyde_d_azote / dioxyde_de_soufre / pm10 / pm25

  → Toutes entités natives AtmoFrance HACS (custom_components/atmofrance — station Vence)
  ✅ Typo corrigée : ring_type: open (capteur O₃) — dashbord_2026-03-20.yalm L29251
```

---

### ✅ L6C3 — Vigilance Eau (Vigieau)
`docs/L6C3_VIGIEAU/`

```
L6C3 Vigieau
  ├── Vignette (custom:button-card — code à fournir)
  │     ├── [NAT] sensor.alert_level_in_vence          (état textuel)
  │     └── [NAT] sensor.alert_level_in_vence_numeric  (0→4, attr: Couleur + icon)
  └── Page /vigieau (section SÉCHERESSE)
        ├── custom:button-card — couleur fond dynamique
        │     └── [NAT] sensor.alert_level_in_vence
        │           États : null / vigilance / alerte / alerte_renforcee / crise
        ├── custom:bar-card
        │     └── [NAT] sensor.alert_level_in_vence_numeric (attr: Couleur)
        └── custom:auto-entities (grid 4 colonnes)
              └── [NAT] sensor.*_restrictions_vence
                    États : Aucune restriction / Sensibilisation /
                            Interdiction sauf exception / Interdiction

  → Toutes entités natives Vigieau HACS (custom_components/vigieau — commune Vence)
  ✅ browser_mod.popup OK — fire-dom-event v1 fonctionnel (intégration installée + navigateur rechargé)
  ✅ Typo corrigé : rgb(254, 178, 76) — état alerte [s12]
  ✅ Page Vigieau fonctionnelle en production [s13]
  ✅ Vignette documentée — L6C3_VIGNETTE_VIGIEAU.md complété [s13]
  ⚠️ Bug corrigé vignette : case 'vigilance' manquait un break — fallthrough vers alerte_renforcee [L1 s13]
```

---

## PAGE HOME (Racine du dashboard)

> 📄 Doc complète : [`docs/WIFI_PRESENCE (Home Page)/PAGE_HOME.md`](./WIFI_PRESENCE%20(Home%20Page)/PAGE_HOME.md)

### ✅ WIFI / Présence
`docs/WIFI_PRESENCE (Home Page)/`

```
Présence
  ├── Détection Wi-Fi
  │     └── [TPL] P4_groupe_presence/02_logique_wifi_cellular.yaml
  │           └── [NAT] device_tracker.* (intégration router / nmap)
  └── Carte état téléphones
        └── [TPL] P4_groupe_presence/01_phones_wifi_cellular_card_autom.yaml
```

---

> 📋 **Statut des pages et vignettes** → voir [[INDEX_PAGES]]

<!-- obsidian-wikilinks -->
---
*Liens : [[WORKFLOW_REBUILD]]  [[CONFIG_ROOT]]  [[INDEX_PAGES]]*
