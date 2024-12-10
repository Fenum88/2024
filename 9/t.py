from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
a=open("input.in").read().split("\n")
nums="1234567890"
a=a[0]
# a="2333133121414131402"
m=[]
M={}
tStart= cl.time()
ss=[]

for i in a:
    b=i
    ss.append(b)


print(a)


i=0
l=0
s=[]

while i<len(a):
    if i%2==0 :
        for x in range(int(a[i])):
            s.append(str(l)) 
        l+=1
    else:
        for x in range(int(a[i])):
            s.append(".") 
    i+=1


i=0
k=len(s)-1
while True:
    print(k)
    while True:
        if s[k]!="." or k<=0:
            ele=s[k]
            eleStart=k
            while ele==s[k]:
                k-=1
            break
        k-=1
    eleLen= eleStart-k
    i=0
    c=False
    while i<k:
        if s[i]==".":
            c2=True
            for h in range(i,i+eleLen):
                if s[h]!=".":
                    c2=False
            if c2:
                c=True
                break
            else:
                i+=1
        else:
            i+=1


    if k<=0:
        break
    # print(i,k)
    # print(s)
    # print("anfang",s[:i])
    # print("Element",s[k+1:eleStart+1])
    # print("AktEle bis alt Ele",s[i+eleLen:k])
    # print("Ende",s[eleStart+1:])
    # print(c)
    ende=[]
    if c:
        for f in range(eleLen):
            ende.append(".")
        s= s[:i]+s[k+1:eleStart+1]+s[i+eleLen:k+1]+ende+s[eleStart+1:]

p1=0
for i in range(len(s)):
    if s[i]!=".":
        p1+= i * int(s[i])
print(p1)
    


print(cl.time()-tStart)


#5624298517