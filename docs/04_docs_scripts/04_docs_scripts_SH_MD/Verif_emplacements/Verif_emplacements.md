# VERIF_EMPLACEMENTS - Controle des fichiers presents a plusieurs emplacements

> **Script :** `Verif_emplacements.py` (Python, lance avec `python -I`)
> **Emplacement local :** `docs/04_docs_scripts/04_docs_scripts_SH/Verif_emplacements/Verif_emplacements.py`
> **Copie prod (miroir docs) :** `H:\docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\`
> **Execute depuis :** le PC (local ReBuild)
> **Cree :** 2026-10-18 (demande d'Eric) ; **derniere modification :** 2026-10-18 (verrous d'editeur `#...#` en ecart attendu)
> **Etape du trigul :** C (appelee par `trigul_run.py`)

---

## Description

Pour chaque fichier de la carte des emplacements, calcule l'empreinte git blob SHA-1 (8 caracteres) a 5 emplacements :

- L : local ReBuild (source de verite) ;
- PR : prod racine `/config` (`H:\`) ;
- PM : prod miroir docs (`H:\docs\...`) ;
- GR : GitHub, racine du depot ;
- GD : GitHub, sous `docs/`.

Carte : `docs/00_IA/00_SOUS_CONTEXT_IA/IA_CARTE_EMPLACEMENTS/IA_CARTE_EMPLACEMENTS.md`. Lecture seule : il n'ecrit que son rapport. La prod ne doit jamais etre en avance sur le local : un fichier de la prod different du local est signale PROD DIFFERENTE DU LOCAL.

## Perimetre

- Fichiers suivis : tout `docs/01_docs_config_system/01_config_system_SH_PY_YAML/`, hors `.bak`, hors les dossiers `notifs`, `themes` et `blueprints` (laisses en prod seule, decision d'Eric du 2026-10-18), hors `secrets.yaml`, `scenes.yaml` et `ip_bans.yaml`.
- Dans `01_config_system_MD` : `GLOBAL_INDEX_REPO/GLOBAL_INDEX_REPO.md` et `README/README.md`.
- Scripts : sous-dossiers `01_scripts.sh` et `02_scripts.py` en local, a plat dans `/config/.scripts/` en prod.

## Verdicts

- Section 1 : SYNC, PROD DIFFERENTE DU LOCAL, GITHUB EN ATTENTE DU BACKUP (normal juste apres un push), ABSENT (emplacements manquants).
- Section 2, presents ailleurs qu'en local : PROD RACINE SEULE, PROD MIROIR SEUL, GITHUB RACINE SEUL, GITHUB DOCS SEUL.
- Section 3, ecarts attendus : fichiers verrou d'editeur `#...#` en prod seule (par exemple `.scripts/#MP_01_monitor_temp.sh.#`). Le `.gitignore` les ignore, ils ne passeront jamais sur GitHub : ils ne comptent pas dans les anomalies.

## Sorties

- `historique/03_RAPPORTS/06_MD5/03_VERIF_EMPLACEMENTS/verif_emplacements_AAAA-MM-JJ.txt` (le rapport du jour deja present est d'abord renomme en `.bak_AAAA_MM_JJ_HHhMMmSSs.txt`). Dernieres lignes : `ANOMALIES` et `RESULTAT`.
- Codes retour : 0 rapport ecrit ; 2 prod H: inaccessible (rien n'est ecrit).
- GitHub injoignable : rapport ecrit avec GR et GD a `?` (aucun verdict GitHub) ; le lanceur le signale en ATTENTION.

## Points d'attention

- Un retard GitHub apres un push en prod est normal jusqu'au backup HA suivant.
- Un cache Python (`__pycache__`) cree par un test dans le dossier suivi apparait en ABSENT : il faut le mettre a la corbeille.
- Pour ajouter un fichier ou un dossier aux exclusions, modifier `PROD_SEULE_DOSSIERS`, `EXCLUS_NOMS` ou `RACINE_MD` en tete du script (sur demande d'Eric, avec sauvegarde `.bak`).

## Dependances

- `trigul_run.py` ; skill `ha-trigul` ; carte `IA_CARTE_EMPLACEMENTS.md`.
- `H:` monte, acces a api.github.com, depot `BerrySwann/home_assistant_re-build`.

## Historique des modifications

- 2026-10-18 : creation (5 emplacements, carte des fichiers suivis).
- 2026-10-18 : `notifs`, `themes` et `blueprints` laisses en prod seule (jamais un ecart).
- 2026-10-18 : fichiers verrou d'editeur `#...#` en prod seule = ecart attendu (section 3 du rapport).