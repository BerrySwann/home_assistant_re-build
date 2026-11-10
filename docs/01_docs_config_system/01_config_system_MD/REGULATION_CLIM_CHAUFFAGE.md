# Regulation clim et chauffage - deroulement complet

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--09-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-System-ffeb3b?style=flat-square)](.)

</div>

Fiche de reference du 2026-11-08. Elle decrit la chaine reelle, telle qu elle tourne, du capteur
brut jusqu a la consigne envoyee aux climatiseurs. Les valeurs et les formules ont ete relues dans
le fichier de production, pas recopiees d une doc anterieure.

Deux etages, et il faut les distinguer :

- le template `P1_01_clim_logique_system_autom.yaml` calcule des temperatures
- le script `p1_master_gestion_clim` decide laquelle envoyer a quelle clim, selon la presence et la periode

Le template ne pilote rien. Il produit des nombres. C est le script qui agit.

## 1. Les constantes

| Capteur | Valeur | Role |
|:--|--:|:--|
| `seuil_non_chauffage` | 19 | seuil de bascule heat vers off, et consigne d hiver |
| `seuil_non_clim` | 26 | seuil de bascule off vers cool, et consigne d ete |
| `temperature_eco_hiver` | 17 | eco de base en hiver |
| `temperature_eco_ete` | 28 | eco de base en ete |
| `delta_1` | 1 | petit ecart, majoration du confort, plafonds de nuit |
| `delta_2` | 2 | ecart moyen, palier de froid |
| `delta_3` | 3 | declare, utilise nulle part |
| `delta_5` | 5 | palier de chaleur |
| `delta_7` | 7 | palier de forte chaleur |

`seuil_non_chauffage` est a 19, mais il peut descendre a 18 pour des raisons d economie d energie.
Comme il sert a la fois de consigne d hiver et de plafond pour la nuit, ce seul chiffre deplace toute la
partie hivernale : la consigne, le confort, les trois pieces, la nuit, et la borne basse de la zone off.
La section 9 bis donne les deux jeux de valeurs cote a cote.

## 2. Le mode, calcule par `mode_ete_hiver`

Le capteur compare la sonde du balcon aux deux seuils :

| Exterieur | Mode | Ce qui se passe |
|:--|:--|:--|
| sous 19 | **heat** | chauffage possible |
| de 19 a 26 exclu | **off** | rien, les clims sont arretees |
| a partir de 26 | **cool** | climatisation possible |

La plage 19 a 26 est morte. Sept degres sur la plage utile ou aucune consigne n est envoyee.

## 3. La consigne

Elle prend simplement la valeur du seuil correspondant a la saison :

`consigne` = `seuil_non_chauffage` en heat, `seuil_non_clim` en cool. Donc 19 en hiver, 26 en ete.

Attention, en mode off le capteur retombe sur `seuil_non_chauffage` : la consigne vaut 19 dans la zone morte aussi.

## 4. Le confort, le moteur

C est `temperature_confort`. Toute la logique de paliers est la.

En chauffage :

| Exterieur | Confort | Formule |
|:--|--:|:--|
| sous 8 | 21 | consigne + delta_2 |
| de 8 a 12 exclu | 20 | consigne + delta_1 |
| au-dessus | 19 | consigne |

En climatisation :

| Exterieur | Confort | Formule |
|:--|--:|:--|
| au-dessus de 34 | exterieur - 8 | exterieur moins delta_7 moins delta_1 |
| de 32 exclu a 34 | exterieur - 6 | exterieur moins delta_5 moins delta_1 |
| jusqu a 32 | 26 | consigne |

Le confort n est pas monotone en ete : a 33 il donne 27, a 34 il redescend a 26, puis il remonte.
Le decrochement vient du passage de delta_5 a delta_7, on retranche huit au lieu de six d un coup.

## 5. Confort jour et confort nuit

`temperature_confort_jour` recopie le confort, sans calcul propre.

`temperature_confort_nuit` a sa propre logique :

| Saison | Nuit | Formule |
|:--|--:|:--|
| cool | 26 | valeur fixe |
| heat | 19 | confort + delta_1, plafonne a seuil_non_chauffage |

En hiver la nuit est donc plate a 19, quel que soit l exterieur. Le plafond `seuil_non_chauffage` vaut justement 19,
il ecrase les 21 et 20 du confort. Les paliers de jour ne traversent pas la nuit.

## 6. Les corrections par piece

Chaque piece a ses propres regles, differentes en hiver et en ete. En hiver ce sont des paliers fixes lus sur la sonde exterieure ; en ete, une seule marche entre 27 et 28 C dehors, sur leurs plafonds respectifs.

| Piece | Hiver | Ete |
|:--|:--|:--|
| Salon | 22 sous 8, 21 de 8 a 12, 20 au-dela | 26 jusqu a 27 C dehors, 27 au-dela |
| Bureau | 20 sous 8, 19 de 8 a 12, 18 au-dela | 26 jusqu a 27 C dehors, 27 au-dela |
| Chambre | 20 sous 8, 19 de 8 a 12, 18 au-dela | 26 jusqu a 27 C dehors, 27 au-dela |

Etat reel du code au 2026-11-10, verifie en service : le salon reste sur la formule par plafond,
`min(confort jour, 22)`, mais le confort jour monte desormais a 22 sous 8 C, donc le plafond mord pile au
bon endroit. Le salon sort 22 sous 8 C, 21 de 8 a 12, 20 au-dessus.

Le confort jour lui-meme a ete corrige le 2026-11-10 : la branche de 8 a 12 C reprenait delta_1 et
rendait exactement la meme valeur que la branche du dessus, et delta_3 n etait lu par personne. Chaque palier
prend maintenant un delta de plus : `consigne + delta_3` sous 8 (22), `consigne + delta_2` de 8 a 12 (21),
`consigne + delta_1` au-dela (20).

Le bureau et la chambre ont ete passes en paliers le 2026-11-10 sur demande d Eric, trois paliers derives
de la consigne et de delta_1 : `consigne + delta_1` sous 8 C (soit 20), `consigne` de 8 a 12 (19), et
`consigne - delta_1` au-dela de 12 (18). Aucune valeur n est ecrite en dur : si la consigne passe de 19 a 18,
les trois paliers deviennent 19, 18 et 17 tout seuls.

Cette section decrivait auparavant une version a paliers fixes ecrits en dur, posee le 2026-11-08 a 11h04
puis retiree le 2026-11-09 a 19h56 sur ordre d Eric. La fiche etait restee sur cette version disparue et ne
correspondait plus au code depuis cette date.

En ete ces trois capteurs n utilisent plus le confort du tout : ils lisent directement la sonde exterieure.
Une seule marche, entre 27 et 28 C dehors.

En hiver, chaque piece bouge maintenant : le salon de 22 a 20, le bureau de 20 a 18, la chambre de 19 a 18.
Aucune ne recopie plus le confort jour, et le groupe de presence ne change plus la source : depuis le
2026-11-08, `groupe_2`, `groupe_3` et `groupe_4` recoivent tous `tccsj_s`, `tccsj_b` et `tccsj_c`.
La seule exception reste `groupe_1`, qui envoie l eco aux trois.

## 6 bis. Les offsets de capteur

Les clims mesurent sur leur retour d air, pas au milieu de la piece, et cette mesure lit sous l ambiance
reelle. Mesure du 2026-11-10 sur la nuit, en regime stable : consigne 19 au bureau sortait 22,0, consigne 19
a la chambre sortait 21,8 a 22,0, consigne 20 au salon sortait 21,5. Les deux premieres derivent de 3 C, le
salon de 1,5 C.

Trois capteurs constants portent ces offsets, declares avec les parametres fixes du master : `offset_salon`
a 1, `offset_bureau` a 3, `offset_chambre` a 3. Le salon demarre a 1 et non 1,5 sur decision d Eric du
2026-11-10 : il veut tester la consommation avec une piece a 21 C avant de descendre a 2.

L offset n est PAS applique dans le master. `temperature_corrige_*` garde son sens de temperature visee,
celle que le tableau de bord affiche. C est le script qui soustrait, au dernier moment, sur la valeur
envoyee a la clim. Pour viser 18 au bureau, la clim recoit 15.

Le sens est le meme en hiver et en ete : le capteur sous-estime, donc en chaud la piece depasse la cible et
en froid elle passerait dessous. C est toujours une soustraction.

Les planchers passent : salon 19 au pire cas pour un minimum accepte de 16, bureau et chambre 15 pour un
minimum de 10.

Ce reglage reste a confirmer. Il vient d une seule nuit et d une clim en phase de chauffe ; si le biais
differe a l arret, l offset ne sera juste qu en chauffage actif.

### La nuit, une seule cible

Le 2026-11-10 un second capteur de nuit avait ete cree pour faire descendre le bureau et la chambre a 18
alors que le salon restait a 19. Il a ete retire le meme soir sur decision d Eric, qui veut y revenir plus
tard. La nuit repasse donc par le seul `temperature_confort_nuit`, plafonne a `seuil_non_chauffage` : 19
pour les trois pieces. Les offsets s appliquent ensuite.

| periode | salon | bureau | chambre |
|:--|:--|:--|:--|
| jour vise | 20 | 18 | 18 |
| jour envoye | 19 | 15 | 15 |
| nuit vise | 19 | 19 | 19 |
| nuit envoye | 18 | 16 | 16 |

## 7. L eco de saison

L eco a une valeur brute, 17 en hiver et 28 en ete, et une valeur corrigee par la temperature exterieure.

`temperature_eco_hiver_corrige` suit les paliers du confort : plus delta_2 sous 8 C dehors,
plus delta_1 sous 12, valeur brute au-dessus.

| Saison | Exterieur | Eco brut | Eco corrige |
|:--|:--|--:|--:|
| hiver | sous 8 | 17 | **19** |
| hiver | de 8 a 12 | 17 | **18** |
| hiver | au-dessus de 12 | 17 | **17** |
| ete | sous 28 | 28 | **27** |
| ete | a partir de 28 | 28 | **28** |

L eco d ete suit une autre regle : il retire delta_1 tant qu il ne fait pas 28 C dehors, et rend la valeur
brute a partir de 28. C est l inverse de l hiver, ou l eco monte quand il fait froid.

## 7 bis. Eco en jour et en nuit

L eco de saison s applique de la meme facon en journee et la nuit. Ce n est pas la periode qui le declenche,
c est l absence : le script prend l eco des que le groupe de presence vaut `groupe_1`, quel que soit le
moment, et aussi quand un capteur manque et qu il bascule en mode degrade.

| Saison | Exterieur | Salon | Bureau | Chambre |
|:--|:--|--:|--:|--:|
| hiver | sous 8 | 19 | 19 | 19 |
| hiver | de 8 a 12 | 18 | 18 | 18 |
| hiver | au-dessus de 12 | 17 | 17 | 17 |
| ete | sous 28 | 27 | 27 | 27 |
| ete | a partir de 28 | 28 | 28 | 28 |

Et quand une fenetre est ouverte, le script ne calcule pas d eco du tout : il coupe les trois unites.


## 8. Le script `p1_master_gestion_clim`

C est lui qui pilote. Le template ne fait que fournir des nombres.

Il est appele par l automation A0 le matin a 7h30 avec `periode: jour`, et par B0 le soir a 21h00 avec
`periode: nuit`. Il recoit aussi l entite declencheuse, pour les notifications de fenetre.

Son deroulement, en huit etapes :

1. Il pose un prefixe de notification, `[AJ]` ou `[AN]`.
2. Si le declencheur est `ha_restart`, il attend une minute que les capteurs se stabilisent.
3. Il boucle jusqu a dix fois, trente secondes entre chaque essai, tant que tous les capteurs necessaires
   ne repondent pas.
4. Passe les dix essais, il diagnostique ce qui manque et pose trois drapeaux : arret de securite,
   mode degrade eco, ou normal.
5. Il applique la sortie : coupure des trois unites, reglage sur l eco de saison, ou on continue.
6. Il calcule ses variables : mode, presence, fenetres ouvertes, eco, cibles par piece.
7. Il calcule les trois cibles, salon, bureau et chambre, selon la periode et le groupe de presence.
8. Enfin, si une fenetre est ouverte il coupe tout et s arrete. Sinon il envoie les consignes aux trois
   unites en parallele, puis un resume par notification.

Le choix des cibles, avec les noms de groupe :

| Groupe | Periode | Salon | Bureau | Chambre |
|:--|:--|:--|:--|:--|
| groupe_1, absent | jour et nuit | eco de saison | eco de saison | eco de saison |
| groupe_2 | jour | tccsj_s | tccsj_b | tccsj_c |
| groupe_3 | jour | tccsj_s | tccsj_b | tccsj_c |
| groupe_4 | jour | tccsj_s | tccsj_b | tccsj_c |
| tout groupe sauf 1 | nuit | valeur nuit | valeur nuit | valeur nuit |

Les trois groupes de jour sont interchangeables depuis le 2026-11-08. Le script ne choisit plus la source
selon qui est present, il envoie a chaque piece celle qu elle calcule.

Deux comportements historiques ont ete supprimes ce jour-la. En `groupe_3`, le salon recevait `tccsj_b`, la
consigne du bureau, donc 3 C de moins que la sienne : c etait un reste de l epoque ou Mamour et Eric avaient
chacun leur piece, conserve apres l essai du 2026-11-07. Et en `groupe_2`, le bureau basculait en eco en
chauffage tout en gardant `tccsj_b` en clim.

Chaque commande est conditionnee a deux verifications : la prise de la clim doit etre alimentee, et le flag
d arret securise doit etre a off. Si la clim est deja eteinte et que le declencheur est `sensor_update`,
le script ne la rallume pas.

## 9. Recapitulatif par plage

D abord ce que la chaine CALCULE, avant que le script ne choisisse :

| Exterieur | Mode | Confort | Jour | Nuit | Salon tccsj_s | Bureau tccsj_b | Chambre tccsj_c | Eco |
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
| 0 a 7 | heat | 21.0 | 21.0 | 19.0 | 22 | 20 | 19 | 19.0 |
| 8 a 11 | heat | 20.0 | 20.0 | 19.0 | 21 | 19 | 19 | 18.0 |
| 12 a 18 | heat | 19.0 | 19.0 | 19.0 | 20 | 18 | 18 | 17.0 |
| 19 a 25 | off | 19.0 | 19.0 | 19.0 | 20 | 18 | 18 | 17.0 |
| 26 a 27 | cool | 26.0 | 26.0 | 26 | 25 | 26 | 26 | 27.0 |
| 28 a 32 | cool | 26.0 | 26.0 | 26 | 26 | 27 | 27 | 28.0 |
| 33 | cool | 27.0 | 27.0 | 26 | 26 | 27 | 27 | 28.0 |
| 34 | cool | 26.0 | 26.0 | 26 | 26 | 27 | 27 | 28.0 |
| 35 | cool | 27.0 | 27.0 | 26 | 26 | 27 | 27 | 28.0 |
| 36 a 40 | cool | 30.0 | 30.0 | 26 | 26 | 27 | 27 | 28.0 |

Puis ce que le script ENVOIE. Depuis le 2026-11-08 les trois cibles sont symetriques :

| Groupe | Periode | Salon recoit | Bureau recoit | Chambre recoit |
|:--|:--|:--|:--|:--|
| groupe_1 | jour et nuit | eco | eco | eco |
| groupe_2 | jour | tccsj_s | tccsj_b | tccsj_c |
| groupe_3 | jour | tccsj_s | tccsj_b | tccsj_c |
| groupe_4 | jour | tccsj_s | tccsj_b | tccsj_c |
| tous sauf 1 | nuit | temp_nuit | temp_nuit | temp_nuit |

Les groupes 2, 3 et 4 sont interchangeables. Avant le 2026-11-08, le groupe_3 envoyait au salon
`tccsj_b` et le groupe_2 basculait le bureau en eco : ces deux exceptions ont ete supprimees.

## 9 bis. Variante seuil_non_chauffage a 18

Le seuil de chauffage vaut 19 en service. S il passe a 18, la consigne et la nuit tombent d un degre,
mais les trois PIECES ne bougent plus : depuis le 2026-11-08 elles ont des paliers fixes, lus sur la
sonde exterieure, et ne dependent plus de la consigne.

| Exterieur | Mode 19 | Conf 19 | Nuit 19 | Mode 18 | Conf 18 | Nuit 18 | Pieces (identiques) |
|:--|:--|--:|--:|:--|--:|--:|:--|
| sous 8 | heat | 21.0 | 19.0 | heat | 20.0 | 18.0 | salon 22, bureau 20, chambre 19 |
| 8 a 12 | heat | 20.0 | 19.0 | heat | 19.0 | 18.0 | salon 21, bureau 19, chambre 19 |
| 12 a 17 | heat | 19.0 | 19.0 | heat | 18.0 | 18.0 | salon 20, bureau 18, chambre 18 |
| 17 a 18 | heat | 19.0 | 19.0 | heat | 18.0 | 18.0 | salon 20, bureau 18, chambre 18 |
| 18 a 19 | heat | 19.0 | 19.0 | off | 18.0 | 18.0 | salon 20, bureau 18, chambre 18 |
| 19 a 26 | off | 19.0 | 19.0 | off | 18.0 | 18.0 | salon 20, bureau 18, chambre 18 |

Seuls le mode, le confort, la nuit et l eco suivent le seuil. Les pieces, elles, sont desormais
insensibles a cette valeur : c est la consequence directe de la refonte du 2026-11-08.
La zone off gagne un degre en bas : elle commence a 18 au lieu de 19.

## 9 ter. Ce que recoit chaque piece, groupe par groupe

Valeurs produites par le script lui-meme, ses trois templates rendus avec les vrais capteurs, consigne a 19
en hiver. Depuis le 2026-11-08 les trois pieces ne dependent plus du groupe : seules la periode et la
temperature exterieure changent la valeur.

### SALON
| Groupe | Periode | sous 8 | 8 a 12 | au-dela de 12 |
|:--|:--|--:|--:|--:|
| groupe_1 | jour | 19.0 | 18.0 | 17.0 |
| groupe_1 | nuit | 19.0 | 18.0 | 17.0 |
| groupe_2 | jour | 22.0 | 21.0 | 20.0 |
| groupe_2 | nuit | 19.0 | 19.0 | 19.0 |
| groupe_3 | jour | 22.0 | 21.0 | 20.0 |
| groupe_3 | nuit | 19.0 | 19.0 | 19.0 |
| groupe_4 | jour | 22.0 | 21.0 | 20.0 |
| groupe_4 | nuit | 19.0 | 19.0 | 19.0 |

### BUREAU
| Groupe | Periode | sous 8 | 8 a 12 | au-dela de 12 |
|:--|:--|--:|--:|--:|
| groupe_1 | jour | 19.0 | 18.0 | 17.0 |
| groupe_1 | nuit | 19.0 | 18.0 | 17.0 |
| groupe_2 | jour | 20.0 | 19.0 | 18.0 |
| groupe_2 | nuit | 19.0 | 19.0 | 19.0 |
| groupe_3 | jour | 20.0 | 19.0 | 18.0 |
| groupe_3 | nuit | 19.0 | 19.0 | 19.0 |
| groupe_4 | jour | 20.0 | 19.0 | 18.0 |
| groupe_4 | nuit | 19.0 | 19.0 | 19.0 |

### CHAMBRE
| Groupe | Periode | sous 8 | 8 a 12 | au-dela de 12 |
|:--|:--|--:|--:|--:|
| groupe_1 | jour | 19.0 | 18.0 | 17.0 |
| groupe_1 | nuit | 19.0 | 18.0 | 17.0 |
| groupe_2 | jour | 19.0 | 19.0 | 18.0 |
| groupe_2 | nuit | 19.0 | 19.0 | 19.0 |
| groupe_3 | jour | 19.0 | 19.0 | 18.0 |
| groupe_3 | nuit | 19.0 | 19.0 | 19.0 |
| groupe_4 | jour | 19.0 | 19.0 | 18.0 |
| groupe_4 | nuit | 19.0 | 19.0 | 19.0 |

Le salon est la seule piece qui monte : 22 sous 8 C, contre 19 avant. Le bureau descend d un degre.
La chambre perd son palier a 19 pour 8-12, elle passe directement de 19 a 18 a 12 C dehors.

La nuit ecrase tout : les trois pieces recoivent `temp_nuit`, 19 en chauffage, sauf en `groupe_1` ou
l eco de saison s applique avant la periode.

## 10. Les pieges

`temperature_cible` et `temperature_t_conferentielle` n existent plus. Ne pas les reintroduire sans
recabler le calcul, l ancienne formule confort plus cible moins consigne a ete retiree le 2026-11-07.

`temperature_corrige_eric` s appelle `temperature_corrige_bureau` depuis le renommage du 2026-11-03.

La zone off de 19 a 26 degres est morte. Toute la mecanique de paliers n a d effet que sous 8 C et au-dela
de 32, parce que la plage intermediaire n est jamais appliquee.

En ete, au-dela de 32 C exterieur le confort suit la sonde et peut demander 32 C a l interieur quand il en
fait 40 dehors. Une clim residentielle refuse generalement au-dela de 30.

Le fichier est critique : toute modification impacte toutes les automations clim. Et HA reecrit `scripts.yaml`
a chaque enregistrement depuis l interface, donc une comparaison de texte brut entre deux copies ne veut rien dire,
il faut comparer le YAML relu.
