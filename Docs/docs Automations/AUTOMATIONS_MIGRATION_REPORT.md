# Automations Extraction & Correction Report
**Date:** 2026-04-04  
**Source:** https://raw.githubusercontent.com/BerrySwann/home-assistant-config/main/automations.yaml  
**Destination:** `/sessions/charming-friendly-feynman/mnt/ReBuild/automations/`

---

## Executive Summary

Successfully extracted and corrected **40 Home Assistant automations** from the source repository. All files have been:
- Extracted as individual YAML files
- Organized into 10 functional folders
- Corrected with 8 entity name replacements
- Validated for YAML syntax compliance
- Formatted to match Home Assistant automation standards

---

## File Statistics

| Metric | Count |
|--------|-------|
| Total Automations Extracted | 40 |
| Folders Created | 10 |
| YAML Syntax Valid | 40/40 (100%) |
| Entity Replacements Applied | 78 total |
| Old Patterns Remaining | 0 |

---

## Folder Organization

### 1. **P1_clim_chauffage/** (13 automations)
Climate control system management - day/night operation, notifications, safety features

- `A0_clim_jour_2026-01-01.yaml` — Daytime climate (07h30-21h00)
- `A0_clim_jour_2026-01-11.yaml` — Daytime climate (updated version)
- `B0_clim_nuit_2026-01-02.yaml` — Nighttime climate (21h00-07h30)
- `B0_clim_nuit_2026-01-11.yaml` — Nighttime climate (updated version)
- `C_gardien_eco.yaml` — Eco mode safety (delta T threshold)
- `D_notif_temp_jour.yaml` — Day temperature notifications
- `E_notif_temp_nuit.yaml` — Night temperature notifications
- `F_notif_fermeture_fenetres.yaml` — Window closure alerts
- `G_arret_clim_notif.yaml` — AC shutdown notifications
- `H_notif_mode_changement.yaml` — Mode change alerts (Heat/Cool/Fan)
- `I_debug_force_mode.yaml` — System watchdog & safety
- `J_synchro_notif_prise_coupee.yaml` — Outlet power sync notifications
- `L_debug_notif_message_clim.yaml` — Debug message logging

### 2. **P1_cuisine/** (2 automations)
Kitchen radiator heating management

- `A_chauffage_cuisine.yaml` — Weekday heating (Mon-Thu)
- `B_chauffage_cuisine_vacances.yaml` — Holiday heating

### 3. **P1_sdb/** (1 automation)
Bathroom equipment management

- `E_minuterie_seche_serviettes.yaml` — Heated towel timer (1h absolute safety)

### 4. **P2_prises/** (6 automations)
Smart outlet and equipment control

- `rodret_soufflant_sdb.yaml` — IKEA button control (bathroom heater)
- `rodret_tv_chambre.yaml` — IKEA button control (bedroom TV)
- `eco_prises.yaml` — Dynamic outlet management (presence-based)
- `gestion_tv_chambre.yaml` — Bedroom TV scene & standby detection
- `bureau_allumage_pc.yaml` — Office PC activation via wireless button
- `gestion_pc_bureau.yaml` — Office PC scene management

### 5. **P3_eclairage/** (1 automation)
Lighting control

- `allumage_lumiere_entree.yaml` — Entrance light control on arrival

### 6. **backup/** (4 automations)
GitHub backup automation system

- `git_au_demarrage.yaml` — Backup on HA startup
- `git_alerte_ko.yaml` — Failure alert (15min threshold)
- `git_hourly.yaml` — Hourly backup
- `git_weekly.yaml` — Weekly backup (Sunday 01:30)

### 7. **stores/** (2 automations)
Motorized blind/shutter management

- `gestion_store_bureau.yaml` — Office blind optimization
- `gestion_store_salon.yaml` — Living room blind with anti-glare mode

### 8. **meteo/** (5 automations)
Weather monitoring and alerts

- `update_prev_temperature.yaml` — Trend tracking (30min intervals)
- `update_prev_humidity.yaml` — Humidity trend tracking
- `alerte_meteo_cartes.yaml` — Weather alert map updates (Météo France)
- `notif_foudre.yaml` — Lightning strike notifications
- `maj_temps_foudre.yaml` — Lightning impact timestamp logging

### 9. **systeme/** (5 automations)
System monitoring and maintenance

- `z2m_last_seen.yaml` — Zigbee2MQTT device timeout detection
- `watchdog_piles.yaml` — Low battery warnings (Hue/IKEA/Sonoff)
- `economie_energie_vscode.yaml` — VS Code server power management
- `db_purge_mariadb.yaml` — Database cleanup (7-day retention) + repack
- `diag_enregistrement_journalier.yaml` — 15-min consumption logging (6 appliances + DUT)

### 10. **energie/** (1 automation)
Energy monitoring

- `surveillance_gros_electro_hp.yaml` — Peak-rate hour warnings (large appliances)

---

## Entity Replacements Applied

All 40 files have been corrected with the following replacements:

| Old Pattern | New Pattern | Occurrences |
|-------------|-------------|-------------|
| `sensor.poco_x7_pro_mamour_*` | `sensor.mamour_*` | 6 |
| `sensor.poco_x7_pro_eric_*` | `sensor.eric_*` | 6 |
| `sensor.poco_x7_pro_*` (generic) | `sensor.eric_*` | - |
| `device_tracker.poco_x7_pro_mamour` | `device_tracker.mamour` | 0* |
| `device_tracker.poco_x7_pro_eric` | `device_tracker.eric` | 0* |
| `notify.mobile_app_poco_x7_pro_eric` | `notify.mobile_app_eric` | 51 |
| `sensor.groupe_clim` | `sensor.groupe` | 13 |
| `sensor.presence_clim` | `sensor.presence` | 6 |

*Note: Device trackers not present in current automation set

**Verification:**
- No old patterns remaining: ✓
- All replacements applied: ✓

---

## YAML Format Specification

Each automation file follows this structure (as Home Assistant automation object, not list):

```yaml
id: '1766771160614'
alias: (A - 0) 2026-01-01 Automatisation CLIM (07h30 <-> 21h00)
description: '[VERSION FINALE] Pilotage des clims basé sur la présence et la saison...'
triggers:
  - alias: SYSTEM
    trigger: homeassistant
    ...
conditions:
  - alias: SÉCURITÉ
    condition: time
    ...
actions:
  - alias: ACTION
    action: ...
    ...
mode: queued
```

**Format Rules Enforced:**
- NO list marker (`-`) at root level ✓
- `id:` field first ✓
- `alias:` field second ✓
- All string values with special characters properly quoted ✓
- Proper YAML indentation ✓
- No ASCII box headers ✓

---

## Validation Results

### YAML Syntax Check
```
All 40 files: VALID ✓
- Proper YAML structure
- All required fields present (id, alias)
- No syntax errors
```

### Entity Replacement Verification
```
Old patterns (poco_x7_pro_*): 0 found ✓
New pattern counts:
  - sensor.mamour_*: 6 ✓
  - sensor.eric_*: 6 ✓
  - notify.mobile_app_eric: 51 ✓
  - sensor.groupe: 13 ✓
  - sensor.presence: 6 ✓
```

### File Organization
```
Folder structure:
  P1_clim_chauffage/ ......... 13 files
  P1_cuisine/ ............... 2 files
  P1_sdb/ ................... 1 file
  P2_prises/ ................ 6 files
  P3_eclairage/ ............. 1 file
  backup/ ................... 4 files
  stores/ ................... 2 files
  meteo/ .................... 5 files
  systeme/ .................. 5 files
  energie/ .................. 1 file
  
Total: 40 files ✓
```

---

## Special Handling Notes

### Files with Colons in Alias
The following files had aliases with colons (`:`) or brackets (`[`), which required YAML quoting:
- `gestion_tv_chambre.yaml` — Contains `:` (quoted)
- `bureau_allumage_pc.yaml` — Contains `:` (quoted)
- `gestion_pc_bureau.yaml` — Contains `:` (quoted)
- `git_alerte_ko.yaml` — Starts with `[` (quoted)
- `git_au_demarrage.yaml` — Starts with `[` (quoted)
- `git_hourly.yaml` — Starts with `[` (quoted)
- `git_weekly.yaml` — Starts with `[` (quoted)

All are now properly quoted in YAML format.

---

## Next Steps

1. **Review** each automation for your specific setup
2. **Adjust** entity names if your Home Assistant uses different naming
3. **Test** in development environment before production deployment
4. **Merge** into your `/config/automations.yaml` when ready
5. **Restart** Home Assistant to load the automations

---

## Reference

**Original Source Repository:**  
https://github.com/BerrySwann/home-assistant-config

**Migration Tool:**  
Python 3 YAML parser with custom replacements

**Generated:** 2026-04-04  
**Validated:** All 40 automations pass syntax check and entity verification
