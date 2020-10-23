#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def checkEqu(equ,p):
    for i in equ:
        if len(i)==1:
            if p[0]==i[0]:
                return True
        else:
            if p[1]==(i[0]*p[0]+i[1]):
                return True
    return False


def length(p1,p2):
    x=(p1[0]-p2[0])**2+(p1[1]-p2[1])**2
    return pow(x,.5)-1
def findEquation(p1,p2):
    if p1[0]!=p2[0]:
        m=((p1[1]-p2[1])/(p1[0]-p2[0]))
        b=(p1[1]-(m*p1[0]))
        return list([m,b])
    else:
        return list([p1[0]])
def endPoints(loc,dim):
    

def adjPoint(dim,loc):
   points=[]
   #  of main dioganal
   if loc[0]+1<=dim[0] and loc[1]+1 <= dim[1]:
      points.append([loc[0]+1,loc[1]+1])
   elif loc[0]-1>0 and loc[1]-1 >0:
      points.append([loc[0]-1,loc[1]-1])
   # line paralell to x axis  
   if loc[0]+1<=dim[0] :
      points.append([loc[0]+1,loc[1]])
   elif loc[0]-1>0:
      points.append([loc[0]-1,loc[1]])
   #  line paralell to y axis
   if loc[1]+1 <= dim[1]:
      points.append([loc[0],loc[1]+1])
   elif loc[1]-1 >0:
      points.append([loc[0],loc[1]-1])
   # off dioganal  
   if loc[0]-1>0 and loc[1]+1 <= dim[1]:
      points.append([loc[0]-1,loc[1]+1])
   elif loc[0]+1<=dim[0] and loc[1]-1 >0:
      points.append([loc[0]+1,loc[1]-1])
   return points
def queensAttack(n, k, r_q, c_q, obstacles):
    adjP = adjPoint([n,n],[r_q,c_q])
    equ=[]
    for i in adjP:
        equ.append(findEquation(i,[r_q,c_q]))
    # print(equ)
    for i in obstacles:
        if checkEqu(equ,i):
            print(length([r_q,c_q],i))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
