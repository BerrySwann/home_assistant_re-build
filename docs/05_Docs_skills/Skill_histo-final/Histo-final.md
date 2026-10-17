---
name: histo-final
description: "Skill HA ReBuild - histo de fin de journee : lance le skill histo complet, puis, apres le rapport et sans confirmation, eteint les lumieres (3 Hue Play du bureau, apres avoir arrete Hue Sync) et arrete le PC. Declencher sur /histo-final, histo final, fin de journee, j'eteins tout, extinction des lumieres et du PC. En cours de journee, utiliser histo (courant)."
---

# Skill : /histo-final - histo complet, puis extinction des lumieres et arret du PC

## Objectif

Fin de journee : tout ce que fait /histo, puis extinction des lumieres et arret du PC en toute derniere action. A utiliser a la place de /histo quand Eric part. En cours de journee, utiliser /histo (histo courant).

## Regles

- La sequence est irreversible pour la session : l'arret du PC coupe la liaison avec Claude. Tout doit etre ecrit, copie et verifie AVANT. Aucun appel d'outil ne suit la commande d'arret.
- Aucune confirmation : Eric n'est plus devant l'ecran (decision du 2026-10-11). Le delai de 7 minutes (420 s) avant l'arret du PC est la seule marge d'annulation. L'arret de /histo reste valable : si le menage attend le go de l'utilisateur (premiere execution du menage sur un dossier, seule pause qui reste ; plus aucun seuil de nombre de fichiers depuis le 2026-10-15), /histo-final s'arrete la, n'eteint rien et le dit dans le rapport ; l'extinction n'a lieu qu'apres le menage execute.
- Pas d'extinction (ni lumieres ni PC) si une etape de /histo a echoue ou reste incomplete : le dire dans le rapport et laisser le PC allume.
- Les lumieres eteintes sont les 3 Hue Play du bureau : `light.hue_play_1_pc_bureau`, `light.hue_play_2_pc_bureau`, `light.hue_play_3_pc_bureau` (decision d'Eric le 2026-10-11, apres test : l'extinction par la prise `switch.ecran_p_c_3_play_hue` est abandonnee). Ne jamais couper cette prise : elle reste `on`. Ne jamais remplacer ces entites par d'autres de memoire.

## Etape 1 - Lancer /histo

Invoquer le skill `histo` (outil Skill) et suivre toutes ses etapes, dans l'ordre : journal, sync_index, journal fusionne, Obsidian, menage, export Dashboard, tree, rapport. Ne pas dupliquer son contenu ici.

## Etape 2 - Verifier que tout est ecrit

1. Le journal des modifs du jour (`historique\modifs\MODIFS_AAAA-MM-JJ_claude.md`) et sa copie `H:\docs\modifs\` ont le meme MD5.
2. Aucun script lance par Claude ne tourne encore (`Get-Process bash,python,powershell` : ne pas compter la session en cours). Sinon attendre sa fin.
3. La liste des taches est terminee ou ce qui reste est signale.
4. `GLOBAL_INDEX_REPO.md` : MD5 de la copie de travail = miroir `H:\docs\05_docs_MD_system\GLOBAL_INDEX_REPO\` = racine `H:\GLOBAL_INDEX_REPO.md` ; `DEPENDANCES_GLOBALES.md` : MD5 local = `H:\docs\05_docs_MD_system\DEPENDANCES_GLOBALES\DEPENDANCES_GLOBALES.md` (pushs faits par /histo, etape 2 de son skill, decides le 2026-10-14). Un ecart apres le push = etape incomplete : pas d'extinction. H: inaccessible : le noter sans bloquer, comme dans /histo.
5. Envoyer le rapport final de /histo a l'utilisateur AVANT l'extinction, avec la prochaine action pour la reprise.

## Etape 3 - Pas de confirmation

Aucune question : enchainer directement sur l'etape 4 si les conditions de l'etape 2 et des regles sont remplies.

## Etape 4 - Notification telephone, puis Hue Sync et lumieres

Avant toute extinction : envoyer une notification sur le telephone d'Eric avec le service Home Assistant `notify.mobile_app_eric` (outil `ha_call_service`, domain `notify`, service `mobile_app_eric`, wait false ; data : title `Fin de journee`, message `Ecran eteint dans 10 s, PC eteint a [HH:MM] (annulation : shutdown /a)`), ou HH:MM = heure actuelle + 7 min 10 s (delai de 420 s de la commande d'arret plus les 10 s d'attente). Releve du 2026-10-13 : notification 22:45:02, commande d'arret 22:46:02, soit environ 1 min entre les deux, donc l'arret effectif tombe environ 1 min apres l'heure annoncee. Delai passe de 300 s a 420 s sur demande d'Eric le 2026-10-14. Verifie le 2026-10-11 : ce service existe, c'est celui des automations d'Eric, et la notification est bien arrivee sur son telephone. Attendre 10 secondes, puis enchainer. L'outil `PushNotification` de Claude ne sert qu'en secours (il ne pousse sur le telephone que si Remote Control est connecte ; test du 2026-10-11 : rien recu). Si HA est injoignable, essayer `PushNotification`, sinon le noter dans le rapport et continuer sans bloquer.

Lumieres (3 Hue Play du bureau). Raison de l'ordre (test d'Eric et de Claude du 2026-10-11) : tant que Hue Sync diffuse (`mode: streaming` sur les Play), le pont Hue ignore `light.turn_off` envoye par HA (HA affiche `off`, les lampes restent allumees). Il faut donc d'abord arreter Hue Sync. Methode retenue (decision d'Eric le 2026-10-11, testee a 19:30) : couper le flux Entertainment par l'API du pont Hue, sans tuer le processus. Resultat du test : `stream.active` passe a `false` en moins de 2 s, les 3 Play repassent en `mode: normal`, `binary_sensor.moniteur_pc` passe `off`, et l'application HueSync, restee ouverte, n'a pas relance le flux pendant les 27 s d'observation. Procedure complete : `docs/06_docs_technique/01_pont_hue_hacking/01_pont_hue_hacking.md`. La cle API du pont n'est ecrite dans aucun fichier : elle est dans la variable d'environnement utilisateur Windows `HUE_BRIDGE_KEY`. Ne jamais l'afficher, ne jamais l'ecrire dans un journal, un rapport ou un fichier.

1. PowerShell sur le PC : `$k=[Environment]::GetEnvironmentVariable('HUE_BRIDGE_KEY','User'); Invoke-RestMethod -Method Put -Uri "http://10.32.154.206/api/$k/groups/4" -Body '{"stream":{"active":false}}' -ContentType 'application/json'`. Reponse attendue : `{"success":{"/groups/4/stream/active":false}}`. Relire ensuite `Invoke-RestMethod -Uri "http://10.32.154.206/api/$k/groups/4"` : `stream.active` doit valoir `false` (afficher seulement `.stream`, jamais l'URL ni `$k`). Si la variable est vide ou si l'appel echoue : secours, fermer le processus avec `Get-Process -Name HueSync -ErrorAction SilentlyContinue | Stop-Process -Force`, puis `Start-Sleep 2`, et le noter dans le rapport. Puis passer au point 2.
2. Attendre que les 3 Play soient en `mode: normal` ET que `binary_sensor.moniteur_pc` soit `off` (`ha_get_state` sur les 4 entites, toutes les 5 s, 30 s au maximum). Le `off` de `moniteur_pc` est necessaire : tant qu'il est `on`, l'automation `automation.bureau_forcer_play_on_si_pc_tourne` rallume les Play a 25 % des qu'elles passent `off`. Si la condition n'est pas atteinte apres 30 s, le noter dans le rapport et passer au point 4 sans eteindre les lampes.
3. `light.turn_off` sur les 3 entites (`ha_call_service`, domain `light`, entity_id `light.hue_play_1_pc_bureau,light.hue_play_2_pc_bureau,light.hue_play_3_pc_bureau`, wait false), attendre 4 a 5 s, relire l'etat : les 3 doivent etre `off`. Si une entite est absente ou `unavailable`, le noter dans le rapport et ne pas chercher d'autre entite.
4. En cas d'echec (lampe pas `off`, mode reste `streaming`), le noter dans le rapport et passer a l'etape 5 (le PC s'arrete quand meme ; l'etat physique des lampes est alors inconnu, le dire).

Ne pas toucher a `switch.ecran_p_c_3_play_hue` (la prise reste `on`).

## Etape 5 - Arret du PC

1. Ajouter au journal des modifs du jour la ligne `ACTION | PC | arret programme (histo-final)`, copier le journal sur `H:\docs\modifs\` et verifier le MD5. C'est la derniere ecriture.
2. Envoyer le message final a l'utilisateur : lumieres eteintes (ou non), arret du PC dans 7 minutes, annulation possible avec `shutdown /a`.
3. Dernier appel d'outil, PowerShell sur le PC : `shutdown.exe /s /t 420 /c "Fin de journee HA ReBuild (histo-final)"`. Ne rien lancer apres. Le delai de 420 secondes (7 minutes) est voulu par Eric (passe de 300 s a 420 s le 2026-10-14 ; 300 s etait voulu le 2026-10-11), a raccourcir si besoin.

## Rapport final

Le rapport de /histo, plus :

```
NOTIFICATION : HA notify.mobile_app_eric envoyee a [HH:MM:SS] | secours PushNotification | non envoyee
LUMIERES : Hue Sync coupe (API pont) + 3 Hue Play off confirme | Hue Sync coupe par secours (processus) + 3 Hue Play off confirme | echec (detail) | non demande
PC : arret programme a [HH:MM:SS] | non demande
```