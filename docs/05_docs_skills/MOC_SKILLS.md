# MOC_SKILLS.md - skills du projet et leur explication

Genere le 2026-10-28 19:13 par docs/04_docs_scripts/04_docs_scripts_SH/gen_moc_docs/gen_moc_docs.py (MOC_SKILLS). Ne pas modifier a la main : le script ecrase les modifications.

Regle d'Eric (2026-10-28) : la liste des skills avec leur explication (champ description du SKILL.md, repris de la copie en docs/05_docs_skills). Une copie par skill : dossier skill_<nom>/<nom>.md. Les liens sont relatifs a ce fichier.

## Controle

- Skills avec copie en docs : 15
- Skills du projet (.claude/skills) : 15
- Skills du projet sans copie en docs : aucun
- Dossiers skill_ sans copie (seulement des .bak) : skill_hermes_aligne, skill_hermes_journal_modifs

## Skills

| Skill | Copie | Explication | Copie datee du |
|:------|:------|:------------|:---------------|
| fix-file | [fix_file.md](skill_fix_file/fix_file.md) | Skill HA ReBuild - analyse une erreur Home Assistant et retourne UNIQUEMENT le bloc YAML corrige. | 2026-10-25 |
| ha-new-yaml | [ha_new_yaml.md](skill_ha_new_yaml/ha_new_yaml.md) | Skill HA ReBuild - genere un squelette YAML conforme aux conventions du projet (bordures ASCII, headers obligatoires, slug tertiaire, name/unique_id). | 2026-10-25 |
| ha-push-docs | [ha_push_docs.md](skill_ha_push_docs/ha_push_docs.md) | Skill HA ReBuild - synchronise les fichiers de documentation locaux (*.md + *.yaml dashboard) vers la prod H:\\Docs (Samba HA). | 2026-10-25 |
| ha-push-md | [ha_push_md.md](skill_ha_push_md/ha_push_md.md) | Skill HA ReBuild - pousse uniquement les fichiers *.md de documentation locaux vers H:\Docs (Samba HA). | 2026-10-25 |
| ha-push-yaml | [ha_push_yaml.md](skill_ha_push_yaml/ha_push_yaml.md) | Skill HA ReBuild - pousse des YAML config locaux vers la prod HA (racine H:\\ ET miroir docs), sauvegarde locale .bak avant modification, MD5-first. | 2026-10-25 |
| ha-resync-tree | [ha_resync_tree.md](skill_ha_resync_tree/ha_resync_tree.md) | Skill HA ReBuild - comparaison config locale / prod / GitHub en lecture seule (ancien resync GitHub -> local, retire le 2026-10-18 : le local fait foi). | 2026-10-25 |
| ha-status | [ha_status.md](skill_ha_status/ha_status.md) | Skill HA ReBuild - genere un resume ultra-compact de l'avancement du projet en 3 points. | 2026-10-25 |
| ha-trigul | [ha_trigul.md](skill_ha_trigul/ha_trigul.md) | Skill HA ReBuild - triangulation des docs entre local (ReBuild), prod (H:) et GitHub : superposition des 3 arbres (en trop, manquant, casse, contenu, format de l'audit MD5 docs), etape profonde automations/scripts et controle des fichiers a 5 emplacements. | 2026-10-25 |
| ha-update-check-cli | [ha_update_check_cli.md](skill_ha_update_check_cli/ha_update_check_cli.md) | Skill HA ReBuild - analyse les mises a jour HA en attente SANS outils MCP (Claude Code en ligne de commande) : versions via .HA_VERSION et API GitHub, notes de version, croisement grep contre la config reelle, pieges ReBuild, checklist post-MAJ. N'installe rien. | 2026-10-25 |
| ha-verif-headers | [ha_verif_headers.md](skill_ha_verif_headers/ha_verif_headers.md) | Skill HA ReBuild - verifie en lecture seule les en-tetes des YAML de config (boites ASCII a largeur variable, 5 headers, slug tertiaire, name et unique_id) selon les normes du CLAUDE.md. | 2026-10-25 |
| histo | [histo.md](skill_histo/histo.md) | Skill HA ReBuild - genere un journal de bord ultra-compact et le sauvegarde, puis enchaine automatiquement le sync_index (DEPENDANCES_GLOBALES.md, docs impactees, GLOBAL_INDEX_REPO.md), le journal fusionne et la copie Obsidian et le menage des sauvegardes .bak puis la mise a jour du tree (IA_ARBO_DETAIL.md). | 2026-10-25 |
| histo-final | [histo_final.md](skill_histo_final/histo_final.md) | Skill HA ReBuild - histo de fin de journee : lance le skill histo complet, puis, apres le rapport et sans confirmation, eteint les lumieres (3 Hue Play du bureau, apres avoir arrete Hue Sync) et arrete le PC. | 2026-10-25 |
| journal-modifs | [journal_modifs.md](skill_journal_modifs/journal_modifs.md) | Skill HA ReBuild - note au fil de l'eau chaque modification de fichier (creation, modification, renommage, suppression, push) dans un journal par auteur, lisible par Claude et Hermes. A appliquer apres chaque ecriture et a lire au debut de session. | 2026-10-21 |
| sync-index | [sync_index.md](skill_sync_index/sync_index.md) | Skill HA ReBuild - met a jour DEPENDANCES_GLOBALES.md et l'index du projet apres validation d'un fichier YAML. | 2026-10-25 |
| update-arbo | [update_arbo.md](skill_update_arbo/update_arbo.md) | Skill HA ReBuild - met a jour IA_ARBO_DETAIL.md (comptages LOCAL + PROD + GitHub) apres toute session qui ajoute, supprime ou deplace des fichiers. | 2026-10-25 |
