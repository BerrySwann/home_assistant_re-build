# TarifElecInfo - prix du contrat HP/HC et alertes avant changement

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--04-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-System-ffeb3b?style=flat-square)](.)

</div>

> **Domaine :** `tarifelecinfo`
> **Version installee :** 0.1.0 (`manifest.json`)
> **Emplacement prod :** `/config/custom_components/tarifelecinfo/`
> **Depot :** `https://github.com/BerrySwann/tarif-elec-info` (public)
> **Type :** integration personnelle, en `custom_components`, avec parcours de configuration
> **Classe IoT :** `cloud_polling` - dependance `pymupdf>=1.24.0`
> **Entree de configuration :** une seule, creee par l'interface

---

## Description

Lit les prix du tarif reglemente, les expose sous forme de capteurs, et previent avant chaque
changement de grille. Elle remplace l'integration `tarif_edf`, dont le depot HACS avait disparu
(404) et qui ne pouvait donc plus etre mise a jour.

Deux interets par rapport a l'ancienne : elle donne le **prochain changement** et le nombre de
**jours restants**, et son code est publie, donc maintenable.

## Les huit capteurs

| Entite | Role |
|:---|:---|
| `sensor.tarifelecinfo_tarif_heures_pleines` | Prix du kWh en heures pleines |
| `sensor.tarifelecinfo_tarif_heures_creuses` | Prix du kWh en heures creuses |
| `sensor.tarifelecinfo_abonnement_mensuel` | Part fixe mensuelle de l'abonnement |
| `sensor.tarifelecinfo_source_des_prix` | D'ou viennent les prix lus (grille publique, fichier de contrat) |
| `sensor.tarifelecinfo_puissance_souscrite` | Puissance du contrat, en kVA |
| `sensor.tarifelecinfo_option_tarifaire` | Option du contrat (HP/HC, Base, Tempo) |
| `sensor.tarifelecinfo_prochain_changement` | Date d'effet de la prochaine grille |
| `sensor.tarifelecinfo_jours_avant_changement` | Nombre de jours restants avant cette date |

**Aucun prix n'est ecrit dans les documents du projet.** Les montants se lisent sur ces capteurs :
ils changent au 1er fevrier et au 1er aout, et une valeur recopiee dans une fiche serait fausse a la
premiere echeance sans que rien ne le signale.

## D'ou viennent les prix

Trois sources publiques, dans cet ordre de preference :

1. **la grille de prix du fournisseur (PDF)** - prix TTC, les seuls qui correspondent a ce qui est
   paye. Lecture par position avec `pymupdf`.
2. **le fichier de contrat public (CSV)** sur data.gouv - utilise si `pymupdf` est absent.
3. **la deliberation de la CRE** - reference des tarifs reglementes.

Le capteur `source_des_prix` dit laquelle a servi. Si les prix affiches paraissent anciens, c'est le
premier endroit a regarder.

## Options de configuration

| Option | Role | Defaut |
|:---|:---|:---|
| `contrat` | Type de contrat (HP/HC, Base) | choisi a l'installation |
| `puissance` | Puissance souscrite, en kVA | choisi a l'installation |
| `notify_service` | Service de notification utilise pour les alertes | choisi a l'installation |
| `jours_avant` | Combien de jours avant l'echeance la premiere alerte part | 9 |
| `heure_veille` | Heure de l'alerte de rappel, la veille | 20 |

## Les deux alertes

1. **J-9** (reglable) : premiere annonce du changement a venir, une fois par echeance.
2. **la veille au soir** (20 h par defaut) : rappel « ce soir minuit », une fois par echeance.

Chacune n'est envoyee qu'une seule fois : l'etat est memorise par echeance, ce qui evite un rappel
quotidien. Le service de notification est celui choisi a l'installation.

> **Non verifie a ce jour** : les deux alertes n'ont pas encore ete observees sur un vrai changement
> de grille. Le point `R40.10` de la TODO suit cette verification et court jusqu'au 1er fevrier 2027.

## Ce qu'elle remplace

| Avant (`tarif_edf`) | Apres (`tarifelecinfo`) |
|:---|:---|
| `sensor.tarif_heures_pleines_ttc` | `sensor.tarifelecinfo_tarif_heures_pleines` |
| `sensor.tarif_heures_creuses_ttc` | `sensor.tarifelecinfo_tarif_heures_creuses` |
| `sensor.puissance_souscrite_hphc_6kva` | `sensor.tarifelecinfo_puissance_souscrite` |

La bascule a ete faite le 2026-11-04, apres verification que les deux jeux de capteurs donnaient le
meme resultat. `tarif_edf` a ete retiree le meme jour : entree de configuration et dossier
`custom_components` supprimes.

Les capteurs **TEMPO** (`sensor.edf_tempo_price_*`) n'ont jamais dependu de `tarif_edf` : ils
viennent de MyElectricalData, en `platform: mqtt`.

## Points d'attention

- **La lecture du PDF est fragile par nature.** Elle se fait par position dans la page : si le
  fournisseur change la mise en page de sa grille, la lecture peut rendre un prix faux **sans lever
  d'erreur**. Le capteur `source_des_prix` et la valeur elle-meme sont les deux choses a regarder
  apres chaque changement de tarif.
- **Le prix ne change pas tout seul au bon moment** : l'integration interroge les sources, elle ne
  connait pas les dates d'effet par avance. Un prix faux reste faux jusqu'a la lecture suivante.
- **Dependance `pymupdf`** : sans elle, l'integration retombe sur le CSV de data.gouv, ce que
  `source_des_prix` signale.
- **Ne jamais ecrire un prix en dur dans un document.** Trois fichiers de la prod lisent ces
  capteurs (le calcul de cout de l'automation Histo Nodon, et les deux templates P0) : une valeur
  recopiee ailleurs serait la premiere a mentir.

## Changelog

| Date | Version | Modification |
|:---|:---|:---|
| 2026-11-04 | 0.1.0 | `tarif_edf` retiree ; les trois fichiers de la prod qui la lisaient passent sur cette integration, a resultat identique. Fiche creee. |
| 2026-11-01 | 0.1.0 | Installation : parcours en trois ecrans, huit capteurs, prix lus sur la grille publique. |
