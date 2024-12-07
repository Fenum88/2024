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
    b=i.replace(":","").split()
    b=[int(x) for x in b]
    m.append(b)

def check(a):
    num = a[0]
    s=[a[1]]
    a= a[2:]

    for i in a:
        s_new=[]
        for k in s:
            s_new.append(k*i)
            s_new.append(k+i)
            s_new.append(int(str(k)+str(i)))
        s=s_new
    return num in s
p1=0
for i in m:
    if(check(i)):
        p1+=i[0]

print(p1)
    
print(cl.time()-tStart)


