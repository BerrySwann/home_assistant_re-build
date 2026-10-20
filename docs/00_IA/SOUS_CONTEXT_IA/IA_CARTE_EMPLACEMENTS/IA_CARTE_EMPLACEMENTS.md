# IA_CARTE_EMPLACEMENTS

*Cree le 2026-10-18 a la demande d'Eric. Source unique pour les fichiers qui existent a plusieurs emplacements. Les skills et scripts s'y referent au lieu de recopier les regles.*

*Lire ce fichier si : push d'un fichier de config ou de GLOBAL_INDEX_REPO / README, controle local / prod / GitHub, mise a jour d'un skill qui copie ou compare des fichiers.*

## 1. Les 5 emplacements

- **L** : local ReBuild (`C:\Users\Berry Swann\Documents\ReBuild\`). Source de verite : la prod ne doit jamais etre en avance sur le local (regle d'Eric du 2026-10-18).
- **PR** : prod racine `/config/` (= `H:\`). C'est ce que HA lit.
- **PM** : prod miroir docs `/config/docs/...` (= `H:\docs\...`).
- **GR** : GitHub, racine du depot `BerrySwann/home_assistant_re-build`.
- **GD** : GitHub, sous `docs/` du depot.

GitHub (GR et GD) est alimente uniquement par le backup HA (`ha_git_backup.sh`), jamais par un push direct. Un ecart GitHub juste apres un push en prod est normal jusqu'au backup suivant.

## 2. Familles de fichiers

### 2.1 Config HA : `docs/01_docs_config_system/config_system_SH_PY_YAML/`

Chaque fichier existe aux 5 emplacements :
- L = `docs/01_docs_config_system/config_system_SH_PY_YAML/<chemin>`
- PR = `/config/<chemin racine>`
- PM = `/config/docs/01_docs_config_system/config_system_SH_PY_YAML/<chemin>`
- GR = `<chemin racine>`
- GD = `docs/01_docs_config_system/config_system_SH_PY_YAML/<chemin>`

Correspondance `<chemin>` vers `<chemin racine>` : identique, sauf les scripts.
- `.scripts/01_scripts.sh/<fichier>.sh` -> `.scripts/<fichier>.sh` (a plat en prod)
- `.scripts/02_scripts.py/<fichier>.py` -> `.scripts/<fichier>.py` (a plat en prod)
- `scripts/<fichier>.sh` -> `scripts/<fichier>.sh`

Les dossiers directement sous `/config/` gardent le nom de la prod (regle 6.16 du document de nommage).

### 2.2 Fichiers de la racine documentes dans `config_system_MD`

- `docs/01_docs_config_system/config_system_MD/GLOBAL_INDEX_REPO/GLOBAL_INDEX_REPO.md` (original local) -> PR `/config/GLOBAL_INDEX_REPO.md`, PM meme chemin sous `/config/docs/`, GR `GLOBAL_INDEX_REPO.md`, GD meme chemin sous `docs/`.
- `docs/01_docs_config_system/config_system_MD/README/README.md` (original local, decision d'Eric du 2026-10-18) -> PR `/config/README.md`, PM, GR `README.md`, GD.
- `Github\README.md` n'est plus l'original (copie sans role depuis le 2026-10-18).

### 2.3 Les autres fichiers de `docs/`

Trois emplacements seulement : L, PM, GD. Controles par `/ha-trigul` (superposition des arbres).

## 3. En prod seule (jamais un ecart)

- Dossiers : `notifs/` (TOUS les fichiers de /config/notifs sont vivants, regeneres par HA : jamais copies dans docs ; sauvegardes au fil de l'eau sur GitHub a la racine `notifs/` par le backup HA, voulu par Eric le 2026-10-18), `themes/`, `blueprints/`.
- Fichiers : `scenes.yaml`, `ip_bans.yaml`, `secrets.yaml` (jamais lu, jamais copie).
- Copie de secours : GitHub.

## 4. Cas traites ailleurs

- `automations.yaml` et `scripts.yaml` : une fiche YAML par unite en local, comparaison unite par unite par l'etape profonde de `/ha-trigul`.
- `Dashboard_*.yaml` a la racine de la prod : etape 5B de `/histo` (tous les exports gardes en local, un seul en prod dans `Dashboard_COMPLET`).
- Fichiers `.bak` : uniquement en local, jamais sur H: ni D:.

## 5. Sens d'ecriture

- On modifie le local d'abord (sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs` a cote).
- Push d'un fichier des familles 2.1 et 2.2 : vers PR ET vers PM, MD5 verifie sur les deux. Jamais un seul des deux.
- Push d'un script vers `/config/.scripts/` ou `/config/scripts/` : seulement sur ordre d'Eric.
- GitHub suit au backup HA lance par Eric.

## 6. Controle

Script en lecture seule : `docs/04_Docs_scripts/Docs_scripts_sh/Verif_emplacements/Verif_emplacements.py`.

Lancement : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_Docs_scripts\Docs_scripts_sh\Verif_emplacements\Verif_emplacements.py"`

Rapport : `historique\MD5\03_verif_emplacements\verif_emplacements_AAAA-MM-JJ.txt`. Verdicts : SYNC, PROD DIFFERENTE DU LOCAL, GITHUB EN ATTENTE DU BACKUP, ABSENT (avec les emplacements manquants), et en section 2 les fichiers presents ailleurs qu'en local (PROD RACINE SEULE, PROD MIROIR SEUL, GITHUB RACINE SEUL, GITHUB DOCS SEUL). Dernieres lignes : `ANOMALIES` et `RESULTAT`.

Premier passage (2026-10-18 17:41, commit GitHub f45a765c) : 97 fichiers suivis, 94 SYNC, 2 en attente du backup GitHub (GLOBAL_INDEX_REPO et README a leur nouvel emplacement), 1 prod differente du local (`check_yaml_forme.py`, poussee en local seulement), 1 fichier verrou d'editeur en prod (`.scripts/#MP_01_monitor_temp.sh.#`).

## 7. Skills et scripts concernes

`histo`, `histo-final`, `ha-push-yaml`, `ha-push-docs`, `ha-trigul`, `sync-index`, `update-arbo`, `ha-resync-tree`, `ha-new-yaml`, `fix-file`. A mettre a jour pour citer cette carte et appeler le script (en cours le 2026-10-18).