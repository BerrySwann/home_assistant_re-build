# Regulation clim et chauffage - deroulement complet

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

Elles s appliquent sur le confort jour, avec un plafond different par piece et par saison.

| Piece | Hiver | Ete |
|:--|:--|:--|
| Salon | confort jour, plafond 21 | 25 jusqu a 27 C dehors, 26 au-dela |
| Bureau | confort jour, plafond 19 | 26 jusqu a 27 C dehors, 27 au-dela |
| Chambre | confort jour, plafond 19 | 26 jusqu a 27 C dehors, 27 au-dela |

En ete ces trois capteurs n utilisent plus le confort du tout : ils lisent directement la sonde exterieure.
Une seule marche, entre 27 et 28 C dehors.

En hiver, le plafond de 19 pour le bureau et la chambre les bloque quel que soit l exterieur. Seul le salon
bouge encore, entre 21 sous 8 C et 19 au-dessus de 12.

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
| groupe_1, absent | jour | eco de saison | eco de saison | eco de saison |
| groupe_2 | jour | valeur du salon | eco de saison | valeur chambre |
| groupe_3 | jour | valeur du bureau | valeur du bureau | valeur chambre |
| groupe_4 | jour | valeur du salon | valeur du bureau | valeur chambre |
| tout groupe sauf 1 | nuit | valeur nuit | valeur nuit | valeur nuit |

Le point a retenir : quand Eric est seul, le salon prend la consigne du **bureau**, pas la sienne. C est un
comportement historique, conserve apres essai le 2026-11-07.

Chaque commande est conditionnee a deux verifications : la prise de la clim doit etre alimentee, et le flag
d arret securise doit etre a off. Si la clim est deja eteinte et que le declencheur est `sensor_update`,
le script ne la rallume pas.

## 9. Recapitulatif par plage

Valeurs que la chaine complete produit, script compris, avec la consigne a 19 en hiver et 26 en ete.

| Exterieur | Mode | Confort | Jour | Nuit | Salon | Bureau | Chambre |
|:--|:--|--:|--:|--:|--:|--:|--:|
| 0 a 7 | heat | 21 | 21 | 19 | 21 | 19 | 19 |
| 8 a 11 | heat | 20 | 20 | 19 | 21 | 19 | 19 |
| 12 a 18 | heat | 19 | 19 | 19 | 19 | 19 | 19 |
| 19 a 25 | off | 19 | 19 | 19 | rien | rien | rien |
| 26 a 27 | cool | 26 | 26 | 26 | 25 | 26 | 26 |
| 28 a 32 | cool | 26 | 26 | 26 | 26 | 27 | 27 |
| 33 | cool | 27 | 27 | 26 | 26 | 27 | 27 |
| 34 | cool | 26 | 26 | 26 | 26 | 27 | 27 |
| 35 | cool | 27 | 27 | 26 | 26 | 27 | 27 |
| 36 a 40 | cool | 28 a 32 | 28 a 32 | 26 | 26 | 27 | 27 |

Degres Celsius.

## 9 bis. Variante seuil_non_chauffage a 18

Le seuil de chauffage vaut 19 en service. Si l on passe a 18 pour economiser, tout l hiver se decale d un degre.
Le plafond de la nuit suit, puisqu il lit ce meme seuil.

| Exterieur | Mode | Conf 19 | Nuit 19 | Salon 19 | Bureau 19 | Chambre 19 | Conf 18 | Nuit 18 | Salon 18 | Bureau 18 | Chambre 18 |
|:--|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| sous 8 | heat | 21 | 19 | 21 | 19 | 19 | **20** | **18** | 20 | 19 | 19 |
| 8 a 12 | heat | 20 | 19 | 20 | 19 | 19 | **19** | **18** | 19 | 19 | 19 |
| 12 a 18 | heat | 19 | 19 | 19 | 19 | 19 | **18** | **18** | 18 | 18 | 18 |
| 18 a 19 | heat | 19 | 19 | 19 | 19 | 19 | rien | rien | rien | rien | rien |
| 19 a 26 | off | 19 | 19 | rien | rien | rien | rien | rien | rien | rien | rien |
| 26 et au-dela | cool | 26 | 26 | 25 a 26 | 26 a 27 | 26 a 27 | identique | identique | identique | identique | identique |

Avec la consigne a 18, la nuit tombe a 18 au lieu de 19, et le confort perd un degre sur chaque palier.
Le bureau et la chambre ne bougent pas sous 8 C ni entre 8 et 12, leurs plafonds a 19 les retenant deja.

La zone off commence un degre plus bas : 18 au lieu de 19. Entre 18 et 19 C dehors, la variante 19 chauffe encore sur sa consigne alors que la variante 18 est deja a l arret. C est la seule plage ou les deux jeux divergent sur le mode et pas seulement sur la valeur.

L ete n est pas touche, `seuil_non_clim` reste a 26.

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
