# REPRISE SOUFFLANT SALLE DE BAIN - SAISON 2026/2027

**Catégorie :** P1_sdb
**Statut :** spécification validée le 2026-09-28 et déployée en production le même jour (voir section 7)
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
  - `D - SALLE DE BAIN : WATCHDOG SÉCURITÉ RADIATEUR` (éteinte, jamais déclenchée).

### Piège de nommage

Une automation dont l'identifiant d'entité est `bouton_ikea_rodret_soufflant_sdb_gestion_on_off`
pilote en réalité le salon. L'identifiant d'entité a été figé à sa création et n'a jamais suivi
le changement d'alias. Toute lecture rapide de la liste des automatisations donne la salle de bain
pour gérée, ce qui est faux.

## 2. Décisions prises le 2026-09-28

- Base simple pour cette saison, aucune modulation de puissance.
- Marche à 2000 W.
- Verrou de deux minutes après le démarrage, bloquant la marche comme l'arrêt.
- Aucune action automatique sur la température, ni coupure ni modulation.
- Arrêt automatique au bout d'une heure : présent dans le code, neutralisé au départ.
- Alerte mobile en cas de dérive thermique : présente, neutralisée au départ.
- Les deux anciennes automatisations sont conservées telles quelles.

## 3. Séquence cible

### Démarrage

1. La prise s'alimente.
2. Commande de mise en route de l'appareil.
3. Deux impulsions pour atteindre 2000 W.
4. Verrou de deux minutes, marche et arrêt bloqués.

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
| Verrou | `input_boolean.verrou_soufflant_salle_de_bain` | Tient le verrou de deux minutes |
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

---

*Fiche créée le 2026-09-28, déploiement consigné le même jour.*
