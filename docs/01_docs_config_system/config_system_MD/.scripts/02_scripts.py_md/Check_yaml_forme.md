# CHECK_YAML_FORME - Contrôle de forme des YAML de configuration

> **Script :** `check_yaml_forme.py` (Python 3)
> **Emplacement prod :** `/config/.scripts/check_yaml_forme.py`
> **Emplacement local :** `docs/01_docs_config_system/config_system_SH_PY_YAML/.scripts/02_scripts.py/check_yaml_forme.py` (copie identique dans `docs/04_docs_scripts/04_docs_scripts_yaml/Check_yaml_forme/Check_yaml_forme.py`)
> **Empreinte relevée le 2026-10-18 :** MD5 `842d0472`, 3335 octets, copies identiques à la prod
> **Dernière modification :** 2026-09-29 (date du fichier)

---

## Description

Contrôle la forme des `*.yaml` d'un dossier, d'après les règles YAML de `CLAUDE.md`. Récupéré le 2026-09-29 de l'étape 3 du `WORKFLOW_REBUILD.md` (supprimé), et remis en état : le dossier est devenu un argument.

## Utilisation

`python check_yaml_forme.py [dossier]`

- Sans argument : `docs/01_docs_config_system/config_system_SH_PY_YAML` (chemin relatif au dossier ReBuild, valeur `DEFAUT_LOCAL` du script).
- Sur la machine HA : passer `/config` en argument.
- Code de retour : 0 sans anomalie, 1 avec anomalies, 2 si le dossier est introuvable.

## Trois contrôles

1. `ENTETE_COLLE` : en-tête secondaire collé (`#|` ou `#+` au lieu de `# |` ou `# +`).
2. `BOITE_DECALEE` : boîte ASCII dont le haut, le titre et le bas n'ont pas la même largeur.
3. `REF_OBSOLETE` : référence à `P3_01_somme_par_piece` (renommée `P3_POWER_2_TOTAL_MULTI_ZONE`), hors journal d'annotations.

Sortie : une ligne `[TYPE] fichier:ligne détail` par anomalie, puis `RESULTAT : <dossier> - N anomalie(s)` ou `aucune anomalie`.

## Points d'attention

- Le chemin par défaut du script est périmé : le dossier local s'appelle `config_system_SH_PY_YAML` depuis le 2026-10-18. Sans argument, le script répond "dossier introuvable". Passer le dossier en argument. Le script n'est pas modifié.
- Aucun appelant (shell_command, automation) n'a été recherché pour cette fiche : inconnu.
- Ne lit que les fichiers `*.yaml`.