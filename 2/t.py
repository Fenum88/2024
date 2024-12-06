from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
a=open("input.in").read().split("\n")
nums="1234567890"
m=[]
M={}
tStart= cl.time()

for i in a:
    b=i.split()
    b= [int(x) for x in b]
    m.append(b)

def calc(i):
    isIncreasing=True
    for k in range(0,len(i)-1):
        if i[k]<= i[k+1] or abs(i[k+1]-i[k])>3:
            isIncreasing=False
    isDecreasing=True
    for k in range(0,len(i)-1):
        if i[k]>= i[k+1] or abs(i[k+1]-i[k])>3:
            isDecreasing=False
    if  isIncreasing or isDecreasing:
        return True
    return False

ans=0
ans2=0
for i in m:
    if calc(i):
        ans+=1

print("Aufgabe1: ", ans)

ans2=0
for i in m:
    h=False
    for k in range(len(i)):
        sub = i[0:k]+i[k+1:]
        h = h or calc(sub)
    if h:
        ans2+=1
print("Aufgabe1: ",ans2)               

print(cl.time()-tStart)


