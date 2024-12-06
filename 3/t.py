from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
import re
a=open("input.in").read().split("\n")
a=a[0]
# a="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

off="don't()"
on="do()"

l=len(off)

a_new=""
i=0
check=True
while i <len(a):
    if off in a[i:i+l]:
        check=False
    if on in a[i:i+l]:
        check=True
    if check:
        a_new+=a[i]
    i+=1 

def count(a):
    pattern = r"mul\(-?\d+,-?\d+\)"
    matches = re.findall(pattern, a)
    ans=0
    for i in matches:
        b=i.replace("mul(","").replace(")","").split(",")
        b= [int(x) for x in b]
        ans+= b[0]*b[1]
    return ans

print("Aufgabe1:",count(a))
print("Aufgabe2:",count(a_new))

