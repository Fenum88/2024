from collections import defaultdict 
from copy import deepcopy
import heapq
from itertools import product
import time as cl
import re
a=open("input.in").read().split("\n")
D=[(1,0),(0,1),(-1,0),(0,-1)]
nums="1234567890"
m=[]
M={}
tStart= cl.time()
X=0
Y=0
(x,y)=(0,0)
(ex,ey)=(0,0)
for i in a:
    b=i
    X=max(X,len(i))
    for c in range(len(i)):
        if i[c]=="S":
            (x,y)=(c,Y)
            M[c,Y]="."
        elif i[c]=="E":
            (ex,ey)=(c,Y)
            M[c,Y]="."
        else:
            M[c,Y]=i[c]
    Y+=1
#finde alle Knoten
K={}
(x_start,y_start)=(x,y)
cube=[(x,y),(ex,ey)]
while len(cube)>0:
    (xs,ys)= cube.pop()
    if (xs,ys) in K:
        continue
    ends=[]
    for d in D:
        (x,y)=(xs,ys)
        (xd,yd)=d
        steps=0
        if M[x+xd,y+yd]=="#":
            continue
        c=True
        while c:
            (x,y)=(x+xd,y+yd)
            steps+=1
            isKnoten=0
            for d2 in D:
                if M[x+d2[0],y+d2[1]]==".":
                    isKnoten+=1
            if isKnoten==1:
                c=False #dead end
            elif isKnoten>2 or (x,y)==(ex,ey):
                ends.append((x,y,steps,d,(xd,yd))) #d=start richtung, endrichtung (xd,yd)
                c=False
            else:
                if M[x+xd,y+yd]==".":
                    c=True
                else: #kurve
                    steps+=1000
                    for i in [1,-1]:
                        d_neu=D[(D.index((xd,yd))+i)%4]
                        if M[x+d_neu[0],y+d_neu[1]]==".":
                            (xd,yd)=d_neu
    K[xs,ys]=ends
    for i in ends:
        cube.append((i[0],i[1]))
            
cube=[]
ans=[]
ans2=[]
for i in K[x_start,y_start]:
    cube.append((0,x_start,y_start,[],(1,0),[]))
p1=10**20
t=0
S={}
while len(cube)>0:
    (steps,x,y,v,aktuelleRichtung,richtungsverlauf)=heapq.heappop(cube)
    if (x,y,aktuelleRichtung[0],aktuelleRichtung[1]) in S:
        if S[x,y,aktuelleRichtung[0],aktuelleRichtung[1]]<steps:
            continue
    S[x,y,aktuelleRichtung[0],aktuelleRichtung[1]]=steps
    if steps>p1:
        continue
    if (x,y)==(ex,ey):
        if steps<p1:
            ans=[]
            ans2=[]
            ans.append(v)
            ans2.append(richtungsverlauf)
            p1=steps
        elif steps==p1:
            ans.append(v)
            ans2.append(richtungsverlauf)
        continue
    v.append((x,y))
    for i in K[x,y]:
        (xn,yn,stepsn,startrichtung2,endrichtung2)=i
        if (xn,yn) in v:
            continue
        if aktuelleRichtung !=startrichtung2:
            stepsn+=1000
        heapq.heappush(cube,deepcopy((steps+stepsn,xn,yn,v,endrichtung2, deepcopy(richtungsverlauf+[startrichtung2]))))

print("Aufgabe 1: ",p1)

S2=[]
for i in range(len(ans)):
    cube=ans[i]
    cubeDir=ans2[i]
    cube.append((ex,ey))
    for k in range(len(cube)-1):
        (x,y)=cube[k]
        (nx,ny)=cube[k+1]
        (xd,yd)=cubeDir[k]
        while True:
            (x,y)=(x+xd,y+yd)
            M[x,y]="O"
            if (x,y)==(nx,ny):
                break
            if M[x+xd,y+yd]=="#":
                for k in [1,-1]:
                    d_neu=D[(D.index((xd,yd))+k)%4]
                    if M[x+d_neu[0],y+d_neu[1]] in [".","O"]:
                        (xd,yd)=d_neu
p2=1
for y1 in range(Y):
    s=""
    for x1 in range(X):
        s+=M[x1,y1]
        if M[x1,y1] =="O":
            p2+=1
    # print(s)
print("Aufgabe 2: ",p2)
print(cl.time()-tStart)