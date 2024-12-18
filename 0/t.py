from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
import heapq
import re
a=open("input2.in").read().split("\n")
nums="1234567890"
m=[]
M={}
D=[(1,0),(0,1),(-1,0),(0,-1)]
tStart= cl.time()

for i in a:
    b=tuple(map(int, re.findall(r'-?\d+', i)))
    print(b)




# cube=[(0,9)]
# (a,b)=heapq.heappop(cube)
# heapq.heappush(cube,(0,9))
    
print(cl.time()-tStart)


