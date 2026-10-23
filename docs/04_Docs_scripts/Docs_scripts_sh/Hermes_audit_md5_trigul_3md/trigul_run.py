#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lanceur du trigul (etapes A, B1 et C) avec journal de trace.

Cree le 2026-10-18 a la demande d'Eric : voir ou le trigul plante le jour ou il plante.
Ne modifie aucun des 3 scripts : il les lance l'un apres l'autre, ecrit CHAQUE evenement
dans le journal (ouverture, ecriture, flush, fsync : une ligne n'est jamais perdue) et
verifie apres chaque script les plantages silencieux :
  - code de retour different de 0, Traceback dans la sortie, depassement de temps ;
  - rapport absent, vide, ou PAS mis a jour pendant ce lancement (un ancien rapport
    serait pris pour le nouveau) ;
  - marqueurs de fin absents du rapport (RESULTAT, controle du script : OK, ANOMALIES) ;
  - dossier temporaire du profond laisse derriere (signe d'un arret au milieu) ;
  - GitHub injoignable (le script 3 continue avec des colonnes '?').

Journal : historique/03_RAPPORTS/06_MD5/04_JOURNAL_TRIGUL/trigul_journal_AAAA-MM-JJ.log (un par jour, ajout).
Format : HH:MM:SS.mmm | NIVEAU | ETAPE | message. Niveaux : INFO, SORTIE, STDERR, NOTE,
OK, ATTENTION, ECHEC. Le journal doit finir par la ligne "FIN DU LANCEUR" : si elle manque,
le lanceur lui-meme a ete tue (PC eteint, session fermee) et la derniere ligne dit ou.

Usage :
    python -I trigul_run.py                      lance A, B1, C
    python -I trigul_run.py --note ETAPE texte   ajoute une ligne NOTE (etapes faites par Claude,
                                                 par exemple B2 categories HA)
Code de retour : 0 si aucune etape en ECHEC, 1 sinon. Lecture seule sur la documentation.
"""
import datetime
import os
import subprocess
import sys
import time
import traceback

ROOT = r'C:\Users\Berry Swann\Documents\ReBuild'
SH = os.path.join(ROOT, 'docs', '04_docs_scripts', 'docs_scripts_SH')
SH3 = os.path.join(ROOT, 'docs', '04_Docs_scripts', 'Docs_scripts_sh')
MD5 = os.path.join(ROOT, 'historique', '03_RAPPORTS', '06_MD5')
LOGDIR = os.path.join(MD5, '04_JOURNAL_TRIGUL')
TODAY = datetime.date.today().strftime('%Y-%m-%d')
LOG = os.path.join(LOGDIR, 'trigul_journal_%s.log' % TODAY)
TMP_PROFOND = os.path.join(ROOT, '_tmp_trigul_profond')

STEPS = [
    dict(name='A_arbres',
         script=os.path.join(SH, 'hermes_audit_md5_trigul_3md', 'hermes_audit_trigul_arbres.py'),
         reports=[os.path.join(MD5, '00_VERIF_FINAL_TRIGUL_ARBRES', 'trigul_arbres_%s.txt' % TODAY),
                  os.path.join(MD5, '00_VERIF_FINAL_TRIGUL_ARBRES', 'trigul_arbres_%s.html' % TODAY)],
         must=['RESULTAT :', 'controle du script : OK'], mustnot=['ERREURS DU SCRIPT'], needs_h=True),
    dict(name='B1_profond',
         script=os.path.join(SH, 'hermes_audit_md5_trigul_3md', 'hermes_audit_md5_trigul_unitaire.py'),
         reports=[os.path.join(MD5, '01_TRIGUL_PROFOND', 'trigul_profond_%s.txt' % TODAY)],
         must=['ETAPES : 1 -', 'AUTOMATIONS :', 'SCRIPTS :'], mustnot=[], needs_h=True, tmpdir=TMP_PROFOND, warn_out=['ATTENTION']),
    dict(name='C_emplacements',
         script=os.path.join(SH3, 'Verif_emplacements', 'Verif_emplacements.py'),
         reports=[os.path.join(MD5, '03_VERIF_EMPLACEMENTS', 'verif_emplacements_%s.txt' % TODAY)],
         must=['ANOMALIES', 'RESULTAT'], mustnot=[], needs_h=True, warn_out=['injoignable']),
]


def log(niveau, etape, msg):
    os.makedirs(LOGDIR, exist_ok=True)
    ligne = '%s | %-9s | %-14s | %s\n' % (datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3], niveau, etape, msg)
    with open(LOG, 'a', encoding='utf-8', newline='\n') as f:
        f.write(ligne)
        f.flush()
        os.fsync(f.fileno())
    try:
        sys.stdout.write(ligne.encode('ascii', 'replace').decode('ascii'))
    except Exception:
        pass


def lire(p):
    with open(p, 'rb') as f:
        return f.read().decode('utf-8', 'replace')


def run_step(st):
    name = st['name']
    start = time.time()
    log('INFO', name, 'DEBUT ' + st['script'])
    if not os.path.isfile(st['script']):
        log('ECHEC', name, 'script introuvable')
        return 'ECHEC'
    if st.get('needs_h') and not os.path.isdir('H:\\'):
        log('ECHEC', name, 'H: inaccessible : etape non lancee')
        return 'ECHEC'
    env = dict(os.environ)
    env['PYTHONIOENCODING'] = 'utf-8'
    verdict = 'OK'
    try:
        cp = subprocess.run([sys.executable, '-I', st['script']], capture_output=True,
                            timeout=st.get('timeout', 300), env=env, cwd=ROOT)
    except subprocess.TimeoutExpired:
        log('ECHEC', name, 'DEPASSEMENT DE TEMPS apres %ds : le script ne repond plus' % st.get('timeout', 300))
        return 'ECHEC'
    except Exception:
        log('ECHEC', name, 'lancement impossible : ' + traceback.format_exc().strip().splitlines()[-1])
        return 'ECHEC'
    out = cp.stdout.decode('utf-8', 'replace')
    err = cp.stderr.decode('utf-8', 'replace')
    log('INFO', name, 'FIN code de retour %d en %.1f s, %d lignes de sortie' % (cp.returncode, time.time() - start, len(out.splitlines())))
    for l in out.strip().splitlines()[-5:]:
        log('SORTIE', name, l[:200])
    for l in err.strip().splitlines()[:40]:
        log('STDERR', name, l[:200])
    if cp.returncode != 0:
        log('ECHEC', name, 'code de retour %d (0 attendu)' % cp.returncode)
        verdict = 'ECHEC'
    if 'Traceback (most recent call last)' in out or 'Traceback (most recent call last)' in err:
        log('ECHEC', name, 'Traceback Python dans la sortie')
        verdict = 'ECHEC'
    for p in st['reports']:
        if not os.path.isfile(p):
            log('ECHEC', name, 'rapport ABSENT : ' + p)
            verdict = 'ECHEC'
            continue
        taille = os.path.getsize(p)
        if taille == 0:
            log('ECHEC', name, 'rapport VIDE : ' + p)
            verdict = 'ECHEC'
        if os.path.getmtime(p) < start - 2:
            log('ECHEC', name, 'rapport NON MIS A JOUR pendant ce lancement (ancien rapport) : ' + p)
            verdict = 'ECHEC'
        else:
            log('INFO', name, 'rapport ecrit %d octets : %s' % (taille, p))
        if p.endswith('.txt') and taille:
            txt = lire(p)
            for m in st['must']:
                if m not in txt:
                    log('ECHEC', name, 'marqueur de fin absent du rapport : ' + m)
                    verdict = 'ECHEC'
            for m in st['mustnot']:
                if m in txt:
                    log('ECHEC', name, 'marqueur d erreur present dans le rapport : ' + m)
                    verdict = 'ECHEC'
    if st.get('tmpdir') and os.path.isdir(st['tmpdir']):
        log('ATTENTION', name, 'dossier temporaire laisse derriere (arret au milieu ?) : ' + st['tmpdir'])
        if verdict == 'OK':
            verdict = 'ATTENTION'
    for m in st.get('warn_out', []):
        if m in out:
            log('ATTENTION', name, 'la sortie contient "%s" : resultat partiel' % m)
            if verdict == 'OK':
                verdict = 'ATTENTION'
    log(verdict, name, 'verdict de l etape')
    return verdict


def main(argv):
    if len(argv) >= 3 and argv[1] == '--note':
        log('NOTE', argv[2], ' '.join(argv[3:]))
        return 0
    log('INFO', 'LANCEUR', 'DEBUT du trigul, python %s, journal %s' % (sys.version.split()[0], LOG))
    res = []
    try:
        if not os.path.isdir(ROOT):
            log('ECHEC', 'LANCEUR', 'dossier ReBuild introuvable : ' + ROOT)
            return 1
        log('INFO', 'LANCEUR', 'H: accessible : %s' % os.path.isdir('H:\\'))
        for st in STEPS:
            res.append((st['name'], run_step(st)))
    except Exception:
        log('ECHEC', 'LANCEUR', 'EXCEPTION : ' + traceback.format_exc().strip().replace('\n', ' // '))
        res.append(('LANCEUR', 'ECHEC'))
    for n, v in res:
        log(v, 'SYNTHESE', n)
    code = 1 if any(v == 'ECHEC' for _, v in res) else 0
    log('INFO', 'LANCEUR', 'FIN DU LANCEUR - code %d' % code)
    return code


if __name__ == '__main__':
    sys.exit(main(sys.argv))