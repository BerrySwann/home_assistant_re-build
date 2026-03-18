<div align="center">

<!-- STATUT : choisir UNE ligne ci-dessous et supprimer les autres -->
[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
<!-- [![Statut](https://img.shields.io/badge/Statut-En%20cours-ff9800?style=flat-square)](.) -->
<!-- [![Statut](https://img.shields.io/badge/Statut-%E2%9B%94%20A%20terminer-f44336?style=flat-square)](.) -->

[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-AAAA--MM--JJ-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-{TYPE_DOC}-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `{PATH_DASHBOARD}` |
| 🔗 **Accès depuis** | `{ACCES_DEPUIS}` |
| 🏗️ **Layout** | `{TYPE_LAYOUT}` |
| 🔴 **Bloquant** | `{CAUSE_SI_BLOQUE}` ← supprimer si statut Actif |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | AAAA-MM-JJ |
| 🏠 **Version HA** | 2025.1.x → 2.0 |

---

# {EMOJI} {TITRE_PRINCIPAL}

---

<!-- SI STATUT "À TERMINER" : coller le bloc ci-dessous et remplir -->
<!--
> ## ⛔ PAGE À TERMINER
>
> **Cause du blocage : {CAUSE}**
>
> Sections non opérationnelles :
> - {SECTION_1} → dépend de {DEPENDANCE}
>
> Ce qui fonctionne déjà :
> - {SECTION_OK} ✅
>
> **Reprendre quand :** {CONDITION_REPRISE}
-->

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Sections](#sections)
4. [Entités utilisées](#entités-utilisées--provenance-complète)
5. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

{DESCRIPTION_COURTE}

### Intégrations requises
- ✅ {INTEGRATION_1}
- ✅ {INTEGRATION_2}

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `{CARTE_1}` | {ROLE_1} |
| `{CARTE_2}` | {ROLE_2} |

---

## 🏗️ ARCHITECTURE

```
┌─────────────────────────────────────────────┐
│  [SECTION 1]                                │
├─────────────────────────────────────────────┤
│  [SECTION 2]                                │
├─────────────────────────────────────────────┤
│  [SECTION N]                                │
└─────────────────────────────────────────────┘
```

---

## 📍 SECTION {NOM_SECTION}

### Code

```yaml
# YAML ici
```

### Rôle
{DESCRIPTION_ROLE}

### Entités
- `{entity.id}` [{SOURCE}] — {DESCRIPTION}

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

> Chaque entité est listée avec son **fichier source exact** dans le repo ReBuild.

---

### 🌐 Intégrations natives HA (UI — aucun fichier YAML à créer)

| Entité | Intégration | Configuré via |
|--------|-------------|---------------|
| `{entity.id}` [{SOURCE}] | {INTEGRATION} | Paramètres > Intégrations |

---

### 📁 `{chemin/fichier.yaml}`
> {DESCRIPTION_FICHIER}

| Entité | unique_id | Rôle |
|--------|-----------|------|
| `{entity.id}` [{SOURCE}] | `{unique_id}` | {ROLE} |

---

## 🐛 DÉPANNAGE

### {PROBLEME_1}
1. {ETAPE_1}
2. {ETAPE_2}

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| {ELEMENT} | {TYPE} | ✅ Essentiel |
| {ELEMENT} | HACS | ⚠️ Optionnel |

---

## 🔗 FICHIERS LIÉS

### Configuration YAML (sources HA v2.0)
- `{fichier1.yaml}`
- `{fichier2.yaml}`

### Documentation
- `{doc_liee.md}`

---

← Retour : `{DOC_PRECEDENTE}` | → Suivant : `{DOC_SUIVANTE}`
