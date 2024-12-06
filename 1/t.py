from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
a=open("input.in").read().split("\n")
nums="1234567890"
m=[]
M={}
tStart= cl.time()

ans=0
ans2=0
l =[]
r=[]

for i in a:
    b=i.split()
    b=[int(x) for x in b]
    l.append(b[0])
    r.append(b[1])

l.sort()
r.sort()

for i in range(0,len(l)):
    ans+= abs(l[i]-r[i])
    ans2+= l[i]* r.count(l[i])


print(ans)
print(ans2)


    
print(cl.time()-tStart)


