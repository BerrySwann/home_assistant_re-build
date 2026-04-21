# (I) WATCHDOG CLIM — FORCE MODE CORRECT & SÉCURITÉ

> **Fichier :** `automations_corrige/P1_clim_chauffage/I_debug_force_mode.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Watchdog en 2 couches :
1. **FORCE OFF** si une clim est allumée alors que sa prise est coupée OU qu'un arrêt sécurisé est en cours.
2. **FORCE MODE SAISON** si une clim est dans le mauvais mode (ex: cool au lieu de heat).

Déclenché par tout changement d'état des clims ou du mode saison.

---

## ⚡ Déclencheurs

| Type | Entité |
|:---|:---|
| `state` (to: null) | `climate.clim_salon/bureau/chambre_rm4_mini` |
| `state` (to: null) | `sensor.mode_ete_hiver` |

---

## ⚙️ Actions

1. Pause 2s
2. Calcul `force_off_list` (clims à éteindre de force)
3. Calcul `force_mode_list` (clims à corriger)
4. Si `force_off_list` non vide → notification + `set_hvac_mode: off`
5. Si `force_mode_list` non vide → notification + `set_hvac_mode: mode_saison`

---

## 🔌 DÉPENDANCES

### Entités lues

| Entité | Rôle |
|:---|:---|
| `sensor.mode_ete_hiver` | Mode saison de référence |
| `climate.clim_*_rm4_mini` ×3 | État courant |
| `switch.clim_*_nous` ×3 | Prise active ? |
| `input_boolean.clim_*_arret_securise_en_cours` ×3 | Arrêt sécurisé actif ? |

### Entités pilotées

| Entité | Action |
|:---|:---|
| `climate.clim_*_rm4_mini` (liste dynamique) | `set_hvac_mode: off` ou mode saison |

### Notifications

| Titre | Condition |
|:---|:---|
| `⛔ SÉCURITÉ CLIM` | Force OFF |
| `🔧 CORRECTION MODE` | Force mode saison |
