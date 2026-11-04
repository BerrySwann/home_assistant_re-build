# GLOBAL_INDEX_SCRIPTS_YAML.md - index des scripts Home Assistant

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--04-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Scripts-4fc3f7?style=flat-square)](.)

</div>

Fichier GENERE le 2026-11-04 19:34 par docs/04_docs_scripts/04_docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py. Ne pas modifier a la main : /histo le regenere et ecrase les modifications.

## Difference entre les index SH, PY et YAML

- Scripts SH et PY (index GLOBAL_INDEX_SCRIPTS_SH.md pour les .sh bash, GLOBAL_INDEX_SCRIPTS_PY.md pour les .py python, dossier 04_docs_scripts_SH) : programmes executes par un interpreteur sur une machine, pas par Home Assistant lui-meme. En prod ils sont dans /config/.scripts (H:\.scripts) et HA les lance par une commande shell_command (dossier H:\shell_command). Les scripts de controle et de generation (hermes_*, gen_*) tournent sur le PC d'Eric, sans passer par HA. Un script SH se modifie et se pousse comme un fichier.
- Scripts YAML (index GLOBAL_INDEX_SCRIPTS_YAML.md, dossier 04_docs_scripts_YAML) : scripts Home Assistant definis dans H:\scripts.yaml, qui existent comme entites script.xxx. Ce sont des suites d'actions HA, appelables par un bouton du dashboard, une automatisation ou un autre script. Un script YAML peut declencher un script SH par une action shell_command.xxx.
- Chaine type : bouton du dashboard -> script YAML (scripts.yaml) -> commande shell_command (H:\shell_command) -> script SH (/config/.scripts).
- Verification par /histo : les trois index sont regeneres par docs/04_docs_scripts/04_docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py a chaque /histo. La section Controle liste les ecarts et /histo doit verifier que la ligne liens=N casses=M donne casses=0. Ne pas modifier ces fichiers a la main.

## Controle

- Scripts dans H:\scripts.yaml (prod) : 9
- Scripts de la prod sans YAML local : 0
- Scripts dont le contenu local differe de la prod : 1 (p1_master_gestion_clim)
- Scripts sans fiche dans 04_docs_scripts_YAML_MD : 0
- YAML locaux absents de scripts.yaml : 0
- Fichiers .py rangés dans 04_docs_scripts_YAML (ce sont des scripts de type SH) : 0

## SCRIPTS HOME ASSISTANT, ILS TOURNENT DANS HOME ASSISTANT

#### .yaml (definis dans H:\scripts.yaml)

| Cle | Alias | Entite HA | Mode | YAML local | Local = prod | Appelle (shell_command -> script SH) | Fiche |
|:----|:------|:----------|:-----|:-----------|:-------------|:-------------------------------------|:------|
| audit_md5 | Audit MD5 GitHub | `script.audit_md5` | single | [Audit_md5.yaml](04_docs_scripts_YAML/Audit_md5/Audit_md5.yaml) | identique | shell_command.audit_md5 -> audit_md5_yaml.sh | [Audit_md5.md](04_docs_scripts_YAML_MD/Audit_md5/Audit_md5.md) |
| audit_md5_md_yaml | Audit MD5 MD YAML | `script.audit_md5_md_yaml` | single | [Audit_md5_md_yaml.yaml](04_docs_scripts_YAML/Audit_md5_md_yaml/Audit_md5_md_yaml.yaml) | identique | shell_command.audit_md5_md_yaml -> audit_md5_md_yaml.sh | [Audit_md5_md_yaml.md](04_docs_scripts_YAML_MD/Audit_md5_md_yaml/Audit_md5_md_yaml.md) |
| j_1_1_salon_clim_on_off_intelligent | J 1-1 SALON - CLIM ON/OFF INTELLIGENT | `script.j_1_1_salon_clim_on_off_intelligent` | single | [J_1_1_salon_clim_on_off_intelligent.yaml](04_docs_scripts_YAML/Climatisation/J_1_1_salon_clim_on_off_intelligent/J_1_1_salon_clim_on_off_intelligent.yaml) | identique | - | [J_1_1_salon_clim_on_off_intelligent.md](04_docs_scripts_YAML_MD/Climatisation/J_1_1_salon_clim_on_off_intelligent/J_1_1_salon_clim_on_off_intelligent.md) |
| j_1_2_bureau_clim_on_off_intelligent | J 1-2 BUREAU - CLIM ON/OFF INTELLIGENT | `script.j_1_2_bureau_clim_on_off_intelligent` | single | [J_1_2_bureau_clim_on_off_intelligent.yaml](04_docs_scripts_YAML/Climatisation/J_1_2_bureau_clim_on_off_intelligent/J_1_2_bureau_clim_on_off_intelligent.yaml) | identique | - | [J_1_2_bureau_clim_on_off_intelligent.md](04_docs_scripts_YAML_MD/Climatisation/J_1_2_bureau_clim_on_off_intelligent/J_1_2_bureau_clim_on_off_intelligent.md) |
| j_1_3_chambre_clim_on_off_intelligent | J 1-3 CHAMBRE - CLIM ON/OFF INTELLIGENT | `script.j_1_3_chambre_clim_on_off_intelligent` | single | [J_1_3_chambre_clim_on_off_intelligent.yaml](04_docs_scripts_YAML/Climatisation/J_1_3_chambre_clim_on_off_intelligent/J_1_3_chambre_clim_on_off_intelligent.yaml) | identique | - | [J_1_3_chambre_clim_on_off_intelligent.md](04_docs_scripts_YAML_MD/Climatisation/J_1_3_chambre_clim_on_off_intelligent/J_1_3_chambre_clim_on_off_intelligent.md) |
| j_2_0_secu_arret_clim_protege | J 2-0 SECU - ARRÊT CLIM PROTÉGÉ | `script.j_2_0_secu_arret_clim_protege` | parallel | [J_2_0_secu_arret_clim_protege.yaml](04_docs_scripts_YAML/Climatisation/J_2_0_secu_arret_clim_protege/J_2_0_secu_arret_clim_protege.yaml) | identique | - | [J_2_0_secu_arret_clim_protege.md](04_docs_scripts_YAML_MD/Climatisation/J_2_0_secu_arret_clim_protege/J_2_0_secu_arret_clim_protege.md) |
| p1_master_gestion_clim | P1 - MASTER : Gestion centralisée climatisation | `script.p1_master_gestion_clim` | queued | [P1_Master_gestion_clim.yaml](04_docs_scripts_YAML/Climatisation/P1_Master_gestion_clim/P1_Master_gestion_clim.yaml) | DIFFERENT | - | [P1_Master_gestion_clim.md](04_docs_scripts_YAML_MD/P1_Master_gestion_clim/P1_Master_gestion_clim.md) |
| sdb_soufflant_arreter | SDB - Soufflant : ARRET (resistances, ventilateur 1 min 30, prise) | `script.sdb_soufflant_arreter` | single | [SDB_soufflant_arreter.yaml](04_docs_scripts_YAML/Soufflant_SDB/SDB_soufflant_arreter/SDB_soufflant_arreter.yaml) | identique | - | [SDB_soufflant_arreter.md](04_docs_scripts_YAML_MD/Soufflant_SDB/SDB_soufflant_arreter/SDB_soufflant_arreter.md) |
| sdb_soufflant_demarrer | SDB - Soufflant : DEMARRAGE (2000 W, verrou 30 s) | `script.sdb_soufflant_demarrer` | single | [SDB_soufflant_demarrer.yaml](04_docs_scripts_YAML/Soufflant_SDB/SDB_soufflant_demarrer/SDB_soufflant_demarrer.yaml) | identique | - | [SDB_soufflant_demarrer.md](04_docs_scripts_YAML_MD/Soufflant_SDB/SDB_soufflant_demarrer/SDB_soufflant_demarrer.md) |

## SCRIPTS HOME ASSISTANT, ILS NE TOURNENT PAS DANS HOME ASSISTANT (YAML locaux absents de scripts.yaml, python non appele par la prod)

### SCRIPTS DE L'IA CLAUDE

- aucun

---

### SCRIPTS DE L'IA HERMES

- aucun

---

<!-- RECAP-ENTITES:DEBUT -->

## Recapitulatif des entites citees par cet index

Total : **685 entites**. Origine de chacune : type, puis le nom de l integration telle qu elle apparait dans Appareils et services.

| origine | nombre | explication |
|:---|---:|:---|
| CREE template | 249 | creee par un YAML du depot, dossier `template`, sans aucune integration dans Appareils et services |
| NAT mqtt | 128 | chaine a trois maillons, verifiee le 2026-11-03 : Zigbee2MQTT (conteneur 200, Proxmox 10.32.154.244) publie vers le broker `core-mosquitto` (add-on Mosquitto, port 1883), que consomme l integration `mqtt` d Appareils et services. Si un des trois manque, les entites tombent |
| CREE utility_meter | 76 | creee par un YAML du depot, dossier `utility_meter`, sans aucune integration dans Appareils et services |
| NAT mobile_app | 49 | integration `mobile_app` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT hue | 35 | integration `hue` du coeur de Home Assistant, installee et visible dans Appareils et services |
| HACS atmofrance | 19 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services sous le nom `Atmo France - Vence` |
| HACS powercalc | 19 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services en 38 entrees (premiere : `Hue ambiance lamp salon 1`) |
| NAT systemmonitor | 11 | integration `systemmonitor` du coeur de Home Assistant, installee et visible dans Appareils et services |
| HACS scheduler | 9 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services sous le nom `Scheduler` |
| CREE statistics | 8 | creee par un YAML du depot, dossier `statistics`, sans aucune integration dans Appareils et services |
| CREE input_booleans | 7 | creee par un YAML du depot, dossier `input_booleans`, sans aucune integration dans Appareils et services |
| HACS meross_lan | 6 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services en 2 entrees (premiere : `Store SALON`) |
| CREE command_line | 5 | creee par un YAML du depot, dossier `command_line`, sans aucune integration dans Appareils et services |
| NAT hassio | 5 | integration `hassio` du coeur de Home Assistant, installee et visible dans Appareils et services |
| CREE history_stats | 4 | creee par un YAML du depot, dossier `history_stats`, sans aucune integration dans Appareils et services |
| CREE timers | 4 | creee par un YAML du depot, dossier `timers`, sans aucune integration dans Appareils et services |
| NAT broadlink | 4 | integration `broadlink` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT meteo_france | 4 | integration `meteo_france` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT proxmoxve | 4 | integration `proxmoxve` du coeur de Home Assistant, installee et visible dans Appareils et services |
| CREE groups | 3 | creee par un YAML du depot, dossier `groups`, sans aucune integration dans Appareils et services |
| CREE smartir | 3 | creee par un YAML du depot, dossier `smartir`, sans aucune integration dans Appareils et services |
| HACS blitzortung | 3 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services sous le nom `Maison` |
| NAT template | 3 | integration `template` du coeur de Home Assistant, installee et visible dans Appareils et services |
| RASPI-PI4-4GO | 3 | entites du Raspberry Pi 4 4 Go : elles existent, le materiel est hors tension (pour Raspberry Pi4 4Go) |
| CREE input_button | 2 | creee par un YAML du depot, dossier `input_button`, sans aucune integration dans Appareils et services |
| CREE input_number | 2 | creee par un YAML du depot, dossier `input_number`, sans aucune integration dans Appareils et services |
| CREE person | 2 | creee par un YAML du depot, dossier `person`, sans aucune integration dans Appareils et services |
| CREE script | 2 | creee par un YAML du depot, dossier `script`, sans aucune integration dans Appareils et services |
| HACS vigieau | 2 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services sous le nom `Vigieau AEP` |
| NAT generic_thermostat | 2 | integration `generic_thermostat` du coeur de Home Assistant, installee et visible dans Appareils et services |
| ARTEFACT-TEMPLATE | 1 | mot-cle de template, pas une entite |
| CREE automation | 1 | creee par un YAML du depot, dossier `automation`, sans aucune integration dans Appareils et services |
| CREE input_datetime | 1 | creee par un YAML du depot, dossier `input_datetime`, sans aucune integration dans Appareils et services |
| CREE input_select | 1 | creee par un YAML du depot, dossier `input_select`, sans aucune integration dans Appareils et services |
| CREE powercalc | 1 | creee par un YAML du depot, dossier `powercalc`, sans aucune integration dans Appareils et services |
| CREE rest | 1 | creee par un YAML du depot, dossier `rest`, sans aucune integration dans Appareils et services |
| CREE sql | 1 | creee par un YAML du depot, dossier `sql`, sans aucune integration dans Appareils et services |
| HACS hacs | 1 | installee via HACS (qui va etre renomme marketplace) ; son entree dans Appareils et services n a pas de nom affiche |
| NAT cpuspeed | 1 | integration `cpuspeed` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT moon | 1 | integration `moon` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT season | 1 | integration `season` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT-SANS-REGISTRE | 1 | fournie par Home Assistant sans entree au registre (zone.home) |

> **Chaine la plus fragile** : les `NAT mqtt` ne dependent pas que de Home Assistant. Mesure du 2026-11-03 : l integration `mqtt` pointe le broker add-on `core-mosquitto` (1883), et les mesures viennent de Zigbee2MQTT, conteneur 200 sur 10.32.154.244. Conteneur arrete, broker en vrac ou integration retiree : les entites tombent, sans que rien ne le signale dans l interface. A la meme date, 114 des 128 entites citees avaient remonte dans les 2 heures.

*Bloc ecrit par `recap_index.py`, encadre par deux marqueurs : il est remplace a chaque passage, jamais edite a la main. Classification : NAT <integration> si l entree de registre a un config entry ; NAT <integration> pour le coeur de Home Assistant, HACS <integration> pour ce qui vient de HACS ou d un depot (dossier custom_components) ; CREE <famille> sinon, famille = dossier du YAML qui declare l objet ; RASPI-PI4-4GO pour les trois entites du Pi 4 4 Go (materiel hors tension, entites existantes) ; SUPPRIMEE pour les noms remplaces ; ARTEFACT-TEMPLATE pour les mots-cles qui ne sont pas des entites.*

<!-- RECAP-ENTITES:FIN -->
