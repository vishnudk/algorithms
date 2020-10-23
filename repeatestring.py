def function(s,n):
    j=1
    posi=[]
    val=0
    for i in s:
        if i == 'a':
            posi.append(j)
        j=j+1
    # print(posi)
    if len(posi)>0:
        if n%len(s)==0:
            val = (n/max(posi))*len(posi)
        else:
            rem = n%len(s)
            val = (int(n/len(s)))*len(posi)
            while len(posin)>0 :
                if rem >= max(posi):
                    val = val+len(posi)
                    break
                posi.pop()
            
    return int (val)

if __name__ == "__main__":
    s='aab'
    n=882787
    print(function(s,n))