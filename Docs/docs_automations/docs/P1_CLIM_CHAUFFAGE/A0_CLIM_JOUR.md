# (A-0) AUTOMATISATION CLIM JOUR (07H30 ↔ 21H00)

> **Fichier corrigé :** `automations_corrige/P1_clim_chauffage/A0_clim_jour_2026-01-11.yaml`
> **Fichier obsolète :** `A0_clim_jour_2026-01-01.yaml` → ❌ À SUPPRIMER DE LA PROD
> **Mode HA :** `queued`

---

## 📝 Description

Automation principale de pilotage des 3 clims sur la plage diurne 07h30–21h00.
Gère 5 types de déclencheurs, boucle de relance au démarrage (10 essais × 30s),
coupure d'urgence sur ouverture de fenêtre, et envoi en parallèle des commandes
vers Salon / Bureau / Chambre avec les températures cibles calculées par groupe.

---

## ⚡ Déclencheurs

| ID trigger | Type | Entité / Horaire |
|:---|:---|:---|
| `ha_restart` | `homeassistant` | Démarrage HA |
| `force_run` | `time` | 07:30:00 |
| `force_run` | `state` | `sensor.mamour_network_type`, `sensor.eric_network_type` |
| `force_run` | `state` | `switch.clim_salon_nous`, `switch.clim_bureau_nous`, `switch.clim_chambre_nous` |
| `window_open` | `state` | 4 capteurs fenêtres → `off` → `on` |
| `window_close` | `state` | 4 capteurs fenêtres → `on` → `off` |
| `sensor_update` | `state` | `sensor.th_balcon_nord_temperature`, `sensor.temperature_cible`, `sensor.mode_ete_hiver`, `sensor.temperature_confort_jour` |

---

## 🔒 Conditions globales

- Plage horaire stricte : `after 07:30 before 21:00`

---

## ⚙️ Actions résumées

1. **Délai sécurité** : si `ha_restart` → attente 1 min
2. **Boucle capteurs** : max 10 tentatives × 30s — vérifie `mode_ete_hiver`, `sensor.groupe`, `temperature_cible`, 3 températures corrigées
3. **Calcul variables** : `mode_saison`, `groupe_presence`, `fenetres_ouvertes`, `temp_eco_c`, `temp_cible`, `temp_conf_m/e/c`, `t_salon/bureau/chambre_target`
4. **CAS URGENCE fenêtre ouverte** : `climate.set_hvac_mode → off` sur les 3 clims + notification ciblée + `stop`
5. **Cas standard** : envoi en `parallel` des températures cibles aux 3 clims (si prise ON et pas d'arrêt sécurisé en cours)
6. **Notification résumé** : `[AJ] presence — Mode / Températures`

---

## 🔌 DÉPENDANCES

### Entités lues (triggers / conditions / templates)

| Entité | Domaine | Rôle |
|:---|:---|:---|
| `sensor.mamour_network_type` | sensor | Détection présence Mamour |
| `sensor.eric_network_type` | sensor | Détection présence Eric |
| `sensor.th_balcon_nord_temperature` | sensor | T° extérieure |
| `sensor.temperature_cible` | sensor | T° cible calculée |
| `sensor.mode_ete_hiver` | sensor | Mode saison (heat/cool/fan_only) |
| `sensor.temperature_confort_jour` | sensor | T° confort jour |
| `sensor.temperature_eco_hiver_corrige` | sensor | T° éco hiver |
| `sensor.temperature_corrige_mamour_hivers` | sensor | T° confort Mamour |
| `sensor.temperature_corrige_eric_hivers` | sensor | T° confort Eric |
| `sensor.temperature_corrige_chambre_hivers` | sensor | T° confort chambre |
| `sensor.groupe` | sensor | Groupe de présence (1–4) |
| `sensor.presence` | sensor | Texte présence (notif) |
| `sensor.nbre_de_fenetres_ouvertes` | sensor | Compteur fenêtres ouvertes |
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | binary_sensor | Fenêtre salon |
| `binary_sensor.contact_fenetre_cuisine_sonoff_contact` | binary_sensor | Fenêtre cuisine |
| `binary_sensor.contact_fenetre_bureau_sonoff_contact` | binary_sensor | Fenêtre bureau |
| `binary_sensor.contact_fenetre_chambre_sonoff_contact` | binary_sensor | Fenêtre chambre |
| `switch.clim_salon_nous` | switch | Prise clim salon (sécurité) |
| `switch.clim_bureau_nous` | switch | Prise clim bureau (sécurité) |
| `switch.clim_chambre_nous` | switch | Prise clim chambre (sécurité) |
| `input_boolean.clim_salon_arret_securise_en_cours` | input_boolean | Flag arrêt sécurisé salon |
| `input_boolean.clim_bureau_arret_securise_en_cours` | input_boolean | Flag arrêt sécurisé bureau |
| `input_boolean.clim_chambre_arret_securise_en_cours` | input_boolean | Flag arrêt sécurisé chambre |

### Entités pilotées (actions)

| Entité | Domaine | Action |
|:---|:---|:---|
| `climate.clim_salon_rm4_mini` | climate | `set_temperature` (mode + target) |
| `climate.clim_bureau_rm4_mini` | climate | `set_temperature` (mode + target) |
| `climate.clim_chambre_rm4_mini` | climate | `set_temperature` (mode + target) |

### Notifications

| Service | Titre | Condition |
|:---|:---|:---|
| `notify.mobile_app_eric` | `[AJ] ATTENTE CAPTEURS` | Boucle relance si capteur KO |
| `notify.mobile_app_eric` | `[AJ] CLIM JOUR COUPÉE` | Fenêtre ouverte |
| `notify.mobile_app_eric` | `[AJ] presence` | Résumé températures envoyées |

---

## ⚠️ Points d'attention

- La version `2026-01-01` est **obsolète** — même `id: force_run` → conflit potentiel si les deux coexistent dans la prod.
- Les températures cibles sont asymétriques : Salon suit Mamour (G2/G4), Bureau suit Eric (G3/G4), Chambre a sa propre variable.
- Le `sensor_update` ne redémarre **pas** une clim déjà en `off` (protection intentionnelle).
