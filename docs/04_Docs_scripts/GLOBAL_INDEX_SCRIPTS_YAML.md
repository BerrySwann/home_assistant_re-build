# GLOBAL_INDEX_SCRIPTS_YAML.md - index des scripts Home Assistant

Fichier GENERE le 2026-10-17 13:47 par docs/04_docs_scripts/docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py. Ne pas modifier a la main : /histo le regenere et ecrase les modifications.

## Difference entre l'index SH et l'index YAML

- Scripts SH (index GLOBAL_INDEX_SCRIPTS_SH.md, dossier docs_scripts_SH) : programmes bash ou python, executes par un interpreteur sur une machine, pas par Home Assistant lui-meme. En prod ils sont dans /config/.scripts (H:\.scripts) et HA les lance par une commande shell_command (dossier H:\shell_command). Les scripts de controle et de generation (hermes_*, gen_*) tournent sur le PC d'Eric, sans passer par HA. Un script SH se modifie et se pousse comme un fichier.
- Scripts YAML (index GLOBAL_INDEX_SCRIPTS_YAML.md, dossier docs_scripts_YAML) : scripts Home Assistant definis dans H:\scripts.yaml, qui existent comme entites script.xxx. Ce sont des suites d'actions HA, appelables par un bouton du dashboard, une automatisation ou un autre script. Un script YAML peut declencher un script SH par une action shell_command.xxx.
- Chaine type : bouton du dashboard -> script YAML (scripts.yaml) -> commande shell_command (H:\shell_command) -> script SH (/config/.scripts).
- Verification par /histo : les deux index sont regeneres par docs/04_docs_scripts/docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py a chaque /histo. La section Controle liste les ecarts et /histo doit verifier que la ligne liens=N casses=M donne casses=0. Ne pas modifier ces fichiers a la main.

## Controle

- Scripts dans H:\scripts.yaml (prod) : 9
- Scripts de la prod sans YAML local : 9 (j_2_0_secu_arret_clim_protege, j_1_1_salon_clim_on_off_intelligent, j_1_2_bureau_clim_on_off_intelligent, j_1_3_chambre_clim_on_off_intelligent, audit_md5, audit_md5_md_yaml, p1_master_gestion_clim, sdb_soufflant_demarrer, sdb_soufflant_arreter)
- Scripts dont le contenu local differe de la prod : 0
- Scripts sans fiche dans docs_scripts_YAML_MD : 4 (audit_md5, audit_md5_md_yaml, sdb_soufflant_demarrer, sdb_soufflant_arreter)
- YAML locaux absents de scripts.yaml : 9 (Audit_md5, Audit_md5_md_yaml, J_1_1_salon_clim_on_off_intelligent, J_1_2_bureau_clim_on_off_intelligent, J_1_3_chambre_clim_on_off_intelligent, J_2_0_secu_arret_clim_protege, P1_Master_gestion_clim, SDB_soufflant_arreter, SDB_soufflant_demarrer)
- Fichiers .py rangés dans docs_scripts_YAML (ce sont des scripts de type SH) : 2

## Scripts YAML

| Cle | Alias | Entite HA | Mode | YAML local | Local = prod | Appelle (shell_command -> script SH) | Fiche |
|:----|:------|:----------|:-----|:-----------|:-------------|:-------------------------------------|:------|
| j_2_0_secu_arret_clim_protege | J 2-0 SECU - ARRÊT CLIM PROTÉGÉ | `script.j_2_0_secu_arret_clim_protege` | parallel | aucun | aucun YAML local | - | [Script_j2_0_secu_arret_clim.md](docs_scripts_YAML_MD/Script_j2_0_secu_arret_clim/Script_j2_0_secu_arret_clim.md) |
| j_1_1_salon_clim_on_off_intelligent | J 1-1 SALON - CLIM ON/OFF INTELLIGENT | `script.j_1_1_salon_clim_on_off_intelligent` | single | aucun | aucun YAML local | - | [Scripts_clim_on_off.md](docs_scripts_YAML_MD/Scripts_clim_on_off/Scripts_clim_on_off.md) |
| j_1_2_bureau_clim_on_off_intelligent | J 1-2 BUREAU - CLIM ON/OFF INTELLIGENT | `script.j_1_2_bureau_clim_on_off_intelligent` | single | aucun | aucun YAML local | - | [Scripts_clim_on_off.md](docs_scripts_YAML_MD/Scripts_clim_on_off/Scripts_clim_on_off.md) |
| j_1_3_chambre_clim_on_off_intelligent | J 1-3 CHAMBRE - CLIM ON/OFF INTELLIGENT | `script.j_1_3_chambre_clim_on_off_intelligent` | single | aucun | aucun YAML local | - | [Scripts_clim_on_off.md](docs_scripts_YAML_MD/Scripts_clim_on_off/Scripts_clim_on_off.md) |
| audit_md5 | Audit MD5 GitHub | `script.audit_md5` | single | aucun | aucun YAML local | shell_command.audit_md5 -> audit_md5_yaml.sh | aucune |
| audit_md5_md_yaml | Audit MD5 MD YAML | `script.audit_md5_md_yaml` | single | aucun | aucun YAML local | shell_command.audit_md5_md_yaml -> audit_md5_md_yaml.sh | aucune |
| p1_master_gestion_clim | P1 - MASTER : Gestion centralisée climatisation | `script.p1_master_gestion_clim` | queued | aucun | aucun YAML local | - | [P1_Master_gestion_clim.md](docs_scripts_YAML_MD/P1_Master_gestion_clim/P1_Master_gestion_clim.md) |
| sdb_soufflant_demarrer | SDB - Soufflant : DEMARRAGE (2000 W, verrou 30 s) | `script.sdb_soufflant_demarrer` | single | aucun | aucun YAML local | - | aucune |
| sdb_soufflant_arreter | SDB - Soufflant : ARRET (resistances, ventilateur 1 min 30, prise) | `script.sdb_soufflant_arreter` | single | aucun | aucun YAML local | - | aucune |

## Fichiers .py rangés dans docs_scripts_YAML

Ces fichiers sont des scripts python lances par shell_command : ils releveraient plutot de l'index SH. Ils sont listes ici parce qu'ils sont rangés dans ce dossier.

- [Check_yaml_forme.py](docs_scripts_YAML/Check_yaml_forme/Check_yaml_forme.py) : copie dans H:\.scripts : identique
- [Correct_linky.py](docs_scripts_YAML/Correct_linky/Correct_linky.py) : copie dans H:\.scripts : identique
