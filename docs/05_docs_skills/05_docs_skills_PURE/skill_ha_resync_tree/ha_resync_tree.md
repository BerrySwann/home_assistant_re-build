---
name: "ha-resync-tree"
description: "HA ReBuild skill - read-only comparison of local / prod / GitHub config (former GitHub -> local resync, removed on 2026-10-18: the local copy is the reference). Trigger on: resync depuis GitHub, pull depuis GitHub, met le local a jour depuis GitHub, quels fichiers ont change sur GitHub. NOT on \"resync tree\" (= update-arbo)."
---

# HA Resync Tree - read-only comparison (former Local <- GitHub)

> Files present in several locations (config, GLOBAL_INDEX_REPO, README): see `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 locations: local, prod root, prod docs mirror, GitHub root, GitHub docs/) and the read-only check `docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py` (decided by Eric on 2026-10-18).

> WARNING (2026-10-18): the LOCAL copy is the reference, prod must never be ahead of local, and GitHub is only a reflection of prod through the HA backup. Never copy GitHub to local without an explicit order from Eric, file by file. The folders `themes/`, `blueprints/` and `notifs/` stay in prod only.

## When Eric says "resync tree"

It means: update `IA_ARBO_DETAIL.md` (local, prod, GitHub counts) with the `update-arbo` skill (observed on 2026-10-18). Do NOT run this skill.

## What this skill does

The former workflow (download the GitHub zip and copy GitHub over `config_system_YAML`) is removed: it contradicted the rule "local is the reference", and the folder `config_system_YAML` no longer exists locally (replaced by `01_config_system_SH_PY_YAML` on 2026-10-18).

This skill now follows the procedure of step C of `/ha-trigul` (taken from the former `ha-resync-docs` skill, deleted on 2026-10-20 as a duplicate of trigul):

1. Compare in read-only mode, on the PC:
   `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py"`
   Report: `historique\03_RAPPORTS\06_MD5\03_VERIF_EMPLACEMENTS\verif_emplacements_[date].txt`.
2. Analyze: PROD DIFFERENTE DU LOCAL -> propose `/ha-push-yaml` (local is the reference); GITHUB EN ATTENTE DU BACKUP -> normal after a push; present in prod or on GitHub but not locally -> report it to Eric.
3. Copy to local: only on an explicit order from Eric, file by file, from prod `H:\` (not from GitHub), after a `.bak_AAAA_MM_JJ_HHhMMmSSs` backup of the local file if it exists, with a line in the modifications journal.
4. Automations and YAML scripts: unit-by-unit comparison by the deep step of `/ha-trigul`.

## RULES

1. Read-only by default.
2. Never overwrite a local file without reporting it.
3. `secrets.yaml` -> NEVER COPY, in any direction.
4. `.md` files are never synchronized by this skill (handled by /ha-push-docs).
5. After a copy validated by Eric, propose `/sync_index` if key entities changed.

## Maintenance note

This is the usable English copy of the skill (written in English to save tokens). Paths, file names, entity ids and report labels stay in French. The French explanation sheet is `docs/05_docs_skills/05_docs_skills_MD/skill_ha_resync_tree/ha_resync_tree.md`: when this file changes, re-read that sheet and update it. The installed skill `.claude/skills/ha-resync-tree/SKILL.md` must stay identical to this copy.
