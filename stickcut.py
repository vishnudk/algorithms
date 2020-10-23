def function(arr):
    l=[]
    while len(arr)!=0:
        l.append(len(arr))
        m=min(arr)
        arr1=[]
        for i in arr:
            if i!=m:
                arr1.append(i)
        arr=[]
        arr=arr1.copy()
    return l



if __name__ == "__main__":
    # arr=[1 ,2 ,3, 4, 3, 3, 2 ,1]
    arr=[5,4,4,2,2,8]
    print(function(arr))