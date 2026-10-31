<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--06--13-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-4fc3f7?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Fichier YAML** | `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C2_PROXMOX/01_vignette/vignette_L4C2_proxmox.yaml` |
| 🔗 **Accès depuis** | L4C2 - Matrice dashboard principal (ligne 4, colonne 2) |
| 🏗️ **Type** | `custom:button-card` - grille custom 4×2 |
| 📅 **Modifié le** | 2026-06-09 |
| 🏠 **Version HA** | 2025.2+ |

---

# 🖥️ L4C2 - VIGNETTE PROXMOX

---

## 🎯 VUE D'ENSEMBLE

Vignette de supervision compacte du nœud Proxmox VE. Affiche la T° CPU package (couleur icône), le statut online/offline, et les métriques CPU/RAM/Storage en lignes colorées. Tap → page détail Proxmox.

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `button-card` | Carte principale - grille + custom_fields |

> ⚠️ **bar-card supprimée** - remplacée par lignes inline dans `custom_fields`

---

## 🏗️ ARCHITECTURE

```
╔════════════════════════════════╗
║  [icône PVE]    [T° pkg °C]   ║
║  _____ Proxmox _____          ║
║  🖥 PVE CPU: XX.X%            ║
║  ⚡ PVE Host: ONLINE          ║
║  💾 PVE RAM: XX.X%            ║
║  💽 PVE Storage: XX.X%        ║
╚════════════════════════════════╝
```

**Grille CSS :** `"i temp" / "n n" / "cpu cpu" / "status status" / "ram ram" / "sd sd"`

### Couleurs dynamiques

| Champ | Entité | Seuils |
|-------|--------|--------|
| Icône + T° | `sensor.proxmox_cpu_package` | <65°C vert · 65-75 orange · >75 rouge |
| CPU | `sensor.pve_utilisation_du_processeur` | <75% blanc · 75-90 orange · >90 rouge |
| Statut | `binary_sensor.pve_status` | on=ONLINE vert · off=OFFLINE rouge |
| RAM | `sensor.pve_memory_usage_percentage` | <75% blanc · 75-90 orange · >90 rouge |
| Storage | `sensor.storage_local_storage_usage_percentage` | <75% blanc · 75-90 orange · >90 rouge |

---

## 📊 ENTITÉS UTILISÉES - PROVENANCE COMPLÈTE

| Entité | Source | Rôle |
|--------|--------|------|
| `sensor.proxmox_cpu_package` | Intégration `proxmox_ve` | T° CPU package - couleur icône + champ temp |
| `sensor.pve_utilisation_du_processeur` | Intégration `proxmox_ve` | CPU % nœud PVE |
| `sensor.pve_memory_usage_percentage` | Intégration `proxmox_ve` | RAM % nœud PVE |
| `sensor.storage_local_storage_usage_percentage` | Intégration `proxmox_ve` | Storage local % |
| `binary_sensor.pve_status` | Intégration `proxmox_ve` | Statut nœud PVE (on=ONLINE) |

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `proxmox_ve` | Intégration HA | ✅ Essentiel |
| `button-card` | HACS | ✅ Essentiel |
| `phu:proxmox` | Icon pack (phu) | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

- `docs/02_docs_dashboard/02_dashboard_docs_YAML/L4C2_PROXMOX/01_vignette/vignette_L4C2_proxmox.yaml`
- `docs/L4C2_PROXMOX/PAGE_PROXMOX.md`
- `docs/00_IA/00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.md`

---

← Retour : `L1C3_CLIM` | → Suivant : `PAGE_PROXMOX`
