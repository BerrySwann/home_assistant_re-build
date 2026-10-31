# audit_carte_docs_hermes.py - audit lecture seule de la carte des docs (arborescence + index)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--31-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-4fc3f7?style=flat-square)](.)

</div>

*Cree le 2026-10-31 : copie maitre du script Hermes rangee dans le depot (ordre d'Eric)*

## Role
Recompte l'arborescence documentaire en local et en prod, sauvegardes `.bak` comptees a part, puis traite chaque fichier d'index : empreinte md5 comparee a la copie de prod, et test d'existence des liens et chemins qu'il cite, en deux passes. Lecture seule : ne modifie AUCUN fichier.

## Emplacement
- Script : `docs\04_docs_scripts\04_docs_scripts_SH\audit_carte_docs_hermes\audit_carte_docs_hermes.py`
- Original vivant : `D:\hermes\skills\smart-home\ha-projet-documentation\scripts\audit_carte_docs.py`
- Fiche : `docs\04_docs_scripts\04_docs_scripts_SH_MD\audit_carte_docs_hermes\audit_carte_docs_hermes.md`
- Constantes a regler avant lancement, en tete du script : `LOCAL` (`C:/Users/Berry Swann/Documents/ReBuild`), `PROD` (`H:` + separateur), `ZONES` (10 zones), `INDEX` (4 fichiers d'index)
- Sous-dossiers ignores partout : `.git`, `node_modules`, `__pycache__`

## Lancement
`python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\audit_carte_docs_hermes\audit_carte_docs_hermes.py"`

- Aucun argument, aucune option : tout est en dur dans `LOCAL`, `PROD`, `ZONES` et `INDEX`. Les regler avant de lancer.
- Le disque `H:` doit etre monte : sinon la colonne prod ressort `-` partout et aucune comparaison de miroir n'est faite pour les index.
- Rien n'est ecrit sur disque : toute la sortie va sur stdout.

## Sortie et codes de retour
Deux blocs, dans cet ordre.

**1. ARBORESCENCE (recomptage)** : une ligne par zone des `ZONES`, colonnes `zone` / `local` / `prod`. La valeur est `N (dont M .bak)` quand le dossier existe, `ABSENT` en local s'il manque, `-` en prod quand la zone est locale seulement (`docs/99_docs_MD_system/`, `historique/`, `scripts/`) ou absente. Le script rappelle ensuite que les `.bak` sont compris dans les totaux et qu'il faut publier les deux chiffres.

**2. INDEX : miroir local / prod puis liens** : pour chaque fichier d'`INDEX`, une ligne `### <chemin relatif>` suivie de l'empreinte md5 sur 8 caracteres et, si la copie prod existe, de `miroir local/prod identique` ou `ECART avec prod (<md5 prod>)`. Un index absent en local donne `### <chemin> : ABSENT en local` et est saute. Pour un index range sous `Github/`, la copie prod est cherchee sans ce prefixe.

Puis, par index : `N references   N DISPARUS   N cites sans leur dossier`, avec au plus 12 lignes `disparu : <lien>` et 6 lignes `a reecrire : <lien>  ->  <emplacement>` (2 emplacements max par nom, prefixes `PROD:` cote prod). Les compteurs affiches restent complets meme quand les listes sont tronquees.

Liens ignores : `http://`, `https://`, `mailto:`, `#`. Un lien est teste en local puis en prod, apres retrait d'un `/` initial, normalisation des `\` et retrait du prefixe `homeassistant/`.

Codes de retour :
- 0 : le script est alle au bout. Un lien disparu ou un ecart md5 n'y change rien : l'alerte est dans le texte, pas dans le code.
- Non nul : exception non rattrapee (index present mais illisible par exemple), sortie interrompue au milieu du bloc 2.

## Limites
- Perimetre fige dans le script : 10 zones et 4 index. Un dossier ou un index hors de ces listes n'est jamais vu.
- `carte_noms` s'arrete a 6 niveaux sous `LOCAL` et sous `PROD` : au-dela, un nom de fichier cite n'est plus reconnu et le lien tombe dans les DISPARUS.
- Les `.bak` sont comptes dans les totaux : ne pas les omettre en reprenant les chiffres.
- Aucune verification reseau ni de contenu : seuls l'existence des chemins et l'empreinte md5 tronquee des index sont controles.
- Un chemin absolu Windows passe tel quel a `os.path.join` (`C:` + reste) : il est juge disparu meme si le fichier existe.
- La resolution par nom retient 2 emplacements par fichier au maximum et ne tranche pas lequel est le bon.
- Index lu en `utf-8` avec `errors="replace"` : un fichier dans un autre encodage ne leve pas d'erreur mais peut fausser la liste des liens.
- md5 tronque a 8 caracteres : suffisant pour reperer un ecart entre local et prod, pas comme preuve d'integrite.
- Ne remplace pas un controle de presence des dossiers `XX_` : cet audit-la est le role de `Check_XX_presents.py`.
