def function(k,s):
    # s.sort()
    prv=[]
    count=0
    checked=[]
    flag=0
 
    prv=[i%k for i in s]

    for i in prv:
        if i!=0:
            if i not in checked:
                if (k-i) not in prv:
                    count=count+prv.count(i)
                    checked.append(i)
                elif i==(k-i):
                    count=count+1
                    checked.append(i)
                     
                else:
                    count=count+max(prv.count(i),prv.count(k-i))
                    checked.append(i)
                    checked.append(k-i)
        else:
            flag=1
            checked.append(i)
    count=count+flag
    return count
            


if __name__ == "__main__":
    k= 3
    s=[1, 7, 2, 4]
    # k=4
    # s=[19,10,12,10,24,25,22]
    print(function(k,s))