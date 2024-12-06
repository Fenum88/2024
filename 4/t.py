from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
a=open("input.in").read().split("\n")
nums="1234567890"
m=[]
M=defaultdict(str)
tStart= cl.time()

ymax=0
for i in a:
    b=i
    xmax=0
    for k in b:
        M[xmax,ymax]=k
        xmax+=1
    ymax+=1


x=0
y=0
ans=0
ans2=0
while True:

    if M[x,y]+M[x+1,y]+M[x+2,y]+M[x+3,y] =="XMAS":
        ans+=1
    if M[x,y]+M[x-1,y]+M[x-2,y]+M[x-3,y] =="XMAS":
        ans+=1
    if M[x,y]+M[x,y+1]+M[x,y+2]+M[x,y+3] =="XMAS":
        ans+=1
    if M[x,y]+M[x,y-1]+M[x,y-2]+M[x,y-3] =="XMAS":
        ans+=1
    
    if M[x,y]+M[x+1,y+1]+M[x+2,y+2]+M[x+3,y+3] =="XMAS":
        ans+=1
    if M[x,y]+M[x-1,y-1]+M[x-2,y-2]+M[x-3,y-3] =="XMAS":
        ans+=1
    if M[x,y]+M[x-1,y+1]+M[x-2,y+2]+M[x-3,y+3] =="XMAS":
        ans+=1
    if M[x,y]+M[x+1,y-1]+M[x+2,y-2]+M[x+3,y-3] =="XMAS":
        ans+=1
    p=0
    if M[x-1,y-1]+M[x,y]+M[x+1,y+1] in ["MAS","SAM"]:
        p+=1
    if M[x-1,y+1]+M[x,y]+M[x+1,y-1] in ["MAS","SAM"]:
        p+=1

    
    if p>=2:
        ans2+=1
    
    x+=1

    if x>xmax:
        x=0
        y+=1
    if y>ymax:
        break



print(ans)
print(ans2)


    
print(cl.time()-tStart)


