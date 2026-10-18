# HERMES_AUDIT_TRIGUL_ARBRES - Superposition des 3 arbres GitHub / local / prod

> **Script :** `hermes_audit_trigul_arbres.py` (Python, lance avec `python -I`)
> **Emplacement local :** `docs/04_docs_scripts/docs_scripts_SH/hermes_audit_md5_trigul_3md/hermes_audit_trigul_arbres.py`
> **Copie prod (miroir docs) :** `H:\docs\04_Docs_scripts\Docs_scripts_sh\Hermes_audit_md5_trigul_3md\`
> **Execute depuis :** le PC (local ReBuild), jamais sur HA : il lit H: et l'API GitHub
> **Cree :** 2026-10-17 (demande d'Eric) ; **derniere modification :** 2026-10-18 (verrous d'editeur `#...#` en ecart attendu)
> **Etape du trigul :** A (appelee par `trigul_run.py`)

---

## Description

Compare le dossier `docs/` aux 3 niveaux : GitHub (dernier commit du depot), local (ReBuild, source de verite) et prod (`H:\docs`), plus le README racine. Une ligne par fichier, trois colonnes R (GitHub), L (local), P (prod). Lecture seule : il ne modifie, ne pousse et ne supprime rien, il n'ecrit que son rapport.

Phase 1, superposition des chemins : ce qui n'existe pas aux 3 niveaux est mis de cote avec son origine (`[L]` local seul, `[P]` prod seule, `[R]` GitHub seul, `[LP]` absent de GitHub, `[LR]` absent de la prod, `[PR]` absent du local). Une casse differente entre niveaux va dans la section CASSE.

Phase 2, contenu : sur les chemins communs de meme casse, comparaison de l'empreinte (git blob SHA-1 des octets). GitHub la fournit dans sa liste, rien n'est telecharge.

Verdicts : SYNC, fin de ligne seule, LOCAL en avance (a pousser), GITHUB en retard (attend le backup HA), PROD seule differente (suspect), 3 contenus differents.

Colonne DIFF : nombre de niveaux ou le fichier manque, plus 1 si le contenu differe.

## Perimetre

- `docs/` complet et le README racine.
- Ignores : les `.bak` (ni comptes ni cites) et le dossier `modifs/`.
- Ecarts attendus (fonction `attendu()` et liste `EXCEPTIONS_TXT`) : sauvegardes locales, archives `_archive_`, anciens exports Dashboard_COMPLET, types ignores par le `.gitignore` de H: presents en local et en prod (.txt .png .jpg .jpeg .gif .webp .ico .pyc, sauf les .txt de `notifs/`), journaux `modifs/` et, depuis le 2026-10-18, les fichiers verrou d'editeur `#...#` presents en prod seule.
- Tout le reste est une anomalie.

## Utilisation

- Lancer : `python -I hermes_audit_trigul_arbres.py` (environ 5 s, avec `PYTHONIOENCODING=utf-8`). L'option `--tout` liste aussi les fichiers SYNC.
- Normalement lance par `trigul_run.py`, qui journalise le resultat.
- Doit tourner sur le PC : l'API GitHub (api.github.com, 2 requetes : le dernier commit puis l'arbre complet) repond 403 depuis le cloud. Si la liste est tronquee ou si l'API ne repond pas, le script s'arrete avec une erreur : ne pas conclure.

## Sorties

- `historique/MD5/00_Verif_Final_trigul_arbres/trigul_arbres_AAAA-MM-JJ.txt` et `.html`. Le rapport du jour deja present est d'abord sauvegarde en `.bak_AAAA_MM_JJ_HHhMMmSSs`.
- Dernieres lignes : `ANOMALIES`, `RESULTAT AUDIT`, `RESULTAT`. La section `== CONTROLE ==` verifie que la somme des chemins (SYNC + a traiter + attendus) egale l'union : ligne `controle du script : OK` sinon `ERREURS DU SCRIPT`.

## Points d'attention

- La prod H: est un partage SMB insensible a la casse : un fichier renomme en local garde son ancien nom en prod et sur GitHub. Le script le signale dans CASSE ; il faut renommer explicitement sur H:.
- Juste apres un backup HA, GitHub change : le rapport indique le commit utilise. Un retard GitHub apres un push en prod est normal jusqu'au backup suivant.
- Si presque tout est absent cote prod, H: n'etait pas visible : verifier l'acces avant de conclure.
- Les fichiers YAML de config de la racine de H: ne sont pas dans ce perimetre : ils sont controles par `Verif_emplacements.py`.

## Dependances

- `trigul_run.py` (lanceur) ; skill `ha-trigul` (protocole et lecture du rapport).
- `H:` monte, acces Internet vers api.github.com, depot `BerrySwann/home_assistant_re-build`.

## Historique des modifications

- 2026-10-17 : creation (superposition R / L / P, colonne DIFF).
- 2026-10-18 : rapports ranges dans le repertoire numerote `00_Verif_Final_trigul_arbres`.
- 2026-10-18 : .svg du dossier docs plus consideres comme ecart attendu (`.gitignore` de H: modifie par Eric).
- 2026-10-18 : fichiers verrou d'editeur `#...#` en prod seule = ecart attendu.