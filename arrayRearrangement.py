def function(num , arr1 , arr2):
   arr1.sort()
   arr2.sort(reverse=True)
   fun = lambda x,y:x+y
   sumArr =  list(map(fun,arr1,arr2))
   return sumArr
if __name__ == "__main__":
   t = int(input())
   for i in range(t):
      dim , num = map (int , input().split())
      arr1 = list(map(int,input().split()))
      arr2 =  list(map(int , input().split()))
      print(function(num , arr1 ,arr2))
