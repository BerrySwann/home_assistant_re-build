# Check_qualite_docs.py - controle de validite des docs avant push

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--09-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Scripts-4fc3f7?style=flat-square)](.)

</div>

## Identite

- **Fichier** : `docs/04_docs_scripts/04_docs_scripts_SH/Check_qualite_docs/Check_qualite_docs.py`
- **Type** : script Python, LECTURE SEULE, ne corrige jamais
- **Cree le** : 2026-11-08, a la suite de la decouverte des six fichiers corrompus
- **Appele par** : `/histo` etape 5C, en tete du push, avant `Push_5C`

## Ce qu il controle

Trois tests, dans cet ordre. Un fichier qui echoue a l un n est pas teste au suivant.

**1. Octets de controle.** Tout octet inferieur a 0x20, sauf tabulation (0x09), CR (0x0D) et LF (0x0A). Ces octets sont le plus souvent les degats d une sequence d echappement interpretee au lieu d etre ecrite : `\0` donne un NUL, `\a` un BEL, `\b` un retour arriere, `\10` en octal un autre retour arriere.

**2. BOM et remplissage.** Deux cas de gravite differente.
Un fichier qui finit par des octets NUL est toujours anormal : c est de la place reservee et jamais remplie. **Le mecanisme est ETABLI par reproduction le 2026-11-08, ce n est plus une hypothese** : un `FileStream` ouvert en `FileMode.Create`, puis `SetLength(Preamble.Length + Bytes.Length)`, puis l ecriture des bytes SANS ecrire le preambule. La taille reserve trois octets pour une BOM UTF-8 que l ecriture n ecrit jamais, et ils restent a zero. Reproduit exactement le symptome : 9266 octets au lieu de 9263, debut sans BOM, fin `00 00 00`.
**Signature a reconnaitre a coup sur** : un fichier de 3 octets de plus que sa taille reelle, qui finit par `00 00 00`, et dont le debut ne porte pas de BOM. Les autres methodes testees ne produisent jamais ca : `Out-File` et `Set-Content -Encoding utf8` ajoutent une BOM et un CRLF, `WriteAllText` avec `UTF8Encoding(true)` met la BOM en tete et finit proprement, `FileStream` AVEC preambule finit proprement.
Une BOM en tete est **fatale** sur `.json` et `.sh`, qui ne l acceptent pas. Sur les autres formats, PyYAML et Python 3 la tolerent : c est une incoherence, **signalee en INFO sans bloquer**. Au 2026-11-08, 7 fichiers YAML du depot en portent une et se parsent tous tres bien.

**3. Parse YAML reel**, sur chaque `.yaml` et `.yml`. Utilise un analyseur qui ACCEPTE les tags Home Assistant `!include`, `!secret`, `!input`, `!env_var` et compagnie, sinon il produit des fausses alertes en masse. Accepte aussi les fichiers a plusieurs documents separes par `---`.

## Perimetre

Tout `docs`, recursif. **Exclus** : `__pycache__`, `node_modules`, `.git`, `Dashboard_COMPLET`, les dossiers `XX_` et `99_`, et tout ce qui contient `.bak` ou finit par `.bak`, `.pyc`, `.log`.

Extensions testees : `.md`, `.yaml`, `.yml`, `.py`, `.sh`, `.txt`, `.json`.

**Porte sur le LOCAL**, jamais sur la prod. Le local fait foi, la prod recoit ; controler la prod apres coup revele les degats au lieu de les empecher.

## Sorties et codes

- **Code 0** : tout est propre, `RESULTAT : OK`, le push peut partir.
- **Code 1** : au moins un fichier en alerte. Il est liste sous `A EXCLURE DU PUSH`. Les autres fichiers partent normalement.
- **Code 2** : outil mal arme (PyYAML absent, dossier `docs` introuvable).

**Un fichier qui echoue est EXCLU du push et signale : il ne bloque pas la session.** C est la regle des garde-fous du 2026-11-03, la meme que `Check_XX_presents.py`.

## Pourquoi ce controle existe

Le 2026-11-08, six fichiers de `docs` portaient des octets de controle issus de sequences d echappement interpretees. L un d eux, `Card_prog_clim_chambre.yaml`, etait REELLEMENT CASSE : `yaml.safe_load` le refusait, `unacceptable character #x0000`. Il etait present en local, en prod et sur GitHub depuis des semaines, et **aucun controle ne l a vu**.

La raison est structurelle : **MD5 compare deux etats, il ne dit rien de leur qualite.** Une corruption identique en local, en prod et sur GitHub donne trois empreintes concordantes. Le trigul voit SYNC, `Check_prod_fonctionnelle` voit quatre colonnes vertes, et le document reste illisible pour tout parseur. Un defaut copie fidelement est invisible a tout controle de synchronisation.

C est pourquoi ce test porte sur la VALIDITE et non sur la comparaison, et pourquoi il tourne avant le push plutot qu apres.

## Placement dans /histo

Etape 5C, en tete. Apres toutes les ecritures (journal, sync index, fusionne, Obsidian, menage, export dashboard, copies de reference), pour valider ce qui part vraiment ; et avant l envoi, pour ne pas propager vers `H:` puis vers GitHub au backup suivant. Place a l etape 6, apres le push, il n aurait servi a rien.

## Limites connues

- Il ne dit rien de la **validite semantique** d un YAML : un document peut se parser et etre faux.
- Il ne teste que `docs`. `H:` racine et `H:/.storage` ont ete scannes une fois a la main le 2026-11-08 (36 fichiers texte, propre), mais ne sont pas couverts a chaque passage.
- Les `.bak` sont exclus : un `.bak` corrompu ne declenche rien.
