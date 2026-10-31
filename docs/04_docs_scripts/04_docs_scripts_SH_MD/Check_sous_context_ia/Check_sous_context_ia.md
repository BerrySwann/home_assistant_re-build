# Check_sous_context_ia.py - controle des fichiers IA_* de 00_IA_SOUS_CONTEXT_IA (lecture seule)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifie](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-4fc3f7?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/Check_sous_context_ia/Check_sous_context_ia.py` |
| Langage | Python 3 (module `yaml` requis) |
| Lance par | /histo (etape 6, point 7). Ne fait pas tourner Home Assistant |
| Ecrit | rien : il rapporte les ecarts |

## Role

Controle les fichiers `IA_*` de `docs/00_IA/00_IA_SOUS_CONTEXT_IA` (le script parle de 9 fichiers). Controles par fichier :

1. structure : dossier = nom du fichier, fichier present, `.bak` bien nommes, plafonds (10 le jour meme, 3 par jour passe) ;
2. prod : `H:\docs\00_IA\00_IA_SOUS_CONTEXT_IA\<nom>\<nom>.md` present et MD5 identique ;
3. date declaree dans l'en-tete contre la date de modification du fichier ;
4. chemins `docs/...` cites : existent en local ;
5. nombres du type "N automations" ou "N vignettes" contre la prod et les dossiers ;
6. entites citees : presentes dans `core.entity_registry` ou `core.restore_state`.

`IA_SKILLS_INVENTAIRE` est dans `NON_POUSSES` (pas en prod tant qu'Eric ne le demande pas).

## Utilisation

```
$env:PYTHONIOENCODING='utf-8'; python -I Check_sous_context_ia.py
```

Derniere ligne : `controle sous_context_ia: dossiers=N baks=N ecarts=N casses=N`.

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture de l'en-tete et des sorties du fichier source.
