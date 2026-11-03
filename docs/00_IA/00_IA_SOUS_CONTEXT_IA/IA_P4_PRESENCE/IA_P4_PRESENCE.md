# 👥 RÉFÉRENTIEL P4 - PRÉSENCE COMPLÈTE
<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--03-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Gelé-f44336?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-IA_System-ffeb3b?style=flat-square)](.)

</div>

*Lire ce fichier si : automation clim, message notify avec présence, logique sensor.groupe ou sensor.presence.*

---

## sensor.groupe - Logique d'automatisation

> Source : `templates/P4_groupe_presence/P4_groupe_presence.yaml`
> Réseau cible : `'Module B.E.R.Y.L. [GG-5.0]'` ou `'Module B.E.R.Y.L. [GG-2.4]'`

Utilisé par les automations (clim, volets, mode éco).

| Valeur | Signification | Condition |
|:-------|:--------------|:----------|
| `groupe_1` | **Absent** - personne sur le réseau cible | ni Mamour ni Eric en WiFi cible |
| `groupe_2` | **Mamour seule** - Eric absent | Mamour en WiFi cible, Eric hors réseau |
| `groupe_3` | **Eric seul** - Mamour absente | Eric en WiFi cible, Mamour hors réseau |
| `groupe_4` | **Tous les deux** - présence simultanée | Mamour ET Eric en WiFi cible |

---

## sensor.presence - Affichage dashboard / en-tête notifications

Utilisé dans les messages : `{{ states('sensor.presence') }}`
Format : `[X: statut_X/statut_Y]` où statut = `WIFI` | `CELL` | `WIFI_!?`

> **Comment le nom est choisi** - règle dite par Eric le 2026-11-03. Trois états par personne, donc 3 x 3 = **9 combinaisons**, réparties en trois groupes :
>
> **1. Trois cas SANS NOM (3)** - les deux statuts sont identiques, l'affichage commence par `[2]` :
> `[2] en [WIFI]`, `[2] en [CELL]`, `[2] en [WIFI_!?]`
>
> **2. Quatre cas AVEC MAMOUR (4)** - c'est le cas **par défaut**, que Mamour soit à la maison ou non :
> - Mamour à la maison : `[Mamour: WIFI/CELL]` (Eric en cellulaire), `[Mamour: WIFI/WIFI_!?]` (Eric sur un autre WiFi)
> - personne à la maison : `[Mamour: WIFI_!? / CELL]` (Mamour sur un autre WiFi), `[Mamour: CELL / WIFI_!?]` (Mamour en cellulaire)
>
> **3. Deux cas AVEC ERIC (2)** - uniquement quand **Eric est sur le réseau domestique et Mamour n'y est pas**
> (elle est en cellulaire, ou sur un autre WiFi) : `[Eric: WIFI/CELL]` et `[Eric: WIFI/WIFI_!?]`.
> Dans ces deux cas seulement, c'est **le statut d'Eric qui vient en premier**.
>
> Total : 3 + 4 + 2 = 9. Le groupe 1 n'affiche aucun nom ; au groupe 2 la première valeur est celle de Mamour, au groupe 3 celle d'Eric.

| Valeur affichée | Situation |
|:----------------|:----------|
| `[2] en [WIFI]` | Les deux sur le réseau domestique |
| `[2] en [CELL]` | Les deux en cellulaire - Aucun sur le domestique |
| `[2] en [WIFI_!?]` | Les deux en WiFi, mais sur un autre réseau - Aucun sur le domestique |
| `[Mamour: WIFI/CELL]` | Mamour présente (domestique), Eric en cellulaire |
| `[Mamour: WIFI/WIFI_!?]` | Mamour présente (domestique), Eric sur autre WiFi |
| `[Mamour: WIFI_!? / CELL]` | Mamour sur un autre WiFi, Eric en cellulaire - personne à la maison |
| `[Mamour: CELL / WIFI_!?]` | Mamour en cellulaire, Eric sur un autre WiFi - personne à la maison |
| `[Eric: WIFI/CELL]` | Eric sur le réseau domestique, Mamour en cellulaire (hors domestique) |
| `[Eric: WIFI/WIFI_!?]` | Eric sur le réseau domestique, Mamour sur un autre WiFi (hors domestique) |

---

## Légende des codes réseau

| Code | Signification |
|:-----|:--------------|
| `WIFI` | Connecté au réseau domestique (Beryl GG-5.0 ou GG-2.4) |
| `WIFI_!?` | Connecté à un autre WiFi (bureau, voisin, hotspot…) |
| `CELL` | Connexion cellulaire (4G/5G) - hors WiFi |
