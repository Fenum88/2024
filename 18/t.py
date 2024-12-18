from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
import heapq
import re
a=open("input.in").read().split("\n")
nums="1234567890"
m=[]
M={}
D=[(1,0),(0,1),(-1,0),(0,-1)]
tStart= cl.time()
for i in a:
    (x,y)=tuple(map(int, re.findall(r'-?\d+', i)))
    m.append((x,y))

def calc(M):
    S={}
    cube=[(0,0,0)]
    xm=6
    xm=70
    while len(cube)>0:
        (steps,x,y)=cube.pop()
        steps+=1
        for i in D:
            (xd,yd)=i
            if x+xd>xm or x+xd<0 or y+yd>xm or y+yd<0 or (x+xd,y+yd) in M:
                continue
            if (x+xd,y+yd) in S:
                if S[x+xd,y+yd]<=steps:
                    continue
            S[x+xd,y+yd]=steps
            cube.append((steps,x+xd,y+yd))
    # print(((xm,xm) in S))
    if (xm,xm) in S:
        return S[xm,xm]
    else:
        return -1

def getM(t):
    M={}
    for i in range(t):
        (x,y)= m[i]
        M[x,y]=1
    return M

print("Aufgabe 1: ", calc(getM(1024)))

t_min=0
t_max=len(m)-1
idx=0
while True:
    t=int((t_max+t_min)/2)
    # t=21
    M=getM(t)
    check= calc(M)
    if check:
        t_min=t
    else:
        t_max=t
    # print(t_min,t_max,t)
    if t_max-t_min ==1:
        break

print("Aufgabe 2:",m[t_max-1])
print(cl.time()-tStart)