import sys

print("Enter the no of elements to be entered")
n=int(input())
print("Enter data to be sorted")
list1=[]
max=-sys.maxsize - 1
for i in range(n):
    tmpVal = [input(), int(input())] 
    if max<tmpVal:
        max=tmpVal
    list1.append(tmpVal)
print(max)