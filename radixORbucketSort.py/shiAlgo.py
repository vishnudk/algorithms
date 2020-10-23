import math
import sympy 
def noOfTimeDiv(n,i):
    count=0
    while n%i==0:
        n=n/i
        count=count+1
    return count
def isPrime(n):
    if n==1:
        return True
    for i in range(2,n-1):
        if n%i==0 and n!=i:
            return False
    return True
def matrix(n):
    print("==================")
    total=1
    for i in range(2,int(n)):
        if n%i==0 and isPrime(i):
            total=total*(noOfTimeDiv(n,i)+1)              
    return total
print(matrix(int(input())))
