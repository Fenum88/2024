from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
a=open("input.in").read().split("\n")
nums="1234567890"
m=[]
M=defaultdict(str)
S={}
tStart= cl.time()
x,y=(0,0)
ymax=0
for i in a:
    xmax=0
    b=i
    for k in b:
        M[xmax,ymax]=k
        if k in "><^v":
            x=xmax
            y=ymax
        xmax+=1
    ymax+=1

x2=x
y2=y


def printCountM(M):
    ans=0
    for y in range(0,ymax+1):
        s=""
        for x in range(0,xmax+1):
            s+=M[x,y]
            if M[x,y] in ["X","^"]:
                ans+=1
        # print(s)
    return ans
O=set()
def calc(M,x,y,d,c):
    L=[]
    while True:
        new_x =x
        new_y=y

        if d==0:
            new_y-=1
        elif d==1:
            new_x+=1
        elif d==2:
            new_y+=1
        else:
            new_x-=1
        
        if M[new_x,new_y] in ["#","O"]:
            d+=1
            d%=4
        else:
            if new_x<0 or new_x>=xmax or new_y<0 or new_y >=ymax:
                if c:
                    print("Aufgabe 1: ",printCountM(M))
                return 1 
            else:
                x=new_x
                y=new_y
                M[x,y]="X"
                if (x,y,d) in L :
                    return -1
                else:
                    L.append((x,y,d))

P1= deepcopy(M)
calc(P1,x,y,0,True)

x=x2
y=y2
d=0
U={}
U2={}
p2=0
while True:
    new_x =x
    new_y=y
    if d==0:
        new_y-=1
    elif d==1:
        new_x+=1
    elif d==2:
        new_y+=1
    else:
        new_x-=1
    
    if M[new_x,new_y] in ["#"]:
        d+=1
        d%=4
    else:
        if new_x<0 or new_x>=xmax or new_y<0 or new_y >=ymax:
            break 
        else:
            if (new_x, new_y,d) not in U and (new_x, new_y) not in U2:
                M2 = deepcopy(M)
                M2[new_x,new_y]="#"
                a=calc(M2,x,y,d,False)
                if a==-1:
                    U[new_x, new_y,d]=1
                    p2+=1
            x=new_x
            y=new_y
            U2[x,y]=1
print("Aufgabe 2:",p2)


print(cl.time()-tStart)
