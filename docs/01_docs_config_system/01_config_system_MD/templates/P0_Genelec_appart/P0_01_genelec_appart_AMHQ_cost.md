# P0_01_Genelec_appart_AMHQ_cost - Coûts HP/HC et total de l'appartement

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

> **Fichier :** `P0_01_genelec_appart_AMHQ_cost.yaml`
> **Emplacement prod :** `/config/templates/P0_energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml`
> **Emplacement local :** `docs/01_docs_config_system/01_config_system_SH_PY_YAML/templates/P0_energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml`
> **Empreinte relevée le 2026-11-04 :** MD5 `f9eb6133`, 17803 octets, copie locale identique à la prod
> **Inclus par :** `configuration.yaml` (`template: !include_dir_merge_list templates/`)
> **Dernière modification :** 2026-11-04 (changement d'intégration de tarifs)

---

## Description

Douze capteurs template calculant le coût en euros de la consommation de l'appartement, en heures
pleines, en heures creuses et au total, sur quatre périodes : quotidien, hebdomadaire, mensuel et
annuel. Le découpage HP/HC vient des compteurs `utility_meter` à paliers, pas de ce fichier.

Les douze entités produites :

| Période | HP | HC | Total |
|:---|:---|:---|:---|
| Quotidien | `sensor.genelec_appart_cout_hp_quotidien` | `_hc_quotidien` | `_total_quotidien` |
| Hebdomadaire | `sensor.genelec_appart_cout_hp_hebdomadaire` | `_hc_hebdomadaire` | `_total_hebdomadaire` |
| Mensuel | `sensor.genelec_appart_cout_hp_mensuel` | `_hc_mensuel` | `_total_mensuel` |
| Annuel | `sensor.genelec_appart_cout_hp_annuel` | `_hc_annuel` | `_total_annuel` |

## Sources et formule

```
cout_hp    = (kWh heures pleines de la periode) x prix HP
cout_hc    = (kWh heures creuses de la periode) x prix HC
cout_total = cout_hp + cout_hc
```

Les kWh viennent de `sensor.genelec_appart_hphc_[periode]_um_hp` et `_um_hc`, alimentés par
`sensor.genelec_appart_totale_kwh` (intégration Riemann) puis par les `utility_meter`.

**Les prix ne sont jamais écrits dans ce fichier.** Ils sont lus sur les capteurs de l'intégration
`tarifelecinfo` : `sensor.tarifelecinfo_tarif_heures_pleines` et
`sensor.tarifelecinfo_tarif_heures_creuses`. Ils changent au 1er février et au 1er août, et le
document n'a donc pas à être modifié à ces dates.

## Chaîne de dépendances

```
NODON (prise appartement) -> sensor.general_electric_appart_*
   -> intégration Riemann -> sensor.genelec_appart_totale_kwh
      -> utility_meter (paliers HP/HC) -> sensor.genelec_appart_hphc_*_um_hp / _um_hc
         -> CE FICHIER + capteurs tarifelecinfo -> sensor.genelec_appart_cout_*
            -> page L2C1 (Energie générale)
```

## Changement d'intégration : tarif_edf -> TarifElecInfo (2026-11-04)

**Pourquoi.** L'intégration `tarif_edf` venait d'un dépôt HACS supprimé (404 sur GitHub), sans
aucune mise à jour possible ; elle avait été réinstallée à la main en 2.0.1. L'intégration
personnelle `tarifelecinfo`, installée le 2026-11-01, la remplace : mêmes prix du contrat, plus le
prochain changement de tarif et le nombre de jours restants, et elle est publiable au lieu de
dépendre d'un dépôt mort.

**Correspondance des capteurs** :

| Avant (`tarif_edf`) | Après (`tarifelecinfo`) |
|:---|:---|
| `sensor.tarif_heures_pleines_ttc` | `sensor.tarifelecinfo_tarif_heures_pleines` |
| `sensor.tarif_heures_creuses_ttc` | `sensor.tarifelecinfo_tarif_heures_creuses` |
| `sensor.puissance_souscrite_hphc_6kva` | `sensor.tarifelecinfo_puissance_souscrite` |

**Ce qui change dans ce fichier** : les trente-six références aux capteurs de tarif. La formule,
les périodes et les arrondis ne bougent pas : seul le nom de la source change.

**Preuve que la bascule est neutre** : le calcul de coût rejoué par l'API `/api/template` rend le
même résultat avec les anciens capteurs et avec les nouveaux. Aucun prix n'est écrit en dur ici.

**Ce qui a été retiré le 2026-11-04** : l'entrée de configuration `tarif_edf` et le dossier
`H:/custom_components/tarif_edf`. Les trois anciens capteurs ont disparu des états.

**Ce qui n'est pas concerné** : les capteurs TEMPO (`sensor.edf_tempo_price_blue_hp`, `_hc`,
`_white_*`, `_red_*`) viennent de MyElectricalData, en `platform: mqtt`. Ils n'ont jamais dépendu de
`tarif_edf` et ne sont pas touchés.

## Points d'attention

- **Aucun prix en dur.** Si un prix était écrit dans le fichier, il deviendrait faux au premier
  février ou au premier août sans que rien ne le signale. Les montants se lisent sur les capteurs.
- **Un capteur de tarif absent ne casse pas le calcul, il le fausse.** Les templates utilisent
  `| float(valeur)`, donc une source `unknown` ou supprimée produit un coût faux, jamais une erreur
  visible. C'est pour cette raison que la migration a été vérifiée avant le retrait de l'ancienne
  intégration.
- **Les entités dérivées servent de sonde.** Les douze `sensor.genelec_appart_cout_*` sont le
  meilleur témoin d'une panne de tarif : leur valeur ne doit pas tomber à zéro d'un coup.
- **Arrondis** : `round(3)` pour les montants HP et HC individuels, `round(2)` pour le total.

## Changelog

| Date | Modification |
|:---|:---|
| 2026-11-04 | Changement d'intégration : les capteurs de tarif passent de `tarif_edf` à `tarifelecinfo`, à valeur identique. Les prix en dur sont retirés des commentaires, la ligne historique du 2026-04-26 est conservée telle quelle. |
| 2026-04-26 | Le calcul du coût passe des tarifs Tempo (`sensor.edf_tempo_price_blue_hp` / `_hc`, alors inconnus) aux capteurs HP/HC du contrat. |
| — | Refonte : remplacement du calcul approximatif (un seul tarif HP) par un vrai découpage HP/HC, et ajout de huit capteurs individuels. |
