<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--05--10-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📍 **Path dashboard** | `/dashboard-tablette/systeme-mini-pc` |
| 🔗 **Vignette** | L4C2 — `L4C2_VIGNETTE_MINI_PC.md` |
| 🃏 **Type layout** | `type: grid` + `type: vertical-stack` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-05-10 |
| 🏠 **Version HA** | 2025.2.x → 2.0 |

---

# 🖥️ PAGE L4C2 : MINI PC

---

## 🏗️ ARCHITECTURE GLOBALE

```
PAGE MINI PC (type: grid)
│
├── [HEADING] Mini - P.C. (icône phu:intel-nuc — retour /dashboard-tablette/0)
│
├── 🗃️ COL PRINCIPALE (vertical-stack — grid_columns: 12)
│   ├── BLOC 1  — Image /local/images/mini pc.png + IP locale / externe + Uptime
│   ├── BLOC 2  — Bar-cards : CPU USED + CPU Temp.
│   ├── BLOC 3  — Bar-cards : RAM % + USED MB + FREE MB
│   ├── BLOC 4  — Bar-card  : SSD SATA 512 Go
│   ├── BLOC 5  — Bar-cards : Download + Upload (via enp6s18)
│   ├── BLOC 6  — ring-tile + mini-graph : CPU Utilisation 24h → #speed
│   ├── BLOC 7  — Bar-card  : CPU SPEED (GHz) → #speed
│   ├── BLOC 8  — Bar-cards : Charges système 1m / 5m / 15m
│   ├── BLOC 9  — ring-tile + mini-graph : Température CPU 24h → #temp
│   ├── BLOC 10 — Bar-cards : Core 0 / Core 1 / Core 2 / Core 3
│   ├── BLOC 11 — Bar-card  : Température CPU (résumé compact) → #temp
│   ├── BLOC 12 — Bar-card  : Température Carte Mère → #temp
│   ├── BLOC 13 — ring-tile + mini-graph : Conso. W 24h → #conso
│   ├── BLOC 14 — Bar-card  : POWER (résumé compact) → #conso
│   ├── BLOC 15 — ring-tile + mini-graph : Mémoire utilisée → #memory
│   └── BLOC 16 — Bar-card  : MEMORY (résumé compact) → #conso
│
├── 🔵 POP-UP #speed   — ApexCharts CPU Utilisation 24h (area stepline + moy 24h + moy 730h)
├── 🌡️ POP-UP #temp    — ApexCharts Température CPU 24h (area + moy 24h + moy 730h)
├── ⚡ POP-UP #conso   — Streamline : conso temps réel + conso mensuelle (prise IKEA)
├── 💿 POP-UP #disk    — ApexCharts Espace disque utilisé 24h (brush 6h)
└── 💾 POP-UP #memory  — ApexCharts Mémoire utilisée 24h (brush 3h)
```

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### Bloc 1 — Infos système

| Entité | Type | Source | Rôle |
|:-------|:----:|:-------|:-----|
| `sensor.local_ip` | NAT | Intégration `local_ip` | IP locale affichée |
| `sensor.ip_externe` | NAT | Intégration `myip` / `ipify` | IP publique affichée |
| `sensor.system_monitor_dernier_demarrage` | NAT | `system_monitor` | Calcul Uptime (Jinja2) |

### Blocs 2–5 — Bar-cards hardware

| Entité | Type | Source | Rôle |
|:-------|:----:|:-------|:-----|
| `sensor.system_monitor_utilisation_du_processeur` | NAT | `system_monitor` | CPU USED % |
| `sensor.temperature_cpu_package` | TPL | `Mini-PC/MP_02` ← MQTT (`sensor.proxmox_cpu_package`) | CPU Temp. °C |
| `sensor.system_monitor_utilisation_de_la_memoire` | NAT | `system_monitor` | RAM % |
| `sensor.system_monitor_memoire_utilisee` | NAT | `system_monitor` | RAM USED MB |
| `sensor.system_monitor_memoire_libre` | NAT | `system_monitor` | RAM FREE MB |
| `sensor.system_monitor_utilisation_du_disque` | NAT | `system_monitor` | SSD % |
| `sensor.system_monitor_debit_du_reseau_entrant_via_enp6s18` | NAT | `system_monitor` | Download MB/s |
| `sensor.system_monitor_debit_du_reseau_sortant_via_enp6s18` | NAT | `system_monitor` | Upload MB/s |

> ⚠️ Interface réseau : **`enp6s18`** (VM KVM — Proxmox). Pas `enp1s0`.

### Blocs 6–8 — CPU détail

| Entité | Type | Source | Rôle |
|:-------|:----:|:-------|:-----|
| `sensor.system_monitor_utilisation_du_processeur` | NAT | `system_monitor` | ring-tile + mini-graph CPU |
| `sensor.cpu_speed` | NAT | `system_monitor` | Fréquence CPU GHz |
| `sensor.system_monitor_charge_1m` | NAT | `system_monitor` | Load average 1min |
| `sensor.system_monitor_charge_5m` | NAT | `system_monitor` | Load average 5min |
| `sensor.system_monitor_charge_15m` | NAT | `system_monitor` | Load average 15min |

### Blocs 9–12 — Températures

| Entité | Type | Source | Rôle |
|:-------|:----:|:-------|:-----|
| `sensor.temperature_cpu_package` | TPL | `Mini-PC/MP_02` ← MQTT `proxmox_cpu_package` | ring-tile + mini-graph + bar résumé |
| `sensor.temperature_core_0` | TPL | `Mini-PC/MP_02` ← MQTT `proxmox_core_0` | Température Core 0 |
| `sensor.temperature_core_1` | TPL | `Mini-PC/MP_02` ← MQTT `proxmox_core_1` | Température Core 1 |
| `sensor.temperature_core_2` | TPL | `Mini-PC/MP_02` ← MQTT `proxmox_core_2` | Température Core 2 |
| `sensor.temperature_core_3` | TPL | `Mini-PC/MP_02` ← MQTT `proxmox_core_3` | Température Core 3 |
| `sensor.temperature_carte_mere` | TPL | `Mini-PC/MP_02` ← MQTT `proxmox_carte_mere` | Température Carte Mère |

### Blocs 13–16 — Consommation & Mémoire

| Entité | Type | Source | Rôle |
|:-------|:----:|:-------|:-----|
| `sensor.prise_mini_pc_ikea_power` | NAT | Z2M (IKEA Inspelning) | Watts instantanés |
| `sensor.prise_mini_pc_ikea_current` | NAT | Z2M | Ampères (pop-up #conso) |
| `sensor.prise_mini_pc_ikea_energy` | NAT | Z2M | kWh cumulatif |
| `sensor.mini_pc_avg_watts_quotidien` | TPL | `P2_AVG/P2_AVG_AMHQ_mini_pc.yaml` | Moyenne W/jour |
| `sensor.mini_pc_avg_watts_mensuel` | TPL | `P2_AVG/P2_AVG_AMHQ_mini_pc.yaml` | Moyenne W/mois |
| `sensor.prise_mini_pc_ikea_quotidien_um` | UM | `P2_UM_AMHQ_mini_pc.yaml` | kWh quotidien |
| `sensor.prise_mini_pc_ikea_mensuel_um` | UM | `P2_UM_AMHQ_mini_pc.yaml` | kWh mensuel |
| `sensor.system_monitor_memoire_utilisee` | NAT | `system_monitor` | ring-tile + mini-graph + bar mémoire |
| `sensor.system_monitor_espace_utilise` | NAT | `system_monitor` | Pop-up #disk (MiB utilisés) |

---

## 🎨 SEUILS COULEUR — RÉCAPITULATIF

| Métrique | Vert | Orange | Rouge |
|:---------|:-----|:-------|:------|
| T° CPU (icon + bars) | < 65°C | 65–74°C | ≥ 75°C |
| CPU % (ring-tile) | < 70% | 70–79% | ≥ 80% |
| RAM % (bar) | < 75% | 75–79% | ≥ 80% |
| Power W (ring-tile) | < 14W | 14–18W | ≥ 19W |
| RAM USED MB (ring-tile) | < 8192 | 8192–12288 | ≥ 12289 |
| Cores (bar) | < 65°C | 65–74°C | ≥ 75°C |

---

## 🔵 POP-UPS — DÉTAIL

| Hash | Titre | Type | Entité(s) |
|:-----|:------|:-----|:----------|
| `#speed` | Utilisation du CPU | ApexCharts (area stepline + moy) | `sensor.system_monitor_utilisation_du_processeur` |
| `#temp` | Température du processeur | ApexCharts (area + moy) | `sensor.temperature_cpu_package` |
| `#conso` | Consommation Mini-PC | Streamline × 2 templates | `prise_mini_pc_ikea_*` + UM + AVG |
| `#disk` | Espace disque (SSD SATA) | ApexCharts brush 6h | `sensor.system_monitor_espace_utilise` |
| `#memory` | Mémoire utilisée | ApexCharts brush 3h | `sensor.system_monitor_memoire_utilisee` |

### Templates Streamline utilisés (pop-up #conso)

| Template | Variables clés |
|:---------|:---------------|
| `conso_temps_reel_appareil` | `energy_entity`, `current_entity`, `avg_daily_entity`, `conso_daily_kwh_entity` |
| `conso_mensuelle_mini_pc` | `energy_entity`, `avg_monthly_entity`, `conso_monthly_kwh_entity` |

---

## 📚 FICHIERS LIÉS

- Vignette : `Dashboard/L4C2_Mini_PC/vignette_L4C2_mini_pc_2026-05-10.yaml`
- Page : `Dashboard/L4C2_Mini_PC/page_L4C2_mini_pc_2026-05-10.yaml`
- Sensors T° : `templates/Mini-PC/MP_01_sonde_température_mini-pc.yaml`
- UM prise : `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml`
- AVG prise : `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml`

---

## 📝 HISTORIQUE

| Date | Changement |
|:-----|:-----------|
| 2026-03-25 | Création PAGE_MINI_PC.md (migration RPi4 → Mini PC Intel NUC) |
| 2026-05-03 | Mise à jour statut prod |
| 2026-05-10 | Refonte complète — entités vérifiées sur YAML prod + interface `enp6s18` confirmée |

---

<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L4C2_VIGNETTE_MINI_PC]]  [[L4C3_VIGNETTE_MAJ]]*
