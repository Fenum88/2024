from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
a=open("input.in").read().split("\n")
nums="1234567890"
m=[]
M={}
tStart= cl.time()

y=0
Y=len(a)
X=0
for i in a:
    x=0
    X=len(i)
    b=i
    for k in i:
        if k not in ["."]:
            M[x,y]=k
        x+=1
    y+=1

def calc(M,p):
    kords = list(M.keys())
    M2={}
    for i in range(len(kords)):
        if not p:
            M2[kords[i][0],kords[i][1]]="#"
        for k in range(0, len(kords)):
            if i==k:
                continue
            if M[kords[i]]== M[kords[k]]:
                xd =  (kords[i][0]-kords[k][0])
                yd =  (kords[i][1]-kords[k][1])
                idx=1
                while True:
                    x=kords[i][0]+xd*idx
                    y=kords[i][1]+yd*idx
                    if not (x<0 or y<0 or x>=X or y>=Y):
                        M2[x,y]="#"
                    else:
                        break   
                    idx+=1
                    if p:
                        break
    p1=0
    for i in M2:
        if M2[i]=="#":
            p1+=1
    return p1

print("Aufgabe 1:",calc(M,True))
print("Aufgabe 2:",calc(M, False))


# for y in range(Y):
#     s=""
#     for x in range(X):
#         if (x,y) not in M2:
#             s+="."
#         else:
#             s+=M2[x,y]
#     print(s)

print(cl.time()-tStart)