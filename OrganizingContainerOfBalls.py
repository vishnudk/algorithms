def function(container):
   sum1=[]
   freq=(len(container))*[0]
   
   for i in container:
      sum1.append(sum(i))
      for j in range(len(i)):
         freq[j]=freq[j]+i[j]
  
   freq.sort()

   sum1.sort()
   
   if freq == sum1:
      return "Possible"
   else:
      return "Impossible"
if __name__ == "__main__": 
   container = [[1,3,1],[2 ,1 ,2],[3,3,3]]
   # container= [[1,1],[1,1]]
   print(function(container))
