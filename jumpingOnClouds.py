def function(c):
    count=-1
    i=0
    while i<(len(c)):
        if i+2<len(c):
            if c[i+2]==0:
                i=i+2
            else:
                i=i+1
        else:
            i=i+1
        count=count+1
        
    return count


if __name__ == "__main__":
    # c=[0,1,0,0,1,0]
    c=[0, 0, 0, 0, 1, 0]
    print(function(c))