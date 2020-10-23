import math as m

def function(s): 
   length = len(s)
   val = length**.5
   maxVal = m.ceil(val)
   minVal = m.floor(val)
   # print([maxVal,minVal])
   matrix=[]
   count = 0
   arr=[]
   string = ''
   lenStr=0
   for i in s:
      lenStr=lenStr+1
      if count < maxVal:
         arr.append(i)
         # print(i)
         count = count + 1
         if count == maxVal or lenStr==len(s):
            matrix.append(arr)
            # print(arr)
            arr=[]
            # print("============")
            count=0
   # matrix=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] 
   finalStr=[]
   tmpStr=[]
   flag=0
   for i in matrix:
      for j in range(len(i)):
         if flag==0:
            tmp=[i[j]]
            finalStr.append(tmp)
         else:
            finalStr[j].append(i[j])
      flag=1
      
   # print(finalStr)
   # print(matrix)
   for i in finalStr:
      for j in i:
         string=string+j
      string=string+" "
   return string

   # return 4**.5


if __name__ == "__main__":
   s = 'haveaniceday' 
   s = 'feedthedog'
   print(function(s))
