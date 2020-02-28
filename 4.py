board_size = 4
#二次元配列による逐次探索
def noConflicts(board,current,qindex,n):
    #qindex行にクイーンがすでにあるかチェック
    for i in range(current):
        if board[qindex][i] == 1:
            return False
    #左上対角成分
    r_tmp = current-1
    g_tmp = qindex-1
    while(r_tmp >= 0 and g_tmp >= 0):
        if(board[g_tmp][r_tmp] == 1):
            return False
        g_tmp -= 1
        r_tmp -= 1    
    #左下対角成分
    r_tmp = current-1
    g_tmp = qindex+1
    while(r_tmp >= 0 and g_tmp <= n-1):
        if(board[g_tmp][r_tmp] == 1):
            return False    
        g_tmp += 1
        r_tmp -= 1
    #衝突なし        
    return True
#一次元配列での簡潔化
def noConflicts_breef(board,current):
    for i in range(current):
        if(board[i] == board[current]):
            return False
        if((current-i) == abs(board[i]-board[current])):
            return False
    return True
        
def FourQueens(n = board_size):
    board = []
    for i in range(n):
        board.append([0]*n)
    #左端の列からクイーンを置いていく
    #1列目
    for i in range(n):
        board[i][0] = 1
        #2列目
        for j in range(n):
            board[j][1] = 1
            if(noConflicts(board,1,j,board_size)):
                for k in range(n):
                    board[k][2] = 1
                    if(noConflicts(board,2,k,board_size)):
                        for l in range(n):
                            board[l][3] = 1
                            if(noConflicts(board,3,l,board_size)):
                                print(board)
                            board[l][3] = 0
                    board[k][2] = 0    
            board[j][1] = 0
        board[i][0] = 0      
    return 
def SetQueens(n = board_size):
    board  = [-1]*n
    for i in range(n):
        board[0] = i
        for j in range(n):
            board[1] = j
            if(noConflicts_breef(board,1)):
                for k in range(n):
                    board[2] = k
                    if(noConflicts_breef(board,2)):
                        for l in range(n):
                            board[3] = l
                            if(noConflicts_breef(board,3)):
                                print(board)
    return 
#FourQueens(board_size)
SetQueens(board_size)

