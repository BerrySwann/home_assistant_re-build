# Push_5C.py - push general de l etape 5C de /histo (docs vers H:\docs). Modes : plan (lecture seule, defaut) | exec.
# Fiche : docs\04_docs_scripts\04_docs_scripts_SH_MD\Push_5C\Push_5C.md . Interpreteur : python -I -X utf8
# annotations_log:
# [2026-11-04] regle des garde-fous d Eric (2026-11-03) : avant chaque ecrasement, l ancienne prod est copiee dans
#   TEMPO\push_5C_L_vers_P_<horodatage>\ (MD5 verifie contre la prod) ; une PROD INCONNUE est poussee quand meme
#   (avertissement, plus un refus) ; un fichier SEUL EN PROD n arrete plus le push : il est signale, jamais supprime
#   sans ordre d Eric.
# [2026-11-04] purge validee par Eric (19h57, alignement sur Hermes) : en mode exec, les dossiers
#   TEMPO\push_5C_L_vers_P_* de plus de 7 jours (date lue dans le nom) partent a la corbeille Windows, jamais supprimes.
import os, hashlib, glob, re, sys, shutil, datetime
L=r"C:\Users\Berry Swann\Documents\ReBuild\docs"; P=r"H:\docs"
TEMPO=r"C:\Users\Berry Swann\Documents\ReBuild\TEMPO"; PFX="push_5C_L_vers_P_"; JOURS_PURGE=7
T=os.path.join(TEMPO,PFX+datetime.datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss"))
MODE=sys.argv[1] if len(sys.argv)>1 else "plan"
def skip(rel):
    parts=rel.split("\\")
    if rel=="99_docs_MD_system\\ENTITES_GLOBAL_INDEX\\ENTITES_GLOBAL_INDEX.md": return False  # exception Eric 2026-10-31 17h33
    if any(p.startswith("XX_") or p=="99_docs_MD_system" for p in parts[:-1]): return True
    n=parts[-1]
    if rel.startswith("98_sauvegarde_hors_docs\\Infra_Proxmox\\") and ".bak" in n: return False  # .bak d Infra_Proxmox gardes (Eric 2026-10-31)
    if ".bak" in n or n=="secrets.yaml" or n.endswith(".pyc") or (n.startswith("#") and n.endswith("#")): return True
    if "__pycache__" in parts or "Dashboard_COMPLET" in parts: return True
    if any(("ARCHIVE" in p.upper() and p.upper().startswith(("_ARCHIVE","ARCHIVE"))) or "_archive_" in p.lower() for p in parts): return True
    return False
def walk(root):
    out={}
    for d,ds,fs in os.walk(root):
        for f in fs:
            full=os.path.join(d,f); out[os.path.relpath(full,root)]=full
    return out
def md5(p):
    h=hashlib.md5()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()
def strip(p):
    t=open(p,"rb").read().decode("utf-8","replace").replace("\r\n","\n")
    t=re.sub(r'<div align="center">.*?</div>\n*','',t,count=1,flags=re.S)
    return hashlib.md5(t.encode()).hexdigest()
if MODE=="exec":
    import subprocess
    _s=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"Sync_98_sauvegarde","Sync_98_sauvegarde.py")
    print("sync 98 :",subprocess.run([sys.executable,"-I","-X","utf8",_s,"exec"],capture_output=True,text=True).stdout.strip().splitlines()[0])
loc={r:p for r,p in walk(L).items() if not skip(r)}
prod={r:p for r,p in walk(P).items() if not skip(r)}
new=[];diff=[];same=0
for r,p in loc.items():
    if r not in prod: new.append(r)
    elif os.path.getsize(p)==os.path.getsize(prod[r]) and md5(p)==md5(prod[r]): same+=1
    else: diff.append(r)
only=[r for r in prod if r not in loc]
connu=[];inconnu=[]
for r in diff:
    if r.startswith("98_sauvegarde_hors_docs\\"): connu.append(r); continue  # copie derivee de Sync_98 : la source locale fait foi
    lp=loc[r]; h=strip(prod[r]); d,n=os.path.split(lp); stem,ext=os.path.splitext(n)
    cands=glob.glob(os.path.join(d,stem+".bak*"))+glob.glob(os.path.join(d,n+".bak*"))
    (connu if any(strip(b)==h for b in cands) else inconnu).append(r)
print("local=%d prod=%d identiques=%d NOUVEAU=%d DIFF=%d (connus %d, INCONNUS %d) SEUL_EN_PROD=%d"%(len(loc),len(prod),same,len(new),len(diff),len(connu),len(inconnu),len(only)))
print("-- SEUL_EN_PROD (jamais supprime sans ordre d Eric, ne bloque pas le push):"); [print("  ",r) for r in sorted(only)]
print("-- DIFF INCONNUS (prod modifiee hors circuit : poussee quand meme, ancienne prod copiee dans TEMPO):"); [print("  ",r) for r in inconnu]
print("-- NOUVEAU (dossiers):")
g={}
for r in new: k="\\".join(r.split("\\")[:2]); g[k]=g.get(k,0)+1
[print("  %4d %s"%(v,k)) for k,v in sorted(g.items())]
def a_purger():
    lim=datetime.date.today()-datetime.timedelta(days=JOURS_PURGE); out=[]
    for n in sorted(os.listdir(TEMPO)) if os.path.isdir(TEMPO) else []:
        if not n.startswith(PFX) or not os.path.isdir(os.path.join(TEMPO,n)): continue
        try: d=datetime.datetime.strptime(n[len(PFX):len(PFX)+10],"%Y-%m-%d").date()
        except ValueError: continue
        if d<lim: out.append(n)
    return out
vieux=a_purger()
print("-- TEMPO copies de securite de plus de %d jours (corbeille Windows en mode exec): %d"%(JOURS_PURGE,len(vieux))); [print("  ",n) for n in vieux]
if MODE!="exec": sys.exit(0)
# 1) copie de securite de l ancienne prod (DIFF connus et inconnus), MD5 verifie contre la prod d origine
sauve=[];ko_copie=[]
for r in connu+inconnu:
    dst=os.path.join(T,r); os.makedirs(os.path.dirname(dst),exist_ok=True); shutil.copy2(prod[r],dst)
    if md5(dst)==md5(prod[r]): sauve.append(r)
    else: ko_copie.append(r)
# 2) push NOUVEAU + DIFF dont la copie de securite est conforme
n=0;bad=[]
for r in new+sauve:
    src=loc[r]; dst=os.path.join(P,r); os.makedirs(os.path.dirname(dst),exist_ok=True); shutil.copyfile(src,dst)
    if md5(src)!=md5(dst): bad.append(r)
    n+=1
print("copie de securite TEMPO :",(T if sauve else "aucune"),"| fichiers copies :",len(sauve))
print("pousses:",n,"MD5 differents apres push:",len(bad)); [print("  KO",r) for r in bad]
print("PROD INCONNUE poussee (avertissement, ancienne prod dans TEMPO):",len([r for r in inconnu if r in sauve])); [print("  ",r) for r in inconnu if r in sauve]
print("non pousses (copie de securite non conforme):",len(ko_copie)); [print("  KO_COPIE",r) for r in ko_copie]
print("SEUL_EN_PROD non supprimes (a decider avec Eric):",len(only))
# 3) purge des copies de securite de plus de 7 jours : corbeille Windows, jamais de suppression definitive
import subprocess as _sp
purge_ok=0; purge_ko=[]
for n in vieux:
    cible=os.path.join(TEMPO,n)
    r=_sp.run(["powershell","-NoProfile","-Command","Add-Type -AssemblyName Microsoft.VisualBasic; [Microsoft.VisualBasic.FileIO.FileSystem]::DeleteDirectory($args[0],'OnlyErrorDialogs','SendToRecycleBin')",cible],capture_output=True,text=True)
    if r.returncode==0 and not os.path.exists(cible): purge_ok+=1
    else: purge_ko.append(n)
print("purge TEMPO (corbeille Windows):",purge_ok,"| echecs:",len(purge_ko)); [print("  KO_PURGE",n) for n in purge_ko]
sys.exit(1 if (bad or ko_copie) else 0)
