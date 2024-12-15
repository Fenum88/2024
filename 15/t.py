from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
import re
a=open("input.in").read().split("\n\n")
nums="1234567890"
m=""
M={}
tStart= cl.time()
Y=0
for i in a[0].split("\n"):
    b=""
    for k in i:
        if k=="O":
            b+="[]"
        elif k=="@":
            b+="@."
        elif k=="#":
            b+="##"
        else:
            b+=".."
    X=len(b)
    for k in range(len(b)):
        if b[k]=="@":
            (x,y)=(k,Y)
            M[k,Y]="."
        else:
            M[k,Y]=b[k]
    Y+=1    

a=a[1].split("\n")
m=""
for i in a:
    m+=i
print(m)

print(len(m))

D=[(1,0),(0,1),(-1,0),(0,-1)]
t=0
print("start")
p2=0
for a in range(Y):
    s=""
    for b in range(X):
        if a==y and x==b:
            s+="@"
        else:
            s+=M[b,a]
    print(s)
for i in m:
    print(t, (len(m)-t))
    cube=[]
    cube_end=[]
    # if t>1:
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
    cube =[(x,y)]
    cube_end=[]

    isHor = d==0 or d==2
    # suche alle Dinge die verschoben werden sollen
    while len(cube)>0:
        (bx,by)= cube.pop()
        cube_end.append((bx,by))
        if M[bx+dx,by+dy] =="[":
            cube.append((bx+dx,by+dy))
            if not isHor:
                cube.append((bx+dx+1,by+dy))
        elif M[bx+dx,by+dy] =="]":
            cube.append((bx+dx,by+dy))
            if not isHor:
                cube.append((bx+dx-1,by+dy))
    #prüfen ob schiebbar
    c=True
    for i in cube_end:
        (bx,by)=i
        if M[bx+dx,by+dy] =="#":
            c=False
    #keinen freien platzt
    if not c:
        continue
    (x,y)=(x+dx,y+dy)
    cube_end=cube_end[1:]
    #erstelle neue Matrix
    M2={}
    # neue punkte +bertragen
    for i in range(len(cube_end)):
        (bx,by)=cube_end[i]
        M2[bx+dx,by+dy]=M[bx,by]
    #alte punkte löschen
    cube=[]
    for i in range(len(cube_end)):
        (bx,by)=cube_end[i]
        cube.append((bx+dx,by+dy))
        M[bx,by]="."
    #restliche Punkte übertragen
    cube = deepcopy(cube)
    for i in M:
        if i not in cube:
            M2[i]=M[i]
    M=deepcopy(M2)
    M2={}
    # fixieren von boxen
    for i in M:
        if M[i]=="#" or M[i]==".":
            M2[i]=M[i]
            continue
        (bx,by)=i
        if M[bx,by]=="]":
            (brx,bry)=(bx,by)
            (blx,bly)=(bx-1,by)
        else:
            (brx,bry)=(bx+1,by)
            (blx,bly)=(bx,by)
        #ist links- oder rechts- bündig
        if M[blx-1,bly]=="#"or M[brx+1,bry]=="#":
            #ist oben oder unten bündig
            if M[brx,bry+1]=="#" or M[brx,bry-1]=="#" or M[blx,bly+1]=="#" or M[blx,bly-1]=="#":
                M2[brx,bry]="#"
                M2[blx,bly]="#"
                p2+=blx+bly*100
            else:
                M2[i]=M[i]
        else:
            M2[i]=M[i]
    M=deepcopy(M2) 






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
    if M[i]=="[":
        if i[1]==1:
            print(i,i[0]+i[1]*100)
        p1+=i[0]+i[1]*100

print(p1,p2,p1+p2/2)
print(cl.time()-tStart)

#1535509