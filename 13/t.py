from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
import re
a=open("input.in").read().split("\n\n")
nums="1234567890"
m=[]
tStart= cl.time()
for i in a:
    m.append(tuple(map(int, re.findall(r'-?\d+', i))))
idx=1
for zahl in [0,10000000000000]:
    p1=0
    for machine in m:
        (ax,ay,bx,by,px,py)=machine
        px+=zahl
        py+=zahl
        zaehler=(px*by-py*bx)
        nenner=(ax*by-ay*bx)
        s= zaehler/nenner
        t= (px-ax*s)/bx
        if s%1==0 and t%1==0:
            p1+=(s*3+t)
    print(f"Aufgabe {idx}: ",int(p1))
    idx+=1
print(cl.time()-tStart)