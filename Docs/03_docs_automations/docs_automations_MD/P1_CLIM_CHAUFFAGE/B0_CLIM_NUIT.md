# (B-0) AUTOMATISATION CLIM NUIT (21H00 ↔ 07H30)

> **Fichier TREE_CORRIGE :** `docs_automations/TREE_CORRIGE/P1_clim_chauffage/b_0_2026_01_11_automatisation_clim_nuit_21h00_07h30.yaml`
> **Mode HA :** `queued` — max: 5
> **Dernière mise à jour :** 2026-06-28 (refactoring LLM local → délégation script)

---

## 📝 Description

Automation wrapper nocturne (21h00–07h30). Miroir de A0, délègue entièrement la
logique à `script.p1_master_gestion_clim` avec `periode: "nuit"`.
La nuit, les 3 pièces utilisent une cible uniforme `temp_nuit` (sauf groupe_1 → eco).

---

## ⚡ Déclencheurs

| ID trigger | Type | Entité / Horaire |
|:---|:---|:---|
| `ha_restart` | `homeassistant` | Démarrage HA |
| `force_run` | `time` | 21:00:00 |
| `force_run` | `state` | `sensor.mamour_network_type`, `sensor.eric_network_type` |
| `force_run` | `state` | 3 prises clim NOUS |
| `window_open` | `state` | 4 capteurs fenêtres → `off` → `on` |
| `window_close` | `state` | 4 capteurs fenêtres → `on` → `off` |
| `sensor_update` | `state` | `sensor.groupe` *(ajouté)*, `sensor.th_balcon_nord_temperature`, `sensor.temperature_cible`, `sensor.mode_ete_hiver`, `sensor.temperature_confort_nuit` |

---

## 🔒 Conditions globales

- Plage horaire : `after 21:00 before 07:30`

---

## ⚙️ Actions

Une seule action :

```yaml
- action: script.p1_master_gestion_clim
  data:
    periode: "nuit"
    trigger_id: "{{ trigger.id if trigger is defined else '' }}"
    trigger_entity_id: "{{ trigger.entity_id if trigger is defined ... else '' }}"
```

→ Voir `docs_scripts/docs/P1_MASTER_GESTION_CLIM.md` pour la logique complète.

---

## 🔌 DÉPENDANCES

### Entités lues (triggers / conditions)

| Entité | Rôle |
|:---|:---|
| `sensor.mamour_network_type` | Présence réseau Mamour |
| `sensor.eric_network_type` | Présence réseau Eric |
| `sensor.groupe` | Groupe de présence (trigger sensor_update) |
| `sensor.th_balcon_nord_temperature` | T° extérieure |
| `sensor.temperature_cible` | T° cible (utilisée comme fallback dans le script) |
| `sensor.mode_ete_hiver` | Mode saison |
| `sensor.temperature_confort_nuit` | T° confort nuit |
| 4× `binary_sensor.contact_fenetre_*` | Capteurs fenêtres |
| 3× `switch.clim_*_nous` | Prises clim (sécurité) |

### Script appelé

| Script | Paramètres | Doc |
|:---|:---|:---|
| `script.p1_master_gestion_clim` | `periode:"nuit"`, `trigger_id`, `trigger_entity_id` | `docs_scripts/docs/P1_MASTER_GESTION_CLIM.md` |

---

## ⚠️ Points d'attention

- **Refactoring 2026-06** : même architecture que A0 — wrapper 30 lignes + délégation script.
- La nuit, `t_salon_target` = `t_bureau_target` = `t_chambre_target` = `temp_nuit` (sauf groupe_1 → eco).
- `sensor.groupe` ajouté au trigger `sensor_update` lors du refactoring.
