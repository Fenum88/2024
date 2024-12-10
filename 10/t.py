from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
a=open("input.in").read().split("\n")
nums="1234567890"
m=[]
M=defaultdict(int)
tStart= cl.time()

Y=0
cube=[]
for i in a:
    X=len(i)
    b=i
    for x in range(len(i)):
        if b[x]==".":
            wert=0
        else:
            wert=int(b[x])
        M[x,Y]=wert
        if M[x,Y]==0 and b[x]!=".":
            cube.append([[x,Y]])
    Y+=1

def calc(cube):
    ans2=[]
    while len(cube)>0:
        ele= cube.pop()
        x=ele[-1][0]
        y=ele[-1][1]
        if M[x,y]==9:
            ans2.append(ele)
            continue
        wert=M[x,y]+1

        for i in [(0,1),(0,-1),(1,0),(-1,0)]:
            if wert ==M[x+i[0],y+i[1]]:
                eleCopy = deepcopy(ele)
                eleCopy.append([x+i[0],y+i[1]])
                cube.append(eleCopy)
    ans=set()
    for i in ans2:
        ele= (i[-1][0],i[-1][1])
        ans.add(ele)
    return len(ans), len(ans2)

p1=0
p2=0
for i in cube:
    (wert,wert2)=calc([i])
    p1+=wert
    p2+=wert2

print("Aufgabe 1:",p1)
print("Aufgabe 2:",p2)

print(cl.time()-tStart)