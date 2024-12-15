from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
import re
a=open("input2.in").read().split("\n")
nums="1234567890"
m=[]
M={}
tStart= cl.time()

for i in a:
    b=tuple(map(int, re.findall(r'-?\d+', i)))
    print(b)




    
print(cl.time()-tStart)


