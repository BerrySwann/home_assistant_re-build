# ⚖️ DIFF AUTOMATIONS — PROD vs ReBuild

> **Analyse croisée — 2026-04-05**
> - **PROD (partiel)** : `automations.yaml` instance HA — 41 automations identifiées dans l'export
> - **ReBuild** : `https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/automations.yaml` — 52 automations
>
> ℹ️ L'export PROD est partiel : toutes les automations de la prod n'ont pas été comparées.
> Les "REBUILD ONLY" marqués ci-dessous peuvent exister en prod sous une autre forme.

---

## 🔴 PROD ONLY — Automations présentes en PROD mais ABSENTES du ReBuild

> → **Action requise** : soit intégrer dans ReBuild, soit confirmer suppression de prod

| # | Alias PROD | Statut | Action ReBuild |
|--:|:-----------|:------:|:---------------|
| P1 | `[00-Backup] Alerte si KO 15 min` | ⚠️ Alias différent | Correspond à `[Backup] Alerte si KO 15 min` — renommer ReBuild vers format `[XX-Backup]` |
| P2 | `[01-Backup] Git hourly H+10` | ⚠️ Alias différent | Correspond à `[Backup] Git hourly H+10` — renommer |
| P3 | `[02-Backup] Git daily (03:00)` | 🆕 NOUVELLE | Absente du ReBuild — **À AJOUTER** dans ReBuild |
| P4 | `[03-Backup] Git weekly (dim 01:30)` | ⚠️ Alias différent | Correspond à `[Backup] Git weekly (dim 01:30)` — renommer |
| P5 | `[04-Backup] Git push manuel` | 🆕 NOUVELLE | Absente du ReBuild — **À AJOUTER** (input_button.git_push_manuel) |
| P6 | `[05-Backup] Git push weekly manuel` | 🆕 NOUVELLE | Absente du ReBuild — **À AJOUTER** (input_button.git_push_weekly_manuel) |
| P7 | `Raspberry CPU Fan PWM 6 States` | 🗑️ OBSOLÈTE | Spécifique RPi4 — **À SUPPRIMER** de la prod (migration Mini-PC) |
| P8 | `E - Minuterie Sèche Serviettes Salle de Bain (Timer Absolu 2h)` | ⚠️ Contenu différent | ReBuild = 1h / PROD = 2h — **Clarifier** : quelle durée est voulue ? |
| P9 | `Gestion Simple du Store Salon (Matin/Soir)` | ⚠️ Version différente | ReBuild a version Optimisée avec anti-reflet — PROD a version simplifiée |
| P10 | `P3_Allumage Lumière Entrée` | ⚠️ Préfixe P3_ | ReBuild = `Allumage Lumière Entrée` (sans préfixe) — harmoniser |
| P11 | `P3_BUREAU - BOUTON RODRET TOGGLE BLANCHES` | ⚠️ Préfixe P3_ | ReBuild = `BUREAU - BOUTON RODRET TOGGLE BLANCHES` — harmoniser |

---

## 🟢 REBUILD ONLY — Automations dans ReBuild mais ABSENTES de PROD

> → **Action requise** : déployer vers prod

| # | Alias ReBuild | Note |
|--:|:--------------|:-----|
| R1 | `A - SALLE DE BAIN - DÉMARRAGE ET INITIALISATION DU SOUFFLANT` | Absent de prod — à déployer |
| R2 | `A - SALLE DE BAIN - GESTION INTELLIGENTE SOUFFLANT` | Version active (3 triggers) — en prod c'est la version 2026/02/01 (4 triggers) |
| R3 | `B - SALLE DE BAIN - GESTION RÉSISTANCES DU SOUFFLANT` | Absent de prod — à déployer |
| R4 | `C - SALLE DE BAIN - GESTION ARRÊT SÉCURISÉ DU SOUFFLANT` | Absent de prod — à déployer |
| R5 | `Bureau : Allumage Manu PC (MQTT) Poussoir (IKEA TRADFRI)` | Absent de prod — à déployer |
| R6 | `Bouton IKEA RODRET - TV Chambre (JSON)` | Absent de prod — à déployer |
| R7 | `Gestion Optimisée du Store Salon (Avec Mode Anti-Reflet PC)` | Prod a version Simple — à remplacer par version Optimisée |
| R8 | `DIAG - ENREGISTREMENT JOURNALIER (6 POSTES + DUT)` | Absent de prod — à déployer |
| R9 | `Mettre à jour le texte du temps écoulé` | Absent de prod — à déployer |
| R10 | `Système - Watchdog Piles (HUE/IKEA/SONOFF)` | Absent de prod — à déployer |
| R11 | `Z2M last_seen` | Absent de prod — à déployer |
| R12 | `NOTIF - Gardien Énergétique (Anomalies)` | Absent de prod — à déployer |
| R13 | `ÉNERGIE - SURVEILLANCE GROS ÉLECTRO EN HP` | Absent de prod — à déployer |

*(Note : les 4 versions archivées clim A-0-2026-01-01 et B-0-2026-01-02 sont dans ReBuild comme référence — non citées ici)*

---

## 🟡 MÊME ALIAS — CONTENU DIFFÉRENT

> → Automations avec correspondance d'alias mais dont le **contenu technique diverge**

### 1. Service de notification — ✅ RÉSOLU

| Élément | PROD | ReBuild |
|:--------|:-----|:--------|
| Service notify | `notify.mobile_app_eric` ✅ | ~~`notify.mobile_app_poco_x7_pro_eric`~~ → corrigé |
| Impact | **Toutes les 30+ automations avec notif** | 26 occurrences corrigées |

**RÉSOLU (2026-04-05) :** `notify.mobile_app_eric` est le service correct (confirmé par la prod).
- Fichiers locaux `ReBuild/automations/**/*.yaml` : déjà corrects.
- `AUTOMATIONS.md` : 26 occurrences corrigées.
- GitHub `automations.yaml` combiné : corrigé dans `/tmp/rebuild_automations.yaml` — **À PUSHER sur GitHub**.
- Plan d'action A1 : ~~en attente~~ → **FAIT**.

---

### 2. Minuterie Sèche-serviettes — Timer différent

| Élément | PROD | ReBuild |
|:--------|:-----|:--------|
| Alias | `E - Minuterie Sèche Serviettes (**Timer Absolu 2h**)` | `E - Minuterie Sèche Serviettes (**Timer Absolu 1h**)` |
| Délai | `delay: 02:00:00` | `delay: 01:00:00` |

**Décision :** 2h semble intentionnel dans la prod (description mise à jour). Corriger ReBuild à 2h.

---

### 3. Clim Jour/Nuit — Triggers et capteurs différents

| Élément | PROD | ReBuild |
|:--------|:-----|:--------|
| Capteur groupe | `sensor.groupe` | `sensor.groupe` ✅ (identique) |
| Trigger sensor update | `sensor.temperature_confort_jour` inclus | Identique ✅ |
| Sensor températures | `sensor.temperature_eco_hiver_corrige`, `sensor.temperature_corrige_*` | Identiques ✅ |
| Notify service | `notify.mobile_app_eric` | `notify.mobile_app_poco_x7_pro_eric` ⚠️ |

→ Structure globale identique, seul le service notify diverge.

---

### 4. BUREAU_ACTIVATION_ECRAN_SYNCHRO — Switch différent

| Élément | PROD | ReBuild |
|:--------|:-----|:--------|
| Switch écran | `switch.ecran_p_c_3_play_hue` | `switch.prise_ecran_bureau` |

**Décision :** Vérifier le bon nom de l'entité switch sur l'instance prod. Mettre à jour ReBuild en conséquence.

---

### 5. Automation éCO. Prises — Entités switches différentes

| Élément | PROD | ReBuild |
|:--------|:-----|:--------|
| Switch PC bureau | `switch.hue_smart_eco_pc_bureau` | `switch.hue_smart_eco_pc_bureau` ✅ |
| Switch écrans | `switch.ecran_p_c_3_play_hue` | `switch.ecran_p_c_3_play_hue` ✅ |
| Switch tête de lit | `switch.prise_tete_de_lit_chambre` | `switch.prise_tete_de_lit_chambre` ✅ |
| Notify | `notify.mobile_app_eric` | `notify.mobile_app_poco_x7_pro_eric` ⚠️ |

→ Structure identique, seul notify diverge.

---

### 6. Gestion PC bureau — Entité switch différente

| Élément | PROD | ReBuild |
|:--------|:-----|:--------|
| Switch éco PC | `switch.hue_smart_eco_pc_bureau` | `switch.hue_smart_eco_pc_bureau` ✅ |
| Trigger power | `sensor.prise_bureau_pc_ikea_power` < 80W | idem ✅ |
| Notify | `notify.mobile_app_eric` | `notify.mobile_app_poco_x7_pro_eric` ⚠️ |

---

### 7. Système - Économie Énergie VS Code — Capteurs différents

| Élément | PROD | ReBuild |
|:--------|:-----|:--------|
| Sensor CPU VSCode | `sensor.studio_code_server_pourcentage_du_processeur` | `sensor.studio_code_server_cpu_percent` |
| Sensor running | `binary_sensor.studio_code_server_en_cours_d_execution` | `binary_sensor.studio_code_server_running` |
| Nb triggers | 2 | 4 |

**Décision :** Vérifier quelles entités existent sur l'instance. Les noms prod semblent être les noms HA générés automatiquement (français). ReBuild a les `unique_id` propres. Préférer les noms du ReBuild si les entités existent.

---

### 8. SdB GESTION INTELLIGENTE — Type d'entité switch vs input_boolean

| Élément | PROD | ReBuild |
|:--------|:-----|:--------|
| Inter soufflant trigger | `switch.inter_soufflant_salle_de_bain` | `switch.inter_soufflant_salle_de_bain` ✅ |
| Inter soufflant état | `switch.inter_soufflant_salle_de_bain` | `switch.inter_soufflant_salle_de_bain` ✅ |

→ La prod utilise bien un `switch`, ReBuild idem. Pas de divergence sur ce point.

*(Note : le Watchdog D utilise `input_boolean.inter_soufflant_salle_de_bain` comme condition dans les deux — cohérent)*

---

### 9. Backup — Format des alias

| Alias PROD | Alias ReBuild |
|:-----------|:--------------|
| `[00-Backup] Alerte si KO 15 min` | `[Backup] Alerte si KO 15 min` |
| `[01-Backup] Git hourly H+10` | `[Backup] Git hourly H+10` |
| `[03-Backup] Git weekly (dim 01:30)` | `[Backup] Git weekly (dim 01:30)` |
| `[02-Backup] Git daily (03:00)` | **ABSENT** |
| `[04-Backup] Git push manuel` | **ABSENT** |
| `[05-Backup] Git push weekly manuel` | **ABSENT** |

Prod a aussi remplacé `[Backup] Git au démarrage HA` par `[02-Backup] Git daily (03:00)`.

---

## 📋 PLAN D'ACTION PRIORITAIRE

### 🔴 URGENT — Décisions bloquantes

| # | Action | Fichier ciblé |
|--:|:-------|:--------------|
| ~~A1~~ | ~~**Confirmer le service notify**~~ | ✅ RÉSOLU — `mobile_app_eric` confirmé, 26 occurrences corrigées |
| A2 | **Timer sèche-serviettes** : confirmer 2h (prod) ou garder 1h (rebuild) ? | ReBuild : E - Minuterie SdB |
| A3 | **Switch écran bureau** : `switch.ecran_p_c_3_play_hue` ou `switch.prise_ecran_bureau` ? | ReBuild : BUREAU_ACTIVATION_ECRAN_SYNCHRO |

### 🟡 À INTÉGRER dans ReBuild (depuis PROD)

| # | Action |
|--:|:-------|
| B1 | Ajouter `[02-Backup] Git daily (03:00)` dans automations.yaml ReBuild |
| B2 | Ajouter `[04-Backup] Git push manuel` + helper `input_button.git_push_manuel` |
| B3 | Ajouter `[05-Backup] Git push weekly manuel` + helper `input_button.git_push_weekly_manuel` |
| B4 | Renommer les alias Backup ReBuild vers format `[XX-Backup]` (optionnel — cohérence prod) |
| B5 | Harmoniser les alias `P3_Allumage Lumière Entrée` et `P3_BUREAU - BOUTON RODRET TOGGLE BLANCHES` (supprimer préfixe P3_ en prod OU ajouter dans ReBuild) |

### 🔴 À SUPPRIMER de PROD

| # | Alias | Raison |
|--:|:------|:-------|
| C1 | `Raspberry CPU Fan PWM 6 States` | RPi4 spécifique — migration Mini-PC done |

### 🟢 À DÉPLOYER vers PROD (depuis ReBuild)

| Priorité | Automations |
|:---------|:------------|
| Haute | R1→R4 (SdB complet), R7 (Store Salon Optimisé remplace Simple) |
| Normale | R5, R6 (Boutons MQTT), R8 (DIAG), R9 (Temps écoulé foudre) |
| Basse | R10 (Watchdog Piles), R11 (Z2M), R12 (Gardien Énergie), R13 (Surveillance HP) |

---

*Analyse basée sur export prod partiel (41/~55 automations) — 2026-04-05*
