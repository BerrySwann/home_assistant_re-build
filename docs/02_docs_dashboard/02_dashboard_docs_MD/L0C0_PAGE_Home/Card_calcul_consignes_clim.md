# Card_calcul_consignes_clim

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--07-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Dashboard-4fc3f7?style=flat-square)](.)

</div>

> Fiche creee le 2026-11-07. Carte `markdown` seule qui explique en clair les consignes de la clim : le palier actif, les consignes par defaut, les consignes calculees, les trois pieces avec leurs plafonds, et l'eco corrige.

| Champ | Valeur |
|:------|:-------|
| **Fichier YAML** | `docs/02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/Card_calcul_consignes_clim.yaml` |
| **Cellule** | L0C0_PAGE_Home |
| **Type racine** | `vertical-stack` avec une seule carte `markdown` |
| **Taille** | 91 lignes, 4556 octets |

## Role

Rendre lisible ce que fait le template master `P1_01_clim_logique_system_autom`, sans avoir a ouvrir le YAML. La carte ne decide rien : elle relit les capteurs et les met en phrase.

## Capteurs lus

- `sensor.th_balcon_nord_temperature`, `sensor.mode_ete_hiver`
- `sensor.consigne`, `sensor.temperature_confort`
- `sensor.delta_1`, `_2`, `_5`, `_7`
- `sensor.temperature_confort_jour`, `sensor.temperature_confort_nuit`
- `sensor.temperature_corrige_salon`, `_bureau`, `_chambre`
- `sensor.temperature_eco_hiver_corrige`, `sensor.temperature_eco_ete_corrige`
- `sensor.temperature_eco_hiver`, `sensor.temperature_eco_ete` pour les bases
- `sensor.temperature_delta_affichage`, `sensor.groupe`, `sensor.presence`

## Vocabulaire tenu par la carte

La consigne de jour est dite **compensee** : elle suit la temperature exterieure, par paliers a 8 et 12 C.
La consigne de nuit est dite **consigne regulee** : le mecanisme tourne, mais la valeur ne bouge pas sous 19 C dehors.
Ne pas ecrire « fixe » a la place de « regulee » : cela suggere une valeur en dur, alors que la nuit est un resultat de calcul.

## Trois pieges de mise en forme, mesures

1. `content: >` replie les retours a la ligne et colle les puces d'une liste sur une seule ligne. Utiliser `content: |`.
2. Un `{% endif %}` manquant rend la carte **vide**, sans message. Il doit y avoir autant de `endif` que de `if` ; un `elif` n'ajoute pas de `endif`.
3. Les balises Jinja laissent des lignes vides qui cassent les listes markdown. Regle qui marche : `-%}` sur `if`, `elif`, `else` et `set`, `%}` nu sur `endif`, et aucune ligne vide dans le source avant un titre qui suit un `endif`.

## A savoir

Les plafonds d hiver sont dans le master seul : 21 pour le salon (baisse de 22 a 21 le 2026-11-07), 21 pour le bureau, 19 pour la chambre. En ete : 26 salon, 27 bureau, 27 chambre. La carte ne reproduit plus aucun plafond en dur : elle affiche la valeur des capteurs temperature_corrige_*, donc elle ne peut plus mentir si un plafond change.

Le palier ete fort (34 C, delta_7) est affiche par la carte **et applique par le master** depuis le 2026-11-07 : temperature_confort_jour teste desormais >= 34 avec delta_7, puis > 32 avec delta_5. Les six lignes de palier de la carte ont ete alignees sur le calcul reel du template, qui majore chaque palier de delta_1 (confort jour). Ecart clos.
