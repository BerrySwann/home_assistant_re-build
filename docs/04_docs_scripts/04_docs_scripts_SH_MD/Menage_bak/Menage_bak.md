# Menage_bak.py - menage des .bak

## Identite

- **Fichier** : `docs/04_docs_scripts/04_docs_scripts_SH/Menage_bak/Menage_bak.py`
- **Type** : script Python, lecture seule par defaut, action seulement avec `--go`
- **Cree le** : 2026-11-08 (R77.1, ferme la decision d'Eric du 2026-10-18)
- **Origine** : le menage des `.bak` etait refait a la main a chaque `/histo`, en suivant `histo_ref_menage.md`. Eric a demande qu il devienne un vrai script range, pour ne plus dependre d une lecture de consigne a chaque fois.

## Ce qu il fait

Applique la REGLE DE SAUVEGARDE de `CLAUDE.md` sur deux plafonds :

- **`.bak` horodates du jour** (`fichier.bak_AAAA_MM_JJ_HHhMMmSSs.ext`) : 10 au maximum par fichier d origine. Le 11e envoie le plus ancien a la corbeille.
- **`.bak` dates des jours passes** (`fichier.bak_AAAA_MM_JJ.ext`) : 3 jours differents au maximum par fichier. Au-dela, les `.bak` des jours les plus anciens partent.

**Aucune suppression definitive.** Tout passe par la CORBEILLE WINDOWS (`SHFileOperationW` avec `FOF_ALLOWUNDO`), donc tout est restaurable. Le script ne vide JAMAIS la corbeille : c est une action separee et volontaire.

## Perimetre

**Traite** : `docs/00_*` a `docs/05_*`, recursif, plus `Claude md SAVE`.

**Jamais touche** : `TODO`, `Github`, `historique`, `Infra_Proxmox`, `_old_avant_staging`, `99_docs_MD_system`, `TEMPO`, `__pycache__`, `.git`.

Les `.bak` du jour ne sont jamais touches a la main : seuls les depassements les font partir.

## Usage

```bash
# dry-run : affiche le plan, ne touche a rien
python -I -X utf8 Menage_bak.py

# execution : envoie a la corbeille
python -I -X utf8 Menage_bak.py --go
```

Codes de sortie : 0 = rien a faire ou tout fait, 1 = echec.

## Noms hors format

Le script **signale** les `.bak` dont le nom ne respecte pas la convention, il ne les renomme jamais lui-meme. Le menage manuel des noms reste une decision humaine : renommer un fichier qu on n a pas nomme est une faute (regle de securite des fichiers).

Format degrade connu : `fichier.bak_2026_11_04_20h_45m05s.md`, avec un underscore parasite dans l heure. Repere, non traite.

## Place dans /histo

Etape 5 (BACKUP CLEANUP), a la place du menage refait a la main. Le dry-run s affiche, et l execution `--go` demande l accord d Eric a la premiere passe sur un dossier. La premiere execution est toujours en dry-run.

## Historique

- **2026-11-08** : creation. Premier dry-run sur le depot reel : 448 fichiers porteurs, 1103 `.bak`, 20 a envoyer a la corbeille, 16 noms hors format.
