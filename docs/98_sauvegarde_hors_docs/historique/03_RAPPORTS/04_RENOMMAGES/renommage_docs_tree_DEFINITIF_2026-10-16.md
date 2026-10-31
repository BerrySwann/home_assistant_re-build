# Renommages dans docs - tree definitif (2026-10-16)

Etat : version definitive a valider par Eric, sous reserve des points en fin de fichier. Rien n est renomme. Ce fichier liste uniquement ce qui changerait, avec les branches qui y menent.

## Regle appliquee
- Dossiers et fichiers de `docs` (le dossier `docs` reste en minuscules), en local seulement.
- Pole : `P` majuscule + numero (`P3_`). Sans pole : premiere lettre en majuscule.
- Premier mot : premiere lettre en majuscule, tout le reste en minuscules.
- Exception : `PAGE_HOME` (dossier et md) devient `Page_Home`.
- Tous les changements sont des changements de casse seule : renommage en deux temps sous Windows, et ancien nom a supprimer ensuite en prod et dans le repo (GitHub distingue la casse).
- Noms laisses intacts (liste complete plus bas) : GLOBAL_INDEX, DEPENDANCES_GLOBALES, IA_*, COULEURS_PRISES_PAR_PIECE, 05_docs_MD_system, 00_IA, IA_CONTEXT_BASE, GRP_0X, LXCX, sigles AVG AMHQ TPL TOTAL DUT BV IB MINI MAXI (dont P?_UM_AMHQ), tout 01_docs_config_system, README, Dashboard_COMPLET.
- Les `.bak` ne sont pas listes : 362 fichiers, ils suivraient le nom de leur fichier.

## Compteurs
- Dossiers : 333 a renommer, 145 inchanges.
- Fichiers (hors .bak) : 259 a renommer, 190 inchanges.
- Collisions de noms : 0.
- Entrees inchangees car "systeme" (tout `01_docs_config_system`) : 179.

## Tree des renommages

```text
docs/
|-- 00_IA/
|   |-- sous_context_ia  ->  Sous_context_ia/
|   |   `-- ... 9 element(s) inchange(s) non liste(s)
|   `-- ... 2 element(s) inchange(s) non liste(s)
|-- 02_docs_dashboard  ->  02_Docs_dashboard/
|   |-- dashboard_docs_MD  ->  Dashboard_docs_md/
|   |   |-- L0C0_PAGE_Home/
|   |   |   |-- 02_page  ->  02_Page/
|   |   |   |   `-- PAGE_HOME.md  ->  Page_Home.md
|   |   |   |-- 03_Carte Météo  ->  03_Carte météo/
|   |   |   |   |-- www_meteocons  ->  Www_meteocons/
|   |   |   |   |   `-- METEOCONS_INSTALL.md  ->  Meteocons_install.md
|   |   |   |   |-- Carte Météo Vence.md  ->  Carte météo vence.md
|   |   |   |   `-- METEOCSS_CARD_MODIF.md  ->  Meteocss_card_modif.md
|   |   |   |-- 04_Studio Code Server  ->  04_Studio code server/
|   |   |   |   `-- CARD_VSCODE_HOME.md  ->  Card_vscode_home.md
|   |   |   |-- 05_Impacte de Foudre  ->  05_Impacte de foudre/
|   |   |   |   `-- CARD_FOUDRE_HOME.md  ->  Card_foudre_home.md
|   |   |   |-- 06_Lave Linge  ->  06_Lave linge/
|   |   |   |   `-- CARD_LAVE_LINGE_HOME.md  ->  Card_lave_linge_home.md
|   |   |   |-- 07_Lave Vaisselle  ->  07_Lave vaisselle/
|   |   |   |   `-- CARD_LAVE_VAISSELLE_HOME.md  ->  Card_lave_vaisselle_home.md
|   |   |   |-- 08_Congélateur/
|   |   |   |   `-- CARD_CONGELATEUR_HOME.md  ->  Card_congelateur_home.md
|   |   |   |-- 09_Détecteur de fuite/
|   |   |   |   `-- CARD_DETECTEUR_FUITE_HOME.md  ->  Card_detecteur_fuite_home.md
|   |   |   |-- 10_Carte Meteoalarm  ->  10_Carte meteoalarm/
|   |   |   |   `-- CARD_METEOALARM_HOME.md  ->  Card_meteoalarm_home.md
|   |   |   `-- 11_Carte Présence  ->  11_Carte présence/
|   |   |       `-- CARD_PRESENCE_HOME.md  ->  Card_presence_home.md
|   |   |-- L1C1_METEO/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page  ->  02_Page/
|   |   |   |   `-- PAGE_METEO.md  ->  Page_meteo.md
|   |   |   `-- TUTO_IMAGES_ALERTES_METEO_FRANCE.md  ->  Tuto_images_alertes_meteo_france.md
|   |   |-- L1C2_TEMPERATURES/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- PAGE_TEMPERATURES.md  ->  Page_temperatures.md
|   |   |-- L1C3_CLIM/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- PAGE_CLIM.md  ->  Page_clim.md
|   |   |-- L2C1_ENERGIE/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page_temps_reel  ->  02_Page_temps_reel/
|   |   |   |   `-- PAGE_ENERGIE_TEMPS_REEL.md  ->  Page_energie_temps_reel.md
|   |   |   |-- 03_page_principale  ->  03_Page_principale/
|   |   |   |   `-- PAGE_ENERGIE.md  ->  Page_energie.md
|   |   |   |-- 04_page_mensuel  ->  04_Page_mensuel/
|   |   |   |   `-- PAGE_ENERGIE_MENSUEL.md  ->  Page_energie_mensuel.md
|   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L2C2_ENERGIE_CLIM/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- PAGE_ENERGIE_CLIM.md  ->  Page_energie_clim.md
|   |   |-- L2C3_ENERGIE_ECLAIRAGE/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page  ->  02_Page/
|   |   |   |   `-- PAGE_ENERGIE_ECLAIRAGE.md  ->  Page_energie_eclairage.md
|   |   |   `-- COULEURS_ECLAIRAGE_PAR_PIECE.md  ->  Couleurs_eclairage_par_piece.md
|   |   |-- L3C1_ECLAIRAGE/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page_gauche  ->  02_Page_gauche/
|   |   |   |   `-- PAGE_ECLAIRAGE_GAUCHE.md  ->  Page_eclairage_gauche.md
|   |   |   `-- 03_page_droite  ->  03_Page_droite/
|   |   |       `-- PAGE_ECLAIRAGE_DROITE.md  ->  Page_eclairage_droite.md
|   |   |-- L3C2_PRISES/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- PAGE_PRISES.md  ->  Page_prises.md
|   |   |-- L3C3_STORES/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- PAGE_STORES.md  ->  Page_stores.md
|   |   |-- L4C1_MINI_PC/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page_mini_pc  ->  02_Page_mini_pc/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 03_page_raspi  ->  03_Page_raspi/
|   |   |       `-- PAGE_RASPI.md  ->  Page_raspi.md
|   |   |-- L4C2_PROXMOX/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- PAGE_PROXMOX.md  ->  Page_proxmox.md
|   |   |-- L4C3_MAJ_HA/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page_gauche  ->  02_Page_gauche/
|   |   |   |   `-- PAGE_MAJ_GAUCHE.md  ->  Page_maj_gauche.md
|   |   |   `-- 03_page_droite  ->  03_Page_droite/
|   |   |       `-- PAGE_MAJ_DROITE.md  ->  Page_maj_droite.md
|   |   |-- L5C1_PILES_BATTERIES/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- PAGE_BATTERIES.md  ->  Page_batteries.md
|   |   |-- L5C2_BATTERIES_PORTABLES/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page_gauche  ->  02_Page_gauche/
|   |   |   |   `-- PAGE_BATTERIES_PORTABLES_GAUCHE.md  ->  Page_batteries_portables_gauche.md
|   |   |   `-- 03_page_droite  ->  03_Page_droite/
|   |   |       `-- PAGE_BATTERIES_PORTABLES_DROITE.md  ->  Page_batteries_portables_droite.md
|   |   |-- L5C3_MARIADB/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page_principale  ->  02_Page_principale/
|   |   |   |   `-- PAGE_SYSTEME.md  ->  Page_systeme.md
|   |   |   `-- 03_page_reserve  ->  03_Page_reserve/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L6C1_AIR_QUALITE/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- PAGE_AIR_QUALITE.md  ->  Page_air_qualite.md
|   |   |-- L6C2_POLLUTION_POLLEN/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- PAGE_POLLUTION_POLLEN.md  ->  Page_pollution_pollen.md
|   |   `-- L6C3_VIGIEAU/
|   |       |-- 01_vignette  ->  01_Vignette/
|   |       |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |       `-- 02_page  ->  02_Page/
|   |           `-- PAGE_VIGIEAU.md  ->  Page_vigieau.md
|   |-- dashboard_docs_YAML  ->  Dashboard_docs_yaml/
|   |   |-- L0C0_PAGE_Home/
|   |   |   |-- 02_page  ->  02_Page/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 03_Carte Météo  ->  03_Carte météo/
|   |   |   |   |-- www_meteocons  ->  Www_meteocons/
|   |   |   |   |   |-- clear-night.svg  ->  Clear-night.svg
|   |   |   |   |   |-- cloudy.svg  ->  Cloudy.svg
|   |   |   |   |   |-- exceptional.svg  ->  Exceptional.svg
|   |   |   |   |   |-- fog.svg  ->  Fog.svg
|   |   |   |   |   |-- hail.svg  ->  Hail.svg
|   |   |   |   |   |-- lightning-rainy.svg  ->  Lightning-rainy.svg
|   |   |   |   |   |-- lightning.svg  ->  Lightning.svg
|   |   |   |   |   |-- partlycloudy-night.svg  ->  Partlycloudy-night.svg
|   |   |   |   |   |-- partlycloudy.svg  ->  Partlycloudy.svg
|   |   |   |   |   |-- pouring.svg  ->  Pouring.svg
|   |   |   |   |   |-- rainy.svg  ->  Rainy.svg
|   |   |   |   |   |-- snowy-rainy.svg  ->  Snowy-rainy.svg
|   |   |   |   |   |-- snowy.svg  ->  Snowy.svg
|   |   |   |   |   |-- sunny.svg  ->  Sunny.svg
|   |   |   |   |   |-- windy-variant.svg  ->  Windy-variant.svg
|   |   |   |   |   `-- windy.svg  ->  Windy.svg
|   |   |   |   |-- card_meteocss_home.yaml  ->  Card_meteocss_home.yaml
|   |   |   |   `-- meteocss-card.js  ->  Meteocss-card.js
|   |   |   |-- 04_Studio Code Server  ->  04_Studio code server/
|   |   |   |   `-- card_vscode_home.yaml  ->  Card_vscode_home.yaml
|   |   |   |-- 05_Impacte de Foudre  ->  05_Impacte de foudre/
|   |   |   |   `-- card_foudre_home.yaml  ->  Card_foudre_home.yaml
|   |   |   |-- 06_Lave Linge  ->  06_Lave linge/
|   |   |   |   `-- card_lave_linge_home.yaml  ->  Card_lave_linge_home.yaml
|   |   |   |-- 07_Lave Vaisselle  ->  07_Lave vaisselle/
|   |   |   |   `-- card_lave_vaisselle_home.yaml  ->  Card_lave_vaisselle_home.yaml
|   |   |   |-- 08_Congélateur/
|   |   |   |   `-- card_congelateur_home.yaml  ->  Card_congelateur_home.yaml
|   |   |   |-- 09_Détecteur de fuite/
|   |   |   |   `-- card_detecteur_fuite_home.yaml  ->  Card_detecteur_fuite_home.yaml
|   |   |   |-- 10_Carte Meteoalarm  ->  10_Carte meteoalarm/
|   |   |   |   `-- card_meteoalarm_home.yaml  ->  Card_meteoalarm_home.yaml
|   |   |   `-- 11_Carte Présence  ->  11_Carte présence/
|   |   |       `-- card_presence_home.yaml  ->  Card_presence_home.yaml
|   |   |-- L1C1_01_Meteo/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page  ->  02_Page/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- card_duree_du_jour.yaml  ->  Card_duree_du_jour.yaml
|   |   |-- L1C2_02_Temperatures/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L1C3_03_Commandes_Clim/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page  ->  02_Page/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- card_calcule_temp_cible.yaml  ->  Card_calcule_temp_cible.yaml
|   |   |   |-- card_prog_clim_bureau.yaml  ->  Card_prog_clim_bureau.yaml
|   |   |   |-- card_prog_clim_chambre.yaml  ->  Card_prog_clim_chambre.yaml
|   |   |   |-- card_prog_clim_salon.yaml  ->  Card_prog_clim_salon.yaml
|   |   |   |-- card_prog_radiateur_cuisine.yaml  ->  Card_prog_radiateur_cuisine.yaml
|   |   |   `-- card_prog_soufflant_sdb.yaml  ->  Card_prog_soufflant_sdb.yaml
|   |   |-- L2C1_04_Energie_Generale/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page_temps_reel  ->  02_Page_temps_reel/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 03_page_principale  ->  03_Page_principale/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 04_page_mensuel  ->  04_Page_mensuel/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L2C2_05_Energie_Clim/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L2C3_06_Energie_Eclairage/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L3C1_07_Commandes_Eclairage/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page_gauche  ->  02_Page_gauche/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 03_page_droite  ->  03_Page_droite/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L3C2_08_Commandes_Prises/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L3C3_09_Stores_Fenetres/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L4C1_10_Mini_PC/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page  ->  02_Page/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- card_popup_memory.yaml  ->  Card_popup_memory.yaml
|   |   |-- L4C2_11_Proxmox/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page  ->  02_Page/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- card_services_ha_z2m_mariadb.yaml  ->  Card_services_ha_z2m_mariadb.yaml
|   |   |-- L4C3_12_MAJ_HA/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page_gauche  ->  02_Page_gauche/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 03_page_droite  ->  03_Page_droite/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L5C1_13_Batteries_Piles/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L5C2_14_Batteries_Portables/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page_gauche  ->  02_Page_gauche/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 03_page_droite  ->  03_Page_droite/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L5C3_15_MariaDB/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 02_page_mariadb  ->  02_Page_mariadb/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- 03_page_systeme_reserve  ->  03_Page_systeme_reserve/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   |-- Script sh/
|   |   |   |   `-- audit_md5.sh  ->  Audit_md5.sh
|   |   |   |-- card_audit_buttons.yaml  ->  Card_audit_buttons.yaml
|   |   |   |-- card_audit_journal.yaml  ->  Card_audit_journal.yaml
|   |   |   |-- card_audit_md5.yaml  ->  Card_audit_md5.yaml
|   |   |   |-- card_audit_recap.yaml  ->  Card_audit_recap.yaml
|   |   |   `-- card_mariadb.yaml  ->  Card_mariadb.yaml
|   |   |-- L6C1_16_Air_Qualite/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L6C2_17_Pollution_Pollen/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- L6C3_18_VigiEau/
|   |   |   |-- 01_vignette  ->  01_Vignette/
|   |   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- PAGE_RASPI  ->  Page_raspi/
|   |   |   `-- 02_page  ->  02_Page/
|   |   |       `-- page_raspi.yaml  ->  Page_raspi.yaml
|   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   `-- ... 1 element(s) inchange(s) non liste(s)
|-- 03_docs_automations  ->  03_Docs_automations/
|   |-- docs_automations_MD  ->  Docs_automations_md/
|   |   |-- _SANS_CATEGORIE  ->  _Sans_categorie/
|   |   |   |-- P4_LOG_ZONES_ERIC  ->  P4_Log_zones_eric/
|   |   |   |   `-- P4_LOG_ZONES_ERIC.md  ->  P4_Log_zones_eric.md
|   |   |   `-- VEILLE_GITHUB_RELEASES  ->  Veille_github_releases/
|   |   |       `-- VEILLE_GITHUB_RELEASES.md  ->  Veille_github_releases.md
|   |   |-- AUTOMATIONS.YALM ORIGINAL  ->  Automations.yalm original/
|   |   |   `-- AUTOMATIONS.md  ->  Automations.md
|   |   |-- Backup HA - GitHub  ->  Backup ha - github/
|   |   |   |-- GIT_ALERTE_KO  ->  Git_alerte_ko/
|   |   |   |   `-- GIT_ALERTE_KO.md  ->  Git_alerte_ko.md
|   |   |   |-- GIT_AU_DEMARRAGE  ->  Git_au_demarrage/
|   |   |   |   `-- GIT_AU_DEMARRAGE.md  ->  Git_au_demarrage.md
|   |   |   |-- GIT_DAILY  ->  Git_daily/
|   |   |   |   `-- GIT_DAILY.md  ->  Git_daily.md
|   |   |   |-- GIT_HOURLY  ->  Git_hourly/
|   |   |   |   `-- GIT_HOURLY.md  ->  Git_hourly.md
|   |   |   |-- GIT_PUSH_MANUEL  ->  Git_push_manuel/
|   |   |   |   `-- GIT_PUSH_MANUEL.md  ->  Git_push_manuel.md
|   |   |   |-- GIT_PUSH_WEEKLY_MANUEL  ->  Git_push_weekly_manuel/
|   |   |   |   `-- GIT_PUSH_WEEKLY_MANUEL.md  ->  Git_push_weekly_manuel.md
|   |   |   `-- GIT_WEEKLY  ->  Git_weekly/
|   |   |       `-- GIT_WEEKLY.md  ->  Git_weekly.md
|   |   |-- Bouton Virtuel  ->  Bouton virtuel/
|   |   |   |-- BOUTON_INTER_IKEA_4  ->  Bouton_inter_ikea_4/
|   |   |   |   `-- BOUTON_INTER_IKEA_4.md  ->  Bouton_inter_ikea_4.md
|   |   |   `-- BOUTON_INTER_SOMRIG  ->  Bouton_inter_somrig/
|   |   |       `-- BOUTON_INTER_SOMRIG.md  ->  Bouton_inter_somrig.md
|   |   |-- Contrôle Entity z2m  ->  Contrôle entity z2m/
|   |   |   `-- Z2M_LAST_SEEN  ->  Z2m_last_seen/
|   |   |       `-- Z2M_LAST_SEEN.md  ->  Z2m_last_seen.md
|   |   |-- Gestion des Stores  ->  Gestion des stores/
|   |   |   |-- GESTION_STORE_BUREAU  ->  Gestion_store_bureau/
|   |   |   |   `-- GESTION_STORE_BUREAU.md  ->  Gestion_store_bureau.md
|   |   |   `-- GESTION_STORE_SALON  ->  Gestion_store_salon/
|   |   |       `-- GESTION_STORE_SALON.md  ->  Gestion_store_salon.md
|   |   |-- MariaDB & VSCode Optimisation  ->  Mariadb & vscode optimisation/
|   |   |   |-- DB_PURGE_MARIADB  ->  Db_purge_mariadb/
|   |   |   |   `-- DB_PURGE_MARIADB.md  ->  Db_purge_mariadb.md
|   |   |   `-- ECONOMIE_ENERGIE_VSCODE  ->  Economie_energie_vscode/
|   |   |       `-- ECONOMIE_ENERGIE_VSCODE.md  ->  Economie_energie_vscode.md
|   |   |-- Météo/
|   |   |   |-- ALERTE_METEO_CARTES  ->  Alerte_meteo_cartes/
|   |   |   |   `-- ALERTE_METEO_CARTES.md  ->  Alerte_meteo_cartes.md
|   |   |   |-- MAJ_TEMPS_FOUDRE  ->  Maj_temps_foudre/
|   |   |   |   `-- MAJ_TEMPS_FOUDRE.md  ->  Maj_temps_foudre.md
|   |   |   |-- NOTIF_FOUDRE  ->  Notif_foudre/
|   |   |   |   `-- NOTIF_FOUDRE.md  ->  Notif_foudre.md
|   |   |   |-- UPDATE_PREV_HUMIDITY  ->  Update_prev_humidity/
|   |   |   |   `-- UPDATE_PREV_HUMIDITY.md  ->  Update_prev_humidity.md
|   |   |   `-- UPDATE_PREV_TEMPERATURE  ->  Update_prev_temperature/
|   |   |       `-- UPDATE_PREV_TEMPERATURE.md  ->  Update_prev_temperature.md
|   |   |-- P0_ENRIGE  ->  P0_Enrige/
|   |   |   |-- DIAG_ENREGISTREMENT_JOURNALIER  ->  Diag_enregistrement_journalier/
|   |   |   |   `-- DIAG_ENREGISTREMENT_JOURNALIER.md  ->  Diag_enregistrement_journalier.md
|   |   |   |-- HISTO_LINKY_QUOTIDIEN  ->  Histo_linky_quotidien/
|   |   |   |   `-- HISTO_LINKY_QUOTIDIEN.md  ->  Histo_linky_quotidien.md
|   |   |   |-- HISTO_NODON_QUOTIDIEN  ->  Histo_nodon_quotidien/
|   |   |   |   `-- HISTO_NODON_QUOTIDIEN.md  ->  Histo_nodon_quotidien.md
|   |   |   |-- LOG_ECART_LINKY_NODON  ->  Log_ecart_linky_nodon/
|   |   |   |   `-- LOG_ECART_LINKY_NODON.md  ->  Log_ecart_linky_nodon.md
|   |   |   |-- RATTRAPAGE_LINKY_ECART  ->  Rattrapage_linky_ecart/
|   |   |   |   `-- RATTRAPAGE_LINKY_ECART.md  ->  Rattrapage_linky_ecart.md
|   |   |   `-- RATTRAPAGE_LINKY_J2  ->  Rattrapage_linky_j2/
|   |   |       `-- RATTRAPAGE_LINKY_J2.md  ->  Rattrapage_linky_j2.md
|   |   |-- P1_01_CLIM_CHAUFFAGE  ->  P1_01_Clim_chauffage/
|   |   |   |-- A0_CLIM_JOUR  ->  A0_clim_jour/
|   |   |   |   `-- A0_CLIM_JOUR.md  ->  A0_clim_jour.md
|   |   |   |-- B0_CLIM_NUIT  ->  B0_clim_nuit/
|   |   |   |   `-- B0_CLIM_NUIT.md  ->  B0_clim_nuit.md
|   |   |   |-- C_NOTIF_TEMP_JOUR  ->  C_notif_temp_jour/
|   |   |   |   `-- C_NOTIF_TEMP_JOUR.md  ->  C_notif_temp_jour.md
|   |   |   |-- D_NOTIF_TEMP_NUIT  ->  D_notif_temp_nuit/
|   |   |   |   `-- D_NOTIF_TEMP_NUIT.md  ->  D_notif_temp_nuit.md
|   |   |   |-- E_NOTIF_FERMETURE_FENETRES  ->  E_notif_fermeture_fenetres/
|   |   |   |   `-- E_NOTIF_FERMETURE_FENETRES.md  ->  E_notif_fermeture_fenetres.md
|   |   |   |-- F_ARRET_CLIM_NOTIF  ->  F_arret_clim_notif/
|   |   |   |   `-- F_ARRET_CLIM_NOTIF.md  ->  F_arret_clim_notif.md
|   |   |   |-- G_NOTIF_MODE_CHANGEMENT  ->  G_notif_mode_changement/
|   |   |   |   `-- G_NOTIF_MODE_CHANGEMENT.md  ->  G_notif_mode_changement.md
|   |   |   |-- H_DEBUG_FORCE_MODE  ->  H_debug_force_mode/
|   |   |   |   `-- H_DEBUG_FORCE_MODE.md  ->  H_debug_force_mode.md
|   |   |   |-- I_SYNCHRO_NOTIF_PRISE_COUPEE  ->  I_synchro_notif_prise_coupee/
|   |   |   |   `-- I_SYNCHRO_NOTIF_PRISE_COUPEE.md  ->  I_synchro_notif_prise_coupee.md
|   |   |   `-- J_DEBUG_NOTIF_MESSAGE_CLIM  ->  J_debug_notif_message_clim/
|   |   |       `-- J_DEBUG_NOTIF_MESSAGE_CLIM.md  ->  J_debug_notif_message_clim.md
|   |   |-- P1_02_Cuisine/
|   |   |   |-- A_CHAUFFAGE_CUISINE  ->  A_chauffage_cuisine/
|   |   |   |   `-- A_CHAUFFAGE_CUISINE.md  ->  A_chauffage_cuisine.md
|   |   |   |-- B_CHAUFFAGE_CUISINE_VACANCES  ->  B_chauffage_cuisine_vacances/
|   |   |   |   `-- B_CHAUFFAGE_CUISINE_VACANCES.md  ->  B_chauffage_cuisine_vacances.md
|   |   |   `-- FICHE_OP_RELAIS_CUISINE_MAJ_SHELLY  ->  Fiche_op_relais_cuisine_maj_shelly/
|   |   |       `-- FICHE_OP_RELAIS_CUISINE_MAJ_SHELLY.md  ->  Fiche_op_relais_cuisine_maj_shelly.md
|   |   |-- P1_03_Chauffage Salle de Bain  ->  P1_03_Chauffage salle de bain/
|   |   |   |-- A_SOUFFLANT_SDB_BOUTON_RODRET  ->  A_soufflant_sdb_bouton_rodret/
|   |   |   |   `-- A_SOUFFLANT_SDB_BOUTON_RODRET.md  ->  A_soufflant_sdb_bouton_rodret.md
|   |   |   |-- B_SOUFFLANT_SDB_ROUTAGE  ->  B_soufflant_sdb_routage/
|   |   |   |   `-- B_SOUFFLANT_SDB_ROUTAGE.md  ->  B_soufflant_sdb_routage.md
|   |   |   |-- C_WATCHDOG_SOUFFLANT_SDB  ->  C_watchdog_soufflant_sdb/
|   |   |   |   `-- C_WATCHDOG_SOUFFLANT_SDB.md  ->  C_watchdog_soufflant_sdb.md
|   |   |   |-- D_SDB_SOUFFLANT_DECOMPTE_60MIN  ->  D_sdb_soufflant_decompte_60min/
|   |   |   |   `-- D_SDB_SOUFFLANT_DECOMPTE_60MIN.md  ->  D_sdb_soufflant_decompte_60min.md
|   |   |   |-- E_SDB_SOUFFLANT_RATTRAPAGE_DEMARRAGE_HA  ->  E_sdb_soufflant_rattrapage_demarrage_ha/
|   |   |   |   `-- E_SDB_SOUFFLANT_RATTRAPAGE_DEMARRAGE_HA.md  ->  E_sdb_soufflant_rattrapage_demarrage_ha.md
|   |   |   |-- F_MINUTERIE_SECHE_SERVIETTES  ->  F_minuterie_seche_serviettes/
|   |   |   |   `-- F_MINUTERIE_SECHE_SERVIETTES.md  ->  F_minuterie_seche_serviettes.md
|   |   |   |-- G_SDB_SECHE_SERVIETTES_DECOMPTE_2H  ->  G_sdb_seche_serviettes_decompte_2h/
|   |   |   |   `-- G_SDB_SECHE_SERVIETTES_DECOMPTE_2H.md  ->  G_sdb_seche_serviettes_decompte_2h.md
|   |   |   |-- H_SDB_SECHE_SERVIETTES_RATTRAPAGE_DEMARRAGE_HA  ->  H_sdb_seche_serviettes_rattrapage_demarrage_ha/
|   |   |   |   `-- H_SDB_SECHE_SERVIETTES_RATTRAPAGE_DEMARRAGE_HA.md  ->  H_sdb_seche_serviettes_rattrapage_demarrage_ha.md
|   |   |   |-- RODRET_SOUFFLANT_SDB  ->  Rodret_soufflant_sdb/
|   |   |   |-- SDB_SOUFFLANT_SPECIFICATION_2026  ->  Sdb_soufflant_specification_2026/
|   |   |   |   `-- SDB_SOUFFLANT_SPECIFICATION_2026.md  ->  Sdb_soufflant_specification_2026.md
|   |   |   |-- TIMERS_SDB_SOUFFLANT_ET_SECHE_SERVIETTES  ->  Timers_sdb_soufflant_et_seche_serviettes/
|   |   |   |   `-- TIMERS_SDB_SOUFFLANT_ET_SECHE_SERVIETTES.md  ->  Timers_sdb_soufflant_et_seche_serviettes.md
|   |   |   |-- Z_SOUFFLANT_SDB_GESTION_INTELLIGENTE  ->  Z_soufflant_sdb_gestion_intelligente/
|   |   |   |   `-- Z_SOUFFLANT_SDB_GESTION_INTELLIGENTE.md  ->  Z_soufflant_sdb_gestion_intelligente.md
|   |   |   `-- Z_SOUFFLANT_SDB_old_2024-2025  ->  Z_soufflant_sdb_old_2024-2025/
|   |   |-- P2_Alarme_Congélateur  ->  P2_Alarme_congélateur/
|   |   |   |-- CONGELATEUR_ALARME_CAPTEUR  ->  Congelateur_alarme_capteur/
|   |   |   |   `-- CONGELATEUR_ALARME_CAPTEUR.md  ->  Congelateur_alarme_capteur.md
|   |   |   |-- CONGELATEUR_ALARME_PANNE  ->  Congelateur_alarme_panne/
|   |   |   |   `-- CONGELATEUR_ALARME_PANNE.md  ->  Congelateur_alarme_panne.md
|   |   |   `-- CONGELATEUR_ALARME_PORTE  ->  Congelateur_alarme_porte/
|   |   |       `-- CONGELATEUR_ALARME_PORTE.md  ->  Congelateur_alarme_porte.md
|   |   |-- P2_PRISES  ->  P2_Prises/
|   |   |-- P2_éCO. Prises  ->  P2_Éco. prises/
|   |   |   |-- ECO_PRISES_DYNAMIQUE  ->  Eco_prises_dynamique/
|   |   |   |   `-- ECO_PRISES_DYNAMIQUE.md  ->  Eco_prises_dynamique.md
|   |   |   |-- GESTION_PC_BUREAU  ->  Gestion_pc_bureau/
|   |   |   |   `-- GESTION_PC_BUREAU.md  ->  Gestion_pc_bureau.md
|   |   |   `-- GESTION_TV_CHAMBRE  ->  Gestion_tv_chambre/
|   |   |       `-- GESTION_TV_CHAMBRE.md  ->  Gestion_tv_chambre.md
|   |   |-- P3_Eclairage/
|   |   |   |-- ALLUMAGE_LUMIERE_ENTREE  ->  Allumage_lumiere_entree/
|   |   |   |   `-- ALLUMAGE_LUMIERE_ENTREE.md  ->  Allumage_lumiere_entree.md
|   |   |   |-- BUREAU_ACTIVATION_ECRAN_SYNCHRO  ->  Bureau_activation_ecran_synchro/
|   |   |   |   `-- BUREAU_ACTIVATION_ECRAN_SYNCHRO.md  ->  Bureau_activation_ecran_synchro.md
|   |   |   |-- BUREAU_FORCER_PLAY_ON  ->  Bureau_forcer_play_on/
|   |   |   |   `-- BUREAU_FORCER_PLAY_ON.md  ->  Bureau_forcer_play_on.md
|   |   |   |-- BUREAU_RODRET_TOGGLE_BLANCHES  ->  Bureau_rodret_toggle_blanches/
|   |   |   |   `-- BUREAU_RODRET_TOGGLE_BLANCHES.md  ->  Bureau_rodret_toggle_blanches.md
|   |   |   |-- BUREAU_WATCHDOG_SYNCHRO_LAMPES  ->  Bureau_watchdog_synchro_lampes/
|   |   |   |   `-- BUREAU_WATCHDOG_SYNCHRO_LAMPES.md  ->  Bureau_watchdog_synchro_lampes.md
|   |   |   `-- SDB_SYNC_MIROIR_LAMPE_ET_RELAIS_SDB  ->  Sdb_sync_miroir_lampe_et_relais_sdb/
|   |   |       `-- SDB_SYNC_MIROIR_LAMPE_ET_RELAIS_SDB.md  ->  Sdb_sync_miroir_lampe_et_relais_sdb.md
|   |   |-- RASPI  ->  Raspi/
|   |   |   `-- RPi4_FAN_PWM  ->  Rpi4_fan_pwm/
|   |   |       `-- RPi4_FAN_PWM.md  ->  Rpi4_fan_pwm.md
|   |   |-- Tarif HC-HP  ->  Tarif hc-hp/
|   |   |   `-- BASCULEMENT_TARIF_HPHC  ->  Basculement_tarif_hphc/
|   |   |       `-- BASCULEMENT_TARIF_HPHC.md  ->  Basculement_tarif_hphc.md
|   |   `-- Watchdog Piles (HUE-IKEA-SONOFF)  ->  Watchdog piles (hue-ikea-sonoff)/
|   |       `-- WATCHDOG_PILES  ->  Watchdog_piles/
|   |           `-- WATCHDOG_PILES.md  ->  Watchdog_piles.md
|   |-- docs_automations_YAML  ->  Docs_automations_yaml/
|   |   |-- _SANS_CATEGORIE  ->  _Sans_categorie/
|   |   |   |-- P4_log_zones_eric  ->  P4_Log_zones_eric/
|   |   |   |   `-- P4_log_zones_eric.yaml  ->  P4_Log_zones_eric.yaml
|   |   |   `-- veille_github_nouvelle_release_detectee  ->  Veille_github_nouvelle_release_detectee/
|   |   |       `-- veille_github_nouvelle_release_detectee.yaml  ->  Veille_github_nouvelle_release_detectee.yaml
|   |   |-- AUTOMATIONS.YALM ORIGINAL  ->  Automations.yalm original/
|   |   |   `-- automations.yaml  ->  Automations.yaml
|   |   |-- Backup HA - GitHub  ->  Backup ha - github/
|   |   |   |-- 00_backup_alerte_si_ko_15_min  ->  00_Backup_alerte_si_ko_15_min/
|   |   |   |   `-- 00_backup_alerte_si_ko_15_min.yaml  ->  00_Backup_alerte_si_ko_15_min.yaml
|   |   |   |-- 01_backup_git_hourly_h_10  ->  01_Backup_git_hourly_h_10/
|   |   |   |   `-- 01_backup_git_hourly_h_10.yaml  ->  01_Backup_git_hourly_h_10.yaml
|   |   |   |-- 02_backup_git_daily_03_00  ->  02_Backup_git_daily_03_00/
|   |   |   |   `-- 02_backup_git_daily_03_00.yaml  ->  02_Backup_git_daily_03_00.yaml
|   |   |   |-- 03_backup_git_weekly_dim_01_30  ->  03_Backup_git_weekly_dim_01_30/
|   |   |   |   `-- 03_backup_git_weekly_dim_01_30.yaml  ->  03_Backup_git_weekly_dim_01_30.yaml
|   |   |   |-- 04_backup_git_push_manuel  ->  04_Backup_git_push_manuel/
|   |   |   |   `-- 04_backup_git_push_manuel.yaml  ->  04_Backup_git_push_manuel.yaml
|   |   |   |-- 05_backup_git_push_weekly_manuel  ->  05_Backup_git_push_weekly_manuel/
|   |   |   |   `-- 05_backup_git_push_weekly_manuel.yaml  ->  05_Backup_git_push_weekly_manuel.yaml
|   |   |   `-- git_push_au_demarrage_ha  ->  Git_push_au_demarrage_ha/
|   |   |       `-- git_push_au_demarrage_ha.yaml  ->  Git_push_au_demarrage_ha.yaml
|   |   |-- Bouton Virtuel  ->  Bouton virtuel/
|   |   |   |-- p3_salon_bouton_ikea_inter_salon  ->  P3_Salon_bouton_ikea_inter_salon/
|   |   |   |   `-- p3_salon_bouton_ikea_inter_salon.yaml  ->  P3_Salon_bouton_ikea_inter_salon.yaml
|   |   |   `-- p3_salon_bouton_ikea_somrig  ->  P3_Salon_bouton_ikea_somrig/
|   |   |       `-- p3_salon_bouton_ikea_somrig.yaml  ->  P3_Salon_bouton_ikea_somrig.yaml
|   |   |-- Contrôle Entity z2m  ->  Contrôle entity z2m/
|   |   |   `-- z2m_last_seen  ->  Z2m_last_seen/
|   |   |       `-- z2m_last_seen.yaml  ->  Z2m_last_seen.yaml
|   |   |-- Gestion des Stores  ->  Gestion des stores/
|   |   |   |-- gestion_optimisee_du_store_bureau  ->  Gestion_optimisee_du_store_bureau/
|   |   |   |   `-- gestion_optimisee_du_store_bureau.yaml  ->  Gestion_optimisee_du_store_bureau.yaml
|   |   |   `-- gestion_simple_du_store_salon_matin_soir  ->  Gestion_simple_du_store_salon_matin_soir/
|   |   |       `-- gestion_simple_du_store_salon_matin_soir.yaml  ->  Gestion_simple_du_store_salon_matin_soir.yaml
|   |   |-- MariaDB & VSCode Optimisation  ->  Mariadb & vscode optimisation/
|   |   |   |-- db_purge_mariadb_repack  ->  Db_purge_mariadb_repack/
|   |   |   |   `-- db_purge_mariadb_repack.yaml  ->  Db_purge_mariadb_repack.yaml
|   |   |   `-- systeme_economie_energie_vs_code  ->  Systeme_economie_energie_vs_code/
|   |   |       `-- systeme_economie_energie_vs_code.yaml  ->  Systeme_economie_energie_vs_code.yaml
|   |   |-- Météo/
|   |   |   |-- alerte_meteo_france_actualisation_des_cartes  ->  Alerte_meteo_france_actualisation_des_cartes/
|   |   |   |   `-- alerte_meteo_france_actualisation_des_cartes.yaml  ->  Alerte_meteo_france_actualisation_des_cartes.yaml
|   |   |   |-- mettre_a_jour_le_temps_du_dernier_impact_de_foudre  ->  Mettre_a_jour_le_temps_du_dernier_impact_de_foudre/
|   |   |   |   `-- mettre_a_jour_le_temps_du_dernier_impact_de_foudre.yaml  ->  Mettre_a_jour_le_temps_du_dernier_impact_de_foudre.yaml
|   |   |   |-- notification_de_la_foudre  ->  Notification_de_la_foudre/
|   |   |   |   `-- notification_de_la_foudre.yaml  ->  Notification_de_la_foudre.yaml
|   |   |   |-- update_previous_humidity  ->  Update_previous_humidity/
|   |   |   |   `-- update_previous_humidity.yaml  ->  Update_previous_humidity.yaml
|   |   |   `-- update_previous_temperature  ->  Update_previous_temperature/
|   |   |       `-- update_previous_temperature.yaml  ->  Update_previous_temperature.yaml
|   |   |-- P0_ENRIGE  ->  P0_Enrige/
|   |   |   |-- diag_enregistrement_journalier  ->  Diag_enregistrement_journalier/
|   |   |   |   `-- diag_enregistrement_journalier.yaml  ->  Diag_enregistrement_journalier.yaml
|   |   |   |-- histo_linky_quotidien  ->  Histo_linky_quotidien/
|   |   |   |   `-- histo_linky_quotidien.yaml  ->  Histo_linky_quotidien.yaml
|   |   |   |-- histo_nodon_quotidien  ->  Histo_nodon_quotidien/
|   |   |   |   `-- histo_nodon_quotidien.yaml  ->  Histo_nodon_quotidien.yaml
|   |   |   |-- log_ecart_linky_vs_nodon  ->  Log_ecart_linky_vs_nodon/
|   |   |   |   `-- log_ecart_linky_vs_nodon.yaml  ->  Log_ecart_linky_vs_nodon.yaml
|   |   |   |-- rattrapage_linky_ecart  ->  Rattrapage_linky_ecart/
|   |   |   |   `-- rattrapage_linky_ecart.yaml  ->  Rattrapage_linky_ecart.yaml
|   |   |   `-- rattrapage_linky_j2_ecart  ->  Rattrapage_linky_j2_ecart/
|   |   |       `-- rattrapage_linky_j2_ecart.yaml  ->  Rattrapage_linky_j2_ecart.yaml
|   |   |-- P1_01_CLIM_CHAUFFAGE  ->  P1_01_Clim_chauffage/
|   |   |   |-- a_0_2026_01_11_automatisation_clim_jour_07h30_21h00  ->  A_0_2026_01_11_automatisation_clim_jour_07h30_21h00/
|   |   |   |   `-- a_0_2026_01_11_automatisation_clim_jour_07h30_21h00.yaml  ->  A_0_2026_01_11_automatisation_clim_jour_07h30_21h00.yaml
|   |   |   |-- b_0_2026_01_11_automatisation_clim_nuit_21h00_07h30  ->  B_0_2026_01_11_automatisation_clim_nuit_21h00_07h30/
|   |   |   |   `-- b_0_2026_01_11_automatisation_clim_nuit_21h00_07h30.yaml  ->  B_0_2026_01_11_automatisation_clim_nuit_21h00_07h30.yaml
|   |   |   |-- c_notification_temperature_up_ou_down_7h30_21h00  ->  C_notification_temperature_up_ou_down_7h30_21h00/
|   |   |   |   `-- c_notification_temperature_up_ou_down_7h30_21h00.yaml  ->  C_notification_temperature_up_ou_down_7h30_21h00.yaml
|   |   |   |-- d_notification_temperature_up_ou_down_21h00_7h30  ->  D_notification_temperature_up_ou_down_21h00_7h30/
|   |   |   |   `-- d_notification_temperature_up_ou_down_21h00_7h30.yaml  ->  D_notification_temperature_up_ou_down_21h00_7h30.yaml
|   |   |   |-- e_clim_notification_de_fermeture_des_fenetres  ->  E_clim_notification_de_fermeture_des_fenetres/
|   |   |   |   `-- e_clim_notification_de_fermeture_des_fenetres.yaml  ->  E_clim_notification_de_fermeture_des_fenetres.yaml
|   |   |   |-- f_clim_automatisation_arret_clim_notification  ->  F_clim_automatisation_arret_clim_notification/
|   |   |   |   `-- f_clim_automatisation_arret_clim_notification.yaml  ->  F_clim_automatisation_arret_clim_notification.yaml
|   |   |   |-- g_clim_notification_de_changement_de_mode_ete_fan_hiver  ->  G_clim_notification_de_changement_de_mode_ete_fan_hiver/
|   |   |   |   `-- g_clim_notification_de_changement_de_mode_ete_fan_hiver.yaml  ->  G_clim_notification_de_changement_de_mode_ete_fan_hiver.yaml
|   |   |   |-- h_clim_debug_force_mode_correct_securite  ->  H_clim_debug_force_mode_correct_securite/
|   |   |   |   `-- h_clim_debug_force_mode_correct_securite.yaml  ->  H_clim_debug_force_mode_correct_securite.yaml
|   |   |   |-- i_synchro_notif_clim_si_prise_coupee  ->  I_synchro_notif_clim_si_prise_coupee/
|   |   |   |   `-- i_synchro_notif_clim_si_prise_coupee.yaml  ->  I_synchro_notif_clim_si_prise_coupee.yaml
|   |   |   |-- j_debug_notifier_les_changements_de_message_clim_mobile  ->  J_debug_notifier_les_changements_de_message_clim_mobile/
|   |   |   |   `-- j_debug_notifier_les_changements_de_message_clim_mobile.yaml  ->  J_debug_notifier_les_changements_de_message_clim_mobile.yaml
|   |   |   `-- ... 2 element(s) inchange(s) non liste(s)
|   |   |-- P1_02_Cuisine/
|   |   |   |-- a_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9  ->  A_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9/
|   |   |   |   `-- a_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9.yaml  ->  A_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9.yaml
|   |   |   `-- b_chauffage_cuisine_vacances  ->  B_chauffage_cuisine_vacances/
|   |   |       `-- b_chauffage_cuisine_vacances.yaml  ->  B_chauffage_cuisine_vacances.yaml
|   |   |-- P1_03_Chauffage Salle de Bain  ->  P1_03_Chauffage salle de bain/
|   |   |   |-- a_soufflant_sdb_bouton_rodret  ->  A_soufflant_sdb_bouton_rodret/
|   |   |   |   `-- a_soufflant_sdb_bouton_rodret.yaml  ->  A_soufflant_sdb_bouton_rodret.yaml
|   |   |   |-- b_soufflant_sdb_routage  ->  B_soufflant_sdb_routage/
|   |   |   |   `-- b_soufflant_sdb_routage.yaml  ->  B_soufflant_sdb_routage.yaml
|   |   |   |-- c_salle_de_bain_watchdog_securite_soufflant  ->  C_salle_de_bain_watchdog_securite_soufflant/
|   |   |   |   `-- c_salle_de_bain_watchdog_securite_soufflant.yaml  ->  C_salle_de_bain_watchdog_securite_soufflant.yaml
|   |   |   |-- d_sdb_soufflant_decompte_60min_timer  ->  D_sdb_soufflant_decompte_60min_timer/
|   |   |   |   `-- d_sdb_soufflant_decompte_60min_timer.yaml  ->  D_sdb_soufflant_decompte_60min_timer.yaml
|   |   |   |-- e_sdb_soufflant_rattrapage_demarrage_ha_timer  ->  E_sdb_soufflant_rattrapage_demarrage_ha_timer/
|   |   |   |   `-- e_sdb_soufflant_rattrapage_demarrage_ha_timer.yaml  ->  E_sdb_soufflant_rattrapage_demarrage_ha_timer.yaml
|   |   |   |-- f_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h  ->  F_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h/
|   |   |   |   `-- f_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h.yaml  ->  F_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h.yaml
|   |   |   |-- g_sdb_seche_serviettes_decompte_2h_timer  ->  G_sdb_seche_serviettes_decompte_2h_timer/
|   |   |   |   `-- g_sdb_seche_serviettes_decompte_2h_timer.yaml  ->  G_sdb_seche_serviettes_decompte_2h_timer.yaml
|   |   |   |-- h_sdb_seche_serviettes_rattrapage_demarrage_ha_timer  ->  H_sdb_seche_serviettes_rattrapage_demarrage_ha_timer/
|   |   |   |   `-- h_sdb_seche_serviettes_rattrapage_demarrage_ha_timer.yaml  ->  H_sdb_seche_serviettes_rattrapage_demarrage_ha_timer.yaml
|   |   |   |-- rodret_soufflant_sdb  ->  Rodret_soufflant_sdb/
|   |   |   `-- z_2026_02_01_salle_de_bain_gestion_intelligente_soufflant  ->  Z_2026_02_01_salle_de_bain_gestion_intelligente_soufflant/
|   |   |       `-- z_2026_02_01_salle_de_bain_gestion_intelligente_soufflant.yaml  ->  Z_2026_02_01_salle_de_bain_gestion_intelligente_soufflant.yaml
|   |   |-- P2_Alarme_Congélateur  ->  P2_Alarme_congélateur/
|   |   |   |-- congelateur_alarme_capteur  ->  Congelateur_alarme_capteur/
|   |   |   |   `-- congelateur_alarme_capteur.yaml  ->  Congelateur_alarme_capteur.yaml
|   |   |   |-- congelateur_alarme_panne  ->  Congelateur_alarme_panne/
|   |   |   |   `-- congelateur_alarme_panne.yaml  ->  Congelateur_alarme_panne.yaml
|   |   |   `-- congelateur_alarme_porte  ->  Congelateur_alarme_porte/
|   |   |       `-- congelateur_alarme_porte.yaml  ->  Congelateur_alarme_porte.yaml
|   |   |-- P2_éCO. Prises  ->  P2_Éco. prises/
|   |   |   |-- eco_prises_dynamique_by_presence_groupe  ->  Eco_prises_dynamique_by_presence_groupe/
|   |   |   |   `-- eco_prises_dynamique_by_presence_groupe.yaml  ->  Eco_prises_dynamique_by_presence_groupe.yaml
|   |   |   |-- gestion_pc_bureau_scene_de_fin_notif  ->  Gestion_pc_bureau_scene_de_fin_notif/
|   |   |   |   `-- gestion_pc_bureau_scene_de_fin_notif.yaml  ->  Gestion_pc_bureau_scene_de_fin_notif.yaml
|   |   |   `-- gestion_tv_chambre_scene_de_fin_notif  ->  Gestion_tv_chambre_scene_de_fin_notif/
|   |   |       `-- gestion_tv_chambre_scene_de_fin_notif.yaml  ->  Gestion_tv_chambre_scene_de_fin_notif.yaml
|   |   |-- P3_Eclairage/
|   |   |   |-- p3_bureau_activation_ecran_synchro  ->  P3_Bureau_activation_ecran_synchro/
|   |   |   |   `-- p3_bureau_activation_ecran_synchro.yaml  ->  P3_Bureau_activation_ecran_synchro.yaml
|   |   |   |-- p3_bureau_bouton_rodret_toggle_blanches  ->  P3_Bureau_bouton_rodret_toggle_blanches/
|   |   |   |   `-- p3_bureau_bouton_rodret_toggle_blanches.yaml  ->  P3_Bureau_bouton_rodret_toggle_blanches.yaml
|   |   |   |-- p3_bureau_forcer_play_on_si_pc_tourne  ->  P3_Bureau_forcer_play_on_si_pc_tourne/
|   |   |   |   `-- p3_bureau_forcer_play_on_si_pc_tourne.yaml  ->  P3_Bureau_forcer_play_on_si_pc_tourne.yaml
|   |   |   |-- p3_bureau_watchdog_synchronisation_lampes_blanches  ->  P3_Bureau_watchdog_synchronisation_lampes_blanches/
|   |   |   |   `-- p3_bureau_watchdog_synchronisation_lampes_blanches.yaml  ->  P3_Bureau_watchdog_synchronisation_lampes_blanches.yaml
|   |   |   |-- p3_entree_allumage_lumiere  ->  P3_Entree_allumage_lumiere/
|   |   |   |   `-- p3_entree_allumage_lumiere.yaml  ->  P3_Entree_allumage_lumiere.yaml
|   |   |   `-- p3_sdb_sync_miroir_lampe_et_relais_sdb  ->  P3_Sdb_sync_miroir_lampe_et_relais_sdb/
|   |   |       `-- p3_sdb_sync_miroir_lampe_et_relais_sdb.yaml  ->  P3_Sdb_sync_miroir_lampe_et_relais_sdb.yaml
|   |   |-- RASPI  ->  Raspi/
|   |   |   `-- ... 1 element(s) inchange(s) non liste(s)
|   |   |-- Tarif HC-HP  ->  Tarif hc-hp/
|   |   |   `-- auto_energie_basculement_tarif_hc_hp_genelec_appart  ->  Auto_energie_basculement_tarif_hc_hp_genelec_appart/
|   |   |       `-- auto_energie_basculement_tarif_hc_hp_genelec_appart.yaml  ->  Auto_energie_basculement_tarif_hc_hp_genelec_appart.yaml
|   |   `-- Watchdog Piles (HUE-IKEA-SONOFF)  ->  Watchdog piles (hue-ikea-sonoff)/
|   |       `-- systeme_watchdog_piles_hue_ikea_sonoff  ->  Systeme_watchdog_piles_hue_ikea_sonoff/
|   |           `-- systeme_watchdog_piles_hue_ikea_sonoff.yaml  ->  Systeme_watchdog_piles_hue_ikea_sonoff.yaml
|   `-- ... 1 element(s) inchange(s) non liste(s)
|-- 04_docs_scripts  ->  04_Docs_scripts/
|   |-- DOCS_SCRIPT_ORIGINAL  ->  Docs_script_original/
|   |-- docs_scripts_SH  ->  Docs_scripts_sh/
|   |   |-- audit_md5  ->  Audit_md5/
|   |   |   `-- audit_md5.sh  ->  Audit_md5.sh
|   |   |-- audit_md5_md_yaml  ->  Audit_md5_md_yaml/
|   |   |   `-- audit_md5_md_yaml.sh  ->  Audit_md5_md_yaml.sh
|   |   |-- audit_md5_yaml  ->  Audit_md5_yaml/
|   |   |   `-- audit_md5_yaml.sh  ->  Audit_md5_yaml.sh
|   |   |-- check_global_index  ->  Check_global_index/
|   |   |   `-- check_global_index.py  ->  Check_global_index.py
|   |   |-- check_sous_context_ia  ->  Check_sous_context_ia/
|   |   |   |-- __pycache__  ->  __Pycache__/
|   |   |   |   `-- check_sous_context_ia.cpython-314.pyc  ->  Check_sous_context_ia.cpython-314.pyc
|   |   |   `-- check_sous_context_ia.py  ->  Check_sous_context_ia.py
|   |   |-- gen_global_index_automations  ->  Gen_global_index_automations/
|   |   |   `-- gen_global_index_automations.py  ->  Gen_global_index_automations.py
|   |   |-- gen_global_index_ia  ->  Gen_global_index_ia/
|   |   |   `-- gen_global_index_ia.py  ->  Gen_global_index_ia.py
|   |   |-- gen_global_index_scripts  ->  Gen_global_index_scripts/
|   |   |   `-- gen_global_index_scripts.py  ->  Gen_global_index_scripts.py
|   |   |-- gen_global_index_vignettes_pages  ->  Gen_global_index_vignettes_pages/
|   |   |   `-- gen_global_index_vignettes_pages.py  ->  Gen_global_index_vignettes_pages.py
|   |   |-- ha_git_backup  ->  Ha_git_backup/
|   |   |   `-- ha_git_backup.sh  ->  Ha_git_backup.sh
|   |   |-- hermes_audit_md5_docs  ->  Hermes_audit_md5_docs/
|   |   |   `-- hermes_audit_md5_docs.sh  ->  Hermes_audit_md5_docs.sh
|   |   |-- hermes_audit_md5_trigul_3md  ->  Hermes_audit_md5_trigul_3md/
|   |   |   |-- hermes_audit_md5_trigul_3md.sh  ->  Hermes_audit_md5_trigul_3md.sh
|   |   |   `-- hermes_audit_md5_trigul_unitaire.py  ->  Hermes_audit_md5_trigul_unitaire.py
|   |   |-- mf_vigilance_images  ->  Mf_vigilance_images/
|   |   |   `-- mf_vigilance_images.sh  ->  Mf_vigilance_images.sh
|   |   `-- MP_01_monitor_temp.sh - save pour RASPI  ->  Mp_01_monitor_temp.sh - save pour raspi/
|   |       `-- #MP_01_monitor_temp.sh.#  ->  #Mp_01_monitor_temp.sh.#
|   |-- docs_scripts_SH_MD  ->  Docs_scripts_sh_md/
|   |   |-- AUDIT_MD5  ->  Audit_md5/
|   |   |   `-- AUDIT_MD5.md  ->  Audit_md5.md
|   |   |-- AUDIT_MD5_DOCS  ->  Audit_md5_docs/
|   |   |   `-- AUDIT_MD5_DOCS.md  ->  Audit_md5_docs.md
|   |   `-- HA_GIT_BACKUP  ->  Ha_git_backup/
|   |       `-- HA_GIT_BACKUP.md  ->  Ha_git_backup.md
|   |-- docs_scripts_YAML  ->  Docs_scripts_yaml/
|   |   |-- audit_md5  ->  Audit_md5/
|   |   |   `-- audit_md5.yaml  ->  Audit_md5.yaml
|   |   |-- audit_md5_md_yaml  ->  Audit_md5_md_yaml/
|   |   |   `-- audit_md5_md_yaml.yaml  ->  Audit_md5_md_yaml.yaml
|   |   |-- check_yaml_forme  ->  Check_yaml_forme/
|   |   |   `-- check_yaml_forme.py  ->  Check_yaml_forme.py
|   |   |-- Climatisation/
|   |   |   |-- j_1_1_salon_clim_on_off_intelligent  ->  J_1_1_salon_clim_on_off_intelligent/
|   |   |   |   `-- j_1_1_salon_clim_on_off_intelligent.yaml  ->  J_1_1_salon_clim_on_off_intelligent.yaml
|   |   |   |-- j_1_2_bureau_clim_on_off_intelligent  ->  J_1_2_bureau_clim_on_off_intelligent/
|   |   |   |   `-- j_1_2_bureau_clim_on_off_intelligent.yaml  ->  J_1_2_bureau_clim_on_off_intelligent.yaml
|   |   |   |-- j_1_3_chambre_clim_on_off_intelligent  ->  J_1_3_chambre_clim_on_off_intelligent/
|   |   |   |   `-- j_1_3_chambre_clim_on_off_intelligent.yaml  ->  J_1_3_chambre_clim_on_off_intelligent.yaml
|   |   |   |-- j_2_0_secu_arret_clim_protege  ->  J_2_0_secu_arret_clim_protege/
|   |   |   |   `-- j_2_0_secu_arret_clim_protege.yaml  ->  J_2_0_secu_arret_clim_protege.yaml
|   |   |   `-- p1_master_gestion_clim  ->  P1_Master_gestion_clim/
|   |   |       `-- p1_master_gestion_clim.yaml  ->  P1_Master_gestion_clim.yaml
|   |   |-- correct_linky  ->  Correct_linky/
|   |   |   `-- correct_linky.py  ->  Correct_linky.py
|   |   `-- Soufflant SDB  ->  Soufflant sdb/
|   |       |-- sdb_soufflant_arreter  ->  Sdb_soufflant_arreter/
|   |       |   `-- sdb_soufflant_arreter.yaml  ->  Sdb_soufflant_arreter.yaml
|   |       `-- sdb_soufflant_demarrer  ->  Sdb_soufflant_demarrer/
|   |           `-- sdb_soufflant_demarrer.yaml  ->  Sdb_soufflant_demarrer.yaml
|   |-- docs_scripts_YAML_MD  ->  Docs_scripts_yaml_md/
|   |   |-- P1_MASTER_GESTION_CLIM  ->  P1_Master_gestion_clim/
|   |   |   `-- P1_MASTER_GESTION_CLIM.md  ->  P1_Master_gestion_clim.md
|   |   |-- SCRIPT_J2_0_SECU_ARRET_CLIM  ->  Script_j2_0_secu_arret_clim/
|   |   |   `-- SCRIPT_J2_0_SECU_ARRET_CLIM.md  ->  Script_j2_0_secu_arret_clim.md
|   |   `-- SCRIPTS_CLIM_ON_OFF  ->  Scripts_clim_on_off/
|   |       `-- SCRIPTS_CLIM_ON_OFF.md  ->  Scripts_clim_on_off.md
|   `-- ... 2 element(s) inchange(s) non liste(s)
|-- 05_docs_MD_system/
|   |-- CONFIG_ROOT  ->  Config_root/
|   |   `-- CONFIG_ROOT.md  ->  Config_root.md
|   |-- matrisse_template_doc  ->  Matrisse_template_doc/
|   |   `-- _TEMPLATE_DOC.md  ->  _Template_doc.md
|   `-- ... 4 element(s) inchange(s) non liste(s)
|-- 05_docs_skills  ->  05_Docs_skills/
|   |-- skill_fix-file  ->  Skill_fix-file/
|   |   `-- fix-file.md  ->  Fix-file.md
|   |-- skill_ha-new-yaml  ->  Skill_ha-new-yaml/
|   |   `-- ha-new-yaml.md  ->  Ha-new-yaml.md
|   |-- skill_ha-push-docs  ->  Skill_ha-push-docs/
|   |   `-- ha-push-docs.md  ->  Ha-push-docs.md
|   |-- skill_ha-push-md  ->  Skill_ha-push-md/
|   |   `-- ha-push-md.md  ->  Ha-push-md.md
|   |-- skill_ha-push-yaml  ->  Skill_ha-push-yaml/
|   |   `-- ha-push-yaml.md  ->  Ha-push-yaml.md
|   |-- skill_ha-resync-docs  ->  Skill_ha-resync-docs/
|   |   `-- ha-resync-docs.md  ->  Ha-resync-docs.md
|   |-- skill_ha-resync-tree  ->  Skill_ha-resync-tree/
|   |   `-- ha-resync-tree.md  ->  Ha-resync-tree.md
|   |-- skill_ha-status  ->  Skill_ha-status/
|   |   `-- ha-status.md  ->  Ha-status.md
|   |-- skill_ha-trigul  ->  Skill_ha-trigul/
|   |   `-- ha-trigul.md  ->  Ha-trigul.md
|   |-- skill_histo  ->  Skill_histo/
|   |   `-- histo.md  ->  Histo.md
|   |-- skill_histo-final  ->  Skill_histo-final/
|   |   `-- histo-final.md  ->  Histo-final.md
|   |-- skill_journal-modifs  ->  Skill_journal-modifs/
|   |   `-- journal-modifs.md  ->  Journal-modifs.md
|   |-- skill_sync-index  ->  Skill_sync-index/
|   |   `-- sync-index.md  ->  Sync-index.md
|   `-- skill_update-arbo  ->  Skill_update-arbo/
|       `-- update-arbo.md  ->  Update-arbo.md
|-- 06_docs_technique  ->  06_Docs_technique/
|   `-- 01_pont_hue_hacking  ->  01_Pont_hue_hacking/
|       `-- 01_pont_hue_hacking.md  ->  01_Pont_hue_hacking.md
`-- ... 1 element(s) inchange(s) non liste(s)
```

## Entrees volontairement inchangees (hors systeme)

### 00_IA / IA_CONTEXT_BASE (1)
- `00_IA/`

### 05_docs_MD_system (1)
- `05_docs_MD_system/`

### COULEURS_PRISES_PAR_PIECE (1)
- `02_docs_dashboard/dashboard_docs_MD/L2C1_ENERGIE/COULEURS_PRISES_PAR_PIECE.md`

### DEPENDANCES_GLOBALES (7)
- `05_docs_MD_system/DEPENDANCES_GLOBALES/`
- `05_docs_MD_system/DEPENDANCES_GLOBALES/DEPENDANCES_GLOBALES.md`
- `05_docs_MD_system/DEPENDANCES_GLOBALES/DEPENDANCES_GLOBALES_archive_2026-09-28.md`
- `05_docs_MD_system/DEPENDANCES_GLOBALES/DEPENDANCES_GLOBALES_archive_2026-10-07_18h13.md`
- `05_docs_MD_system/DEPENDANCES_GLOBALES/DEPENDANCES_GLOBALES_archive_2026-10-07_19h20.md`
- `05_docs_MD_system/DEPENDANCES_GLOBALES_HERMES/`
- `05_docs_MD_system/DEPENDANCES_GLOBALES_HERMES/DEPENDANCES_GLOBALES_HERMES_V1.md`

### Dashboard_COMPLET (1)
- `02_docs_dashboard/dashboard_docs_YAML/Dashboard_COMPLET/`

### GLOBAL_INDEX (9)
- `00_IA/GLOBAL_INDEX_IA.md`
- `02_docs_dashboard/GLOBAL_INDEX_VIGNETTES_PAGES.md`
- `03_docs_automations/GLOBAL_INDEX_AUTOMATIONS.md`
- `04_docs_scripts/GLOBAL_INDEX_SCRIPTS_SH.md`
- `04_docs_scripts/GLOBAL_INDEX_SCRIPTS_YAML.md`
- `05_docs_MD_system/ENTITES_GLOBAL_INDEX/`
- `05_docs_MD_system/ENTITES_GLOBAL_INDEX/ENTITES_GLOBAL_INDEX.md`
- `05_docs_MD_system/GLOBAL_INDEX_REPO/`
- `05_docs_MD_system/GLOBAL_INDEX_REPO/GLOBAL_INDEX_REPO.md`

### IA_* (20)
- `00_IA/IA_CONTEXT_BASE/`
- `00_IA/IA_CONTEXT_BASE/IA_CONTEXT_BASE.md`
- `00_IA/sous_context_ia/IA_ARBO_DETAIL/`
- `00_IA/sous_context_ia/IA_ARBO_DETAIL/IA_ARBO_DETAIL.md`
- `00_IA/sous_context_ia/IA_AUDIT_ENERGETIQUE_ET_THERMIQUE/`
- `00_IA/sous_context_ia/IA_AUDIT_ENERGETIQUE_ET_THERMIQUE/IA_AUDIT_ENERGETIQUE_ET_THERMIQUE.md`
- `00_IA/sous_context_ia/IA_AUTOMATIONS_NOTIFS/`
- `00_IA/sous_context_ia/IA_AUTOMATIONS_NOTIFS/IA_AUTOMATIONS_NOTIFS.md`
- `00_IA/sous_context_ia/IA_CMD_TERMINAL_HA/`
- `00_IA/sous_context_ia/IA_CMD_TERMINAL_HA/IA_CMD_TERMINAL_HA.md`
- `00_IA/sous_context_ia/IA_INDEX_AUTOMATIONS/`
- `00_IA/sous_context_ia/IA_INDEX_AUTOMATIONS/IA_INDEX_AUTOMATIONS.md`
- `00_IA/sous_context_ia/IA_INDEX_NAVIGATION/`
- `00_IA/sous_context_ia/IA_INDEX_NAVIGATION/IA_INDEX_NAVIGATION.md`
- `00_IA/sous_context_ia/IA_INTEGRATIONS_CARTES/`
- `00_IA/sous_context_ia/IA_INTEGRATIONS_CARTES/IA_INTEGRATIONS_CARTES.md`
- `00_IA/sous_context_ia/IA_P4_PRESENCE/`
- `00_IA/sous_context_ia/IA_P4_PRESENCE/IA_P4_PRESENCE.md`
- `00_IA/sous_context_ia/IA_SKILLS_INVENTAIRE/`
- `00_IA/sous_context_ia/IA_SKILLS_INVENTAIRE/IA_SKILLS_INVENTAIRE.md`

### LXCX (vignette) (99)
- `02_docs_dashboard/dashboard_docs_MD/L0C0_PAGE_Home/`
- `02_docs_dashboard/dashboard_docs_MD/L1C1_METEO/`
- `02_docs_dashboard/dashboard_docs_MD/L1C1_METEO/01_vignette/L1C1_VIGNETTE_METEO.md`
- `02_docs_dashboard/dashboard_docs_MD/L1C2_TEMPERATURES/`
- `02_docs_dashboard/dashboard_docs_MD/L1C2_TEMPERATURES/01_vignette/L1C2_VIGNETTE_TEMPERATURES.md`
- `02_docs_dashboard/dashboard_docs_MD/L1C3_CLIM/`
- `02_docs_dashboard/dashboard_docs_MD/L1C3_CLIM/01_vignette/L1C3_VIGNETTE_CLIM.md`
- `02_docs_dashboard/dashboard_docs_MD/L2C1_ENERGIE/`
- `02_docs_dashboard/dashboard_docs_MD/L2C1_ENERGIE/01_vignette/L2C1_VIGNETTE_ENERGIE.md`
- `02_docs_dashboard/dashboard_docs_MD/L2C2_ENERGIE_CLIM/`
- `02_docs_dashboard/dashboard_docs_MD/L2C2_ENERGIE_CLIM/01_vignette/L2C2_VIGNETTE_ENERGIE_CLIM.md`
- `02_docs_dashboard/dashboard_docs_MD/L2C3_ENERGIE_ECLAIRAGE/`
- `02_docs_dashboard/dashboard_docs_MD/L2C3_ENERGIE_ECLAIRAGE/01_vignette/L2C3_VIGNETTE_ECLAIRAGE.md`
- `02_docs_dashboard/dashboard_docs_MD/L3C1_ECLAIRAGE/`
- `02_docs_dashboard/dashboard_docs_MD/L3C1_ECLAIRAGE/01_vignette/L3C1_VIGNETTE_ECLAIRAGE.md`
- `02_docs_dashboard/dashboard_docs_MD/L3C2_PRISES/`
- `02_docs_dashboard/dashboard_docs_MD/L3C2_PRISES/01_vignette/L3C2_VIGNETTE_PRISES.md`
- `02_docs_dashboard/dashboard_docs_MD/L3C3_STORES/`
- `02_docs_dashboard/dashboard_docs_MD/L3C3_STORES/01_vignette/L3C3_VIGNETTE_STORES.md`
- `02_docs_dashboard/dashboard_docs_MD/L4C1_MINI_PC/`
- `02_docs_dashboard/dashboard_docs_MD/L4C1_MINI_PC/01_vignette/L4C1_VIGNETTE_MINI_PC.md`
- `02_docs_dashboard/dashboard_docs_MD/L4C2_PROXMOX/`
- `02_docs_dashboard/dashboard_docs_MD/L4C2_PROXMOX/01_vignette/L4C2_VIGNETTE_PROXMOX.md`
- `02_docs_dashboard/dashboard_docs_MD/L4C3_MAJ_HA/`
- `02_docs_dashboard/dashboard_docs_MD/L4C3_MAJ_HA/01_vignette/L4C3_VIGNETTE_MAJ.md`
- `02_docs_dashboard/dashboard_docs_MD/L5C1_PILES_BATTERIES/`
- `02_docs_dashboard/dashboard_docs_MD/L5C1_PILES_BATTERIES/01_vignette/L5C1_VIGNETTE_BATTERIES.md`
- `02_docs_dashboard/dashboard_docs_MD/L5C2_BATTERIES_PORTABLES/`
- `02_docs_dashboard/dashboard_docs_MD/L5C2_BATTERIES_PORTABLES/01_vignette/L5C2_VIGNETTE_BATTERIES_PORTABLES.md`
- `02_docs_dashboard/dashboard_docs_MD/L5C3_MARIADB/`
- `02_docs_dashboard/dashboard_docs_MD/L5C3_MARIADB/01_vignette/L5C3_VIGNETTE_MARIADB.md`
- `02_docs_dashboard/dashboard_docs_MD/L5C3_MARIADB/03_page_reserve/PAGE_L5C3_SYSTEME_RESERVE.md`
- `02_docs_dashboard/dashboard_docs_MD/L6C1_AIR_QUALITE/`
- `02_docs_dashboard/dashboard_docs_MD/L6C1_AIR_QUALITE/01_vignette/L6C1_VIGNETTE_AIR_QUALITE.md`
- `02_docs_dashboard/dashboard_docs_MD/L6C2_POLLUTION_POLLEN/`
- `02_docs_dashboard/dashboard_docs_MD/L6C2_POLLUTION_POLLEN/01_vignette/L6C2_VIGNETTE_POLLUTION_POLLEN.md`
- `02_docs_dashboard/dashboard_docs_MD/L6C3_VIGIEAU/`
- `02_docs_dashboard/dashboard_docs_MD/L6C3_VIGIEAU/01_vignette/L6C3_VIGNETTE_VIGIEAU.md`
- `02_docs_dashboard/dashboard_docs_YAML/L0C0_PAGE_Home/`
- `02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/`
- `02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/01_vignette/vignette_L1C1_meteo.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/02_page/page_L1C1_meteo.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L1C2_02_Temperatures/`
- `02_docs_dashboard/dashboard_docs_YAML/L1C2_02_Temperatures/01_vignette/vignette_L1C2_temperatures.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L1C2_02_Temperatures/02_page/page_L1C2_temperatures.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/`
- `02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/01_vignette/vignette_L1C3_clim.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/02_page/page_L1C3_clim.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/`
- `02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/01_vignette/vignette_L2C1_energie.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/02_page_temps_reel/page_L2C1_energie_temps_reel.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/03_page_principale/page_L2C1_energie_principale.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/04_page_mensuel/page_L2C1_energie_mensuel.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L2C2_05_Energie_Clim/`
- `02_docs_dashboard/dashboard_docs_YAML/L2C2_05_Energie_Clim/01_vignette/vignette_L2C2_energie_clim.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L2C2_05_Energie_Clim/02_page/page_L2C2_energie_clim.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L2C3_06_Energie_Eclairage/`
- `02_docs_dashboard/dashboard_docs_YAML/L2C3_06_Energie_Eclairage/01_vignette/vignette_L2C3_energie_eclairage.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L2C3_06_Energie_Eclairage/02_page/page_L2C3_energie_eclairage.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/`
- `02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/01_vignette/vignette_L3C1_eclairage.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/02_page_gauche/page_L3C1_eclairage_gauche.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/03_page_droite/page_L3C1_eclairage_droite.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L3C2_08_Commandes_Prises/`
- `02_docs_dashboard/dashboard_docs_YAML/L3C2_08_Commandes_Prises/01_vignette/vignette_L3C2_prises.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L3C2_08_Commandes_Prises/02_page/page_L3C2_prises.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L3C3_09_Stores_Fenetres/`
- `02_docs_dashboard/dashboard_docs_YAML/L3C3_09_Stores_Fenetres/01_vignette/vignette_L3C3_stores.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L3C3_09_Stores_Fenetres/02_page/page_L3C3_stores.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Mini_PC/`
- `02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Mini_PC/01_vignette/vignette_L4C1_mini_pc.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Mini_PC/02_page/page_L4C1_mini_pc.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Proxmox/`
- `02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Proxmox/01_vignette/vignette_L4C2_proxmox.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Proxmox/02_page/page_L4C2_proxmox.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/`
- `02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/01_vignette/vignette_L4C3_maj_ha.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/02_page_gauche/page_L4C3_maj_ha_gauche.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/03_page_droite/page_L4C3_maj_ha_droite.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L5C1_13_Batteries_Piles/`
- `02_docs_dashboard/dashboard_docs_YAML/L5C1_13_Batteries_Piles/01_vignette/vignette_L5C1_batteries_piles.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L5C1_13_Batteries_Piles/02_page/page_L5C1_batteries_piles.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/`
- `02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/01_vignette/vignette_L5C2_batteries_portables.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/02_page_gauche/page_L5C2_batteries_portables_gauche.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/03_page_droite/page_L5C2_batteries_portables_droite.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/`
- `02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/01_vignette/vignette_L5C3_mariadb.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/02_page_mariadb/page_L5C3_mariadb.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/03_page_systeme_reserve/page_L5C3_systeme_reserve.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L6C1_16_Air_Qualite/`
- `02_docs_dashboard/dashboard_docs_YAML/L6C1_16_Air_Qualite/01_vignette/vignette_L6C1_air_qualite.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L6C1_16_Air_Qualite/02_page/page_L6C1_air_qualite.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L6C2_17_Pollution_Pollen/`
- `02_docs_dashboard/dashboard_docs_YAML/L6C2_17_Pollution_Pollen/01_vignette/vignette_L6C2_pollution_pollen.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L6C2_17_Pollution_Pollen/02_page/page_L6C2_pollution_pollen.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L6C3_18_VigiEau/`
- `02_docs_dashboard/dashboard_docs_YAML/L6C3_18_VigiEau/01_vignette/vignette_L6C3_vigieau.yaml`
- `02_docs_dashboard/dashboard_docs_YAML/L6C3_18_VigiEau/02_page/page_L6C3_vigieau.yaml`

### sigle MINI (1)
- `02_docs_dashboard/dashboard_docs_MD/L4C1_MINI_PC/02_page_mini_pc/PAGE_MINI_PC.md`

## Points a confirmer avant execution
- `05_docs_YAML_system` n existe ni en local ni en prod : s agit-il de `01_docs_config_system` (deja inchange) ou d un autre dossier ?
- Dossiers de generateurs en minuscules qui seraient renommes : `04_docs_scripts/docs_scripts_SH/gen_global_index_automations`, `04_docs_scripts/docs_scripts_SH/gen_global_index_ia`, `04_docs_scripts/docs_scripts_SH/gen_global_index_scripts`, `04_docs_scripts/docs_scripts_SH/gen_global_index_vignettes_pages`
- Les YAML de `docs_automations_YAML` et `docs_scripts_YAML` (ex. `p3_salon_bouton_ikea_inter_salon` -> `P3_Salon_bouton_ikea_inter_salon`) : aucun lien avec un autre outil verifie.
- Apres renommage : corriger les chemins cites dans 15 skills, dans `Github\README.md`, dans les 2 MOC, dans les generateurs et dans 31 fiches avec liens relatifs ; regenerer les index.
