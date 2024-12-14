from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
import re
a=open("input.in").read().split("\n")
nums="1234567890"
m=[]
M={}
tStart= cl.time()

for i in a:
    m.append(tuple(map(int, re.findall(r'-?\d+', i))))

mx=101
my=103
# mx=11
# my=7
t=0
c=True
while c:
    c=False
    m_end=[]
    for i in m:
        (x,y,vx,vy)=i
        x= (x+vx)%mx
        y=(y+vy)%my
        m_end.append((x,y,vx,vy))
    m=m_end
    t+=1
    if t==100:
        ans=[0,0,0,0]
        for i in m_end:
            xs=int(mx/2)
            ys=int(my/2)
            r1=[range(0,xs),range(0,ys)]
            r2=[range(0,xs),range(ys+1,my)]
            r3=[range(xs+1,mx),range(0,ys)]
            r4=[range(xs+1,mx),range(ys+1,my)]

            if i[0] in r1[0] and i[1] in r1[1]:
                ans[0]+=1
            if i[0] in r2[0] and i[1] in r2[1]:
                ans[1]+=1
            if i[0] in r3[0] and i[1] in r3[1]:
                ans[2]+=1
            if i[0] in r4[0] and i[1] in r4[1]:
                ans[3]+=1
        p1=1
        for i in ans:
            p1*=i
        print("Aufgabe 1: ",p1)
    for i in range(len(m)-1):
        for k in range(i+1,len(m)):
            if m[i][0]==m[k][0] and m[i][1]==m[k][1]: 
                c=True
                break
        if  c:
            break

print("Aufgabe 2: ",t)
print(cl.time()-tStart)


