def function(arr):
    max=0
    for i in arr:
        if arr.count(i)>max:
            max=arr.count(i)

    return len(arr)-max
    


if __name__ == "__main__":
    arr=[1,2,2,3]
    print(function(arr))