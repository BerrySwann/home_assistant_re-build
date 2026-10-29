# VERIF_HEADERS_YAML - Controle des en-tetes des YAML de configuration

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Scripts-ff9800?style=flat-square)](.)

</div>

> **Script :** `Verif_headers_yaml.py` (Python, lance avec `python -I`)
> **Emplacement local :** `docs/04_docs_scripts/04_docs_scripts_SH/Verif_headers_yaml/Verif_headers_yaml.py`
> **Copie prod :** aucune (script local, non pousse en prod)
> **Execute depuis :** le PC (local ReBuild)
> **Cree :** 2026-10-20 (demande d'Eric : un skill qui verifie les ASCII, slugs, name et unique_id selon le CLAUDE.md)
> **Derniere modification :** 2026-10-20

---

## Description

Controle en LECTURE SEULE les YAML de `docs/01_docs_config_system/01_config_system_SH_PY_YAML/` contre les normes du `CLAUDE.md` (sections 4, 5, 7 et 8). Il ne corrige rien. Il complete `check_yaml_forme.py` (alignement des boites seul) en ajoutant les en-tetes, les slugs, les `name` et les `unique_id`.

## Controles

ERREUR (structure, a corriger) :
- `BOITE_DECALEE` : haut, titre et bas de largeur differente ; `BOITE_TROP_ETROITE` : le titre depasse la boite ; `ENTETE_COLLE` : `#` colle au trait de boite ;
- `BOITE_PRINCIPALE_ABSENTE` : pas de boite a coins arrondis en tete de fichier ;
- `HEADER_ABSENT` / `HEADER_ORDRE` : les 5 headers (DESCRIPTION, CALCUL & SOURCES, CHAINE DE DEPENDANCES, IMPORTANT (PIEGES), TABLEAU DE BORD (VIGNETTES PRINCIPALES)) doivent etre presents dans cet ordre, sous la forme `# ## ...` ;
- `SLUG_ABSENT` / `SLUG_DIFFERENT` : chaque entite doit avoir juste au-dessus `# --- unique_id_exact ---` ;
- `ID_DOUBLON` / `ID_FORMAT` : `unique_id` unique dans le fichier, en minuscules, chiffres et underscores.

AVIS (convention, a juger) : `BOITE_COINS` (arrondis pour le principal, carres pour le secondaire), `BOITE_LARGEUR` (principal < 78, secondaire < 37, ou boite plus large que necessaire), `BOITE_MINUSCULES`, `NUMEROTATION` (secondaire : numero 1 a 9, croissant), `SLUG_ORPHELIN`, `NOM_ID_DIFFERENT` (le `name` normalise ne redonne pas le `unique_id`), `NOM_INITIALE`, `TABLEAU_DEPENDANCES_ABSENT`, `PREFIXE_POLE` (seulement avec `--prefixe`).

Largeur des boites : 78 (principal) et 37 (secondaire) sont le cadre standard, pas une limite. Quand le titre ne tient pas, la boite s'allonge (largeur mini = longueur du texte + 5, de preference + 6 pour garder un espace avant la barre). Le haut, le titre et le bas gardent la meme largeur, indentation exclue.

## Utilisation

- `python -I Verif_headers_yaml.py` : tout le dossier config (avec `PYTHONIOENCODING=utf-8`).
- `python -I Verif_headers_yaml.py <fichier ou dossier>` : un fichier ou un sous-dossier.
- `--erreurs` : n'affiche que les ERREUR. `--prefixe` : controle aussi le prefixe de pole dans `name`.
- Derniere ligne : `controle verif_headers: fichiers=N erreurs=N avis=N`. Code de retour 0 sans ERREUR, 1 avec ERREUR, 2 si le chemin est introuvable.
- Ignores : sauvegardes `.bak_`, noms contenant une date, dossiers `.scripts`, `scripts`, `notifs`, `themes`, `blueprints`, `ARCHIVE`.

## Points d'attention

- Premier releve (2026-10-20, 89 fichiers) : 64 erreurs et 286 avis, dont 14 fichiers sans les 5 headers `# ## ...` et 9 slugs absents ou differents. Rien n'a ete corrige ce jour-la.
- Une heuristique cherche le `name` le plus proche du `unique_id` (a moins de 8 lignes) : un AVIS `NOM_ID_DIFFERENT` n'est pas forcement une erreur.
- Lecture seule : aucune ecriture, aucun fichier cree.

## Dependances

- Skill `ha-verif-headers` ; normes de `Claude md SAVE/CLAUDE.md` ; complete `check_yaml_forme.py`.

## Historique des modifications

- 2026-10-20 : creation (boites ASCII, 5 headers, slugs, name et unique_id).