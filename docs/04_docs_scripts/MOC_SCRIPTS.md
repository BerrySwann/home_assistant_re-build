# MOC_SCRIPTS.md - 1 script = 1 fiche .md

Genere le 2026-10-29 22:05 par docs/04_docs_scripts/04_docs_scripts_SH/gen_moc_docs/gen_moc_docs.py (MOC_SCRIPTS). Ne pas modifier a la main : le script ecrase les modifications.

Regle d'Eric (2026-10-28) : chaque script de docs/04_docs_scripts a sa fiche .md. Rapprochement par le nom du fichier, sinon par une fiche qui cite le nom du fichier ; fiche proche mais non rattachee = candidate (a valider, jamais comptee OK). Classement (Eric, 2026-10-28) : deux groupes. Home Assistant : les .sh, puis les .py, puis les scripts YAML (les scripts de Home Assistant). Audit interne : les .sh, puis les .py ; ces scripts ne font pas tourner Home Assistant. Un script est range en verification ou audit quand son nom commence par Audit, Check, Verif, Hermes_audit ou trigul_run. La colonne Appele par Home Assistant dit si le nom du fichier apparait dans les YAML de la prod (H:), lecture seule. Voir GLOBAL_INDEX_SCRIPTS_SH.md et GLOBAL_INDEX_SCRIPTS_YAML.md. Les liens sont relatifs a ce fichier.

## Controle

- Scripts SH (bash et python) : 26 sources, 26 avec fiche, 0 sans fiche (dont 0 avec candidate a valider), 0 fiches sans source
- Scripts YAML (Home Assistant) : 11 sources, 11 avec fiche, 0 sans fiche (dont 0 avec candidate a valider), 0 fiches sans source
- Repartition : 2 scripts bash, 9 scripts python, 9 scripts YAML Home Assistant, 5 verification ou audit en bash, 12 verification ou audit en python

- Sans fiche .md mais documentes dans leur en-tete (3 sections ou plus) : 0 ()

## Home Assistant

### .sh

<table style="table-layout:fixed;width:100%;overflow-wrap:anywhere">
<colgroup><col width="18%"><col width="26%"><col width="24%"><col width="32%"></colgroup>
<thead><tr><th>Dossier</th><th>Source</th><th>Fiche</th><th>Appele par Home Assistant</th></tr></thead>
<tbody>
<tr><td>Ha_git_backup</td><td><a href="04_docs_scripts_SH/Ha_git_backup/Ha_git_backup.sh">Ha_git_backup.sh</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Ha_git_backup/Ha_git_backup.md">fiche</a></td><td>oui (GitHub_backup_GitHub.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Mf_vigilance_images</td><td><a href="04_docs_scripts_SH/Mf_vigilance_images/Mf_vigilance_images.sh">Mf_vigilance_images.sh</a></td><td>Fiche OK <a href="../01_docs_config_system/01_config_system_MD/scripts/Mf_vigilance_images.md">fiche</a> (rattachement manuel)</td><td>non trouve dans les YAML de la prod</td></tr>
</tbody></table>

---

### .py

<table style="table-layout:fixed;width:100%;overflow-wrap:anywhere">
<colgroup><col width="18%"><col width="26%"><col width="24%"><col width="32%"></colgroup>
<thead><tr><th>Dossier</th><th>Source</th><th>Fiche</th><th>Appele par Home Assistant</th></tr></thead>
<tbody>
<tr><td>Correct_linky</td><td><a href="04_docs_scripts_YAML/Correct_linky/Correct_linky.py">Correct_linky.py</a></td><td>Fiche OK <a href="../01_docs_config_system/01_config_system_MD/.scripts/02_scripts.py_md/Correct_linky/Correct_linky.md">fiche</a> (rattachement manuel)</td><td>oui (P0_correct_linky.yaml, automations.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Gen_GLOBAL_INDEX_automations</td><td><a href="04_docs_scripts_SH/Gen_GLOBAL_INDEX_automations/Gen_GLOBAL_INDEX_automations.py">Gen_GLOBAL_INDEX_automations.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Gen_GLOBAL_INDEX_automations/Gen_GLOBAL_INDEX_automations.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Gen_GLOBAL_INDEX_ia</td><td><a href="04_docs_scripts_SH/Gen_GLOBAL_INDEX_ia/Gen_GLOBAL_INDEX_ia.py">Gen_GLOBAL_INDEX_ia.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Gen_GLOBAL_INDEX_ia/Gen_GLOBAL_INDEX_ia.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Gen_GLOBAL_INDEX_scripts</td><td><a href="04_docs_scripts_SH/Gen_GLOBAL_INDEX_scripts/Gen_GLOBAL_INDEX_scripts.py">Gen_GLOBAL_INDEX_scripts.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Gen_GLOBAL_INDEX_scripts/Gen_GLOBAL_INDEX_scripts.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Gen_GLOBAL_INDEX_vignettes_pages</td><td><a href="04_docs_scripts_SH/Gen_GLOBAL_INDEX_vignettes_pages/Gen_GLOBAL_INDEX_vignettes_pages.py">Gen_GLOBAL_INDEX_vignettes_pages.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Gen_GLOBAL_INDEX_vignettes_pages/Gen_GLOBAL_INDEX_vignettes_pages.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>gen_moc_dashboard</td><td><a href="04_docs_scripts_SH/gen_moc_dashboard/gen_moc_dashboard.py">gen_moc_dashboard.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/gen_moc_dashboard/gen_moc_dashboard.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>gen_moc_docs</td><td><a href="04_docs_scripts_SH/gen_moc_docs/gen_moc_docs.py">gen_moc_docs.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/gen_moc_docs/gen_moc_docs.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>histo_html</td><td><a href="04_docs_scripts_SH/histo_html/histo_html.py">histo_html.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/histo_html/histo_html.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>histo_trace</td><td><a href="04_docs_scripts_SH/histo_trace/histo_trace.py">histo_trace.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/histo_trace/histo_trace.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
</tbody></table>

---

### .yaml (scripts Home Assistant, ils tournent dans Home Assistant)

<table style="table-layout:fixed;width:100%;overflow-wrap:anywhere">
<colgroup><col width="18%"><col width="26%"><col width="24%"><col width="32%"></colgroup>
<thead><tr><th>Dossier</th><th>Source</th><th>Fiche</th><th>Appele par Home Assistant</th></tr></thead>
<tbody>
<tr><td>Audit_md5</td><td><a href="04_docs_scripts_YAML/Audit_md5/Audit_md5.yaml">Audit_md5.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Audit_md5/Audit_md5.md">fiche</a></td><td>oui (GitHub_backup_GitHub.yaml, P4_log_eric_zone.yaml, scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Audit_md5_md_yaml</td><td><a href="04_docs_scripts_YAML/Audit_md5_md_yaml/Audit_md5_md_yaml.yaml">Audit_md5_md_yaml.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Audit_md5_md_yaml/Audit_md5_md_yaml.md">fiche</a></td><td>oui (GitHub_backup_GitHub.yaml, scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>J_1_1_salon_clim_on_off_intelligent</td><td><a href="04_docs_scripts_YAML/Climatisation/J_1_1_salon_clim_on_off_intelligent/J_1_1_salon_clim_on_off_intelligent.yaml">J_1_1_salon_clim_on_off_intelligent.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Climatisation/Scripts_clim_on_off/Scripts_clim_on_off.md">fiche</a> (rattachement manuel)</td><td>oui (scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>J_1_2_bureau_clim_on_off_intelligent</td><td><a href="04_docs_scripts_YAML/Climatisation/J_1_2_bureau_clim_on_off_intelligent/J_1_2_bureau_clim_on_off_intelligent.yaml">J_1_2_bureau_clim_on_off_intelligent.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Climatisation/Scripts_clim_on_off/Scripts_clim_on_off.md">fiche</a> (rattachement manuel)</td><td>oui (scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>J_1_3_chambre_clim_on_off_intelligent</td><td><a href="04_docs_scripts_YAML/Climatisation/J_1_3_chambre_clim_on_off_intelligent/J_1_3_chambre_clim_on_off_intelligent.yaml">J_1_3_chambre_clim_on_off_intelligent.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Climatisation/Scripts_clim_on_off/Scripts_clim_on_off.md">fiche</a> (rattachement manuel)</td><td>oui (scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>J_2_0_secu_arret_clim_protege</td><td><a href="04_docs_scripts_YAML/Climatisation/J_2_0_secu_arret_clim_protege/J_2_0_secu_arret_clim_protege.yaml">J_2_0_secu_arret_clim_protege.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Climatisation/J_2_0_secu_arret_clim_protege/J_2_0_secu_arret_clim_protege.md">fiche</a></td><td>oui (scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>P1_Master_gestion_clim</td><td><a href="04_docs_scripts_YAML/Climatisation/P1_Master_gestion_clim/P1_Master_gestion_clim.yaml">P1_Master_gestion_clim.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/P1_Master_gestion_clim/P1_Master_gestion_clim.md">fiche</a></td><td>oui (automations.yaml, scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>SDB_soufflant_arreter</td><td><a href="04_docs_scripts_YAML/Soufflant_SDB/SDB_soufflant_arreter/SDB_soufflant_arreter.yaml">SDB_soufflant_arreter.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Soufflant_SDB/SDB_soufflant_arreter/SDB_soufflant_arreter.md">fiche</a></td><td>oui (automations.yaml, scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>SDB_soufflant_demarrer</td><td><a href="04_docs_scripts_YAML/Soufflant_SDB/SDB_soufflant_demarrer/SDB_soufflant_demarrer.yaml">SDB_soufflant_demarrer.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Soufflant_SDB/SDB_soufflant_demarrer/SDB_soufflant_demarrer.md">fiche</a></td><td>oui (P1_timer_60mn_soufflant_SDB.yaml, automations.yaml, scripts.yaml)</td></tr>
</tbody></table>

## Audit interne (ils ne font pas tourner Home Assistant)

Outils de controle, pour Eric, Claude et Hermes. Certains sont lances depuis un bouton ou une automation de Home Assistant (voir la colonne Appele par Home Assistant), mais ils ne servent qu'a controler : la maison fonctionnerait sans eux.

### .sh

<table style="table-layout:fixed;width:100%;overflow-wrap:anywhere">
<colgroup><col width="18%"><col width="26%"><col width="24%"><col width="32%"></colgroup>
<thead><tr><th>Dossier</th><th>Source</th><th>Fiche</th><th>Appele par Home Assistant</th></tr></thead>
<tbody>
<tr><td>Audit_md5</td><td><a href="04_docs_scripts_SH/Audit_md5/Audit_md5.sh">Audit_md5.sh</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Audit_md5/Audit_md5.md">fiche</a></td><td>oui (P4_log_eric_zone.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Audit_md5_md_yaml</td><td><a href="04_docs_scripts_SH/Audit_md5_md_yaml/Audit_md5_md_yaml.sh">Audit_md5_md_yaml.sh</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Audit_md5_md_yaml/Audit_md5_md_yaml.md">fiche</a></td><td>oui (GitHub_backup_GitHub.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Audit_md5_yaml</td><td><a href="04_docs_scripts_SH/Audit_md5_yaml/Audit_md5_yaml.sh">Audit_md5_yaml.sh</a></td><td>Fiche OK <a href="../01_docs_config_system/01_config_system_MD/.scripts/01_scripts.sh_md/Audit_md5_yaml/Audit_md5_yaml.md">fiche</a> (rattachement manuel)</td><td>oui (GitHub_backup_GitHub.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Hermes_audit_md5_docs</td><td><a href="04_docs_scripts_SH/Hermes_audit_md5_docs/Hermes_audit_md5_docs.sh">Hermes_audit_md5_docs.sh</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Hermes_audit_md5_docs/Hermes_audit_md5_docs.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Hermes_audit_md5_trigul_3md</td><td><a href="04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_3md.sh">Hermes_audit_md5_trigul_3md.sh</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_3md.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
</tbody></table>

---

### .py

<table style="table-layout:fixed;width:100%;overflow-wrap:anywhere">
<colgroup><col width="18%"><col width="26%"><col width="24%"><col width="32%"></colgroup>
<thead><tr><th>Dossier</th><th>Source</th><th>Fiche</th><th>Appele par Home Assistant</th></tr></thead>
<tbody>
<tr><td>Check_badges_fiches</td><td><a href="04_docs_scripts_SH/Check_badges_fiches/Check_badges_fiches.py">Check_badges_fiches.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Check_badges_fiches/Check_badges_fiches.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Check_DEPENDANCES</td><td><a href="04_docs_scripts_SH/Check_DEPENDANCES/Check_DEPENDANCES.py">Check_DEPENDANCES.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Check_DEPENDANCES/Check_DEPENDANCES.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Check_GLOBAL_INDEX</td><td><a href="04_docs_scripts_SH/Check_GLOBAL_INDEX/Check_GLOBAL_INDEX.py">Check_GLOBAL_INDEX.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Check_GLOBAL_INDEX/Check_GLOBAL_INDEX.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Check_sous_context_ia</td><td><a href="04_docs_scripts_SH/Check_sous_context_ia/Check_sous_context_ia.py">Check_sous_context_ia.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Check_sous_context_ia/Check_sous_context_ia.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Check_XX_presents</td><td><a href="04_docs_scripts_SH/Check_XX_presents/Check_XX_presents.py">Check_XX_presents.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Check_XX_presents/Check_XX_presents.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Check_yaml_forme</td><td><a href="04_docs_scripts_YAML/Check_yaml_forme/Check_yaml_forme.py">Check_yaml_forme.py</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Check_yaml_forme/Check_yaml_forme.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Hermes_audit_md5_trigul_3md</td><td><a href="04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_unitaire.py">Hermes_audit_md5_trigul_unitaire.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Hermes_audit_md5_trigul_unitaire/Hermes_audit_md5_trigul_unitaire.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td></td><td><a href="04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/hermes_audit_trigul_arbres.py">hermes_audit_trigul_arbres.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Hermes_audit_trigul_arbres/Hermes_audit_trigul_arbres.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td></td><td><a href="04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/trigul_run.py">trigul_run.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Trigul_run/Trigul_run.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Verif_emplacements</td><td><a href="04_docs_scripts_SH/Verif_emplacements/Verif_emplacements.py">Verif_emplacements.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Verif_emplacements/Verif_emplacements.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Verif_headers_yaml</td><td><a href="04_docs_scripts_SH/Verif_headers_yaml/Verif_headers_yaml.py">Verif_headers_yaml.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Verif_headers_yaml/Verif_headers_yaml.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Verif_integrations_file</td><td><a href="04_docs_scripts_SH/Verif_integrations_file/Verif_integrations_file.py">Verif_integrations_file.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Verif_integrations_file/Verif_integrations_file.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
</tbody></table>

## Fiches sans source correspondante (Scripts SH (bash et python))

- aucune

## Fiches sans source correspondante (Scripts YAML (Home Assistant))

- aucune
