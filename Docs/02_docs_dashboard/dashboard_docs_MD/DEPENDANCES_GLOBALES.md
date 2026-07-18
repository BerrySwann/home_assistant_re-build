# 🔗 DÉPENDANCES GLOBALES — TABLEAU DE BORD HA
*Dernière mise à jour : 2026-07-18 (Nettoyage résidu chambre : capteur MQTT dispo + bloc mqtt: de configuration.yaml + dossier mqtt/, local + prod H:\)*
*2026-07-17 (Resync local ← GitHub/prod : configuration.yaml + scripts.yaml — fix chambre script J-2-0)*

---

## LÉGENDE

| Symbole | Signification |
|:-------:|:-------------|
| ✅ | Chaîne validée et opérationnelle |
| 🔲 | À documenter |
| ⚠️ | Rupture de chaîne ou entité obsolète — ex : `source:` pointe vers une entité supprimée/renommée, `unique_id` dupliqué, fichier YAML présent en prod mais absent de `TREE_CORRIGE`, ou entité référencée dans le dashboard mais inexistante dans HA |
| NAT | Entité native HA (intégration directe) |
| TPL | Template (`templates/`) |
| UM | Utility Meter (`utility_meter/`) |
| SEN | Sensor (`sensors/`) |

---

## MATRICE DES 18 VIGNETTES — STATUT DÉPENDANCES

| ID | Vignette | Statut |
|:---|:---------|:------:|
| **L1C1** | **Météo** | ✅ |
| **L1C2** | **Températures** | ✅ |
| **L1C3** | **Commandes Clim** | ✅ |
| **L2C1** | **Énergie Générale** | ✅ |
| **L2C2** | **Énergie Clim / Rad / Soufflant** | ✅ |
| **L2C3** | **Énergie Éclairage** | ✅ |
| **L3C1** | **Commandes Éclairage** | ✅ |
| **L3C2** | **Commandes Éco/Prises** | ✅ |
| **L3C3** | **Stores / Fenêtres** | ✅ |
| **L4C1** | **Proxmox PVE** | ✅ |
| **L4C2** | **Mini-PC** | ✅ |
| **L4C3** | **Mises à jour HA** | ✅ |
| **L5C1** | **Batteries / Piles** | ✅ |
| **L5C2** | **Batteries portables** | ✅ |
| **L5C3** | **MariaDB** | ✅ |
| **L6C1** | **Qualité de l'air** | ✅ |
| **L6C2** | **Pollution / Pollen** | ✅ |
| **L6C3** | **Vigilance Eau** | ✅ |

---

## ✅ L1C1 — MÉTÉO (VIGNETTE + PAGE)
*Validée le 2026-05-09*

### Vignette — Chaîne de dépendances

```
AUCUNE ENTITÉ — Vignette purement navigationnelle
  └─→ tap_action: navigate → /dashboard-tablette/meteo
        └─→ PAGE MÉTÉO DÉTAILLÉE (voir ci-dessous)
```

> La vignette `custom:button-card` est statique : icône `mdi:weather-partly-cloudy`, nom "Météo".
> Aucun `triggers_update`, aucun `custom_fields`, aucune entité référencée.

### Page — Chaîne de dépendances

```
MATÉRIEL / INTÉGRATION
  ├─→ Météo France (intégration officielle)
  │     └─→ sensor.meteo_france_*  (NAT)
  ├─→ command_line: carte_meteo_france.yaml
  │     └─→ camera.carte_vigilance_meteo_france  (command_line → image URL)
  ├─→ Blitzortung (intégration HACS)
  │     └─→ sensor.blitzortung_lightning_*  (NAT)
  │           └─→ UM: M_03_meteo_UM_blitzortung.yaml  (compteurs foudre AMHQ)
  │           └─→ TPL: M_03_meteo_blitzortung.yaml  (card_content HTML)
  ├─→ SONOFF (Z2M — balcon nord)
  │     └─→ sensor.th_balcon_nord_temperature / _humidity  (NAT)
  │           └─→ TPL: M_04_tendances_th_ext_card.yaml  (tendances mini-graph)
  ├─→ Météo France (alertes)
  │     └─→ binary_sensor.meteo_france_alerte_*  (NAT)
  │           └─→ TPL: M_01_meteo_alertes_card.yaml  (card HTML couleurs)
  ├─→ Météo France (vent)
  │     └─→ sensor.meteo_france_wind_speed / _bearing  (NAT)
  │           └─→ TPL: M_02_meteo_vent_vence_card.yaml  (windrose-card HTML)
  └─→ sun.sun  (HA natif)
        └─→ sensor.sun_next_rising / next_setting  (NAT)
              └─→ apexcharts-card (data_generator JS — courbe durée du jour)
```

### Entités consommées par la page

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `camera.carte_vigilance_meteo_france` | NAT | `command_line/meteo/carte_meteo_france.yaml` |
| `sensor.meteo_france_*` (prévisions) | NAT | Intégration Météo France |
| `sensor.blitzortung_lightning_distance` | NAT | Intégration Blitzortung |
| `sensor.blitzortung_lightning_count` | NAT | Intégration Blitzortung |
| `sensor.meteo_france_blitzortung_count_quotidien` | UM | `utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml` |
| `sensor.meteo_france_alerte_card_content` | TPL | `templates/meteo/M_01_meteo_alertes_card.yaml` |
| `sensor.meteo_france_vent_vence_card_content` | TPL | `templates/meteo/M_02_meteo_vent_vence_card.yaml` |
| `sensor.blitzortung_card_content` | TPL | `templates/meteo/M_03_meteo_blitzortung.yaml` |
| `sensor.tendances_th_ext_card_content` | TPL | `templates/meteo/M_04_tendances_th_ext_card.yaml` |
| `sensor.th_balcon_nord_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_balcon_nord_humidity` | NAT | SONOFF via Z2M |
| `sun.sun` | NAT | HA Core |
| `sensor.variation_quotidienne` | NAT | Météo France (variation durée jour) |

### Entités ApexCharts (data_generator JS — durée du jour)

| Données | Source | Note |
|:--------|:-------|:-----|
| Durée du jour (courbe annuelle théorique) | Calcul JS astronomique | `lat = 43.72°N` — formule déclinaison + angle horaire |
| Gain/Perte quotidien (area smooth) | Calcul JS différentiel | Plage complète 365j — pas de `extend_to` |
| `sensor.sun_next_rising` | NAT | Lever réel (graphe historique) |
| `sensor.sun_next_setting` | NAT | Coucher réel (graphe historique) |

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L1C1_01_Meteo/vignette_L1C1_meteo_2026-05-09.yaml` | ✅ |
| `Dashboard/L1C1_01_Meteo/page_L1C1_meteo_2026-05-09.yaml` | ✅ |
| `command_line/meteo/carte_meteo_france.yaml` | ✅ |
| `utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml` | ✅ |
| `templates/meteo/M_01_meteo_alertes_card.yaml` | ✅ |
| `templates/meteo/M_02_meteo_vent_vence_card.yaml` | ✅ |
| `templates/meteo/M_03_meteo_blitzortung.yaml` | ✅ |
| `templates/meteo/M_04_tendances_th_ext_card.yaml` | ✅ |

---

## ✅ L1C2 — TEMPÉRATURES (VIGNETTE + PAGE)
*Validée le 2026-05-13*

### Vignette — Chaîne de dépendances

```
MATÉRIEL (SONOFF TH via Z2M)
  └─→ sensor.th_*_temperature / _humidity  (NAT — 7 pièces)
        └─→ VIGNETTE L1C2 (button-card — grille piece/temp/humidite)
              └─→ tap_action: navigate → /dashboard-tablette/temperatures
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.th_balcon_nord_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_balcon_nord_humidity` | NAT | SONOFF via Z2M |
| `sensor.th_salon_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_salon_humidity` | NAT | SONOFF via Z2M |
| `sensor.th_cellier_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_cellier_humidity` | NAT | SONOFF via Z2M |
| `sensor.th_cuisine_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_cuisine_humidity` | NAT | SONOFF via Z2M |
| `sensor.th_bureau_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_bureau_humidity` | NAT | SONOFF via Z2M |
| `sensor.th_salle_de_bain_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_salle_de_bain_humidity` | NAT | SONOFF via Z2M |
| `sensor.th_chambre_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_chambre_humidity` | NAT | SONOFF via Z2M |

### Page — Entités clés supplémentaires

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.vence_temperature` | NAT | Météo France |
| `sensor.temperature_moyenne_interieure` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.temperature_delta_affichage` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.th_*_temperature_trend` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.th_*_humidity_trend` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.conso_clim_rad_total` | TPL | `P1_TOTAL/P1_TOTAL_AMHQ.yaml` |
| `sensor.conso_clim_rad_total_quotidien` | TPL | `P1_TOTAL/P1_TOTAL_AMHQ.yaml` |
| `sensor.conso_clim_rad_total_mensuel` | TPL | `P1_TOTAL/P1_TOTAL_AMHQ.yaml` |
| `sensor.clim_rad_total_avg_watts_quotidien` | TPL | `P1_AVG/P1_AVG_TOTAL_AMHQ.yaml` |
| `sensor.*_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.clim_*_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `climate.clim_salon_rm4_mini` | NAT | SmartIR |
| `climate.radiateur_cuisine` | NAT | Meross |
| `climate.clim_bureau_rm4_mini` | NAT | SmartIR |
| `climate.clim_chambre_rm4_mini` | NAT | SmartIR |

### Streamline templates utilisés

| Template | Rôle |
|:---------|:-----|
| `temperature_humidite` | Affichage T°+Humidité par pièce |
| `calcule_temp_cible` | Pop-up #tendances — calcul T° cible *(corrigé 2026-06-21 : entités + logique cool)* |
| `carte_des_temperatures` | Pop-ups #salon/#bureau/etc — historique T° |

> ⚠️ **Flag** : `custom:temperature-heatmap-card` utilisé dans le pop-up `#exterieur` — **absent du référentiel HACS officiel**. À vérifier / ajouter si installé.

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L1C2_02_Temperatures/vignette_L1C2_temperatures_2026-05-12.yaml` | ✅ |
| `Dashboard/L1C2_02_Temperatures/page_L1C2_temperatures_2026-05-22.yaml` | ⚠️ obsolète — `climate.clim_chambre_rm4_mini` |
| `Dashboard/L1C2_02_Temperatures/page_L1C2_temperatures_2026-07-14.yaml` | ✅ `climate.clim_chambre_rm4_mini` + `sensor.temperature_corrige_chambre` |

---

## ✅ L1C3 — COMMANDES CLIM (VIGNETTE + PAGE)
*Validée le 2026-05-13 - chambre sur `climate.clim_chambre_rm4_mini` depuis le 2026-07-14*

### Vignette — Chaîne de dépendances

```
MATÉRIEL (NOUS SP via Z2M + SmartIR + Meross)
  └─→ sensor.*_power / climate.*   (NAT)
        └─→ TPL: P1_ui_dashboard.yaml  (*_power_status / *_etat)
              └─→ sensor.temperature_moyenne_interieure  (TPL P1_ui_dashboard)
              └─→ sensor.delta_ademe_recommande          (TPL P1_clim_logique)
              └─→ sensor.mode_ete_hiver_etat             (TPL P1_clim_logique)
                    └─→ VIGNETTE L1C3 (button-card — grille piece/mode/consigne)
                          └─→ tap_action: navigate → /dashboard-tablette/clim
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.temperature_moyenne_interieure` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.delta_ademe_recommande` | TPL | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.mode_ete_hiver_etat` | TPL | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.clim_salon_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.radiateur_cuisine_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.clim_bureau_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.sdb_soufflant_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.sdb_seche_serviette_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.clim_chambre_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.salon_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.cuisine_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.bureau_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.sdb_soufflant_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.sdb_seche_serviette_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.chambre_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `climate.clim_salon_rm4_mini` | NAT | SmartIR |
| `climate.radiateur_cuisine` | NAT | Meross |
| `climate.clim_bureau_rm4_mini` | NAT | SmartIR |
| `climate.soufflant_salle_de_bain` | NAT | Meross |
| `climate.clim_chambre_rm4_mini` | NAT | SmartIR |

### Entités clés de la page

| Entité | Type | Rôle |
|:-------|:----:|:-----|
| `sensor.conso_clim_rad_total` | TPL | Bar-card puissance totale P1 |
| `sensor.*_nous_power` (×4 clims) | NAT | Bar-cards puissance individuelle |
| `sensor.radiateur_elec_cuisine_power` | NAT | Bar-card puissance cuisine |
| `sensor.prise_soufflant_salle_de_bain_nous_power` | NAT | Bar-card puissance SdB |
| `input_boolean.clim_*_arret_securise_en_cours` | NAT | Bandeaux avertissement arrêt sécurisé |
| `sensor.*_power_lock` | TPL | Verrou script J-2-0 |
| `sensor.*_power_status_affichage` | TPL | Conditional prise coupée |
| `switch.clim_*_nous` | NAT | Badge power + script J-1-x |
| `remote.clim_*` | NAT | Badge état télécommande IR |
| `switch.schedule_clim_*` | NAT | Badges planificateur Sem./W-E |
| `input_select.etat_resistance_soufflant_sdb` | NAT | Affichage puissance soufflant (0/1000/2000W) |
| `switch.inter_soufflant_salle_de_bain` | NAT | Affichage conditionnel soufflant |
| `sensor.th_salle_de_bain_temperature` | NAT | Delta T°/consigne soufflant |

### Scripts appelés depuis la page

| Script | Déclencheur | Statut |
|:-------|:------------|:------:|
| `script.j_1_1_salon_clim_on_off_intelligent` | Badge power Salon | ✅ |
| `script.j_1_2_bureau_clim_on_off_intelligent` | Badge power Bureau | ✅ |
| `script.j_1_3_chambre_clim_on_off_intelligent` | Badge power Chambre | ✅ |
| `script.j_2_0_secu_arret_clim_protege` | Verrou sécurité (déclenché en interne, pas depuis un badge) | ✅ *(fix 2026-07-17 : `clim_entity` chambre — condition spéciale ajoutée pour pointer sur `climate.clim_chambre_rm4_mini` au lieu du pattern générique `climate.clim_{{p}}_rm4_mini`, synchronisé depuis prod/GitHub)* |

### Streamline templates utilisés

| Template | Rôle |
|:---------|:-----|
| `calcule_temp_cible` | Pop-up `#calcul` — delta intérieur/extérieur *(corrigé 2026-06-21)* |
| `nav_bar` | Barre de navigation bas de page |

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L1C3_03_Commandes_Clim/vignette_L1C3_clim_2026-05-13.yaml` | ⚠️ obsolète (rm4_mini) |
| `Dashboard/L1C3_03_Commandes_Clim/page_L1C3_clim_2026-05-13.yaml` | ⚠️ obsolète (rm4_mini) |
| `Dashboard/L1C3_03_Commandes_Clim/page_L1C3_clim_2026-05-22.yaml` | ⚠️ obsolète (rm4_mini) |
| `Dashboard/L1C3_03_Commandes_Clim/vignette_L1C3_clim_2026-07-08.yaml` | ✅ chambre → rm4_mini (revert 2026-07-14) |
| `Dashboard/L1C3_03_Commandes_Clim/page_L1C3_clim_2026-07-08.yaml` | ✅ chambre → rm4_mini (revert 2026-07-14) |

### Entités Chambre (RM4 Mini)

| Entité | Type | Rôle |
|:-------|:----:|:-----|
| `climate.clim_chambre_rm4_mini` | Climate (Broadlink) | Thermostat chambre — actif |
| `sensor.temperature_corrige_chambre` | TPL | Consigne chambre affichée dans vignette L1C3 |
| `Dashboard/L1C3_03_Commandes_Clim/card_prog_clim_salon_2026-07-14.yaml` | ✅ |
| `Dashboard/L1C3_03_Commandes_Clim/card_prog_radiateur_cuisine_2026-07-14.yaml` | ✅ |
| `Dashboard/L1C3_03_Commandes_Clim/card_prog_clim_bureau_2026-07-14.yaml` | ✅ |
| `Dashboard/L1C3_03_Commandes_Clim/card_prog_soufflant_sdb_2026-07-14.yaml` | ✅ |
| `Dashboard/L1C3_03_Commandes_Clim/card_prog_clim_chambre_2026-07-14.yaml` | ✅ |

### Entités Scheduler consommées — Programmation manuelle (ajout 2026-07-14)

| Entité | Equipment | Type |
|:-------|:----------|:-----|
| `switch.schedule_clim_du_salon_week` | Clim Salon | Scheduler (Semaine) |
| `switch.schedule_clim_du_salon_week_end` | Clim Salon | Scheduler (Week-End) |
| `switch.schedule_radiateur_cuisine_week` | Radiateur Cuisine | Scheduler (Semaine) |
| `switch.schedule_radiateur_cuisine_week_end` | Radiateur Cuisine | Scheduler (Week-End) |
| `switch.schedule_clim_du_bureau_week` | Clim Bureau | Scheduler (Semaine) |
| `switch.schedule_clim_du_bureau_week_end` | Clim Bureau | Scheduler (Week-End) |
| `switch.schedule_soufflant_salle_de_bain_week` | Soufflant SdB | Scheduler (Semaine) |
| `switch.schedule_soufflant_salle_de_bain_week_end` | Soufflant SdB | Scheduler (Week-End) |
| `switch.schedule_clim_de_la_chambre_week` | Clim Chambre | Scheduler (Semaine) |
| `switch.schedule_clim_de_la_chambre_week_end` | Clim Chambre | Scheduler (Week-End) |

### Automations liées (P1 clim chauffage)

| Fichier | Alias | Statut | Modifié le |
|:--------|:------|:------:|:-----------|
| `docs_automations/TREE_CORRIGE/P1_clim_chauffage/a_0_2026_01_11_automatisation_clim_jour_07h30_21h00.yaml` | (A-0) CLIM JOUR | ✅ | 2026-06-21 |
| `docs_automations/TREE_CORRIGE/P1_clim_chauffage/b_0_2026_01_11_automatisation_clim_nuit_21h00_07h30.yaml` | (B-0) CLIM NUIT | ✅ | 2026-06-21 |

### Nouveaux sensors P1_MASTER — session 2026-06-21

| Entité | Type | Fichier source | Consommé par |
|:-------|:----:|:--------------|:-------------|
| `sensor.temperature_eco_ete` | TPL | `P1_MASTER_CLIM_TEMPLATES.yaml` | `temperature_eco_ete_corrige`, automations a_0/b_0 |
| `sensor.temperature_eco_ete_corrige` | TPL | `P1_MASTER_CLIM_TEMPLATES.yaml` | automations a_0 (temp_eco_ec) + b_0 (temp_eco_ec) |

### Corrections sensors P1_MASTER — session 2026-06-21

| Entité | Correction |
|:-------|:-----------|
| `sensor.temperature_corrige_mamour` | Été : `min(T°ext - 1, 27)` dynamique |
| `sensor.temperature_corrige_eric` | Été : `min(T°ext + 1, 28)` dynamique |
| `sensor.temperature_corrige_chambre` | Été : `min(T°ext + 1, 28)` — hiver : fallback `float(18)` à corriger |
| `sensor.temperature_eco_hiver_corrige` | Source corrigée : lit `temperature_eco_hiver` (était `temperature_eco_ete`) |
| `sensor.temperature_confort_jour` | À corriger : ajouter `cool` mode → retourner `base` (26°C) |

### Corrections sensors P1_MASTER — session 2026-06-29

| Entité | Correction | Statut |
|:-------|:-----------|:------:|
| `sensor.temperature_eco_ete_corrige` | Courbe validée : ≤28°C→30 / 29-32°C→29 / >32°C→28 (monotone décroissante ✓) | ✅ |
| `sensor.temperature_confort_nuit` | Seuil 29°C ajouté — zone 26-32°C scindée : ≤29→+d1(26°C) / >29→+d2(27°C) — floor nuit 27°C garanti | ✅ |

### Corrections Dashboard — session 2026-06-29

| Entité / Carte | Correction | Statut |
|:---------------|:-----------|:------:|
| `card_mod prise_tete_de_lit_chambre` | `position: relative !important` ajouté — suppression `flex/column/center` (conflit mushroom) — `watts=0` forcé si switch OFF (résidu 2W Zigbee) | ✅ |

---

## ✅ L2C1 — ÉNERGIE GÉNÉRALE (VIGNETTE + PAGE)
*Documentée le 2026-06-18*
*Source P0 depuis 2026-06-17 : Nodon SEM-4-1-00 (pince Z2M) — Ecojoko retiré*

> **Source énergie générale (depuis 2026-06-17) : Nodon SEM-4-1-00** (pince ampèremétrique Z2M)
> - `sensor.general_electric_appart_energy` (kWh) → source des UM P0
> - `sensor.general_electric_appart_power` (W) → puissance temps réel
>
> **Linky (MyElectricalData)** = J-1 uniquement (HP/HC historique) — source secondaire

### Chaîne de dépendances

```
MATÉRIEL (Nodon SEM-4-1-00 via Z2M)
  └─→ sensor.general_electric_appart_energy (kWh natif)
  └─→ sensor.general_electric_appart_power  (W natif)
        └─→ UM: 01_UM_AMHQ.yaml               (genelec_appart_*_um : Q/H/M/A)
        └─→ UM: 02_UM_genelec_appart_HPHC_AMHQ.yaml (HP/HC × 4 cycles)
              └─→ TPL: 01_genelec_appart_AMHQ_cost.yaml  (coûts € : cout_total/hp/hc_quotidien…)
              └─→ TPL: 02_ratio_hp_hc.yaml               (genelec_appart_ratio_hc_quotidien/hebdo/mensuel)
              └─→ TPL: 03_AVG_genelec_appart.yaml        (genelec_appart_avg_watts_quotidien/mensuel)
              └─→ TPL: MyElectricalData.yaml             (Linky J-1 — lecture seule)
MATÉRIEL (PowerCalc P2/P3)
  └─→ sensor.diag_poste_*_quotidien/hebdomadaire/mensuel → TPL: total_par_poste_7.yaml
  └─→ sensor.total_poste_*_puissance → TPL: total_par_poste_7.yaml
SENSORS P0
  └─→ sensor.genelec_appart_conso_mini_24h / _maxi_24h → sensors/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml
                    └─→ VIGNETTE L2C1 ✅
                    └─→ PAGE L2C1 Principale (3 onglets : Journalier/Hebdo/Mensuel) ✅
                    └─→ PAGE L2C1 Temps Réel ✅
                    └─→ PAGE L2C1 Mensuel (détail par appareil) ✅
```

### Entités consommées — Vignette L2C1

| Entité | Fichier source | Role |
|:-------|:---------------|:-----|
| `sensor.genelec_appart_conso_mini_24h` | `sensors/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml` | Min W 24h |
| `sensor.general_electric_appart_power` | Nodon SEM-4-1-00 (natif Z2M) | W temps réel |
| `sensor.genelec_appart_conso_maxi_24h` | `sensors/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml` | Max W 24h |
| `sensor.genelec_appart_cout_total_quotidien` | `templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml` | Coût € total J |
| `sensor.genelec_appart_cout_hp_quotidien` | `templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml` | Coût € HP J |
| `sensor.genelec_appart_cout_hc_quotidien` | `templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml` | Coût € HC J |

### Fichiers YAML déployables (Dashboard versionnés)

| Fichier | Taille | Navigation | Statut |
|:--------|:-------|:-----------|:------:|
| `Dashboard/L2C1_Energie/vignette_L2C1_energie_2026-06-18.yaml` | 4,4 Ko | (vignette) | ✅ |
| `Dashboard/L2C1_Energie/page_L2C1_energie_principale_2026-06-18.yaml` | 19,4 Ko | `/energie` | ✅ |
| `Dashboard/L2C1_Energie/page_L2C1_energie_temps_reel_2026-06-18.yaml` | 38,7 Ko | `/energie-temps-reel` | ✅ |
| `Dashboard/L2C1_Energie/page_L2C1_energie_mensuel_2026-06-18.yaml` | 12,5 Ko | `/energie-mensuel` | ✅ |

### Fichiers YAML impactés par changement P0 (Ecojoko → Nodon)

| Fichier | Entité modifiée | Statut |
|:--------|:----------------|:------:|
| `utility_meter/P0_Energie_total/Genelec_appart/01_UM_AMHQ.yaml` | source → `general_electric_appart_energy` | ✅ |
| `utility_meter/P0_Energie_total/Genelec_appart/02_UM_genelec_appart_HPHC_AMHQ.yaml` | source → `general_electric_appart_energy` | ✅ |
| `templates/P0_Energie_total_diag/P0_Genelec_appart/P0_02_ratio_hp_hc.yaml` | source → Nodon | ✅ |
| `templates/P0_Energie_total_diag/P0_Genelec_appart/P0_03_AVG_genelec_appart.yaml` | source → Nodon | ✅ |
| `templates/P0_Energie_total_diag/P0_Linky/P0_MyElectricalData.yaml` | Linky J-1 conservé | ✅ |
| Docs vignettes L2C1, L2C2 | Impact Ecojoko → Nodon vérifié : L2C1 ✅, L2C2 ✅ (zero référence Ecojoko en L2C2 — entités P1 pures) | ✅ |

---

## ✅ L2C2 — ÉNERGIE CLIM / RAD / SOUFFLANT
*Validée le 2026-05-13*

### Chaîne de dépendances

```
MATÉRIEL (NOUS SP via Z2M)
  └─→ sensor.*_power / climate.*   (HA natif)
        └─→ UM: P1_UM_AMHQ.yaml          (6 appareils × 4 cycles AMHQ → *_um)
              └─→ TPL: P1_TOTAL_AMHQ.yaml (conso_clim_rad_total_Q/M)
              └─→ TPL: P1_ui_dashboard.yaml (*_power_status / *_etat)
                    └─→ VIGNETTE L2C2 (button-card 3 colonnes)
                    └─→ PAGE L2C2 (apexcharts + tabbed-card + streamline)
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
| `sensor.clim_salon_quotidien_um` | UM | `P1_clim_chauffage/P1_UM_AMHQ.yaml` |
| `sensor.radiateur_elec_cuisine_quotidien_um` | UM | idem |
| `sensor.clim_bureau_quotidien_um` | UM | idem |
| `sensor.soufflant_sdb_quotidien_um` | UM | idem |
| `sensor.seche_serviette_sdb_quotidien_um` | UM | idem |
| `sensor.clim_chambre_quotidien_um` | UM | idem |
| `sensor.conso_clim_rad_total_quotidien` | TPL | `P1_TOTAL/P1_TOTAL_AMHQ.yaml` |
| `sensor.clim_salon_mensuel_um` | UM | `P1_clim_chauffage/P1_UM_AMHQ.yaml` |
| `sensor.radiateur_elec_cuisine_mensuel_um` | UM | idem |
| `sensor.clim_bureau_mensuel_um` | UM | idem |
| `sensor.soufflant_sdb_mensuel_um` | UM | idem |
| `sensor.seche_serviette_sdb_mensuel_um` | UM | idem |
| `sensor.clim_chambre_mensuel_um` | UM | idem |
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

### Entités consommées par la page

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.temperature_delta_affichage` | TPL | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.dut_clim_salon` | SEN | `P1_DUT/P1_DUT_clim_chauffage.yaml` |
| `sensor.dut_radiateur_cuisine` | SEN | idem |
| `sensor.dut_clim_bureau` | SEN | idem |
| `sensor.dut_sdb_total` | TPL | `P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml` |
| `sensor.dut_clim_chambre` | SEN | `P1_DUT/P1_DUT_clim_chauffage.yaml` |
| `sensor.mode_ete_hiver_etat` | TPL | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.conso_clim_rad_total` (puissance W) | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.th_*_temperature` (×5 pièces) | NAT | SONOFF thermostats |
| `climate.*` (×5) | NAT | SmartIR / Meross |

### Streamline templates (page)

| Template | Usage |
|:---------|:------|
| `conso_temps_reel_clim_rad` | Onglet INSTANTANÉ — apexcharts conso en temps réel |
| `conso_mensuelle_clim` | Onglet MENSUEL — apexcharts conso mensuelle |
| `apex_dut_piece` | Onglet DUT — apexcharts durée utilisation par pièce |
| `clim_voltage_ring-tile` | ring-tile-card tension (V) par appareil |
| `clim_ampere_ring-tile` | ring-tile-card ampérage (A) par appareil |
| `calcule_temp_cible` | Pop-up #tendances — logique calcul T° cible *(corrigé 2026-06-21)* |

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml` | ✅ |
| `templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml` | ✅ |
| `templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml` | ✅ |
| `templates/P1_clim_chauffage/P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml` | ✅ |
| `sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml` | ✅ |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L2C2_05_Energie_Clim/vignette_L2C2_energie_clim_2026-05-13.yaml` | ✅ |
| `Dashboard/L2C2_05_Energie_Clim/page_L2C2_energie_clim_2026-05-13.yaml` | ✅ |
| `Dashboard/L2C2_05_Energie_Clim/page_L2C2_energie_clim_2026-05-22.yaml` | ✅ |
| `Dashboard/L2C2_05_Energie_Clim/page_L2C2_energie_clim_2026-06-18.yaml` | ⚠️ obsolète — `climate.clim_chambre_rm4_mini` |
| `Dashboard/L2C2_05_Energie_Clim/page_L2C2_energie_clim_2026-07-14.yaml` | ✅ `climate.clim_chambre_rm4_mini` (NOUS SP1 conservé) |

---

## ✅ L2C3 — ÉNERGIE ÉCLAIRAGE (LAMPES)
*Validée le 2026-04-29 — Migration TPL kWh complète (_um → _um_kwh_tpl) | Dashboard archivé le 2026-05-13 | 2026-06-14 state_class total_increasing → total (× 116 sensors)*

### Chaîne de dépendances

```
MATÉRIEL (Hue Bridge / Sonoff via Z2M)
  └─→ _energy (firmware direct, kWh cumulatif)
        └─→ UM: P3_UM_AMHQ_1_UNITE.yaml  (19 ampoules × 4 cycles = 76 _um)
              └─→ TPL: P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml  (76 _um_kwh_tpl)
                    └─→ TPL: P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml  (zones → 40 _um_kwh_tpl)
                    └─→ TPL: P3_ENERGIE_TPL/P3_TPL_AMHQ_3_TOTAL.yaml (4 total _kwh_tpl)
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
| `sensor.eclairage_appart_2_quotidien_um_kwh_tpl` | TPL | `P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml` |
| `sensor.eclairage_salon_5_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_cuisine_1_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_bureau_5_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_sdb_2_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_chambre_4_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_total_unit_quotidien_kwh_tpl` | TPL | `P3_ENERGIE_TPL/P3_TPL_AMHQ_3_TOTAL.yaml` |
| `sensor.eclairage_appart_2_mensuel_um_kwh_tpl` | TPL | `P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml` |
| `sensor.eclairage_salon_5_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_cuisine_1_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_bureau_5_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_sdb_2_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_chambre_4_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_total_unit_mensuel_kwh_tpl` | TPL | `P3_ENERGIE_TPL/P3_TPL_AMHQ_3_TOTAL.yaml` |

### TPL ENERGIE — Détail des 3 fichiers P3_ENERGIE_TPL

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
| `templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml` | ✅ |
| `templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml` | ✅ |
| `templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_3_TOTAL.yaml` | ✅ |
| `templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml` | ✅ |
| `templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml` | ✅ |
| `templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml` | ✅ |
| `templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml` | ✅ |
| `templates/P3_eclairage/ui_dashboard/etats_status.yaml` | ✅ |

### Entités supplémentaires (page uniquement)

| Entité | Type | Fichier source | Usage |
|:-------|:----:|:--------------|:------|
| `sensor.eclairage_appart_3_*_um_kwh_tpl` (Q/H/M/A) | TPL | `P3_TPL_AMHQ_2_ZONE.yaml` | Section Entrée-Cuisine-Couloir (3 ampoules) |
| `sensor.eclairage_*_hebdomadaire_um_kwh_tpl` | TPL | `P3_TPL_AMHQ_2_ZONE.yaml` | Badges H (hebdo) par zone |
| `sensor.eclairage_*_annuel_um_kwh_tpl` | TPL | `P3_TPL_AMHQ_2_ZONE.yaml` | Badges A (annuel) par zone |
| `sensor.eclairage_*_avg_watts_mensuel` | TPL | `P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml` | Ligne moyenne 30j (salon/bureau/sdb/chambre/appart_3) |
| `sensor.hue_*_quotidien_um_kwh_tpl` (19 ampoules) | TPL | `P3_TPL_AMHQ_1_UNITE.yaml` | Donuts journaliers par pièce |
| `sensor.hue_*_mensuel_um_kwh_tpl` (19 ampoules) | TPL | `P3_TPL_AMHQ_1_UNITE.yaml` | Donuts mensuels par pièce |
| `light.salon`, `light.table`, `light.entree`, `light.cuisine`, `light.couloir`, `light.bureau`, `light.chambre`, `light.lit` | NAT | Hue Bridge | Badges état ON/OFF heading |
| `light.hue_white_lamp_salle_de_bain` | NAT | Hue Bridge | Badge état SDB |
| `switch.relais_lumiere_sdb_sonoff` | NAT | Z2M Sonoff | Badge état miroir SDB |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L2C3_06_Energie_Eclairage/vignette_L2C3_energie_eclairage_2026-05-13.yaml` | ✅ |
| `Dashboard/L2C3_06_Energie_Eclairage/page_L2C3_energie_eclairage_2026-05-13.yaml` | ✅ |

---

## ✅ L3C1 — COMMANDES ÉCLAIRAGE (LAMPES)
*Validée le 2026-05-04 | Dashboard archivé le 2026-05-13*

### Chaîne de dépendances

```
MATÉRIEL (Hue Bridge / Sonoff)
  └─→ light.* / switch.*  (HA natif — state on/off)
        └─→ TPL: ui_dashboard/etats_status.yaml  (lumiere_*_etat / bureau_etat / chambre_etat)
              └─→ VIGNETTE L3C1 (button-card 3 colonnes : pièce / état / compteur X/N)
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.lumiere_appartement_etat` | TPL | `P3_eclairage/ui_dashboard/etats_status.yaml` |
| `sensor.lumiere_salon_etat` | TPL | idem |
| `sensor.lumiere_cuisine_etat` | TPL | idem |
| `sensor.bureau_etat` | TPL | idem |
| `sensor.lumiere_ecran_etat` | TPL | idem |
| `sensor.lumiere_salle_de_bain_etat` | TPL | idem |
| `sensor.chambre_etat` | TPL | idem |
| `light.entree` | NAT | Hue Bridge |
| `light.couloir` | NAT | Hue Bridge |
| `light.salon` | NAT | Hue Bridge |
| `light.table` | NAT | Hue Bridge |
| `light.cuisine` | NAT | Hue Bridge |
| `light.hue_white_lamp_salle_de_bain` | NAT | Hue Bridge |
| `light.chambre` | NAT | Hue Bridge |
| `light.hue_color_candle_chambre_gege` | NAT | Hue Bridge |
| `light.hue_color_candle_chambre_eric` | NAT | Hue Bridge |
| `light.lit` | NAT | Hue Bridge | Groupe tête de lit — cible du tap_action toggle (fix B4) |
| `switch.prise_tete_de_lit_chambre` | NAT | Intégration native |

### Entités disponibles (etats_status) non encore intégrées

| Entité | Note |
|:-------|:-----|
| `sensor.lumiere_bureau_etat` | Nouveau slug unifié — remplacera `bureau_etat` à terme |
| `sensor.lumiere_chambre_etat` | Idem — remplacera `chambre_etat` à terme |
| `sensor.lumiere_tete_de_lit_etat` | Nouvel état dédié tête de lit |

### Entités page (toggle + badges + pop-ups)

| Entité | Type | Fichier source | Usage |
|:-------|:----:|:--------------|:------|
| `sensor.th_salon_temperature` | NAT | SONOFF via Z2M | Badge T° heading Salon |
| `sensor.th_cuisine_temperature` | NAT | SONOFF via Z2M | Badge T° heading Cuisine |
| `sensor.th_bureau_temperature` | NAT | SONOFF via Z2M | Badge T° heading Bureau |
| `sensor.th_salle_de_bain_temperature` | NAT | SONOFF via Z2M | Badge T° heading SdB |
| `sensor.th_chambre_temperature` | NAT | SONOFF via Z2M | Badge T° heading Chambre |
| `cover.store_salon` | NAT | MQTT/Z2M | Badge volet heading Salon |
| `cover.store_bureau` | NAT | MQTT/Z2M | Badge volet heading Bureau |
| `light.entree` | NAT | Hue Bridge | Mushroom toggle + heading badge |
| `light.salon` | NAT | Hue Bridge | Mushroom toggle + heading badge |
| `light.table` | NAT | Hue Bridge | Mushroom toggle + heading badge |
| `light.cuisine` | NAT | Hue Bridge | Mushroom toggle + heading badge |
| `light.couloir` | NAT | Hue Bridge | Mushroom toggle + heading badge |
| `light.bureau` | NAT | Hue Bridge | Mushroom toggle (Hue White bureau_1+2) + pop-up |
| `light.hue_white_lamp_salle_de_bain` | NAT | Hue Bridge | Mushroom toggle SdB + heading badge |
| `light.chambre` | NAT | Hue Bridge | Mushroom toggle Chambre + heading badge |
| `switch.relais_lumiere_sdb_sonoff` | NAT | Z2M Sonoff | Mushroom toggle SdB (miroir) + heading badge |
| `switch.ecran_p_c_3_play_hue` | NAT | Hue Bridge | Condition affichage section Écran PC |
| `light.moniteur_pc` | NAT | Hue Bridge | Pop-up #ecranpc (groupe Play 1/2/3) |
| `light.zone_gege` | NAT | Hue Bridge | Pop-up #tete_de_lit |
| `light.zone_eric` | NAT | Hue Bridge | Pop-up #tete_de_lit |
| `switch.prise_tete_de_lit_chambre` | NAT | Intégration native | Condition visibilité section Têtes de Lit |

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `templates/P3_eclairage/ui_dashboard/etats_status.yaml` | ✅ |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L3C1_07_Commandes_Eclairage/vignette_L3C1_eclairage_2026-05-13.yaml` | ✅ |
| `Dashboard/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_gauche_2026-05-13.yaml` | ✅ |
| `Dashboard/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_droite_2026-05-13.yaml` | ✅ |

---

## ✅ L3C2 — COMMANDES ÉCO/PRISES
*Archivée le 2026-05-14*

### Vignette — Chaîne de dépendances

```
MATÉRIEL / INTÉGRATION
  ├─→ Zigbee2MQTT (Z2M) → MQTT → HA
  │     ├─→ switch.prise_horloge_ikea          (natif Z2M — IKEA TRADFRI)
  │     ├─→ switch.prise_tv_salon_ikea          (natif Z2M — IKEA TRADFRI)
  │     ├─→ switch.prise_tete_de_lit_chambre    (natif Z2M — IKEA TRADFRI)
  │     ├─→ light.hue_smart_eco_salon           (natif Z2M — Hue Smart Plug)
  │     ├─→ light.hue_smart_eco_pc_bureau       (natif Z2M — Hue Smart Plug)
  │     └─→ light.hue_smart_eco_tv_chambre      (natif Z2M — Hue Smart Plug)
  │           └─→ VIGNETTE L3C2 (button-card 2 colonnes : piece / etat)
  │                 tap_action → /dashboard-tablette/prises
```

### Entités utilisées — Vignette

| Entité | Type | Source | Rôle |
|:-------|:-----|:-------|:-----|
| `switch.prise_horloge_ikea` | switch | Z2M natif | État Horloge Entrée |
| `light.hue_smart_eco_salon` | light | Z2M natif | État Eco Salon (chargeur) |
| `switch.prise_tv_salon_ikea` | switch | Z2M natif | État TV Salon |
| `light.hue_smart_eco_pc_bureau` | light | Z2M natif | État PC Bureau |
| `switch.prise_tete_de_lit_chambre` | switch | Z2M natif | État Têtes de Lit |
| `light.hue_smart_eco_tv_chambre` | light | Z2M natif | État TV Chambre |

### Entités utilisées — Page

| Entité contrôlée | Sensor puissance | Sensor tension | Sensor courant | MAX |
|:-----------------|:-----------------|:---------------|:---------------|:----|
| `switch.prise_horloge_ikea` | `sensor.prise_horloge_ikea_power` | `sensor.prise_horloge_ikea_voltage` | `sensor.prise_horloge_ikea_current` | 2500W |
| `light.hue_smart_eco_salon` | `sensor.prise_salon_chargeur_nous_power` | `sensor.prise_salon_chargeur_nous_voltage` | `sensor.prise_salon_chargeur_nous_current` | 2500W |
| `switch.prise_tv_salon_ikea` | `sensor.prise_tv_salon_ikea_power` | `sensor.prise_tv_salon_ikea_voltage` | `sensor.prise_tv_salon_ikea_current` | 250W (mA) |
| `light.hue_smart_eco_pc_bureau` | `sensor.prise_bureau_pc_ikea_power` | `sensor.prise_bureau_pc_ikea_voltage` | `sensor.prise_bureau_pc_ikea_current` | 500W (couleur gris si OFF) |
| `light.hue_smart_eco_tv_chambre` | `sensor.prise_tv_chambre_nous_power` | `sensor.prise_tv_chambre_nous_voltage` | `sensor.prise_tv_chambre_nous_current` | 500W |
| `switch.prise_tete_de_lit_chambre` | `sensor.prise_tete_de_lit_chambre_power` | `sensor.prise_tete_de_lit_chambre_voltage` | `sensor.prise_tete_de_lit_chambre_current` | 50W |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L3C2_08_Commandes_Prises/vignette_L3C2_prises_2026-05-14.yaml` | ✅ |
| `Dashboard/L3C2_08_Commandes_Prises/page_L3C2_prises_2026-05-14.yaml` | ✅ |

---

## ✅ L3C3 — STORES / FENÊTRES (VIGNETTE + PAGE)
*Validée le 2026-05-14*

### Vignette — Chaîne de dépendances

```
MATÉRIEL / INTÉGRATION
  ├─→ Zigbee2MQTT — SONOFF SNZB-04 (4 contacts de fenêtre)
  │     ├─→ binary_sensor.contact_fenetre_salon_sonoff_contact   (NAT/Z2M)
  │     ├─→ binary_sensor.contact_fenetre_cuisine_sonoff_contact (NAT/Z2M)
  │     ├─→ binary_sensor.contact_fenetre_bureau_sonoff_contact  (NAT/Z2M)
  │     └─→ binary_sensor.contact_fenetre_chambre_sonoff_contact (NAT/Z2M)
  │           └─→ VIGNETTE L3C3 — colonne "Fenêtres" (on=rouge Ouvert, off=vert Fermé)
  ├─→ TPL: templates/Stores/S_01_STORES.yaml
  │     ├─→ sensor.store_salon_status   (TPL — texte état store salon)
  │     └─→ sensor.store_bureau_status  (TPL — texte état store bureau)
  │           └─→ VIGNETTE L3C3 — colonne "Stores" (texte brut)
  └─→ sensor.store_cuisine_status / sensor.store_chambre_status
        └─→ VIGNETTE L3C3 — colonne "Stores" (placeholders N/A — stores non motorisés)
```

### Entités consommées par la vignette

| Entité | Type | Fichier source | Rôle |
|:-------|:----:|:--------------|:-----|
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | NAT | Z2M (SONOFF SNZB-04) | Fenêtre Salon — Ouvert/Fermé |
| `binary_sensor.contact_fenetre_cuisine_sonoff_contact` | NAT | Z2M (SONOFF SNZB-04) | Fenêtre Cuisine — Ouvert/Fermé |
| `binary_sensor.contact_fenetre_bureau_sonoff_contact` | NAT | Z2M (SONOFF SNZB-04) | Fenêtre Bureau — Ouvert/Fermé |
| `binary_sensor.contact_fenetre_chambre_sonoff_contact` | NAT | Z2M (SONOFF SNZB-04) | Fenêtre Chambre — Ouvert/Fermé |
| `sensor.store_salon_status` | TPL | `templates/Stores/S_01_STORES.yaml` | Store Salon — texte état |
| `sensor.store_bureau_status` | TPL | `templates/Stores/S_01_STORES.yaml` | Store Bureau — texte état |

### Page — Chaîne de dépendances

```
MATÉRIEL / INTÉGRATION
  ├─→ SONOFF (Z2M — balcon nord)
  │     └─→ sensor.th_balcon_nord_temperature  (NAT)  ← badge condition seuil (+34° salon / +18°–+25° bureau)
  ├─→ Zigbee2MQTT — SONOFF SNZB-04
  │     ├─→ binary_sensor.contact_fenetre_salon_sonoff_contact   (NAT)  ← badge état fenêtre salon
  │     ├─→ sensor.contact_fenetre_salon_sonoff_battery           (NAT)  ← badge batterie fenêtre salon
  │     ├─→ binary_sensor.contact_fenetre_bureau_sonoff_contact  (NAT)  ← badge état fenêtre bureau
  │     └─→ sensor.contact_fenetre_bureau_sonoff_battery          (NAT)  ← badge batterie fenêtre bureau
  ├─→ Zigbee2MQTT — covers (stores motorisés)
  │     ├─→ cover.store_salon   (NAT/Z2M)  ← enhanced-shutter-card + boutons positions (100/85/70/49/20)
  │     └─→ cover.store_bureau  (NAT/Z2M)  ← enhanced-shutter-card + boutons positions (100/90/65/50/30)
  ├─→ sensor.store_salon_signal_strength   (NAT/Z2M)  ← signal_entity enhanced-shutter-card salon
  ├─→ sensor.store_bureau_signal_strength  (NAT/Z2M)  ← signal_entity enhanced-shutter-card bureau
  └─→ Hue Bridge
        ├─→ light.store_salon_dnd   (NAT)  ← voyant DnD mushroom-light-card salon
        └─→ light.store_bureau_dnd  (NAT)  ← voyant DnD mushroom-light-card bureau
```

### Entités consommées par la page

| Entité | Type | Fichier source | Rôle |
|:-------|:----:|:--------------|:-----|
| `sensor.th_balcon_nord_temperature` | NAT | Z2M (SONOFF balcon nord) | Badge condition seuil fermeture auto |
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | NAT | Z2M (SONOFF SNZB-04) | Badge état fenêtre Salon |
| `sensor.contact_fenetre_salon_sonoff_battery` | NAT | Z2M (SONOFF SNZB-04) | Badge batterie fenêtre Salon |
| `binary_sensor.contact_fenetre_bureau_sonoff_contact` | NAT | Z2M (SONOFF SNZB-04) | Badge état fenêtre Bureau |
| `sensor.contact_fenetre_bureau_sonoff_battery` | NAT | Z2M (SONOFF SNZB-04) | Badge batterie fenêtre Bureau |
| `cover.store_salon` | NAT | Z2M (store motorisé) | enhanced-shutter-card — commande store Salon |
| `cover.store_bureau` | NAT | Z2M (store motorisé) | enhanced-shutter-card — commande store Bureau |
| `sensor.store_salon_signal_strength` | NAT | Z2M | signal_entity — force signal store Salon |
| `sensor.store_bureau_signal_strength` | NAT | Z2M | signal_entity — force signal store Bureau |
| `light.store_salon_dnd` | NAT | Hue Bridge | Voyant DnD mushroom-light-card — Salon |
| `light.store_bureau_dnd` | NAT | Hue Bridge | Voyant DnD mushroom-light-card — Bureau |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L3C3_09_Stores_Fenetres/vignette_L3C3_stores_2026-05-14.yaml` | ✅ |
| `Dashboard/L3C3_09_Stores_Fenetres/page_L3C3_stores_2026-05-14.yaml` | ✅ |

---

## ✅ L4C1 — PROXMOX PVE (VIGNETTE + PAGE)
*Validée le 2026-06-13 (docs entièrement réécrites — +5e section MyElectricalData)*

> Page complète supervision infrastructure Proxmox VE.
> Vignette : température CPU, CPU %, RAM %, Storage %, PVE Status.
> Page : **5 sections** (PVE, HA, Z2M, MariaDB, MyElectricalData) × métriques détaillées + apexcharts CPU 1h.
> Path → `/dashboard-tablette/systeme-proxmox`.

### Vignette — Entités consommées

| Entité | Type | Source |
|:-------|:----:|:-------|
| `sensor.proxmox_cpu_package` | NAT | Proxmox VE (MQTT Discovery) |
| `sensor.pve_utilisation_du_processeur` | NAT | Proxmox VE |
| `sensor.pve_memory_usage_percentage` | NAT | Proxmox VE |
| `sensor.storage_local_storage_usage_percentage` | NAT | Proxmox VE |
| `binary_sensor.pve_status` | NAT | Proxmox VE |

### Page — Entités consommées (complet)

**PROXMOX VE**
| Entité | Métrique |
|:-------|:---------|
| `sensor.pve_statut` | Status |
| `sensor.pve_utilisation_du_processeur` | CPU % |
| `sensor.pve_memory_usage_percentage` | RAM % |
| `sensor.pve_utilisation_du_disque` | Disk GiB |
| `sensor.pve_uptime` | Uptime |
| `binary_sensor.pve_backup_status` | Backup |
| `sensor.pve_max_cpu` | vCPU |
| `button.pve_tout_demarrer` | Start All |
| `button.pve_tout_stopper` | Stop All |
| `button.pve_redemarrer` | Reboot |
| `button.pve_shut_down` | Shutdown |

**HOME ASSISTANT**
| Entité | Métrique |
|:-------|:---------|
| `sensor.homeassistant_statut` | Status |
| `sensor.homeassistant_utilisation_du_processeur` | CPU % |
| `sensor.homeassistant_memory_usage_percentage` | RAM % |
| `sensor.homeassistant_utilisation_du_disque` | Disk GiB |
| `sensor.homeassistant_uptime` | Uptime |
| `sensor.homeassistant_max_cpu` | vCPU |
| `button.homeassistant_demarrer` | Start |
| `button.homeassistant_stopper` | Stop |
| `button.homeassistant_redemarrer` | Restart LXC |
| `button.homeassistant_restart` | Restart HA |
| `button.homeassistant_reload` | Reload |

**ZIGBEE2MQTT**
| Entité | Métrique |
|:-------|:---------|
| `sensor.z2m_statut` | Status |
| `sensor.z2m_utilisation_du_processeur` | CPU % |
| `sensor.z2m_memory_usage_percentage` | RAM % |
| `sensor.z2m_utilisation_du_disque` | Disk GiB |
| `sensor.z2m_uptime` | Uptime |
| `sensor.z2m_max_cpu` | vCPU |
| `button.z2m_demarrer` | Start |
| `button.z2m_stopper` | Stop |
| `button.z2m_redemarrer` | Restart |

**MARIADB**
| Entité | Métrique |
|:-------|:---------|
| `sensor.mariadb_statut` | Status |
| `sensor.mariadb_utilisation_du_processeur` | CPU % |
| `sensor.mariadb_memory_usage_percentage` | RAM % |
| `sensor.mariadb_utilisation_du_disque` | Disk GiB |
| `sensor.mariadb_uptime` | Uptime |
| `sensor.mariadb_max_cpu` | vCPU |
| `button.mariadb_demarrer` | Start |
| `button.mariadb_stopper` | Stop |
| `button.mariadb_redemarrer` | Restart |

**MYELECTRICALDATA (LXC 202)** ← *ajouté 2026-06-13*
| Entité | Métrique | Note |
|:-------|:---------|:-----|
| `sensor.myelectricaldata_statut` | Status (enum) | running/stopped/suspended |
| `binary_sensor.myelectricaldata_status` | Running (bool) | device_class: running |
| `sensor.myelectricaldata_utilisation_du_processeur` | CPU % | |
| `sensor.myelectricaldata_memory_usage_percentage` | RAM % | |
| `sensor.myelectricaldata_utilisation_de_la_memoire` | RAM GiB | |
| `sensor.myelectricaldata_utilisation_maximale_de_la_memoire` | RAM Max GiB | max allouée = 1.0 GiB |
| `sensor.myelectricaldata_utilisation_du_disque` | Disk GiB | ⚠️ PAS de % — GiB uniquement |
| `sensor.myelectricaldata_utilisation_maximale_du_disque` | Disk Max GiB | max = 3.86 GiB |
| `sensor.myelectricaldata_uptime` | Uptime (h float) | même format que pve_uptime |
| `sensor.myelectricaldata_max_cpu` | vCPU | = 1 |
| `sensor.myelectricaldata_network_input` | Réseau In GiB | total_increasing |
| `sensor.myelectricaldata_network_output` | Réseau Out GiB | total_increasing |
| `button.myelectricaldata_demarrer` | Start | |
| `button.myelectricaldata_stopper` | Stop | |
| `button.myelectricaldata_redemarrer` | Restart | |
| `button.myelectricaldata_create_snapshot` | Snapshot | |

> ⚠️ Pas de `binary_sensor.myelectricaldata_backup_status` (contrairement à PVE).
> Pas de `sensor.myelectricaldata_utilisation_du_disque` en % — seuils page à exprimer en GiB absolu.
> Badge : vert `rgb(15,157,88)` — couleur section : `#00bcd4`.

### Seuils de couleur

| Section | Métrique | Vert | Orange | Rouge |
|:--------|:---------|:-----|:--------|:------|
| **PVE** | CPU % | ≤75% | 75–90% | >90% |
| **PVE** | RAM % | ≤75% | 75–90% | >90% |
| **PVE** | Storage % | ≤60% | 60–80% | >80% |
| **HA** | CPU % | ≤75% | 75–90% | >90% |
| **HA** | RAM % | ≤75% | 75–90% | >90% |
| **HA** | Disk GiB | ≤20 | 20–28 | >28 |
| **Z2M** | CPU % | ≤40% | 40–60% | >60% |
| **Z2M** | RAM % | ≤50% | 50–70% | >70% |
| **Z2M** | Disk GiB | ≤2.5 | 2.5–3.4 | >3.4 |
| **MDB** | CPU % | ≤50% | 50–75% | >75% |
| **MDB** | RAM % | ≤60% | 60–80% | >80% |
| **MDB** | Disk GiB | ≤5 | 5–7 | >7 |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs_dashboard/docs/L4C1_PROXMOX/L4C1_VIGNETTE_PROXMOX.md` | ✅ |
| `Dashboard/L4C1_10_Proxmox/vignette_L4C1_proxmox_2026-06-18.yaml` | ✅ |
| `docs_dashboard/docs/L4C1_PROXMOX/PAGE_PROXMOX.md` | ✅ |
| `Dashboard/L4C1_10_Proxmox/page_L4C1_proxmox_2026-06-18.yaml` | ✅ |

---

## ✅ L4C2 — MINI PC (VIGNETTE + PAGE)
*Validée le 2026-06-18 — vignette refactorisée : proxmox_cpu_package direct (sans template) | ⚠️ uptime bug non encore corrigé en page*

> ⚠️ **BUG UPTIME CONNU** (non corrigé) : Jinja2 dans la page utilise `| int(0)` + `/ 86400` alors que `sensor.pve_uptime` retourne des **heures** (float), pas des secondes. Résultat : affiche ~0j 0h. Fix à appliquer :
> ```yaml
> {% set uptime = states('sensor.pve_uptime') | float(0) %}
> {% set jours = (uptime / 24) | int(0) %}
> {% set heures = (uptime % 24) | int(0) %}
> {% set minutes = ((uptime % 1) * 60) | int(0) %}
> ```

### Vignette — Chaîne de dépendances

```
MATÉRIEL / INTÉGRATION
  ├─→ Proxmox VE (intégration officielle HA)
  │     ├─→ sensor.proxmox_cpu_package                    (NAT)  ← entité principale (icône + champ temp)
  │     ├─→ sensor.pve_utilisation_du_processeur          (NAT)  ← CPU %
  │     ├─→ sensor.pve_memory_usage_percentage            (NAT)  ← RAM %
  │     └─→ sensor.storage_local_storage_usage_percentage (NAT)  ← Disk %
  └─→ Zigbee2MQTT (prise IKEA Inspelning)
        └─→ sensor.prise_mini_pc_ikea_power  (NAT)   ← Watts instantanés
              └─→ VIGNETTE L4C2 (button-card 6 zones CSS — icône phu:intel-nuc)
```

### Entités consommées par la vignette

| Entité | Type | Fichier source | Rôle |
|:-------|:----:|:--------------|:-----|
| `sensor.proxmox_cpu_package` | NAT | Proxmox VE (MQTT Discovery) | Entité principale — icône + champ `temp` |
| `sensor.pve_utilisation_du_processeur` | NAT | Proxmox VE | Champ `cpu` — CPU % |
| `sensor.pve_memory_usage_percentage` | NAT | Proxmox VE | Champ `ram` — RAM % |
| `sensor.storage_local_storage_usage_percentage` | NAT | Proxmox VE | Champ `sd` — Disk % |
| `sensor.prise_mini_pc_ikea_power` | NAT | Z2M (IKEA Inspelning) | Champ `conso` — Watts |

### Page — Chaîne de dépendances

```
MATÉRIEL / INTÉGRATION
  ├─→ local_ip + myip/ipify (intégrations)
  │     └─→ sensor.local_ip / sensor.ip_externe  (NAT)  ← Bloc 1
  ├─→ system_monitor (intégration HA)
  │     ├─→ sensor.system_monitor_dernier_demarrage      ← Bloc 1 (Uptime Jinja2)
  │     ├─→ sensor.system_monitor_utilisation_du_processeur  ← Blocs 2, 6, 8
  │     ├─→ sensor.system_monitor_utilisation_de_la_memoire  ← Bloc 3
  │     ├─→ sensor.system_monitor_memoire_utilisee            ← Blocs 3, 15, 16, #memory
  │     ├─→ sensor.system_monitor_memoire_libre               ← Bloc 3
  │     ├─→ sensor.system_monitor_utilisation_du_disque       ← Bloc 4
  │     ├─→ sensor.system_monitor_espace_utilise              ← Pop-up #disk
  │     ├─→ sensor.system_monitor_debit_du_reseau_entrant_via_enp6s18  ← Bloc 5
  │     ├─→ sensor.system_monitor_debit_du_reseau_sortant_via_enp6s18  ← Bloc 5
  │     ├─→ sensor.system_monitor_charge_1m / 5m / 15m        ← Bloc 8
  │     └─→ sensor.cpu_speed  (NAT)                           ← Bloc 7
  ├─→ Proxmox VE (intégration officielle HA — MQTT Discovery)
  │     └─→ sensor.proxmox_cpu_package / sensor.proxmox_carte_mere / core_0/1/2/3  (NAT)
  │           ├─→ sensor.proxmox_cpu_package   ← Blocs 2, 9, 11
  │           ├─→ sensor.proxmox_core_0 / core_1 / core_2 / core_3  ← Bloc 10
  │           └─→ sensor.proxmox_carte_mere    ← Bloc 12
  └─→ Zigbee2MQTT (prise IKEA Inspelning)
        ├─→ sensor.prise_mini_pc_ikea_power   ← Blocs 13, 14, Pop-up #conso
        ├─→ sensor.prise_mini_pc_ikea_current ← Pop-up #conso
        ├─→ sensor.prise_mini_pc_ikea_energy  ← Pop-up #conso
        ├─→ sensor.mini_pc_avg_watts_quotidien  (TPL)  ← Pop-up #conso
        ├─→ sensor.mini_pc_avg_watts_mensuel    (TPL)  ← Pop-up #conso
        ├─→ sensor.prise_mini_pc_ikea_quotidien_um  (UM)  ← Pop-up #conso
        └─→ sensor.prise_mini_pc_ikea_mensuel_um    (UM)  ← Pop-up #conso
```

> ⚠️ Interface réseau : **`enp6s18`** (VirtIO KVM sous Proxmox) — PAS `enp1s0`.

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L4C2_11_Mini_PC/vignette_L4C2_mini_pc_2026-06-04.yaml` | ✅ |
| `Dashboard/L4C2_11_Mini_PC/vignette_L4C2_mini_pc_2026-06-09.yaml` | ✅ |
| `Dashboard/L4C2_11_Mini_PC/vignette_L4C2_mini_pc_2026-06-18.yaml` | ✅ refonte — proxmox_cpu_package direct (sans template) |
| `Dashboard/L4C2_11_Mini_PC/page_L4C2_mini_pc_2026-06-09.yaml` | ✅ |
| `Dashboard/L4C2_11_Mini_PC/page_L4C2_mini_pc_2026-06-10.yaml` | ✅ icônes `mdi:cpu-64-bit` + `mdi:harddisk` ajoutées aux mini-graph-cards |
| `Dashboard/L4C2_11_Mini_PC/page_L4C2_mini_pc_2026-06-18.yaml` | ✅ versioning 2026-06-18 |
| `Dashboard/L4C2_11_Mini_PC/card_popup_memory_2026-06-09.yaml` | ✅ |
| `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml` | ✅ |
| `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml` | ✅ |

---

## ✅ L4C3 — MISES À JOUR HA (VIGNETTE + 2 PAGES)
*Validée le 2026-05-14*

### Vignette — Chaîne de dépendances

```
HA (intégration native)
  └─→ sensor.available_updates  (NAT — compteur global MàJ disponibles)
        └─→ VIGNETTE L4C3 (button-card — couleur orange si > 0, texte MàJ)
              └─→ tap_action: navigate → /dashboard-tablette/maj
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.available_updates` | NAT | HA Core (compteur updates natif) |

### Page gauche (H.A. SERVER) — Chaîne de dépendances

```
HA Core (intégration hassio)
  ├─→ update.home_assistant_core_update          (NAT) → mushroom-update-card + version info
  ├─→ update.home_assistant_operating_system_update (NAT) → mushroom-update-card
  ├─→ update.home_assistant_supervisor_update    (NAT) → mushroom-update-card
  ├─→ sensor.available_updates                   (NAT) → markdown ha-alert (compteur)
  └─→ HACS (intégration)
        ├─→ auto-entities domain:update → mushroom-chips-card (liste HACS updates)
        └─→ update.install (action) → bouton install
```

### Page droite (H.A. UPDATE + ADD-ON) — Chaîne de dépendances

```
HA Core
  ├─→ auto-entities domain:update state:on (excl. Home*, hacs, mqtt)
  │     └─→ button-card cardupload (MàJ HA hors HACS)
  ├─→ HACS (intégration)
  │     └─→ auto-entities integration:hacs
  │           ├─→ button-card cardurl (lien release)
  │           └─→ button-card cardupload (install update)
  ├─→ markdown (ha-alert error) → intégrations nécessitant redémarrage
  ├─→ Z2M (intégration mqtt)
  │     └─→ auto-entities integration:mqtt → entity-row Z2M
  └─→ HA Add-ons (hassio)
        ├─→ update.mosquitto_broker_update    (NAT) → mushroom-update-card
        └─→ update.studio_code_server_update  (NAT) → mushroom-update-card
              + chips cpu/memory (system_monitor)
```

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L4C3_12_MAJ_HA/vignette_L4C3_maj_ha_2026-05-14.yaml` | ✅ |
| `Dashboard/L4C3_12_MAJ_HA/page_L4C3_maj_ha_gauche_2026-05-14.yaml` | ✅ |
| `Dashboard/L4C3_12_MAJ_HA/page_L4C3_maj_ha_droite_2026-05-14.yaml` | ✅ |

---

## ✅ L5C1 — BATTERIES / PILES (VIGNETTE + PAGE)
*Validée le 2026-05-14 — ⚠️ page partiellement tronquée (3 sections HUE/IKEA/SONOFF à compléter)*

### Vignette — Chaîne de dépendances

```
groups/ (GRP_01/02/03)
  ├─→ group.hue_devices   → 11 sensors sensor.hue_smart_button_*_batterie
  ├─→ group.ikea_devices  → 8 sensors IKEA (contacts, remotes, détecteurs)
  └─→ group.sonoff_devices → 7 sensors sensor.th_*_battery
        └─→ VIGNETTE L5C1 (button-card)
              ├─→ grid 6 colonnes : count | marque | 100-75 | 75-50 | 50-25 | 25-0
              ├─→ Alerte rouge ≤10% : icône ⚠️ + nom marque rouge
              └─→ tap_action: navigate → /dashboard-tablette/battery-bp
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `group.hue_devices` | GRP | `groups/GRP_01_batteries_hue.yaml` |
| `group.ikea_devices` | GRP | `groups/GRP_02_batteries_ikea.yaml` |
| `group.sonoff_devices` | GRP | `groups/GRP_03_batteries_sonoff.yaml` |

### Page — Chaîne de dépendances

```
Philips Hue Bridge / Z2M / SONOFF (ZHA/Z2M)
  ├─→ [HUE] 11× sensor.hue_smart_button_*_batterie
  │     └─→ battery-state-card collapse "Boutons HUE"
  ├─→ [IKEA] 8× sensor.*_ikea_battery (remotes, détecteurs fuite, Vallhorn, poussoir)
  │     └─→ battery-state-card collapse "Capteurs IKEA"
  ├─→ [IKEA] 4× sensor.contact_fenetre_*_ikea_battery
  │     └─→ battery-state-card collapse "Contacts IKEA"
  ├─→ [SONOFF] 4× sensor.contact_fenetre_*_sonoff_battery
  │     └─→ battery-state-card collapse "Contacts SONOFF"
  └─→ [SONOFF] 7× sensor.th_*_battery
        └─→ battery-state-card collapse "Thermostats SONOFF"
```

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L5C1_13_Batteries_Piles/vignette_L5C1_batteries_piles_2026-05-14.yaml` | ✅ |
| `Dashboard/L5C1_13_Batteries_Piles/page_L5C1_batteries_piles_2026-05-14.yaml` | ⚠️ tronqué |

---

## ✅ L5C2 — BATTERIES PORTABLES (VIGNETTE + 2 PAGES)
*Validée le 2026-05-12 — ⚠️ todo: vérifier sensor.ne2213_mamour_battery_health + temperature*

### Vignette — Chaîne de dépendances

```
HA Companion App (iOS/Android)
  ├─→ sensor.eric_battery_level / sensor.eric_battery_state
  ├─→ sensor.mamour_battery_level / sensor.mamour_battery_state
  ├─→ sensor.ne2213_eric_battery_level / sensor.ne2213_eric_battery_state
  ├─→ sensor.ne2213_mamour_battery_level / sensor.ne2213_mamour_battery_state
  ├─→ sensor.gm1901_battery_level / sensor.gm1901_battery_state
  ├─→ sensor.sm_a530f_battery_level / sensor.sm_a530f_battery_state
  └─→ sensor.tablette_battery_level / sensor.tablette_battery_state
        └─→ VIGNETTE L5C2 (button-card)
              ├─→ grid 3 colonnes : nom | batterie (couleur) | réserve (icône charge)
              └─→ tap_action: navigate → /dashboard-tablette/phone
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.eric_battery_level` | NAT | HA Companion (Poco X7 Pro Eric) |
| `sensor.mamour_battery_level` | NAT | HA Companion (Poco X7 Pro Mamour) |
| `sensor.ne2213_eric_battery_level` | NAT | HA Companion (OnePlus NE2213 Eric) |
| `sensor.ne2213_mamour_battery_level` | NAT | HA Companion (OnePlus NE2213 Mamour) |
| `sensor.gm1901_battery_level` | NAT | HA Companion (OnePlus GM1901) |
| `sensor.sm_a530f_battery_level` | NAT | HA Companion (Samsung SM-A530F) |
| `sensor.tablette_battery_level` | NAT | HA Companion (Tablette) |
| `sensor.*_battery_state` | NAT | HA Companion (état charge : charging/discharging/full) |

### Page gauche (Eric + SM-A530F + Tablette) — Chaîne de dépendances

```
HA Companion App
  ├─→ Poco X7 Pro Eric : conditional (state_not unavailable/unknown)
  │     ├─→ custom:streamline-card template:portable
  │     └─→ entities: level, state, charger_type, health, temperature, network, wifi
  ├─→ OnePlus NE2213 Eric : conditional (state_not unavailable/unknown)
  │     ├─→ custom:streamline-card template:portable
  │     └─→ entities: level, state, charger_type, health, temperature, network, wifi
  ├─→ Samsung SM-A530F : conditional (state_not unavailable/unknown)
  │     ├─→ custom:streamline-card template:portable
  │     └─→ entities: level, state, charger_type, health, temperature, network, wifi
  └─→ Tablette : conditional (state_not unavailable/unknown)
        ├─→ custom:streamline-card template:portable
        └─→ entities: level, state, charger_type, health, temperature, network, wifi
```

### Page droite (Mamour + GM1901) — Chaîne de dépendances

```
HA Companion App
  ├─→ Poco X7 Pro Mamour : vertical-stack (sans conditional)
  │     ├─→ custom:streamline-card template:portable
  │     └─→ entities: level, state, charger_type, health, temperature, network, wifi
  ├─→ OnePlus NE2213 Mamour : vertical-stack (sans conditional)
  │     ├─→ custom:streamline-card template:portable
  │     └─→ entities: level, state, charger_type, health, temperature, network, wifi  ⚠️ TODO
  └─→ OnePlus GM1901 : vertical-stack (sans conditional)
        ├─→ custom:streamline-card template:portable
        └─→ entities: level, state, charger_type, health, temperature, network, wifi
```

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L5C2_14_Batteries_Portables/vignette_L5C2_batteries_portables_2026-05-12.yaml` | ✅ |
| `Dashboard/L5C2_14_Batteries_Portables/page_L5C2_batteries_portables_gauche_2026-05-12.yaml` | ✅ |
| `Dashboard/L5C2_14_Batteries_Portables/page_L5C2_batteries_portables_droite_2026-05-12.yaml` | ✅ |

---

## ✅ L5C3 — MARIADB / SYSTÈME (VIGNETTE + PAGE)
*Validée le 2026-05-10*

### Vignette — Chaîne de dépendances

```
MariaDB (intégration sql.yaml)
  └─→ sensor.taille_db_home_assistant  (SQL — taille en MiB)
        └─→ VIGNETTE L5C3 (custom:flex-horseshoe-card dans button-card)
              ├─→ horseshoe colorstop : 0→vert, 1800→gold, 3500→orange, 4000→red
              └─→ tap_action: navigate → /dashboard-tablette/reserve
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.taille_db_home_assistant` | NAT | `sql.yaml` (requête MariaDB) |

### Page — Chaîne de dépendances

```
Audit MD5 (script + template/command_line)
  ├─→ script.audit_md5                  (scripts.yaml) → button-card déclencheur
  └─→ sensor.audit_md5_journal          (attr: text) → markdown résultat + chemin log
GitHub (shell_command + command_line)
  ├─→ sensor.backup_github_status       (NAT) → chip OK/KO + apexcharts 7j
  ├─→ sensor.backup_github_journal      (NAT) → markdown journal 10 derniers
  ├─→ sensor.git_last_weekly_tag        (NAT) → chip tag hebdo (vert si semaine courante)
  ├─→ sensor.github_default_branch      (NAT) → chip branche (vert si main)
  ├─→ shell_command.git_backup_push_weekly   → hold_action chip tag
  └─→ shell_command.git_backup_push_manual  → tap_action chip Push
MariaDB
  ├─→ sensor.taille_db_home_assistant   (NAT) → apexcharts 7j évolution
  └─→ automation.db_purge_mariadb_repack     → button-card déclencheur manuel
```

### Entités consommées par la page

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `script.audit_md5` | NAT | `scripts.yaml` |
| `sensor.audit_md5_journal` | NAT | `command_line/audit/audit_logs.yaml` |
| `sensor.backup_github_status` | NAT | `command_line/github_maintenance/github_maintenance.yaml` |
| `sensor.backup_github_journal` | NAT | `command_line/github_maintenance/github_maintenance.yaml` |
| `sensor.git_last_weekly_tag` | NAT | `command_line/github_maintenance/github_maintenance.yaml` |
| `sensor.github_default_branch` | NAT | `command_line/github_maintenance/github_maintenance.yaml` |
| `sensor.taille_db_home_assistant` | NAT | `sql.yaml` |
| `automation.db_purge_mariadb_repack` | NAT | `automations/systeme/` |
| `shell_command.git_backup_push_weekly` | NAT | `shell_command/Ghithub/backup_github.yaml` |
| `shell_command.git_backup_push_manual` | NAT | `shell_command/Ghithub/backup_github.yaml` |

### Page — Chaîne de dépendances (NOUVEAU 2026-05-18)

```
Proxmox VE (intégration superviseur)
  ├─→ Home Assistant Container (Proxmox)
  │     ├─→ sensor.homeassistant_utilisation_du_processeur  (NAT)
  │     ├─→ sensor.homeassistant_uptime  (NAT)
  │     ├─→ sensor.homeassistant_memory_usage_percentage  (NAT)
  │     └─→ sensor.homeassistant_utilisation_de_la_memoire  (NAT)
  │           └─→ PAGE RÉSERVE SYSTÈME (page_L5C3_systeme_reserve)
  ├─→ Z2M (Zigbee2MQTT) Container (Proxmox)
  │     ├─→ sensor.z2m_utilisation_du_processeur  (NAT)
  │     ├─→ sensor.z2m_uptime  (NAT)
  │     ├─→ sensor.z2m_memory_usage_percentage  (NAT)
  │     └─→ sensor.z2m_utilisation_de_la_memoire  (NAT)
  └─→ MariaDB Container (Proxmox)
        ├─→ sensor.mariadb_utilisation_du_processeur  (NAT)
        ├─→ sensor.mariadb_uptime  (NAT)
        ├─→ sensor.mariadb_memory_usage_percentage  (NAT)
        ├─→ sensor.mariadb_utilisation_de_la_memoire  (NAT)
        └─→ sensor.taille_db_home_assistant  (NAT — SQL)
```

### Entités consommées par la page RÉSERVE SYSTÈME

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.homeassistant_utilisation_du_processeur` | NAT | `proxmox_ve` (intégration) |
| `sensor.homeassistant_uptime` | NAT | `proxmox_ve` (intégration) |
| `sensor.homeassistant_memory_usage_percentage` | NAT | `proxmox_ve` (intégration) |
| `sensor.homeassistant_utilisation_de_la_memoire` | NAT | `proxmox_ve` (intégration) |
| `sensor.z2m_utilisation_du_processeur` | NAT | `proxmox_ve` (intégration) |
| `sensor.z2m_uptime` | NAT | `proxmox_ve` (intégration) |
| `sensor.z2m_memory_usage_percentage` | NAT | `proxmox_ve` (intégration) |
| `sensor.z2m_utilisation_de_la_memoire` | NAT | `proxmox_ve` (intégration) |
| `sensor.mariadb_utilisation_du_processeur` | NAT | `proxmox_ve` (intégration) |
| `sensor.mariadb_uptime` | NAT | `proxmox_ve` (intégration) |
| `sensor.mariadb_memory_usage_percentage` | NAT | `proxmox_ve` (intégration) |
| `sensor.mariadb_utilisation_de_la_memoire` | NAT | `proxmox_ve` (intégration) |
| `sensor.taille_db_home_assistant` | NAT | `sql.yaml` (requête MariaDB) |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L5C3_15_MariaDB/vignette_L5C3_mariadb_2026-05-10.yaml` | ✅ |
| `Dashboard/L5C3_15_MariaDB/page_L5C3_mariadb_2026-05-10.yaml` (GitHub + MariaDB) | ✅ |
| `Dashboard/L5C3_15_MariaDB/card_mariadb_2026-05-18.yaml` | ✅ |
| `Dashboard/L5C3_15_MariaDB/page_L5C3_systeme_reserve_2026-05-18.yaml` (HA + Z2M + MariaDB) | ✅ |
| `Dashboard/L5C3_15_MariaDB/page_L5C3_mariadb_2026-06-15.yaml` (Audit MD5 + GitHub + MariaDB) | ✅ |

---

## ✅ L6C1 — QUALITÉ DE L'AIR (VIGNETTE + PAGE)
*Validée le 2026-05-14*

### Vignette — Chaîne de dépendances

```
IKEA VINDSTYRKA (Zigbee via Z2M)
  ├─→ sensor.qualite_air_salon_ikea_pm25        (NAT) → vignette PM2.5 Salon (couleur JS)
  ├─→ sensor.qualite_air_bureau_ikea_pm25       (NAT) → vignette PM2.5 Bureau (couleur JS)
  ├─→ sensor.qualite_air_chambre_ikea_pm25      (NAT) → vignette PM2.5 Chambre (couleur JS)
  ├─→ sensor.qualite_air_salon_ikea_voc_index   (NAT) → vignette tCOV Salon (couleur JS)
  ├─→ sensor.qualite_air_bureau_ikea_voc_index  (NAT) → vignette tCOV Bureau (couleur JS)
  └─→ sensor.qualite_air_chambre_ikea_voc_index (NAT) → vignette tCOV Chambre (couleur JS)
        └─→ VIGNETTE L6C1 (custom:button-card)
              ├─→ Grid 3 colonnes × 9 zones (titre + 3×PM2.5 + 3×tCOV)
              ├─→ Seuils PM2.5 : >35→rouge, >11→orange, sinon blanc
              ├─→ Seuils tCOV/VOC index : >1000→rouge, >250→orange, sinon blanc
              ├─→ unavailable/unknown → gris #808080
              └─→ tap_action: navigate → /dashboard-tablette/air-quality
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.qualite_air_salon_ikea_pm25` | NAT | IKEA VINDSTYRKA Salon (Z2M) |
| `sensor.qualite_air_bureau_ikea_pm25` | NAT | IKEA VINDSTYRKA Bureau (Z2M) |
| `sensor.qualite_air_chambre_ikea_pm25` | NAT | IKEA VINDSTYRKA Chambre (Z2M) |
| `sensor.qualite_air_salon_ikea_voc_index` | NAT | IKEA VINDSTYRKA Salon (Z2M) |
| `sensor.qualite_air_bureau_ikea_voc_index` | NAT | IKEA VINDSTYRKA Bureau (Z2M) |
| `sensor.qualite_air_chambre_ikea_voc_index` | NAT | IKEA VINDSTYRKA Chambre (Z2M) |

### Page — Chaîne de dépendances

```
IKEA VINDSTYRKA (Zigbee via Z2M)
  ├─→ sensor.qualite_air_salon_ikea_pm25        (NAT) → streamline-card pm25_ring-tile + bouton + pop-up pm25
  ├─→ sensor.qualite_air_bureau_ikea_pm25       (NAT) → streamline-card pm25_ring-tile + bouton + pop-up pm25
  ├─→ sensor.qualite_air_chambre_ikea_pm25      (NAT) → streamline-card pm25_ring-tile + bouton + pop-up pm25
  ├─→ sensor.qualite_air_salon_ikea_voc_index   (NAT) → streamline-card cov_ring-tile + pop-up cov
  ├─→ sensor.qualite_air_bureau_ikea_voc_index  (NAT) → streamline-card cov_ring-tile + pop-up cov
  └─→ sensor.qualite_air_chambre_ikea_voc_index (NAT) → streamline-card cov_ring-tile + pop-up cov

sensors/Air_quality/A_01_AIR_QUALITY.yaml (SEN — stats mean 24h)
  ├─→ sensor.pm2_5_salon_moy_24h   (SEN) → marker2 ring-tile Salon PM2.5
  ├─→ sensor.pm2_5_bureau_moy_24h  (SEN) → marker2 ring-tile Bureau PM2.5
  ├─→ sensor.pm2_5_chambre_moy_24h (SEN) → marker2 ring-tile Chambre PM2.5
  ├─→ sensor.tcov_salon_moy_24h    (SEN) → marker2 ring-tile Salon tCOV
  ├─→ sensor.tcov_bureau_moy_24h   (SEN) → marker2 ring-tile Bureau tCOV
  └─→ sensor.tcov_chambre_moy_24h  (SEN) → marker2 ring-tile Chambre tCOV

templates/Air_quality/A_01_AIR_QUALITY.yaml (TPL — conversion ppb)
  ├─→ sensor.tcov_salon_ppb    (TPL) → entity bouton tCOV Salon + streamline-card cov
  ├─→ sensor.tcov_bureau_ppb   (TPL) → entity bouton tCOV Bureau + streamline-card cov
  └─→ sensor.tcov_chambre_ppb  (TPL) → entity bouton tCOV Chambre + streamline-card cov

        └─→ PAGE L6C1 — 3 sections (SALON / BUREAU / CHAMBRE)
              ├─→ custom:streamline-card templates : pm25_ring-tile, cov_ring-tile, pm25, cov
              ├─→ custom:bubble-card pop-up via hash (#spm25, #scov, #bpm25, #bcov, #cpm25, #ccov)
              └─→ bubble-card separator × 3 (SALON, BUREAU, CHAMBRE)
```

### Entités consommées par la page

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.qualite_air_salon_ikea_pm25` | NAT | IKEA VINDSTYRKA Salon (Z2M) |
| `sensor.qualite_air_bureau_ikea_pm25` | NAT | IKEA VINDSTYRKA Bureau (Z2M) |
| `sensor.qualite_air_chambre_ikea_pm25` | NAT | IKEA VINDSTYRKA Chambre (Z2M) |
| `sensor.qualite_air_salon_ikea_voc_index` | NAT | IKEA VINDSTYRKA Salon (Z2M) |
| `sensor.qualite_air_bureau_ikea_voc_index` | NAT | IKEA VINDSTYRKA Bureau (Z2M) |
| `sensor.qualite_air_chambre_ikea_voc_index` | NAT | IKEA VINDSTYRKA Chambre (Z2M) |
| `sensor.pm2_5_salon_moy_24h` | SEN | `sensors/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.pm2_5_bureau_moy_24h` | SEN | `sensors/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.pm2_5_chambre_moy_24h` | SEN | `sensors/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.tcov_salon_moy_24h` | SEN | `sensors/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.tcov_bureau_moy_24h` | SEN | `sensors/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.tcov_chambre_moy_24h` | SEN | `sensors/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.tcov_salon_ppb` | TPL | `templates/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.tcov_bureau_ppb` | TPL | `templates/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.tcov_chambre_ppb` | TPL | `templates/Air_quality/A_01_AIR_QUALITY.yaml` |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L6C1_16_Air_Qualite/vignette_L6C1_air_qualite_2026-05-14.yaml` | ✅ |
| `Dashboard/L6C1_16_Air_Qualite/page_L6C1_air_qualite_2026-05-14.yaml` | ✅ |

---

## ✅ L6C2 — POLLUTION / POLLEN (VIGNETTE + PAGE)
*Validée le 2026-05-14*

### Vignette — Chaîne de dépendances

```
Atmo France (intégration HACS)
  ├─→ sensor.qualite_globale_vence        (NAT) → score IQA 0-7 → couleur JS Air
  └─→ sensor.qualite_globale_pollen_vence (NAT) → score pollen 0-7 → couleur JS Pollen
        └─→ VIGNETTE L6C2 (custom:button-card — name JS)
              ├─→ Palette couleur 0-7 : grey→green→lightgreen→gold→orange→red→darkred→purple
              ├─→ Affichage : "Air X / Pollen Y" avec couleurs dynamiques
              └─→ tap_action: navigate → /dashboard-tablette/pollen-pollution
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.qualite_globale_vence` | NAT | Intégration Atmo France |
| `sensor.qualite_globale_pollen_vence` | NAT | Intégration Atmo France |

### Page — Chaîne de dépendances

```
Atmo France (intégration HACS) — Section POLLENS
  ├─→ sensor.qualite_globale_pollen_vence    (NAT) → entity-progress-card (barre globale)
  │     └─→ state_attr('Libellé') + state_attr('Couleur') → label + bar_color dynamiques
  ├─→ sensor.concentration_gramine_vence     (NAT) → ring-tile entity
  ├─→ sensor.niveau_gramine_vence            (NAT) → ring-tile ring_entity (index 0-7)
  ├─→ sensor.concentration_ambroisie_vence   (NAT) → ring-tile entity
  ├─→ sensor.niveau_ambroisie_vence          (NAT) → ring-tile ring_entity
  ├─→ sensor.concentration_armoise_vence     (NAT) → ring-tile entity
  ├─→ sensor.niveau_armoise_vence            (NAT) → ring-tile ring_entity
  ├─→ sensor.concentration_aulne_vence       (NAT) → ring-tile entity
  ├─→ sensor.niveau_aulne_vence              (NAT) → ring-tile ring_entity
  ├─→ sensor.concentration_bouleau_vence     (NAT) → ring-tile entity
  ├─→ sensor.niveau_bouleau_vence            (NAT) → ring-tile ring_entity
  ├─→ sensor.concentration_olivier_vence     (NAT) → ring-tile entity
  └─→ sensor.niveau_olivier_vence            (NAT) → ring-tile ring_entity

Atmo France (intégration HACS) — Section QUALITE DE L'AIR
  ├─→ sensor.qualite_globale_vence           (NAT) → entity-progress-card (barre globale)
  │     └─→ state_attr('Libellé') + state_attr('Couleur') → label + bar_color dynamiques
  ├─→ sensor.ozone_vence                     (NAT) → ring-tile O₃ (entity + ring_entity identiques)
  ├─→ sensor.dioxyde_d_azote_vence           (NAT) → ring-tile NO₂
  ├─→ sensor.dioxyde_de_soufre_vence         (NAT) → ring-tile SO₂
  ├─→ sensor.pm10_vence                      (NAT) → ring-tile PM10
  └─→ sensor.pm25_vence                      (NAT) → ring-tile PM25

        └─→ PAGE L6C2 — 2 sections (POLLENS / QUALITE DE L'AIR)
              ├─→ custom:entity-progress-card × 2 (barres globales)
              ├─→ custom:ring-tile × 6 (pollens, grid 3 colonnes, scale 0-7)
              ├─→ custom:ring-tile × 5 (polluants, grid 5 colonnes, scale 0-7)
              ├─→ custom:text-divider-row × 2 (séparateurs sections)
              └─→ custom:stack-in-card + custom:vertical-stack-in-card
```

### Entités consommées par la page

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.qualite_globale_pollen_vence` | NAT | Intégration Atmo France |
| `sensor.qualite_globale_vence` | NAT | Intégration Atmo France |
| `sensor.concentration_gramine_vence` | NAT | Intégration Atmo France |
| `sensor.niveau_gramine_vence` | NAT | Intégration Atmo France |
| `sensor.concentration_ambroisie_vence` | NAT | Intégration Atmo France |
| `sensor.niveau_ambroisie_vence` | NAT | Intégration Atmo France |
| `sensor.concentration_armoise_vence` | NAT | Intégration Atmo France |
| `sensor.niveau_armoise_vence` | NAT | Intégration Atmo France |
| `sensor.concentration_aulne_vence` | NAT | Intégration Atmo France |
| `sensor.niveau_aulne_vence` | NAT | Intégration Atmo France |
| `sensor.concentration_bouleau_vence` | NAT | Intégration Atmo France |
| `sensor.niveau_bouleau_vence` | NAT | Intégration Atmo France |
| `sensor.concentration_olivier_vence` | NAT | Intégration Atmo France |
| `sensor.niveau_olivier_vence` | NAT | Intégration Atmo France |
| `sensor.ozone_vence` | NAT | Intégration Atmo France |
| `sensor.dioxyde_d_azote_vence` | NAT | Intégration Atmo France |
| `sensor.dioxyde_de_soufre_vence` | NAT | Intégration Atmo France |
| `sensor.pm10_vence` | NAT | Intégration Atmo France |
| `sensor.pm25_vence` | NAT | Intégration Atmo France |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L6C2_17_Pollution_Pollen/vignette_L6C2_pollution_pollen_2026-05-14.yaml` | ✅ |
| `Dashboard/L6C2_17_Pollution_Pollen/page_L6C2_pollution_pollen_2026-05-14.yaml` | ✅ |

---

## ✅ L6C3 — VIGILANCE EAU / VIGIEAU (VIGNETTE + PAGE)
*Validée le 2026-05-14*

### Vignette — Chaîne de dépendances

```
VigiEau (intégration HACS)
  └─→ sensor.alert_level_in_vence         (NAT) → icon dynamique (attr.icon) + couleur (attr.Couleur)
        └─→ VIGNETTE L6C3 (custom:button-card — icon + name JS)
              ├─→ Icon : sensor.attributes.icon (fourni par l'intégration) ou mdi:water-outline
              ├─→ Couleur icône : sensor.attributes.Couleur ou white
              ├─→ Niveaux : null / vigilance (pas de restriction) / vigilance / alerte / alerte_renforcee / crise
              └─→ tap_action: navigate → /dashboard-tablette/vigieau
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.alert_level_in_vence` | NAT | Intégration VigiEau (HACS) |

### Page — Chaîne de dépendances

```
VigiEau (intégration HACS) — Section SÉCHERESSE
  ├─→ sensor.alert_level_in_vence          (NAT) → button-card état global (6 niveaux colorés)
  │     └─→ states : null/vigilance/alerte/alerte_renforcee/crise → icône + couleur dédiés
  ├─→ sensor.alert_level_in_vence_numeric  (NAT) → bar-card jauge 0-4 (severity colorée)
  │     └─→ attributes.icon + attributes.Couleur → icône et couleur dynamiques
  └─→ sensor.*_restrictions_vence          (NAT, auto-entities glob) → grille 4 colonnes button-cards
        ├─→ Couleur border + icône selon état : Aucune restriction / Sensibilisation /
        │   Interdiction sauf exception / Interdiction (+ fallback longueur > 30 car.)
        ├─→ tap_action: browser_mod.popup → détail complet de la restriction
        └─→ exclude: state = "Aucune restriction" (masque les usages sans restriction)
```

### Entités consommées par la page

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.alert_level_in_vence` | NAT | Intégration VigiEau (HACS) |
| `sensor.alert_level_in_vence_numeric` | NAT | Intégration VigiEau (HACS) |
| `sensor.*_restrictions_vence` (glob) | NAT | Intégration VigiEau (HACS) — entités dynamiques par usage |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/L6C3_18_VigiEau/vignette_L6C3_vigieau_2026-05-14.yaml` | ✅ |
| `Dashboard/L6C3_18_VigiEau/page_L6C3_vigieau_2026-05-14.yaml` | ✅ |

---

## ✅ HOME PAGE — CARTES PERMANENTES (hors grille 18 vignettes)
*Validée le 2026-06-13*

> Les 18 vignettes de la grille sont documentées dans leurs sections respectives (L1C1–L6C3).
> Cette section couvre **uniquement les cartes permanentes en haut de la HOME page** qui n'appartiennent à aucune vignette.

### Chaîne de dépendances globale

```
HOME PAGE (type: grid)
  ├─→ [1] picture-elements — meteocss v2.2.1
  │     ├─→ packages/cssmeteo.yaml + custom_templates/meteo.jinja
  │     │     └─→ (fond animé ciel + foreground nuages/pluie/neige)
  │     ├─→ custom_templates/rotation.jinja
  │     │     ├─→ sensor.sun_left / sun_top / sun_opacity  (TPL meteocss)
  │     │     └─→ sensor.moon_left / moon_top / moon_opacity / moon_phase  (TPL meteocss)
  │     ├─→ sensor.moon_api (attr: moon_parallactic_angle)  (NAT — intégration Moon)
  │     ├─→ sensor.vence_original_condition  (NAT — command_line/meteo/carte_meteo_france.yaml)
  │     ├─→ sensor.th_balcon_nord_temperature  (NAT — SONOFF via Z2M)
  │     └─→ sensor.alerte_meteo  (TPL — templates/meteo/M_01_meteo_alertes_card.yaml)
  ├─→ [2] meteofrance-weather-card  (toujours visible)
  │     └─→ weather.vence + sensor.vence_* (NAT — Météo France)
  ├─→ [3] conditional — VS Code Server  (visible si CPU > 1%)
  │     └─→ sensor.studio_code_server_pourcentage_du_processeur  (NAT — Studio Code Server add-on)
  ├─→ [4] button-card — Foudre  (visible si lightning_counter > 1)
  │     ├─→ sensor.maison_lightning_counter  (TPL — M_03_meteo_blitzortung.yaml)
  │     ├─→ sensor.maison_lightning_distance  (TPL — idem)
  │     ├─→ sensor.maison_lightning_localisation  (TPL — idem)
  │     ├─→ sensor.maison_lightning_azimuth  (TPL — idem)
  │     └─→ sensor.dernier_impact_temps_reel  (TPL — idem)
  ├─→ [5] mushroom — Lave-linge  (visible si power > 50W)
  │     └─→ sensor.prise_lave_linge_nous_power  (NAT — NOUS SP via Z2M)
  ├─→ [6] mushroom — Lave-vaisselle  (visible si power > 50W)
  │     └─→ sensor.prise_lave_vaisselle_nous_power  (NAT — NOUS SP via Z2M)
  ├─→ [7] bubble-card separator + 2× button — Présence
  │     ├─→ sensor.etat_wifi_maison  (TPL — P4/02_logique_wifi_cellular.yaml)
  │     ├─→ device_tracker.poco  (NAT — Mobile App Eric)
  │     ├─→ person.eric  (NAT — HA Personnes)
  │     ├─→ device_tracker.mamour  (NAT — Mobile App Mamour)
  │     └─→ person.mamour  (NAT — HA Personnes)
  ├─→ [8] mushroom — Détecteur fuite  (visible si on | unavailable | unknown)
  │     └─→ binary_sensor.detecteur_de_fuite_ikea_water_leak  (NAT — IKEA Vallhorn via Z2M)
  └─→ [9] type: grid — 18 vignettes  (voir sections L1C1–L6C3)
```

### Entités consommées — Cartes permanentes HOME

| Entité | Type | Fichier source | Carte |
|:-------|:----:|:--------------|:------|
| `sensor.sun_left` | TPL | `custom_templates/rotation.jinja` (meteocss) | [1] picture-elements |
| `sensor.sun_top` | TPL | idem | [1] |
| `sensor.sun_opacity` | TPL | idem | [1] |
| `sensor.moon_left` | TPL | idem | [1] |
| `sensor.moon_top` | TPL | idem | [1] |
| `sensor.moon_opacity` | TPL | idem | [1] |
| `sensor.moon_phase` | TPL | idem | [1] |
| `sensor.moon_api` (attr: `moon_parallactic_angle`) | NAT | Intégration Moon (HACS) | [1] |
| `sensor.vence_original_condition` | NAT | `command_line/meteo/carte_meteo_france.yaml` | [1] |
| `sensor.th_balcon_nord_temperature` | NAT | SONOFF via Z2M | [1] |
| `sensor.alerte_meteo` | TPL | `templates/meteo/M_01_meteo_alertes_card.yaml` | [1] |
| `weather.vence` | NAT | Météo France | [2] |
| `sensor.vence_rain_chance` / `vence_uv` / `vence_cloud_cover` | NAT | Météo France | [2] |
| `sensor.vence_freeze_chance` / `vence_snow_chance` / `vence_next_rain` | NAT | Météo France | [2] |
| `sensor.06_weather_alert` | NAT | Météo France | [2] |
| `sensor.temperature_delta_affichage` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` | [2] |
| `sensor.studio_code_server_pourcentage_du_processeur` | NAT | Studio Code Server add-on | [3] |
| `sensor.maison_lightning_counter` | TPL | `templates/meteo/M_03_meteo_blitzortung.yaml` | [4] |
| `sensor.maison_lightning_distance` | TPL | idem | [4] |
| `sensor.maison_lightning_localisation` | TPL | idem | [4] |
| `sensor.maison_lightning_azimuth` | TPL | idem | [4] |
| `sensor.dernier_impact_temps_reel` | TPL | idem | [4] |
| `sensor.prise_lave_linge_nous_power` | NAT | NOUS SP via Z2M (P2 — cuisine) | [5] |
| `sensor.prise_lave_vaisselle_nous_power` | NAT | NOUS SP via Z2M (P2 — cuisine) | [6] |
| `sensor.etat_wifi_maison` | TPL | `templates/P4_groupe_presence/02_logique_wifi_cellular.yaml` | [7] |
| `device_tracker.poco` | NAT | Mobile App (Companion) — Eric | [7] |
| `person.eric` | NAT | HA Personnes | [7] |
| `device_tracker.mamour` | NAT | Mobile App (Companion) — Mamour | [7] |
| `person.mamour` | NAT | HA Personnes | [7] |
| `binary_sensor.detecteur_de_fuite_ikea_water_leak` | NAT | IKEA Vallhorn via Z2M | [8] |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `Dashboard/PAGE_Home/page_home_2026-06-13.yaml` | ✅ page complète |
| `Dashboard/PAGE_Home/card_meteocss_home_2026-06-13.yaml` | ✅ picture-elements 7 layers |
| `Dashboard/PAGE_Home/card_vscode_home_2026-06-13.yaml` | ✅ VS Code conditional |
| `Dashboard/PAGE_Home/card_foudre_home_2026-06-13.yaml` | ✅ Foudre button-card |
| `Dashboard/PAGE_Home/card_lave_linge_home_2026-06-13.yaml` | ✅ Lave-linge mushroom |
| `Dashboard/PAGE_Home/card_lave_vaisselle_home_2026-06-13.yaml` | ✅ Lave-vaisselle mushroom |
| `Dashboard/PAGE_Home/card_presence_home_2026-06-13.yaml` | ✅ Présence (separator + Eric + Mamour) |
| `Dashboard/PAGE_Home/card_detecteur_fuite_home_2026-06-13.yaml` | ✅ Détecteur fuite mushroom |

### Documentation

| Fichier | Statut |
|:--------|:------:|
| `docs_dashboard/docs/HOME PAGE/PAGE_HOME.md` | ✅ (MàJ 2026-06-13) |

---

## 📁 COMPLÉMENT — FICHIERS CONFIG RACINE & RÉPERTOIRES HORS DASHBOARD

> Ces fichiers font partie intégrante de la config HA et sont audités par `audit_md5.sh`.
> Ils n'alimentent pas directement d'entités dashboard — référencés ici pour inventaire complet.
> *Ajouté le 2026-06-15*

### Fichiers racine `/config/`

| Fichier | Rôle | Audité |
|:--------|:-----|:------:|
| `automations.yaml` | Toutes les automations HA (géré via UI) | ✅ |
| `scripts.yaml` | Scripts HA (J-1-x, J-2-0, audit_md5) | ✅ |
| `shell_command/` (répertoire) | Commandes shell (git backup, audit MD5, zone log P4) — `!include_dir_merge_named` | ✅ |
| `configuration.yaml` | Point d'entrée HA — includes, intégrations | ✅ |
| `sql.yaml` | Capteurs SQL (taille MariaDB) → L5C3 | ✅ |
| `input_button.yaml` | Boutons virtuels (déclencheurs UI) | ✅ |
| `input_datetime.yaml` | Helpers date/heure | ✅ |
| `input_select.yaml` | Helpers liste (mode soufflant SDB, etc.) | ✅ |
| `scenes.yaml` | Scènes HA | ❌ hors scope |
| `secrets.yaml` | Identifiants — **NE PAS auditer / synchroniser** | ⛔ |

### Répertoires audités (DIRS)

| Répertoire | Contenu | Audité |
|:-----------|:--------|:------:|
| `sensors/` | Intégrations kWh, stats min/max, qualité air | ✅ |
| `templates/` | Calculs, AVG, UI, météo, présence, stores | ✅ |
| `utility_meter/` | Compteurs AMHQ (P0→P3, météo) | ✅ |
| `command_line/` | Météo France, GitHub maintenance, audit MD5, IP externe | ✅ |
| `groups/` | Groupes batteries HUE/IKEA/SONOFF → L5C1 | ✅ |
| `input_booleans/` | Helpers booléens (verrous clim, présence…) | ✅ |
| `input_number/` | Helpers numériques | ✅ |
| `packages/` | Packages CSS météo (cssmeteo.yaml, demometeo.yaml) — Moon API | ✅ |
| `shell_command/` | Commandes shell (backup Git, audit MD5, zone log P4) | ✅ |

### Intégration FILE (UI uniquement — notify.file interdit en YAML)

> Configurée via : Paramètres → Appareils & Services → Ajouter → File
> Génère des services `notify.file_*` utilisés par les automations.

| Service généré | Fichier destination | Utilisé par |
|:---------------|:--------------------|:------------|
| `notify.file_zone_eric_txt` | `/config/.logs/zone_eric.txt` | `shell_command/P4/P4_log_eric_zone.yaml` → automation P4 présence |
| `notify.file_diag_conso_elec_txt` | `/config/notifs/diag_conso_elec.txt` | automation `energie/diag_enregistrement_journalier.yaml` |
| `notify.file_ecart_liky_vs_nodon_txt` | `/config/notifs/ecart_liky_vs_nodon.txt` | automation `energie/log_ecart_linky_vs_nodon.yaml` |

### Répertoires hors scope audit

| Répertoire | Raison |
|:-----------|:-------|
| `.scripts/` | Scripts shell — pas des entités HA |
| `notifs/` | Fichiers .txt — hors périmètre YAML |
| `blueprints/` | Blueprints HA — non modifiés manuellement |
| `custom_components/` | Intégrations HACS — non versionnées ici |
| `www/` | Ressources frontend — hors config HA |
| `docs_da