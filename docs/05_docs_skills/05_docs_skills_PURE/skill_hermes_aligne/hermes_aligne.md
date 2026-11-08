---
name: "hermes-aligne"
description: "Alignement d'Hermes sur Claude en LECTURE SEULE. Declencher quand Eric dit : aligne-toi, t'aligner, s'aligner, alignement, fais un clone de Claude, prends les infos de Claude. Hermes lit les regles et les modifications de Claude, les assimile et le dit. Il ne cree, ne modifie, ne renomme, ne deplace et ne supprime AUCUN fichier ni dossier, nulle part (ReBuild, H:, D:, GitHub, skills d'Hermes compris), sauf un message PROPOSITION dans sa propre boite d'echanges."
---

# Skill : hermes-aligne - s'aligner = LIRE, jamais ECRIRE

## Ce que veut dire "aligne-toi" (decision d'Eric, 2026-10-18)

Quand Eric dit "aligne-toi" ou "s'aligner", Hermes prend les infos de Claude et les infos que Claude a modifiees, les lit, les assimile et se comporte ensuite comme Claude : memes regles, memes protocoles, meme facon de verifier. C'est un clone de comportement, dans sa tete, pour la session.

S'aligner ne veut PAS dire : mettre les fichiers d'Hermes au meme etat que ceux de Claude, copier, synchroniser, nettoyer, ranger, restaurer ou corriger quoi que ce soit. Rien n'est ecrit.

## Pourquoi ce skill (incident du 2026-10-17, lu dans MODIFS_2026-10-17_hermes.md)

Pour s'aligner, Hermes a fait `rm -rf` de `docs\00_IA\sous_context_ia` et de `docs\00_IA\SOUS_CONTEXT_IA`, en les prenant pour un doublon. Sur Windows et sur la prod H: (partage SMB), les noms ne tiennent pas compte de la casse : c'etait UN SEUL dossier. Ensuite il a supprime aussi `H:\docs\00_IA\sous_context_ia`. Il a fallu restaurer depuis GitHub, la corbeille Windows et des .bak. Une version (IA_ARBO_DETAIL du 15h48) a failli etre perdue. Le 17/10 a 16h10, il avait aussi ecrase deux SKILL.md de `D:\hermes\skills` pour "realigner". Ce skill existe pour que cela ne se reproduise plus.

## Regle absolue : ZERO ecriture pendant un alignement

Interdit, sans exception, quel que soit le lieu (ReBuild local, H:, D:, GitHub, `C:\Users\Berry Swann\AppData\Local\hermes\skills`, le dossier de travail d'Hermes) :
- creer, modifier, ecraser, renommer, deplacer, copier-sur, supprimer un fichier ou un dossier (`rm`, `rm -rf`, `rmdir`, `del`, `Remove-Item`, `mv`, `Move-Item`, `cp`, `Copy-Item`, `>`, `>>`, `tee`, `sed -i`, `Set-Content`, `Out-File`) ;
- git (add, commit, push, checkout, reset, clean) ;
- lancer un script qui ecrit (trigul, menage, generateurs d'index, backup) ;
- ecrire une ligne de journal : il n'y a rien a journaliser puisque rien n'est modifie ;
- vider une corbeille, restaurer depuis une corbeille ou depuis un .bak.

Meme si Hermes pense bien faire. "Doublon", "fichier en trop", "ancienne version", "menage", "mise a jour evidente", "differences a corriger" : ce sont des constats a rapporter a Eric, jamais des actions.

Une seule exception (decision d'Eric, 2026-11-01 09h32) : un message `PROPOSITION` ajoute a sa propre boite d'echanges (voir plus bas).

## Commandes autorisees (liste fermee)

Lecture uniquement : `cat`, `type`, `Get-Content`, `ls`, `dir`, `Get-ChildItem`, `Test-Path`, `Get-FileHash` / `md5sum`, `grep` / `Select-String`, `wc`, `diff` / `Compare-Object` (comparaison affichee a l'ecran, pas de sortie vers un fichier).

Avant CHAQUE commande, se poser une seule question : "cette commande ecrit-elle quelque chose ?". Si la reponse est oui ou "je ne suis pas sur", ne pas la lancer.

## Que lire (dans cet ordre)

Si un chemin est inaccessible, le dire a Eric et continuer avec le reste. Ne pas chercher ailleurs, ne rien creer pour le remplacer.

1. Les regles de Claude : `C:\Users\Berry Swann\Documents\ReBuild\Claude md SAVE\CLAUDE.md`. `IA_CONTEXT_BASE.md` (`docs\00_IA\00_IA_CONTEXT_BASE\`, copies `D:\docs\00_IA\IA_CONTEXT_BASE.md` et `H:\docs\00_IA\00_IA_CONTEXT_BASE\`) n'est PAS une copie MD5 identique de `CLAUDE.md` : les deux fichiers sont lus separement, et seules les trois copies d'`IA_CONTEXT_BASE.md` se comparent entre elles. Noter le MD5 (8 caracteres) de chacun.
2. L'index IA : `docs\00_IA\00_IA_GLOBAL_INDEX_memoire\IA_GLOBAL_INDEX_memoire.md`, puis les fichiers de `docs\00_IA\00_IA_SOUS_CONTEXT_IA\` dont l'index dit qu'ils servent a la tache d'Eric. Matrice commune des dependances (elle part en prod au push 5C) : `docs\00_IA\00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire\DEPENDANCES_GLOBALES_CLAUDE_memoire.md`.
3. Ce que Claude a fait et dit : `historique\03_RAPPORTS\01_MODIFS_IA\MODIFS_AAAA-MM-JJ_claude.md` (aujourd'hui et la veille ; pas de copie sur H: depuis le 2026-10-22), les messages de Claude `C:\Users\Berry Swann\AppData\Local\hermes\Discussion_Claude_Hermes\echanges_AAAA-MM-JJ_claude.md` (aujourd'hui et la veille : c'est la que Claude passe les decisions d'Eric), puis les pages `histo_AAAA-MM-JJ.html` de `historique\02_HISTO_ET_FUSIONNE\` et le `JOURNAL_FUSIONNE_*` le plus recent de `historique\02_HISTO_ET_FUSIONNE\FUSIONNE\`.
4. Les skills de Claude : `docs\05_docs_skills\05_docs_skills_PURE\skill_<nom>\<nom>.md` (copies utilisables, en anglais), leurs fiches francaises dans `docs\05_docs_skills\05_docs_skills_MD\`, et la liste dans `docs\05_docs_skills\MOC_SKILLS.md`. Lire ceux qui concernent la demande d'Eric ; si Eric n'en designe aucun, lister les noms et lui demander lesquels.
5. Les memoires et preferences qu'Eric designe (par exemple ses regles de verification, de format, de langue).

Un fichier de sauvegarde (`.bak_...`) n'est jamais une source : seul le fichier courant compte.

## Comment s'aligner (dans la tete d'Hermes, pas sur le disque)

1. Dire d'abord : "ALIGNEMENT en lecture seule : je n'ecris rien."
2. Lire les sources ci-dessus. Pour chaque fichier lu : chemin, date de modification, MD5 (8 premiers caracteres).
3. Retenir et appliquer des maintenant, comme Claude : repondre en francais ; concis et direct ; verifier avant d'affirmer (chaque fait precis est "etabli" avec sa source, "deduit" avec son raisonnement, ou "inconnu" sans valeur approximative) ; dire a Eric quand un de ses faits ou choix parait faux ; signaler un prompt imprecis avant de le traiter ; typographie ASCII sans caractere Alt ; la REGLE DE SAUVEGARDE, la corbeille Windows, le journal des modifs, "ne jamais supprimer sur H: sans copie locale verifiee", "ne jamais pousser un script ou un skill sans l'ordre d'Eric".
4. Une regle recue se recopie avec son EXCEPTION, sa date et son decideur, jamais en resume plat (par exemple "99_ local seul" sans "sauf ENTITES_GLOBAL_INDEX.md, Eric 2026-10-31 17h33" est une regle fausse).
5. Ne pas reecrire ses propres skills ni sa memoire pour "fixer" l'alignement. Si Eric veut que l'alignement soit durable, il le demande explicitement, et c'est une autre operation (voir plus bas).

## Regles de Claude a appliquer (decisions d'Eric, a relire dans CLAUDE.md ; le texte de CLAUDE.md fait foi)

- Dossiers `XX_*` : LOCAL SEUL, jamais en prod ni sur GitHub ; leur liste est celle du manifeste `docs\04_docs_scripts\04_docs_scripts_JSON\Check_XX_presents\XX_manifest.json` (a ne pas deplacer, renommer ni regenerer : propriete de Claude, mise a jour `--maj` seulement sur ordre d'Eric).
- `99_docs_MD_system` : local seul, SAUF le fichier `99_docs_MD_system\ENTITES_GLOBAL_INDEX\ENTITES_GLOBAL_INDEX.md` (jamais ses `.bak`), qui part en prod au 5C (Eric, 2026-10-31 17h33 ; autorise par `PROD_AUTORISE` de `Check_XX_presents.py`).
- `98_sauvegarde_hors_docs` : copie de `Infra_Proxmox`, `TODO` et `historique` faite par `Sync_98_sauvegarde.py` (avant chaque 5C), secrets caviardes ; elle VA EN PROD avec le 5C (Eric, 2026-10-31).
- Push general 5C : tout `docs` hors dossiers `XX_`, hors `.bak`, hors `99_docs_MD_system` sauf `ENTITES_GLOBAL_INDEX.md` ; `98_sauvegarde_hors_docs` INCLUS ; MD5 avant et apres ; jamais sans ordre d'Eric.
- TEMPO (`ReBuild\TEMPO`) : par defaut, copie dans `TEMPO\<operation>_AAAA-MM-JJ\`, MD5 de chaque fichier, copies a la corbeille Windows, puis suppression sur H: ; les copies ne restent dans TEMPO qu'apres un gros changement ou pour un fichier dit critique ; ces dossiers sont vides par ERIC SEUL. Tri en `Groupe_A`, `Groupe_B`, `Groupe_C` fait par Claude, A et B a la corbeille seulement apres le go d'Eric (2026-11-01). Hermes ne range ni ne supprime rien dans TEMPO ; `XX_sauvegarde_2026-10-25` reste a la racine.
- Sauvegarde `.bak` : a cote du fichier modifie, jamais sur H: ni dans `D:\docs` et les autres copies de ReBuild ; les fichiers d'Hermes de `C:\Users\Berry Swann\AppData\Local\hermes` gardent leur `.bak` a cote d'eux, sur D: (Eric, 2026-11-01 09h25).
- Chaque fiche `.md` porte 8 badges ; une fiche par script (sh, py, yaml) meme en doublon, le doublon est note dans toutes les fiches du meme contenu, et chaque fiche cite le nom exact de son fichier source.
- Index par type de script : `docs\04_docs_scripts\GLOBAL_INDEX_SCRIPTS_SH.md`, `_PY.md`, `_YAML.md`, tries comme `MOC_SCRIPTS.md` (scripts qui tournent dans HA / qui ne tournent pas, IA Claude / IA Hermes, par type).
- Trace en trois endroits pour toute modification : `.bak`, ligne du journal MODIFS, et ligne `annotations_log` dans le fichier (skill journal-modifs).

## Proposer une amelioration pendant un alignement (decision d'Eric, 2026-11-01 09h32)

Pendant ou a la fin d'un alignement, si une amelioration te vient (une regle, un skill, un script, une fiche, un index, un chemin, ton propre fonctionnement ou celui de Claude), tu la donnes a Claude. Forme : un message `PROPOSITION` dans `C:\Users\Berry Swann\AppData\Local\hermes\Discussion_Claude_Hermes\echanges_AAAA-MM-JJ_hermes.md`, une idee par message, avec le fichier concerne, le constat prouve (chemin, ligne, MD5 si utile), la modification proposee et le gain attendu. C'est la SEULE ecriture permise pendant un alignement. Tu ne fais JAMAIS la modification toi-meme : Claude la traite avec Eric, qui donne le go fichier par fichier. Aucune idee : tu n'ecris rien et tu ne le dis pas.

## Rapport de fin d'alignement (dans la conversation uniquement)

Court, en prose ou liste simple, sans tableau :
- sources lues (chemin, date, MD5) et sources inaccessibles ;
- les regles de Claude retenues, en une dizaine de lignes au plus, celles qui changent le comportement d'Hermes ;
- les ecarts constates entre ce que fait Hermes aujourd'hui et ce que fait Claude, avec le chemin du fichier concerne : LISTE SEULE, aucune correction ;
- les doublons, dossiers en trop, noms de casse differente, versions anciennes vus pendant la lecture : LISTE SEULE ; on ne les touche pas ;
- les points sur lesquels il hesite ou qu'il ne sait pas : "inconnu", jamais une valeur devinee ;
- la phrase finale : "Aucun fichier ni dossier n'a ete cree, modifie ou supprime, sauf les messages PROPOSITION de ma boite d'echanges."

## Si Eric veut ensuite un changement (operation separee, jamais automatique)

Un alignement ne se transforme jamais tout seul en modification. Pour changer un fichier, Eric doit le demander en nommant le fichier. Alors, et seulement alors :
1. montrer d'abord ce qui va changer (ancien contenu, nouveau contenu, MD5 avant) et attendre son "go" pour ce fichier ;
2. faire la sauvegarde `nom.bak_AAAA_MM_JJ_HHhMMmSSs.ext` a cote du fichier (jamais sur H:, ni dans les copies de ReBuild sur D: ; pour un fichier d'Hermes sur C:\Users\Berry Swann\AppData\Local\hermes, a cote de lui), 10 au plus le jour meme, 3 `.bak_AAAA_MM_JJ` pour les jours passes (dans `historique\` : une seule `.bak_AAAA_MM_JJ` par fichier et par jour, gardee indefiniment, sans plafond de jours, decision d'Eric le 2026-10-21) ;
3. une suppression n'est jamais faite sans que Eric ait nomme le fichier ou dossier ; elle passe par la corbeille Windows ; sur H: (pas de corbeille) : copie dans `ReBuild\TEMPO\<operation>_AAAA-MM-JJ\`, MD5 de chaque copie, puis seulement si tous les MD5 correspondent, copies a la corbeille Windows et suppression sur H: (les copies ne restent dans TEMPO que dans les deux cas de la regle TEMPO ci-dessus) ;
4. noter une ligne dans `historique\03_RAPPORTS\01_MODIFS_IA\MODIFS_AAAA-MM-JJ_hermes.md` (jamais sur `H:\docs\modifs\` : plus d'ecriture ni de copie sur H: depuis le 2026-10-22, decision d'Eric), et la ligne `annotations_log` dans le fichier ;
5. verifier le MD5 apres l'ecriture et le dire.

## En cas de doute

Hermes s'arrete et demande a Eric, en une question courte. Un doute sur le nom d'un dossier, sur la casse, sur "est-ce un doublon", sur "est-ce que je peux ecrire" : on ne devine pas, on ne supprime pas, on demande.