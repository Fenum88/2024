from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
a=open("input.in").read().split("\n\n")
nums="1234567890"
m=[]
M={}
tStart= cl.time()
for i in a:
    b=i.split("\n")
    N={}
    aw=b[0].split("+")
    ax= int(aw[1].split(",")[0])
    ay= int(aw[-1])
    N["a"]=(ax,ay)
    bw=b[1].split("+")
    bx= int(bw[1].split(",")[0])
    by= int(bw[-1])
    N["b"]=(bx,by)
    pw=b[2].split("=")
    px= int(pw[1].split(",")[0])
    py= int(pw[-1])
    N["p"]=(px,py)
    m.append(N)
idx=1
for zahl in [0,10000000000000]:
    p1=0
    for machine in m:
        machine["p"]=(machine["p"][0]+zahl,machine["p"][1]+zahl)
        (ax,ay)=machine["a"]
        (bx,by)=machine["b"]
        (px,py)=machine["p"]
        zaehler=(px*by-py*bx)
        nenner=(ax*by-machine["a"][1]*bx)
        s= zaehler/nenner
        t= (px-ax*s)/bx
        if s%1==0 and t%1==0:
            p1+=(s*3+t)
    print(f"Aufgabe {idx}: ",int(p1))
    idx+=1
print(cl.time()-tStart)