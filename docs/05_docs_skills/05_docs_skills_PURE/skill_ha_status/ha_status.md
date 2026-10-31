---
name: ha-status
description: >
  HA ReBuild skill - produces an ultra-compact 3-point summary of the project progress.
  MUST trigger when the user types /status, or asks "ou en est le projet", "quel est l'avancement",
  "resume la situation", "c'est quoi l'etat actuel", "on en est ou",
  or asks for a quick review of what was done / what remains to do in the HA ReBuild project.
  Saves tokens: avoids re-reading the whole conversation history.
---

# Skill: /ha_status - HA ReBuild project progress

## Goal

Summarize the project state in **3 points maximum**, ultra-compact.
No speech, no repetition of code that is already validated.

## Execution protocol

### 1. Read the available sources

In priority order:
1. The history of the current conversation (files mentioned, validations, errors)
2. `docs\00_IA\` (state of the chains)
3. Recent files in `docs\01_docs_config_system\01_config_system_SH_PY_YAML\` (modification dates)

### 2. Mandatory answer format (labels stay in French, Eric reads them)

```
STATUS - [today's date]

[1] FAIT    : [short list of files/entities validated recently]
[2] EN COURS : [task or file currently being processed]
[3] SUIVANT  : [next priority action identified]

Blocages : [aucun | short description if blocking]
```

### Brevity rules

- Maximum 2 lines per point
- Use the matrix IDs (L1C1, P2, etc.) to reference tiles and poles
- Use short file names (e.g. `P1_kWh_clim_chauffage.yaml`)
- If nothing was done in the session: `[1] FAIT : aucune modification validee dans cette session`
- Never repeat YAML content already posted in the conversation

## Maintenance note

This is the usable English copy of the skill (written in English to save tokens). Paths, file names, entity ids and report labels stay in French. The French explanation sheet is `docs/05_docs_skills/05_docs_skills_MD/skill_ha_status/ha_status.md`: when this file changes, re-read that sheet and update it. The installed skill `.claude/skills/ha-status/SKILL.md` must stay identical to this copy.
