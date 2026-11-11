# (K) CONSIGNE NUIT ANTI-DERIVE BUREAU

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--11-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-4fc3f7?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_01_Clim_chauffage/K_P1_Clim_Bureau_Consigne_nuit_anti_derive/`
> **Mode HA :** `single`

---

## 📝 Description

Corrige la derive de la clim de bureau la nuit. La clim mesure sur son retour d air et
chauffe au-dela de la consigne demandee. Plutt que d envoyer une consigne fausse en permanence,
cette automation fait taire la clim pendant 10 minutes quand la piece depasse vraiment la cible.

Quand `sensor.th_bureau_temperature` depasse `input_number.clim_consigne_nuit_bureau` plus
`sensor.offset_nuit_bureau` pendant la plage 21h a 7h30, elle met la consigne a 18 et
demarre `timer.clim_consigne_nuit_bureau_10mn`. A la fin du timer, elle remet 19.

---

## ⚡ Déclencheurs

| Type | Entité | Événement |
|:---|:---|:---|
| `state` | `sensor.th_bureau_temperature` | tout changement de température |
| `event` | `timer.finished` sur `timer.clim_consigne_nuit_bureau_10mn` | fin du décompte |

---

## ⚙️ Actions

Si le déclencheur est `mesure` et qu'on est entre 21h et 7h30 et que la pièce dépasse la consigne
plus l'offset : consigne à 18, puis démarrage du timer de 10 minutes.

Si le déclencheur est `fin_timer` : consigne remise à 19.

---

## 🔗 Dépendances

| Sens | Objet |
|:---|:---|
| Lit | `sensor.th_bureau_temperature` |
| Lit | `input_number.clim_consigne_nuit_bureau` |
| Lit | `sensor.offset_nuit_bureau` |
| Écrit | `input_number.clim_consigne_nuit_bureau` |
| Écrit | `timer.clim_consigne_nuit_bureau_10mn` |
| Aval | script `p1_master_gestion_clim`, qui envoie cette consigne à `climate.clim_bureau_rm4_mini` |

---

## ⚠️ Pièges

- L'offset de 0,3 est une bande morte, pas une température visée : sans elle la pièce oscillerait
  entre 19,05 et 19,0 et redéclencherait toutes les dix minutes.
- Le déclencheur `state` ne se réveille que si la valeur **change**. Une pièce stable à 21 avec une
  consigne à 18 ne redéclenche pas, ce qui est voulu : le timer fait le retour.
- Si la fin du timer tombe pendant un arrêt de HA, `timer.finished` n'est pas émis au redémarrage.
  La consigne resterait à 18 jusqu'au prochain changement de température.
- Cette automation ne fonctionne que si le script lit les `input_number` en période nuit. Tant qu'il
  envoie `temperature_confort_nuit`, elle tourne à vide.
