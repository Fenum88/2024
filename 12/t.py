from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
a=open("input.in").read().split("\n")
nums="1234567890"
m=[]
M=defaultdict(str)
tStart= cl.time()
Y=0
for i in a:
    b=i
    X=len(i)
    for x in range(len(i)):
        M[x,Y]=i[x]
    Y+=1

def isConnected(x,y,ele):
    ans=[]
    for d in [[1,0],[0,1],[-1,0],[0,-1]]:
        if M[x+d[0],y+d[1]] ==ele:
            ans.append((x+d[0],y+d[1]))
    return ans

def findPoints(x,y):
    ele=M[x,y]
    p=[(x,y)]
    while True:
        pc= deepcopy(p)
        b=[]
        for i in pc:
            a=isConnected(i[0],i[1],ele)
            b+=a
        pc+=b
        pc=list(set(pc))
        if len(pc)==len(p):
            break
        p=pc
    return p

D=[(1,0),(0,1),(-1,0),(0,-1)]
def calPerimeter(a):
    ele=M[a[0]]
    ans=[]
    for i in a:
        x=i[0]
        y=i[1]
        for k in range(4):
            d=D[k]
            if M[x+d[0],y+d[1]] !=ele:
                ans.append((x+d[0],y+d[1],(k+1)%4))
    return ans

def calcSides(per):
    ans=0
    while len(per)>0:
        (x,y,d)=deepcopy(per[0]) 
        #suche den Anfang der seite
        d2= (d+2)%4
        while True:
            if (x+D[d2][0],y+D[d2][1],d) in per:
                x+=D[d2][0]
                y+=D[d2][1]
            else:
                break
        #lösche alle Elemente aus der Cube
        while True:
            if (x,y,d) in per:
                per.remove((x,y,d))
                x+=D[d][0]
                y+=D[d][1]
            else:
                ans+=1
                break
    return ans

p1=0
p2=0
cube=list(M.keys())
for i in cube:
    if M[i]=="":
        continue
    points= findPoints(i[0],i[1])
    per= calPerimeter(points)
    p1+=len(points)*len(per)
    sides=calcSides(per)
    p2+=len(points)*sides
    for k in points:
        M[k]=""

print("Aufgabe 1: ",p1)
print("Aufgabe 2: ",p2)
print(cl.time()-tStart)


