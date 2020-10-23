
def picNumber(a):
    uniq=[]
    count=[]
    for i in a:
        if i not in uniq:
            uniq.append(i)
    uniq.sort()
    freq=0
    v1=0
    max=-1
    for i in range(len(uniq)):
        v1=a.count(uniq[i])
        count.append(v1)
        if max<(v1):
            max=v1
    print(uniq)
    print(count)
    for i in range(len(uniq)-1):
        if uniq[i+1]-uniq[i]==1:
            if freq<(a.count(uniq[i])+a.count(uniq[i+1])):
                freq=a.count(uniq[i])+a.count(uniq[i+1])
        elif freq<count[i]:
                freq=count[i]
    return freq


if __name__ == "__main__":
    # print(picNumber([4 ,6 ,5 ,3 ,3 ,1]))
    # print(picNumber([1,2,2,3,1,2]))
    # print(picNumber([1,3,1,1,1,1,1,3,3,4]))
    print(picNumber([4,97,5,97,97,4,97,4,97,97,97,97,4,4,5,5,97,5,97,99,4,97,5,97,97,97,5,5,97,4,5,97,97,5,97,4,97,5,4,4,97,5,5,5,4,97,97,4,97,5,4,4,97,97,97,5,5,97,4,97,97,5,4,97,97,4,97,97,97,5,4,4,97,4,4,97,5,97,97,97,97,4,97,5,97,5,4,97,4,5,97,97,5,97,5,97,5,97,97,97]))