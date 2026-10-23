# -*- coding: utf-8 -*-
r"""
Verif_integrations_file.py - controle EN LECTURE SEULE des integrations File (notify) de Home Assistant.
Fiche de reference : docs/01_docs_config_system/config_system_MD/integrations_file/integrations_file.md
Cree le 2026-10-23 a la demande d'Eric.

Compare les integrations File reellement presentes dans HA avec le tableau de la fiche :
  - /config/.storage/core.config_entries (H:\.storage\) : entrees du domaine "file" UNIQUEMENT
    (chemin du fichier, option horodatage, entree desactivee) ;
  - /config/.storage/core.entity_registry : entites de la plateforme "file" UNIQUEMENT (lien entree -> entite notify).
Ces deux fichiers contiennent des secrets d'autres integrations : seuls les champs utiles des entrees "file" sont lus
et ecrits dans le rapport. Aucune ecriture dans .storage.

Verdicts par ligne de la fiche : OK, MANQUANT DANS HA, ENTITE DIFFERENTE, HORODATAGE ACTIF, ENTREE DESACTIVEE.
Entrees de HA absentes de la fiche : EN TROP (ABSENTE DE LA FICHE).
Ecrit : historique/03_RAPPORTS/06_MD5/05_VERIF_INTEGRATIONS_FILE/verif_integrations_file_AAAA-MM-JJ.txt
(le rapport du jour existant est d'abord renomme en .bak_AAAA_MM_JJ_HHhMMmSSs.txt)
Codes retour : 0 rapport ecrit ; 2 prod H: inaccessible (rien ecrit) ; 3 fiche illisible (rien ecrit).
"""
import os, sys, json, re, datetime

REBUILD = r'C:\Users\Berry Swann\Documents\ReBuild'
STORAGE = 'H:\\.storage'
FICHE = os.path.join(REBUILD, 'docs', '01_docs_config_system', 'config_system_MD', 'integrations_file', 'integrations_file.md')
RAPPORT_DIR = os.path.join(REBUILD, 'historique', '03_RAPPORTS', '06_MD5', '05_VERIF_INTEGRATIONS_FILE')


def norm_path(p):
    """chemin complet sous /config : HA stocke parfois un chemin relatif (notifs/x.txt)"""
    p = (p or '').strip().replace('\\', '/')
    if not p.startswith('/'):
        p = '/config/' + p
    return p


def lire_json(nom):
    with open(os.path.join(STORAGE, nom), encoding='utf-8') as f:
        return json.load(f)


def lire_ha():
    """retourne (entrees, entites) du domaine/plateforme file uniquement"""
    cfg = lire_json('core.config_entries')['data']['entries']
    reg = lire_json('core.entity_registry')['data']['entities']
    entrees = {}
    for e in cfg:
        if e.get('domain') != 'file':
            continue
        entrees[e['entry_id']] = {
            'path': norm_path((e.get('data') or {}).get('file_path')),
            'timestamp': bool((e.get('options') or {}).get('timestamp')),
            'desactivee': e.get('disabled_by'),
            'entite': None,
        }
    for r in reg:
        if r.get('platform') == 'file' and r.get('config_entry_id') in entrees:
            entrees[r['config_entry_id']]['entite'] = r.get('entity_id')
    return entrees


def lire_fiche():
    """lignes du tableau : | `chemin` | `notify.x` | automation | horodatage |"""
    lignes = []
    with open(FICHE, encoding='utf-8') as f:
        for ln in f:
            if not ln.startswith('| `/'):
                continue
            cols = [c.strip() for c in ln.strip().strip('|').split('|')]
            if len(cols) < 4:
                continue
            lignes.append({'path': norm_path(cols[0].strip('`')),
                           'entite': cols[1].strip('`'),
                           'horodatage': cols[3].strip().lower()})
    return lignes


def main():
    maintenant = datetime.datetime.now()
    try:
        entrees = lire_ha()
    except Exception as e:
        print('ERREUR : prod H: / .storage inaccessible (%s)' % type(e).__name__)
        return 2
    try:
        fiche = lire_fiche()
        if not fiche:
            raise ValueError('aucune ligne de tableau')
    except Exception as e:
        print('ERREUR : fiche illisible (%s)' % e)
        return 3

    par_chemin = {}
    for eid, e in entrees.items():
        par_chemin.setdefault(e['path'], []).append((eid, e))

    out = []
    anomalies = 0
    out.append('VERIF_INTEGRATIONS_FILE - %s' % maintenant.strftime('%Y-%m-%d %H:%M:%S'))
    out.append('Fiche : %d lignes | HA : %d entrees File' % (len(fiche), len(entrees)))
    out.append('')
    out.append('1. Lignes de la fiche')
    vus = set()
    for l in fiche:
        trouvees = par_chemin.get(l['path'], [])
        if not trouvees:
            verdict = 'MANQUANT DANS HA'
            anomalies += 1
        else:
            eid, e = trouvees[0]
            vus.add(eid)
            if e['desactivee']:
                verdict = 'ENTREE DESACTIVEE'
                anomalies += 1
            elif e['entite'] != l['entite']:
                verdict = 'ENTITE DIFFERENTE (HA : %s)' % e['entite']
                anomalies += 1
            elif e['timestamp'] or l['horodatage'] != 'non':
                verdict = 'HORODATAGE ACTIF (HA : %s, fiche : %s)' % ('oui' if e['timestamp'] else 'non', l['horodatage'])
                anomalies += 1
            else:
                verdict = 'OK'
        out.append('  %-45s %-32s %s' % (l['path'], l['entite'], verdict))
    out.append('')
    out.append('2. Entrees de HA absentes de la fiche')
    en_trop = [(eid, e) for eid, e in entrees.items() if eid not in vus]
    if not en_trop:
        out.append('  aucune')
    for eid, e in en_trop:
        anomalies += 1
        out.append('  %-45s %-32s EN TROP (ABSENTE DE LA FICHE)' % (e['path'], e['entite']))
    out.append('')
    out.append('ANOMALIES : %d' % anomalies)
    out.append('RESULTAT : %s' % ('OK' if anomalies == 0 else 'ECART'))

    os.makedirs(RAPPORT_DIR, exist_ok=True)
    rapport = os.path.join(RAPPORT_DIR, 'verif_integrations_file_%s.txt' % maintenant.strftime('%Y-%m-%d'))
    if os.path.exists(rapport):
        bak = rapport[:-4] + '.bak_%s.txt' % maintenant.strftime('%Y_%m_%d_%Hh%Mm%Ss')
        os.rename(rapport, bak)
    with open(rapport, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    print('\n'.join(out))
    print('Rapport : ' + rapport)
    return 0


if __name__ == '__main__':
    sys.exit(main())