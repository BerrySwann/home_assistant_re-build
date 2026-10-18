---
name: "ha-resync-docs"
description: "Skill HA ReBuild - compare les fichiers YAML config locaux a la prod et a GitHub (lecture seule par defaut ; le local fait foi). Declencher sur : \"resync depuis GitHub\", \"compare local vs GitHub\", \"audit MD5 YAML\", \"est-ce que le local est a jour\", \"debut de session\", \"on commence par un audit\"."
---

# HA Resync Docs - comparaison config locale / prod / GitHub

> Fichiers presents a plusieurs emplacements (config, GLOBAL_INDEX_REPO, README) : voir `docs\00_IA\SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 emplacements : local, prod racine, prod miroir docs, GitHub racine, GitHub docs/) et le controle en lecture seule `docs\04_Docs_scripts\Docs_scripts_sh\Verif_emplacements\Verif_emplacements.py` (decide par Eric le 2026-10-18).

> ATTENTION (2026-10-18) : le LOCAL fait foi, la prod ne doit jamais etre en avance sur le local et GitHub n'est qu'un reflet de la prod via le backup HA. Ne jamais copier GitHub vers le local sans ordre explicite d'Eric, fichier par fichier. Les dossiers `themes/`, `blueprints/` et `notifs/` restent en prod seule.

Compare les fichiers YAML de config locaux avec la prod (`H:\`, racine et miroir docs) et le repo GitHub (`home_assistant_re-build`), reflet de la prod HA.

## CHEMINS DE REFERENCE

- **Local (Windows)** : `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_SH_PY_YAML\`
- **Automations local** : `docs\03_docs_automations\docs_automations_YAML\` (comparaison unite par unite : etape profonde de /ha-trigul)

## WORKFLOW

### 1 - Comparer (lecture seule, sur le PC)

```powershell
$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_Docs_scripts\Docs_scripts_sh\Verif_emplacements\Verif_emplacements.py"
```

Le script compare chaque fichier de `config_system_SH_PY_YAML` aux 5 emplacements (local, prod racine, prod miroir docs, GitHub racine, GitHub docs/) et ecrit `historique\MD5\03_verif_emplacements\verif_emplacements_[date].txt`. Il lit GitHub par l'API (une requete), il doit tourner sur le PC.

Statuts : SYNC / PROD DIFFERENTE DU LOCAL / GITHUB EN ATTENTE DU BACKUP / ABSENT (emplacements manquants) ; section 2 : fichiers presents en prod ou sur GitHub mais pas en local.

### 2 - Analyser les ecarts

| Cas | Action |
|:----|:-------|
| PROD DIFFERENTE DU LOCAL | Le local fait foi : proposer `/ha-push-yaml`. Si la prod a ete modifiee a la main (ecart non explique), le signaler a Eric avant tout push. |
| GITHUB EN ATTENTE DU BACKUP | Normal apres un push : le backup HA lance par Eric mettra GitHub a jour. |
| Present en prod ou sur GitHub, absent du local | Le signaler a Eric (fichier cree en prod a la main ?). Copie vers le local uniquement sur son ordre. |
| Absent de la prod | Proposer `/ha-push-yaml`. |

### 3 - Copie vers le local (uniquement sur ordre explicite d'Eric)

Fichier par fichier, depuis la prod `H:\` (pas depuis GitHub, qui peut etre en retard), apres sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs` du fichier local s'il existe. Signaler chaque copie et l'ecrire au journal des modifs.

### 4 - Resume
- Lignes `ANOMALIES` et `RESULTAT` du script
- Fichiers en ecart et action proposee
- Proposer /sync_index si des entites cles ont change

## REGLES

1. Lecture seule par defaut : aucun fichier local ni prod modifie sans ordre d'Eric.
2. Ne jamais ecraser un fichier local sans le signaler.
3. secrets.yaml -> NE JAMAIS COPIER dans aucun sens.
4. docs/ du repo GitHub = documentation : comparee par /ha-trigul, pas ici (sauf le miroir de config controle par le script).
5. ***.md -> NE JAMAIS SYNCHRONISER** dans aucun sens par ce skill. Les .md sont la source de verite locale, geres par /ha-push-docs.