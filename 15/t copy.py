from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
import re
a=open("input2.in").read().split("\n\n")
nums="1234567890"
m=""
M={}
tStart= cl.time()
Y=0
for i in a[0].split("\n"):
    b=i
    X=len(i)
    for k in range(len(i)):
        if i[k]=="@":
            (x,y)=(k,Y)
            M[k,Y]="."
        else:
            M[k,Y]=i[k]

    Y+=1    

a=a[1].split("\n")
m=""
for i in a:
    m+=i
print(m)



D=[(1,0),(0,1),(-1,0),(0,-1)]
t=0
print("start")
for i in m:
    # if t>2:
    #     break
    t+=1

    d=0
    if i ==">":
        d=0
    elif i =="v":
        d=1
    elif i=="<":
        d=2
    else:
        d=3
    (dx,dy)=D[d]
    #prüfen ob schiebbar
    c=True
    idx=1
    while True:
        (xn,yn)=(x+dx*idx,y+dy*idx)
        if M[xn,yn]==".":
            c=False
            M[xn,yn]="O"
            break
        if M[xn,yn]=="#":
            break
        idx+=1
    #keinen freien platzt
    if c:
        continue
    (x,y)=(x+dx,y+dy)
    M[x,y]="."
    t+=1
    


for a in range(Y):
    s=""
    for b in range(X):
        if a==y and x==b:
            s+="@"
        else:
            s+=M[b,a]

    print(s)

p1=0

for i in M:
    if M[i]=="O":
        p1+=i[0]+i[1]*100

print(p1)
print(cl.time()-tStart)


