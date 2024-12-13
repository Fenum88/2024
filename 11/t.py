from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
a=open("input.in").read().split("\n")
nums="1234567890"
m=[]
M=defaultdict(int)
tStart= cl.time()

a="125 17".split(" ")
# a="0 1 10 99 999".split(" ")
a="8793800 1629 65 5 960 0 138983 85629".split(" ")

    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.


    # The first stone, 0, becomes a stone marked 1.
    # The second stone, 1, is multiplied by 2024 to become 2024.
    # The third stone, 10, is split into a stone marked 1 followed by a stone marked 0.
    # The fourth stone, 99, is split into two stones marked 9.
    # The fifth stone, 999, is replaced by a stone marked 2021976.

def lead(a):
    idx=0
    while idx<len(a):
        if a[idx]!="0":
            break
        idx+=1
    if len(a[idx:])==0:
        return "0"
    return a[idx:]

M={}

def calc(ele,t):
    ele = lead(ele)
    if t==0:
        return 1   
    if ele=="0":
        if ("1",t-1) not in M:
            M["1",t-1]=calc("1",t-1)
        return M["1",t-1]
    elif len(ele)%2==0:
        l= len(ele)
        links=ele[0:int(l/2)]
        rechts=ele[int(l/2):]
        if (links,t-1) not in M:
            M[links,t-1]=calc(links,t-1)
        if (rechts,t-1) not in M:
            M[rechts,t-1]=calc(rechts,t-1)
        return M[links,t-1]+ M[rechts,t-1]
    else:
        return calc(str(int(ele)*2024),t-1)

idx=0

p2=0

for i in range(len(a)):
    w=calc(a[i],75)
    p2+=w

print(p2)
print(cl.time()-tStart)