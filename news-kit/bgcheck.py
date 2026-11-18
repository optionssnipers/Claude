#!/usr/bin/env python3
"""usage: bgcheck.py NEW_COVER.png REPO_DIR  -> exit 1 if the new cover background looks similar to ANY earlier cover.
Compares only the background areas (left/right edges + middle band, text areas masked) using colour layout + structure."""
import sys,glob
from PIL import Image
import numpy as np
def feat(p):
    im=Image.open(p).convert('RGB').resize((108,135))
    a=np.asarray(im).astype(float)
    m=np.ones(a.shape[:2],bool); m[:22,:]=False; m[40:105,5:103]=False  # mask top bar, headline/badge area
    m[40:105,:]=False
    keep=np.zeros_like(m); keep[22:40,:]=True; keep[105:,:]=True      # sky/skyline band + lower band
    keep[40:105,:12]=True; keep[40:105,-12:]=True                     # side strips
    return a,keep
def dist(p,q):
    a,k=feat(p); b,_=feat(q)
    d=np.abs(a-b).mean(axis=2)[k].mean()
    ha=np.histogram(a[k].reshape(-1,3).mean(axis=1),bins=16,range=(0,255))[0]/k.sum()
    ca=np.array([a[k][:,i].mean() for i in range(3)]); cb=np.array([b[k][:,i].mean() for i in range(3)])
    return d, np.abs(ca-cb).sum()
new,repo=sys.argv[1],sys.argv[2]
bad=[]
for q in sorted(glob.glob(repo+'/20*/news-*/slide-1.png')+glob.glob(repo+'/20*/news/slide-1.png')):
    if q==new: continue
    d,c=dist(new,q)
    if d<6.5 or c<12: bad.append((q,round(d,1),round(c,1)))
print('SIMILAR to:' if bad else 'OK: distinct from all earlier covers'); [print(' ',b) for b in bad]
sys.exit(1 if bad else 0)
