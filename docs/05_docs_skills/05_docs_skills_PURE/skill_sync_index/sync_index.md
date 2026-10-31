---
name: "sync-index"
description: "HA ReBuild skill - updates DEPENDANCES_GLOBALES_CLAUDE_memoire.md and the project index after a YAML file is validated. MUST trigger when the user types /sync_index, says \"met a jour l'index\", \"synchronise les dependances\", \"update DEPENDANCES_GLOBALES\", after validating or fixing a config, automation or script YAML file, or when a modified entity impacts a dashboard tile."
---

# Skill: /sync_index - Update of the index and dependencies

> Files present in several locations (config, GLOBAL_INDEX_REPO, README): see `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 locations: local, prod root, prod docs mirror, GitHub root, GitHub docs/) and the read-only check `docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py` (decided by Eric on 2026-10-18).

## Goal

After a YAML file (config, automation or script) is validated, update the dependency
documentation to keep the project consistent.

## Scope

| Type of validated file | Source folder |
|:---|:---|
| HA config (sensors, templates, utility_meter...) | `docs/01_docs_config_system/01_config_system_SH_PY_YAML/` |
| Automation | `docs/03_docs_automations/03_docs_automations_YAML/` |
| Script | `docs/04_docs_scripts/04_docs_scripts_YAML/` |

## Files to update depending on the type

| Validated type | Index file to update |
|:---|:---|
| Config YAML | `docs/00_IA/00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.md` |
| Automation | `docs/03_docs_automations/03_docs_automations_MD/{nom_automation}.md` + automations index if it exists |
| Script | `docs/04_docs_scripts/04_docs_scripts_YAML_MD/{nom_script}.md` |
| Any type impacting a tile | `DEPENDANCES_GLOBALES_CLAUDE_memoire.md` |

**Windows paths:**
- `C:\Users\Berry Swann\Documents\ReBuild\docs\00_IA\00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire\DEPENDANCES_GLOBALES_CLAUDE_memoire.md`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\03_docs_automations\03_docs_automations_MD\`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_YAML_MD\`

## Execution protocol

### 1. Identify the type and the impacted entities

Determine:
- **Type**: config YAML / automation / script
- **unique_id** or alias of the entity/automation/script
- **Source file** (path in the right folder)
- **Tile(s) concerned** (L1C1 to L6C3) if applicable

### 2. Update DEPENDANCES_GLOBALES_CLAUDE_memoire.md (if config or tile impacted)

Read the file, locate the lines concerned, change the non-valid statuses -> OK.
Fill the "Fichier source" and "Entite" columns if empty.
Update the date at the top of the file.

### 3. Update the automation doc (if automation validated)

Check whether a `.md` file exists in `docs/03_docs_automations/03_docs_automations_MD/` for this automation.
- If yes: update the "Etat" or "Derniere validation" section.
- If not: report that a doc is missing and propose to create it.

### 4. Update the script doc (if script validated)

Check whether a `.md` file exists in `docs/04_docs_scripts/04_docs_scripts_YAML_MD/` for this script.
- If yes: update the "Etat" section.
- If not: report that a doc is missing and propose to create it.

### 5. Answer format (labels stay in French)

```
SYNC_INDEX - [today's date]

Type valide : [config YAML / automation / script]
Fichier     : [short path]
Entite/alias: [unique_id or alias]
Vignette    : [L*C* or N/A]

Mises a jour :
- DEPENDANCES_GLOBALES_CLAUDE_memoire.md : [line] -> OK  (if applicable)
- 03_docs_automations_MD/{nom}.md : [section updated]  (if automation)
- 04_docs_scripts_YAML_MD/{nom}.md : [section updated]  (if script)
```

### 6. If an index file is missing or incomplete

Report: `>> {fichier} introuvable ou incomplet - verifier le chemin`
Propose to create/complete the missing section.

## Rules

- **Rewrite only the lines concerned** - not the whole file (saves tokens).
- If no dependency is impacted: answer "Index deja a jour - aucune action" (1 line).
- The file paths quoted in DEPENDANCES_GLOBALES_CLAUDE_memoire.md must have the exact case of the disk (GitHub is case-sensitive; resync of 2026-10-18).

## Maintenance note

This is the usable English copy of the skill (written in English to save tokens). Paths, file names, entity ids and report labels stay in French. The French explanation sheet is `docs/05_docs_skills/05_docs_skills_MD/skill_sync_index/sync_index.md`: when this file changes, re-read that sheet and update it. The installed skill `.claude/skills/sync-index/SKILL.md` must stay identical to this copy.
