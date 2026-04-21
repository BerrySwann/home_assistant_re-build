# (B-0) AUTOMATISATION CLIM NUIT (21H00 ↔ 07H30)

> **Fichier corrigé :** `automations_corrige/P1_clim_chauffage/B0_clim_nuit_2026-01-11.yaml`
> **Fichier obsolète :** `B0_clim_nuit_2026-01-02.yaml` → ❌ À SUPPRIMER DE LA PROD
> **Mode HA :** `queued`

---

## 📝 Description

Miroir nocturne de l'automation A0. Pilote les 3 clims entre 21h00 et 07h30.
Même structure (boucle capteurs, sécurité fenêtres, parallèle), mais températures
cibles simplifiées : une seule `temp_nuit` pour les 3 pièces quand quelqu'un est présent.

---

## ⚡ Déclencheurs

| ID trigger | Type | Entité / Horaire |
|:---|:---|:---|
| `ha_restart` | `homeassistant` | Démarrage HA |
| `force_run` | `time` | 21:00:00 |
| `force_run` | `state` | `sensor.mamour_network_type`, `sensor.eric_network_type` |
| `force_run` | `state` | 3 prises clim NOUS |
| `window_open` | `state` | 4 capteurs fenêtres → `off` → `on` |
| `window_close` | `state` | 4 capteurs fenêtres → `on` → `off` |
| `sensor_update` | `state` | `sensor.th_balcon_nord_temperature`, `sensor.temperature_cible`, `sensor.mode_ete_hiver`, `sensor.temperature_confort_nuit` |

---

## 🔒 Conditions globales

- Plage horaire stricte : `after 21:00 before 07:30`

---

## ⚙️ Actions résumées

1. Délai sécurité si `ha_restart` (1 min)
2. Boucle capteurs (max 10 × 30s)
3. Variables : `mode_saison`, `groupe_presence`, `fenetres_ouvertes`, `temp_eco_c`, `temp_cible`, `temp_nuit` — cible uniforme pour les 3 pièces
4. CAS URGENCE fenêtre → OFF toutes clims + notif ciblée + stop
5. Cas standard → parallel Salon / Bureau / Chambre
6. Notification résumé nuit

---

## 🔌 DÉPENDANCES

### Entités lues

| Entité | Rôle |
|:---|:---|
| `sensor.temperature_confort_nuit` | T° confort nuit (unique pour les 3 pièces) |
| `sensor.mode_ete_hiver` | Mode saison |
| `sensor.groupe` | Groupe présence |
| `sensor.temperature_eco_hiver_corrige` | T° éco |
| `sensor.temperature_cible` | T° cible |
| `sensor.th_balcon_nord_temperature` | T° extérieure |
| `sensor.mamour_network_type` / `sensor.eric_network_type` | Présence réseau |
| 4× `binary_sensor.contact_fenetre_*` | Sécurité fenêtres |
| 3× `switch.clim_*_nous` | Sécurité prises |
| 3× `input_boolean.clim_*_arret_securise_en_cours` | Flags sécurité |

### Entités pilotées

| Entité | Action |
|:---|:---|
| `climate.clim_salon_rm4_mini` | `set_temperature` |
| `climate.clim_bureau_rm4_mini` | `set_temperature` |
| `climate.clim_chambre_rm4_mini` | `set_temperature` |

### Notifications

| Titre | Condition |
|:---|:---|
| `[AN] ATTENTE CAPTEURS` | Boucle relance |
| `[AN] CLIM NUIT COUPÉE` | Fenêtre ouverte |
| `[AN] presence` | Résumé températures |

---

## ⚠️ Points d'attention

- Contrairement à A0 (jour), la nuit utilise **une seule** `temp_nuit` pour Salon + Bureau + Chambre.
- La version `2026-01-02` est obsolète.
