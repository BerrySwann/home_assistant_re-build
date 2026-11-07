# 📇 INDEX ENTITÉS - RÉFÉRENCE BIDIRECTIONNELLE

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--31-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-System-ffeb3b?style=flat-square)](.)

</div>

*Généré depuis docs/00_IA/00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.md (2026-07-14)*

*Mise à jour 2026-10-18 : resync des chemins (531 chemins remis aux noms réels après les renommages du 17/10 : 02_dashboard_docs_MD, 02_dashboard_docs_YAML, L0C0_PAGE_Home, pages 02_Page) ; entités inchangées.*

*Mise à jour 2026-09-29 : deux entités renommées (sensor.mode_ete_hiver, sensor.proxmox_cpu_package), neuf entités disparues retirées (cartes météo/blitzortung, ancienne prise radiateur).*

*Section HOME PAGE ajoutée manuellement le 2026-09-20 (intégration WashData).*

*Mise à jour 2026-09-24 : contact porte Congélateur (HOME PAGE + L1C2) + batterie porte_congel (L5C1).*

**Navigation:** Cherche une entité → trouve sa source + son utilisation dans les vignettes/pages

---

## HOME PAGE

### `sensor.lave_linge_etat`
- **Vignette:** HOME PAGE
- **Type:** sensor
- **Source:** WashData (HACS) - appareil Lave-Linge
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/`

### `sensor.lave_linge_temps_restant`
- **Vignette:** HOME PAGE
- **Type:** sensor
- **Source:** WashData (HACS) - appareil Lave-Linge
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/`

### `sensor.lave_linge_progres`
- **Vignette:** HOME PAGE
- **Type:** sensor
- **Source:** WashData (HACS) - appareil Lave-Linge
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/`

### `sensor.prise_lave_linge_nous_power`
- **Vignette:** HOME PAGE
- **Type:** sensor
- **Source:** NOUS SP via Z2M (P2) - prise lave-linge
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/`

### `sensor.lave_vaisselle_etat`
- **Vignette:** HOME PAGE
- **Type:** sensor
- **Source:** WashData (HACS) - appareil Lave-Vaisselle
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/`

### `sensor.lave_vaisselle_temps_restant`
- **Vignette:** HOME PAGE
- **Type:** sensor
- **Source:** WashData (HACS) - appareil Lave-Vaisselle
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/`

### `sensor.lave_vaisselle_progres`
- **Vignette:** HOME PAGE
- **Type:** sensor
- **Source:** WashData (HACS) - appareil Lave-Vaisselle
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/`

### `sensor.prise_lave_vaisselle_nous_power`
- **Vignette:** HOME PAGE
- **Type:** sensor
- **Source:** NOUS SP via Z2M (P2) - prise lave-vaisselle
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/`

### `sensor.prise_congelateur_cuisine_nous_power`
- **Vignette:** HOME PAGE
- **Type:** sensor
- **Source:** NOUS SP via Z2M (P2) - prise congélateur cuisine
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/`

### `switch.prise_congelateur_cuisine_nous`
- **Vignette:** HOME PAGE
- **Type:** switch
- **Source:** NOUS SP via Z2M (P2) - prise congélateur cuisine
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/`

### `sensor.tongel_temperature`
- **Vignette:** HOME PAGE
- **Type:** sensor
- **Source:** SONOFF Tongel via Z2M - sonde congélateur
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/`

---

### `binary_sensor.porte_congel_contact`
- **Vignette:** HOME PAGE (carte Congélateur #7)
- **Type:** binary_sensor (contact porte)
- **Source:** Z2M - équipement porte_congel
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/08_Congélateur/Card_congelateur_home.yaml`

## L1C1

### `sensor.sun_next_rising`
- **Vignette:** L1C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C1_*/`L1C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C1_*/`

### `sensor.sun_next_setting`
- **Vignette:** L1C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C1_*/`L1C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C1_*/`

### `sensor.th_balcon_nord_humidity`
- **Vignette:** L1C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C1_*/`L1C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C1_*/`

### `sensor.th_balcon_nord_temperature`
- **Vignette:** L1C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C1_*/`L1C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C1_*/`

### `sensor.variation_quotidienne`
- **Vignette:** L1C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C1_*/`L1C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C1_*/`

## L1C2

*(Complété le 2026-09-20 : entités cartes clim button-card + bloc Congélateur + tendances balcon)*

### `sensor.clim_rad_total_avg_watts_quotidien`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.conso_clim_rad_total`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.conso_clim_rad_total_mensuel`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.conso_clim_rad_total_quotidien`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.temperature_delta_affichage`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.temperature_moyenne_interieure`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_balcon_nord_humidity`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_balcon_nord_temperature`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_bureau_humidity`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_bureau_temperature`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_cellier_humidity`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_cellier_temperature`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_chambre_humidity`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_chambre_temperature`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_cuisine_humidity`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_cuisine_temperature`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_salle_de_bain_humidity`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_salle_de_bain_temperature`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_salon_humidity`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_salon_temperature`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.vence_temperature`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`


### `climate.soufflant_salle_de_bain`
- **Vignette:** L1C2
- **Type:** climate
- **Source:** Helper UI generic_thermostat (créé 2026-03-22)
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.clim_salon_nous_power`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.clim_bureau_nous_power`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.clim_chambre_nous_power`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.radiateur_elec_cuisine_power`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.prise_soufflant_salle_de_bain_nous_power`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.tongel_battery`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.tongel_humidity`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.tongel_temperature`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_balcon_nord_humidity_trend`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `sensor.th_balcon_nord_temperature_trend`
- **Vignette:** L1C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C2_*/`L1C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_*/`

### `binary_sensor.porte_congel_contact`
- **Vignette:** L1C2 (carte appliance Congélateur, fin de page #42)
- **Type:** binary_sensor (contact porte)
- **Source:** Z2M - équipement porte_congel
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C2_TEMPERATURES/L1C2_TEMPERATURES_02_Page/L1C2_Page_TEMPERATURES.yaml`

## L1C3

### `sensor.bureau_power_status`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.chambre_power_status`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.clim_bureau_etat`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.clim_chambre_etat`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.clim_salon_etat`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.conso_clim_rad_total`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.cuisine_power_status`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.delta_ademe_recommande`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.mode_ete_hiver_etat`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.prise_soufflant_salle_de_bain_nous_power`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.radiateur_cuisine_etat`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.radiateur_elec_cuisine_power`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.salon_power_status`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.sdb_seche_serviette_etat`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.sdb_seche_serviette_power_status`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.sdb_soufflant_etat`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.sdb_soufflant_power_status`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.temperature_moyenne_interieure`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `sensor.th_salle_de_bain_temperature`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

### `switch.inter_soufflant_salle_de_bain`
- **Vignette:** L1C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L1C3_*/`L1C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L1C3_*/`

## L2C2

*(Complété le 2026-09-20 : entités page Energie Clim - refonte cartes clim button-card + compteurs UM + prises)*

### `sensor.bureau_power_status`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.chambre_power_status`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_bureau_etat`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_bureau_mensuel_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_bureau_quotidien_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_chambre_etat`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_chambre_mensuel_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_chambre_quotidien_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_salon_etat`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_salon_mensuel_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_salon_quotidien_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.conso_clim_rad_total`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.conso_clim_rad_total_mensuel`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.conso_clim_rad_total_quotidien`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.cuisine_power_status`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.dut_clim_bureau`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.dut_clim_chambre`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.dut_clim_salon`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.dut_radiateur_cuisine`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.dut_sdb_total`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.mode_ete_hiver_etat`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.radiateur_cuisine_etat`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.radiateur_elec_cuisine_mensuel_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.radiateur_elec_cuisine_quotidien_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.salon_power_status`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.sdb_seche_serviette_etat`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.sdb_seche_serviette_power_status`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.sdb_soufflant_etat`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.sdb_soufflant_power_status`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.seche_serviette_sdb_mensuel_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.seche_serviette_sdb_quotidien_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.soufflant_sdb_mensuel_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.soufflant_sdb_quotidien_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.temperature_delta_affichage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`


### `climate.clim_bureau_rm4_mini`
- **Vignette:** L2C2
- **Type:** climate
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `climate.clim_chambre_rm4_mini`
- **Vignette:** L2C2
- **Type:** climate
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `climate.clim_salon_rm4_mini`
- **Vignette:** L2C2
- **Type:** climate
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `climate.radiateur_cuisine`
- **Vignette:** L2C2
- **Type:** climate
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.bureau_power_status_affichage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.chambre_power_status_affichage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.cuisine_power_status_affichage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.salon_power_status_affichage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.sdb_power_status_affichage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.sdb_seche_serviette_power_status_affichage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_bureau_annuel_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_bureau_hebdomadaire_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_chambre_annuel_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_chambre_hebdomadaire_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_salon_annuel_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_salon_hebdomadaire_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.radiateur_elec_cuisine_annuel_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.radiateur_elec_cuisine_hebdomadaire_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.soufflant_sdb_annuel_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.soufflant_sdb_hebdomadaire_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.seche_serviette_sdb_annuel_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.seche_serviette_sdb_hebdomadaire_um`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_salon_avg_watts_quotidien`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_salon_avg_watts_mensuel`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_bureau_avg_watts_quotidien`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_bureau_avg_watts_mensuel`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_chambre_avg_watts_quotidien`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_chambre_avg_watts_mensuel`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.radiateur_elec_cuisine_avg_watts_quotidien`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.radiateur_elec_cuisine_avg_watts_mensuel`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.soufflant_sdb_avg_watts_quotidien`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.soufflant_sdb_avg_watts_mensuel`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.seche_serviette_sdb_avg_watts_quotidien`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.seche_serviette_sdb_avg_watts_mensuel`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_salon_nous_current`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_salon_nous_energy`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_salon_nous_voltage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_bureau_nous_current`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_bureau_nous_energy`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_bureau_nous_voltage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_chambre_nous_current`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_chambre_nous_energy`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.clim_chambre_nous_voltage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.radiateur_elec_cuisine_current`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.radiateur_elec_cuisine_energy`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.radiateur_elec_cuisine_voltage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.prise_soufflant_salle_de_bain_nous_current`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.prise_soufflant_salle_de_bain_nous_energy`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.prise_soufflant_salle_de_bain_nous_voltage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.prise_seche_serviette_salle_de_bain_nous_power`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.prise_seche_serviette_salle_de_bain_nous_current`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.prise_seche_serviette_salle_de_bain_nous_energy`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.prise_seche_serviette_salle_de_bain_nous_voltage`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

### `sensor.mode_ete_hiver`
- **Vignette:** L2C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C2_*/`L2C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C2_*/`

## L2C3

### `sensor.eclairage_total_group_puissance_tpl`
- **Vignette:** L2C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C3_*/`L2C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C3_*/`

### `sensor.eclairage_total_unit_mensuel_kwh_tpl`
- **Vignette:** L2C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C3_*/`L2C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C3_*/`

### `sensor.eclairage_total_unit_quotidien_kwh_tpl`
- **Vignette:** L2C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C3_*/`L2C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C3_*/`

### `sensor.lumiere_appartement_etat`
- **Vignette:** L2C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C3_*/`L2C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C3_*/`

### `sensor.lumiere_bureau_etat`
- **Vignette:** L2C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C3_*/`L2C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C3_*/`

### `sensor.lumiere_chambre_etat`
- **Vignette:** L2C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C3_*/`L2C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C3_*/`

### `sensor.lumiere_cuisine_etat`
- **Vignette:** L2C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C3_*/`L2C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C3_*/`

### `sensor.lumiere_salle_de_bain_etat`
- **Vignette:** L2C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C3_*/`L2C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C3_*/`

### `sensor.lumiere_salon_etat`
- **Vignette:** L2C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C3_*/`L2C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C3_*/`

### `switch.relais_lumiere_sdb_sonoff`
- **Vignette:** L2C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L2C3_*/`L2C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L2C3_*/`

## L3C1

### `sensor.bureau_etat`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.chambre_etat`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.lumiere_appartement_etat`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.lumiere_bureau_etat`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.lumiere_chambre_etat`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.lumiere_cuisine_etat`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.lumiere_ecran_etat`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.lumiere_salle_de_bain_etat`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.lumiere_salon_etat`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.lumiere_tete_de_lit_etat`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.th_bureau_temperature`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.th_chambre_temperature`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.th_cuisine_temperature`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.th_salle_de_bain_temperature`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `sensor.th_salon_temperature`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `switch.prise_tete_de_lit_chambre`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

### `switch.relais_lumiere_sdb_sonoff`
- **Vignette:** L3C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C1_*/`L3C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C1_*/`

## L3C2

### `light.hue_smart_eco_pc_bureau`
- **Vignette:** L3C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C2_*/`L3C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C2_*/`

### `light.hue_smart_eco_salon`
- **Vignette:** L3C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C2_*/`L3C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C2_*/`

### `light.hue_smart_eco_tv_chambre`
- **Vignette:** L3C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C2_*/`L3C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C2_*/`

### `switch.prise_horloge_ikea`
- **Vignette:** L3C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C2_*/`L3C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C2_*/`

### `switch.prise_tete_de_lit_chambre`
- **Vignette:** L3C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C2_*/`L3C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C2_*/`

### `switch.prise_tv_salon_ikea`
- **Vignette:** L3C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C2_*/`L3C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C2_*/`

## L3C3

### `binary_sensor.contact_fenetre_bureau_sonoff_contact`
- **Vignette:** L3C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C3_*/`L3C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C3_*/`

### `binary_sensor.contact_fenetre_chambre_sonoff_contact`
- **Vignette:** L3C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C3_*/`L3C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C3_*/`

### `binary_sensor.contact_fenetre_cuisine_sonoff_contact`
- **Vignette:** L3C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C3_*/`L3C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C3_*/`

### `binary_sensor.contact_fenetre_salon_sonoff_contact`
- **Vignette:** L3C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C3_*/`L3C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C3_*/`

### `sensor.contact_fenetre_bureau_sonoff_battery`
- **Vignette:** L3C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C3_*/`L3C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C3_*/`

### `sensor.contact_fenetre_salon_sonoff_battery`
- **Vignette:** L3C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C3_*/`L3C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C3_*/`

### `sensor.store_bureau_signal_strength`
- **Vignette:** L3C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C3_*/`L3C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C3_*/`

### `sensor.store_bureau_status`
- **Vignette:** L3C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C3_*/`L3C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C3_*/`

### `sensor.store_salon_signal_strength`
- **Vignette:** L3C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C3_*/`L3C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C3_*/`

### `sensor.store_salon_status`
- **Vignette:** L3C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C3_*/`L3C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C3_*/`

### `sensor.th_balcon_nord_temperature`
- **Vignette:** L3C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L3C3_*/`L3C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L3C3_*/`

## L4C1

### `binary_sensor.pve_backup_status`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `binary_sensor.pve_status`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.homeassistant_max_cpu`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.homeassistant_memory_usage_percentage`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.homeassistant_statut`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.homeassistant_uptime`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.homeassistant_utilisation_du_disque`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.homeassistant_utilisation_du_processeur`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.mariadb_max_cpu`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.mariadb_memory_usage_percentage`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.mariadb_statut`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.mariadb_uptime`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.mariadb_utilisation_du_disque`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.mariadb_utilisation_du_processeur`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.pve_max_cpu`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.pve_memory_usage_percentage`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.pve_statut`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.pve_uptime`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.pve_utilisation_du_disque`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.pve_utilisation_du_processeur`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.storage_local_storage_usage_percentage`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

### `sensor.proxmox_cpu_package`
- **Vignette:** L4C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C1_*/`L4C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C1_*/`

## L4C2

### `sensor.prise_mini_pc_ikea_power`
- **Vignette:** L4C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C2_*/`L4C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C2_*/`

### `sensor.system_monitor_utilisation_de_la_memoire`
- **Vignette:** L4C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C2_*/`L4C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C2_*/`

### `sensor.system_monitor_utilisation_du_disque`
- **Vignette:** L4C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C2_*/`L4C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C2_*/`

### `sensor.system_monitor_utilisation_du_processeur`
- **Vignette:** L4C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C2_*/`L4C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C2_*/`

### `sensor.proxmox_cpu_package`
- **Vignette:** L4C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C2_*/`L4C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C2_*/`

## L4C3

### `sensor.available_updates`
- **Vignette:** L4C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L4C3_*/`L4C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C3_*/`

## L5C1

### `sensor.porte_congel_battery`
- **Vignette:** L5C1 (carte Batteries - Thermostats SONOFF) + `group.sonoff_devices`
- **Type:** sensor (batterie %)
- **Source:** Z2M - équipement porte_congel
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C1_PILES_BATTERIES/L5C1_PILES_BATTERIES_02_Page/L5C1_Page_PILES_BATTERIES.yaml`

## L5C2

### `sensor.eric_battery_level`
- **Vignette:** L5C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C2_*/`L5C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C2_*/`

### `sensor.mamour_battery_level`
- **Vignette:** L5C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C2_*/`L5C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C2_*/`

### `sensor.tablette_battery_level`
- **Vignette:** L5C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C2_*/`L5C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C2_*/`

## L5C3

### `proxmox_ve`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.backup_github_journal`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.backup_github_status`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.git_last_weekly_tag`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.github_default_branch`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.homeassistant_memory_usage_percentage`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.homeassistant_uptime`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.homeassistant_utilisation_de_la_memoire`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.homeassistant_utilisation_du_processeur`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.mariadb_memory_usage_percentage`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.mariadb_uptime`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.mariadb_utilisation_de_la_memoire`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.mariadb_utilisation_du_processeur`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

### `sensor.taille_db_home_assistant`
- **Vignette:** L5C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L5C3_*/`L5C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L5C3_*/`

## L6C1

### `sensor.qualite_air_bureau_ikea_voc_index`
- **Vignette:** L6C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C1_*/`L6C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C1_*/`

### `sensor.qualite_air_chambre_ikea_voc_index`
- **Vignette:** L6C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C1_*/`L6C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C1_*/`

### `sensor.qualite_air_salon_ikea_voc_index`
- **Vignette:** L6C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C1_*/`L6C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C1_*/`

### `sensor.tcov_bureau_ppb`
- **Vignette:** L6C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C1_*/`L6C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C1_*/`

### `sensor.tcov_chambre_ppb`
- **Vignette:** L6C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C1_*/`L6C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C1_*/`

### `sensor.tcov_salon_ppb`
- **Vignette:** L6C1
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C1_*/`L6C1_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C1_*/`

## L6C2

### `sensor.concentration_ambroisie_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.concentration_armoise_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.concentration_aulne_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.concentration_bouleau_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.concentration_gramine_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.concentration_olivier_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.dioxyde_d_azote_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.dioxyde_de_soufre_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.niveau_ambroisie_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.niveau_armoise_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.niveau_aulne_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.niveau_bouleau_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.niveau_gramine_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.niveau_olivier_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.ozone_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.qualite_globale_pollen_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

### `sensor.qualite_globale_vence`
- **Vignette:** L6C2
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C2_*/`L6C2_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C2_*/`

## L6C3

### `sensor.alert_level_in_vence`
- **Vignette:** L6C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C3_*/`L6C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C3_*/`

### `sensor.alert_level_in_vence_numeric`
- **Vignette:** L6C3
- **Type:** sensor/switch/binary_sensor/camera
- **Source:** Voir ``docs/02_docs_dashboard/02_dashboard_docs_MD/L6C3_*/`L6C3_*/`
- **YAML:** `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C3_*/`

<!-- RECAP-ENTITES:DEBUT -->

## Recapitulatif des entites citees par cet index

Total : **684 entites**. Origine de chacune : type, puis le nom de l integration telle qu elle apparait dans Appareils et services.

| origine | nombre | explication |
|:---|---:|:---|
| CREE template | 248 | creee par un YAML du depot, dossier `template`, sans aucune integration dans Appareils et services |
| NAT mqtt | 128 | chaine a trois maillons, verifiee le 2026-11-03 : Zigbee2MQTT (conteneur 200, Proxmox 10.32.154.244) publie vers le broker `core-mosquitto` (add-on Mosquitto, port 1883), que consomme l integration `mqtt` d Appareils et services. Si un des trois manque, les entites tombent |
| CREE utility_meter | 76 | creee par un YAML du depot, dossier `utility_meter`, sans aucune integration dans Appareils et services |
| NAT mobile_app | 49 | integration `mobile_app` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT hue | 35 | integration `hue` du coeur de Home Assistant, installee et visible dans Appareils et services |
| HACS atmofrance | 19 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services sous le nom `Atmo France - Vence` |
| HACS powercalc | 19 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services en 38 entrees (premiere : `Hue ambiance lamp salon 1`) |
| NAT systemmonitor | 11 | integration `systemmonitor` du coeur de Home Assistant, installee et visible dans Appareils et services |
| HACS scheduler | 9 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services sous le nom `Scheduler` |
| CREE statistics | 8 | creee par un YAML du depot, dossier `statistics`, sans aucune integration dans Appareils et services |
| CREE input_booleans | 7 | creee par un YAML du depot, dossier `input_booleans`, sans aucune integration dans Appareils et services |
| HACS meross_lan | 6 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services en 2 entrees (premiere : `Store SALON`) |
| CREE command_line | 5 | creee par un YAML du depot, dossier `command_line`, sans aucune integration dans Appareils et services |
| NAT hassio | 5 | integration `hassio` du coeur de Home Assistant, installee et visible dans Appareils et services |
| CREE history_stats | 4 | creee par un YAML du depot, dossier `history_stats`, sans aucune integration dans Appareils et services |
| CREE timers | 4 | creee par un YAML du depot, dossier `timers`, sans aucune integration dans Appareils et services |
| NAT broadlink | 4 | integration `broadlink` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT meteo_france | 4 | integration `meteo_france` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT proxmoxve | 4 | integration `proxmoxve` du coeur de Home Assistant, installee et visible dans Appareils et services |
| CREE groups | 3 | creee par un YAML du depot, dossier `groups`, sans aucune integration dans Appareils et services |
| CREE smartir | 3 | creee par un YAML du depot, dossier `smartir`, sans aucune integration dans Appareils et services |
| HACS blitzortung | 3 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services sous le nom `Maison` |
| NAT template | 3 | integration `template` du coeur de Home Assistant, installee et visible dans Appareils et services |
| RASPI-PI4-4GO | 3 | entites du Raspberry Pi 4 4 Go : elles existent, le materiel est hors tension (pour Raspberry Pi4 4Go) |
| CREE input_button | 2 | creee par un YAML du depot, dossier `input_button`, sans aucune integration dans Appareils et services |
| CREE input_number | 2 | creee par un YAML du depot, dossier `input_number`, sans aucune integration dans Appareils et services |
| CREE person | 2 | creee par un YAML du depot, dossier `person`, sans aucune integration dans Appareils et services |
| CREE script | 2 | creee par un YAML du depot, dossier `script`, sans aucune integration dans Appareils et services |
| HACS vigieau | 2 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services sous le nom `Vigieau AEP` |
| NAT generic_thermostat | 2 | integration `generic_thermostat` du coeur de Home Assistant, installee et visible dans Appareils et services |
| ARTEFACT-TEMPLATE | 1 | mot-cle de template, pas une entite |
| CREE automation | 1 | creee par un YAML du depot, dossier `automation`, sans aucune integration dans Appareils et services |
| CREE input_datetime | 1 | creee par un YAML du depot, dossier `input_datetime`, sans aucune integration dans Appareils et services |
| CREE input_select | 1 | creee par un YAML du depot, dossier `input_select`, sans aucune integration dans Appareils et services |
| CREE powercalc | 1 | creee par un YAML du depot, dossier `powercalc`, sans aucune integration dans Appareils et services |
| CREE rest | 1 | creee par un YAML du depot, dossier `rest`, sans aucune integration dans Appareils et services |
| CREE sql | 1 | creee par un YAML du depot, dossier `sql`, sans aucune integration dans Appareils et services |
| HACS hacs | 1 | installee via HACS (qui va etre renomme marketplace) ; son entree dans Appareils et services n a pas de nom affiche |
| NAT cpuspeed | 1 | integration `cpuspeed` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT moon | 1 | integration `moon` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT season | 1 | integration `season` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT-SANS-REGISTRE | 1 | fournie par Home Assistant sans entree au registre (zone.home) |

> **Chaine la plus fragile** : les `NAT mqtt` ne dependent pas que de Home Assistant. Mesure du 2026-11-03 : l integration `mqtt` pointe le broker add-on `core-mosquitto` (1883), et les mesures viennent de Zigbee2MQTT, conteneur 200 sur 10.32.154.244. Conteneur arrete, broker en vrac ou integration retiree : les entites tombent, sans que rien ne le signale dans l interface. A la meme date, 114 des 128 entites citees avaient remonte dans les 2 heures.

*Bloc ecrit par `recap_index.py`, encadre par deux marqueurs : il est remplace a chaque passage, jamais edite a la main. Classification : NAT <integration> si l entree de registre a un config entry ; NAT <integration> pour le coeur de Home Assistant, HACS <integration> pour ce qui vient de HACS ou d un depot (dossier custom_components) ; CREE <famille> sinon, famille = dossier du YAML qui declare l objet ; RASPI-PI4-4GO pour les trois entites du Pi 4 4 Go (materiel hors tension, entites existantes) ; SUPPRIMEE pour les noms remplaces ; ARTEFACT-TEMPLATE pour les mots-cles qui ne sont pas des entites.*

<!-- RECAP-ENTITES:FIN -->
