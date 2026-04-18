<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--01-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Tutoriel-ff9800?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-HACF-2196f3?style=flat-square)](https://forum.hacf.fr/t/alerte-meteo/23930)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Fichiers produits** | `command_line/meteo/carte_meteo_france.yaml` |
| 🔗 **Utilisé dans** | `docs/L1C1_METEO/PAGE_METEO.md` → POP-UP #ALERT |
| 🏗️ **Méthode** | `command_line` sensor + `camera: local_file` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-01 |
| 🏠 **Version HA** | 2025.1.x → 2.0 |

---

# 🗺️ TUTO — IMAGES DE VIGILANCE MÉTÉO FRANCE

> Récupérer et afficher les **cartes nationales de vigilance Météo France** (aujourd'hui et demain)
> directement dans Home Assistant, via l'API officielle Météo France.

---

## 📋 TABLE DES MATIÈRES

1. [Principe de fonctionnement](#principe-de-fonctionnement)
2. [Pré-requis](#pré-requis)
3. [Étape 1 — Créer le compte API Météo France](#étape-1--créer-le-compte-api-météo-france)
4. [Étape 2 — Préparer l'image de fallback](#étape-2--préparer-limage-de-fallback)
5. [Étape 3 — Configurer command_line.yaml](#étape-3--configurer-command_lineyaml)
6. [Étape 4 — Déclarer les caméras](#étape-4--déclarer-les-caméras)
7. [Étape 5 — Automatisation de rafraîchissement](#étape-5--automatisation-de-rafraîchissement)
8. [Étape 6 — Afficher dans le dashboard](#étape-6--afficher-dans-le-dashboard)
9. [Vérification](#vérification)
10. [Dépannage](#dépannage)
11. [Fichiers liés](#fichiers-liés)

---

## ⚙️ PRINCIPE DE FONCTIONNEMENT

```
  portail-api.meteofrance.fr
           │
           │ API Key
           ▼
  public-api.meteofrance.fr
  /DPVigilance/v1/vignettenationale-J/encours   ← Aujourd'hui
  /DPVigilance/v1/vignettenationale-J1/encours  ← Demain
           │
           │ curl (base64 → PNG)
           ▼
  /config/www/weather/
  ├── meteo_france_alerte_today.png
  ├── meteo_france_alerte_tomorrow.png
  └── meteo_france_alerte_nodata.png   ← fallback si API KO
           │
           │ camera: local_file
           ▼
  camera.mf_alerte_today
  camera.mf_alerte_tomorrow
           │
           │ POP-UP #ALERT (bubble-card)
           ▼
  Dashboard Tablette → Page Météo
```

**Cycle de mise à jour :** toutes les **4h** (scan_interval) + refresh forcé à **06:32** et **16:32** via automation.

---

## ✅ PRÉ-REQUIS

- Home Assistant avec accès au fichier `command_line.yaml` (ou équivalent inclus depuis `configuration.yaml`)
- Accès Shell / Terminal HA (ou File Editor)
- Un compte sur `portail-api.meteofrance.fr` (gratuit)
- `curl` disponible dans l'environnement HA (natif sur HA OS et Container)
- Le dossier `/config/www/weather/` créé (ou à créer)

---

## ÉTAPE 1 — CRÉER LE COMPTE API MÉTÉO FRANCE

### 1.1 Inscription

1. Aller sur **https://portail-api.meteofrance.fr/**
2. Cliquer sur **"Se connecter"** → **"Créer un compte"**
3. Remplir le formulaire (nom d'utilisateur **≠ email**, noter le username soigneusement)
4. Valider l'email de confirmation

### 1.2 Souscrire à l'API Vigilance

1. Une fois connecté, aller dans **"Catalogue des APIs"**
2. Rechercher : **`DonneesPubliquesVigilance`**
3. Cliquer sur l'API → **"Souscrire"**
4. Choisir le plan **"Freemium"** (gratuit, suffisant)
5. Valider la souscription

### 1.3 Générer l'API Key

1. Aller dans **"Mes applications"** → **"Ajouter une application"**
2. Donner un nom (ex: `home-assistant`)
3. Sélectionner la souscription `DonneesPubliquesVigilance`
4. Cliquer **"Générer les clés"**
5. Choisir le type **"API Key"** — Durée : `94672800` secondes (≈ 3 ans)
6. **Copier la clé générée** et la stocker dans `secrets.yaml` :

```yaml
# secrets.yaml
mf_api_key: "VOTRE_CLE_ICI"
```

> ⚠️ **Ne jamais coller la clé en dur dans les fichiers de config** — toujours passer par `secrets.yaml`.

---

## ÉTAPE 2 — PRÉPARER L'IMAGE DE FALLBACK

L'image `meteo_france_alerte_nodata.png` est utilisée quand l'API est indisponible après 5 tentatives.

### Créer le dossier

Via le **File Editor** ou **Terminal** :

```bash
mkdir -p /config/www/weather
```

### Télécharger une image de fallback

Télécharger une image grise/neutre de taille correcte (≈ 600×600 px) et la nommer :

```
/config/www/weather/meteo_france_alerte_nodata.png
```

> 💡 Tu peux en générer une simple via n'importe quel éditeur d'image, ou récupérer l'image officielle de Météo France quand le service est nominal et la renommer en `nodata.png`.

---

## ÉTAPE 3 — CONFIGURER COMMAND_LINE.YAML

Fichier concerné dans ReBuild : **`command_line/meteo/carte_meteo_france.yaml`**

### Vérifier l'include dans configuration.yaml

```yaml
# configuration.yaml
command_line: !include command_line.yaml
```

> Si tu utilises la structure ReBuild avec des sous-dossiers, l'include peut être :
> ```yaml
> command_line: !include_dir_merge_list command_line/
> ```

### Code complet — carte_meteo_france.yaml

```yaml
# --- sensor_meteo_france_alertes_image_today ---
- sensor:
    name: "Météo France alertes image today"
    unique_id: meteo_france_alertes_image_today
    scan_interval: 14400
    command_timeout: 10
    command: |-
      api_key="!secret mf_api_key";
      i=0;
      while true; do
        today=$(curl -s -X GET \
          "https://public-api.meteofrance.fr/public/DPVigilance/v1/vignettenationale-J/encours" \
          -H "accept: */*" \
          -H "apikey: $api_key" | base64 -w 0);
        $((i++));
        if [[ $(expr length "$today") -gt "10000" ]]; then
          echo "$today" | base64 -d > /config/www/weather/meteo_france_alerte_today.png;
          echo on;
          break;
        elif [[ "$i" == '5' ]]; then
          cp -f "/config/www/weather/meteo_france_alerte_nodata.png" \
                "/config/www/weather/meteo_france_alerte_today.png";
          echo unavailable;
          break;
        fi
        sleep 1;
      done
    value_template: "{{ value }}"

# --- sensor_meteo_france_alertes_image_tomorrow ---
- sensor:
    name: "Météo France alertes image tomorrow"
    unique_id: meteo_france_alertes_image_tomorrow
    scan_interval: 14400
    command_timeout: 10
    command: |-
      api_key="!secret mf_api_key";
      i=0;
      while true; do
        tomorrow=$(curl -s -X GET \
          "https://public-api.meteofrance.fr/public/DPVigilance/v1/vignettenationale-J1/encours" \
          -H "accept: */*" \
          -H "apikey: $api_key" | base64 -w 0);
        $((i++));
        if [[ $(expr length "$tomorrow") -gt "10000" ]]; then
          echo "$tomorrow" | base64 -d > /config/www/weather/meteo_france_alerte_tomorrow.png;
          echo on;
          break;
        elif [[ "$i" == '5' ]]; then
          cp -f "/config/www/weather/meteo_france_alerte_nodata.png" \
                "/config/www/weather/meteo_france_alerte_tomorrow.png";
          echo unavailable;
          break;
        fi
        sleep 1;
      done
    value_template: "{{ value }}"
```

### Logique du script expliquée

| Étape | Ce qui se passe |
|:------|:----------------|
| `curl` vers l'API | Télécharge l'image en binaire depuis Météo France |
| `\| base64 -w 0` | Encode le binaire en base64 (chaîne de texte sans saut de ligne) |
| `expr length "$today" -gt 10000` | Vérifie que la réponse est une vraie image (>10Ko) |
| `base64 -d > fichier.png` | Décode et écrit le PNG sur disque |
| `$((i++))` + `"$i" == '5'` | Compteur de tentatives — max 5 avant fallback |
| `cp nodata.png` | Fallback : copie l'image grise si API KO |
| `echo on` / `echo unavailable` | État du sensor HA (on = succès, unavailable = échec) |
| `scan_interval: 14400` | Refresh automatique toutes les 4h |

---

## ÉTAPE 4 — DÉCLARER LES CAMÉRAS

Les caméras lisent simplement les fichiers PNG créés par les sensors command_line.

### Dans configuration.yaml

```yaml
# configuration.yaml
camera:
  - platform: local_file
    name: MF alerte today
    file_path: /config/www/weather/meteo_france_alerte_today.png

  - platform: local_file
    name: MF alerte tomorrow
    file_path: /config/www/weather/meteo_france_alerte_tomorrow.png
```

> Cela crée automatiquement :
> - `camera.mf_alerte_today`
> - `camera.mf_alerte_tomorrow`

---

## ÉTAPE 5 — AUTOMATISATION DE RAFRAÎCHISSEMENT

Le `scan_interval` suffit pour la mise à jour quotidienne, mais les alertes peuvent changer rapidement. Cette automation force un refresh à des horaires clés.

```yaml
alias: METEO - Refresh cartes alertes Météo France
description: "Force la mise à jour des images de vigilance MF à 06h32 et 16h32"
trigger:
  - platform: homeassistant
    event: start
  - platform: time
    at: "06:32:00"
  - platform: time
    at: "16:32:00"
  - platform: state
    entity_id:
      - sensor.meteo_france_alertes_image_today
      - sensor.meteo_france_alertes_image_tomorrow
    to: "unavailable"
    for:
      minutes: 5
condition: []
action:
  - service: homeassistant.update_entity
    target:
      entity_id:
        - sensor.meteo_france_alertes_image_today
        - sensor.meteo_france_alertes_image_tomorrow
  - delay:
      seconds: 5
  - service: homeassistant.update_entity
    target:
      entity_id:
        - camera.mf_alerte_today
        - camera.mf_alerte_tomorrow
mode: single
```

> **Pourquoi le délai de 5s ?** Les sensors command_line doivent finir d'écrire le fichier PNG avant que la caméra ne soit rafraîchie.

---

## ÉTAPE 6 — AFFICHER DANS LE DASHBOARD

### Carte basique (image plein format)

```yaml
- type: picture-entity
  entity: camera.mf_alerte_today
  show_state: false
  show_name: false
  card_mod:
    style: |
      ha-card {
        border: none !important;
        box-shadow: none !important;
        background: transparent;
      }
```

### Affichage côte à côte (Aujourd'hui / Demain)

```yaml
- type: horizontal-stack
  cards:
    - type: picture-entity
      entity: camera.mf_alerte_today
      show_state: false
      show_name: true
      name: Aujourd'hui

    - type: picture-entity
      entity: camera.mf_alerte_tomorrow
      show_state: false
      show_name: true
      name: Demain
```

### Dans un pop-up Bubble Card (usage PAGE_METEO)

```yaml
- type: custom:bubble-card
  card_type: pop-up
  hash: "#alert"
  name: Alertes Météo France
  icon: mdi:alert-outline

  cards:
    - type: horizontal-stack
      cards:
        - type: picture-entity
          entity: camera.mf_alerte_today
          show_name: true
          name: Aujourd'hui

        - type: picture-entity
          entity: camera.mf_alerte_tomorrow
          show_name: true
          name: Demain
```

---

## ✔️ VÉRIFICATION

Après redémarrage de HA :

1. **Outils de développement → États** → chercher `sensor.meteo_france_alertes_image_today`
   - État attendu : `on`
   - Si `unavailable` → problème API (voir Dépannage)

2. **Outils de développement → États** → chercher `camera.mf_alerte_today`
   - Doit être présente

3. **Vérifier le fichier créé** (File Editor ou Terminal) :
   ```bash
   ls -lh /config/www/weather/
   ```
   → Les fichiers `meteo_france_alerte_today.png` et `tomorrow.png` doivent exister et avoir une taille > 10 Ko.

4. **Appeler manuellement le sensor** :
   Outils de développement → Services → `homeassistant.update_entity`
   → entity_id : `sensor.meteo_france_alertes_image_today`

---

## 🐛 DÉPANNAGE

### Sensor reste en `unavailable`

| Cause | Solution |
|:------|:---------|
| API Key incorrecte | Revérifier `secrets.yaml`, recopier la clé depuis le portail |
| Souscription expirée | Aller sur `portail-api.meteofrance.fr` → renouveler |
| API Météo France instable | Attendre — l'API MF est connue pour être instable, le retry à 5 tentatives est là pour ça |
| `curl` non disponible | Vérifier l'environnement HA (HA OS : curl est natif) |
| Erreur return code 56 | Problème réseau ou API MF HS — transitoire, se résout seul |

### L'image s'affiche mais est grise (nodata)

→ L'API a renvoyé une réponse vide ou trop petite (<10 Ko) lors des 5 tentatives.
→ Forcer un refresh manuel via l'automation ou attendre le prochain cycle.

### La caméra affiche une ancienne image

→ Vider le cache navigateur (`Ctrl+Shift+R`)
→ Forcer le refresh de la caméra : Services → `homeassistant.update_entity` → `camera.mf_alerte_today`

### Logs utiles

```bash
# Dans les journaux HA (Paramètres > Système > Journaux)
# Filtrer par : command_line
```

---

## 🔗 FICHIERS LIÉS

### Configuration YAML (sources HA v2.0)
- `command_line/meteo/carte_meteo_france.yaml` ← **ce fichier**
- `configuration.yaml` (déclaration camera: local_file)

### Documentation
- Page utilisant ces cameras : `docs/L1C1_METEO/PAGE_METEO.md` → section POP-UP #ALERT
- Template des alertes : `templates/meteo/M_01_meteo_alertes_card.yaml`

### Sources externes
- [Forum HACF — Alerte météo (thread principal)](https://forum.hacf.fr/t/alerte-meteo/23930)
- [Portail API Météo France](https://portail-api.meteofrance.fr/)
- [Endpoint Vigilance Today](https://public-api.meteofrance.fr/public/DPVigilance/v1/vignettenationale-J/encours)
- [Endpoint Vigilance Tomorrow](https://public-api.meteofrance.fr/public/DPVigilance/v1/vignettenationale-J1/encours)

---

← Retour : `docs/L1C1_METEO/PAGE_METEO.md` | → Suivant : `docs/L1C1_METEO/` *(à venir)*


<!-- obsidian-wikilinks -->
---
*Liens : [[L1C1_VIGNETTE_METEO]]  [[PAGE_METEO]]*
