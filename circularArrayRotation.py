def circularArray(a, k, queries):
    m = len(a)
    lenght=m
    if k>=m:
        m=k%m
    else:
        m=k
    f_list=[]
    for i in queries:
        tmp=i
        if i < m:
            r = m-i
            f_list.append(a[lenght-r])
        else:
            f_list.append(a[i-m])
    return f_list


        


if __name__ == "__main__":
    a=[1, 2, 3]
    k=2
    queries=[0, 1, 2]
    print(circularArray(a,k,queries))
