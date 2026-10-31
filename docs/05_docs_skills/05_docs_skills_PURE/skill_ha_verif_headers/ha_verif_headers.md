---
name: "ha-verif-headers"
description: "HA ReBuild skill - read-only check of the headers of the config YAML files (ASCII boxes of variable width, 5 headers, tertiary slug, name and unique_id) according to the CLAUDE.md standards. Trigger on: /ha-verif-headers, verifie les headers, verifie les ascii slug name unique_id, controle de forme des YAML, le fichier est-il conforme, after creating or modifying a config YAML."
---

# HA Verif Headers - check of the config YAML headers

> Files present in several locations (config, GLOBAL_INDEX_REPO, README): see `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` and the check `Verif_emplacements.py` (decided by Eric on 2026-10-18).

Created on 2026-10-20 at Eric's request. Checks that a YAML file in `docs\01_docs_config_system\01_config_system_SH_PY_YAML\` follows the standards of `Claude md SAVE\CLAUDE.md`: sections 4 (ASCII borders), 5 (5 mandatory headers), 7 (tertiary slug), 8 (name and unique_id). READ-ONLY: the skill corrects nothing without an order from Eric.

Complements `ha-new-yaml` (which generates a compliant skeleton) and `check_yaml_forme.py` (box alignment only).

## WORKFLOW

### 1 - Run the check (on the PC)

```powershell
$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Verif_headers_yaml\Verif_headers_yaml.py" [file or folder] [--erreurs] [--prefixe]
```

- Without argument: all YAML files of `01_config_system_SH_PY_YAML` (about 90 files).
- With a path: one file or one sub-folder. After creating or modifying a YAML, run it on that file.
- `--erreurs`: ERREUR only. `--prefixe`: also checks the pole prefix in `name` (rarely followed today, so disabled by default).
- Last line: `controle verif_headers: fichiers=N erreurs=N avis=N`. Exit code 0 without ERREUR, 1 with ERREUR.

### 2 - Read the result

ERREUR (structure, must be fixed): `BOITE_DECALEE` (top, title and bottom of different widths), `BOITE_TROP_ETROITE`, `ENTETE_COLLE`, `BOITE_PRINCIPALE_ABSENTE`, `HEADER_ABSENT`, `HEADER_ORDRE`, `SLUG_ABSENT`, `SLUG_DIFFERENT`, `ID_DOUBLON`, `ID_FORMAT`.

AVIS (convention, to judge with Eric): `BOITE_COINS`, `BOITE_LARGEUR`, `BOITE_MINUSCULES`, `NUMEROTATION`, `SLUG_ORPHELIN`, `NOM_ID_DIFFERENT`, `NOM_INITIALE`, `TABLEAU_DEPENDANCES_ABSENT`, `PREFIXE_POLE`.

Box width rules (reminder from Eric, 2026-10-20): 78 (main, rounded corners) and 37 (secondary, square corners) are the standard frame, not a limit. A box is longer when its title is longer: minimum width = text length + 5 (preferably + 6, one space before the bar). The top, the title and the bottom always keep the same width, indentation excluded. Never truncate a title to fit in 78.

An AVIS is not necessarily a fault: `NOM_ID_DIFFERENT` comes from a heuristic (normalized name compared with unique_id), `NOM_INITIALE` triggers on acronyms like tCOV. Say so, do not fix in bulk.

### 3 - Report

- Give the `controle verif_headers` line, then the ERREUR per file (file:line, type, detail), then the number of AVIS per type.
- An old deviation (already present before the session) is reported, not fixed without a request.
- Propose the fix file by file: local backup `.bak_AAAA_MM_JJ_HHhMMmSSs` before modification, modification in local, re-run the check on the file, line in the modifications journal, then `/ha-push-yaml` on Eric's order.

## RULES

1. Read-only by default: no file modified without an order from Eric.
2. Standards = `Claude md SAVE\CLAUDE.md`; if in doubt about a standard, read CLAUDE.md, do not guess.
3. Backups (`.bak_`), dated names and the folders `.scripts`, `scripts`, `notifs`, `themes`, `blueprints`, `ARCHIVE` are ignored by the script.
4. Does not touch automations or dashboards (outside the `01_config_system_SH_PY_YAML` scope).
5. Script sheet: `docs\04_docs_scripts\04_docs_scripts_SH_MD\Verif_headers_yaml\Verif_headers_yaml.md`.

## Maintenance note

This is the usable English copy of the skill (written in English to save tokens). Paths, file names, entity ids, check codes and report labels stay in French. The French explanation sheet is `docs/05_docs_skills/05_docs_skills_MD/skill_ha_verif_headers/ha_verif_headers.md`: when this file changes, re-read that sheet and update it. The installed skill `.claude/skills/ha-verif-headers/SKILL.md` must stay identical to this copy.
