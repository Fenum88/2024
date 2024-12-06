from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
a=open("input.in").read().split("\n")
nums="1234567890"
m=[]
m1=[]
M=defaultdict(list)
tStart= cl.time()
c=True

for i in a:
    b=i
    if len(b)==0:
        c=False
        continue
    if c:
        b=b.split("|")
        M[int(b[0])].append(int(b[1]))
    else:
        b=b.split(",")
        b= [int(x) for x in b]
        m1.append(b)

ans=[]
ans2=[]
for i in m1:
    c=True
    for k in range(len(i)-1):
        if i[k+1] not in M[i[k]]:
            c=False
    if c:
        ans.append(i)
    else:
        ans2.append(i)

p1=0
for i in ans:
    p1+= i[int(len(i)/2)]
print("Aufgabe 1: " ,p1)

ans3=[]
for i in ans2:
    a=i
    index=0
    while index < len(a)-1:
        if a[index+1] not in M[a[index]]:
            ele= a[index+1]
            a=[]+ a[:index+1]+a[index+2:]
            for k in range(len(a)):
                if a[k]  in M[ele]:
                    a.insert(k,ele)
                    index=0
                    break
        else:
            index+=1
    ans3.append(a)

p2=0
for i in ans3:
    p2+= i[int(len(i)/2)]
print("Aufgabe 2: ",p2)
print(cl.time()-tStart)