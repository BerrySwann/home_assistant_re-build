#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Journal de trace commun a /histo et /histo-final (cree le 2026-10-19 a la demande d'Eric).

But : voir ou une sequence histo s'arrete ou plante en silence, et garder la trace de chaque
validation demandee a Eric. Chaque evenement est ecrit sur disque tout de suite (flush + fsync).

Journal brut : historique/01_journal_trace/logs/histo_trace_AAAA-MM-JJ.log (un par jour, ajout). Dossier renomme
par Eric le 2026-10-21 pour etre en haut de historique/ ; les pages HTML sont directement dans 01_journal_trace.
Format : HH:MM:SS.mmm | NIVEAU | ETAPE | message
Niveaux : SEQ_DEBUT, SEQ_FIN, DEBUT, FIN, VALIDATION, NOTE.
Pour FIN, le statut est dans le message : OK, ATTENTION ou ECHEC (ex : "OK ..." ).

Usage (Claude l'appelle autour de chaque etape de /histo et /histo-final) :
  python -I histo_trace.py seq-debut histo|histo-final
  python -I histo_trace.py debut ETAPE [texte]
  python -I histo_trace.py fin ETAPE OK|ATTENTION|ECHEC [texte]
  python -I histo_trace.py validation ETAPE texte   (une validation a ete demandee a Eric)
  python -I histo_trace.py note ETAPE texte
  python -I histo_trace.py seq-fin
  python -I histo_trace.py verifier                 (lit le journal du jour, code 1 si anomalie)
  python -I histo_trace.py recap [AAAA-MM-JJ]       (horodatage des taches de la derniere sequence du jour)
  python -I histo_trace.py html [AAAA-MM-JJ|tout]   (page HTML du journal du jour, d'un jour, ou de tous les jours)
Verifier signale : sequence sans SEQ_FIN (PC eteint, session fermee, plantage), etape DEBUT sans
FIN (blocage silencieux), etapes ECHEC ou ATTENTION, validations demandees.
Recap (demande par Eric le 2026-10-21) : une ligne par tache (= chaque DEBUT), heure de debut de la
tache 1, puis pour chaque tache suivante la duree de la tache precedente et son heure de debut ; derniere
ligne : fin de sequence, duree de la derniere tache et duree totale. Heures lues dans le journal.
Variable HISTO_TRACE_DIR : remplace le dossier 01_journal_trace (essais seulement).
Html (demande par Eric le 2026-10-21) : ecrit historique/01_journal_trace/histo_trace_AAAA-MM-JJ.html (un par jour,
sombre, toutes les sequences du jour, duree de chaque tache, resultat de la ligne FIN, notes) et index.html. Si la page
du jour existe deja avec un contenu different, elle est d'abord copiee en histo_trace_AAAA-MM-JJ.bak_AAAA_MM_JJ_HHhMMmSSs.html
(10 au maximum le meme jour, menage fait par /histo, famille F). Page identique : rien n'est ecrit.
index.html est refait a partir des pages HTML presentes, meme si le .log d'un jour a ete supprime.
Aucun secret dans les messages. Ne touche a aucun autre fichier que ces journaux et leurs pages HTML.
"""
import datetime
import html as _html
import os
import re
import shutil
import sys

ROOT = r'C:\Users\Berry Swann\Documents\ReBuild'
JOURNALDIR = os.environ.get('HISTO_TRACE_DIR') or os.path.join(ROOT, 'historique', '01_journal_trace')
LOGDIR = os.path.join(JOURNALDIR, 'LOGS')


def chemin():
    return os.path.join(LOGDIR, 'histo_trace_%s.log' % datetime.date.today().strftime('%Y-%m-%d'))


def ecrire(niveau, etape, msg):
    os.makedirs(LOGDIR, exist_ok=True)
    ligne = '%s | %-10s | %-18s | %s\n' % (datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3],
                                         niveau, etape, msg.replace('\n', ' ').replace('\r', ' '))
    with open(chemin(), 'a', encoding='utf-8', newline='\n') as f:
        f.write(ligne)
        f.flush()
        os.fsync(f.fileno())
    sys.stdout.write(ligne.encode('ascii', 'replace').decode('ascii'))

def lire():
    p = chemin()
    if not os.path.isfile(p):
        return []
    with open(p, 'rb') as f:
        return f.read().decode('utf-8', 'replace').splitlines()


def verifier():
    lignes = lire()
    if not lignes:
        print('JOURNAL ABSENT OU VIDE : ' + chemin())
        return 1
    anomalies = 0
    seq = None
    ouvertes = {}
    for l in lignes:
        parts = [x.strip() for x in l.split('|', 3)]
        if len(parts) < 4:
            continue
        heure, niv, etape, msg = parts
        if niv == 'SEQ_DEBUT':
            if seq is not None:
                print('ANOMALIE : sequence %s (%s) sans SEQ_FIN, interrompue avant %s' % (seq[1], seq[0], heure))
                anomalies += 1
            seq, ouvertes = (heure, msg), {}
        elif niv == 'SEQ_FIN':
            seq = None
        elif niv == 'DEBUT':
            ouvertes[etape] = heure
        elif niv == 'FIN':
            ouvertes.pop(etape, None)
            if msg.startswith('ECHEC') or msg.startswith('ATTENTION'):
                print('%s : %s a %s : %s' % (msg.split()[0], etape, heure, msg))
                anomalies += 1
        elif niv == 'VALIDATION':
            print('VALIDATION demandee a %s : %s : %s' % (heure, etape, msg))
    for e, h in ouvertes.items():
        print('ANOMALIE : etape %s commencee a %s sans FIN (blocage ou plantage silencieux)' % (e, h))
        anomalies += 1
    if seq is not None:
        print('ANOMALIE : sequence %s (%s) sans SEQ_FIN : derniere ligne = %s' % (seq[1], seq[0], lignes[-1]))
        anomalies += 1
    print('RESULTAT : %s' % ('aucune anomalie' if anomalies == 0 else '%d anomalie(s)' % anomalies))
    return 1 if anomalies else 0


def _duree(s):
    s = int(round(s))
    return '%d min %02d s' % (s // 60, s % 60) if s >= 60 else '%d s' % s


def _sec(h):
    hh, mm, ss = h.split(':')
    return int(hh) * 3600 + int(mm) * 60 + float(ss)


def recap(jour=None):
    """Horodatage des taches de la derniere sequence du journal (du jour ou de AAAA-MM-JJ)."""
    p = chemin() if not jour else os.path.join(LOGDIR, 'histo_trace_%s.log' % jour)
    if not os.path.isfile(p):
        print('JOURNAL ABSENT : ' + p)
        return 1
    with open(p, 'rb') as f:
        lignes = f.read().decode('utf-8', 'replace').splitlines()
    ev = []
    for l in lignes:
        parts = [x.strip() for x in l.split('|', 3)]
        if len(parts) == 4:
            ev.append(parts)
    debut = [i for i, e in enumerate(ev) if e[1] == 'SEQ_DEBUT']
    if not debut:
        print('AUCUNE SEQUENCE dans ' + p)
        return 1
    ev = ev[debut[-1]:]
    taches = [(e[2], e[0]) for e in ev if e[1] == 'DEBUT']
    fin = [e[0] for e in ev if e[1] == 'SEQ_FIN']
    if not taches:
        print('AUCUNE TACHE dans la derniere sequence')
        return 1
    print('sequence %s, debut %s' % (ev[0][3], ev[0][0][:8]))
    for n, (nom, h) in enumerate(taches, 1):
        if n == 1:
            print('- tache 1 (%s) : debut %s' % (nom, h[:8]))
        else:
            d = _sec(h) - _sec(taches[n - 2][1])
            print('- tache %d (%s) : ( tache %d -> %s ) - debut %s' % (n, nom, n - 1, _duree(d), h[:8]))
    if fin:
        d = _sec(fin[0]) - _sec(taches[-1][1])
        print('- fin de sequence : ( tache %d -> %s ) - %s' % (len(taches), _duree(d), fin[0][:8]))
        print('duree totale : %s' % _duree(_sec(fin[0]) - _sec(taches[0][1])))
    else:
        print('fin de sequence : absente (sequence ouverte ou interrompue)')
    return 0


CSS = """body{font-family:system-ui,Arial,sans-serif;margin:0 auto;padding:20px 16px;max-width:1000px;background:#12181b;color:#e4eaed;font-size:15px;line-height:1.5}
h2{margin:0 0 4px}h3{margin:28px 0 4px}p{color:#93a3ab;margin:4px 0}a{color:#4fb8c9}table{border-collapse:collapse;width:100%;background:#1a2226;border:1px solid #2c383d}
th,td{padding:6px 8px;border-bottom:1px solid #2c383d;text-align:left;vertical-align:top}th{color:#93a3ab;font-weight:500;font-size:.8rem}
.b{background:#4fb8c9;height:6px;border-radius:3px;min-width:1px;margin-top:3px}.t{margin-top:10px;font-size:17px;font-weight:bold;color:#e4eaed}
.st{font-weight:600;font-size:.8rem}.ok{color:#5fc07f}.warn{color:#e0a23a}.crit{color:#ef6f5b}.nt{color:#93a3ab;font-size:.85rem}.de{color:#93a3ab;font-size:.85rem}
td:nth-child(3),td:nth-child(4){white-space:nowrap}"""


def _tete(titre):
    return ('<!doctype html><html lang="fr"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title><style>%s</style></head><body>\n'
            % (_html.escape(titre), CSS))


def _sequences(lignes):
    seqs, cur = [], None
    for l in lignes:
        p = [x.strip() for x in l.split('|', 3)]
        if len(p) < 4:
            continue
        t, lv, etape, txt = p
        if lv == 'SEQ_DEBUT':
            cur = {'nom': txt, 'debut': t, 'fin': None, 'ev': []}
            seqs.append(cur)
            continue
        if cur is None:
            cur = {'nom': '(sans debut de sequence)', 'debut': t, 'fin': None, 'ev': []}
            seqs.append(cur)
        if lv == 'SEQ_FIN':
            cur['fin'] = t
            continue
        cur['ev'].append((t, lv, etape, txt))
    return seqs


def _taches(seq):
    taches = []

    def nouvelle(etape, debut, texte):
        tk = {'etape': etape, 'debut': debut, 'texte': texte, 'res': '', 'notes': []}
        taches.append(tk)
        return tk

    for t, lv, etape, txt in seq['ev']:
        if lv == 'DEBUT':
            nouvelle(etape, t, txt)
        elif lv == 'FIN':
            tk = next((x for x in reversed(taches) if x['etape'] == etape and not x['res']), None)
            if tk is None:
                tk = nouvelle(etape, None, '')
            tk['res'] = txt
        else:
            tk = next((x for x in reversed(taches) if x['etape'] == etape), None)
            if tk is None:
                tk = nouvelle(etape, None, '')
            tk['notes'].append('%s : %s' % (lv.lower(), txt))
    return taches


def rendre_jour(jour, fichier):
    """Retourne (page, nb_sequences, nb_taches, nb_a_voir). Contenu deterministe (pas d'heure de generation)."""
    with open(fichier, 'rb') as f:
        lignes = f.read().decode('utf-8', 'replace').splitlines()
    seqs = _sequences(lignes)
    corps = ''
    nb_t = a_voir = 0
    for i, s in enumerate(seqs, 1):
        taches = _taches(s)
        durs = []
        for k, tk in enumerate(taches):
            d = None
            if tk['debut']:
                suiv = next((x['debut'] for x in taches[k + 1:] if x['debut']), None) or s['fin']
                if suiv:
                    d = _sec(suiv) - _sec(tk['debut'])
            durs.append(d)
        mx = max([d for d in durs if d is not None] + [1])
        rows = ''
        for n, (tk, d) in enumerate(zip(taches, durs), 1):
            statut, _, msg = tk['res'].partition(' ')
            cls = {'OK': 'ok', 'ATTENTION': 'warn', 'ECHEC': 'crit'}.get(statut, '')
            if not tk['res']:
                statut, msg, cls = ('sans fin', '', 'crit') if tk['debut'] else ('-', '', '')
            elif not cls:
                statut, msg = '-', tk['res']
            if cls in ('warn', 'crit'):
                a_voir += 1
            notes = ''.join('<div class="nt">%s</div>' % _html.escape(x) for x in tk['notes'])
            desc = '<div class="de">%s</div>' % _html.escape(tk['texte']) if tk['texte'] else ''
            barre = '<div class="b" style="width:%d%%"></div>' % int(100 * d / mx) if d is not None else ''
            rows += ('<tr><td>%d</td><td>%s%s</td><td>%s</td><td>%s%s</td><td><span class="st %s">%s</span> %s%s</td></tr>\n'
                     % (n, _html.escape(tk['etape']), desc, (tk['debut'] or '-')[:8],
                        _duree(d) if d is not None else '-', barre, cls, _html.escape(statut), _html.escape(msg), notes))
        nb_t += len(taches)
        if s['fin']:
            total = 'Duree totale : ' + _duree(_sec(s['fin']) - _sec(s['debut']))
        else:
            total = 'Sequence sans fin (interrompue ou en cours) : pas de duree totale'
            a_voir += 1
        corps += ('<h3>Sequence %d - %s</h3><p>Debut %s - fin %s</p>'
                  '<table><tr><th>Tache</th><th>Nom</th><th>Debut</th><th>Duree de la tache</th><th>Resultat</th></tr>\n%s</table>'
                  '<p class="t">%s</p>\n' % (i, _html.escape(s['nom']), s['debut'][:8], (s['fin'] or '-')[:8], rows, _html.escape(total)))
    page = (_tete('Journal de trace ' + jour) + '<h2>Journal de trace du %s</h2><p><a href="index.html">Retour a la liste</a></p>\n%s'
            "<p style=\"font-size:12px\">Duree d'une tache = debut de la tache suivante moins son debut (pour la derniere, fin de sequence). "
            'Resultat = ligne FIN du journal. Source : %s</p></body></html>\n' % (jour, corps, _html.escape(os.path.basename(fichier))))
    return page, len(seqs), nb_t, a_voir


def _ecrire_html(chemin_html, page, avec_bak=True):
    donnees = page.encode('utf-8')
    etat = 'cree'
    if os.path.isfile(chemin_html):
        with open(chemin_html, 'rb') as f:
            if f.read() == donnees:
                return 'inchange'
        etat = 'mis a jour'
        if avec_bak:
            bak = '%s.bak_%s.html' % (os.path.splitext(chemin_html)[0], datetime.datetime.now().strftime('%Y_%m_%d_%Hh%Mm%Ss'))
            shutil.copy2(chemin_html, bak)
            etat += ' (bak ' + os.path.basename(bak) + ')'
    with open(chemin_html, 'wb') as f:
        f.write(donnees)
    return etat


def _stats_html(chemin_html):
    """Compte sequences, taches et points a voir dans une page HTML deja ecrite (pour index.html)."""
    with open(chemin_html, 'rb') as f:
        t = f.read().decode('utf-8', 'replace')
    return (t.count('<h3>'), len(re.findall(r'<tr><td>\d+</td>', t)),
            len(re.findall(r'class=.?st (?:warn|crit)', t)) + t.count('Sequence sans fin'))


def html_cmd(arg=None):
    """Pages HTML des journaux : `html` (jour courant), `html AAAA-MM-JJ`, `html tout`. Regenere toujours index.html."""
    jours = {}
    if os.path.isdir(LOGDIR):
        for nom in sorted(os.listdir(LOGDIR)):
            m = re.match(r'^histo_trace_(\d{4}-\d{2}-\d{2})\.log$', nom)
            if m:
                jours[m.group(1)] = os.path.join(LOGDIR, nom)
    if arg == 'tout':
        cibles = list(jours)
        if not jours:
            print('AUCUN .log dans ' + LOGDIR + ' : pages HTML existantes gardees, seul index.html est refait')
    else:
        j = arg or datetime.date.today().strftime('%Y-%m-%d')
        if j not in jours:
            print('JOURNAL ABSENT : ' + os.path.join(LOGDIR, 'histo_trace_%s.log' % j))
            return 1
        cibles = [j]
    os.makedirs(JOURNALDIR, exist_ok=True)
    for j in cibles:
        page = rendre_jour(j, jours[j])[0]
        print('histo_trace_%s.html : %s' % (j, _ecrire_html(os.path.join(JOURNALDIR, 'histo_trace_%s.html' % j), page)))
    index = []
    for nom in sorted(os.listdir(JOURNALDIR)):
        m = re.match(r'^histo_trace_(\d{4}-\d{2}-\d{2})\.html$', nom)
        if m:
            index.append((m.group(1),) + _stats_html(os.path.join(JOURNALDIR, nom)))
    lst = ''.join('<tr><td><a href="histo_trace_%s.html">%s</a></td><td>%d</td><td>%d</td><td>%s</td></tr>\n'
                  % (j, j, ns, nt, '%d a voir' % av if av else 'rien') for j, ns, nt, av in reversed(index))
    idx = (_tete('Journaux de trace') + '<h2>Journaux de trace</h2>\n<table><tr><th>Jour</th><th>Sequences</th><th>Taches</th>'
           '<th>ATTENTION / ECHEC / sans fin</th></tr>\n' + lst + '</table></body></html>\n')
    print('index.html : ' + _ecrire_html(os.path.join(JOURNALDIR, 'index.html'), idx, avec_bak=False))
    return 0


def main(a):
    if not a:
        print(__doc__)
        return 2
    c, r = a[0], a[1:]
    if c == 'seq-debut' and r:
        ecrire('SEQ_DEBUT', 'SEQUENCE', r[0])
    elif c == 'seq-fin':
        ecrire('SEQ_FIN', 'SEQUENCE', 'fin de sequence')
    elif c == 'debut' and r:
        ecrire('DEBUT', r[0], ' '.join(r[1:]))
    elif c == 'fin' and len(r) >= 2 and r[1] in ('OK', 'ATTENTION', 'ECHEC'):
        ecrire('FIN', r[0], ' '.join(r[1:]))
    elif c == 'validation' and len(r) >= 2:
        ecrire('VALIDATION', r[0], ' '.join(r[1:]))
    elif c == 'note' and len(r) >= 2:
        ecrire('NOTE', r[0], ' '.join(r[1:]))
    elif c == 'verifier':
        return verifier()
    elif c == 'recap':
        return recap(r[0] if r else None)
    elif c == 'html':
        return html_cmd(r[0] if r else None)
    else:
        print('commande inconnue ou arguments manquants')
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))