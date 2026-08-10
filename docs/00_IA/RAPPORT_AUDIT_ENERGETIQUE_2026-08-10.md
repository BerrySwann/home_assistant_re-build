# RAPPORT D'AUDIT ENERGETIQUE - BILAN AU 2026-08-10
*Genere le 2026-08-10 - Donnees : diag_conso_elec.txt (03/01 -> 10/08, 13 958 lignes, 13 956 parsees)*

**Perimetre :** Confrontation du RAPPORT_AUDIT_ENERGETIQUE_2026-07-19.md aux donnees corrigees
(parseur 6 variantes + suffixe DUT variable). Corrige la sous-evaluation Avr->Aout du rapport
precedent (-49 % de lignes perdues, variante `[2] en [WIFI]` ignoree).

---

## 1. CORRECTIONS APPORTEES AUX DONNEES

| Point du rapport 19/07 | Realite corrigee | Verdict |
|:---|:---|:---|
| "11 880 lignes, donnees 20/12 -> 19/07" | 13 958 lignes, 03/01 -> 10/08 (20/12 = en-tete seul) | Fichier complete |
| "Juillet en cours, N=18 j" | Juillet = 31 jours COMPLETS (443,8 kWh) | Le parseur cachait la fin de mois |
| "Juin absent des logs" | Juin = 30 jours COMPLETS (327,6 kWh) | Faux - bug de parse |
| "Fevrier 9 j" | 10 j | Ecart mineur |
| DUT hiver (S 3,93 / B 9,98 / C 11,72, ratio 1,17) | Identiques | Rapport valide sur l'hiver |
| Artefact "%}" ponctuel (19/01) | SYSTEMATIQUE sur le format 2 (19/01 -> 15/04, 3 062 lignes) | Note "ponctuel" fausse |

Seule veritable lacune restante : mars absent, avril/mai partiels (21/22 j).

---

## 2. CONSO MENSUELLE - RAPPORT vs CORRIGE

| Mois | Rapport 19/07 | Corrige 10/08 | kWh/j | Ecart |
|:---|:---|:---|:---|:---|
| Janv | 391,8 (29 j) | 397,2 | 13,7 | +1 % (colonne Autres) |
| Fevr | partiel 9 j | 151,5 (10 j) | 15,2 | - |
| Avr | 127,8 (18 j) | 151,9 (21 j) | 7,2 | +19 % |
| Mai | "absent" | 162,7 (22 j) | 7,4 | trouve |
| Juin | "absent" | 327,6 (30 j) | 10,9 | trouve |
| Juil | ~270 (18 j) | 443,8 (31 j) | 14,3 | +64 % |
| Aout | - | 182,8 (10 j) | 18,3 | nouveau |

Total periode : ~1 817 kWh (7 mois et 10 jours).

### Ranking complet par mois (kWh, tous postes, corrige)

| Mois | Hyg | Cuis | Froid | Chauff | Multi | Lum | Autres | TOTAL |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Janv | 19,9 | 28,2 | 20,9 | 222,9 | 93,4 | 6,7 | 5,2 | 397,2 |
| Fevr | 6,9 | 11,2 | 7,8 | 85,3 | 31,0 | 4,5 | 4,8 | 151,5 |
| Avr | 15,5 | 20,1 | 21,0 | 8,0 | 72,8 | 6,3 | 8,3 | 151,9 |
| Mai | 13,6 | 19,8 | 22,1 | 4,9 | 83,3 | 8,2 | 10,8 | 162,7 |
| Juin | 17,4 | 24,4 | 36,5 | 120,9 | 104,2 | 15,1 | 9,0 | 327,6 |
| Juil | 14,0 | 16,3 | 42,7 | 240,6 | 102,9 | 17,7 | 9,6 | 443,8 |
| Aout | 6,8 | 6,2 | 12,5 | 97,7 | 48,7 | 7,9 | 3,0 | 182,8 |

---

## 3. DUT PAR PIECE - INVERSION ESTIVALE COMPLETEE

| Mois | Salon S | Bureau B | Chambre C | Ratio C/B |
|:---|:---|:---|:---|:---|
| Janv (hiver) | 3,93 h | 9,98 h | 11,72 h | 1,17 (chambre +17 %) |
| Fevr | 4,61 | 8,68 | 10,55 | 1,22 |
| Juin | 4,92 | 4,03 | 1,14 | 0,28 |
| Juil (complet) | 9,31 | 8,69 | 2,98 | 0,34 |
| Aout (9 j, hors 10/08 partiel) | 10,57 | 13,53 | 6,54 | 0,48 |

- Hiver du rapport VALIDE a l'identique (S 3,93 / R 0,78 / B 9,98 / C 11,72, ratio 1,17).
- Inversion estivale CONFIRMEE : la chambre, pire piece l'hiver, devient la meilleure l'ete.
- Salon x2,5 en ete : confirme (3,93 -> 9,88 h).
- DECOUVERTE : en aout, le Bureau depasse le Salon (13,53 vs 10,57 h, hors jour partiel
  du 10/08). PC Eric (~190 W) + canicule + CHALEUR DU SALON TRANSFEREE PAR LA CLOISON
  CARREAU DE PLATRE (mur mitoyen 40 %, le salon est le coeur chaud en ete) = Daikin
  bureau quasi-continue (15,3 h le 09/08). Le Bureau devient le poste clim le plus
  couteux d'aout.
- La mitoyennete salon/bureau (carreau de platre, 40 % du mur) est a DOUBLE TRANCHANT :
  rediffusion gratuite l'hiver (renforce le ratio C/B 1,17), transfert de chaleur l'ete -
  c'est la meme cause structurelle qui protege la chambre l'ete (2 murs beton) et la
  penalise l'hiver.

---

## 4. TALON NOCTURNE (Multi @02h00)

| Mois | Rapport | Corrige |
|:---|:---|:---|
| Janv | 122 W | 122 W |
| Fevr | 83 W | 83 W |
| Avr | 103 W | 99 W |
| Mai | - | 53 W (propre) |
| Juin | - | ~90 W (hors glitch 15/06) |
| Juil | - | 61 W (propre) |
| Aout | - | ~112 W (vacances) |

Juin : la moyenne 211 W affichee precedemment etait GONFLEE par le 15/06 (4 035 W au
talon = RESET MANQUE A MINUIT : compteur Multi reparti de 7,92 kWh au lieu de ~0, puis
reset en cours de journee - meme famille que les 8 resets intra-jour de janv/fevr, pas un
evenement de conso). Le total du 15/06 (3,04 kWh) reste valide (post-reset).
Hors incident : ~90 W, avec 4 nuits a 200-255 W (09, 11, 21, 22/06) = PC laisse allume la
nuit, intermittent. Aout : ~112 W avec 2 nuits hautes (05/08 255 W, 10/08 185 W) -
coherent avec des soirees tardives de vacances (voir section 9). Juillet propre (61 W).

---

## 5. CANICULE

### Periode
42 jours a >= 29 C de moyenne entre le 30/05 et le 09/08 - canicule quasi ininterrompue :
- mai : 1 j (30/05)
- juin : 11 j (20-30/06)
- juillet : 21 j
- aout : 9 j (01-09/08, canicule continue)

### Pics de consommation

| Jour | T ext moy | Chauff/clim | Remarque |
|:---|:---|:---|:---|
| 28/06 | 32,6 C | 14,1 kWh | Pic absolu de la periode |
| 09/08 | 31,0 C | 12,3 kWh | Dernier pic enregistre |

### Cas particuliers

- **30/05 (1,6 kWh) : donnee PARTIELLE** - 17 lignes seulement, fin a 17h. Valeur incomplete.
- **10-12/07 (~1-2 kWh/j) : conso faible MAIS meteo chaude (~29 C)** - explique par
  l'ABSENCE des 2 occupants ([2] en [CELL], voir section 9), pas par une accalmie meteo.
- **10/08 (27 C) : retour sous le seuil** - la canicule semble casser.

### Lecture
La conso clim suit la temperature : 6-8 kWh/j a 29 C, 9-12 kWh/j a 30-31 C,
14 kWh/j a 32,6 C (pic).

### Points de rupture (A ACTUALISER A CHAQUE BILAN)

| Saison | Decrochage | Preuve | Fiabilite |
|:---|:---|:---|:---|
| Hiver | ~8 C de moyenne | Ti chute (20,0 -> 19,5-19,7 C), chambre quasi-continue (15,8 h/j a 6 C), conso au max sans resultat | Seuil solide (n=11) ; < 8 C : 4 jours seulement |
| Ete | ~29 C de moyenne | la nuit ne refroidit plus (Ti bloquee a 26,5 C a 5h15), conso sans plafond (7,6 -> 14,1 kWh/j de 29 a 33 C) | Solide |

- Regime plein hiver (palier ~8,5-9 kWh/j) : des ~10-11 C de moyenne ; conso quasi nulle au-dessus de 15-17 C.
- Ce sont des moyennes journalieres : 8 C moy ~= Tmin 3-5 C ; 29 C moy ~= Tmax 33-35 C.
- Les seuils sont a affiner a chaque bilan avec les nouvelles donnees (hivers/etes supplementaires).
- **OCCUPATION - a verifier a CHAQUE bilan avant de conclure** : croiser les chiffres avec les tags presence - l'occupation explique Multi (vacances = +47 %), talon nocturne (soirees tardives), DUT des jours calmes (absences = -80 a -90 %). Ne jamais qualifier un chiffre d'anomalie sans avoir verifie l'occupation (vecu aout 2026).

---

## 6. COUTS ESTIMES (tarifs verifies sur grille officielle EDF 01/08/2026)

### Horaires HP/HC du contrat (confirme par Eric le 2026-08-10)

| Plage | Heures |
|:---|:---|
| **Heures creuses - nuit** | 01h30 -> 07h30 |
| **Heures creuses - jour** | 13h00 -> 14h30 |
| **Heures pleines** | 07h30 -> 13h00 + 14h30 -> 01h30 |

Total HC : 7,5 h/j (6 h nuit + 1,5 h jour). Consequence : la clim de 22h a 01h30
(pic soiree) est facturee en HP (voir section 11).

Verification internet le 2026-08-10 (grille Tarif Bleu EDF, PDF officiel, applicable au 01/08/2026) :

| Element | Grille debut 2026 (doc v6.3) | Grille 01/08/2026 | Ecart |
|:---|:---|:---|:---|
| HP | 0,2065 EUR/kWh | 0,2142 EUR/kWh | +3,7 % (hausse du 01/08) |
| HC | 0,1578 EUR/kWh | 0,1589 EUR/kWh | +0,7 % |
| Abonnement 6 kVA | - | 15,86 EUR/mois | - |
| Base 6 kVA (comparaison) | - | 0,2001 EUR/kWh | HPHC reste avantageux (19,6 cts pondere a 1/3 HC) |

Les TRV bougent chaque 1er fevrier et 1er aout - a reverifier a chaque bilan.

Mix reel mesure par deltas horaires avec les fenetres HC CONFIRMEES par Eric
(nuit 01h30-07h30 + jour 13h-14h30, 7,5 h/j) :

| Mois | HP % | HC % | Cout pondere | Cout mix reel |
|:---|:---|:---|:---|:---|
| Janv | 71 % | 29 % | 0,1979 | ~79 EUR |
| Fevr | 70 % | 30 % | 0,1978 | ~30 EUR |
| Avr | 77 % | 23 % | 0,2014 | ~31 EUR |
| Mai | 78 % | 22 % | 0,2023 | ~33 EUR |
| Juin | 74 % | 26 % | 0,1997 | ~65 EUR |
| Juil | 77 % | 23 % | 0,2016 | ~89 EUR |
| Aout | 74 % | 26 % | 0,1998 | ~37 EUR (rythme ~110 EUR/mois) |
| **Total** | ~75 % | ~25 % | ~0,20 | **~364 EUR** |

Lecture : la fenetre HC nuit courte (01h30-07h30) DEFAVORISE l'ete - la clim de 22h a
01h30 est facturee en HP (voir section 11). Total = 1 817,9 kWh.

---

## 7. STATUT DES ANOMALIES DU RAPPORT 19/07

| # | Anomalie | Statut au 10/08 |
|:--|:---|:---|
| A1 | Auto B radiateur sans arret force (CRITIQUE) | Non verifiable en ete (DUT R = 0 juil/aout). Fix docs/03 "non deploye" au 19/07 - a confirmer en prod avant l'hiver |
| A2 | Chambre +17 % DUT hiver | Confirme (1,17 janv, 1,22 fevr). Option A (rappel 21h30) : statut inconnu |
| A3 | Talon nocturne > 100 W | Nuance : aout = vacances (soirees tardives, pas un bug) ; juin = 4 nuits hautes + glitch donnees 15/06 (4 035 W) |
| A4 | Logs discontinus | Corrige en partie : juin + juillet complets. Reste mars absent, avr/mai troues |
| A5 | Hitachi 2008 a remplacer | Toujours valide, ROI 18-24 ans inchange (~50 EUR/an d'economie) |
| A6 | Multi = 2e poste toute l'annee | Nuance : vrai hiver/printemps, mais clim repasse 1er poste en juillet-aout (54 %) |

---

## 8. RANKING ETE (juillet complet, corrige)

Chauff/clim 54 % > Multi 23 % > Froid 10 % > Lum 4 % > Cuis 4 % > Hyg 3 % > Autres 2 %.

La projection du rapport 19/07 ("Multi dominant l'ete", basee sur avril) est INVALIDEE :
en canicule, la clim est le poste n1 comme le chauffage en hiver. Le froid double en ete
(42,7 vs 20,9 kWh en janvier).

---

## 9. PRESENCE / OCCUPATION (tags sensor.presence)

Les tags de presence ont ete ajoutes au fichier de logs par Eric (depuis le 29/04) pour
eviter les incomprehensions sur certains chiffres (referentiel : IA_P4_PRESENCE.md).

| Tag | Signification |
|:---|:---|
| `[2] en [WIFI]` | Eric + Mamour a la maison (WiFi domestique Beryl) |
| `[2] en [CELL]` | Les deux absents (cellulaire) |
| `[Eric: WIFI/CELL]` | Eric a la maison, Mamour en cellulaire |
| `[Mamour: WIFI/CELL]` | Mamour a la maison, Eric en cellulaire |

### Empreinte energetique de la presence

| Mois | Multi kWh/j | Talon @02h | Presence dominante | Lecture |
|:---|:---|:---|:---|:---|
| Juin | 3,47 | ~90 W (hors glitch) | `[2] en [WIFI]` quasi tous les jours | 4 nuits a 200-255 W (PC la nuit, intermittent) |
| Juil | 3,32 | 61 W | `[2] en [WIFI]` | propre |
| Aout | 4,87 | ~112 W | `[2] en [WIFI]` | vacances : soirees tardives, talon haut = style de vie |

**Empreinte "etre a la maison" (PC + TV) :** jours absents des 2 (10-12/07, `[2] en [CELL]`)
= 0,85-0,97 kWh/j vs jours presents = 2,5-6,6 kWh/j -> +2 a 3 kWh/j quand quelqu'un est la.

**Corrections de conclusions (v1 du bilan) :**
- Aout : Multi +47 % (4,87 vs 3,32 kWh/j) EXPLIQUE par les vacances a la maison -
  pas une anomalie technique.
- Juin : moyenne 211 W faussee par le 15/06 (reset manque a minuit : compteur Multi
  reparti de 7,92 kWh au lieu de ~0, puis reset en cours de journee) ; hors incident
  ~90 W avec 4 nuits hautes = PC laisse allume, intermittent.
- Les jours calmes 10-12/07 (chauff ~2 kWh) = absence des 2 ([2] en [CELL]), pas un G1 partiel.

**Croisement DUT x presence (juillet) :** jours absents des 2 (10-12/07, [2] en [CELL]) :
Salon 1,0-3,2 h, Bureau 1,4-4,2 h, Chambre 0,2-2,0 h vs moyennes juillet (S 9,31 /
B 8,69 / C 2,98 h) -> Salon -80 a -90 %, Bureau -80 %, Chambre -50 a -90 %. Le mode
absence coupe quasi tout - les 1-2 kWh residuels = maintien minimal ou retour en cours
de journee.

---

## 10. EFFICACITE ETE (kWh clim / C d'ecart int-ext, valeur absolue)

| Mois | kWh/C | Clim moy | Ecart moy | Ti / Text |
|:---|:---|:---|:---|:---|
| Juin | 2,81 | 7,9 kWh/j | 3,3 C | 26,5 / 29,6 |
| Juil | 3,84 | 8,2 kWh/j | 2,5 C | 26,9 / 29,4 |
| Aout | 3,75 | 10,5 kWh/j | 2,9 C | 26,9 / 29,8 |

Reference hiver (janvier) : ~0,8 kWh/C a 10-12 C d'ecart.

**Lecture : l'ete coute ~4x plus par degre d'ecart que l'hiver (3,8 vs 0,8 kWh/C).**
Causes probables :
1. Charge thermique additionnelle : apports solaires qui entrent par le vitrage simple
   AVANT d'etre bloques par le store interieur + PC (~380 W cumules Eric + Mamour)
   + TV 180 W le soir (20h30-23h30, ~0,5 kWh/j - soit ~355 W d'apports internes dans
   le salon pendant le pic de 19h-22h) + chaleur du salon transferee au Bureau par la
   cloison carreau de platre (mur mitoyen 40 %).
2. Bati qui emmagasine : Ti reste a 26,5-26,9 C la nuit malgre la clim (inertie +
   Text nocturne 26-27 C).
3. EER des appareils < COP (surtout le Hitachi 2008 du Salon).

---

## 11. PROFIL HORAIRE CLIM AOUT (deltas Chauff, 10 j - 97,8 kWh)

| Tranche | kWh/h typique | Lecture |
|:---|:---|:---|
| 00h-03h | 3,7-5,4 | la nuit ne refroidit pas, la clim continue (Text 26-27 C) |
| 05h-09h | 2,0-3,1 | creux relatif (minimum du cycle) |
| 12h-17h | 4,5-5,0 | plateau journee (soleil + PC) |
| 19h-22h | 5,1-5,7 | PIC soiree : chaleur accumulee par le bati |

La clim tourne 24h/24 en canicule. Part HC reelle (01h30-07h30 + 13h-14h30) : 27 % -
le bloc 22h-01h30 represente ~17 kWh sur les 10 j, FACTURE EN HP avec vos plages.
Avec une fenetre HC nuit qui demarre a 01h30, le decalage nocturne ne profite qu'au
creux relatif du petit matin - peu de marge supplementaire.

---

## 12. PROJECTION ANNUELLE (fourchette, extrapolation lineaire des jours dispo)

| Mois | Donnees | Jours | Extrapolation |
|:---|:---|:---|:---|
| Janv | 397,2 (29 j) | 31 | complet |
| Fevr | 151,5 (10 j) | 28 | ~424 |
| Mars | absent des logs | 31 | ~200-250 (estime sur avr/mai) |
| Avr | 151,9 (21 j) | 30 | ~217 |
| Mai | 162,7 (22 j) | 31 | ~229 |
| Juin | 327,6 (30 j) | 30 | complet |
| Juil | 443,8 (31 j) | 31 | complet |
| Aout | 182,8 (10 j) | 31 | ~434 a 567 (fin de canicule incertaine) |

**Total estime : ~2 700 a 2 830 kWh/an** -> ~540 a 565 EUR/an d'energie (mix 0,20)
+ abonnement 15,86 x 12 = 190 EUR -> **~730 a 755 EUR/an TTC**.

Fragilite : fevrier (10 j) et aout (canicule en cours - le 10/08 a 27 C suggere une
accalmie, la projection basse est plus probable).

---

## SYNTHESE

1. Le rapport du 19/07 tenait sur l'hiver (DUT valides a l'identique) mais sous-evaluait
   tout l'ete : juin et juillet sont des mois complets et l'ete DEPASSE l'hiver
   (Juil 443,8 > Janv 397,2 kWh).
2. Trois dossiers ouverts : A1 (auto B - deja dans TODO P1-CUISINE-B, a verifier avant
   l'hiver), A3 (PC la nuit, intermittent - juin/aout, en partie explique par les
   vacances), clim du Bureau en canicule (PC Eric + simple vitrage).
3. Tarif : HPHC CONFIRME et VERIFIE (grille EDF 01/08/2026 : HP 0,2142 / HC 0,1589 EUR).
   Mix reel mesure avec les fenetres HC (nuit 01h30-07h30 + jour 13h-14h30) ~75/25 ->
   total periode ~364 EUR ; projection annuelle ~2 700-2 830 kWh
   (~730-755 EUR/an TTC avec abonnement).
4. Efficacite ete ~4x l'hiver par degre d'ecart (3,8 vs 0,8 kWh/C) : le levier n1 reste
   de bloquer les apports solaires AVANT le vitrage (store/toile exterieur, vitrage).

---

*Rapport genere par Hermes - Eric (BerrySwann) - 2026-08-10*
*Sources : diag_conso_elec.txt (13 958 lignes) + RAPPORT_AUDIT_ENERGETIQUE_2026-07-19.md*
*+ IA_AUDIT_ENERGETIQUE_ET_THERMIQUE.md v6.4 + skill ha-energy-thermal-analysis*
*Parseur : parse_diag_conso.py (6 variantes, suffixe DUT variable)*
