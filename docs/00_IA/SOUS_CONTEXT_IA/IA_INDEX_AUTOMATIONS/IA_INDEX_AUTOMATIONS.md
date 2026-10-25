# IA_INDEX_AUTOMATIONS.md - Contexte & Competence INDEX AUTOMATIONS

*Mis a jour le : 2026-10-13 (comptages, arborescence et procedure remis a jour ; version precedente du 2026-07-21)*

---

## Ce que c'est

Les automations sont indexees a deux endroits :
- **Index detaille genere** : `docs/03_Docs_automations/GLOBAL_INDEX_AUTOMATIONS.md` (une ligne par automation : alias, id prod, id local, entity HA, fiche .md, YAML source, commentaire). Regenere a chaque `/histo` par `docs/04_Docs_scripts/Docs_scripts_sh/Gen_GLOBAL_INDEX_automations/Gen_GLOBAL_INDEX_automations.py`. Ne jamais le modifier a la main.
- **Resume** : section `03-AUTOMATIONS` de `GLOBAL_INDEX_REPO.md` (racine de `H:\` + copie locale `docs/01_docs_config_system/config_system_MD/GLOBAL_INDEX_REPO/GLOBAL_INDEX_REPO.md`). Maintenue a la main, non regeneree.

Il n'y a plus de fichier `INDEX_AUTOMATIONS.md` distinct - fusionne dans GLOBAL_INDEX_REPO.md (2026-07-16).

---

## Arborescence locale des automations

```
docs/03_Docs_automations/
- GLOBAL_INDEX_AUTOMATIONS.md  <- index genere (ne pas modifier)
- Docs_automations_yaml/       <- YAML individuels par automation (reference locale), un dossier par categorie HA :
    _SANS_CATEGORIE/  Backup HA - GitHub/  Bouton Virtuel/  Contrôle Entity z2m/
    Gestion des Stores/  MariaDB & VSCode Optimisation/  Météo/  P0_ENRIGE/
    P1_01_CLIM_CHAUFFAGE/  P1_02_Cuisine/  P1_03_Chauffage Salle de Bain/
    P2_Alarme_Congélateur/  P2_éCO. Prises/  P3_Eclairage/  RASPI/  Tarif HC-HP/
    Watchdog Piles (HUE-IKEA-SONOFF)/  AUTOMATIONS.YALM ORIGINAL/ (export d'origine, ignore par l'index)
- Docs_automations_md/         <- Fiches texte par automation
```

> ⚠️ Ne jamais modifier `automations.yaml` directement.
> Tout changement passe par l'UI HA, en s'appuyant sur les fichiers `Docs_automations_yaml/`.

---

## Comptage (verifie 2026-10-13)

**62 automations** dans `automations.yaml` prod (controle du script : 62 en prod, 63 YAML locaux retenus, 66 fiches dont 62 rattachees).

| Categories HA | Nb reel |
|:--------------|:--------|
| _SANS_CATEGORIE | 2 |
| Backup HA <-> GitHub | 7 |
| Bouton Virtuel | 2 |
| Controle Entity z2m | 1 |
| Gestion des Stores | 2 |
| MariaDB & VSCode Optimisation | 2 |
| Meteo | 5 |
| P0_ENRIGE | 6 |
| P1_01_CLIM_CHAUFFAGE | 10 |
| P1_02_Cuisine | 2 |
| P1_03_Chauffage Salle de Bain | 9 |
| P2_Alarme_Congelateur | 3 |
| P2_eCO. Prises | 3 |
| P3_Eclairage | 6 |
| Tarif HC/HP | 1 |
| Watchdog Piles (HUE/IKEA/SONOFF) | 1 |

> Source : sections du `GLOBAL_INDEX_AUTOMATIONS.md` genere le 2026-10-13 (somme = 62). Hors prod : 1 YAML local (RASPI : ventilateur Raspberry Pi 4, sans id), liste dans la section "Hors prod ou sans id" de l'index.

---

## Structure de l'index genere

Une section par categorie HA, avec le nombre d'automations entre parentheses. Colonnes : `N | Alias | id prod | id local (ReBuild) | Entity HA | Documentation (md) | YAML source | Commentaire`. Les liens sont relatifs au fichier. En tete, un bloc "Controle" donne les ecarts (sans YAML, sans fiche, sans entity_id, YAML hors prod, fiches non rattachees).

---

## Anomalies connues / ouvertes

- Le bloc "Controle" de l'index (2026-10-13) signale 1 automation sans fiche rattachee : `AUTO. ENERGIE. Basculement Tarif HC/HP - Genelec Appart` (fiche `BASCULEMENT_TARIF_HPHC.md` non rattachee a un YAML).
- Le resume `03-AUTOMATIONS` de GLOBAL_INDEX_REPO.md n'est pas regenere : il peut etre en retard sur l'index genere.

---

## Comment mettre a jour l'index

Apres ajout/suppression/renommage d'une automation dans HA :

1. Creer/archiver le fichier YAML correspondant dans `Docs_automations_yaml/` et la fiche dans `Docs_automations_md/`.
2. Lancer `/histo` (regenere `GLOBAL_INDEX_AUTOMATIONS.md`) ou, a la main : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_Docs_scripts\Docs_scripts_sh\Gen_GLOBAL_INDEX_automations\Gen_GLOBAL_INDEX_automations.py"`.
3. Verifier la ligne `liens=N casses=M` : `casses` doit etre 0.
4. Mettre a jour a la main le resume `03-AUTOMATIONS` de `GLOBAL_INDEX_REPO.md` si besoin (compteur de la categorie), puis pousser `H:\GLOBAL_INDEX_REPO.md` aux 2 endroits (racine et miroir docs) avec `/ha-push-docs`.
