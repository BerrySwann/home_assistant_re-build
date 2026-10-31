# MOC_SKILLS.md - skills du projet et leur explication

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--31-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Skill-ffeb3b?style=flat-square)](.)

</div>

Genere le 2026-10-31 15:52 par docs/04_docs_scripts/04_docs_scripts_SH/gen_moc_docs/gen_moc_docs.py (MOC_SKILLS). Ne pas modifier a la main : le script ecrase les modifications.

Regle d'Eric (2026-10-28) : la liste des skills avec leur explication (champ description du SKILL.md, repris de la copie en docs/05_docs_skills). Une copie par skill : dossier `skill_NOM/NOM.md` (anglais, dans 05_docs_skills_PURE) et fiche francaise dans 05_docs_skills_MD. Les liens sont relatifs a ce fichier.

## Controle

- Skills avec copie en docs : 15
- Skills du projet (.claude/skills) : 15
- Skills du projet sans copie en docs : aucun
- Dossiers skill_ sans copie (seulement des .bak) : skill_hermes_aligne, skill_hermes_journal_modifs

## Skills

| Skill | Anglais | FR | Explication | Date |
|:------|:------|:------|:------------|:---------------|
| fix-file | [fix_file.md](05_docs_skills_PURE/skill_fix_file/fix_file.md) | [fix_file.md](05_docs_skills_MD/skill_fix_file/fix_file.md) | Tu colles une erreur Home Assistant (log, trace, message de l'interface) ou un bloc YAML qui plante. Le ski... | 2026-10-31 |
| ha-new-yaml | [ha_new_yaml.md](05_docs_skills_PURE/skill_ha_new_yaml/ha_new_yaml.md) | [ha_new_yaml.md](05_docs_skills_MD/skill_ha_new_yaml/ha_new_yaml.md) | Le skill cree un fichier YAML vide mais entierement conforme aux conventions du projet : boites ASCII, 5 he... | 2026-10-31 |
| ha-push-docs | [ha_push_docs.md](05_docs_skills_PURE/skill_ha_push_docs/ha_push_docs.md) | [ha_push_docs.md](05_docs_skills_MD/skill_ha_push_docs/ha_push_docs.md) | Le skill synchronise la documentation locale (`*.md` et `*.yaml` de dashboard) vers `H:\docs`, en ne poussa... | 2026-10-31 |
| ha-push-md | [ha_push_md.md](05_docs_skills_PURE/skill_ha_push_md/ha_push_md.md) | [ha_push_md.md](05_docs_skills_MD/skill_ha_push_md/ha_push_md.md) | Version restreinte de `ha-push-docs` : elle ne pousse que les fichiers `*.md` de documentation (dashboard,... | 2026-10-31 |
| ha-push-yaml | [ha_push_yaml.md](05_docs_skills_PURE/skill_ha_push_yaml/ha_push_yaml.md) | [ha_push_yaml.md](05_docs_skills_MD/skill_ha_push_yaml/ha_push_yaml.md) | Operation critique : le skill pousse des YAML de `01_config_system_SH_PY_YAML` vers la prod, aux deux empla... | 2026-10-31 |
| ha-resync-tree | [ha_resync_tree.md](05_docs_skills_PURE/skill_ha_resync_tree/ha_resync_tree.md) | [ha_resync_tree.md](05_docs_skills_MD/skill_ha_resync_tree/ha_resync_tree.md) | Ancien "resync GitHub vers local", retire le 2026-10-18 parce que le local fait foi. Le skill ne fait plus... | 2026-10-31 |
| ha-status | [ha_status.md](05_docs_skills_PURE/skill_ha_status/ha_status.md) | [ha_status.md](05_docs_skills_MD/skill_ha_status/ha_status.md) | Resume ultra-compact de l'etat du projet : ce qui est fait, ce qui est en cours, ce qui suit, plus les bloc... | 2026-10-31 |
| ha-trigul | [ha_trigul.md](05_docs_skills_PURE/skill_ha_trigul/ha_trigul.md) | [ha_trigul.md](05_docs_skills_MD/skill_ha_trigul/ha_trigul.md) | Trois controles enchaines, en lecture seule, qui comparent la documentation entre le local (ReBuild, qui fa... | 2026-10-31 |
| ha-update-check-cli | [ha_update_check_cli.md](05_docs_skills_PURE/skill_ha_update_check_cli/ha_update_check_cli.md) | [ha_update_check_cli.md](05_docs_skills_MD/skill_ha_update_check_cli/ha_update_check_cli.md) | Analyse les mises a jour HA en attente quand les outils MCP ne sont pas disponibles (Claude Code en ligne d... | 2026-10-31 |
| ha-verif-headers | [ha_verif_headers.md](05_docs_skills_PURE/skill_ha_verif_headers/ha_verif_headers.md) | [ha_verif_headers.md](05_docs_skills_MD/skill_ha_verif_headers/ha_verif_headers.md) | Verifie en lecture seule qu'un YAML de `01_config_system_SH_PY_YAML` respecte les normes du CLAUDE.md : boi... | 2026-10-31 |
| histo | [histo.md](05_docs_skills_PURE/skill_histo/histo.md) | [histo.md](05_docs_skills_MD/skill_histo/histo.md) | Ce skill fait le point sur une session de travail et remet tout en ordre : il ecrit le journal de bord, met... | 2026-10-31 |
| histo-final | [histo_final.md](05_docs_skills_PURE/skill_histo_final/histo_final.md) | [histo_final.md](05_docs_skills_MD/skill_histo_final/histo_final.md) | Fin de journee : le skill lance tout `/histo`, verifie que tout est ecrit et pousse, envoie une notificatio... | 2026-10-31 |
| journal-modifs | [journal_modifs.md](05_docs_skills_PURE/skill_journal_modifs/journal_modifs.md) | [journal_modifs.md](05_docs_skills_MD/skill_journal_modifs/journal_modifs.md) | Chaque agent (Claude, Hermes) note une ligne par fichier modifie, au moment de la modification, dans son pr... | 2026-10-31 |
| sync-index | [sync_index.md](05_docs_skills_PURE/skill_sync_index/sync_index.md) | [sync_index.md](05_docs_skills_MD/skill_sync_index/sync_index.md) | Apres validation d'un fichier YAML (config, automation ou script), le skill met a jour la documentation de... | 2026-10-31 |
| update-arbo | [update_arbo.md](05_docs_skills_PURE/skill_update_arbo/update_arbo.md) | [update_arbo.md](05_docs_skills_MD/skill_update_arbo/update_arbo.md) | Apres une session qui ajoute, supprime ou deplace des fichiers, le skill rafraichit les comptages et les in... | 2026-10-31 |
