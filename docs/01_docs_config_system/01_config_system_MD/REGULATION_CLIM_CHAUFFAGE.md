# Regulation clim et chauffage - deroulement complet

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--12-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-System-ffeb3b?style=flat-square)](.)

</div>

Fiche de reference, relue dans le fichier de production le 2026-11-11. Les valeurs et les formules
sont relevees dans `P1_01_clim_logique_system_autom.yaml`, pas recopiees d une doc anterieure.
Les editions precedentes annonçaient `delta_3` sous 8 degres : c etait faux, cette correction a ete
annulee et `delta_3` n est lu nulle part.

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
| `delta_1` | 1 | majoration du confort, plafond de nuit, ecart de nuit |
| `delta_2` | 2 | palier de froid, sous 8 degres dehors |
| `delta_3` | 3 | declare, **lu nulle part** |
| `delta_5` | 5 | palier de chaleur, entre 32 et 34 |
| `delta_7` | 7 | palier de forte chaleur, au-dela de 34 |
| `offset_nuit_salon` | 0,3 | largeur de bande morte de la derive de nuit |
| `offset_nuit_bureau` | 0,3 | idem |
| `offset_nuit_chambre` | 0,3 | idem |

`seuil_non_chauffage` est a 19. Il peut descendre a 18 pour des raisons d economie, et ce seul chiffre
deplace toute la partie hivernale : la consigne, le confort, la nuit, et la borne basse de la zone off.

## 2. Le mode, calcule par `mode_ete_hiver`

| Exterieur | Mode | Ce qui se passe |
|:--|:--|:--|
| sous 19 | **heat** | chauffage possible |
| de 19 a 26 exclu | **off** | rien, les clims sont arretees |
| a partir de 26 | **cool** | climatisation possible |

La plage 19 a 26 est morte : sept degres ou aucune consigne n est envoyee.

## 3. La consigne

`consigne` = `seuil_non_chauffage` en heat, `seuil_non_clim` en cool. Donc 19 en hiver, 26 en ete.
En mode off le capteur retombe sur `seuil_non_chauffage` : la consigne vaut 19 dans la zone morte aussi.

## 4. Le confort, avec un plancher sur la sonde exterieure

`temperature_confort` commence par ramener la sonde du balcon a l entier inferieur :

    {% set t_ext = states('sensor.th_balcon_nord_temperature') | float(0) | round(0, 'floor') %}

**Plancher et non arrondi.** Un arrondi deplace les bornes d un demi-degre : a 7,9 il rend 8, donc la
comparaison `8 < 8` devient fausse et la piece bascule en palier doux alors que la sonde est encore a 7,9.
Un plancher rend 7 et la borne reste juste. Mesure du 2026-11-11 sur 20 releves de nuit : 18 changements
d etat pour la sonde brute, 6 avec le plancher, 1 avec l arrondi, mais l arrondi se trompe de seuil a
chaque bascule.

Attention, cette correction ne couvre que `temperature_confort`. Les capteurs de piece en ete lisent la
sonde brute sans plancher, voir section 6.

En chauffage :

| Exterieur | Confort | Formule |
|:--|--:|:--|
| sous 8 | 21 | consigne + delta_2 |
| de 8 a 12 exclu | 20 | consigne + delta_1 |
| au-dessus | 20 | consigne + delta_1 |

Les deux dernieres lignes donnent la meme valeur : le palier 8 a 12 ne se distingue plus.

En climatisation :

| Exterieur | Confort | Formule |
|:--|--:|:--|
| au-dessus de 34 | exterieur - 7 | exterieur moins delta_7 |
| de 32 exclu a 34 | exterieur - 5 | exterieur moins delta_5 |
| jusqu a 32 | 26 | consigne |

Le confort n est pas monotone en ete : 26 a 32, 28 a 33, puis 27 a 34, puis il remonte (29 a 36).
Le decrochement a 34 vient du passage de delta_5 a delta_7.

## 5. Confort jour et confort nuit

`temperature_confort_jour` recopie le confort, sans calcul propre.

`temperature_confort_nuit` a sa propre logique, et ses replis sont volontairement 18 et 26, jamais 0 :
un seuil indisponible a 0 ferait tomber `min()` a zero et enverrait une consigne nulle aux trois clims.

| Saison | Nuit | Formule |
|:--|--:|:--|
| heat | 19 | confort + delta_1, plafonne par seuil_non_chauffage |
| cool | 26 | confort, plafonne par seuil_non_clim |

En hiver la nuit est plate a 19, le plafond ecrase les 21 et 20 du confort. En ete elle est plate a 26.

**Cette nuit n est plus la consigne envoyee.** Depuis le 2026-11-11 le script lit
`temperature_consigne_nuit_*`, voir section 7. `temperature_confort_nuit` alimente encore les captures de
nuit et part dans `delta_ademe_recommande`, ne pas la supprimer.

## 6. Les corrections par piece

| Piece | Hiver | Ete |
|:--|:--|:--|
| Salon | min(confort jour, 22) | min(exterieur - 1, 26) |
| Bureau | min(confort jour, 19) | min(exterieur, 27) |
| Chambre | min(confort jour, 19) | min(exterieur + 1, 27) |

En hiver le confort vaut au minimum 20, donc **bureau et chambre sont plats a 19** et seule la modulation
du salon subsiste, entre 21 sous 8 degres et 20 au-dela. Les trois pieces ne lisent plus la consigne, elles
suivent le confort jour plafonne.

En ete elles ne suivent plus le confort du tout : elles lisent directement la sonde du balcon, et **sans
plancher** puisque le plancher ne s applique qu a l interieur de `temperature_confort`. Une seule marche,
entre 26 et 28 degres dehors.

Depuis le 2026-11-08, `groupe_2`, `groupe_3` et `groupe_4` recoivent tous `tccj_s`, `tccj_b` et `tccj_c`.
La seule exception reste `groupe_1`, qui envoie l eco aux trois.

## 7. Les consignes de nuit et l anti-derive

Ajout du 2026-11-11. C est un dispositif distinct de la nuit de la section 5, et il ne sert qu en periode
de nuit, de 21h00 a 7h30.

Trois capteurs de consigne, un par piece :

    temperature_consigne_nuit_salon = seuil de la saison + input_number.clim_consigne_nuit_salon

Le seuil de la saison vaut 19 en hiver et 26 en ete. L `input_number` vaut 0 par defaut, et va de -3 a +3
par pas de 0,5 : c est la main humaine sur la consigne, sans toucher au YAML.

Trois capteurs d ecart, un par piece, qui prennent la temperature reelle moins la consigne de nuit :

    ecart_nuit_salon = sensor.th_salon_temperature - temperature_consigne_nuit_salon

Trois capteurs de correction, un par piece, qui portent le decalage a retirer de la consigne AVANT
de l envoyer a la clim, pour compenser son capteur de reprise d air qui lit sous l ambiance reelle :

| Capteur | Valeur | Justification |
|:--|--:|:--|
| `correction_temperature_nuit_salon` | 1 | consigne 20 tenait 21,5, ecart 1,5 arrondi |
| `correction_temperature_nuit_bureau` | 3 | consigne 18 tenait 22,0, ecart 4,0 arrondi |
| `correction_temperature_nuit_chambre` | 3 | consigne 18 tenait 21,6, ecart 3,6 arrondi |

Ces ecarts ont ete mesures une seule nuit, le 2026-11-10. Ils sont donc fragiles, et arrondis vers
le bas. Un arrondi vers le bas laisse la piece au-dessus de 19 : c est un choix assume, a reverifier
sur plusieurs nuits.

**Cible et consigne envoyee sont deux choses distinctes, et c est le point a ne pas casser.**
`temperature_consigne_nuit_*` est la CIBLE, celle que lisent J K L, `ecart_nuit_*` et `derive_nuit_*`.
La soustraction se fait dans le script, sur ses variables `tccn_*`, au moment de l envoi. Le
2026-11-12 a la mi-journee, la soustraction avait ete posee dans le capteur de consigne : la cible
est tombee de 19 a 18 et 16, J K L declenchaient en permanence puisque leur seuil etait devenu
18,3 et 16,3, et le -1 restait colle toute la nuit. Corrige le meme jour a 19h15.

Trois capteurs de derive, un par piece, qui appliquent la bonne regle selon la saison :

| Saison | Derive active si | Sens |
|:--|:--|:--|
| heat | ecart > +offset | la piece est trop chaude, on peut baisser |
| cool | ecart < -offset | la piece est trop froide, on peut monter |
| off | jamais | rien a faire |

L offset vaut 0,3 degre. C est une bande morte qui evite qu une piece a 19,05 declenche, puis 19,0 remonte,
en boucle. Sans cette bande un simple dixieme de bruit suffirait a faire osciller le systeme.

Les trois automatisations J, K et L lisent ces derives. **Elles ne les lisent pas encore** : a ce jour elles
comparent la temperature brute a la consigne plus un offset. C est juste en hiver, ou la derive va dans le
sens du chauffage, et aveugle en ete, ou elle s inverse. Correctif a faire.

## 8. L eco de saison

L eco a une valeur brute, 17 en hiver et 28 en ete, et une valeur corrigee par la temperature exterieure.

| Saison | Exterieur | Eco brut | Eco corrige |
|:--|:--|--:|--:|
| hiver | sous 8 | 17 | **19** |
| hiver | de 8 a 12 | 17 | **18** |
| hiver | au-dessus de 12 | 17 | **17** |
| ete | sous 28 | 28 | **27** |
| ete | a partir de 28 | 28 | **28** |

L eco d ete retire delta_1 tant qu il ne fait pas 28 dehors, c est l inverse de l hiver.

L eco s applique de la meme facon en journee et la nuit. Ce n est pas la periode qui le declenche, c est
l absence : le script prend l eco des que le groupe de presence vaut `groupe_1`, et aussi quand un capteur
manque et qu il bascule en mode degrade. Quand une fenetre est ouverte, le script ne calcule pas d eco :
il coupe les trois unites.

## 9. Le script `p1_master_gestion_clim`

C est lui qui pilote. Le template ne fait que fournir des nombres.

Appele par l automation A0 le matin a 7h30 avec `periode: jour`, par B0 le soir a 21h00 avec `periode: nuit`.

Son deroulement, en huit etapes :

1. Il pose un prefixe de notification, `[AJ]` ou `[AN]`.
2. Si le declencheur est `ha_restart`, il attend une minute que les capteurs se stabilisent.
3. Il boucle jusqu a dix fois, trente secondes entre chaque essai, tant que les capteurs necessaires ne
   repondent pas.
4. Passe les dix essais, il diagnostique ce qui manque et pose trois drapeaux : arret de securite, mode
   degrade eco, ou normal.
5. Il applique la sortie : coupure des trois unites, reglage sur l eco de saison, ou on continue.
6. Il calcule ses variables : mode, presence, fenetres ouvertes, eco, cibles par piece.
7. Il calcule les trois cibles selon la periode et le groupe de presence.
8. Si une fenetre est ouverte il coupe tout et s arrete. Sinon il envoie les consignes aux trois unites
   en parallele, puis un resume par notification.

Le choix des cibles :

| Groupe | Periode | Salon | Bureau | Chambre |
|:--|:--|:--|:--|:--|
| groupe_1, absent | jour et nuit | eco de saison | eco de saison | eco de saison |
| groupe_2, 3 ou 4 | jour | tccj_s | tccj_b | tccj_c |
| tout groupe sauf 1 | nuit | tccn_s | tccn_b | tccn_c |

Et ces `tccn_*` ne valent pas la cible : le script soustrait la correction au moment de l envoi.

    tccn_s = temperature_consigne_nuit_salon  - correction_temperature_nuit_salon   -> 19 - 1 = 18
    tccn_b = temperature_consigne_nuit_bureau - correction_temperature_nuit_bureau  -> 19 - 3 = 16
    tccn_c = temperature_consigne_nuit_chambre- correction_temperature_nuit_chambre -> 19 - 3 = 16

Donc la clim vise 18 et 16 alors que la cible interne reste 19. Pendant une derive, J K L
ajoutent le -1 et la clim vise 17 et 15 pendant dix minutes.

Les variables du script se lisent ainsi : `tcc` pour temperature de consigne de confort, puis `j` ou `n`
pour la periode, jour ou nuit, puis `s`, `b` ou `c` pour la piece. Donc `tccj_s` est la consigne de confort
du jour pour le salon, et `tccn_b` celle de la nuit pour le bureau. Une edition anterieure de cette fiche
ecrivait `tccsj_*` : ce nom n existe pas dans le script.

Les trois groupes de jour sont interchangeables depuis le 2026-11-08. Deux comportements historiques ont
ete supprimes ce jour-la : en `groupe_3` le salon recevait `tccj_b`, et en `groupe_2` le bureau basculait en
eco en chauffage tout en gardant `tccj_b` en clim.

Chaque commande est conditionnee a deux verifications : la prise de la clim doit etre alimentee, et le flag
d arret securise doit etre a off. Si la clim est deja eteinte et que le declencheur est `sensor_update`, le
script ne la rallume pas.

Les offsets d envoi, appliques au moment de l envoi et non dans les calculs : salon 1, bureau 3, chambre 3.
Ils corrigent l ecart entre la consigne demandee et ce que la clim affiche, constate en service le
2026-11-10 : salon +1,5, bureau +4,0, chambre +3,6. Un integrateur avait ete tente le meme jour, il s est
emballe parce qu en mode heat la clim ne peut pas refroidir et que l erreur restait negative : l offset fixe
ne s emballe jamais, il a ete prefere.

## 10. Recapitulatif, consigne a 19, balcon ramene a l unite

| Exterieur | Mode | Confort | Nuit | Salon | Bureau | Chambre |
|:--|:--|--:|--:|--:|--:|--:|
| 0 a 7 | heat | 21 | 19 | 21 | 19 | 19 |
| 8 a 18 | heat | 20 | 19 | 20 | 19 | 19 |
| 19 a 25 | off | 20 | 19 | 20 | 19 | 19 |
| 26 a 27 | cool | 26 | 26 | 25 | 26 | 27 |
| 28 a 32 | cool | 26 | 26 | 26 | 27 | 27 |
| 33 | cool | 28 | 26 | 26 | 27 | 27 |
| 34 | cool | 27 | 26 | 26 | 27 | 27 |
| 36 a 40 | cool | 29 a 33 | 26 | 26 | 27 | 27 |

## 11. Les pieges

`temperature_cible` et `temperature_t_conferentielle` n existent plus. Ne pas les reintroduire sans
recabler le calcul.

`temperature_corrige_eric` s appelle `temperature_corrige_bureau` depuis le 2026-11-03.

`delta_3` est declare et n est lu nulle part. Si une formule doit l utiliser, le dire explicitement,
ne pas supposer qu il est deja branche.

La zone off de 19 a 26 degres est morte. Toute la mecanique de paliers n a d effet que sous 8 degres et
au-dela de 32, parce que la plage intermediaire n est jamais appliquee.

Comparer l exterieur a un seuil avec un arrondi deplace la borne d un demi-degre. Le plancher est fidele
pour `< 8`, `< 12` et `>= 34`. Pour la borne `> 32` de l ete il faudrait ecrire `>= 33`, sinon la branche
canicule est atteinte un demi-degre plus tard qu avec la sonde brute. A corriger.

En ete, au-dela de 32 degres exterieur le confort suit la sonde et peut demander 32 a l interieur quand il
en fait 40 dehors. Une clim residentielle refuse generalement au-dela de 30.

Le fichier est critique : toute modification impacte toutes les automations clim. Et HA reecrit
`scripts.yaml` a chaque enregistrement depuis l interface, donc une comparaison de texte brut entre deux
copies ne veut rien dire, il faut comparer le YAML relu.
