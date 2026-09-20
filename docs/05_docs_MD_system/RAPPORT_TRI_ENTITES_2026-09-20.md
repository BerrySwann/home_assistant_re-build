# 🧹 TRI DES ENTITÉS INDISPONIBLES — RAPPORT
*Audit du 2026-09-20 — photo live : **2 221 entités** · **282 en unavailable/unknown** (110 unavailable · 172 unknown)*
*MàJ du soir : 34 scènes Hue désactivées le 2026-09-20 → compteur indispo/unknown à **248** ; ménage du pont Hue fait (27 supprimées, 7 conservées — bouton Entrée 2 repointé sur « Lumineux ») ; orphelins Riemann `energie_totale_*` purgés (47) → compteur à **201** ; 22 scènes fantômes du pont (corbeille 2020/2023) purgées ; orphelins « RASPI4 » (13 capteurs + 1 automation du printemps) archivés (`historique/RASPI4/`) puis purgés → compteur à **187** ; 9 fantômes « orphelins de config » (avril→août) archivés (`historique/FANTOMES_2026-09-20/`) + purgés → compteur à **178**.*

> **Objet :** séparer le **bruit normal** (ne rien faire) de ce qui est **à virer / nettoyer**.
>
> **Méthode :** `unavailable` = entité coupée (appareil off, réseau perdu, plateforme HS) ;
> `unknown` = entité jamais initialisée / jamais pressée / en attente de premier événement.

---

## ✅ 1. NORMAL — ne rien faire

### 1.1 Boutons sans état — 80 inventoriés (détail complet en Annexe A)

Rappel : **une entité `button` n'a pas d'état avant d'avoir été pressée** (état `unknown`). Aucun impact.

| Famille | Nb | Nature |
|:--------|:--:|:-------|
| Contrôles Proxmox (pve + VM HA + 5 LXC dont Z2M) | 30 | Démarrer / Arrêter / Redémarrer / Snapshot — jamais utilisés depuis HA |
| Identify (repérage visuel des appareils) | 32 | Fait clignoter la LED du device pour le retrouver — usage ponctuel |
| WashData (lave-linge / lave-vaisselle) | 10 | Indisponibles hors cycle — normal |
| Réserve (prises stockées) | 2 | Voir § À virer — HS volontaires |
| Z2M bridge + divers (BILRESA, store, « Ignorer tout ») | 6 | Jamais utilisés pour l'essentiel |

### 1.2 Inter Matter BILRESA — 9 boutons `unknown`

Les 9 entrées `event.bilresa_scroll_wheel_bouton_*` sont vides **avant le premier appui** — comportement normal des entités `event`.

### 1.3 Companion / vieux appareils

- `sm_a530f` (+ ses capteurs) : appareil **non connecté au .241** (RPi éteint) — normal.
- `gm1901`, `remaining_charge_time` ×4 : veilles / infos de charge indisponibles — normal.

### 1.4 Divers système

- `tts` / `stt` / `conversation` (`home_assistant_cloud`) : sans état par nature.
- Groupes (`group.hue_devices`, etc.) : dépendent des membres — normal.
- **Scènes** : les 34 étaient en `unknown` — ✅ désactivées le 2026-09-20 (voir § 3.2).

---

## 🟠 2. À VÉRIFIER (1 point restant, rien d'urgent)

### 2.1 Hue — capteurs d'énergie indisponibles — ✅ résolu le 2026-09-20

Ces capteurs (14 Hue + 33 autres) étaient des **orphelins Riemann** de la migration du 25/04 (`platform: integration`, définitions YAML supprimées, entrées de registre coincées en `unavailable`).

**Purge faite : 47 orphelins retirés du registre** → compteur indispo/unknown 248 → **201**.
Épargnés : `sensor.radiateur_elec_cuisine_energie_totale_kwh` (exception cuisine P1, encore utilisée) et les `_energie_totale` WashData (vivants).
Trace : `~/Documents/purge_orphelins_riemann_2026-09-20.txt`. La chaîne vivante (`_energy` → `_um` → `_tpl`) est intacte.

### 2.2 Zigbee2MQTT bridge

- `sensor.zigbee2mqtt_bridge_version` et `select.zigbee2mqtt_bridge_log_level` indisponibles — curieux (Z2M tourne).
- Les boutons `zigbee2mqtt_bridge_restart` : jamais pressés = normal.

---

## 🗑️ 3. À VIRER / NETTOYER

### 3.1 Prises « réserve » NOUS A1Z + A7Z — 24 entités dans cette photo (≈40 avec tout leur voisinage)

HS **volontaires** (prises stockées, débranchées). Options : **masquer** (recommandé, réversible) · désactiver · supprimer.

### 3.2 Scènes Hue — ✅ réglé le 2026-09-20

Les 34 scènes viennent du **pont Hue** (`platform: hue` — scènes classiques de l'app : Lumineux / Atténué / Veilleuse / Lecture / Default ; `lit_default_2` = doublon de nom côté pont). Vérifié : **aucune référence** à `scene.` dans la conf HA (automations, scripts, dashboard, templates, command_line, sensors, shell_command, groups).

- ✅ **Désactivées côté HA** le 2026-09-20 (registre, 34 entités, `disabled_by: user` — **réversible**) → compteur indispo/unknown : 282 → **248** ;
- ✅ **Ménage du pont Hue — FAIT le 2026-09-20** (API du pont, GO de Berry ; contrôlé aussi en v1 : schedules/rules/resourcelinks = 0 réf.) :
  - ✅ **7 scènes conservées** (liées aux boutons Hue « Smart buttons ») : « Lumineux » de Chambre / Bureau / Cuisine / Couloir / Table / Salle de bain / Entrée 1 — appuis des boutons physiques intacts ;
  - 🔁 **Bouton Entrée 2 repointé** de « Lecture » → « Lumineux » (même appui), puis **« Lecture » supprimée** → **27 supprimées au total (34 → 7)** ;
  - Backups : `~/Documents/scenes_hue_supprimees_backup_2026-09-20.json` + `hue_bouton_entree2_backup_2026-09-20.json` ;
  - Résultat : le pont ne garde que les 7 « Lumineux » (toutes pilotées par bouton) ; 0 scène fantôme côté HA ; catalogue technique purgé (22 zombies de 2020/2023 éliminés — backup : `~/Documents/scenes_zombies_hue_backup_2026-09-20.json`) ;
- Liste des 34 : Annexe B (pour réactivation éventuelle — Paramètres → Entités → afficher les désactivées).

### 3.3 Références fantômes doc L2C2 (déjà notées)

- `sensor.ete_hiver` (chips DUT) et `sensor.prise_radiateur_salle_de_bain_inspelning_ikea_power` (onglet sèche-serviette)
  introuvables en live — à repointer (GO attendu).

### 3.4 Orphelins « RASPI4 » — ✅ archivés + purgés le 2026-09-20

13 capteurs `template` (températures `core_0..3` / `cpu_package` / carte mère — télémétrie d'une machine 4 cœurs, attribués au RPi4) et 1 automation fantôme (`p3_sdb_bouton_hue_toggle_relais_lumiere`, jamais déclenchée) : **archivés** dans `historique/RASPI4/` (README + registre + références) puis **purgés du registre HA**.

### 3.5 Fantômes « orphelins de config » — ✅ archivés + purgés le 2026-09-20

9 entités sans plus aucune définition (vérifiées une à une) : 4 `genelec_appart_*_kwh_um` (renommage d'avril), 3 automations dont les fonctions vivent ailleurs (`sdb_watchdog` → remplacée par la SYNC MIROIR SdB ; `diag_7_postes_dut` → version active `_2` ; `energie_reset` → one-shot obsolète), 1 script + 1 capteur `audit_md5_docs*` (remplacés le 09/08). Archive : `historique/FANTOMES_2026-09-20/`.

---

## 📎 ANNEXE A — Les 80 boutons (liste complète)

### Contrôles Proxmox (pve + VM HA + LXC) (30)

| Entité | Nom |
|:-------|:----|
| `button.bureau_homeassistant_pause` | HomeAssistant Pause |
| `button.homeassistant` | HomeAssistant |
| `button.homeassistant_arreter` | HomeAssistant Arrêter |
| `button.homeassistant_create_snapshot` | HomeAssistant Créer un instantané |
| `button.homeassistant_demarrer` | HomeAssistant Démarrer |
| `button.homeassistant_hiberner` | HomeAssistant Suspend |
| `button.homeassistant_redemarrer` | HomeAssistant Redémarrer |
| `button.homeassistant_reinitialiser` | HomeAssistant Réinitialiser |
| `button.homeassistant_stopper` | HomeAssistant Arrêter |
| `button.mariadb_create_snapshot` | mariadb Créer un instantané |
| `button.mariadb_demarrer` | mariadb Démarrer |
| `button.mariadb_redemarrer` | mariadb Redémarrer |
| `button.mariadb_stopper` | mariadb Arrêter |
| `button.myelectricaldata_create_snapshot` | myelectricaldata Créer un instantané |
| `button.myelectricaldata_demarrer` | myelectricaldata Démarrer |
| `button.myelectricaldata_redemarrer` | myelectricaldata Redémarrer |
| `button.myelectricaldata_stopper` | myelectricaldata Arrêter |
| `button.pve_arreter` | pve Arrêter |
| `button.pve_redemarrer` | pve Redémarrer |
| `button.pve_suspend_all` | pve Suspendre tout |
| `button.pve_tout_demarrer` | pve Tout démarrer |
| `button.pve_tout_stopper` | pve Tout arrêter |
| `button.searxng_arreter` | searxng Arrêter |
| `button.searxng_creer_un_instantane` | searxng Créer un instantané |
| `button.searxng_demarrer` | searxng Démarrer |
| `button.searxng_redemarrer` | searxng Redémarrer |
| `button.z2m_create_snapshot` | Z2M Créer un instantané |
| `button.z2m_demarrer` | Z2M Démarrer |
| `button.z2m_redemarrer` | Z2M Redémarrer |
| `button.z2m_stopper` | Z2M Arrêter |

### Identify (32)

| Entité | Nom |
|:-------|:----|
| `button.clim_bureau_nous_identify` | Clim Bureau (NOUS) Identifier |
| `button.clim_chambre_nous_identify` | Clim Chambre (NOUS) Identifier |
| `button.clim_salon_nous_identify` | Clim Salon (NOUS) Identifier |
| `button.detecteur_de_fuite_ikea_identify` | détecteur de fuite (IKEA) Identifier |
| `button.detecteur_ikea_vallhorn_identify` | Detecteur (IKEA VALLHORN) Identifier |
| `button.ecran_p_c_3_play_hue_identify` | Ecran P.C. 3 PLAY HUE Identifier |
| `button.inter_bureau_rodret_identify` | Inter Bureau (RODRET) Identifier |
| `button.inter_radiateur_salle_de_bain_ikea_rodret_identify` | Inter Radiateur Salle de Bain (IKEA RODRET) Identifier |
| `button.inter_reserve_ikea_rodret_identify` | Inter Reserve IKEA RODRET Identifier |
| `button.inter_salon_4_ikea_identify` | Inter Salon (4) (IKEA) Identifier |
| `button.inter_somrig_identify` | Inter (SOMRIG) Identifier |
| `button.poussoir_pc_ikea_tradfri_identify` | Poussoir PC (IKEA TRADFRI) Identifier |
| `button.poussoir_tv_ikea_tradfri_identify` | Poussoir TV (IKEA TRADFRI) Identifier |
| `button.prise_airfryer_ninja_nous_identify` | prise airfryer ninja (NOUS) Identifier |
| `button.prise_box_internet_ikea_identify` | prise box internet (IKEA) Identifier |
| `button.prise_bureau_fer_a_repasser_nous_identify` | prise bureau fer a repasser (NOUS) Identifier |
| `button.prise_bureau_pc_ikea_identify` | prise bureau pc (IKEA) Identifier |
| `button.prise_congelateur_cuisine_nous_identify` | prise congelateur cuisine (NOUS) Identifier |
| `button.prise_four_micro_ondes_nous_identify` | prise four micro ondes (NOUS) Identifier |
| `button.prise_frigo_cuisine_nous_identify` | prise frigo cuisine (NOUS) Identifier |
| `button.prise_horloge_ikea_identify` | prise horloge (IKEA) Identifier |
| `button.prise_lave_linge_nous_identify` | prise lave linge (NOUS) Identifier |
| `button.prise_lave_vaisselle_nous_identify` | prise lave vaisselle (NOUS) Identifier |
| `button.prise_mini_pc_ikea_identify` | prise mini pc (IKEA) Identifier |
| `button.prise_pc_s_gege_ikea_identify` | prise pc's gege (IKEA) Identifier |
| `button.prise_petit_dejeune_nous_identify` | prise petit dejeune  (NOUS) Identifier |
| `button.prise_salon_chargeur_nous_identify` | prise salon chargeur (NOUS) Identifier |
| `button.prise_seche_serviette_salle_de_bain_nous_identify` | prise seche serviette salle de bain (NOUS) Identifier |
| `button.prise_soufflant_salle_de_bain_nous_identify` | prise soufflant salle de bain (NOUS) Identifier |
| `button.prise_tete_de_lit_chambre_identify` | prise tete de lit chambre Identifier |
| `button.prise_tv_chambre_nous_identify` | prise tv chambre (NOUS) Identifier |
| `button.prise_tv_salon_ikea_identify` | Prise TV Salon (IKEA) Identifier |

### BILRESA (1)

| Entité | Nom |
|:-------|:----|
| `button.bilresa_scroll_wheel_identifier_1` | BILRESA scroll wheel Identifier (1) |

### WashData (10)

| Entité | Nom |
|:-------|:----|
| `button.lave_linge_arreter_l_enregistrement_du_cycle` | Lave-Linge Arrêter l'enregistrement du cycle |
| `button.lave_linge_cycle_de_pause` | Lave-Linge Cycle de pause |
| `button.lave_linge_demarrer_l_enregistrement_du_cycle` | Lave-Linge Démarrer l'enregistrement du cycle |
| `button.lave_linge_forcer_la_fin_du_cycle` | Lave-Linge Forcer la fin du cycle |
| `button.lave_linge_reprendre_le_cycle` | Lave-Linge Reprendre le cycle |
| `button.lave_vaisselle_arreter_l_enregistrement_du_cycle` | Lave-Vaisselle Arrêter l'enregistrement du cycle |
| `button.lave_vaisselle_cycle_de_pause` | Lave-Vaisselle Cycle de pause |
| `button.lave_vaisselle_demarrer_l_enregistrement_du_cycle` | Lave-Vaisselle Démarrer l'enregistrement du cycle |
| `button.lave_vaisselle_forcer_la_fin_du_cycle` | Lave-Vaisselle Forcer la fin du cycle |
| `button.lave_vaisselle_reprendre_le_cycle` | Lave-Vaisselle Reprendre le cycle |

### Réserve (2)

| Entité | Nom |
|:-------|:----|
| `button.prise_reserve_nous_a1z_identify` | prise reserve (NOUS A1Z) Identifier |
| `button.prise_reserve_nous_a7z_identify` | prise reserve (NOUS A7Z) Identifier |

### Z2M bridge (2)

| Entité | Nom |
|:-------|:----|
| `button.zigbee2mqtt_bridge_restart` | Zigbee2MQTT Bridge Restart |
| `button.zigbee2mqtt_bridge_restart_2` | Zigbee2MQTT Bridge Restart |

### Divers (3)

| Entité | Nom |
|:-------|:----|
| `button.ignore_all_issues` | Repairs Ignorer tout |
| `button.store_bureau_refresh` | Store BUREAU Refresh |
| `button.store_bureau_reload` | Store BUREAU Reload |

## 📎 ANNEXE B — Les 34 scènes (27 supprimées le 2026-09-20 → restent les 7 « Lumineux » des boutons)

| Entité | Nom |
|:-------|:----|
| `scene.bureau_lumineux` | Bureau Lumineux |
| `scene.chambre_attenue` | Chambre Atténué |
| `scene.chambre_lumineux` | Chambre Lumineux |
| `scene.chambre_veilleuse` | Chambre Veilleuse |
| `scene.couloir_attenue` | Couloir Atténué |
| `scene.couloir_lumineux` | Couloir Lumineux |
| `scene.couloir_veilleuse` | Couloir Veilleuse |
| `scene.cuisine_attenue` | Cuisine Atténué |
| `scene.cuisine_lumineux` | Cuisine Lumineux |
| `scene.cuisine_veilleuse` | Cuisine Veilleuse |
| `scene.entree_attenue` | Entrée Atténué |
| `scene.entree_lecture` | Entrée Lecture |
| `scene.entree_lumineux` | Entrée Lumineux |
| `scene.entree_veilleuse` | Entrée Veilleuse |
| `scene.lit_attenue` | Lit Atténué |
| `scene.lit_default_2` | Lit default |
| `scene.lit_default` | Lit default |
| `scene.lit_lumineux` | Lit Lumineux |
| `scene.lit_veilleuse` | Lit Veilleuse |
| `scene.salle_de_bain_lecture` | Salle de bain Lecture |
| `scene.salle_de_bain_lumineux` | Salle de bain Lumineux |
| `scene.salon_attenue` | Salon Atténué |
| `scene.salon_lumineux` | Salon Lumineux |
| `scene.salon_salon` | Salon salon |
| `scene.salon_veilleuse` | Salon Veilleuse |
| `scene.table_attenue` | Table Atténué |
| `scene.table_lumineux` | Table Lumineux |
| `scene.table_veilleuse` | Table Veilleuse |
| `scene.zone_eric_attenue` | Zone Eric Atténué |
| `scene.zone_eric_lumineux` | Zone Eric Lumineux |
| `scene.zone_eric_veilleuse` | Zone Eric Veilleuse |
| `scene.zone_gege_attenue` | Zone Gégé Atténué |
| `scene.zone_gege_lumineux` | Zone Gégé Lumineux |
| `scene.zone_gege_veilleuse` | Zone Gégé Veilleuse |

---
*Généré par Hermes le 2026-09-20 (soirée) — données live HA.*