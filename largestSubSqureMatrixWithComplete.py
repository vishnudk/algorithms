def function(mat):
    l=len(mat)
    n = l
    while l>0:
        yStart=xStart=0
        yEnd=xEnd=l
        while yEnd<=n:
            while xEnd<=n:
                flag=0
                for i in range(xStart,xEnd):
                    for j in range(yStart,yEnd):
                        if mat[i][j]==0:
                            flag=-1
                            break
                    if flag==-1:
                        break
                if flag==0:
                    return l
                xStart=xStart+1
                xEnd=xEnd+1
            yStart=yStart+1
            yEnd=yEnd+1
            xStart=0
            xEnd=l
        l=l-1
    return 0

        



if __name__ == "__main__":
    mat=[[0,1,1],[1,1,1],[0,1,0]]
    print(function(mat))