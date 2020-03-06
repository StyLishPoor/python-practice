"""
def mergeSort(L):
    print(L)
    if len(L) == 2:
        if L[0] <= L[1]:
            return [L[0],L[1]]
        else:
            return [L[1],L[0]]
    elif len(L) == 1:
        return [L[0]]
    else:
        middle = len(L) // 2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        print('left:',left,'right',right)
        return merge(left,right)

def merge(left,right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

input = [1,19,3,-7,5,0,2]
output = mergeSort(input)

print(output)
"""
def recursiveTile(yard,size,originR,originC,rMiss,cMiss,nextPlace):
    #c:列,r:行
    #nextPiece:ヘルパー変数，タイルを置く順番を割り振る
    quadMiss = 2*(rMiss >= size//2) + (cMiss >= size//2)
    if size == 2: #基底部
        piecePos = [(0,0),(0,1),(1,0),(1,1)]
        piecePos.pop(quadMiss)
        for (r,c) in piecePos:
            yard[originR + r][originC + c] = nextPlace
        nextPlace += 1
        return nextPlace
    else:
        for quad in range(4):
            shiftR = size//2 * (quad >= 2)
            shiftC = size//2 * (quad % 2 == 1)
            if quad == quadMiss:
                nextPlace = recursiveTile(yard,size//2,originR+shiftR,originC+shiftC,rMiss-shiftR,cMiss-shiftC,nextPlace)
            else:
                newrMiss = (size//2-1) * (quad < 2)
                newcMiss = (size//2-1) * (quad % 2 == 0)
                nextPlace = recursiveTile(yard,size//2,originR+shiftR,originC+shiftC,newrMiss,newcMiss,nextPlace)
        #最後に中央部にタイルを置く
        centerPos = [(r + size//2 - 1,c + size//2 -1) for (r,c) in [(0,0),(0,1),(1,0),(1,1)]]
        centerPos.pop(quadMiss)
        for (r,c) in centerPos:
            yard[originR + r][originC + c] = nextPlace
        nextPlace += 1
        return nextPlace #基底部外でもreturnしないと基底部にたどり着かない

def CanTile(n,missPos):
    size = 2**n
    dimlist = []
    allDiferrent = True
    #4つの象限が全て異なるかチェック
    for pos in missPos:
        dim = 2*(pos[0] >= size//2) + (pos[1] >= size//2)
        if dim in dimlist:
            allDiferrent = False
            break
        else:
            dimlist.append(dim)
    if allDiferrent:
        return True
    #3つにトロミノが当てはまるかチェック
    
    for first in missPos:
        r_check,c_check = False,False
        test = missPos[:]
        test.remove(first)
        for second in test:
            if abs(second[0]-first[0])==1 and second[1] == first[1]:
                c_check = True
                continue
            if abs(second[1]-first[1])==1 and second[0] == first[0]:
                r_check = True
                continue
        if c_check and r_check:
            return True
    return False

EMPTYPIECE = -1
def tileMissingYard(n,rMiss,cMiss):
    yard = [[EMPTYPIECE for i in range(2**n)] for j in range(2**n)]
    
    recursiveTile(yard,2**n,0,0,rMiss,cMiss,0)
    
    return yard

def printYard(yard):
    for i in range(len(yard)):
        row = '' 
        for j in range(len(yard[0])):
            if yard[i][j] != EMPTYPIECE:
                row += chr((yard[i][j] % 26) + ord('A'))
            else:
                row += ' '
        print(row)

#printYard(tileMissingYard(5,20,11))
#print(CanTile(3,[(0,0),(6,1),(1,6),(6,6)]))

def binarySearch(num,T,minR=0,minC=0,count=0):
    print(minR,minC)
    print(T)
    searchR = (len(T)-1)//2 
    searchC = (len(T[0])-1)//2 
    print("search",searchR,searchC,T[searchR][searchC])
    if (T[searchR][searchC]) == num:
        print("Found")
        return searchR+minR,searchC+minC
    elif len(T) == 1:
        print("next")
        return -1,-1

        """
        searchR = (len(T)-1)//2 
        print("min",minR,minC)
        searchC = (len(T[0])-1)//2 
        print("search",searchR,searchC,T[searchR][searchC])
        
    
        
            if(T[searchR][searchC]==num):
            print("Correct")

            return searchR+minR,searchC+minC
        """
    elif(T[searchR][searchC] > num):
        nextT = []
        for i in range(searchR+1):

            nextT.append(T[i][:searchC+1]) 
        return binarySearch(num,nextT)
    else:
        right = []
        down = []
        diag = []
        for i in range(searchR+1):
            right.append(T[i][searchC+1:])
        minC = searchC + 1
        for i in range(searchR+1,len(T)):
            down.append(T[i][:searchC])
        minR = searchR + 1
        for i in range(searchR+1,len(T)):
            diag.append(T[i][searchC+1:])
        minR,minC = searchR+1,searchC+1
        binarySearch(num,right)
        binarySearch(num,down)
        binarySearch(num,diag)
        return searchR,searchC

T = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(binarySearch(11,T))





