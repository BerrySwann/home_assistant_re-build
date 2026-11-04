# MOC_SCRIPTS.md - 1 script = 1 fiche .md

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--04-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Scripts-4fc3f7?style=flat-square)](.)

</div>

Genere le 2026-11-04 20:01 par docs/04_docs_scripts/04_docs_scripts_SH/gen_moc_docs/gen_moc_docs.py (MOC_SCRIPTS). Ne pas modifier a la main : le script ecrase les modifications.

Regle d'Eric (2026-10-28) : chaque script de docs/04_docs_scripts a sa fiche .md. Rapprochement par le nom du fichier, sinon par une fiche qui cite le nom du fichier ; fiche proche mais non rattachee = candidate (a valider, jamais comptee OK). Classement (Eric, 2026-10-28) : deux groupes. Home Assistant : les .sh, puis les .py, puis les scripts YAML (les scripts de Home Assistant). Audit interne : les .sh, puis les .py ; ces scripts ne font pas tourner Home Assistant. Un script est range en verification ou audit quand son nom commence par Audit, Check, Verif, Hermes_audit ou trigul_run. La colonne Appele par Home Assistant dit si le nom du fichier apparait dans les YAML de la prod (H:), lecture seule. Voir GLOBAL_INDEX_SCRIPTS_SH.md et GLOBAL_INDEX_SCRIPTS_YAML.md. Les liens sont relatifs a ce fichier.

## SCRIPTS HOME ASSISTANT, ILS TOURNENT DANS HOME ASSISTANT

### .sh

<table style="table-layout:fixed;width:100%;overflow-wrap:anywhere">
<colgroup><col width="18%"><col width="26%"><col width="24%"><col width="32%"></colgroup>
<thead><tr><th>Dossier</th><th>Source</th><th>Fiche</th><th>Appele par Home Assistant</th></tr></thead>
<tbody>
<tr><td>Ha_git_backup</td><td><a href="04_docs_scripts_SH/Ha_git_backup/Ha_git_backup.sh">Ha_git_backup.sh</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Ha_git_backup/Ha_git_backup.md">fiche</a></td><td>oui (GitHub_backup_GitHub.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Mf_vigilance_images</td><td><a href="04_docs_scripts_SH/Mf_vigilance_images/Mf_vigilance_images.sh">Mf_vigilance_images.sh</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Mf_vigilance_images/Mf_vigilance_images.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
</tbody></table>

---

### .py

<table style="table-layout:fixed;width:100%;overflow-wrap:anywhere">
<colgroup><col width="18%"><col width="26%"><col width="24%"><col width="32%"></colgroup>
<thead><tr><th>Dossier</th><th>Source</th><th>Fiche</th><th>Appele par Home Assistant</th></tr></thead>
<tbody>
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
<tr><td>J_1_1_salon_clim_on_off_intelligent</td><td><a href="04_docs_scripts_YAML/Climatisation/J_1_1_salon_clim_on_off_intelligent/J_1_1_salon_clim_on_off_intelligent.yaml">J_1_1_salon_clim_on_off_intelligent.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Climatisation/J_1_1_salon_clim_on_off_intelligent/J_1_1_salon_clim_on_off_intelligent.md">fiche</a></td><td>oui (scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>J_1_2_bureau_clim_on_off_intelligent</td><td><a href="04_docs_scripts_YAML/Climatisation/J_1_2_bureau_clim_on_off_intelligent/J_1_2_bureau_clim_on_off_intelligent.yaml">J_1_2_bureau_clim_on_off_intelligent.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Climatisation/J_1_2_bureau_clim_on_off_intelligent/J_1_2_bureau_clim_on_off_intelligent.md">fiche</a></td><td>oui (scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>J_1_3_chambre_clim_on_off_intelligent</td><td><a href="04_docs_scripts_YAML/Climatisation/J_1_3_chambre_clim_on_off_intelligent/J_1_3_chambre_clim_on_off_intelligent.yaml">J_1_3_chambre_clim_on_off_intelligent.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Climatisation/J_1_3_chambre_clim_on_off_intelligent/J_1_3_chambre_clim_on_off_intelligent.md">fiche</a></td><td>oui (scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>J_2_0_secu_arret_clim_protege</td><td><a href="04_docs_scripts_YAML/Climatisation/J_2_0_secu_arret_clim_protege/J_2_0_secu_arret_clim_protege.yaml">J_2_0_secu_arret_clim_protege.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Climatisation/J_2_0_secu_arret_clim_protege/J_2_0_secu_arret_clim_protege.md">fiche</a></td><td>oui (scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>P1_Master_gestion_clim</td><td><a href="04_docs_scripts_YAML/Climatisation/P1_Master_gestion_clim/P1_Master_gestion_clim.yaml">P1_Master_gestion_clim.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/P1_Master_gestion_clim/P1_Master_gestion_clim.md">fiche</a></td><td>oui (automations.yaml, scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>SDB_soufflant_arreter</td><td><a href="04_docs_scripts_YAML/Soufflant_SDB/SDB_soufflant_arreter/SDB_soufflant_arreter.yaml">SDB_soufflant_arreter.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Soufflant_SDB/SDB_soufflant_arreter/SDB_soufflant_arreter.md">fiche</a></td><td>oui (automations.yaml, scripts.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>SDB_soufflant_demarrer</td><td><a href="04_docs_scripts_YAML/Soufflant_SDB/SDB_soufflant_demarrer/SDB_soufflant_demarrer.yaml">SDB_soufflant_demarrer.yaml</a></td><td>Fiche OK <a href="04_docs_scripts_YAML_MD/Soufflant_SDB/SDB_soufflant_demarrer/SDB_soufflant_demarrer.md">fiche</a></td><td>oui (P1_timer_60mn_soufflant_SDB.yaml, automations.yaml, scripts.yaml)</td></tr>
</tbody></table>

## SCRIPTS HOME ASSISTANT, ILS NE TOURNENT PAS DANS HOME ASSISTANT (audit, verification, generation, historique et sauvegarde : la maison fonctionnerait sans eux)

Outils de controle, pour Eric, Claude et Hermes. Certains sont lances depuis un bouton ou une automation de Home Assistant (voir la colonne Appele par Home Assistant), mais ils ne servent qu'a controler, generer ou sauvegarder : la maison fonctionnerait sans eux. Un script python que les YAML de la prod n'appellent pas est range ici. Classement par auteur : un script dont le nom contient hermes est a Hermes, les autres sont a Claude.

### SCRIPTS DE L'IA CLAUDE

#### .sh

<table style="table-layout:fixed;width:100%;overflow-wrap:anywhere">
<colgroup><col width="18%"><col width="26%"><col width="24%"><col width="32%"></colgroup>
<thead><tr><th>Dossier</th><th>Source</th><th>Fiche</th><th>Appele par Home Assistant</th></tr></thead>
<tbody>
<tr><td>Audit_md5</td><td><a href="04_docs_scripts_SH/Audit_md5/Audit_md5.sh">Audit_md5.sh</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Audit_md5/Audit_md5.md">fiche</a></td><td>oui (P4_log_eric_zone.yaml)</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Audit_md5_docs_local</td><td><a href="04_docs_scripts_SH/Audit_md5_docs_local/Audit_md5_docs_local.sh">Audit_md5_docs_local.sh</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Audit_md5_docs_local/Audit_md5_docs_local.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Audit_md5_yaml</td><td><a href="04_docs_scripts_SH/Audit_md5_yaml/Audit_md5_yaml.sh">Audit_md5_yaml.sh</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Audit_md5_yaml/Audit_md5_yaml.md">fiche</a></td><td>oui (GitHub_backup_GitHub.yaml)</td></tr>
</tbody></table>

#### .py

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
<tr><td>Check_prod_fonctionnelle</td><td><a href="04_docs_scripts_SH/Check_prod_fonctionnelle/Check_prod_fonctionnelle.py">Check_prod_fonctionnelle.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Check_prod_fonctionnelle/Check_prod_fonctionnelle.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Check_sous_context_ia</td><td><a href="04_docs_scripts_SH/Check_sous_context_ia/Check_sous_context_ia.py">Check_sous_context_ia.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Check_sous_context_ia/Check_sous_context_ia.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Check_XX_presents</td><td><a href="04_docs_scripts_SH/Check_XX_presents/Check_XX_presents.py">Check_XX_presents.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Check_XX_presents/Check_XX_presents.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Copie_reference</td><td><a href="04_docs_scripts_SH/Copie_reference/Copie_reference.py">Copie_reference.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Copie_reference/Copie_reference.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
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
<tr><td>Hermes_audit_md5_trigul_3md</td><td><a href="04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/trigul_run.py">trigul_run.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Trigul_run/Trigul_run.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>histo_html</td><td><a href="04_docs_scripts_SH/histo_html/histo_html.py">histo_html.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/histo_html/histo_html.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>histo_trace</td><td><a href="04_docs_scripts_SH/histo_trace/histo_trace.py">histo_trace.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/histo_trace/histo_trace.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Push_5C</td><td><a href="04_docs_scripts_SH/Push_5C/Push_5C.py">Push_5C.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Push_5C/Push_5C.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Recap_index</td><td><a href="04_docs_scripts_SH/Recap_index/Recap_index.py">Recap_index.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Recap_index/Recap_index.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Sync_98_sauvegarde</td><td><a href="04_docs_scripts_SH/Sync_98_sauvegarde/Sync_98_sauvegarde.py">Sync_98_sauvegarde.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Sync_98_sauvegarde/Sync_98_sauvegarde.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Verif_emplacements</td><td><a href="04_docs_scripts_SH/Verif_emplacements/Verif_emplacements.py">Verif_emplacements.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Verif_emplacements/Verif_emplacements.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Verif_headers_yaml</td><td><a href="04_docs_scripts_SH/Verif_headers_yaml/Verif_headers_yaml.py">Verif_headers_yaml.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Verif_headers_yaml/Verif_headers_yaml.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Verif_integrations_file</td><td><a href="04_docs_scripts_SH/Verif_integrations_file/Verif_integrations_file.py">Verif_integrations_file.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Verif_integrations_file/Verif_integrations_file.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
</tbody></table>

---

### SCRIPTS DE L'IA HERMES

#### .sh

<table style="table-layout:fixed;width:100%;overflow-wrap:anywhere">
<colgroup><col width="18%"><col width="26%"><col width="24%"><col width="32%"></colgroup>
<thead><tr><th>Dossier</th><th>Source</th><th>Fiche</th><th>Appele par Home Assistant</th></tr></thead>
<tbody>
<tr><td>Hermes_audit_md5_docs</td><td><a href="04_docs_scripts_SH/Hermes_audit_md5_docs/Hermes_audit_md5_docs.sh">Hermes_audit_md5_docs.sh</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Hermes_audit_md5_docs/Hermes_audit_md5_docs.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Hermes_audit_md5_trigul_3md</td><td><a href="04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_3md.sh">Hermes_audit_md5_trigul_3md.sh</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_3md.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
</tbody></table>

#### .py

<table style="table-layout:fixed;width:100%;overflow-wrap:anywhere">
<colgroup><col width="18%"><col width="26%"><col width="24%"><col width="32%"></colgroup>
<thead><tr><th>Dossier</th><th>Source</th><th>Fiche</th><th>Appele par Home Assistant</th></tr></thead>
<tbody>
<tr><td>audit_carte_docs_hermes</td><td><a href="04_docs_scripts_SH/audit_carte_docs_hermes/audit_carte_docs_hermes.py">audit_carte_docs_hermes.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/audit_carte_docs_hermes/audit_carte_docs_hermes.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>audit_huissier_hermes</td><td><a href="04_docs_scripts_SH/audit_huissier_hermes/audit_huissier_hermes.py">audit_huissier_hermes.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/audit_huissier_hermes/audit_huissier_hermes.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>boite_claude_watch_hermes</td><td><a href="04_docs_scripts_SH/boite_claude_watch_hermes/boite_claude_watch_hermes.py">boite_claude_watch_hermes.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/boite_claude_watch_hermes/boite_claude_watch_hermes.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>check_xx_repertoires_hermes</td><td><a href="04_docs_scripts_SH/check_xx_repertoires_hermes/check_xx_repertoires_hermes.py">check_xx_repertoires_hermes.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/check_xx_repertoires_hermes/check_xx_repertoires_hermes.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>edition_tracee_hermes</td><td><a href="04_docs_scripts_SH/edition_tracee_hermes/edition_tracee_hermes.py">edition_tracee_hermes.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/edition_tracee_hermes/edition_tracee_hermes.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>Hermes_audit_md5_trigul_3md</td><td><a href="04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_unitaire.py">Hermes_audit_md5_trigul_unitaire.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Hermes_audit_md5_trigul_unitaire/Hermes_audit_md5_trigul_unitaire.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td></td><td><a href="04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/hermes_audit_trigul_arbres.py">hermes_audit_trigul_arbres.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/Hermes_audit_trigul_arbres/Hermes_audit_trigul_arbres.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>hermes_gen_dependances</td><td><a href="04_docs_scripts_SH/hermes_gen_dependances/hermes_gen_dependances.py">hermes_gen_dependances.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/hermes_gen_dependances/hermes_gen_dependances.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>renomme_chemins_trace_hermes</td><td><a href="04_docs_scripts_SH/renomme_chemins_trace_hermes/renomme_chemins_trace_hermes.py">renomme_chemins_trace_hermes.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/renomme_chemins_trace_hermes/renomme_chemins_trace_hermes.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
<tr><td colspan="4">&nbsp;</td></tr>
<tr><td>verif_ecriture_hermes</td><td><a href="04_docs_scripts_SH/verif_ecriture_hermes/verif_ecriture_hermes.py">verif_ecriture_hermes.py</a></td><td>Fiche OK <a href="04_docs_scripts_SH_MD/verif_ecriture_hermes/verif_ecriture_hermes.md">fiche</a></td><td>non trouve dans les YAML de la prod</td></tr>
</tbody></table>

---

## Controle des fiches

- Scripts SH (bash et python) : 39 sources, 39 avec fiche, 0 sans fiche (dont 0 avec candidate a valider), 0 fiches sans source
- Scripts YAML (Home Assistant) : 9 sources, 9 avec fiche, 0 sans fiche (dont 0 avec candidate a valider), 1 fiches sans source
- Repartition : 2 scripts bash, 0 scripts python, 9 scripts YAML Home Assistant, 5 verification ou audit en bash, 32 verification ou audit en python

- Sans fiche .md mais documentes dans leur en-tete (3 sections ou plus) : 0 ()

## Fiches sans source correspondante (Scripts SH (bash et python))

- aucune

## Fiches sans source correspondante (Scripts YAML (Home Assistant))

- [Climatisation/Scripts_clim_on_off/Scripts_clim_on_off.md](04_docs_scripts_YAML_MD/Climatisation/Scripts_clim_on_off/Scripts_clim_on_off.md)
