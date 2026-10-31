---
name: "ha-update-check-cli"
description: "HA ReBuild skill - analyses the pending HA updates WITHOUT MCP tools (Claude Code command line): versions through .HA_VERSION and the GitHub API, release notes, grep cross-check against the real config, ReBuild traps, post-update checklist. Installs nothing. Trigger on /ha-update-cli, mise a jour HA en CLI, maj HA sans MCP."
---

# ha-update-check-cli - Pre-update HA analysis (without MCP)

> Files present in several locations (config, GLOBAL_INDEX_REPO, README): see `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 locations: local, prod root, prod docs mirror, GitHub root, GitHub docs/) and the read-only check `docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py` (decided by Eric on 2026-10-18).

Goal: read the changes of the pending HA updates, cross them with Eric's real config (grep), and output a short top list: what he must do before, what will break, what to do after. This version INSTALLS NOTHING: installation, backup and restart are done from the HA UI, by Eric.

If the HA MCP tools (ha_manage_updates, ha_get_overview, ha_manage_backup...) are available in the session, use the account skill ha-update-check instead (analysis, backup, installation, restart, cache).

## Rules

- Answer in French, concise, direct. No table, no emoji, no systematic bold.
- Typography: only plain hyphen, three dots, straight quotes, straight apostrophe. No Alt character. Arrow = ->, bullet = -.
- Every precise fact (version, option name, date) is qualified: established (read in a file, an API or a page, say which one), deduced (say from what), or unknown (say you do not know, never an approximate value).
- Release notes summarized by WebFetch are NOT the full text: say so.
- Never guess a compatibility (minimum HA version, etc.): unknown.
- A "not verified" point is never presented as "no impact".
- Never display a token, a password or an API key (see ReBuild traps).

## Step 1 - Versions (without MCP)

- Installed core: read H:\.HA_VERSION (deduced: H:\ is the config folder of prod, see ha-push-yaml; to confirm at first use). If unreadable: unknown, ask Eric.
- Available core: GitHub API, https://api.github.com/repos/home-assistant/core/releases/latest (WebFetch or curl depending on what is available). If the API is unreachable (rate limit, network): unknown, do not guess.
- Custom cards and integrations (HACS): their versions cannot be read reliably without MCP. Ask Eric for the list of pending updates (HACS -> updates, or a screenshot) and note for each one: name, installed version -> target version, release link.
- If several versions are skipped: read the notes of ALL the intermediate versions.

## Step 2 - Read the changes

For each update:
1. GitHub release notes (link given by Eric, or the releases API of the repository). For the core: https://www.home-assistant.io/blog/categories/release-notes/.
2. WebFetch with the explicit request: breaking changes, renamed or deprecated or removed options, removed entities/services, minimum HA version, migrations, "restart HA" or "clear the cache" banners.
3. Classify each point: breaking change, removal, deprecation, renamed option, new feature, fix.

## Step 3 - Cross with the real config (grep)

Declare as impacted only what is verified. Otherwise: "non verifie".

Scope (read-only):
- Local: C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\ and docs\03_docs_automations\03_docs_automations_YAML\
- Prod: H:\ (config YAML; themes/, blueprints/ and notifs/ exist only in prod)

For each option, entity, service or card (custom:xxx) quoted by the notes: grep -rIn on the scope, note file and line. Zero result = "non utilise (verifie dans <scope>)". Dashboards stored outside YAML and nested content are not covered by this grep: say so.

## Step 4 - ReBuild traps to check systematically

Labels taken from Eric's list of 2026-10-13. The detail (exact symptom and verification) was not provided: TO BE COMPLETED by Eric in this file ("A COMPLETER par Eric", still open on 2026-10-31). Meanwhile, check only what grep allows and say the rest as "non verifie".

- token API 403
- dashboard 1.7 Mo
- 5 sensors uptime avec parseFloat (grep -rIn "parseFloat")
- cartes custom a surveiller: mushroom v5, button-card, etc. (grep -rIn "custom:mushroom" and "custom:button-card")
- condition state + for + attribute
- mqtt.publish admin-only (grep -rIn "mqtt.publish")
- CARTO / API key (never display the key)

## Step 5 - Decision and report

Verdict per update: INSTALLER / BLOQUER.
BLOQUER if a breaking change or a removal touches an element verified in step 3 or a trap of step 4, if a manual migration is required, or if the notes cannot be found. A deprecation without removal does not block: list it.

Output format, short (labels stay in French):

Verdict: (one line per update, with the reason)

TOP (by severity, max 5 lines): quoi -> consequence pour Eric -> action.

A FAIRE AVANT: backup from the HA UI, manipulations quoted in the notes.

CE QUI VA CASSER / A REFAIRE: impacted elements (verified). Otherwise: "rien de verifie".

A FAIRE APRES: restart HA if requested, clear the frontend cache (Ctrl+F5 on PC, Companion app cache on mobile), checks of step 6.

NON VERIFIE / INCONNU: everything the notes, grep or APIs did not allow to establish.

## Step 6 - Post-update checklist

Eric's detailed 14-point checklist was not provided: TO BE PASTED HERE ("A COLLER ICI", still open on 2026-10-31). Meanwhile, minimal checks (to be done by Eric in the UI):
- Developer tools -> YAML -> check configuration: valid.
- Settings -> System -> Repairs: compare with the state before.
- Settings -> System -> Logs: new errors related to the updated components.
- Dashboards concerned: the cards are displayed.
- Frontend cache cleared.

## Step 7 - Installation

Never by this skill. Eric installs from the HA UI after a backup (Settings -> System -> Backups). Recommended order: HACS cards -> HACS integrations -> apps -> core -> OS. Core and OS one at a time.

## End of session

If project files were modified: apply journal-modifs. Propose /histo.

## Maintenance note

This is the usable English copy of the skill (written in English to save tokens). Paths, file names, entity ids and report labels stay in French. The French explanation sheet is `docs/05_docs_skills/05_docs_skills_MD/skill_ha_update_check_cli/ha_update_check_cli.md`: when this file changes, re-read that sheet and update it. The installed skill `.claude/skills/ha-update-check-cli/SKILL.md` must stay identical to this copy.
