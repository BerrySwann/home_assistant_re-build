# 📋 AUTOMATIONS — INVENTAIRE COMPLET (ReBuild)

> **Source unique et autoritaire :**
> `https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/automations.yaml`
> 52 automations — état au 2026-04-05
> ⚠️ Ne jamais documenter depuis le dépôt PROD (`home-assistant-config`).

---

## 🗂️ TABLE DE SYNTHÈSE GLOBALE (52 automations)

| # | Alias | Section | Mode | Triggers | Notif |
|--:|:------|:--------|:----:|:--------:|:-----:|
| 01 | (A - 0) 2026-01-01 Automatisation CLIM (07h30 <-> 21h00) | P1 / Clim | queued | 7 | ✅ |
| 02 | (A - 0) 2026-01-11 AUTOMATISATION CLIM JOUR (07H30 <-> 21H00) | P1 / Clim | queued | 7 | ✅ |
| 03 | (B - 0) 2026-01-02 Automatisation CLIM NUIT (21h00 <-> 07h30) | P1 / Clim | queued | 7 | ✅ |
| 04 | (B - 0) 2026-01-11 AUTOMATISATION CLIM NUIT (21H00 <-> 07H30) | P1 / Clim | queued | 7 | ✅ |
| 05 | (C) (CLIM OFF) Gardien Éco (Delta T < -1 et T°Ext > Seuil) | P1 / Clim | single | 1 | ✅ |
| 06 | (D) Notification température Up ou Down (7h30 -> 21h00) | P1 / Clim | queued | 2 | ✅ |
| 07 | (E) Notification température Up ou Down (21h00 -> 7h30) | P1 / Clim | queued | 2 | ✅ |
| 08 | (F) (CLIM) Notification de fermeture des fenêtres | P1 / Clim | queued | 1 | ✅ |
| 09 | (G) (CLIM) Automatisation Arrêt Clim Notification | P1 / Clim | queued | 1 | ✅ |
| 10 | (H) (CLIM) Notification changement de mode Été/Fan/Hiver | P1 / Clim | single | 1 | ✅ |
| 11 | (I) (CLIM DEBUG) Force Mode Correct & Sécurité | P1 / Clim | single | 2 | ✅ |
| 12 | (J) Synchro & Notif Clim si Prise Coupée | P1 / Clim | parallel | 1 | ✅ |
| 13 | (K) (DEBUG) Notifier les changements de message clim | P1 / Clim | single | 1 | ✅ |
| 14 | A - Chauffage Cuisine (LMMJ 4h45-7h / VSD 5h45-8h, 19.9°↔20.5°) | P1 / Cuisine | single | 6 | ✅ |
| 15 | B - Chauffage Cuisine Vacances | P1 / Cuisine | single | 3 | ✅ |
| 16 | A - SALLE DE BAIN - DÉMARRAGE ET INITIALISATION DU SOUFFLANT | P1 / SdB | single | 1 | — |
| 17 | A - 2026/02/01 - SALLE DE BAIN - GESTION INTELLIGENTE SOUFFLANT | P1 / SdB | queued | 4 | — |
| 18 | A - SALLE DE BAIN - GESTION INTELLIGENTE SOUFFLANT | P1 / SdB | queued | 3 | — |
| 19 | B - SALLE DE BAIN - GESTION RÉSISTANCES DU SOUFFLANT | P1 / SdB | single | 2 | — |
| 20 | C - SALLE DE BAIN - GESTION ARRÊT SÉCURISÉ DU SOUFFLANT | P1 / SdB | single | 1 | — |
| 21 | D - SALLE DE BAIN : WATCHDOG SÉCURITÉ RADIATEUR | P1 / SdB | single | 1 | ✅ |
| 22 | E - Minuterie Sèche Serviettes Salle de Bain (Timer Absolu 1h) | P1 / SdB | single | 1 | ✅ |
| 23 | Bureau : Allumage Manu PC (MQTT) Poussoir (IKEA TRADFRI) | P2 / Bureau | single | 1 | — |
| 24 | Automation éCO. Prises | P2 / Multi | queued | 2 | ✅ |
| 25 | Gestion PC bureau : Scène de Fin + Notif | P2 / Bureau | parallel | 2 | ✅ |
| 26 | Gestion TV Chambre : Scène de Fin + Notif | P2 / Chambre | parallel | 3 | ✅ |
| 27 | Bouton IKEA RODRET - Soufflant SdB Gestion ON/OFF (JSON) | P2 / SdB | restart | 1 | — |
| 28 | Bouton IKEA RODRET - TV Chambre (JSON) | P2 / Chambre | restart | 1 | — |
| 29 | Allumage Lumière Entrée | P3 / Entrée | queued | 1 | — |
| 30 | BUREAU_ACTIVATION_ECRAN_SYNCHRO | P3 / Bureau | restart | 2 | — |
| 31 | BUREAU - BOUTON RODRET TOGGLE BLANCHES | P3 / Bureau | restart | 1 | — |
| 32 | Bureau - Forcer Play ON si PC tourne | P3 / Bureau | parallel | 1 | — |
| 33 | BUREAU - WATCHDOG SYNCHRONISATION LAMPES BLANCHES | P3 / Bureau | restart | 2 | — |
| 34 | [Backup] Alerte si KO 15 min | Système / Backup | single | 1 | — |
| 35 | [Backup] Git au démarrage HA | Système / Backup | single | 1 | — |
| 36 | [Backup] Git hourly H+10 | Système / Backup | single | 1 | — |
| 37 | [Backup] Git weekly (dim 01:30) | Système / Backup | single | 1 | ✅ |
| 38 | Gestion Optimisée du Store Bureau | Stores | single | 4 | — |
| 39 | Gestion Optimisée du Store Salon (Avec Mode Anti-Reflet PC) | Stores | single | 4 | — |
| 40 | Alerte Météo France actualisation des "CARTES" | Météo | single | 4 | — |
| 41 | Mettre à jour le temps du dernier impact de foudre | Météo | single | 1 | — |
| 42 | Notification de la foudre | Météo | single | 1 | ✅ |
| 43 | Update previous humidity | Météo | single | 1 | — |
| 44 | Update previous temperature | Météo | single | 1 | — |
| 45 | DB Purge MariaDB + Repack | Système | single | 1 | — |
| 46 | DIAG - ENREGISTREMENT JOURNALIER (6 POSTES + DUT) | Système | single | 1 | — |
| 47 | Système - Économie Énergie VS Code | Système | single | 4 | ✅ |
| 48 | Mettre à jour le texte du temps écoulé | Météo | single | 2 | — |
| 49 | Système - Watchdog Piles (HUE/IKEA/SONOFF) | Système | single | 3 | ✅ |
| 50 | Z2M last_seen | Système / Zigbee | single | 2 | ✅ |
| 51 | NOTIF - Gardien Énergétique (Anomalies) | Énergie | single | 3 | ✅ |
| 52 | ÉNERGIE - SURVEILLANCE GROS ÉLECTRO EN HP | Énergie | single | 2 | ✅ |

---

## 📝 NOTE SUR LES VERSIONS PARALLÈLES (PAIRES A/B)

Les automations `01/02` (clim jour) et `03/04` (clim nuit) existent en **double version** dans le dépôt ReBuild — c'est intentionnel : la version datée (2026-01-01 / 2026-01-02) est l'ancienne version conservée comme référence, et la version datée 2026-01-11 est la version active corrigée. Les deux sont présentes dans `automations.yaml` mais **une seule doit être active en production** (désactiver la version obsolète via l'UI HA).

De même pour les automatisations SdB : la `17` (2026/02/01) est la version intermédiaire conservée pour référence — la `18` est la version courante.

---

## 🔍 FICHES DÉTAILLÉES — P1 CLIM (13 automations)

---

### #01 — (A - 0) 2026-01-01 Automatisation CLIM (07h30 <-> 21h00)
**⚠️ VERSION ARCHIVÉE — Remplacée par #02 (2026-01-11)**

**Rôle :** Pilotage des 3 climatiseurs (Salon, Bureau, Chambre) sur la plage jour 07h30→21h00.
Logique de présence à 4 groupes : absent (1), Mamour seule (2), Éric seul (3), les deux (4).
Calcule la température cible en fonction du groupe présent et de la saison (Été/Hiver/Fan).

**Triggers (7) :**
- `homeassistant.start` → id `force_run`
- `time: 07:30:00` → id `force_run`
- Changement `sensor.mamour_network_type` / `sensor.eric_network_type` → id `force_run`
- Changement état prise `switch.clim_*_nous` (×3) → id `force_run`
- Ouverture fenêtre `binary_sensor.contact_fenetre_*_contact` (×4) from `off` → `on` → id `window_open`
- Fermeture fenêtre idem → id `window_close`

**Mode :** `queued` | **Notif :** `mobile_app_eric`

---

### #02 — (A - 0) 2026-01-11 AUTOMATISATION CLIM JOUR (07H30 <-> 21H00)
**✅ VERSION ACTIVE**

**Rôle :** Version améliorée de #01. Pilotage clims jour avec boucle de relance et notification ciblée fenêtres.
Mêmes 4 groupes de présence. Ajout : gestion de la boucle de relance en cas d'échec IR.

**Triggers (7) :** Identiques à #01 (start, 07h30, réseau, prises, fenêtres)

**Entités clés :**
- `switch.clim_salon_nous` / `switch.clim_bureau_nous` / `switch.clim_chambre_nous`
- `climate.clim_salon_rm4_mini` / `climate.clim_bureau_rm4_mini` / `climate.clim_chambre_rm4_mini`
- `input_boolean.clim_*_arret_securise_en_cours`
- `sensor.mamour_network_type` / `sensor.eric_network_type`
- `sensor.mode_ete_hiver` / `input_number.temperature_confort_*`

**Mode :** `queued` | **Notif :** `mobile_app_eric`

---

### #03 — (B - 0) 2026-01-02 Automatisation CLIM NUIT (21h00 <-> 07h30)
**⚠️ VERSION ARCHIVÉE — Remplacée par #04 (2026-01-11)**

**Rôle :** Pilotage des clims sur la plage nuit 21h00→07h30.
Logique simplifiée nuit : si présent → `temperature_confort_nuit`, sinon coupure.

**Triggers (7) :** Identiques à #01 mais déclenchement horaire `21:00:00` à la place de `07:30:00`

**Mode :** `queued` | **Notif :** `mobile_app_eric`

---

### #04 — (B - 0) 2026-01-11 AUTOMATISATION CLIM NUIT (21H00 <-> 07H30)
**✅ VERSION ACTIVE**

**Rôle :** Version améliorée de #03. Pilotage clims nuit avec boucle de relance et notification ciblée fenêtres.

**Triggers (7) :** Identiques à #03 (start, 21h00, réseau, prises, fenêtres)

**Entités clés :** Identiques à #02
**Mode :** `queued` | **Notif :** `mobile_app_eric`

---

### #05 — (C) (CLIM OFF) Gardien Éco (Delta T < -1 et T°Ext > Seuil Non-Chauffage)

**Rôle :** Module de sécurité ÉCO. Coupe tous les climatiseurs si l'air extérieur est plus chaud que l'intérieur (inutile de chauffer) ou si le delta T dépasse le seuil de non-chauffage.

**Trigger (1) :**
- Changement de `sensor.temperature_delta_valeur`

**Conditions :**
- `sensor.temperature_delta_valeur` < -1 (T°ext > T°int)
- `sensor.th_balcon_nord_temperature` > seuil non-chauffage

**Actions :**
- Coupure des 3 climatiseurs via IR (`climate.set_hvac_mode: off`)
- Notification mobile

**Mode :** `single` | **Notif :** `mobile_app_eric`

---

### #06 — (D) Notification température Up ou Down (7h30 -> 21h00)

**Rôle :** Envoie le message personnalisé clim si le texte du capteur change OU au réveil à 07h30.

**Triggers (2) :**
- Changement de `sensor.message_clim_personnalise_7h30_21h00`
- `time: 07:30:00`

**Actions :**
- `notify.mobile_app_eric` avec le contenu du sensor de message

**Mode :** `queued` | **Notif :** `mobile_app_eric`

---

### #07 — (E) Notification température Up ou Down (21h00 -> 7h30)

**Rôle :** Idem #06 mais sur la plage nuit. Déclenche sur `sensor.message_clim_personnalise_21h00_7h30` OU à 21h00.

**Triggers (2) :**
- Changement de `sensor.message_clim_personnalise_21h00_7h30`
- `time: 21:00:00`

**Mode :** `queued` | **Notif :** `mobile_app_eric`

---

### #08 — (F) (CLIM) Notification de fermeture des fenêtres

**Rôle :** Envoie une notification lorsqu'une fenêtre est fermée (pour information post-coupure clim).

**Trigger (1) :**
- Fermeture de l'une des 4 fenêtres (`binary_sensor.contact_fenetre_*`) → `off`

**Actions :**
- Notification mobile indiquant quelle fenêtre vient d'être fermée

**Mode :** `queued` | **Notif :** `mobile_app_eric`

---

### #09 — (G) (CLIM) Automatisation Arrêt Clim Notification

**Rôle :** Notification quand une clim est coupée manuellement (uniquement si fenêtres fermées et prise alimentée — pour éviter les faux positifs).

**Trigger (1) :**
- Passage à `off` de `switch.clim_salon_nous` ou `switch.clim_bureau_nous` ou `switch.clim_chambre_nous`

**Conditions :**
- Toutes les fenêtres fermées
- Prise correspondante encore `on` (coupure manuelle, pas automatique)

**Mode :** `queued` | **Notif :** `mobile_app_eric`

---

### #10 — (H) (CLIM) Notification changement de mode Été/Fan/Hiver

**Rôle :** Notification lorsque `sensor.mode_ete_hiver` change entre Été (`cool`), Ventilateur (`fan_only`) ou Hiver (`heat`).

**Trigger (1) :**
- Changement de `sensor.mode_ete_hiver`

**Mode :** `single` | **Notif :** `mobile_app_eric`

---

### #11 — (I) (CLIM DEBUG) Force Mode Correct & Sécurité

**Rôle :** WATCHDOG double :
1. **FORCE OFF** : Si une clim tente de démarrer alors que sa prise est `off` ou qu'un arrêt sécurisé est en cours → coupure forcée.
2. **FORCE MODE** : Si une clim tourne dans le mauvais mode HVAC (ex: `heat` en été) → correction automatique.

**Triggers (2) :**
- Changement de `sensor.mode_ete_hiver`
- Changement d'état des 3 climatiseurs

**Mode :** `single` | **Notif :** `mobile_app_eric`

---

### #12 — (J) Synchro & Notif Clim si Prise Coupée

**Rôle :** Met à jour l'état du thermostat virtuel HA et notifie si la prise physique est coupée manuellement (évite le désalignement état HA / état réel).

**Trigger (1) :**
- Passage à `off` de `switch.clim_*_nous` (via template dynamique)

**Mode :** `parallel` | **Notif :** `mobile_app_eric`

---

### #13 — (K) (DEBUG) Notifier les changements de message clim

**Rôle :** Debug/surveillance : notifie chaque changement d'état du sensor `message_clim_personnalise_7h30_21h00` sur le mobile.

**Trigger (1) :**
- Changement de `sensor.message_clim_personnalise_7h30_21h00`

**Mode :** `single` | **Notif :** `mobile_app_eric`

---

## 🍳 P1 CUISINE (2 automations)

---

### #14 — A - Chauffage Cuisine (LMMJ 4h45-7h / VSD 5h45-8h, 19.9°↔20.5°)

**Rôle :** Régulation du radiateur bain d'huile cuisine (`switch.radiateur_cuisine`) selon plage horaire et hysteresis de température.
- Lundi→Jeudi : 04h45 → 07h00
- Vendredi→Dimanche : 05h45 → 08h00
- Hysteresis : allume si T° < 19.9°C, éteint si T° > 20.5°C
- Condition présence : au moins `person.eric` ou `person.mamour` à domicile

**Triggers (6) :** Horaires de démarrage (4 triggers time) et arrêt (2 triggers time) + changement T° cuisine

**Entités clés :**
- `sensor.th_cuisine_temperature`
- `switch.radiateur_cuisine`
- `person.eric` / `person.mamour`

**Mode :** `single` | **Notif :** `mobile_app_eric`

---

### #15 — B - Chauffage Cuisine Vacances

**Rôle :** Variante vacances : plage 06h00→08h30, même hysteresis 19.9°/20.5°C, sans contrainte de présence.

**Triggers (3) :**
- `time: 06:00:00`
- `time: 08:30:00`
- Changement de `sensor.th_cuisine_temperature`

**Mode :** `single` | **Notif :** `mobile_app_eric`

---

## 🚿 P1 SDB — SOUFFLANT (7 automations)

> **Contexte matériel :**
> Le soufflant SdB (2×1000W) est piloté via une **télécommande IR** (`remote.soufflant_sdb_rm4_mini`) car il n'a pas de commande directe — la prise `switch.prise_soufflant_salle_de_bain_nous` sert à couper l'alimentation physique.
> L'état logique ON/OFF est géré par `switch.inter_soufflant_salle_de_bain` (helper switch).
> La puissance active (0W / 1000W / 2000W) est mémorisée dans `input_select.etat_resistance_soufflant_sdb`.

---

### #16 — A - SALLE DE BAIN — DÉMARRAGE ET INITIALISATION DU SOUFFLANT

**Rôle :** Procédure d'allumage initial — allume la prise physique, envoie IR `on_off`, sélectionne la puissance de démarrage selon la T° (< 21°C → 2000W, > 21°C → 1000W).

**Trigger (1) :**
- Passage à `on` de `switch.inter_soufflant_salle_de_bain`

**Condition :**
- `sensor.th_salle_de_bain_temperature` < 25°C (sécurité anti-boucle watchdog)

**Séquence :**
1. `switch.turn_on` → `switch.prise_soufflant_salle_de_bain_nous`
2. Délai 1s
3. IR `on_off` → allumage soufflant
4. `choose` : si T° < 21°C → IR `1000w` × 2 (= 2000W) / sinon IR `1000w` × 1
5. Mise à jour `input_select.etat_resistance_soufflant_sdb`

**Mode :** `single`

---

### #17 — A - 2026/02/01 - SALLE DE BAIN — GESTION INTELLIGENTE SOUFFLANT
**⚠️ VERSION INTERMÉDIAIRE — Conservée pour référence**

**Rôle :** Version complète avec auto-off 60 min. Gère démarrage, régulation (23°C/22°C) et auto-extinction avec refroidissement.

**Triggers (4) :**
- Changement état `switch.inter_soufflant_salle_de_bain` → id `inter_change`
- `sensor.th_salle_de_bain_temperature` > 22.9°C (for 1min) → id `temp_high`
- `sensor.th_salle_de_bain_temperature` < 21.9°C → id `temp_low`
- `switch.inter_soufflant_salle_de_bain` ON depuis 01:00:00 → id `auto_off`

**Mode :** `queued`

---

### #18 — A - SALLE DE BAIN — GESTION INTELLIGENTE SOUFFLANT
**✅ VERSION ACTIVE**

**Rôle :** Version courante — Démarrage selon T°, régulation 23°C/22°C, commandes IR Swing et passage à 0W.

**Triggers (3) :**
- Changement état `switch.inter_soufflant_salle_de_bain` → id `inter_change`
- `sensor.th_salle_de_bain_temperature` > 22.9°C (for 1min) → id `temp_high`
- `sensor.th_salle_de_bain_temperature` < 21.9°C → id `temp_low`

**Séquence démarrage (id `inter_change` → `on`) :**
1. `switch.turn_on` prise physique
2. IR `on_off` (power ON)
3. `choose` puissance initiale (< 21°C → 2000W / sinon 1000W)
4. Mise à jour `input_select`

**Séquence T° haute (id `temp_high`) :**
1. `choose` selon puissance active :
   - 1000W → IR `on_off` × 2 (→ 0W)
   - 2000W → IR `on_off` × 1 (→ 1000W)
2. Mise à jour `input_select`

**Séquence T° basse (id `temp_low`) :**
- Si état actuel 0W → réactiver (1000W)

**Mode :** `queued`

---

### #19 — B - SALLE DE BAIN — GESTION RÉSISTANCES DU SOUFFLANT

**Rôle :** Ajustement ou coupure des résistances selon la T° ambiante et la puissance active actuelle. Complément de #18 pour la régulation fine.

**Triggers (2) :**
- `sensor.th_salle_de_bain_temperature` > 22.9°C for 1min → id `temp_23`
- `sensor.th_salle_de_bain_temperature` < 20.9°C for 1min → id `temp_21`

**Condition :**
- `switch.inter_soufflant_salle_de_bain` = `on`

**Logique T° > 23°C :**
- Si 1000W → IR ×2 → 0W
- Si 2000W → IR ×1 → 1000W
- Mise à jour `input_select`

**Logique T° < 21°C (id `temp_21`) :**
- Si état actuel = 0W → réactiver 1000W via IR

**Mode :** `single`

---

### #20 — C - SALLE DE BAIN — GESTION ARRÊT SÉCURISÉ DU SOUFFLANT

**Rôle :** Procédure d'extinction propre : IR d'abord, délai de refroidissement (1 min), puis coupure physique de la prise.

**Trigger (1) :**
- Passage à `off` de `switch.inter_soufflant_salle_de_bain`

**Condition :**
- `switch.prise_soufflant_salle_de_bain_nous` = `on` (évite l'exécution si déjà coupé par watchdog)

**Séquence :**
1. IR `on_off` (power OFF soufflant)
2. Délai 1 min (refroidissement résistance)
3. `climate.set_hvac_mode: off` sur thermostat virtuel
4. `switch.turn_off` prise physique

**Mode :** `single`

---

### #21 — D - SALLE DE BAIN : WATCHDOG SÉCURITÉ RADIATEUR

**Rôle :** Reset d'urgence physique si T° > 25°C avec dérive rapide (+0.5°C). Prévient la surchauffe.

**Trigger (1) :**
- Changement de `sensor.th_salle_de_bain_temperature`

**Conditions (4) :**
- Prise physique `on`
- `input_boolean.inter_soufflant_salle_de_bain` = `on`
- T° > 25°C
- Dérive : T° actuelle ≥ T° précédente + 0.5°C (template)

**Séquence :**
1. Attente 1 min (stabilisation)
2. IR `on_off` reset
3. `input_boolean.turn_off` (coupe la logique)
4. Attente 1 min (sécurité)
5. `switch.turn_off` prise physique
6. Notification : `"Dérive thermique détectée à XX°C. Reset IR lancé."`

**Mode :** `single` | **Notif :** `mobile_app_eric`

---

### #22 — E - Minuterie Sèche Serviettes Salle de Bain (Timer Absolu 1h)

**Rôle :** Timer de sécurité 1h sur le sèche-serviettes. Après extinction, réarme la prise en veille pour permettre le suivi conso.

**Trigger (1) :**
- `sensor.prise_seche_serviette_salle_de_bain_nous_power` > 50W

**Séquence :**
1. Délai 1h
2. Vérifie si prise encore `on`
3. `switch.turn_off` prise sèche-serviettes
4. Notification : `"1h écoulée. Arrêt automatique."`
5. Délai 1 min
6. `switch.turn_on` (réarmement en veille pour suivi conso)

**Mode :** `single` | **Notif :** `mobile_app_eric` (title: `Sèche-Serv. OFF`)

---

## 🔌 P2 PRISES (6 automations)

---

### #23 — Bureau : Allumage Manu PC (MQTT) Poussoir (IKEA TRADFRI)

**Rôle :** Allume `switch.hue_smart_eco_pc_bureau` dès réception du signal ON via MQTT (bouton IKEA TRADFRI poussoir bureau).

**Trigger (1) :** MQTT topic Zigbee2MQTT — bouton IKEA TRADFRI bureau
**Mode :** `single`

---

### #24 — Automation éCO. Prises

**Rôle :** Pilotage dynamique des prises selon le groupe de présence (1→4). Gère : horloge entrée, lampes Hue salon, écrans, PC Bureau, tête de lit chambre.

**Triggers (2) :**
- Changement de `sensor.groupe_clim` (groupe de présence)
- Changement d'état `light.hue_smart_salon`

**Logique :** `choose` sur `sensor.groupe_clim` :
- Groupe 1 (absent) → coupure de toutes les prises non-essentielles
- Groupe 2 (Mamour seule) → configuration prises Mamour
- Groupe 3 (Éric seul) → configuration prises Éric
- Groupe 4 (les deux) → configuration complète

**Mode :** `queued` | **Notif :** `mobile_app_eric`

---

### #25 — Gestion PC bureau : Scène de Fin + Notif

**Rôle :** Éteint la prise logique PC (`switch.hue_smart_eco_pc_bureau`) et notifie quand une veille prolongée ou fin de session est détectée. Laisse la prise physique `switch.prise_bureau_pc_ikea` ON pour continuer le suivi conso.

**Triggers (2) :**
- `sensor.prise_bureau_pc_ikea_power` < seuil for durée X
- Condition temporelle (nuit)

**Mode :** `parallel` | **Notif :** `mobile_app_eric`

---

### #26 — Gestion TV Chambre : Scène de Fin + Notif

**Rôle :** Éteint les lumières chambre et notifie quand la TV chambre passe en veille (<20W) après une durée. Laisse prise physique ON pour suivi conso.

**Triggers (3) :**
- `sensor.prise_tv_chambre_nous_power` < 20W for durée
- Changement état `light.hue_smart_tv_chambre`
- Condition horaire nuit

**Mode :** `parallel` | **Notif :** `mobile_app_eric`

---

### #27 — Bouton IKEA RODRET - Soufflant SdB Gestion ON/OFF (JSON)

**Rôle :** Toggle `input_boolean.inter_soufflant_salle_de_bain` via le bouton RODRET physique SdB (MQTT JSON payload).

**Trigger (1) :** MQTT topic `zigbee2mqtt/Bouton SdB RODRET` — payload JSON action
**Mode :** `restart`

---

### #28 — Bouton IKEA RODRET - TV Chambre (JSON)

**Rôle :** Toggle `switch.prise_tv_chambre_nous` via le bouton RODRET chambre (MQTT JSON payload).

**Trigger (1) :** MQTT topic `zigbee2mqtt/Bouton TV Chambre RODRET` — payload JSON action
**Mode :** `restart`

---

## 💡 P3 ÉCLAIRAGE (5 automations)

---

### #29 — Allumage Lumière Entrée

**Rôle :** Gestion éclairage entrée basée sur les transitions du groupe de présence et la luminosité (sun.sun).
Allume `light.entree` à l'arrivée si le soleil est couché ou en dessous d'un seuil.

**Trigger (1) :** Changement de `sensor.groupe_clim`
**Mode :** `queued`

---

### #30 — BUREAU_ACTIVATION_ECRAN_SYNCHRO

**Rôle :** Synchronise l'alimentation de l'écran bureau (`switch.prise_ecran_bureau`) avec l'état du PC (`binary_sensor.bureau_pc_status`).
PC ON → écran ON / PC OFF depuis 2 min → écran OFF.

**Triggers (2) :**
- `binary_sensor.bureau_pc_status` → `on` (id `pc_on`)
- `binary_sensor.bureau_pc_status` → `off` for 00:02:00 (id `pc_off`)

**Mode :** `restart`

---

### #31 — BUREAU - BOUTON RODRET TOGGLE BLANCHES

**Rôle :** Toggle des 2 lampes blanches bureau (`light.hue_white_lamp_bureau_1` et `_2`) via le bouton RODRET bureau (MQTT). Logique : si l'une est ON → tout éteindre / si tout est OFF → tout allumer.

**Trigger (1) :** MQTT topic `zigbee2mqtt/Inter Bureau (RODRET)`
**Condition payload :** `action in ['on', 'off']`
**Mode :** `restart`

---

### #32 — Bureau - Forcer Play ON si PC tourne

**Rôle :** Si les Hue Play bureau sont éteintes manuellement alors que le PC tourne (`binary_sensor.moniteur_pc = on`), les rallume automatiquement.

**Trigger (1) :** Passage à `off` de `light.hue_play_1_pc_bureau`, `_2`, ou `_3`
**Condition :** `binary_sensor.moniteur_pc = on`
**Action :** `light.turn_on` sur `{{ trigger.entity_id }}`
**Mode :** `parallel`

---

### #33 — BUREAU - WATCHDOG SYNCHRONISATION LAMPES BLANCHES

**Rôle :** Si l'une des 2 lampes blanches bureau s'allume, force l'allumage de l'autre dans les 5s. Garantit le fonctionnement en paire.

**Triggers (2) :**
- `light.hue_white_lamp_bureau_1` → `on` for 00:00:05
- `light.hue_white_lamp_bureau_2` → `on` for 00:00:05

**Condition :** L'une des deux est encore `off`
**Mode :** `restart`

---

## 💾 BACKUP GIT (4 automations)

| # | Alias | Déclencheur | Description |
|--:|:------|:------------|:------------|
| 34 | [Backup] Alerte si KO 15 min | `sensor.backup_github_status` = KO for 15min | Notification alerte backup échoué |
| 35 | [Backup] Git au démarrage HA | `homeassistant.start` | Push Git immédiat au boot |
| 36 | [Backup] Git hourly H+10 | `time_pattern: minutes: 10` | Push Git toutes les heures |
| 37 | [Backup] Git weekly (dim 01:30) | `time: dimanche 01:30` | Push + tag weekly, notification |

---

## 🪟 STORES (2 automations)

---

### #38 — Gestion Optimisée du Store Bureau

**Rôle :** Gestion store bureau avec priorité sommeil et anti-reflet. Bloque tout mouvement si la fenêtre est ouverte.

**Triggers (4) :**
- Horaires (matin/soir)
- Changement `sensor.th_balcon_nord_temperature`
- Changement `binary_sensor.contact_fenetre_bureau_sonoff_contact`
- État fenêtre

**Sécurité :** Si fenêtre ouverte → aucun mouvement autorisé
**Mode :** `single`

---

### #39 — Gestion Optimisée du Store Salon (Avec Mode Anti-Reflet PC)

**Rôle :** Gère : canicule (fermeture si T° > 34°C), froid (ouverture soleil), confort visuel Mamour (anti-reflet écran). Bloque si fenêtre ouverte.

**Triggers (4) :**
- `binary_sensor.contact_fenetre_salon_sonoff_contact`
- `sensor.th_balcon_nord_temperature`
- Horaires
- État présence

**Mode :** `single`

---

## 🌩️ MÉTÉO (5 automations)

---

### #40 — Alerte Météo France actualisation des "CARTES"

**Rôle :** Force la mise à jour des images d'alerte Météo France (vigilances) au démarrage HA, aux heures clés ou sur changement de vigilance.

**Triggers (4) :** `homeassistant.start`, horaires clés, changement `sensor.meteo_france_alertes_image_today`, changement `_tomorrow`
**Mode :** `single`

---

### #41 — Mettre à jour le temps du dernier impact de foudre

**Rôle :** Met à jour `input_datetime.dernier_eclair` à chaque changement du compteur foudre Blitzortung.

**Trigger (1) :** Changement de `sensor.blitzortung_lightning_counter`
**Mode :** `single`

---

### #42 — Notification de la foudre

**Rôle :** Alerte mobile avec distance, ville ou direction et décompte des impacts.

**Trigger (1) :** Changement de `sensor.blitzortung_lightning_counter`
**Actions :** Notification avec `sensor.blitzortung_lightning_distance`, `sensor.blitzortung_lightning_localisation`, compteur
**Mode :** `single` | **Notif :** `mobile_app_eric`

---

### #43 — Update previous humidity
**Rôle :** Enregistre `sensor.th_balcon_nord_humidity` dans `input_number.th_balcon_nord_humidity_previous` toutes les 30 min pour calculer la tendance.
**Trigger :** `time_pattern: minutes: /30` | **Mode :** `single`

---

### #44 — Update previous temperature
**Rôle :** Enregistre `sensor.th_balcon_nord_temperature` dans `input_number.th_balcon_nord_temperature_previous` toutes les 30 min pour calculer la tendance.
**Trigger :** `time_pattern: minutes: /30` | **Mode :** `single`

---

### #48 — Mettre à jour le texte du temps écoulé

**Rôle :** Calcule et met à jour `input_text.dernier_impact_de_foudre_temps_ecoule` toutes les minutes (texte lisible "il y a X minutes/heures").

**Triggers (2) :**
- `time_pattern: minutes: /1`
- Changement de `input_datetime.dernier_eclair`

**Mode :** `single`

---

## 🖥️ SYSTÈME (6 automations)

---

### #45 — DB Purge MariaDB + Repack

**Rôle :** Ménage nocturne MariaDB — purge sur 7 jours de rétention + `OPTIMIZE TABLE` pour réduire la taille sur disque.

**Trigger (1) :** Horaire nuit
**Mode :** `single`

---

### #46 — DIAG - ENREGISTREMENT JOURNALIER (6 POSTES + DUT)

**Rôle :** Log toutes les 15 min la consommation des 6 postes (P0→P3), la T° extérieure et le DUT chauffage dans un fichier via `notify.file`.

**Trigger (1) :** `time_pattern: minutes: /15`
**Actions :** `notify.file` avec template JSON/CSV
**Mode :** `single`

---

### #47 — Système - Économie Énergie VS Code

**Rôle :** Coupe VS Code serveur si le CPU dépasse 10% ou s'il est inactif, avec demande de confirmation (H24). Évite la consommation inutile du mini-PC.

**Triggers (4) :**
- `sensor.system_monitor_utilisation_du_processeur` > 10% (for 30min)
- `sensor.studio_code_server_cpu_percent` > seuil
- `binary_sensor.studio_code_server_running` = `on` (nuit)
- Horaire nuit

**Mode :** `single` | **Notif :** `mobile_app_eric`

---

### #49 — Système - Watchdog Piles (HUE/IKEA/SONOFF)

**Rôle :** Vérification 3×/jour du niveau des piles de tous les capteurs Zigbee (seuil 11%). Si alerte → notification groupée.

**Triggers (3) :** Horaires (ex: 08:00, 14:00, 20:00)
**Mode :** `single` | **Notif :** `mobile_app_eric`

---

### #50 — Z2M last_seen

**Rôle :** Surveille les capteurs Zigbee injoignables (last_seen > 8h ou indisponibles). Alerte si un capteur est perdu.

**Triggers (2) :** Horaires de vérification
**Mode :** `single` | **Notif :** `mobile_app_eric`

---

## ⚡ ÉNERGIE — ALERTES (2 automations)

---

### #51 — NOTIF - Gardien Énergétique (Anomalies)

**Rôle :** Surveillance de 3 types d'anomalies énergétiques avec alertes ciblées :

| Trigger ID | Condition | Notification |
|:-----------|:----------|:-------------|
| `radiateur_cuisine` | `sensor.alerte_radiateur_cuisine_hors_plage` = ON for 5min | "Radiateur Cuisine chauffe hors horaires depuis 5 min !" |
| `sdb_oublie` | `sensor.duree_cycle_seche_serviettes` > 90 | "Sèche-serviettes tourne depuis 1h30..." |
| `multi_nuit` | `sensor.conso_multi_nuit_2h_5h` > 90W for 15min | "Coin Multimédia consomme XXW à 3h du matin..." |

**Triggers (3) :**
- `sensor.alerte_radiateur_cuisine_hors_plage` → `ON` for 00:05:00
- `sensor.duree_cycle_seche_serviettes` > 90
- `sensor.conso_multi_nuit_2h_5h` > 90W for 00:15:00

**Mode :** `single` | **Notif :** `mobile_app_eric`

---

### #52 — ÉNERGIE - SURVEILLANCE GROS ÉLECTRO EN HP

**Rôle :** Alerte si le lave-linge ou le lave-vaisselle démarre pendant les Heures Pleines.

**Triggers (2) :**
- `sensor.prise_lave_linge_nous_power` > 100W for 2min
- `sensor.prise_lave_vaisselle_*_power` > 100W for 2min

**Condition :**
- `binary_sensor.heures_creuses_electriques` = `off` (= on est en HP)

**Notification :**
- Title : `"Alerte Conso. HP"` (15 car.)
- Message : `"Un appareil de gros électroménager vient de démarrer en Heures Pleines ! Il est HH:MM. Vérifiez si le départ différé a bien été activé."`

**Mode :** `single` | **Notif :** `mobile_app_eric`

---

## 📊 RÉPARTITION PAR SECTION

| Section | Automations | Avec Notif |
|:--------|:-----------:|:----------:|
| P1 Clim (A→K) | 13 | 13 |
| P1 Cuisine | 2 | 2 |
| P1 SdB Soufflant | 7 | 2 |
| P2 Prises | 6 | 3 |
| P3 Éclairage | 5 | — |
| Backup Git | 4 | 1 |
| Stores | 2 | — |
| Météo | 5 | 2 |
| Système | 6 | 4 |
| Énergie Alertes | 2 | 2 |
| **TOTAL** | **52** | **29** |

---

*Généré depuis : `https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/automations.yaml`*
*Mis à jour : 2026-04-05*
