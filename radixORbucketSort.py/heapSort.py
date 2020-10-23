def maxHeapyfy(graphList):
    len1=len(graphList)
    rangeOFleafnodes=[int(len1/2),len1-1]
    flag=0
    
    for val in range(rangeOFleafnodes[0]):
        i=rangeOFleafnodes[0]-1-val
        leftChild=(i*2)+1
        rightChild=(i*2)+2

        if leftChild<len1:
            if rightChild<len1:
                if graphList[leftChild]<graphList[rightChild]:
                    if graphList[rightChild]>graphList[i]:
                        tmp=graphList[i]
                        graphList[i]=graphList[rightChild]
                        graphList[rightChild]=tmp
                        flag=1
                else:
                    if graphList[i]<graphList[leftChild]:
                        tmp = graphList[i]
                        graphList[i]= graphList[leftChild]
                        graphList[leftChild]=tmp
                        flag=1
            else:
                if graphList[i]<graphList[leftChild]:
                        tmp = graphList[i]
                        graphList[i]= graphList[leftChild]
                        graphList[leftChild]=tmp
                        flag=1
      
    if flag==1:
        graphList=maxHeapyfy(graphList)

    return graphList

def heapSort(graphList):
    len1=len(graphList)
    for i in range(len1):
        tmpList = maxHeapyfy(graphList)
        print(graphList.pop(0))
n

if __name__ == "__main__":
    heapSort([5,3,7,8])