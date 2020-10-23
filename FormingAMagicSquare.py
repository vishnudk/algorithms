import numpy as np
import statistics as stc
def createMagicSquareWithoutnumpy(square):
    min=9999
    magicSquares=[[[8,1,6],[3,5,7],[4,9,2]],[[6,1,8],[7,5,3],[2,9,4]],[[4,9,2],[3,5,7],[8,1,6]],[[2,9,4],[7,5,3],[6,1,8]],[[8,3,4],[1,5,9],[6,7,2]],[[4,3,8],[9,5,1],[2,7,6]],[[6,7,2],[1,5,9],[8,3,4]],[[2,7,6],[9,5,1],[4,3,8]]]
    for mat in magicSquares:
        val=0
        for i in range(3):
            for j in range(3):
                val=val+abs(mat[i][j]-square[i][j])
        if min>val:
            min=val
    return min

def createMagicSquare(square):
    sqr=np.asarray(square)
    min=9999
    magicSquares=[[[8,1,6],[3,5,7],[4,9,2]],[[6,1,8],[7,5,3],[2,9,4]],[[4,9,2],[3,5,7],[8,1,6]],[[2,9,4],[7,5,3],[6,1,8]],[[8,3,4],[1,5,9],[6,7,2]],[[4,3,8],[9,5,1],[2,7,6]],[[6,7,2],[1,5,9],[8,3,4]],[[2,7,6],[9,5,1],[4,3,8]]]
    for i in magicSquares:
        val=(np.sum(np.absolute(np.subtract(sqr,i))))
        if min>val:
            min=val
    print(min)
if __name__ == "__main__":
    createMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]])
    createMagicSquareWithoutnumpy(([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))
    createMagicSquare([[4,8 ,2],[
4 ,5 ,7],[
6 ,1 ,6]])