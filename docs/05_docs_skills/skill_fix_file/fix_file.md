---
name: "fix-file"
description: "Skill HA ReBuild - analyse une erreur Home Assistant et retourne UNIQUEMENT le bloc YAML corrige. Declencher OBLIGATOIREMENT quand l'utilisateur tape /fix_file, colle un log HA, une trace d'erreur, un message \"invalid config\", \"error loading\", \"unknown platform\", ou demande de corriger/reparer un fichier YAML Home Assistant. S'active aussi sur : \"ca plante\", \"erreur HA\", \"fix this YAML\", \"corrige le fichier\", ou tout message contenant une trace d'erreur HA a resoudre."
---

# Skill : /fix_file - Correcteur YAML Home Assistant

> Fichiers presents a plusieurs emplacements (config, GLOBAL_INDEX_REPO, README) : voir `docs\00_IA\00_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 emplacements : local, prod racine, prod miroir docs, GitHub racine, GitHub docs/) et le controle en lecture seule `docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py` (decide par Eric le 2026-10-18).

## Objectif

L'utilisateur fournit une erreur HA (log, trace, message UI) et/ou un bloc YAML defaillant.
Retourner **uniquement** le bloc corrige - aucun discours superflu.

## Protocole d'execution

### 1. Identifier l'erreur

Reperer :
- Le **fichier source** (sensors/, templates/, utility_meter/, command_line/)
- Le **type d'erreur** (YAML syntax, entite inconnue, plateforme deprecee, unique_id manquant, etc.)
- Le **bloc precis** a corriger

Si le fichier existe dans `01_config_system_SH_PY_YAML/` (local), le lire avant de corriger.

**Chemin local :** `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\`

### 2. Appliquer les regles du projet

**Fichiers modulaires** (sensors, templates, utility_meter, command_line) :
- Bordure ASCII titre principal coins arrondis - 78 caracteres total
- Slug tertiaire `# --- unique_id_exact ---` au-dessus de chaque entite
- `name:` avec majuscules initiales + prefixe pole
- `unique_id:` minuscules + underscores

**Convention notify** : `notify.file` interdit -> remplacer par `notify.file_diag_log_file`

### 3. Format de reponse

```
[NOM_FICHIER] - [TYPE ERREUR]

[bloc YAML corrige uniquement]

# annotations_log:
# L.XX : [description courte de la correction]
```

- Ne jamais renvoyer le fichier complet sauf demande explicite
- Annoter chaque ligne modifiee avec `# "[L...] modif"`
- Bloc `# annotations_log:` obligatoire en fin de reponse
- La correction se fait en local ; la mise en prod passe par `/ha-push-yaml` (racine `H:\` ET miroir docs).

### 4. Verification dependances (rapide)

Si l'entite modifiee peut impacter une vignette ou `DEPENDANCES_GLOBALES.md`, signaler :
`>> Impact potentiel : [vignette L*C*] - /sync_index recommande`

**Chemin DEPENDANCES_GLOBALES :** `docs\XX_docs_MD_system\DEPENDANCES_GLOBALES\DEPENDANCES_GLOBALES.md`