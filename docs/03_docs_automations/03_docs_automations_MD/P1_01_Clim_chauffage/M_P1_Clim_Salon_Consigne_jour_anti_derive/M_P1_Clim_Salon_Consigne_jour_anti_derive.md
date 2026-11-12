# (M) CONSIGNE JOUR ANTI-DERIVE SALON

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--12-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-4fc3f7?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_01_Clim_chauffage/M_P1_Clim_SALON_Consigne_jour_anti_derive/M_P1_Clim_SALON_Consigne_jour_anti_derive.yaml`
> **Mode HA :** `single`
> **Identifiant :** `1794417183991`

---

## 📝 Description

Pendant de jour de l automatisation de nuit. La clim mesure sur son retour d air et chauffe au-dela de
la consigne demandee. Plutot que de lui envoyer une consigne fausse en permanence, cette automation la
fait taire pendant 10 minutes quand la piece depasse vraiment sa cible de jour.

Quand `sensor.th_salon_temperature` arrondi au plancher depasse `sensor.temperature_corrige_salon` plus
`sensor.offset_nuit_salon`, entre 7h30 et 21h et hors `groupe_1`, elle ecrit `-1` dans
`input_number.clim_consigne_jour_salon` et demarre `timer.clim_consigne_jour_salon_10mn`. A la fin du
timer, elle remet `0`.

---

## ⚡ Déclencheurs

| Type | Entité | Événement |
|:---|:---|:---|
| `state` | `sensor.th_salon_temperature` | tout changement de température |
| `event` | `timer.finished` sur `timer.clim_consigne_jour_salon_10mn` | fin du décompte |

---

## ⚙️ Actions

Si le déclencheur est `mesure`, qu on est entre 7h30 et 21h, que le groupe n est pas `groupe_1` et que
la pièce dépasse sa cible plus l offset : elle écrit `-1` dans l `input_number`, puis démarre le timer
de 10 minutes.

Si le déclencheur est `fin_timer` : elle remet `0`, la cible repasse à sa valeur de journée.

---

## 🔗 Dépendances

| Sens | Objet |
|:---|:---|
| Lit | `sensor.th_salon_temperature` |
| Lit | `sensor.temperature_corrige_salon` |
| Lit | `sensor.offset_nuit_salon` |
| Lit | `sensor.groupe` |
| Écrit | `input_number.clim_consigne_jour_salon` (-1 puis 0) |
| Écrit | `timer.clim_consigne_jour_salon_10mn` |
| Aval | script `p1_master_gestion_clim`, qui envoie `temperature_corrige_salon` à `climate.clim_salon_rm4_mini` |

---

## ⚠️ Pièges

- **La cible vient de `temperature_corrige_salon`, pas de `temperature_confort_jour`.** Le confort jour
  est global, 21 sous 8 degrés et 20 au-dela. `temperature_corrige_salon` est deja plafonnee par piece,
  c est elle qui porte la vraie cible.
- **`groupe_1` est exclu.** En absence c est l eco de saison qui s applique, et le `-1` n a plus de sens.
- L offset de 0,3 est une bande morte, pas une température visée : sans elle la pièce oscillerait entre
  la cible plus 0,05 et la cible, et redéclencherait toutes les dix minutes.
- Le déclencheur `state` ne se réveille que si la valeur **change**. Une pièce stable ne redéclenche pas,
  c est voulu : le timer fait le retour.
- Si la fin du timer tombe pendant un arrêt de HA, `timer.finished` n est pas émis au redémarrage. La
  consigne resterait à `-1` jusqu au prochain changement de température.
- **Etat au 2026-11-12 : `unavailable`.** L automation est ecrite, `config_check` l accepte et l API la
  connait, mais elle ne se charge pas. Deux rechargements sans effet, piste du redemarrage complet non
  testee.
