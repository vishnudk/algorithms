#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def getTotalX(a, b):
    fun = lambda x,y:x%y
    max_a=max(a)
    min_b=min(b)
    count=0
    if max_a<=min_b:
        fun = lambda x,y:x%y
        for i in range(min_b-max_a+1):
            l1=map(fun,b,[i+max_a]*len(b))
            l2=map(fun,[i+max_a]*len(a),a)
            if sum(list(l1))==0 and sum(list(l2))==0:
                count=count+1
        return count
    else:
        return 0

if __name__ == "__main__":
    a=[2,4]
    b=[16,32,96]
    print(getTotalX(a,b))
    # testFun(a,b)