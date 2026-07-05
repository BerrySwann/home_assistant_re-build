# (A-0) AUTOMATISATION CLIM JOUR (07H30 ↔ 21H00)

> **Fichier TREE_CORRIGE :** `docs_automations/TREE_CORRIGE/P1_clim_chauffage/a_0_2026_01_11_automatisation_clim_jour_07h30_21h00.yaml`
> **Mode HA :** `queued` — max: 5
> **Dernière mise à jour :** 2026-06-28 (refactoring LLM local → délégation script)

---

## 📝 Description

Automation wrapper diurne (07h30–21h00). Surveille tous les événements pertinents
et délègue **intégralement** la logique à `script.p1_master_gestion_clim` avec
`periode: "jour"`. Plus de logique inline — tout est centralisé dans le script.

---

## ⚡ Déclencheurs

| ID trigger | Type | Entité / Horaire |
|:---|:---|:---|
| `ha_restart` | `homeassistant` | Démarrage HA |
| `force_run` | `time` | 07:30:00 |
| `force_run` | `state` | `sensor.mamour_network_type`, `sensor.eric_network_type` |
| `force_run` | `state` | `switch.clim_salon_nous`, `switch.clim_bureau_nous`, `switch.clim_chambre_nous` |
| `window_open` | `state` | 4 capteurs fenêtres → `off` → `on` |
| `window_close` | `state` | 4 capteurs fenêtres → `on` → `off` |
| `sensor_update` | `state` | `sensor.groupe` *(ajouté)*, `sensor.th_balcon_nord_temperature`, `sensor.temperature_cible`, `sensor.mode_ete_hiver`, `sensor.temperature_confort_jour` |

> ⚠️ `sensor.groupe` a été **ajouté** au trigger `sensor_update` lors du refactoring (2026-06).
> L'ancienne version ne déclenchait pas sur un changement de présence direct.

---

## 🔒 Conditions globales

- Plage horaire : `after 07:30 before 21:00`

---

## ⚙️ Actions

Une seule action :

```yaml
- action: script.p1_master_gestion_clim
  data:
    periode: "jour"
    trigger_id: "{{ trigger.id if trigger is defined else '' }}"
    trigger_entity_id: "{{ trigger.entity_id if trigger is defined ... else '' }}"
```

→ Toute la logique est dans `script.p1_master_gestion_clim` — voir `docs_scripts/docs/P1_MASTER_GESTION_CLIM.md`

---

## 🔌 DÉPENDANCES

### Entités lues (triggers / conditions)

| Entité | Rôle |
|:---|:---|
| `sensor.mamour_network_type` | Présence réseau Mamour |
| `sensor.eric_network_type` | Présence réseau Eric |
| `sensor.groupe` | Groupe de présence (trigger sensor_update) |
| `sensor.th_balcon_nord_temperature` | T° extérieure |
| `sensor.temperature_cible` | T° cible calculée |
| `sensor.mode_ete_hiver` | Mode saison |
| `sensor.temperature_confort_jour` | T° confort jour |
| 4× `binary_sensor.contact_fenetre_*` | Capteurs fenêtres |
| 3× `switch.clim_*_nous` | Prises clim (sécurité) |

### Script appelé

| Script | Paramètres | Doc |
|:---|:---|:---|
| `script.p1_master_gestion_clim` | `periode:"jour"`, `trigger_id`, `trigger_entity_id` | `docs_scripts/docs/P1_MASTER_GESTION_CLIM.md` |

---

## ⚠️ Points d'attention

- **Refactoring 2026-06** : logique inline (~250 lignes) déplacée dans le script master. L'automation est maintenant un simple wrapper de 30 lignes.
- **SALON groupe_3 JOUR** : Eric seul → `temp_conf_e` (comportement identique à l'ancienne version inline).
- `trigger_id` et `trigger_entity_id` sont passés au script pour que la notification fenêtre reste ciblée.
- Le `sensor_update` ne redémarre **pas** une clim déjà en `off` (protection maintenue dans le script).
