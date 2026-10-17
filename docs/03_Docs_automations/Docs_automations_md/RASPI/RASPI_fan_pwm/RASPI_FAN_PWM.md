# Raspberry Pi4 - CPU Fan PWM 6 States

**Catégorie :** RASPI (sauvegarde du Raspberry, ce n'est pas une automation de Home Assistant)
**Alias HA :** `Raspberry CPU Fan PWM 6 States`

## Description

Règle la vitesse du ventilateur du Raspberry (`fan.rpi_cooling_fan`) en fonction de la température du CPU (`sensor.system_monitor_temperature_du_processeur`). Au démarrage de HA le ventilateur est mis à 100 %. Déclencheurs : démarrage, et franchissement à la hausse et à la baisse des seuils 30, 40, 50, 60 et 70. Sous 30 : 30 %. Les autres paliers sont dans le YAML.

## Déclencheurs

- `homeassistant`
- `numeric_state`

## Entités principales

- `sensor.system_monitor_temperature_du_processeur`
- `fan.rpi_cooling_fan`

## Fichier source

`docs/03_docs_automations/docs_automations_YAML/RASPI/A_RASPI_fan_pwm_6_states/A_RASPI_fan_pwm_6_states.yaml`

---
*Doc générée le 2026-05-30 ; relue et complétée le 2026-10-11 d'après le YAML (description, chemin source). Pas d'ID HA : l'automation tourne sur le Raspberry.*
