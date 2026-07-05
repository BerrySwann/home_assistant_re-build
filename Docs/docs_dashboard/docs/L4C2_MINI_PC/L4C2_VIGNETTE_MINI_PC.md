<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--06--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Fichier YAML** | `Dashboard/L4C2_11_Mini_PC/vignette_L4C2_mini_pc_2026-06-18.yaml` |
| 🔗 **Accès depuis** | L4C2 — Matrice dashboard principal (ligne 4, colonne 2) |
| 🏗️ **Type** | `custom:button-card` — grille custom 3×2 |
| 📅 **Modifié le** | 2026-06-21 |
| 🏠 **Version HA** | 2025.2+ |

---

# 🖥️ L4C2 — VIGNETTE MINI-PC

---

## 🎯 VUE D'ENSEMBLE

Vignette de supervision compacte du Mini-PC Intel NUC (hôte Proxmox). Affiche la T° CPU package (couleur icône), CPU%, consommation électrique W, RAM% et Storage%. Tap → page détail Mini-PC.

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `button-card` | Carte principale — grille + custom_fields |

---

## 🏗️ ARCHITECTURE

```
╔════════════════════════════════════╗
║  [icône Intel NUC]  [T° pkg °C]  ║
║  _____ Mini - P.C. _____         ║
║  🖥 CPU: XX.X%                   ║
║  ⚡ Power: XX.XW                 ║
║  💾 RAM: XX.X%                   ║
║  💽 SSD: XX.X%                   ║
╚════════════════════════════════════╝
```

**Grille CSS :** `"i temp" / "n n" / "cpu cpu" / "conso conso" / "ram ram" / "sd sd"`

### Couleurs dynamiques

| Champ | Entité | Seuils | Icône dynamique |
|-------|--------|--------|:---------------:|
| Icône + T° | `sensor.proxmox_cpu_package` | <65°C vert · 65-75 orange · >75 rouge | ✅ (direct) |
| CPU | `sensor.pve_utilisation_du_processeur` | <75% blanc · 75-90 orange · >90 rouge | ✅ `--icon-color-sensor` |
| Power | `sensor.prise_mini_pc_ikea_power` | <15W blanc · 15-19 orange · >19 rouge | ❌ hardcodé vert |
| RAM | `sensor.pve_memory_usage_percentage` | <75% blanc · 75-90 orange · >90 rouge | ✅ `--icon-color-sensor` |
| SSD | `sensor.storage_local_storage_usage_percentage` | <75% blanc · 75-90 orange · >90 rouge | ✅ `--icon-color-sensor` |

> 🔧 **Correction 2026-06-21** : RAM et SSD utilisaient `color:rgb(70,175,75)` hardcodé → remplacé par `var(--icon-color-sensor)` avec variable CSS définie dans `card_mod.styles`. L'icône change maintenant de couleur selon le % (identique à L4C1 Proxmox).

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

| Entité | Source | Rôle |
|--------|--------|------|
| `sensor.proxmox_cpu_package` | Intégration `proxmox_ve` | T° CPU package — icône + champ temp |
| `sensor.pve_utilisation_du_processeur` | Intégration `proxmox_ve` | CPU % nœud PVE |
| `sensor.pve_memory_usage_percentage` | Intégration `proxmox_ve` | RAM % nœud PVE |
| `sensor.storage_local_storage_usage_percentage` | Intégration `proxmox_ve` | Storage local % |
| `sensor.prise_mini_pc_ikea_power` | Z2M — prise IKEA | Consommation W temps réel |

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `proxmox_ve` | Intégration HA | ✅ Essentiel |
| Z2M — prise IKEA Mini-PC | Zigbee2MQTT | ✅ Essentiel |
| `button-card` | HACS | ✅ Essentiel |
| `phu:intel-nuc` | Icon pack (phu) | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

- `Dashboard/L4C2_11_Mini_PC/vignette_L4C2_mini_pc_2026-06-18.yaml`
- `docs/L4C2_MINI_PC/PAGE_MINI_PC.md`
- `docs/DEPENDANCES_GLOBALES.md`

---

← Retour : `L4C1_PROXMOX` | → Suivant : `PAGE_MINI_PC`
