from collections import defaultdict 
from copy import deepcopy
from itertools import product
import time as cl
import heapq
import re
a=open("input.in").read().split("\n")
nums="1234567890"
m=[]
M={}
D=[(1,0),(0,1),(-1,0),(0,-1)]
tStart= cl.time()

program= "0,3,5,4,3,0".split(",")
program= "2,4,1,5,7,5,1,6,4,1,5,5,0,3,3,0".split(",")
program=[int(x) for x in program]



def calc(a):
    def getWert(wert):
        if wert<=3:
            return wert
        if wert ==4:
            return a
        if wert ==5:
            return b
        if wert ==6:
            return c
        print("error")
        return-1
    idx=0
    b= 0
    c= 0
    p1=[]
    while idx<len(program)-1:
        befehl=program[idx]  #Opcode 
        wert=program[idx+1]    #Operand 
        cWert=getWert(program[idx+1]) 

        if befehl==0:
            a= a//(2**cWert)
        elif befehl==1:
            b=b^wert
        elif befehl==2:
            b=cWert%8
        elif befehl==3:
            if a!=0:
                idx=wert
                continue
        elif befehl==4:
            b=b^c
        elif befehl==5:
            p1.append(int(cWert%8)) 
        elif befehl==6:
            b= a//(2**cWert)
        elif befehl==7:
            c= a//(2**cWert)
        idx+=2
    return p1
p1=calc(60589763)
p1=[str(x) for x in p1]
print(p1)
print("Aufgabe 1:", ",".join(p1))



i=107413700222900
while True:
    p1=calc(i)
    # if p1[:5]==program[:5]:
    # print(i,p1[len(p1)-13:],program[len(p1)-13:])
    # print(i,p1,program)
    # if p1[len(p1)-12:]==program[len(program)-12:]:
    # if p1[len(p1)-10:]!=program[len(program)-10:]:
    if p1==program:
        print("Aufgabe 2:",i)
        break
    i+=1
    # i-=10**3

# i=1
# i_old=0
# p1=[]
# l=len(program)
# # Startwert suchen
# while len(p1)<l:
#     i*=10
#     p1=calc(i)

# print(len(p1),len(program),len(str(i)))
# print(p1,program,107413700222900>i)
# t=10**8
# idx=0
# c=False
# while idx<l:
#     p1=calc(i+t)
#     if p1[l-idx-1:]==program[l-idx-1:]:
#         # print(p1,t,p1[l-1]==program[l-1],p1[l-1],program[l-1])
#         t=int(t/10)
#         if t==0:
#             t=10**9
#             idx+=1
#             print(p1,program,idx,i,107413700222900>i,107413700222900- i)
#             if c:
#                 i+=1
#             c=False
#     else:
#         # print(p1,i)
#         c=True
#         i+=t
# p1=calc(i)
# p2=calc(i+1)
# print(p1,p2,program,program[l-1],107413700222900>i,107413700222900-i)  
print(cl.time()-tStart)


