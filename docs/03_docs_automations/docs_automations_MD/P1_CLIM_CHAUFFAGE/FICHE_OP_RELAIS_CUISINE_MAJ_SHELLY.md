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
- [ ] **App Shelly (Smart Control) du portable** prête (compte configuré), téléphone avec Bluetooth ON
  et le **2,4 GHz** accessible (l'appairage Shelly Gen4 se fait en Bluetooth + WiFi) ;
- [ ] Accès Z2M admin (Permit join) ; je peux vérifier le côté HA/Z2M en direct pendant l'opération.

## ÉTAPES
### 1) Bascule en WiFi
- [ ] Retirer le relais de Z2M (après avoir noté IEEE + nom) ;
- [ ] Reset du module (selon le manuel Shelly : bouton Reset — appuis/maintien ; l'app te guidera) ;
- [ ] **App Shelly** : « Ajouter un appareil » → détection (Bluetooth) → saisir le WiFi 2,4 GHz.

### 2) Mise à jour firmware
- [ ] **Depuis l'app Shelly du portable** : page de l'appareil → **Mise à jour du firmware** → lancer ;
- [ ] Attendre la fin (ne pas couper l'alimentation).

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
