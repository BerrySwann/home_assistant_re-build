# HERMES_AUDIT_MD5_TRIGUL_UNITAIRE - Comparaison unite par unite de automations.yaml et scripts.yaml

> **Script :** `hermes_audit_md5_trigul_unitaire.py` (Python, lance avec `python -I`)
> **Emplacement local :** `docs/04_docs_scripts/docs_scripts_SH/hermes_audit_md5_trigul_3md/hermes_audit_md5_trigul_unitaire.py`
> **Copie prod (miroir docs) :** `H:\docs\04_Docs_scripts\Docs_scripts_sh\Hermes_audit_md5_trigul_3md\`
> **Execute depuis :** le PC (local ReBuild), il lit `H:\automations.yaml` et `H:\scripts.yaml`
> **Etape du trigul :** B1, etape profonde (decidee le 2026-10-11), appelee par `trigul_run.py`
> **Derniere modification :** 2026-10-18 (8 etapes numerotees, analyse sur les copies bak)

---

## Description

Compare chaque automation et chaque script de la prod (`H:\automations.yaml`, `H:\scripts.yaml`) au YAML local correspondant, unite par unite. GitHub n'est pas compare a cette etape. Le MD5 compare est un MD5 logique : YAML parse, cles triees, `category` et `labels` ignores, espaces de debut et de fin ignores, commentaires et mise en forme ignores.

La prod est plus importante que le local : une prod en avance sur le local (unite DIFFERENT) se signale en premier. Lecture seule sur H: et sur les YAML locaux ; le script n'ecrit que les deux copies datees, le rapport et un dossier temporaire.

## Les 8 etapes

Chaque etape s'affiche en `ETAPE n` et est reprise dans la ligne `ETAPES :` du rapport.

- 1. Points bak : reserve les noms `automations.bak_<date_heure>.yaml` (dossier `AUTOMATIONS.YALM ORIGINAL`) et `scripts.bak_<date_heure>.yaml` (dossier `DOCS_SCRIPT_ORIGINAL`), cree les dossiers, s'arrete (code 3) si un point existe deja.
- 2. Copie de `H:\automations.yaml` et `H:\scripts.yaml` vers ces points.
- 3. MD5 de chaque fichier de la prod contre son bak. Si l'un differe : ATTENTION, mais l'analyse continue (decide par Eric le 2026-10-18 : c'est elle qui dit quelles unites ont change).
- 4. L'analyse lit les COPIES bak, plus H:.
- 5. Extraction de chaque unite dans `ReBuild/_tmp_trigul_profond/` (un fichier par unite).
- 6. Controle final : MD5 de la prod relu apres l'analyse. ATTENTION dans le rapport si la prod a bouge pendant l'analyse.
- 7. Comparaison au YAML local et ecriture du rapport.
- 8. Effacement du dossier temporaire (garde-fou : uniquement le dossier attendu).

## Statuts du rapport

- Automations : IDENTIQUE, IDENTIQUE_HORS_ID_ALIAS (rapprochee par l'alias quand l'export local n'a pas d'id), DIFFERENT, ABSENT_LOCAL.
- Scripts : IDENTIQUE, DIFFERENT, ABSENT_LOCAL.
- Les exports locaux sans automation en prod sont listes a part. Au 2026-10-18 : `Automations.yalm original\Automations.yaml`, `P1_SDB\h_soufflant_SDB_routage.yaml`, `P1_SDB\i_soufflant_SDB_bouton_rodret.yaml`.

## Sorties

- `historique/MD5/01_trigul_profond/trigul_profond_AAAA-MM-JJ.txt` (sauvegarde `.bak_date_heure` si le rapport du jour existe). En-tete : ligne `ETAPES :`, copies faites, MD5 des fichiers, nombre d'unites, AUTOMATIONS et SCRIPTS, duree.
- Les copies datees dans les deux dossiers ORIGINAL sont des `.bak` ordinaires, rangees par le menage de /histo.
- Code de retour : 0 normal ; 2 si `H:` est introuvable ; 3 si un point bak existe deja.

## Points d'attention

- Une collision de nom (deux lancements dans la meme seconde) arrete le script a l'etape 1.
- Les categories HA (etape B2 du trigul) ne sont pas lues par ce script : Claude les lit via `ha_config_get_category`.
- Dependance : module Python `yaml`.

## Dependances

- `trigul_run.py` (lanceur) ; skill `ha-trigul` ; section PROTOCOLE TRIGUL PROFOND de CLAUDE.md.
- `H:` monte.

## Historique des modifications

- 2026-10-11 : etape profonde decidee (62 automations et 9 scripts, moins d'une seconde).
- 2026-10-18 : rapport range dans le repertoire numerote `01_trigul_profond`.
- 2026-10-18 : 8 etapes numerotees ; l'analyse lit les copies bak ; MD5 prod relu en fin d'analyse ; un MD5 different n'arrete plus le script (ATTENTION).