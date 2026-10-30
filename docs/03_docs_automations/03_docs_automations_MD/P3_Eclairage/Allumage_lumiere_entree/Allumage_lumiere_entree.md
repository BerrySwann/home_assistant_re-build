# ALLUMAGE LUMIÈRE ENTRÉE

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P3_Eclairage/p3_entree_allumage_lumiere/p3_entree_allumage_lumiere.yaml`
> **Mode HA :** `queued`

---

## 📝 Description

Allume la lumière de l'entrée lors d'une arrivée. Gère deux cas :
1. Arrivée initiale (G1 → G2/G3/G4) en période diurne (soleil levé)
2. Retour de Mamour quand Eric est déjà là (G3 → G4)

---

## ⚡ Déclencheurs

| Type | Entité |
|:---|:---|
| `state` | `sensor.groupe` |

---

## ⚙️ Actions - Choose

**CAS 1 - Arrivée initiale diurne :**
- Condition : `from == groupe_1` ET `to in [groupe_2, groupe_3, groupe_4]`
- Condition : `sun.sun == above_horizon`
- Action : `light.turn_on → light.entree`

**CAS 2 - Retour Mamour (G3→G4) :**
- Condition : `from == groupe_3` ET `to == groupe_4`
- Action : `light.turn_on → light.entree`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.groupe` | Déclencheur + logique de transition |
| `sun.sun` | Condition lever/coucher soleil |
| `light.entree` | Lumière entrée (Hue White) |
