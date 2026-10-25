<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.0-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Carte-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `02_dashboard_docs_yaml/L0C0_PAGE_Home/04_Studio Code Server/card_vscode_home.yaml` |
| 🔗 **Accès depuis** | Vue principale Home (`L0C0_PAGE_Home`) |
| 🏗️ **Layout** | `conditional + custom:button-card` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-10-11 |
| 🏠 **Version HA** | 2026.10.0 |

---

# 💻 Carte : Studio Code Server (CPU)

---

## 📋 VUE D'ENSEMBLE

Carte conditionnelle de la page Home : elle affiche la charge CPU de l'add-on Studio Code Server et permet de le redémarrer. Elle n'apparaît que si le CPU dépasse 1 %.

Carte HACS utilisée : `custom:button-card` (dans un `conditional`).

---

## 🎯 FONCTIONNEMENT

| Condition | Rendu |
|:----------|:------|
| CPU <= 1 % | carte masquée (condition `numeric_state`, au-dessus de 1) |
| 1 % < CPU <= 20 % | fond bleu `#03a9f4` |
| CPU > 20 % | fond rouge `#f44336` + clignotement (`blink`, 1 s) |

- Valeur affichée avec 2 décimales suivies de `%`.
- Tap : fenétre de confirmation ("VS Code semble bloqué ? Voulez-vous forcer le redémarrage de l'Add-on ?"), puis service `hassio.addon_restart` sur l'add-on `a0d7b954_vscode`.

---

## 📊 ENTITÉS UTILISÉES

| Entité | Rôle |
|:---------|:-----|
| `sensor.studio_code_server_pourcentage_du_processeur` | Condition de visibilité (> 1) + valeur affichée + couleur |

Add-on piloté par le tap : `a0d7b954_vscode`.

---

## 📁 FICHIERS LIÉS

- YAML : `card_vscode_home.yaml` (dossier `04_Studio Code Server` côté YAML)
- Page : [PAGE_HOME.md](../02_page/PAGE_HOME.md), carte 3
