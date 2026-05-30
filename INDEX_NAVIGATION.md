# 📇 INDEX NAVIGATION — L1C1

*Structure arborescente avec pop-ups — Test avec L1C1 Météo*

---

## L1C1_01_METEO

### Vignette L1C1
- [📄 Docs Vignette](docs_dashboard/L1C1_01_METEO/L1C1_VIGNETTE_METEO.md)
- [⚙️ YAML Vignette](Dashboard/L1C1_01_METEO/vignette_L1C1_meteo_2026-05-29.yaml)

### Page L1C1
- [📄 Docs Page](docs_dashboard/L1C1_01_METEO/PAGE_METEO.md)
- [⚙️ YAML Page](Dashboard/L1C1_01_METEO/page_L1C1_meteo_2026-05-29.yaml)

#### Pop-up #ALERT
- [→ Section du YAML page](docs_dashboard/L1C1_01_METEO/PAGE_METEO.md#pop-up-alert)
- *(Extraction de [`page_L1C1_meteo_2026-05-29.yaml`](Dashboard/L1C1_01_METEO/page_L1C1_meteo_2026-05-29.yaml))*

#### Pop-up #FOUDRE
- [→ Section du YAML page](docs_dashboard/L1C1_01_METEO/PAGE_METEO.md#pop-up-foudre)
- *(Extraction de [`page_L1C1_meteo_2026-05-29.yaml`](Dashboard/L1C1_01_METEO/page_L1C1_meteo_2026-05-29.yaml))*

#### Pop-up #SUN
- [→ Section du YAML page](docs_dashboard/L1C1_01_METEO/PAGE_METEO.md#pop-up-sun)
- *(Extraction de [`page_L1C1_meteo_2026-05-29.yaml`](Dashboard/L1C1_01_METEO/page_L1C1_meteo_2026-05-29.yaml))*

### Entités — Groupées par fichier source

#### [`docs_dashboard/TREE_CORRIGE/templates/meteo/M_02_meteo_vent_vence_card.yaml`](docs_dashboard/TREE_CORRIGE/templates/meteo/M_02_meteo_vent_vence_card.yaml)
- `sensor.meteo_france_wind_speed`
- `sensor.meteo_france_wind_bearing`
- `sensor.meteo_france_vent_vence_card_content`

#### [`docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml`](docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml)
- `sensor.meteo_france_alerte_card_content`

#### [`docs_dashboard/TREE_CORRIGE/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml`](docs_dashboard/TREE_CORRIGE/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml)
- `sensor.blitzortung_lightning_count`
- `sensor.blitzortung_lightning_distance`

#### [`docs_dashboard/TREE_CORRIGE/templates/meteo/M_03_meteo_blitzortung.yaml`](docs_dashboard/TREE_CORRIGE/templates/meteo/M_03_meteo_blitzortung.yaml)
- `sensor.blitzortung_card_content`

#### [`docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml`](docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml)
- `sensor.tendances_th_ext_card_content`

#### NAT — Intégrations natives HA
- `sensor.th_balcon_nord_temperature` (Z2M SONOFF balcon Nord)
- `sensor.th_balcon_nord_humidity` (Z2M SONOFF balcon Nord)
- `sensor.sun_next_rising` (HA Core — sun.sun)
- `sensor.sun_next_setting` (HA Core — sun.sun)

---

**Renommer:** `INDEX_NAVIGATION.md` à la racine du repo