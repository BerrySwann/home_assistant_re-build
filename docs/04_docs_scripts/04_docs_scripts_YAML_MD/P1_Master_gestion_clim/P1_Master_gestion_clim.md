# P1_MASTER_GESTION_CLIM - Script centralisé climatisation

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--22-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-4fc3f7?style=flat-square)](.)

</div>

> **Script HA :** `script.p1_master_gestion_clim`
> **Fichier source :** `docs/04_docs_scripts/04_docs_scripts_YAML/Climatisation/P1_Master_gestion_clim/P1_Master_gestion_clim.yaml`
> **Ancien chemin cité par cette fiche :** `docs/04_docs_scripts/04_docs_scripts_YAML/p1_master_gestion_clim/p1_master_gestion_clim_2026-09-09.yaml` (versions antérieures : `_2026-09-06.yaml`)
> **Mode :** `queued` - max: 10
> **Appelé par :** Automation A0 (JOUR) + Automation B0 (NUIT)
> **Créé par :** Refactoring LLM local - 2026-06

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
- Vérifie 9 capteurs : `mode_ete_hiver`, `groupe`, `temperature_eco_hiver_corrige`, `temperature_eco_ete_corrige`, `temperature_corrige_salon`, `temperature_corrige_bureau`, `temperature_corrige_chambre` + selon `periode` : `temperature_confort_jour` (JOUR) ou `temperature_confort_nuit` (NUIT)
- Aucune notif pendant la boucle (fini le spam par essai)
- Au 10e cycle, **diagnostic 3 sorties** :
  - **SORTIE 1 - OFF sécurité** : `mode_ete_hiver` HS, OU éco de saison HS alors qu'on en a besoin (groupe_1, groupe HS, ou une température normale HS) → off des 3 clims + message « Arrêt sécurité capteur HS »
  - **SORTIE 2 - Mode dégradé éco** : éco de saison OK mais groupe HS ou une température normale HS → les 3 clims réglées sur la température éco de saison (eco heat si saison heat / eco cool si saison cool, lue sur les capteurs éco, jamais en dur) + message « mode dégradé »
  - **SORTIE 3 - Mode normal** : tout est OK → logique groupe/période normale

### 4. Calcul variables globales
| Variable | Source |
|:---|:---|
| `mode_saison` | `sensor.mode_ete_hiver` → heat/cool/off |
| `groupe_presence` | `sensor.groupe` |
| `fenetres_ouvertes` | expand 4× `binary_sensor.contact_fenetre_*` |
| `temp_eco_hc` | `sensor.temperature_eco_hiver_corrige` |
| `temp_eco_ec` | `sensor.temperature_eco_ete_corrige` |
| `temp_cible` | `sensor.temperature_confort_jour` |
| `tccn_s` | `sensor.temperature_consigne_nuit_salon` moins `sensor.correction_temperature_salon` |
| `tccn_b` | `sensor.temperature_consigne_nuit_bureau` moins `sensor.correction_temperature_bureau` |
| `tccn_c` | `sensor.temperature_consigne_nuit_chambre` moins `sensor.correction_temperature_chambre` |
| `tccj_s` | `sensor.temperature_corrige_salon` moins `sensor.correction_temperature_salon` |
| `tccj_b` | `sensor.temperature_corrige_bureau` moins `sensor.correction_temperature_bureau` |
| `tccj_c` | `sensor.temperature_corrige_chambre` moins `sensor.correction_temperature_chambre` |

### 5. Calcul cibles par pièce

#### SALON
| Groupe | Période | Cible |
|:---|:---|:---|
| `groupe_1` (absent) | - | chauffage : `eco_hc_salon` (eco moins la correction du salon, plancher `min_temp` de la clim) ; clim : eco ete |
| `groupe_2` (Mamour) | JOUR | `tccj_s` |
| `groupe_3` (Eric) | JOUR | `tccj_s` - `sensor.correction_script_salon` |
| `groupe_4` (Tous) | JOUR | `tccj_s` |
| tout | NUIT | `tccn_s` |

Le groupe_3 recoit `tccj_s` moins `sensor.correction_script_salon` (3). Les groupes 2 et 4 recoivent `tccj_s` sans correction.

#### BUREAU
| Groupe | Période | Cible |
|:---|:---|:---|
| `groupe_1` (absent) | - | chauffage : `eco_hc_bureau` (eco moins la correction du bureau, plancher `min_temp`) ; clim : eco ete |
| `groupe_2` (Mamour) | JOUR | `tccj_b` - `sensor.correction_script_bureau` |
| `groupe_3` (Eric) | JOUR | `tccj_b` - `sensor.correction_script_bureau` |
| `groupe_4` (Tous) | JOUR | `tccj_b` - `sensor.correction_script_bureau` |
| tout | NUIT | `tccn_b` |

En jour, les groupes 2, 3 et 4 recoivent `tccj_b` moins `sensor.correction_script_bureau` (1). Le chauffage eco du bureau en groupe_2 a ete retire le 2026-11-22 au soir.

#### CHAMBRE
| Groupe | Période | Cible |
|:---|:---|:---|
| `groupe_1` (absent) | - | chauffage : `eco_hc_chambre` (eco moins la correction de la chambre, plancher `min_temp`) ; clim : eco ete |
| `groupe_2`, `groupe_3`, `groupe_4` | JOUR | `tccj_c` - `sensor.correction_script_chambre` |
| tout | NUIT | `tccn_c` |

Hors des quatre groupes (valeur inattendue), la cible de jour retombe sur l eco de saison (`temp_eco_hc` ou `temp_eco_ec`).

**Eco en groupe_1, chauffage (depuis le 2026-11-22)** : le script calcule `eco_hc_salon`, `eco_hc_bureau` et `eco_hc_chambre`, c est a dire l eco moins la correction de la piece (1 / 2 / 2), sans descendre sous le `min_temp` lu sur l entite climate (16 au salon, 10 au bureau et a la chambre). Avec l eco a 17, il envoie 16 / 15 / 15, soit 17 reel partout. Avant : 17 envoye, donc 18 / 19 / 19 reel. L eco ete (`temp_eco_ec`), le mode degrade (`eco_saison_val`) et le bureau en groupe_2 de jour (eco sans correction) restent inchanges. La notification affiche la cible reelle de la piece : la valeur envoyee (`t_salon_target`, `t_bureau_target`, `t_chambre_target`) plus la correction de la piece, depuis le 2026-11-22 (en groupe_1 chauffage : 17 / 17 / 17 pour 16 / 15 / 15 envoye).

### 6. Exécution

**CAS URGENCE - fenêtre ouverte :**
- `climate.set_hvac_mode → off` sur les 3 clims
- Notif ciblée sur la fenêtre déclenchante
- `stop`

**Cas standard (parallel) :**
- SALON : si `switch.clim_salon_nous ON` et `input_boolean.clim_salon_arret_securise_en_cours OFF` → `climate.set_temperature`
- BUREAU : idem avec clim bureau
- CHAMBRE : idem avec clim chambre
- `sensor_update` + clim déjà en `off` → on ne la redémarre pas (protection intentionnelle)
- Délai 2s
- Notif résumé `[AJ/AN] presence - Mode / Températures` (cible réelle = valeur envoyée + correction de la pièce, arrondie à 1 décimale)

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
| `sensor.temperature_confort_jour` | T° cible jour |
| `sensor.temperature_consigne_nuit_salon` | Cible de nuit salon, seuil + décalage |
| `sensor.temperature_consigne_nuit_bureau` | Cible de nuit bureau |
| `sensor.temperature_consigne_nuit_chambre` | Cible de nuit chambre |
| `sensor.correction_temperature_salon` | Correction d'envoi salon (1) |
| `sensor.correction_temperature_bureau` | Correction d'envoi bureau (2) |
| `sensor.correction_temperature_chambre` | Correction d'envoi chambre (2) |
| `sensor.correction_script_salon` | Correction cible jour salon (3) |
| `sensor.correction_script_bureau` | Correction cible jour bureau (1) |
| `sensor.correction_script_chambre` | Correction cible jour chambre (1) |
| `sensor.consigne` | Fallback général |
| `sensor.temperature_corrige_salon` | T° confort Salon |
| `sensor.temperature_corrige_bureau` | T° confort Bureau |
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
| `climate.clim_chambre_rm4_mini` | `set_temperature` (temperature simple - SmartIR Daikin) |
| `climate.clim_salon_rm4_mini` / `clim_bureau_rm4_mini` / `clim_chambre_rm4_mini` | `set_hvac_mode: off` (urgence fenêtre) |

### Notifications
| Service | Titre | Déclenchement |
|:---|:---|:---|
| `notify.mobile_app_eric` | `[AJ/AN] ATTENTE CAPTEURS` | Boucle relance si KO |
| `notify.mobile_app_eric` | `[AJ/AN] CLIM JOUR/NUIT COUPÉE` | Fenêtre ouverte |
| `notify.mobile_app_eric` | `[AJ/AN] presence` | Résumé après commandes |

---

## ⚠️ Points d'attention

- **Libelles de `hs_list`** : le rapport de sante nomme les capteurs muets sous forme courte (`corrige_salon`, `corrige_bureau`, `corrige_chambre`, `eco_hiver_corrige`, `eco_ete_corrige`, `groupe`). Ces etiquettes sont ecrites en dur dans le script et ne suivent PAS automatiquement le renommage des entites : apres chaque renommage de capteur il faut les corriger separement, dans la copie locale ET dans la prod. Un oubli ne casse rien a l'execution, il fait seulement diverger les deux copies en silence.
- **HA reecrit `scripts.yaml`** : apres chaque enregistrement depuis l'interface, Home Assistant reformate le fichier (guillemets, passages a la ligne, echappements). Un diff brut montre alors des dizaines de lignes differentes qui ne sont que de la mise en forme : la comparaison doit se faire sur le YAML relu, jamais sur le texte.
- **SALON groupe_3 JOUR** : Eric seul, le salon recoit la cible du bureau ramenee au salon (`tccj_b` + correction bureau - correction salon), c est a dire `temperature_corrige_bureau` moins la correction du salon. C est le code du script en prod (relu le 2026-11-22) et la regle voulue par Eric : groupe_3 le jour seulement, pas la nuit. La fiche annoncait a tort `tccsj_s` pour tous les groupes depuis le 2026-11-08.
- **CIBLE ET CONSIGNE ENVOYEE SONT DEUX CHOSES (2026-11-12).** `temperature_consigne_nuit_*` est la CIBLE,
  celle que lisent les automatisations J K L, `ecart_nuit_*` et `derive_nuit_*`. La correction de dérive du
  capteur de reprise d'air se soustrait ICI, dans `tccn_*`, au moment de l'envoi. L'avoir mise dans le capteur
  de consigne faisait passer la cible de 19 à 18 et 16, donc J K L déclenchaient en permanence et le -1 restait
  collé. Ne jamais remettre la soustraction dans le template.
- **Repli de la correction à 0** : si un `correction_temperature_*` devient `unavailable`, le script
  envoie la consigne brute sans correction et SANS ALERTE. La clim vise alors 19 au lieu de 18 ou 17.
- **Les valeurs de correction sont en dur dans le template** (`state: "1"`, `"2"`, `"2"`), ce qui va
  contre la règle sans hard code. À arbitrer : constantes assumées ou `input_number`.
- `sensor_update` ne redémarre pas une clim déjà en `off` (protection intentionnelle via `trigger_id`).
- Script `mode: queued, max: 10` - les déclenchements simultanés sont mis en file.
- **Logique 3 sorties (09-09)** : si un capteur reste HS après les 10 essais, le script ne calcule plus avec des valeurs au hasard : OFF (critique), mode dégradé éco de saison (groupe ou temp normale HS), ou normal. Le message part une seule fois, au 10e cycle.
- Les températures eco sont lues sur les capteurs (`temperature_eco_hiver_corrige` / `temperature_eco_ete_corrige`) selon la saison - jamais de valeur en dur. Si l'éco de saison est HS et qu'on en a besoin → OFF (sortie 1).
---

## 📋 Changelog

| Date | Session | Modification | config_hash |
|:---|:---|:---|:---|
| 2026-11-22 | Hermes | **Cibles de jour pilotees par capteurs.** Remplacement des offsets fixes (-3/-1) par `sensor.correction_script_salon` (3), `_bureau` (1), `_chambre` (1), crees dans P1_01_clim_logique_system_autom.yaml. Salon groupe_3 = `tccj_s` - 3 ; bureau g2/g3/g4 = `tccj_b` - 1 ; chambre g2/g3/g4 = `tccj_c` - 1. Salon g2/g4 reste `tccj_s` sans offset. Version lisible |- poussee en prod. | - |
| 2026-11-22 | Claude | **Fiche corrigee, script inchange.** Cibles de jour des groupes 2, 3 et 4 alignees sur le code : salon en groupe_3 = cible du bureau ramenee au salon (`tccj_b` + correction bureau - correction salon), bureau en groupe_2 = eco en chauffage et `tccj_b` en clim. Variables `tccsj_*` renommees `tccj_*` (corrige moins correction), comme dans le script. | `ee25a74797646c88` |
| 2026-11-22 | Claude | **Notification resume : cibles reelles.** Le resume affiche valeur envoyee + correction de la piece (`t_s`, `t_b`, `t_c`) au lieu de la valeur envoyee, arrondie a 1 decimale. Les consignes envoyees aux clims ne changent pas. | `feb1f6683d7f047c` |
| 2026-11-22 | Claude | **Eco corrige en groupe_1 (chauffage).** Trois variables `eco_hc_salon`, `eco_hc_bureau`, `eco_hc_chambre` : eco moins la correction de la piece (1 / 2 / 2), plancher `min_temp` de la clim lu sur l entite climate (16 salon, 10 bureau et chambre). Envoye 16 / 15 / 15 au lieu de 17, reel 17 partout au lieu de 18 / 19 / 19. Notification : vrais sauts de ligne, valeurs `t_salon_target`, `t_bureau_target`, `t_chambre_target` (valeur reellement envoyee). YAML local reconstruit depuis la prod (il datait du 2026-11-17). | `ee25a74797646c88` |
| 2026-11-17 | Claude | **Fiche realignee sur la prod.** Capteurs `correction_temperature_salon`, `_bureau`, `_chambre` (sans `_nuit_`), valeurs relevees dans HA le 2026-11-17 : 1 / 2 / 2. La fiche annoncait 1 / 3 / 3 ; auteur et date du passage de 3 a 2 inconnus. | - |
| 2026-11-12 | Hermes | **Cible et consigne envoyee separees.** `tccn_s/b/c` ne valent plus `temperature_confort_nuit` mais `temperature_consigne_nuit_*` moins `correction_temperature_nuit_*`. Trois capteurs de correction crees dans le template : 1 au salon, 3 au bureau et a la chambre, mesures du 2026-11-10 (ecarts 1,5 / 4,0 / 3,6 du capteur de reprise d'air). Le script envoie donc 18 / 16 / 16 alors que la cible reste 19. La soustraction avait d'abord ete posee dans le template, ce qui cassait J K L : la cible tombait a 18 et 16, les automatisations declenchaient en permanence et le -1 restait colle. | - |
| 2026-11-07 | Hermes | **References aux entites supprimees** : 11 references remplacees apres la suppression de `sensor.consigne_de_base` et `sensor.temperature_cible` le meme jour. `consigne_de_base` devient `sensor.consigne` (renommage pur, meme valeur). `temperature_cible` devient `sensor.temperature_confort_jour`, qui porte desormais la cible du jour dans le template P1_01. **Pourquoi c'etait urgent** : `float()` sur une entite inconnue rend 0, donc `temp_cible` valait 0.0 et le repli `eco_saison_val` tombait aussi a 0.0, ce qui aurait envoye une consigne de 0 C aux trois clims des qu'une branche degradee s'activait. Apres correction : 20.0 et 20.0. Signale par Spook. | - |
| 2026-11-04 | S2 | **Libelles `hs_list` alignes sur la prod** : `corrige_mamour` devient `corrige_salon` et `corrige_eric` devient `corrige_bureau` dans la copie locale. Les noms d'entites avaient ete renommes le 2026-11-03, mais pas ces deux etiquettes du rapport de sante : la copie locale divergeait de la prod d'exactement deux libelles, ce que `Gen_GLOBAL_INDEX_scripts.py` signalait par `different=1`, desormais `0`. | - |
| 2026-11-03 | S2 | **Renommage des cibles de confort** : `sensor.temperature_corrige_mamour` devient `sensor.temperature_corrige_salon`, `sensor.temperature_corrige_eric` devient `sensor.temperature_corrige_bureau`. Quatre references d'entites et deux libelles de `hs_list` dans `scripts.yaml`, corriges en prod puis dans les copies. Les noms des VARIABLES internes (`tccsj_s`, `tccsj_b`) sont conserves : ils n'apparaissent nulle part a l'ecran, et les renommer aurait touche la logique de repartition par piece sans aucun gain lisible. | - |
| 2026-09-09 | Hermes | **Logique 3 sorties** après les 10 essais capteurs (version `_2026-09-09.yaml`) : sortie 1 OFF si `mode_ete_hiver` HS ou éco de saison HS + besoin éco ; sortie 2 mode dégradé éco de saison si groupe HS ou température normale HS ; sortie 3 normal. Clamp du 06-09 retiré (rollback 09-08). Chambre pilotée en `temperature` simple (SmartIR Daikin, plus de NodOn). Notif unique au 10e cycle (plus de notif par essai). | |
| 2026-09-06 | S1 | **Fix `temp_out_of_range`** : bloc `INIT : CIBLES DE TEMPÉRATURE PAR PIÈCE` reécrit avec clamp Jinja2 `[[_v, min_temp]|max, max_temp]|min` sur `state_attr` live pour `t_salon_target`, `t_bureau_target`, `t_chambre_target`. Empêche tout appel `climate.set_temperature` hors plage physique AC (Salon 16-32°C, Bureau/Chambre 18-32°C). 279→291 lignes. | `83cd286eafa2f8df` |

<!-- annotations_log:
[2026-11-17] noms des capteurs de correction (sans _nuit_) et valeurs 1/2/2 alignes sur HA ; repli 18 ou 17.
[2026-11-22] eco groupe_1 chauffage : correction soustraite, plancher min_temp (eco_hc_salon, eco_hc_bureau, eco_hc_chambre) ; notification = valeur envoyee ; YAML local realigne sur la prod (ee25a74797646c88).
[2026-11-22] cibles de jour des groupes 2/3/4 alignees sur le code prod (salon g3 = cible bureau ramenee au salon, bureau g2 = eco en chauffage) ; tccsj_* renomme tccj_*.
[2026-11-22] note SALON groupe_3 JOUR corrigee (la fiche annoncait tccsj_s pour tous les groupes).
[2026-11-22] notification resume : affiche la cible reelle (valeur envoyee + correction de la piece) au lieu de la valeur envoyee ; config_hash feb1f6683d7f047c.
[2026-11-22] cibles de jour : offsets fixes remplaces par sensor.correction_script_salon (3), _bureau (1), _chambre (1) ; salon g2/g4 sans offset ; version lisible |- poussee en prod. -->
