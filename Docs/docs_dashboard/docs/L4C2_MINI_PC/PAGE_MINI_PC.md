<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--06--13-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Fichier YAML** | `Dashboard/L4C2_11_Mini_PC/page_L4C2_mini_pc_2026-06-18.yaml` |
| 🔗 **Accès depuis** | Tap sur vignette L4C2 → `/dashboard-tablette/systeme-mini-pc` |
| 🏗️ **Layout** | `grid` → `vertical-stack` — sections bar-card + ring-tile + mini-graph + 5 pop-ups |
| 📅 **Modifié le** | 2026-06-10 |
| 🏠 **Version HA** | 2025.2+ |

---

# 🖥️ PAGE MINI-PC — SUPERVISION COMPLÈTE

---

## 🎯 VUE D'ENSEMBLE

Page de supervision matérielle du Mini-PC Intel NUC (hôte Proxmox). Affiche photo du NUC, IPs, uptime, puis des sections CPU/RAM/Disk/Réseau/Températures/Conso avec jauges bar-card, ring-tiles et graphes mini-graph 24h. 5 pop-ups bubble-card pour les graphes détaillés apexcharts.

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `bar-card` | Jauges CPU%, RAM GiB, Disk GiB, Network, T°, Speed, Load, Power |
| `ring-tile-card` | Indicateurs circulaires CPU / T° / Conso / RAM / Disk |
| `mini-graph-card` | Graphes 24h CPU / T° / Conso / RAM / Disk |
| `mushroom-template-card` | Affichage IPs + Uptime |
| `stack-in-card` | Groupement vertical/horizontal sans bordure |
| `bubble-card` | 5 pop-ups graphes détaillés (hash: speed/temp/conso/memory/disk) |
| `apexcharts-card` | Graphes détaillés dans les pop-ups (24h + brush) |
| `streamline-card` | Conso temps réel + mensuel pop-up #conso |

---

## 🏗️ ARCHITECTURE GÉNÉRALE

```
┌────────────────────────────────────────┐
│  🏷️ Mini - P.C.  (heading)             │
│  vertical-stack                         │
│  ├── Photo NUC (/local/images/mini pc.png)
│  ├── IP Int. / Ext. (mushroom × 3)    │
│  ├── Uptime (mushroom × 2)            │ ⚠️ BUG (voir ci-dessous)
│  ├── CPU % + CPU Temp (bar-card × 2) │
│  ├── RAM % + Used MB + Free MB (bar×3)│
│  ├── Disk PVE GiB (bar-card)         │
│  ├── Network DL/UL (bar-card × 2)    │
│  ├── [ring-tile CPU] [mini-graph CPU 24h]│
│  ├── CPU Speed (bar-card)            │
│  ├── Load 1m/5m/15m (bar-card × 3)  │
│  ├── [ring-tile T°] [mini-graph T° 24h]│
│  ├── Core 0/1/2/3 T° (bar-card × 4) │
│  ├── Température CPU (bar-card)      │
│  ├── Température Carte Mère (bar-card)│
│  ├── [ring-tile Conso] [mini-graph W 24h]│
│  ├── Power bar-card                  │
│  ├── [ring-tile RAM MB] [mini-graph RAM 24h]│
│  ├── Memory bar-card                 │
│  ├── [ring-tile Disk GiB] [mini-graph Disk 24h]│
│  └── Disk bar-card                   │
├── bubble-card #speed  (apexcharts CPU 24h)
├── bubble-card #temp   (apexcharts T° 24h)
├── bubble-card #conso  (streamline Conso)
├── bubble-card #memory (apexcharts RAM 24h)
└── bubble-card #disk   (apexcharts Disk 24h)
```

---

## ⚠️ BUG CONNU — UPTIME (À CORRIGER)

La carte Uptime utilise un template Jinja2 qui traite `sensor.pve_uptime` comme des **secondes** :
```yaml
{% set uptime = states('sensor.pve_uptime') | int(0) %}
{% set jours = (uptime / 86400) | int(0) %}
```
Or `sensor.pve_uptime` retourne des **heures flottantes** (confirmé lors du fix L4C1).  
→ Résultat : uptime affiche ~0j 0h au lieu de la vraie valeur.

**Correction à appliquer :**
```yaml
{% set uptime = states('sensor.pve_uptime') | float(0) %}
{% set jours = (uptime / 24) | int(0) %}
{% set heures = (uptime % 24) | int(0) %}
{% set minutes = ((uptime % 1) * 60) | int(0) %}
```

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### Image & Réseau
| Entité | Source | Rôle |
|--------|--------|------|
| `/local/images/mini pc.png` | Fichier local HA | Photo du NUC |
| `sensor.local_ip` | Intégration System Monitor | IP interne |
| `sensor.ip_externe` | Template/intégration | IP externe WAN |

### Uptime
| Entité | Source | Note |
|--------|--------|------|
| `sensor.pve_uptime` | Intégration `proxmox_ve` | ⚠️ retourne heures — template bugué (traite comme secondes) |

### CPU
| Entité | Source | Seuils bar-card |
|--------|--------|-----------------|
| `sensor.pve_utilisation_du_processeur` | `proxmox_ve` | <75% bleu · 75-90 orange · >90 rouge (max 100) |
| `sensor.cpu_speed` | System Monitor | <2.9 GHz vert · 3-3.3 orange · >3.4 rouge (max 4 GHz) |
| `sensor.system_monitor_charge_1m` | System Monitor | <2 vert · 2-3 orange · >3 rouge |
| `sensor.system_monitor_charge_5m` | System Monitor | idem |
| `sensor.system_monitor_charge_15m` | System Monitor | idem |

### Températures
| Entité | Source | Seuils |
|--------|--------|--------|
| `sensor.proxmox_cpu_package` | `proxmox_ve` | <65°C vert · 65-74 orange · >75 rouge (max 100) |
| `sensor.proxmox_carte_mere` | `proxmox_ve` | idem |
| `sensor.proxmox_core_0` | `proxmox_ve` | idem |
| `sensor.proxmox_core_1` | `proxmox_ve` | idem |
| `sensor.proxmox_core_2` | `proxmox_ve` | idem |
| `sensor.proxmox_core_3` | `proxmox_ve` | idem |

### RAM
| Entité | Source | Seuils / Max |
|--------|--------|--------------|
| `sensor.pve_memory_usage_percentage` | `proxmox_ve` | <75% vert · 75-79 orange · >80 rouge (max 100%) |
| `sensor.system_monitor_memoire_utilisee` | System Monitor | max 16384 MB · target 7500 |
| `sensor.system_monitor_memoire_libre` | System Monitor | max 16384 MB · target 7500 |

### Disk
| Entité | Source | Seuils |
|--------|--------|--------|
| `sensor.pve_utilisation_du_disque` | `proxmox_ve` | <358 GiB vert · 358-404 orange · >405 rouge (max 477 GiB) |

### Réseau
| Entité | Source | Max |
|--------|--------|-----|
| `sensor.system_monitor_debit_du_reseau_entrant_via_enp6s18` | System Monitor | 130 MiB/s |
| `sensor.system_monitor_debit_du_reseau_sortant_via_enp6s18` | System Monitor | 130 MiB/s |

### Consommation électrique
| Entité | Source | Seuils |
|--------|--------|--------|
| `sensor.prise_mini_pc_ikea_power` | Z2M prise IKEA | <14W vert · 14-18 orange · >19 rouge (max 25W) |
| `sensor.prise_mini_pc_ikea_current` | Z2M prise IKEA | Pop-up #conso |
| `sensor.mini_pc_avg_watts_quotidien` | Template AVG P2 | Pop-up #conso |
| `sensor.prise_mini_pc_ikea_quotidien_um` | Utility Meter P2 | Pop-up #conso |
| `sensor.prise_mini_pc_ikea_energy` | Z2M prise IKEA | Pop-up #conso |
| `sensor.mini_pc_avg_watts_mensuel` | Template AVG P2 | Pop-up #conso |
| `sensor.prise_mini_pc_ikea_mensuel_um` | Utility Meter P2 | Pop-up #conso |

---

## 🫧 POP-UPS BUBBLE-CARD

| Hash | Titre | Contenu |
|------|-------|---------|
| `#speed` | Utilisation du CPU | apexcharts 24h — `pve_utilisation_du_processeur` × 4 series (instant ×2, moy. 24h, moy. mois) |
| `#temp` | Températures processeur | apexcharts 24h — `proxmox_cpu_package` + `proxmox_carte_mere` (color_threshold) |
| `#conso` | Consommation Mini-PC | streamline-card temps réel + mensuel — `prise_mini_pc_ikea_power` |
| `#memory` | Mémoire RAM | apexcharts 24h — `pve_memory_usage_percentage` × 3 series |
| `#disk` | Espace disque — PVE VM | apexcharts 24h + brush — `pve_utilisation_du_disque` (max 477 GiB) |

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `proxmox_ve` | Intégration HA | ✅ Essentiel |
| System Monitor | Intégration HA | ✅ Essentiel |
| Z2M — prise IKEA Mini-PC | Zigbee2MQTT | ✅ Essentiel |
| `bar-card` | HACS | ✅ Essentiel |
| `ring-tile-card` | HACS | ✅ Essentiel |
| `mini-graph-card` | HACS | ✅ Essentiel |
| `mushroom-template-card` | HACS | ✅ Essentiel |
| `stack-in-card` | HACS | ✅ Essentiel |
| `bubble-card` | HACS | ✅ Essentiel |
| `apexcharts-card` | HACS | ✅ Essentiel |
| `streamline-card` | HACS | ✅ Essentiel |
| `card-mod` | HACS | ✅ Essentiel |
| `/local/images/mini pc.png` | Fichier local HA | ✅ Essentiel |
| `phu:intel-nuc` | Icon pack | ✅ Vignette uniquement |

---

## 🔗 FICHIERS LIÉS

- `Dashboard/L4C2_11_Mini_PC/page_L4C2_mini_pc_2026-06-18.yaml`
- `docs/L4C2_MINI_PC/L4C2_VIGNETTE_MINI_PC.md`
- `docs/DEPENDANCES_GLOBALES.md`

---

← Retour : `L4C2_VIGNETTE_MINI_PC.md` | → Suivant : `docs/L4C3_MAJ_HA/`
