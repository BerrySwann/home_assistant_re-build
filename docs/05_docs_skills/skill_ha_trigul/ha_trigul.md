---
name: "ha-trigul"
description: "Skill HA ReBuild - triangulation des docs entre local (ReBuild), prod (H:) et GitHub : superposition des 3 arbres (en trop, manquant, casse, contenu, format de l'audit MD5 docs), etape profonde automations/scripts et controle des fichiers a 5 emplacements. Declencher sur /trigul, trigul, triangulation, audit md5 des docs, les docs sont-ils a jour en prod et sur GitHub."
---

# Skill : /ha-trigul - triangulation des docs (local / prod / GitHub)

> Fichiers presents a plusieurs emplacements (config, GLOBAL_INDEX_REPO, README) : voir `docs\00_IA\SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 emplacements : local, prod racine, prod miroir docs, GitHub racine, GitHub docs/) et le controle en lecture seule `docs\04_Docs_scripts\Docs_scripts_sh\Verif_emplacements\Verif_emplacements.py` (decide par Eric le 2026-10-18, etape C ci-dessous).

## Objectif

Trois controles enchaines, rapports ranges dans `historique\03_RAPPORTS\06_MD5\`, un sous-repertoire numerote par type de rapport (voir "Fichiers et chemins"). Lecture seule : le skill ne modifie, ne pousse et ne corrige aucun fichier de documentation. Il n'ecrit que les rapports (et, pour l'etape profonde, les copies datees de la prod dans les dossiers ORIGINAL).

1. Superposition des 3 arbres (script python) : fait ce que fait l'audit MD5 docs cote HA (H:\.scripts\audit_md5_md_yaml.sh, qui compare la prod a GitHub), mais sur les 3 niveaux GitHub, local, prod. Il fait l'union des chemins, tous types de fichiers, met de cote ce qui est en trop ou manquant (avec son origine) et les differences de casse, puis compare le contenu de ce qui est commun. Il remplace le trigul .md en bash depuis le 2026-10-18 (decision d'Eric : le trigul .md ne voyait que les .md et partait de la liste locale, donc ne voyait ni les fichiers de la prod ou de GitHub absents du local, ni les .yaml, ni les .sh).
2. Etape profonde : automations et scripts YAML unite par unite, puis categories HA.
3. Fichiers a plusieurs emplacements (config, GLOBAL_INDEX_REPO, README) : 5 emplacements compares (etape C).

Le trigul se lance par un lanceur qui ecrit un journal de trace (voir "Lancement et journal de trace") : il montre ou le trigul s'arrete le jour ou il plante, et detecte les echecs silencieux (ancien rapport pris pour un nouveau, script mort sans bruit).

Perimetre de la superposition : `docs/` complet + le README racine (`docs/01_docs_config_system/config_system_MD/README/README.md` en local, original depuis le 2026-10-18 ; `README.md` a la racine de H: et du depot, compare sous le nom `(racine)/README.md`), hors `.bak` (ignores completement, ni comptes ni cites) et hors le dossier `modifs/` (journaux des agents, ignore aux 3 niveaux depuis le 2026-10-18, comme l'audit HA). Les YAML de config de la racine de H: ne sont pas dans la superposition : ils sont controles par l'etape C.

Source de verite = LOCAL (ReBuild). Un ecart local/prod veut dire prod EN RETARD ; un ecart prod/depot veut dire depot EN RETARD. GitHub = dernier commit du depot, alimente par le backup HA (jamais de push direct) : un retard apres un push en prod est normal jusqu'au backup suivant.

Pre-requis : la session doit etre liee au PC (desktop Claude). Sans liaison, ni H:, ni le disque local, ni l'API GitHub ne sont accessibles (GitHub repond 403 depuis le conteneur cloud) : le dire, ne pas conclure.

## Fichiers et chemins

- Script 1 (superposition des arbres) : `C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\hermes_audit_md5_trigul_3md\hermes_audit_trigul_arbres.py`
- Script 2 (profond) : `...\hermes_audit_md5_trigul_3md\hermes_audit_md5_trigul_unitaire.py` (meme dossier)
- Script 3 (emplacements) : `C:\Users\Berry Swann\Documents\ReBuild\docs\04_Docs_scripts\Docs_scripts_sh\Verif_emplacements\Verif_emplacements.py`
- Lanceur avec journal de trace (decide par Eric le 2026-10-18) : `C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\hermes_audit_md5_trigul_3md\trigul_run.py` (meme dossier que les scripts 1 et 2). Il lance les scripts 1, 2 et 3 sans les modifier.
- Ancien trigul .md en bash : `...\hermes_audit_md5_trigul_3md\hermes_audit_md5_trigul_3md.sh` (meme dossier que le script 1). Ne plus le lancer : il est redondant avec le script 1. Le fichier reste en place (ne pas le supprimer sans demande d'Eric).
- Interpreteur : `python -I` (scripts 1, 2 et 3 et lanceur).
- Dossier des rapports : `C:\Users\Berry Swann\Documents\ReBuild\historique\03_RAPPORTS\06_MD5\`, avec un sous-repertoire numerote par type de rapport (decide par Eric le 2026-10-18) :
  - `00_VERIF_FINAL_TRIGUL_ARBRES` : `trigul_arbres_[YYYY-MM-DD].txt` et `.html`, ecrits par le script 1 (teste le 2026-10-18 : les 2 rapports du jour y sont) ;
  - `01_TRIGUL_PROFOND` : `trigul_profond_[YYYY-MM-DD].txt`, ecrit par le script 2 (verifie le 2026-10-18 : le rapport arrive bien dans ce repertoire) ;
  - `02_CATEGORIES_HA` : `categories_ha_[YYYY-MM-DD].txt`, ecrit par Claude a l'etape B2, pas par un script ;
  - `03_VERIF_EMPLACEMENTS` : `verif_emplacements_[YYYY-MM-DD].txt`, ecrit par le script 3 (cree le 2026-10-18).
  - `04_JOURNAL_TRIGUL` : `trigul_journal_[YYYY-MM-DD].log`, journal de trace ecrit par le lanceur (une ligne par evenement, un fichier par jour, ajout) ;
  - Un nouveau type de rapport = le repertoire suivant (`05_...`, puis `06_...`) : le creer avec son numero, puis l'ajouter ici et dans CLAUDE.md.
  - Le menage des `.bak` de ces repertoires est fait par /histo (etape 5, chapitre "Cas particulier : historique\03_RAPPORTS\06_MD5\") : 10 sauvegardes horodatees au maximum le jour meme, 3 sauvegardes datees pour les jours passes ; les rapports eux-memes (un par jour) ne sont pas limites.
- L'ancien `hermes_md5_audit_md_*.txt` n'est plus produit.
- Rapport de l'audit HA (prod contre GitHub, pour recoupement) : `H:\.logs\md5_audit_md_yaml_[YYYY-MM-DD].txt`.

Les scripts peuvent etre modifies sur demande d'Eric (decision du 2026-10-17) : sauvegarde `nom.bak_AAAA_MM_JJ_HHhMMmSSs.ext` dans le meme dossier avant toute modification, controle de syntaxe (`python -I -W error -c "import ast..."` ou `bash -n`), ligne dans le journal des modifs. Ne jamais pousser un script en prod (docs ou H:\.scripts) sans ordre d'Eric. Le script 1 n'a pas encore de fiche dans docs_scripts_sh_md.

## Protocole

### Lancement et journal de trace (decide par Eric le 2026-10-18)

Lancer le trigul avec le lanceur : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\hermes_audit_md5_trigul_3md\trigul_run.py"` (environ 10 s). Il enchaine A (script 1), B1 (script 2) et C (script 3), sans modifier les scripts, et ecrit `historique\03_RAPPORTS\06_MD5\04_JOURNAL_TRIGUL\trigul_journal_[YYYY-MM-DD].log` ligne par ligne (heure | niveau | etape | message ; niveaux INFO, SORTIE, STDERR, NOTE, OK, ATTENTION, ECHEC), chaque ligne forcee sur le disque. Apres chaque script il controle : code de retour, Traceback, depassement de temps (300 s), rapport absent, vide ou pas mis a jour pendant ce lancement (un ancien rapport serait pris pour le nouveau), marqueurs de fin du rapport (RESULTAT, controle du script : OK, ANOMALIES), dossier temporaire du profond laisse derriere, mention "injoignable" dans la sortie du script 3. Verdict par etape : OK, ATTENTION ou ECHEC. Code de retour du lanceur : 0 sans ECHEC, 1 sinon.

Apres le lancement :
1. Lire les lignes ECHEC et ATTENTION du journal du jour et les mettre EN TETE du compte rendu.
2. Si la derniere ligne du journal n'est pas `FIN DU LANCEUR`, le lanceur a ete interrompu (PC eteint, session fermee) : le dire et citer la derniere ligne.
3. L'etape B2 (categories HA) est faite par Claude : ajouter sa ligne au journal avec `python -I trigul_run.py --note B2_categories_ha "texte"`.
4. Un ECHEC ne se corrige pas sans demande : citer l'etape, la ligne du journal et le fichier concerne.

Les sections A, B et C ci-dessous decrivent ce que fait chaque script et comment lire son rapport. Lancer un script seul n'est a faire que pour un essai, hors journal.

### A. Superposition des 3 arbres (script 1)

Lancer : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\hermes_audit_md5_trigul_3md\hermes_audit_trigul_arbres.py"`. Duree : environ 5 s, un seul appel. Le script ecrit le rapport `.txt` et sa version `.html` dans `historique\03_RAPPORTS\06_MD5\00_VERIF_FINAL_TRIGUL_ARBRES\` et sauvegarde lui-meme les rapports du jour en `.bak_...` s'ils existent. Il lit la liste complete du dernier commit GitHub par l'API (api.github.com, une requete, sans telechargement) : il doit tourner sur le PC. Si la liste est tronquee ou si l'API ne repond pas, il s'arrete avec une erreur : le dire, ne pas conclure. Option `--tout` : liste aussi les fichiers SYNC dans le rapport.

Methode :
- Chaque niveau est scanne en entier (local et prod : disque ; GitHub : liste de l'API avec le git blob SHA-1 de chaque fichier). Les chemins sont groupes sans tenir compte de la casse, puis la casse est comparee exactement.
- Un chemin qui n'est pas aux 3 niveaux est mis de cote avec son origine : `[L]` local seul, `[P]` prod seule, `[R]` GitHub seul, `[LP]` absent de GitHub, `[LR]` absent de la prod, `[PR]` absent du local. Un meme chemin avec une casse differente entre niveaux va dans la section CASSE.
- Sur les chemins aux 3 niveaux et de meme casse : comparaison de l'empreinte (git blob SHA-1 des octets ; local et prod sont recalcules pareil). Verdicts : SYNC, fin de ligne seule (sans action), LOCAL en avance (prod = GitHub, local different : a pousser), GITHUB en retard (local = prod, GitHub different : attend le backup HA), PROD seule differente (suspect), 3 contenus differents (a voir a la main).
- Ecarts attendus mis a part avec leur raison (liste `EXCEPTIONS_TXT` et fonction `attendu()` du script, a faire evoluer sur demande d'Eric) : archives `_archive_` locales (local seul), types ignores par le `.gitignore` de H: presents en local + prod (.txt .png .jpg .jpeg .gif .webp .ico .pyc). Les .svg ne sont plus un ecart attendu depuis le 2026-10-18 : Eric a ajoute `!docs/**/*.svg` dans H:\.gitignore (les .svg hors docs restent ignores). Les fichiers verrou d'editeur `#...#` presents en prod seule (par exemple `.scripts/#MP_01_monitor_temp.sh.#`) sont un ecart attendu depuis le 2026-10-18 (decide par Eric : le `.gitignore` les ignore, ils ne passeront jamais sur GitHub) ; le script 3 les liste dans la section 3 ECARTS ATTENDUS de son rapport. Tout le reste est une anomalie.

Colonne DIFF (regle d'Eric du 2026-10-18) : nombre de niveaux ou le fichier manque, plus 1 si le contenu differe entre les niveaux presents (fin de ligne seule : 0 de contenu). `aucune` si tout est bon, sinon `x N diff` (1 niveau manquant = 1 diff, 2 manquants = 2 diff, contenu different = 1 diff, contenu different plus un manquant = 2 diff, trois contenus tous differents = 2 diff).

Lecture du rapport `trigul_arbres_[date].txt`, dans l'ordre :
- en-tete : commit GitHub utilise (sha, date, message), nombre de fichiers par niveau ;
- `== AUDIT ==` : ligne `RESULTAT AUDIT : N fichiers (a .md - b .yaml - c .sh) - SYNC - fin de ligne seule - DIFF - CASSE - ABSENT GITHUB - ABSENT PROD - ABSENT LOCAL - ABSENT 2 NIVEAUX`, meme perimetre (.md .yaml .sh) et meme esprit que le RESULTAT de l'audit HA, sur les 3 niveaux ; les statuts s'excluent mutuellement et leur somme egale le total (le script le controle) ;
- `== COMPTES PAR NIVEAU ==` : une ligne `RESULTAT GitHub / local / prod / union : N fichiers (.md, .yaml, .sh, autres)` ;
- `== VUE D ENSEMBLE ==` : chemins de l'union, SYNC, a traiter par verdict, ecarts attendus ;
- `== 1. A TRAITER ==` : colonnes `R (GitHub) | L (local) | P (prod) | R L P | DIFF | FICHIER`, une case = empreinte courte de 8 caracteres ou `-` si absent, `R L P` = presence (1 present, 0 absent). Attention : la mention `[meme contenu]` sur une ligne ou un niveau est absent veut dire que les DEUX niveaux presents ont la meme empreinte (par exemple GitHub = prod pour un fichier absent du local). Elle ne veut pas dire qu'un fichier local de meme contenu existe sous un autre nom : le verifier a part par l'empreinte ;
- `== 2. ECARTS ATTENDUS == ` ;
- `== CONTROLE ==` : la somme des chemins (SYNC + a traiter + attendus) doit etre egale a l'union, un fichier present partout doit avoir 3 - 1 - 1 - 1 = 0 ; ligne `controle du script : OK` sinon `ERREURS DU SCRIPT` (a signaler en tete du compte rendu) ;
- dernieres lignes : `ANOMALIES : aucune` ou `ANOMALIES : x N fichiers, M diff au total`, la ligne `RESULTAT AUDIT`, la ligne `RESULTAT`.

Si presque tout est absent cote prod, la prod H: n'etait pas visible depuis le processus lance : verifier l'acces a H: avant de conclure.

Piege de la casse (constate le 2026-10-17) : la prod H: est un partage SMB insensible a la casse. Copier un fichier ou un dossier renomme en local vers H: garde l'ancien nom en prod, sans erreur et avec un MD5 identique, et GitHub (alimente par le backup HA depuis H:) garde aussi l'ancien nom. Le script signale ce cas dans la section CASSE. Pour changer la casse en prod il faut renommer explicitement sur H: (Rename-Item), fichiers d'abord puis repertoires ; GitHub suit au backup HA suivant. Le 2026-10-17 : 283 noms renommes en prod, puis 0 ecart de casse.

Autres pieges : le `.gitignore` de H: est un fichier cache (l'ecrire avec `[IO.File]::WriteAllText` donne un acces refuse : ouvrir avec FileMode.Open, SetLength(0), puis ecrire). Juste apres un backup HA, GitHub peut changer : le rapport indique le commit utilise.

### B. Etape profonde (automations et scripts, decidee le 2026-10-11)

Comparaison unite par unite de H:\automations.yaml et H:\scripts.yaml avec les YAML locaux (prod contre local ; GitHub n'est pas compare a cette etape). Elle est integree au /trigul (moins d'une seconde pour 71 unites). Protocole complet : section PROTOCOLE TRIGUL PROFOND de CLAUDE.md.

1. Lancer : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\docs_scripts_SH\hermes_audit_md5_trigul_3md\hermes_audit_md5_trigul_unitaire.py"`. Le script suit 8 etapes numerotees (affichees `ETAPE n` et reprises dans le rapport, ligne `ETAPES :`) : (1) points bak : reserve les noms `AUTOMATIONS.YALM ORIGINAL\automations.bak_<date_heure>.yaml` et `DOCS_SCRIPT_ORIGINAL\scripts.bak_<date_heure>.yaml`, cree les dossiers, s'arrete (code 3) si un point existe deja ; (2) copie de `H:\automations.yaml` et `H:\scripts.yaml` vers ces points ; (3) MD5 de chaque fichier de la prod contre son bak : si l'un differe, ATTENTION mais l'analyse continue (decide par Eric le 2026-10-18 : c'est elle qui dit quelles automations ou quels scripts ont change) ; (4) l'analyse lit les COPIES bak, plus H: ; (5) extraction de chaque unite dans `ReBuild\_tmp_trigul_profond\` ; (6) controle final : MD5 de la prod relu apres l'analyse, ATTENTION dans le rapport si la prod a bouge pendant l'analyse ; (7) comparaison au YAML local et ecriture de `historique\03_RAPPORTS\06_MD5\01_TRIGUL_PROFOND\trigul_profond_[YYYY-MM-DD].txt` (sauvegarde `.bak_date_heure` si le rapport du jour existe) ; (8) effacement du dossier temporaire. Le lanceur controle que le rapport contient la ligne `ETAPES :` et les lignes AUTOMATIONS et SCRIPTS, et signale tout ATTENTION. Prod toujours plus importante que le local : une prod en avance sur le local (unites DIFFERENT) est a signaler en premier.
2. Categories HA : lire `ha_config_get_category` (scopes automation et script), ecrire `historique\03_RAPPORTS\06_MD5\02_CATEGORIES_HA\categories_ha_[YYYY-MM-DD].txt` (lignes `scope | category_id | nom | icone`, triees, en-tete `CATEGORIES HA - date heure (lues via ha_config_get_category)`), comparer aux lignes de donnees de la version precedente du meme repertoire et signaler ajouts, suppressions, renommages. Releve du 2026-10-18 : 15 categories d'automations, 0 pour les scripts, inchangees.
3. Compte rendu : synthese du rapport profond, DIFFERENT et ABSENT_LOCAL (au 2026-10-18 : 62/62 automations identiques, 9/9 scripts identiques, trois exports locaux sans automation en prod : `Automations.yalm original\Automations.yaml`, `P1_SDB\h_soufflant_SDB_routage.yaml`, `P1_SDB\i_soufflant_SDB_bouton_rodret.yaml`), ecarts de categories. Ne rien corriger sans demande.

### C. Fichiers a plusieurs emplacements (script 3, decide le 2026-10-18)

Lancer : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_Docs_scripts\Docs_scripts_sh\Verif_emplacements\Verif_emplacements.py"`. Lecture seule. Carte : `docs\00_IA\SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md`.

- Fichiers suivis : tout `docs\01_docs_config_system\config_system_SH_PY_YAML\` (hors `.bak`, hors `notifs`, `themes`, `blueprints`, hors `secrets.yaml`, `scenes.yaml`, `ip_bans.yaml`) et, dans `config_system_MD`, `GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md` et `README\README.md`.
- 5 colonnes : L (local), PR (prod racine /config), PM (prod miroir docs), GR (GitHub racine), GD (GitHub docs/). Scripts : sous-dossiers `01_scripts.sh` / `02_scripts.py` en local, a plat dans `/config/.scripts/`.
- Verdicts : SYNC, PROD DIFFERENTE DU LOCAL, GITHUB EN ATTENTE DU BACKUP (normal juste apres un push), ABSENT (emplacements manquants) ; section 2 : PROD RACINE SEULE, PROD MIROIR SEUL, GITHUB RACINE SEUL, GITHUB DOCS SEUL ; section 3 ECARTS ATTENDUS : fichiers verrou d'editeur `#...#` en prod seule (non comptes dans les anomalies).
- Rapport : `historique\03_RAPPORTS\06_MD5\03_VERIF_EMPLACEMENTS\verif_emplacements_[YYYY-MM-DD].txt`, dernieres lignes `ANOMALIES` et `RESULTAT`.
- Releve du 2026-10-18 17:41 (commit f45a765c) : 97 fichiers suivis, 94 SYNC, 2 en attente du backup GitHub, 1 prod differente (`check_yaml_forme.py`), 1 verrou d'editeur en prod (depuis, ecart attendu, section 3 du rapport). Repere seulement : relire le rapport du jour.

### C2. Analyser les ecarts de l'etape C (repris de l'ancien skill ha-resync-docs, supprime le 2026-10-20 car doublon du trigul)

Le LOCAL fait foi, la prod ne doit jamais etre en avance sur le local, GitHub n'est qu'un reflet de la prod via le backup HA. Ne jamais copier GitHub vers le local sans ordre explicite d'Eric, fichier par fichier. Les dossiers `themes/`, `blueprints/` et `notifs/` restent en prod seule.

| Cas | Action |
|:----|:-------|
| PROD DIFFERENTE DU LOCAL | Le local fait foi : proposer `/ha-push-yaml`. Si la prod a ete modifiee a la main (ecart non explique), le signaler a Eric avant tout push. |
| GITHUB EN ATTENTE DU BACKUP | Normal apres un push : le backup HA lance par Eric mettra GitHub a jour. |
| Present en prod ou sur GitHub, absent du local | Le signaler a Eric (fichier cree en prod a la main ?). Copie vers le local uniquement sur son ordre. |
| Absent de la prod | Proposer `/ha-push-yaml`. |

Copie vers le local (uniquement sur ordre explicite d'Eric) : fichier par fichier, depuis la prod `H:\` (pas depuis GitHub, qui peut etre en retard), apres sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs` du fichier local s'il existe. Signaler chaque copie et l'ecrire au journal des modifs. Proposer /sync_index si des entites cles ont change.

Regles : `secrets.yaml` ne se copie JAMAIS, dans aucun sens. Les `.md` ne se synchronisent JAMAIS par ce skill (source de verite locale, geres par /ha-push-docs).

## Etat de reference du 2026-10-18 (08h02, GitHub au commit b6eddd9 du backup de 01h30)

Superposition : 567 chemins, 402 SYNC, 160 a traiter pour 214 diff au total, 5 ecarts attendus, controle du script OK. `RESULTAT AUDIT : 530 fichiers (184 .md - 338 .yaml - 8 .sh) - SYNC 398 - DIFF 2 - ABSENT LOCAL 88 - ABSENT 2 NIVEAUX 42`. Les 2 DIFF : Ha_git_backup.sh et le script du trigul (local different de la prod et de GitHub). Les 160 anomalies : 52 locaux seuls, 88 prod + GitHub sans chemin local (anciens noms, dont 14 .md orphelins sans equivalent local par le contenu ni le nom, et des fichiers de `_old_avant_staging`), 3 fichiers verrou d'editeur (2 en prod, 1 en local), 16 .svg des icones meteo attendant le backup HA (apres le backup, relancer le script : ils doivent passer SYNC), 2 locaux en avance. Profond : 62/62 automations, 9/9 scripts identiques. Ces chiffres sont des reperes, pas des valeurs a recopier : relire le rapport du jour.

Second releve du 2026-10-18 (relance du script 1 a 10h26, GitHub au commit c723097) : 477 chemins, 472 SYNC, 2 a traiter (les deux scripts du trigul, LOCAL en avance), 3 ecarts attendus. `RESULTAT AUDIT : 468 fichiers - SYNC 466 - DIFF 2`. Les 2 DIFF sont les deux scripts du trigul modifies en local et pas encore pousses en prod (attente d'un ordre d'Eric). Repere lui aussi : relire le rapport du jour.

## Compte rendu a l'utilisateur

- Mettre en tete les lignes ECHEC et ATTENTION du journal de trace du jour, s'il y en a.
- Donner les lignes `ANOMALIES`, `RESULTAT AUDIT` et `RESULTAT` du script 1, la synthese de l'etape profonde et les lignes `ANOMALIES` et `RESULTAT` du script 3, telles quelles.
- Lister les ecarts hors ecarts attendus : fichier, origine ou niveau en retard. Pour la section 1, donner le nombre par origine puis les exemples utiles ; le detail complet est dans le rapport. S'il n'y a pas d'anomalie, le dire (`ANOMALIES : aucune`).
- Une fois les resultats donnes, Eric cherche les fichiers manquants ou differents : proposer d'enqueter en lecture seule sur les groupes (empreinte identique sous un autre nom, anciens noms, orphelins) avant toute action.
- Donner les chemins des rapports, dans leurs repertoires numerotes de `historique\03_RAPPORTS\06_MD5\` (`00_VERIF_FINAL_TRIGUL_ARBRES`, `01_TRIGUL_PROFOND`, `02_CATEGORIES_HA`, `03_VERIF_EMPLACEMENTS`, `04_JOURNAL_TRIGUL`).
- Ne rien pousser, renommer ni supprimer sans demande, cas par cas. Pour une prod en retard, proposer ha-push-md, ha-push-docs ou ha-push-yaml. Pour GitHub : jamais de push direct, le depot est alimente par le backup HA lance par Eric.
- Ajouter une ligne au journal des modifs du jour pour les rapports ecrits (skill journal-modifs ; une ligne LOT suffit).
- Repondre en francais, concis, sans emojis ni tableaux.