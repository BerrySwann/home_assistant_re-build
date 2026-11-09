# IA_PRISE_eCO

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--09-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-IA_System-ffeb3b?style=flat-square)](.)

</div>

*Cree le 2026-11-09 a la demande d'Eric. Liste des prises qui sont coupees ou eteintes VOLONTAIREMENT : les entites indisponibles qui en dependent sont NORMALES et ne sont pas une anomalie dans les controles HA (check complet, trigul, rapports).*

*Lire ce fichier si : rapport d'entites indisponibles (unavailable), diagnostic d'une lumiere ou d'un appareil qui ne repond pas, ajout d'une prise a la liste.*

## Regle

- Une entite indisponible rattachee a une prise de cette liste est normale : ne pas la signaler comme panne, ne pas proposer de la supprimer ni de rallumer la prise.
- Toute autre entite indisponible reste a signaler.
- Source : Eric, 2026-11-09. Chaque ajout a cette liste vient d'une phrase d'Eric.

## Groupes de presence (dit par Eric le 2026-11-09 19:19)

- Source des groupes : `sensor.groupe` (etabli : valeur `groupe_4` depuis 19:03 le 2026-11-09).
- Sens des valeurs (etabli : CLAUDE.md, referentiel P4 sensor.groupe) : `groupe_1` = Absent ; `groupe_2` = Mamour seule ; `groupe_3` = Eric seul ; `groupe_4` = tous les deux. Deduit : Mamour = Geraldine.
- Usage `groupe_2` (dit par Eric) : eclairage pour Geraldine.
- Usage `groupe_3` et `groupe_4` (dit par Eric 19:22) : peuvent servir d'eclairage quand le PC ne tourne pas, ou a l'espace loisirs quand le PC tourne (ecrans).
- Quand le PC ne tourne pas, les 3 Hue Play servent, avec les 2 lampes Hue du bureau, d'eclairage du bureau (dit par Eric). C'est la raison de leur presence dans les groupes 2, 3 et 4 pour `switch.ecran_p_c_3_play_hue`.
- Les 2 lampes Hue du bureau : entites non identifiees ici.
## Montage en cascade (dit par Eric le 2026-11-09)

- Les prises eCO sont montees en cascade avec une prise qui compte l'energie, entre autres (formule d'Eric).
- Prise tete de lit : elle est le seul eCO a compter l'energie, entre autres (dit par Eric 18:45). Pour les autres prises eCO, rien n'est note : a preciser par Eric.
- Deduit (non confirme) : si la prise en amont est coupee, la prise eCO en aval et ses entites passent indisponibles, ce qui explique les entites indisponibles normales ci-dessous (TV 70pus7855_12 coupee par la prise eco TV chambre).

---

- Cas chambre TV (dit par Eric 18:37) : `sensor.prise_tv_chambre_nous_power` (prise `switch.prise_tv_chambre_nous`, qui mesure) est couple avec la prise Hue eco. Eric a ecrit `light.hue_smart_eco_pc_bureau`.
  - A confirmer : `light.hue_smart_eco_pc_bureau` est la prise eco du PC bureau, pas de la chambre. Deduit (nom, contexte chambre) : Eric voulait peut-etre `light.hue_smart_eco_tv_chambre`. Ne pas lire cette ligne comme confirmee.
  - Releve 2026-11-09 18:37 (etabli : ha_get_state) : `light.hue_smart_eco_tv_chambre` off depuis 00:03, `sensor.prise_tv_chambre_nous_power` a 0 W depuis 00:04, `switch.prise_tv_chambre_nous` on, `light.hue_smart_eco_pc_bureau` on depuis 17:54. Les deux premiers collent avec un couplage de la prise Hue eco TV chambre (deduit).
  - Ce que la coupure eco coupe (dit par Eric) : la TV, le bluetooth des casques, le switch reseau, la FireTV Amazon, le switch SPIF, la base du casque "sheinerser" (graphie d'Eric, a confirmer).
  - Seul non coupe (dit par Eric) : `sensor.qualite_air_chambre_ikea_*` (etabli : 4 capteurs existent le 2026-11-09 : humidity, pm25, temperature, voc_index).

---

- Cas salon TV (dit par Eric 18:51) : `light.hue_smart_eco_tv_salon` (mode absent_only, groupes vides) coupe la TV du salon et un stick Fire TV Amazon (laisse sur off car Eric ne s'en sert jamais).
  - En cascade avec `switch.prise_tv_salon_ikea` (Prise TV Salon IKEA), qui compte l'energie entre autres (capteurs `sensor.prise_tv_salon_ikea_power`, `_energy`, `_current`, `_voltage`, `_quotidien_um`, `_hebdomadaire_um`, `_mensuel_um`, `_annuel_um`).
  - Branche en permanence sur cette prise IKEA (dit par Eric) : le capteur qualite air salon (IKEA), `sensor.qualite_air_salon_ikea_*` (etabli : 4 capteurs existent le 2026-11-09 : humidity, pm25, temperature, voc_index). Il n'est donc jamais coupe par l'eco.
  - Releve 2026-11-09 18:51 (etabli : ha_get_state) : `light.hue_smart_eco_tv_salon` off depuis le 2026-11-08 14:02, `switch.prise_tv_salon_ikea` on, `sensor.prise_tv_salon_ikea_power` 0.7 W. Deduit : ces 0.7 W viennent du capteur qualite air (a confirmer).

---

- Cas salon chargeurs (dit par Eric 18:56) : `light.hue_smart_eco_salon` (groupes 2 et 4) coupe les chargeurs d'accus de batteries : les rondes "27100" et celles de taille inferieure "16100" (references d'Eric, "je crois, a verifier" : a verifier sur les chargeurs, ces formats ne sont pas des references standard connues), plus un chargeur qui sert a recharger les vapotes.
  - En cascade avec `switch.prise_salon_chargeur_nous` (prise salon chargeur NOUS). Elle a des capteurs de mesure (etabli : `sensor.prise_salon_chargeur_nous_power`, `_energy`, `_current`, `_voltage`, `_quotidien_um`, `_hebdomadaire_um`, `_mensuel_um`, `_annuel_um`) ; qu'elle serve de prise de comptage n'est pas dit par Eric, deduit du nom et des capteurs.
  - Eric dit qu'elle est "connectee avec" le robot laveur / aspirateur Roborock. Le sens exact (le Roborock est-il coupe par l'eco ou reste-t-il alimente ?) est a preciser par Eric. Etabli : aucune entite dont le nom contient "roborock" dans HA le 2026-11-09.
  - Releve 2026-11-09 18:56 (etabli : ha_get_state) : `light.hue_smart_eco_salon` off depuis 17:50, `switch.prise_salon_chargeur_nous` on, `sensor.prise_salon_chargeur_nous_power` 0 W.

---

- Cas horloge IKEA (dit par Eric 19:00) : `switch.prise_horloge_ikea` compte l'energie ET coupe (c'est elle-meme la prise eCO, groupes 2 et 4) un chargeur a plusieurs sorties qui recharge la tablette et, quand c'est necessaire, les 2 petites batteries (utilisees pour recharger le telephone quand sa batterie est faible).
  - Capteurs de mesure (etabli : ha_search 2026-11-09) : `sensor.prise_horloge_ikea_power`, `_energy`, `_current`, `_voltage`, `_quotidien_um`, `_hebdomadaire_um`, `_mensuel_um`, `_annuel_um`.
  - Releve 2026-11-09 19:00 (etabli) : `switch.prise_horloge_ikea` off depuis 17:50, `sensor.prise_horloge_ikea_power` 0.2 W, `_current` 0. Une valeur de 0.2 W alors que la prise est off n'est pas expliquee (inconnu : valeur restee en memoire ou consommation propre de la prise).

---

- Cas ecran PC (dit par Eric 19:02, corrige 19:10) : `switch.ecran_p_c_3_play_hue` (nom affiche HA : "Ecran P.C. 3 PLAY HUE", groupes 2, 3 et 4) coupe les 3 Hue Play situes derriere l'un des 2 ecrans du PC, PLUS une lampe d'architecte a LED (dit par Eric 19:10, qui remplace son "uniquement les 3 Play" de 19:02).
  - Les 3 Play sont `light.hue_play_1_pc_bureau`, `light.hue_play_2_pc_bureau`, `light.hue_play_3_pc_bureau` (etabli : skill histo-final).
  - Regle existante (etabli : skill histo-final, decision d'Eric du 2026-10-11) : cette prise n'est jamais coupee pour eteindre les lumieres en fin de journee, elle reste `on` ; l'extinction passe par le service turn_off du domaine light sur les 3 Play, apres l'arret de Hue Sync.
  - Releve 2026-11-09 19:02 : a lire par ha_get_state au besoin (dernier releve connu : on depuis 14:45, 18:14).

---

- Cas bureau PC (dit par Eric 19:07) : `light.hue_smart_eco_pc_bureau` (mode absent_only, groupes vides) coupe le PC, les 2 ecrans du PC, l'Echo Show 5 Amazon et l'alimentation d'un switch USB.
  - Quelle prise compte l'energie pour ce montage : non dit par Eric, a preciser.
  - Cette liste n'est pas celle du cas chambre TV (TV, bluetooth casques, switch reseau, FireTV, switch SPIF, base casque). Deduit : le message de 18:37 qui citait `pc_bureau` visait bien la prise eco TV chambre ; a confirmer par Eric.
  - Releve 2026-11-09 18:14 (etabli) : `light.hue_smart_eco_pc_bureau` on depuis 17:54.
## Prises coupees volontairement

### 1. Prise eco tete de lit (chambre) : `switch.prise_tete_de_lit_chambre`

- Dit par Eric le 2026-11-09 18:45 : "prise tete de lit chambre", c'est le seul eCO a compter l'energie, entre autres. Elle remplace une phrase precedente d'Eric (18:13) qui designait `prise_reserve_nous_a1z` : c'est la plus recente qui fait foi, et elle colle avec la liste eco de HA (`sensor.eco_prises_config`, groupes 2 et 4).
- Etat releve 2026-11-09 18:12 : `off` (depuis 17:50). Ses entites sont disponibles.
- Ce qu'elle coupe (dit par Eric) :
  - les bougies Hue chambre_eric et chambre_gege
  - 2 chargeurs de telephone (Eric et Gege)
  - 1 chargeur avec 2 appareils : les protheses auditives et la base de recharge de la montre d'Eric (sert aussi, quand c'est necessaire, aux brosses a dents electriques et a la montre de Gege)
  - 2 boules Alexa avec l'heure dessus (nom exact : Eric ne s'en souvient plus, a retrouver)
- Entites indisponibles normales quand la prise est coupee (etabli : liste du check HA du 2026-11-09) :
  - `light.hue_color_candle_chambre_eric`, `light.hue_color_candle_chambre_gege`
  - `sensor.hue_color_candle_chambre_eric_power`, `sensor.hue_color_candle_chambre_eric_energy`
  - `sensor.hue_color_candle_chambre_gege_power`, `sensor.hue_color_candle_chambre_gege_energy`
  - compteurs eric et gege : `sensor.hue_color_candle_chambre_<eric|gege>_<quotidien|hebdomadaire|mensuel|annuel>_um` et `..._um_kwh_tpl` (16 entites)
- Entites des chargeurs, montres et boules Alexa : non identifiees, a lister si Eric le demande.

---

### 2. Prise Hue TV chambre

- Dit par Eric le 2026-11-09 : "prise hue tv chambre = le televiseur 70pus7855_12".
- Entites indisponibles normales (etabli : liste du check HA du 2026-11-09) :
  - `light.70pus7855_12_ambilight`
  - `switch.70pus7855_12_etat_de_l_ecran`
  - `switch.70pus7855_12_ambilight_hue`
- Prise de cette TV : voir la section Montage en cascade (a confirmer, light.hue_smart_eco_tv_chambre deduite).

## Prise retiree

- `switch.prise_reserve_nous_a1z` : Eric l'a retiree ("j'ai vire la prise reserve", 2026-11-09 18:45). Ses entites indisponibles (switch, child lock, countdown, 3 selects, puissance, courant, tension, energie) sont donc orphelines, pas une panne. Nettoyage possible dans Zigbee2MQTT / HA seulement sur ordre d'Eric.

## Pas dans cette liste (restent a traiter)

- Entites du bridge zigbee2mqtt (log_level, version, permit_join) : idem.
- Capteur CPU de Studio Code Server : idem.

*Fin de fiche*