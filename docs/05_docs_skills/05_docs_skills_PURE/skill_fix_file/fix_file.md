---
name: "fix-file"
description: "HA ReBuild skill - analyses a Home Assistant error and returns ONLY the corrected YAML block. MUST trigger when the user types /fix_file, pastes an HA log, a stack trace, an \"invalid config\", \"error loading\" or \"unknown platform\" message, or asks to fix/repair a Home Assistant YAML file. Also triggers on: \"ca plante\", \"erreur HA\", \"fix this YAML\", \"corrige le fichier\", or any message containing an HA error trace to solve."
---

# Skill: /fix_file - Home Assistant YAML fixer

> Language note: this skill is written in English to save tokens. Paths, file names and entity names stay in French on purpose (real names on disk). Eric talks French: replies to him are in French. French explanation sheet: `docs\05_docs_skills\05_docs_skills_MD\skill_fix_file\fix_file.md` (re-read and update it whenever this skill changes).

> Files present at several locations (config, GLOBAL_INDEX_REPO, README): see `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 locations: local, prod root, prod docs mirror, GitHub root, GitHub docs/) and the read-only check `docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py` (decided by Eric on 2026-10-18).

## Goal

The user provides an HA error (log, trace, UI message) and/or a faulty YAML block.
Return **only** the corrected block - no superfluous talk.

## Execution protocol

### 1. Identify the error

Find:
- The **source file** (sensors/, templates/, utility_meter/, command_line/)
- The **error type** (YAML syntax, unknown entity, deprecated platform, missing unique_id, etc.)
- The **exact block** to fix

If the file exists in `01_config_system_SH_PY_YAML/` (local), read it before fixing.

**Local path:** `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\`

### 2. Apply the project rules

**Modular files** (sensors, templates, utility_meter, command_line):
- ASCII main title border with rounded corners - 78 characters total
- Tertiary slug `# --- unique_id_exact ---` above each entity
- `name:` with initial capitals + pole prefix
- `unique_id:` lowercase + underscores

**Notify convention**: `notify.file` is forbidden -> replace with `notify.file_diag_log_file`

### 3. Reply format

```
[FILE_NAME] - [ERROR TYPE]

[corrected YAML block only]

# annotations_log:
# L.XX : [short description of the fix]
```

- Never return the whole file unless explicitly asked
- Annotate each modified line with `# "[L...] modif"`
- The `# annotations_log:` block is mandatory at the end of the reply
- The fix is done locally; going to prod goes through `/ha-push-yaml` (root `H:\` AND docs mirror).

### 4. Dependencies check (quick)

If the modified entity may impact a tile or `DEPENDANCES_GLOBALES_CLAUDE_memoire.md`, report:
`>> Impact potentiel : [tile L*C*] - /sync_index recommande`

**DEPENDANCES_GLOBALES path:** `docs\00_IA\`
