# FICHE OPÉRATOIRE — Relais cuisine (Shelly 1PM Gen4) : mise à jour firmware

*Créée le 2026-09-20 — à exécuter avant l'hiver (rien d'urgent, mais à ne pas oublier).*

## Équipement
- **Relais radiateur cuisine — Shelly 1PM Gen4** (WiFi + Zigbee, relais avec metering),
  piloté aujourd'hui en **Z2M via Zigbee**.
- Entités HA clés : `switch.radiateur_elec_cuisine` + metering (`power` / `voltage` / `current` / `ac_frequency`) ;
  ⚠️ `sensor.radiateur_elec_cuisine_energy` = **unknown** → **c'est le bug que la MAJ doit éliminer**
  (c'est aussi la raison du capteur Riemann « exception cuisine » et du doute conso P1).
- Config WiFi actuelle (lue via Z2M) : SSID « Module B.E.R.Y.L. [GG-2.4] », IP statique `10.32.154.246`,
  passerelle `10.32.154.1`, DNS `1.1.1.1`.

## PRÉ-REQUIS / AVANT
- [ ] Dans Z2M : noter le **nom exact** + l'**adresse IEEE** du device + capture de sa config (avant retrait) ;
- [ ] Vérifier qu'aucune automation chauffage cuisine ne tourne (hors saison : tout est OFF ✓) ;
- [ ] Un **navigateur** (téléphone ou PC) — AUCUN compte Shelly requis (voie web locale, validée
  doc officielle 21/09 : « you do not need ... Shelly Cloud ... just be in the same Wi-Fi network ») ;
  ⚠️ si tu tiens quand même à l'app : son login est actuellement bloqué (compte/MDP) — inutile pour l'op.
- [ ] Accès Z2M admin (Permit join) ; je peux vérifier le côté HA/Z2M en direct pendant l'opération.

## ÉTAPES
### 1) Bascule en WiFi — VOIE WEB (sans compte)
- [ ] Retirer le relais de Z2M (après avoir noté IEEE + nom) ;
- [ ] Reset du module : **appui long ~10 s** sur son bouton (jusqu'au clignotement) —
  ⚠️ efface aussi les identifiants WiFi provisionnés le 21/09, c'est normal ;
- [ ] Téléphone/PC : se connecter au WiFi du Shelly (« **Shelly1PMG4-XXXXXXXXXX** ») ;
- [ ] Navigateur → **http://192.168.33.1** (interface locale du device, sans compte, sans internet) ;
- [ ] **Settings → Wi-Fi** → choisir le réseau + mot de passe → sauvegarder :
  un message clair s'affiche si la connexion échoue (ça diagnostic tout seul !),
  l'IP s'affiche si c'est bon (option : remettre la statique 10.32.154.246).

### 2) Mise à jour firmware — VOIE WEB
- [ ] Depuis le réseau maison : navigateur → **IP du Shelly** (ex. 10.32.154.246) ;
- [ ] ⚙️ Avant de lancer : vérifier **Settings → Power on default** (mettre « Off » pour éviter
  que le radiateur se rallume au reboot de fin de MAJ — piège connu) ;
- [ ] **Settings → Firmware Update** → vérifier la dispo → lancer ;
- [ ] Attendre 100% (ne pas couper l'alimentation).

### 3) Rebascule en Z2M
- [ ] Sortir l'appareil de l'app (ou reset) ;
- [ ] Z2M : **Permit join** → appairer ;
- [ ] **Renommer exactement `radiateur_elec_cuisine`** (sinon toutes les entités HA changent de nom) ;
- [ ] Re-vérifier les entités : `switch.radiateur_elec_cuisine` répond on/off.

### 4) Couper la WiFi
- [ ] Vérifier que le module ne reste pas sur le WiFi (statut WiFi muet côté Z2M) ;
- [ ] Si la config statique `10.32.154.246` traîne encore : la neutraliser
  (⚠️ cette IP est aussi celle que `reseau.md` réservait à un futur CT Cloudflared — à démêler).

## VÉRIFICATIONS (après coup — le vrai juge de paix)
- [ ] `sensor.radiateur_elec_cuisine_energy` : **unknown → un nombre** ? (LE but de la MAJ) ;
- [ ] `power` / `voltage` (~231 V) / `current` remontent ;
- [ ] `update.radiateur_elec_cuisine` : état après MAJ ;
- [ ] Test chauffage : allumer le radiateur 10 min → power > 0, energy qui grimpe ;
- [ ] Automations chauffage cuisine intactes (test complet à la saison).

## SI ÇA TOURNE MAL (rollback)
- Module injoignable : reset + re-appairage Z2M (l'IEEE ne change pas → Z2M retrouve son entrée ; renommer si besoin) ;
- En attendant : pilotage manuel via `switch.radiateur_elec_cuisine` (rien de vital hors saison).

## Lien avec F-1
Si la MAJ répare le metering natif → le remplacement par NodOn (F-1) **peut devenir inutile** : à re-décider après.
(Note : F-1 parlait d'un « Tuya TS0001 » — vestige de l'ancien relais, retiré par Berry ; le relais en place est un **Shelly 1PM Gen4**.)

## Notes (21/09/2026)
- **Identifiants WiFi déjà poussés dans le relais via Zigbee** (commande `wifi_config`) : enabled/ssid/IP/mot de passe OK — seule l'écriture gateway/DNS a échoué sur une erreur de route (valeurs identiques, sans impact). L'app Shelly devrait voir le relais arriver directement sur le WiFi lors de l'opération.
- **OTA Zigbee : impossible pour l'instant** — doc Z2M officielle : « connect Shelly devices by WiFi /
  Bluetooth, and update their firmware, until they gain support for OTA updates over Zigbee ».
  Confirmé par test réel (21/09) : `No endpoint found with OTA cluster support` + aucune image
  Shelly dans l'index OTA de Z2M (0 entrée). → La procédure WiFi/App ci-dessus est LA seule voie.
- 🎯 **But concret de la MAJ : la dernière firmware corrige les lectures de puissance négatives**
  (« fixes known issues like negative power readings ») — constaté sur ce relais : -1797 W pendant
  une chauffe le 21/09. Roll-out par phases → si le bug persiste après la MAJ stable, voir canal beta.
- Option Z2M si le relais ne rejoint pas le WiFi à l'op : **`shelly_wifi_ssid`** (le cluster Shelly
  peut rapporter un SSID raccourci — renseigner alors le nom complet du réseau dans les options device).
- ⚠️ Route Zigbee de ce relais capricieuse (`SOURCE_ROUTE_FAILURE` récurrent sur le nœud 63712).
- Petit piège : chaque `wifi_config` set s'écrit en morceaux ; le DERNIER (gateway+DNS, valeurs redondantes)
  échoue souvent sur cette route → le set est signalé 'failed' ALORS QUE l'essentiel est passé
  (enabled/ssid/mot de passe/IP). **NE PAS re-tenter en boucle** : c'est cosmétique.
  Confirmation définitive du mot de passe : au premier boot WiFi du relais (jour de l'op).
