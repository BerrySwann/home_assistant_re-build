---
name: "ha-verif-headers"
description: "Skill HA ReBuild - verifie en lecture seule les en-tetes des YAML de config (boites ASCII a largeur variable, 5 headers, slug tertiaire, name et unique_id) selon les normes du CLAUDE.md. Declencher sur : /ha-verif-headers, verifie les headers, verifie les ascii slug name unique_id, controle de forme des YAML, le fichier est-il conforme, apres creation ou modification d'un YAML de config."
---

# HA Verif Headers - controle des en-tetes des YAML de config

> Fichiers presents a plusieurs emplacements (config, GLOBAL_INDEX_REPO, README) : voir `docs\00_IA\SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` et le controle `Verif_emplacements.py` (decide par Eric le 2026-10-18).

Cree le 2026-10-20 sur demande d'Eric. Verifie qu'un YAML de `docs\01_docs_config_system\config_system_SH_PY_YAML\` respecte les normes du `Claude md SAVE\CLAUDE.md` : sections 4 (bordures ASCII), 5 (5 headers obligatoires), 7 (slug tertiaire), 8 (name et unique_id). LECTURE SEULE : le skill ne corrige rien sans ordre d'Eric.

Complement de `ha-new-yaml` (qui genere un squelette conforme) et de `check_yaml_forme.py` (alignement des boites seul).

## WORKFLOW

### 1 - Lancer le controle (sur le PC)

```powershell
$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\Verif_headers_yaml\Verif_headers_yaml.py" [fichier ou dossier] [--erreurs] [--prefixe]
```

- Sans argument : tous les YAML de `config_system_SH_PY_YAML` (environ 90 fichiers).
- Avec un chemin : un fichier ou un sous-dossier. Apres avoir cree ou modifie un YAML, le lancer sur ce fichier.
- `--erreurs` : seulement les ERREUR. `--prefixe` : controle aussi le prefixe de pole dans `name` (tres peu suivi aujourd'hui, donc desactive par defaut).
- Derniere ligne : `controle verif_headers: fichiers=N erreurs=N avis=N`. Code de retour 0 sans ERREUR, 1 avec ERREUR.

### 2 - Lire le resultat

ERREUR (structure, a corriger) : `BOITE_DECALEE` (haut, titre et bas de largeurs differentes), `BOITE_TROP_ETROITE`, `ENTETE_COLLE`, `BOITE_PRINCIPALE_ABSENTE`, `HEADER_ABSENT`, `HEADER_ORDRE`, `SLUG_ABSENT`, `SLUG_DIFFERENT`, `ID_DOUBLON`, `ID_FORMAT`.

AVIS (convention, a juger avec Eric) : `BOITE_COINS`, `BOITE_LARGEUR`, `BOITE_MINUSCULES`, `NUMEROTATION`, `SLUG_ORPHELIN`, `NOM_ID_DIFFERENT`, `NOM_INITIALE`, `TABLEAU_DEPENDANCES_ABSENT`, `PREFIXE_POLE`.

Regles de largeur des boites (rappel d'Eric du 2026-10-20) : 78 (principal, coins arrondis) et 37 (secondaire, coins carres) sont le cadre standard, pas une limite. Une boite est plus longue quand son titre est plus long : largeur mini = longueur du texte + 5 (de preference + 6, un espace avant la barre). Le haut, le titre et le bas gardent toujours la meme largeur, indentation exclue. Ne jamais tronquer un titre pour tenir dans 78.

Un AVIS n'est pas forcement une faute : `NOM_ID_DIFFERENT` vient d'une heuristique (name normalise compare au unique_id), `NOM_INITIALE` tombe sur des sigles comme tCOV. Le dire, ne pas corriger en masse.

### 3 - Compte rendu

- Donner la ligne `controle verif_headers`, puis les ERREUR par fichier (fichier:ligne, type, detail), puis le nombre d'AVIS par type.
- Un ecart ancien (deja present avant la session) se signale, il ne se corrige pas sans demande.
- Proposer la correction fichier par fichier : sauvegarde locale `.bak_AAAA_MM_JJ_HHhMMmSSs` avant modification, modification en local, relance du controle sur le fichier, ligne au journal des modifs, puis `/ha-push-yaml` sur ordre d'Eric.

## REGLES

1. Lecture seule par defaut : aucun fichier modifie sans ordre d'Eric.
2. Normes = `Claude md SAVE\CLAUDE.md` ; en cas de doute sur une norme, lire le CLAUDE.md, ne pas deviner.
3. Les sauvegardes (`.bak_`), les noms dates et les dossiers `.scripts`, `scripts`, `notifs`, `themes`, `blueprints`, `ARCHIVE` sont ignores par le script.
4. Ne touche ni aux automations ni aux dashboards (hors perimetre `config_system_SH_PY_YAML`).
5. Fiche du script : `docs\04_docs_scripts\04_docs_scripts_sh_md\Verif_headers_yaml\Verif_headers_yaml.md`.