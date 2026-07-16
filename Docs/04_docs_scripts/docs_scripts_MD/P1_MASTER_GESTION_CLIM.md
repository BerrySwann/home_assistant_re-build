# P1_MASTER_GESTION_CLIM — Script centralisé climatisation

> **Script HA :** `script.p1_master_gestion_clim`
> **Fichier TREE_CORRIGE :** `docs_scripts/TREE_CORRIGE/p1_master_gestion_clim.yaml`
> **Mode :** `queued` — max: 10
> **Appelé par :** Automation A0 (JOUR) + Automation B0 (NUIT)
> **Créé par :** Refactoring LLM local — 2026-06

---

## 📝 Description

Script maître qui centralise **toute** la logique de pilotage des 3 clims.
Remplace le code inline qui était dupliqué dans les automations A0 et B0.
Prend un paramètre `periode` (`"jour"` ou `"nuit"`) et adapte les cibles en conséquence.

---

## 📥 Paramètres d'entrée (fields)

| Paramètre | Requis | Valeurs | Description |
|:---|:---|:---|:---|
| `periode` | ✅ | `"jour"` / `"nuit"` | Détermine les cibles de température et le préfixe notif |
| `trigger_id` | ❌ | string | ID du trigger HA (ex: `"ha_restart"`, `"sensor_update"`) |
| `trigger_entity_id` | ❌ | string | Entity ID déclencheur (pour message fenêtre ciblé) |

---

## 🔢 Séquence (6 étapes)

### 1. Préfixe notification
- `[AJ]` si `periode == 'jour'`, `[AN]` si `nuit`

### 2. Délai sécurité redémarrage
- Si `trigger_id == 'ha_restart'` → attente 1 minute

### 3. Boucle attente capteurs (max 10 × 30s)
- Vérifie : `mode_ete_hiver`, `groupe`, `temperature_eco_hiver_corrige`, `temperature_eco_ete_corrige`, `temperature_corrige_mamour/eric`
- + selon `periode` :
  - JOUR : `temperature_cible`, `temperature_corrige_chambre`
  - NUIT : `temperature_confort_nuit`, `temperature_corrige_chambre`
- Si KO après 10 essais : notif `[AJ/AN] ATTENTE CAPTEURS`

### 4. Calcul variables globales
| Variable | Source |
|:---|:---|
| `mode_saison` | `sensor.mode_ete_hiver` → heat/cool/off |
| `groupe_presence` | `sensor.groupe` |
| `fenetres_ouvertes` | expand 4× `binary_sensor.contact_fenetre_*` |
| `temp_eco_hc` | `sensor.temperature_eco_hiver_corrige` |
| `temp_eco_ec` | `sensor.temperature_eco_ete_corrige` |
| `temp_cible` | `sensor.temperature_cible` |
| `temp_nuit` | `sensor.temperature_confort_nuit` |
| `temp_conf_m` | `sensor.temperature_corrige_mamour` |
| `temp_conf_e` | `sensor.temperature_corrige_eric` |
| `temp_conf_c` | `sensor.temperature_corrige_chambre` |

### 5. Calcul cibles par pièce

#### SALON
| Groupe | Période | Cible |
|:---|:---|:---|
| `groupe_1` (absent) | — | eco (hc ou ec selon saison) |
| `groupe_2` (Mamour) | JOUR | `temp_conf_m` |
| `groupe_3` (Eric) | JOUR | `temp_conf_e` |
| `groupe_4` (Tous) | JOUR | `temp_conf_m` |
| tout | NUIT | `temp_nuit` |

#### BUREAU
| Groupe | Période | Cible |
|:---|:---|:---|
| `groupe_1` (absent) | — | eco |
| `groupe_2` (Mamour) | JOUR | eco |
| `groupe_3` (Eric) | JOUR | `temp_conf_e` |
| `groupe_4` (Tous) | JOUR | `temp_conf_e` |
| tout | NUIT | `temp_nuit` |

#### CHAMBRE
| Groupe | Période | Cible |
|:---|:---|:---|
| `groupe_1` (absent) | — | eco |
| tout autre | JOUR | `temp_conf_c` |
| tout | NUIT | `temp_nuit` |

### 6. Exécution

**CAS URGENCE — fenêtre ouverte :**
- `climate.set_hvac_mode → off` sur les 3 clims
- Notif ciblée sur la fenêtre déclenchante
- `stop`

**Cas standard (parallel) :**
- SALON : si `switch.clim_salon_nous ON` et `input_boolean.clim_salon_arret_securise_en_cours OFF` → `climate.set_temperature`
- BUREAU : idem avec clim bureau
- CHAMBRE : idem avec clim chambre
- `sensor_update` + clim déjà en `off` → on ne la redémarre pas (protection intentionnelle)
- Délai 2s
- Notif résumé `[AJ/AN] presence — Mode / Températures`

---

## 🔌 ENTITÉS UTILISÉES

### Lues
| Entité | Rôle |
|:---|:---|
| `sensor.mode_ete_hiver` | Mode saison |
| `sensor.groupe` | Présence groupe |
| `sensor.temperature_eco_hiver_corrige` | T° éco hiver |
| `sensor.temperature_eco_ete_corrige` | T° éco été |
| `sensor.temperature_eco_hiver` | Fallback éco hiver |
| `sensor.temperature_eco_ete` | Fallback éco été |
| `sensor.temperature_cible` | T° cible jour |
| `sensor.temperature_confort_nuit` | T° cible nuit |
| `sensor.consigne_de_base` | Fallback général |
| `sensor.temperature_corrige_mamour` | T° confort Mamour |
| `sensor.temperature_corrige_eric` | T° confort Eric |
| `sensor.temperature_corrige_chambre` | T° confort chambre |
| `sensor.presence` | Texte présence (notif) |
| `sensor.nombre_de_fenetres_ouvertes` | Compteur fenêtres |
| 4× `binary_sensor.contact_fenetre_*_contact` | Sécurité fenêtres |
| 3× `switch.clim_*_nous` | Sécurité alimentation |
| 3× `input_boolean.clim_*_arret_securise_en_cours` | Flags arrêt sécurisé |

### Pilotées
| Entité | Action |
|:---|:---|
| `climate.clim_salon_rm4_mini` | `set_temperature` (hvac_mode + temperature) |
| `climate.clim_bureau_rm4_mini` | `set_temperature` |
| `climate.clim_chambre_rm4_mini` | `set_temperature` (target_temp_low/high — NodOn Z2M) |
| `climate.clim_salon_rm4_mini` / `clim_bureau_rm4_mini` / `clim_chambre_rm4_mini` | `set_hvac_mode: off` (urgence fenêtre) |

### Notifications
| Service | Titre | Déclenchement |
|:---|:---|:---|
| `notify.mobile_app_eric` | `[AJ/AN] ATTENTE CAPTEURS` | Boucle relance si KO |
| `notify.mobile_app_eric` | `[AJ/AN] CLIM JOUR/NUIT COUPÉE` | Fenêtre ouverte |
| `notify.mobile_app_eric` | `[AJ/AN] presence` | Résumé après commandes |

---

## ⚠️ Points d'attention

- **SALON groupe_3 JOUR** : Eric seul → `temp_conf_e` (même comportement que l'ancienne version inline).
- `sensor_update` ne redémarre pas une clim déjà en `off` (protection intentionnelle via `trigger_id`).
- Script `mode: queued, max: 10` — les déclenchements simultanés sont mis en file.
- Les températures eco ont un fallb