def function(c,k,n):
    i=0
    e=100
    i=(i+k)%n
    e=e-1
    if c[i]==1:
        e=e-2
    while i!=0:
        i=(i+k)%n
        e=e-1
        if c[i]==1:
            e=e-2
    return e


if __name__ == "__main__":
    c=[0, 0 ,1 ,0, 0, 1 ,1 ,0]
    k=2
    n=8
    print(function(c,k,n))