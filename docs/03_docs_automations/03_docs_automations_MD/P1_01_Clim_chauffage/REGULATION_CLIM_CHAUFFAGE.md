# Regulation clim et chauffage - deroulement complet

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--14-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-System-ffeb3b?style=flat-square)](.)

</div>

Fiche de reference, relue dans le fichier de production le 2026-11-14. Les valeurs et les formules sont
relevees dans `P1_01_clim_logique_system_autom.yaml`, pas recopiees d une fiche anterieure. Les editions
precedentes annoncaient des capteurs `delta_1` a `delta_7` et des `offset_nuit_*` : ils ont ete supprimes
ou renommes, et cette fiche les decrivait encore.

Deux etages, et il faut les distinguer :

- le template `P1_01_clim_logique_system_autom.yaml` calcule des temperatures
- le script `p1_master_gestion_clim` decide laquelle envoyer a quelle clim, selon la presence et la periode

Le template ne pilote rien. Il produit des nombres. C est le script qui agit.

## 1. Les constantes

| Capteur | Valeur | Role |
|:--|--:|:--|
| `seuil_chauffage` | 19 | seuil de bascule heat vers off, et consigne d hiver |
| `seuil_clim` | 26 | seuil de bascule off vers cool, et consigne d ete |
| `temperature_eco_hiver` | 17 | eco de base en hiver |
| `temperature_eco_ete` | 28 | eco de base en ete |
| `point_tres_froid` | 8 | borne du palier grand froid |
| `point_froid` | 12 | borne du palier froid |
| `point_chaud` | 32 | borne du palier chaleur |
| `point_tres_chaud` | 34 | borne du palier forte chaleur |
| `max_chaud_hiver` | 22 | plafond de piece en hiver, et c est le salon qui l atteint |
| `max_chaud_ete` | 27 | plafond de piece en ete |
| `offset_salon` | 0,3 | bande morte de la derive, salon |
| `offset_bureau` | 0,3 | idem, bureau |
| `offset_chambre` | 0,3 | idem, chambre |
| `correction_temperature_salon` | 1 | decalage retire avant envoi, salon |
| `correction_temperature_bureau` | 3 | idem, bureau |
| `correction_temperature_chambre` | 3 | idem, chambre |

Il n existe plus de capteurs `delta_*`. Les majorations de confort sont ecrites en clair dans la formule :
`consigne + 1` et `consigne + 2`. Un delta declare en capteur pour etre relu avec un repli sur sa propre
valeur n etait qu une valeur en dur avec un capteur de plus.

Le suffixe `nuit` a ete retire des corrections le 2026-11-12 : elles servent aussi au jour, seule la cible
de depart change.

`seuil_chauffage` est a 19. Il peut descendre a 18 pour des raisons d economie, et ce seul chiffre deplace
toute la partie hivernale : la consigne, le confort, la nuit, et la borne basse de la zone off.

## 2. Le mode, calcule par `mode_ete_hiver`

| Exterieur | Mode | Ce qui se passe |
|:--|:--|:--|
| sous 19 | **heat** | chauffage possible |
| de 19 a 26 exclu | **off** | rien, les clims sont arretees |
| a partir de 26 | **cool** | climatisation possible |

Si la sonde du balcon ne repond pas, le capteur rend `unknown` et non `off` : il vaut mieux ne rien
decider qu annoncer a tort une zone morte.

La plage 19 a 26 est morte : sept degres ou aucune consigne n est envoyee.

## 3. La consigne

`consigne` = `seuil_chauffage` en hiver, `seuil_clim` en ete. Donc 19 en hiver, 26 en ete.
En mode off le capteur retombe sur `seuil_chauffage` : la consigne vaut 19 dans la zone morte aussi.

## 4. Le confort, avec un plancher sur la sonde exterieure

`temperature_confort` commence par ramener la sonde du balcon a l entier inferieur :

    {% set t_ext = states('sensor.th_balcon_nord_temperature') | float(0) | round(0, 'floor') %}

**Plancher et non arrondi.** Un arrondi deplace les bornes d un demi-degre : a 7,9 il rend 8, donc la
comparaison `8 < 8` devient fausse et la piece bascule en palier doux alors que la sonde est encore a 7,9.
Un plancher rend 7 et la borne reste juste. Mesure du 2026-11-11 sur 20 releves de nuit : 18 changements
d etat pour la sonde brute, 6 avec le plancher, 1 avec l arrondi, mais l arrondi se trompe de seuil a
chaque bascule.

Attention, cette correction ne couvre que `temperature_confort`. Les capteurs de piece en ete lisent la
sonde brute sans plancher, voir section 5.

En chauffage :

| Exterieur | Confort | Formule |
|:--|--:|:--|
| sous 8 | 21 | consigne + 2 |
| de 8 a 12 exclu | 20 | consigne + 1 |
| au-dessus | 19 | consigne |

Les trois paliers sont distincts depuis le 2026-11-14. La branche du palier doux calculait `consigne + 1`
et donnait 20, si bien que le palier 19 n existait pas et que la maison restait a 20 par temps doux.

En climatisation :

| Exterieur | Confort | Formule |
|:--|--:|:--|
| au-dessus de 34 | exterieur - 7 | exterieur moins 7 |
| de 32 exclu a 34 | exterieur - 5 | exterieur moins 5 |
| jusqu a 32 | 26 | consigne |

Le confort n est pas monotone en ete : 26 a 32, 28 a 33, puis 27 a 34, puis il remonte (29 a 36).
Le decrochement a 34 vient du passage de moins 5 a moins 7.

## 5. Les corrections par piece

| Piece | Hiver | Ete |
|:--|:--|:--|
| Salon | min(confort jour, max_chaud_hiver) + 1 + input jour | min(exterieur - 1, seuil clim) |
| Bureau | (min(confort jour, max_chaud_hiver) - 1) + input jour | min(exterieur, max_chaud ete) |
| Chambre | (min(confort jour, max_chaud_hiver) - 1) + input jour | min(exterieur + 1, max_chaud ete) |

**Le salon prend un degre de plus que le confort, bureau et chambre un degre de moins.** Et ce decalage
s applique APRES le plafonnement, jamais sur le plafond. La formule `min(confort, max_chaud_hiver - 1)`
plafonnait la piece a 21 et donnait 19, 20, 20 : le palier bas et le palier median se confondaient.
`min(confort, max_chaud_hiver) - 1` donne 18, 19, 20 et garde les trois paliers.

Avec la consigne a 19 et `max_chaud_hiver` a 22 :

| Piece | Ext >= 12 | Ext 8 a 12 | Ext < 8 |
|:--|--:|--:|--:|
| Salon | 20 | 21 | 22 |
| Bureau | 18 | 19 | 20 |
| Chambre | 18 | 19 | 20 |

Le salon est la seule piece a pouvoir atteindre 22, et c est voulu : il y a son epouse, la piece est
occupee toute la journee. Le bureau compense par le PC qui tourne, la chambre est la piece la plus froide.

Les trois `input_number` de jour, `clim_consigne_jour_salon`, `_bureau` et `_chambre`, valent 0 par defaut
et vont de -5 a +5 par pas de 0,5. Ce sont les automatisations M, N et O qui y ecrivent -1 pendant dix
minutes quand une piece depasse sa cible.

En ete les pieces ne suivent plus le confort du tout : elles lisent directement la sonde du balcon, et
**sans plancher** puisque le plancher ne s applique qu a l interieur de `temperature_confort`. Une seule
marche, entre 26 et 28 degres dehors.

Depuis le 2026-11-08, `groupe_2`, `groupe_3` et `groupe_4` recoivent tous `tccj_s`, `tccj_b` et `tccj_c`.
La seule exception reste `groupe_1`, qui envoie l eco aux trois.

## 6. Confort jour, confort nuit, et consigne de nuit

`temperature_confort_jour` recopie le confort, sans calcul propre.

`temperature_confort_nuit` a sa propre logique, et ses replis sont volontairement 19 et 26, jamais 0 :
un seuil indisponible a 0 ferait tomber `min()` a zero et enverrait une consigne nulle aux trois clims.

| Saison | Nuit | Formule |
|:--|--:|:--|
| heat | 19 | confort + 1, plafonne par seuil_chauffage |
| cool | 26 | confort, plafonne par seuil_clim |

En hiver la nuit est plate a 19, le plafond ecrase les 20 et 21 du confort. En ete elle est plate a 26.

**Cette nuit n est plus la consigne envoyee.** Le script lit `temperature_consigne_nuit_*`, voir section 8.
`temperature_confort_nuit` alimente encore les captures de nuit et part dans `delta_ademe_recommande`,
ne pas la supprimer.

## 7. Les consignes de nuit et l anti-derive

Dispositif distinct du precedent, actif de 21h00 a 7h30.

Trois capteurs de consigne, un par piece :

    temperature_consigne_nuit_salon = seuil de la saison + input_number.clim_consigne_nuit_salon

Le seuil de la saison vaut 19 en hiver et 26 en ete. L `input_number` vaut 0 par defaut.

Trois capteurs d ecart, un par piece, qui prennent la temperature reelle moins la consigne de nuit :

    ecart_nuit_salon = sensor.th_salon_temperature - temperature_consigne_nuit_salon

Trois capteurs de derive, un par piece, qui appliquent la bonne regle selon la saison :

| Saison | Derive active si | Sens |
|:--|:--|:--|
| heat | ecart > +offset | la piece est trop chaude, on peut baisser |
| cool | ecart < -offset | la piece est trop froide, on peut monter |
| off | jamais | rien a faire |

L offset vaut 0,3 degre. C est une bande morte qui evite qu une piece a 19,05 declenche, puis 19,0 remonte,
en boucle. Sans cette bande un simple dixieme de bruit suffirait a faire osciller le systeme.

**Les automatisations J, K et L ne lisent pas `derive_nuit_*`.** Elles comparent la temperature de la piece,
arrondie au plancher, a `temperature_consigne_nuit_* + offset_*`. C est juste en hiver, ou la derive va
dans le sens du chauffage, et aveugle en ete, ou elle s inverse. Correctif a faire.

## 8. Les corrections de derive

Trois capteurs, un par piece, qui portent le decalage a retirer de la consigne AVANT de l envoyer a la
clim, pour compenser son capteur de reprise d air qui lit sous l ambiance reelle :

| Capteur | Valeur | Justification |
|:--|--:|:--|
| `correction_temperature_salon` | 1 | ecart mesure 1,5, arrondi vers le bas |
| `correction_temperature_bureau` | 3 | ecart mesure 4,0, arrondi vers le bas |
| `correction_temperature_chambre` | 3 | ecart mesure 3,6, arrondi vers le bas |

Mesures du 2026-11-10, sur une seule nuit. Elles sont donc fragiles, et arrondies vers le bas. Un arrondi
vers le bas laisse la piece au-dessus de la cible : c est un choix assume, a reverifier sur plusieurs nuits.

**Cible et consigne envoyee sont deux choses distinctes, et c est le point a ne pas casser.**
`temperature_consigne_nuit_*` et `temperature_corrige_*` sont les CIBLES, celles que lisent J K L,
`ecart_nuit_*` et `derive_nuit_*`. La soustraction se fait dans le script, sur ses variables `tccn_*` et
`tccj_*`, au moment de l envoi. Le 2026-11-12, la soustraction avait ete posee dans le capteur de consigne :
la cible est tombee de 19 a 18 et 16, J K L declenchaient en permanence puisque leur seuil etait devenu
18,3 et 16,3, et le -1 restait colle toute la nuit. Corrige le meme jour a 19h15.

## 9. L eco de saison

L eco a une valeur brute, 17 en hiver et 28 en ete, et une valeur corrigee par la temperature exterieure.

| Saison | Exterieur | Eco brut | Eco corrige |
|:--|:--|--:|--:|
| hiver | sous 8 | 17 | **19** |
| hiver | de 8 a 12 | 17 | **18** |
| hiver | au-dessus de 12 | 17 | **17** |
| ete | sous 28 | 28 | **27** |
| ete | a partir de 28 | 28 | **28** |

L eco d ete retire 1 tant qu il ne fait pas 28 dehors, c est l inverse de l hiver.

L eco s applique de la meme facon en journee et la nuit. Ce n est pas la periode qui le declenche, c est
l absence : le script prend l eco des que le groupe de presence vaut `groupe_1`, et aussi quand un capteur
manque et qu il bascule en mode degrade. Quand une fenetre est ouverte, le script ne calcule pas d eco :
il coupe les trois unites.

## 10. Le script `p1_master_gestion_clim`

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

Et ces variables ne valent pas la cible : le script soustrait la correction au moment de l envoi, au jour
comme a la nuit.

    tccj_s = temperature_corrige_salon  - correction_temperature_salon
    tccn_s = temperature_consigne_nuit_salon - correction_temperature_salon

Donc la clim vise la cible moins la correction, et pendant une derive les automatisations ajoutent le -1
sur dix minutes.

Les variables du script se lisent ainsi : `tcc` pour temperature de consigne de confort, puis `j` ou `n`
pour la periode, jour ou nuit, puis `s`, `b` ou `c` pour la piece. Donc `tccj_s` est la consigne de confort
du jour pour le salon, et `tccn_b` celle de la nuit pour le bureau.

Chaque commande est conditionnee a deux verifications : la prise de la clim doit etre alimentee, et le flag
d arret securise doit etre a off. Si la clim est deja eteinte et que le declencheur est `sensor_update`, le
script ne la rallume pas.

## 11. Les automatisations anti-derive

Six automatisations, toutes sur le meme modele. J, K et L pour la nuit, M, N et O pour le jour.

| Periode | Automatisations | Fenetre | Capteur de consigne | Input ecrit |
|:--|:--|:--|:--|:--|
| nuit | J, K, L | 21h00 a 7h30 | `temperature_consigne_nuit_*` | `clim_consigne_nuit_*` |
| jour | M, N, O | 7h30 a 21h00 | `temperature_corrige_*` | `clim_consigne_jour_*` |

Chacune se declenche sur le changement d etat de la sonde de sa piece, et sur la fin de son timer de
dix minutes. Quand la piece depasse sa cible plus l offset, elle ecrit -1 dans l `input_number` et lance
le timer. A la fin du timer, elle remet 0.

Le jour lit `temperature_corrige_*` et non `temperature_confort_jour` : ce dernier est commun aux trois
pieces et ferait declencher le bureau et la chambre deux degres trop tard, puisque leur cible est un degre
sous celle du salon.

**Une indentation fausse rend l automatisation invisible.** La deuxieme branche du `choose`, celle du
timer, doit etre indentee de quatre espaces pour rester dans le `choose`. A deux espaces elle en sort et
devient un deuxieme element de `actions`, et comme `conditions` n est pas une action, Home Assistant refuse
l automatisation entiere. L entite reste au registre avec seulement `id` et `friendly_name`, donc
`unavailable`, et `check_config` ne dit rien puisque le YAML est syntaxiquement valide. Vecu du 2026-11-12
au 2026-11-14 sur M, N et O.

## 12. Recapitulatif, consigne a 19, balcon ramene a l unite

| Exterieur | Mode | Confort | Nuit | Salon | Bureau | Chambre |
|:--|:--|--:|--:|--:|--:|--:|
| 0 a 7 | heat | 21 | 19 | 22 | 20 | 20 |
| 8 a 18 | heat | 20 | 19 | 21 | 19 | 19 |
| 19 a 25 | off | 19 | 19 | 20 | 18 | 18 |
| 26 a 27 | cool | 26 | 26 | 25 | 26 | 27 |
| 28 a 32 | cool | 26 | 26 | 26 | 27 | 27 |
| 33 | cool | 28 | 26 | 26 | 27 | 27 |
| 34 | cool | 27 | 26 | 26 | 27 | 27 |
| 36 a 40 | cool | 29 a 33 | 26 | 26 | 27 | 27 |

## 13. Les pieges

`temperature_cible` et `temperature_t_conferentielle` n existent plus. Ne pas les reintroduire sans
recabler le calcul.

`temperature_corrige_eric` s appelle `temperature_corrige_bureau` depuis le 2026-11-03.

Les capteurs `delta_1` a `delta_7` ont ete supprimes le 2026-11-13, et les `offset_nuit_*` renommes en
`offset_*` le 2026-11-14. Leurs entites sont restees au registre en `unavailable` : c est du menage a faire
dans Parametres, pas un capteur vivant.

La zone off de 19 a 26 degres est morte. Toute la mecanique de paliers n a d effet que sous 8 degres et
au-dela de 32, parce que la plage intermediaire n est jamais appliquee.

Comparer l exterieur a un seuil avec un arrondi deplace la borne d un demi-degre. Le plancher est fidele
pour `< 8`, `< 12` et `>= 34`. Pour la borne `> 32` de l ete il faudrait ecrire `>= 33`, sinon la branche
canicule est atteinte un demi-degre plus tard qu avec la sonde brute. A corriger.

En ete, au-dela de 32 degres exterieur le confort suit la sonde et peut demander 32 a l interieur quand il
en fait 40 dehors. Une clim residentielle refuse generalement au-dela de 30.

Le `unique_id` ne donne pas l `entity_id`. Le bloc porte `unique_id: max_chaud_hiver` et l entite peut
s appeler autrement si le registre a garde un ancien nom. Une formule qui ecrit un nom inexistant ne leve
rien : elle retombe sur son `float()` de repli. Verifier avec l API des etats avant de conclure.

Un `.bak` depose dans `H:/templates` est charge comme un template. `!include_dir_merge_list templates/`
prend tous les `.yaml`, et un nom `...autom.bak_2026_11_13_20h_32m_33s.yaml` finit par `.yaml`. Vecu le
2026-11-13 : trois definitions du meme `unique_id` se chargeaient, la derniere gagnait, et un capteur
restait fige sur une ancienne valeur alors que la formule rendait la bonne.

Le fichier est critique : toute modification impacte toutes les automations clim. Et HA reecrit
`scripts.yaml` a chaque enregistrement depuis l interface, donc une comparaison de texte brut entre deux
copies ne veut rien dire, il faut comparer le YAML relu.
