---
name: "ha-new-yaml"
description: "HA ReBuild skill - generates a YAML skeleton that follows the project conventions (ASCII borders, mandatory headers, tertiary slug, name/unique_id). Trigger on: \"cree un nouveau fichier YAML\", \"nouveau sensor/template/utility_meter\", \"squelette YAML\", \"nouveau fichier P0/P1/P2/P3\", \"cree le fichier [nom]\"."
---

# HA New YAML - compliant skeleton generation

> Files present in several locations (config, GLOBAL_INDEX_REPO, README): see `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 locations: local, prod root, prod docs mirror, GitHub root, GitHub docs/) and the read-only check `docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py` (decided by Eric on 2026-10-18).

Generates an empty YAML file that fully follows the HA ReBuild project conventions:
ASCII borders, mandatory headers, tertiary slug, consistent name/unique_id.

> Scope: sensors/, templates/, utility_meter/, command_line/. Never automations.

---

## QUESTIONS TO ASK BEFORE GENERATING

1. **Pole**: P0 Energie / P1 Chauffage / P2 Prises / P3 Eclairage / P4 Presence / M Meteo / A Air / S Stores / MP Mini-PC?
2. **File type**: sensor / template / utility_meter / command_line?
3. **Room** (if applicable): Entree / Cellier / Toilette / Salon / Cuisine / Couloir / Bureau / SDB / Chambre?
4. **Functional name**: what does this file do, in one sentence?
5. **Source entity(ies)**: which raw sensor or HA entity feeds this file?
6. **Downstream**: which file or tile consumes the entities produced?

---

## COMPLIANCE RULES

### Main title border - rounded corners, 78 characters
Use the real Unicode characters: rounded corners (U+256D/256E/256F/2570), bars (U+2500/2502).
- If the title is longer than 74 chars -> widen the box, do not truncate.
- Always in UPPERCASE.

### Secondary title border - square corners, 37 characters
Use the real Unicode characters: square corners (U+250C/2510/2514/2518), bars (U+2500/2502).
- One per logical group of entities. Numbered 1 to 9.

### Mandatory header lines (right under the main box; the labels stay in French)
```yaml
# ## DESCRIPTION :
# ## CALCUL & SOURCES :
# ## CHAINE DE DEPENDANCES :
#   | MATERIEL | CAPTEUR BRUT (source) | CE FICHIER (unique_id) | AVAL |
# ## IMPORTANT (PIEGES) :
# ## TABLEAU DE BORD (VIGNETTES PRINCIPALES) :
```

### Tertiary slug
```yaml
# --- unique_id_exact_de_l_entite ---
```

### name / unique_id
- `name`: initial capitals + pole prefix. Ex: `"Radiateur Cuisine Energie Quotidien"`
- `unique_id`: lowercase + underscores. Ex: `radiateur_cuisine_energie_quotidien`
- Cross-consistency is mandatory.

---

## LOCATION OF THE GENERATED FILE

| Type | Windows path |
|:-----|:-------------|
| sensor | `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\sensors\P{N}_{domaine}\` |
| template | `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\templates\P{N}_{domaine}\` |
| utility_meter | `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\utility_meter\P{N}_{domaine}\` |
| command_line | `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML\command_line\` |

Naming: `P{N}_TYPE_NOM_AMHQ.yaml` if multi-cycle, otherwise `P{N}_TYPE_NOM.yaml` (also follow the naming document `IA_NOM_DES_REPERTOIRES_ET_FICHIERS.md`).

After generation, run `/ha-verif-headers` on the file (read-only check of the ASCII boxes, the 5 headers, the slug, the name and the unique_id), then propose `/sync_index`. Going to prod is done with `/ha-push-yaml`, which pushes to the root `H:\` AND to the mirror `H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\`.

## Maintenance note

This is the usable English copy of the skill (written in English to save tokens). Paths, file names, entity ids and report labels stay in French. The French explanation sheet is `docs/05_docs_skills/05_docs_skills_MD/skill_ha_new_yaml/ha_new_yaml.md`: when this file changes, re-read that sheet and update it. The installed skill `.claude/skills/ha-new-yaml/SKILL.md` must stay identical to this copy.
