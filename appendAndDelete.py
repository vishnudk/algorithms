def function(s,t,k):
    l1=len(s)
    l2=len(t)
    for i in range(min(l1,l2)):
        if s[i]!=t[i]:
            break
    if i==(min(l1,l2))-1:
        i=i+1
    total = (l1-i)+(l2-i)

    if k<total:
        return 'NO'
    elif k==total:
        return 'YES'
    else:
        if k-total>=(2*l2):
            return 'YES'
        elif (k-total)%2==0:
            return 'YES'
        else:
            return 'NO'


if __name__ == "__main__":
    s= 'abcdef'
    t= 'fedcba'
    k= 15
    print(function(s,t,k))