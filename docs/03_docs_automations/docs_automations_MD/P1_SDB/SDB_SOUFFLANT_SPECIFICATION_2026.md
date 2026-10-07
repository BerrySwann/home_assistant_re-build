# REPRISE SOUFFLANT SALLE DE BAIN - SAISON 2026/2027

**Catégorie :** P1_sdb
**Statut :** spécification validée le 2026-09-28 et déployée en production le même jour (voir section 7)
**Mise à jour :** 2026-09-29, sécurités ajoutées et cycle réel validé (voir section 8)
**Ancienne fiche conservée :** `A_SOUFFLANT_SDB_old_2024-2025.md`

## 1. État des lieux relevé le 2026-09-28

- Appareil piloté en infrarouge par `remote.soufflant_sdb`.
- Alimentation par la prise mesurante `switch.prise_soufflant_salle_de_bain_nous`.
- Thermostat de pièce : `sensor.th_salle_de_bain_temperature`.
- Entrée actuelle : interrupteur virtuel `input_boolean.inter_soufflant_salle_de_bain`, doublé de
  l'interrupteur calculé `switch.inter_soufflant_salle_de_bain` (bouton du tableau de bord).
- Compteur d'état logiciel : `input_select.etat_resistance_soufflant_sdb` (actuellement `0W`).
- Consommation cumulée relevée : 187,53 kWh.
- Le bouton IKEA Rodret de la salle de bain existe et répond (batterie 100), mais aucun
  automatisme de la maison ne le capte. Source de l'appui à trancher.
- Deux anciennes automatisations, toutes deux éteintes, conservées comme réservoir d'idées :
  - `A - 2026/02/01 - SALLE DE BAIN - GESTION INTELLIGENTE SOUFFLANT` (éteinte depuis le 2026-05-27),
    régulation par paliers de 1000 et 2000 W ;
  - `D - SALLE DE BAIN : WATCHDOG SÉCURITÉ RADIATEUR` (réactivée le 2026-09-29, active, jamais déclenchée à ce jour).

### Piège de nommage

Une automation dont l'identifiant d'entité est `bouton_ikea_rodret_soufflant_sdb_gestion_on_off`
pilote en réalité le salon. L'identifiant d'entité a été figé à sa création et n'a jamais suivi
le changement d'alias. Toute lecture rapide de la liste des automatisations donne la salle de bain
pour gérée, ce qui est faux.

## 2. Décisions prises le 2026-09-28

- Base simple pour cette saison, aucune modulation de puissance.
- Marche à 2000 W.
- Verrou de trente secondes après le démarrage, bloquant la marche comme l'arrêt.
- Aucune action automatique sur la température, ni coupure ni modulation.
- Arrêt automatique au bout d'une heure : présent dans le code, neutralisé au départ.
- Alerte mobile en cas de dérive thermique : présente, neutralisée au départ.
- Les deux anciennes automatisations sont conservées telles quelles.

## 3. Séquence cible

### Démarrage

1. La prise s'alimente.
2. Commande de mise en route de l'appareil.
3. Deux impulsions pour atteindre 2000 W.
4. Verrou de trente secondes, marche et arrêt bloqués.

### Arrêt

1. Commande de coupure des deux résistances ; le ventilateur continue de tourner pour les refroidir.
2. Attente d'une minute trente.
3. Coupure de la prise, afin de ne pas payer les 4 W de veille.

## 4. Observation pour l'analyse de fin de saison

La température de la pièce et la puissance de la prise sont déjà enregistrées par la base
MariaDB, avec une purge à trente jours. L'analyse devra donc être faite dans le mois qui suit
la saison, pas au printemps.

Point à mesurer : si la puissance tombe à zéro alors qu'aucun ordre n'a été donné, l'appareil
s'est coupé de lui-même. La température de la pièce à cet instant donne sa température de
coupure réelle.

## 5. Point de sécurité à assumer

Avec l'arrêt automatique d'une heure et l'alerte mobile neutralisés au départ, et aucune coupure
sur température, aucun filet n'est actif. Un soufflant de 2000 W allumé par distraction
tournerait sans fin. Les deux interrupteurs seront en place, il suffira de les basculer.

## 6. Reste à faire

- [x] Trancher la source de l'appui : les deux. Le bouton IKEA Rodret commande l'interrupteur
      virtuel du tableau de bord, qui reste l'entrée unique.
- [x] Écrire les automatisations et les scripts.
- [x] Déployer.
- [ ] Tester en réel et vérifier les paliers de puissance sur la prise (0 W, environ 40 W, 1000 W, 2000 W).
- [ ] Consigner la température de coupure observée.

## 7. Ce qui est déployé le 2026-09-28

| Élément | Entité | Rôle |
|:--|:--|:--|
| Verrou | `input_boolean.verrou_soufflant_salle_de_bain` | Tient le verrou de trente secondes |
| Script | `script.sdb_soufflant_demarrer` | Prise, mise en route, 2000 W, verrou |
| Script | `script.sdb_soufflant_arreter` | Résistances, ventilateur 1 min 30, prise |
| Automation | SDB - SOUFFLANT - ROUTAGE | Interrupteur virtuel vers les séquences |
| Automation | SDB - SOUFFLANT - BOUTON IKEA RODRET | Appui du bouton vers l'interrupteur virtuel |

Chaîne complète : bouton IKEA Rodret (MQTT) ou bouton du tableau de bord, puis interrupteur
virtuel `switch.inter_soufflant_salle_de_bain`, puis automation de routage, puis script de
démarrage ou d'arrêt, puis infrarouge `remote.soufflant_sdb` et prise
`switch.prise_soufflant_salle_de_bain_nous`.

Déploiement : ajout dans `automations.yaml`, `scripts.yaml` et le fichier d'interrupteurs
virtuels, puis rechargement des trois domaines. Aucun redémarrage de Home Assistant.

Exports : `docs_automations_YAML/P1_sdb/h_soufflant_sdb_routage.yaml` et
`i_soufflant_sdb_bouton_rodret.yaml`, `docs_scripts_YAML/sdb_soufflant_demarrer.yaml` et
`sdb_soufflant_arreter.yaml`.

Le piège de nommage reste en place : l'automation dont l'identifiant parle de soufflant salle
de bain (`bouton_ikea_rodret_soufflant_sdb_gestion_on_off_json`) pilote toujours le salon.

## 8. Mise à jour du 2026-09-29

### 8.1 Sécurités ajoutées dans les scripts

| Ajout | Où | Effet |
|:--|:--|:--|
| Garde de saison | `sdb_soufflant_demarrer`, première ligne de la séquence | Refus de démarrer si `sensor.mode_ete_hiver` vaut cool (modifié le 2026-10-07). Elle remplace la garde des 25 degrés du 2026-09-29, qui aurait bloqué les démarrages en hiver. Placée avant le verrou, la prise et l'infrarouge. |
| Affichage du climate | `sdb_soufflant_demarrer` après les impulsions, `sdb_soufflant_arreter` en fin de séquence | Le climate passe en heat au démarrage et sur off à l'arrêt, comme le faisait l'automation de février. |
| Arrêt forcé 60 minutes | `sdb_soufflant_demarrer`, fin de séquence | Si l'interrupteur est encore en marche après une heure, il est éteint et la séquence d'arrêt enchaîne. Le compte démarre à la fin du verrou, l'arrêt tombe donc environ 60 minutes 30 secondes après l'appui. |

La garde de saison doit rester la première ligne. Placée plus bas, un refus laissait le verrou
posé et bloquait toute commande d'arrêt, ce qui s'est produit lors des essais du 2026-09-29. Mise à jour 2026-10-07 : décision d'Eric, le verrou passe de 2 minutes à 30 secondes. Son rôle est d'éviter un arrêt prématuré, par exemple un appui sur on suivi d'un appui sur off sans le vouloir. Un off pendant le verrou n'est pas annulé : le script le traite à la fin du verrou, et un nouvel appui sur on dans les 30 secondes le rattrape (déduit de la séquence, pas testé).

### 8.2 Cycle réel validé

Appui sur le bouton Rodret le 2026-09-29 à 17 h 46 : interrupteur en marche, séquence de démarrage,
prise alimentée, appareil en chauffe. Appui à 17 h 48 : interrupteur remis sur arrêt, arrêt refusé
pendant le verrou, puis séquence d'arrêt. Le compteur d'énergie est passé de 187,55 à 187,77 kWh,
soit environ 2 kW pendant trois minutes. Le cycle décrit en section 3 est donc conforme.

### 8.3 Mesure de puissance de la prise : diagnostic clos

La puissance et le courant de `switch.prise_soufflant_salle_de_bain_nous` restaient à zéro alors que
le compteur d'énergie montait. Après réapplication de la configuration depuis l'interface Zigbee2MQTT
le 2026-09-29 à 17 h 29, la prise publie de nouveau ses rapports : 1645 W relevés en pleine chauffe.
Les capteurs `sensor.sdb_soufflant_etat` et `sensor.sdb_soufflant_power_status` restent néanmoins
calculés sur cette puissance avec un seuil de 20 W : une prise muette les fige sur éteint, et ils ne
suivent donc pas le bouton.

### 8.4 Thermostat de la salle de bain

`climate.soufflant_salle_de_bain` est un `generic_thermostat` dont le chauffage est
`switch.inter_soufflant_salle_de_bain`, c'est-à-dire l'interrupteur du montage lui-même. Consigne
portée de 21 à 32 degrés le 2026-09-29, bornes réglées entre 21 et 32. Conséquences vérifiées : à
consigne plus basse que la température de la pièce, le passage en heat coupe l'interrupteur dans la
seconde et interrompt la séquence ; à consigne plus haute, il laisse chauffer mais rallume
l'interrupteur tout seul dès qu'il le trouve éteint, et il coupe à la consigne plus la tolérance. Ce
thermostat commande donc réellement le montage, il n'est pas un simple affichage. Deux voies restent
ouvertes : le laisser ainsi, ou lui retirer l'interrupteur pour qu'il devienne un voyant.

Mise à jour 2026-10-07 : décision d'Eric, le thermostat devient un voyant. Il a été recréé dans
l'interface (tolérances 0, bornes 19 à 32), puis son chauffage a été remplacé par
`switch.voyant_thermostat_soufflant_salle_de_bain`, un switch template neutre qui suit
`input_boolean.voyant_thermostat_soufflant_salle_de_bain` et ne commande aucun matériel. Le thermostat
ne peut donc plus couper ni rallumer le soufflant. Contrepartie : il n'y a plus de coupure en
température par le thermostat (elle tombait à la consigne, 32 degrés au plus). Restent l'arrêt forcé
à 60 minutes et la watchdog D. Les deux nouvelles entités sont déclarées dans `input_booleans/P1/
P1_BV_IB_inter_soufflant_sdb.yaml` et `templates/Inter_BP_Virtuel/P1/P1_BV_IB_SW_inter_souflant_sdb.yaml`.

### 8.5 Watchdog : remis en service mais inopérant

`D - SALLE DE BAIN : WATCHDOG SÉCURITÉ RADIATEUR` a été réactivée le 2026-09-29. Elle est
correctement câblée, mais elle n'a jamais déclenché : son compteur d'exécutions est à zéro. Sa
quatrième condition exige une hausse de 0,5 degré entre deux mesures consécutives, alors que le
capteur de la salle de bain remonte par pas de 0,2 (25,5 puis 25,7 puis 25,9 puis 26,1). La
condition est donc infaisable en pratique. Depuis que le script refuse de démarrer au-dessus de
25 degrés, cette condition de dérive est devenue inutile : les trois autres suffisent.

Mise à jour 2026-10-07 : Eric a passé le seuil de dérive à 0,4 degré (relu en direct). Efficacité
non démontrée (relevés par pas de 0,2) et risque de double IR `on_off` entre D et le script d'arrêt
non testé : voir `D_WATCHDOG_RADIATEUR_SDB.md`, section "État au 2026-10-07".

### 8.6 Points ouverts au 2026-09-29

- Quand le script refuse un démarrage, l'interrupteur reste en marche sans effet : rien ne le remet
  sur arrêt, et le tableau de bord affiche un appareil en marche qui ne chauffe pas.
- Le compte d'une heure vit dans le script : un redémarrage de Home Assistant pendant la marche
  l'efface. L'automation de février, elle, se réarmait seule après un redémarrage.
- Aucune des trois sécurités n'a été observée en fonctionnement réel.
- Depuis le 2026-10-07 la garde de saison ne regarde plus la température de la pièce : un démarrage reste possible au-dessus de 25 degrés hors mode cool.
- Les capteurs `sdb_soufflant_etat` et `sdb_soufflant_power_status` restent faux quand la prise ne
  publie pas sa puissance : mieux vaudrait les calculer sur l'interrupteur.

---

*Fiche créée le 2026-09-28, déploiement consigné le même jour. Mise à jour du 2026-09-29.*
