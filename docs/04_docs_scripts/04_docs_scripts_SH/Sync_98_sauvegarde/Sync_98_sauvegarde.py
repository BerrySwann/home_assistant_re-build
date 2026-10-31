# Sync_98_sauvegarde.py - copie Infra_Proxmox, TODO et historique (hors docs) vers docs\98_sauvegarde_hors_docs pour la prod/GitHub. Modes : plan (defaut) | exec
# Fiche : docs\04_docs_scripts\04_docs_scripts_SH_MD\Sync_98_sauvegarde\Sync_98_sauvegarde.md . Interpreteur : python -I -X utf8
import os,re,sys,hashlib
B=r"C:\Users\Berry Swann\Documents\ReBuild"
D=os.path.join(B,"docs","98_sauvegarde_hors_docs")
SRC=["Infra_Proxmox","TODO","historique"]
EXCLUS={r"Infra_Proxmox\docs\sonoff\SONOFF_STATUS_2026-05-23.md"}  # mot de passe en clair, decision Claude 2026-10-31, a valider par Eric
TXT=(".md",".html",".log",".txt",".csv",".tsv",".json",".js",".svg",".sh",".ps1",".py",".yaml",".yml")
MASK=re.compile(rb"ghp_[A-Za-z0-9]+|github_pat_[A-Za-z0-9_]+")
def ignore(n):
    return (".bak" in n or ".avant_" in n or ".racine_avant" in n or n=="secrets.yaml" or n.endswith(".pyc")
            or (n.startswith("#") and n.endswith("#")))
mode=sys.argv[1] if len(sys.argv)>1 else "plan"
new=chg=same=0; excl=[]; masked=[]
for s in SRC:
    for dp,dn,fn in os.walk(os.path.join(B,s)):
        dn[:]=[d for d in dn if d!="__pycache__"]
        for f in fn:
            if ignore(f): continue
            p=os.path.join(dp,f); rel=os.path.relpath(p,B)
            if rel in EXCLUS: excl.append(rel); continue
            data=open(p,"rb").read()
            if f.lower().endswith(TXT):
                m=MASK.sub(b"ghp_***",data)
                if m!=data: masked.append(rel); data=m
            dst=os.path.join(D,rel)
            if os.path.exists(dst):
                if hashlib.md5(open(dst,"rb").read()).digest()==hashlib.md5(data).digest(): same+=1; continue
                chg+=1
            else: new+=1
            if mode=="exec":
                os.makedirs(os.path.dirname(dst),exist_ok=True); open(dst,"wb").write(data)
print("mode=%s nouveaux=%d modifies=%d identiques=%d exclus=%d jetons_masques=%d"%(mode,new,chg,same,len(excl),len(masked)))
for e in excl: print("EXCLU",e)