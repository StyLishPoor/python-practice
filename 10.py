def noConflicts(board,current):
#currentは新しくクイーンを置いた列
    for i in range(current):
        if(board[i] == board[current]):
            return False
        if(current-i == abs(board[current]-board[i])):
            return False
    return True

def rQueens(board,current,size,location):
    if(current == size):
        return True
    else:
        for i in range(size):
            if location[current] >= 0:
                board[current] = location[current]
            else:
                board[current] = i #iは列currentに置かれたクイーンの行
            if noConflicts(board,current):
                found = rQueens(board,current+1,size,location)
                if found:
                    return True
    return False

def nQueens(N,location):
    board = [-1] * N
    found = rQueens(board,0,N,location)
    if found:
        plot(board)
    else:
        print("No Solutions found")
    #print(board)

def plot(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[j] == i):
                print('Q',end=' ')
            else:
                print('•',end=' ')
        print('')
                
#locations = [-1,-1,4,-1,-1,-1,-1,0,-1,5]
#nQueens(10,locations)

#回文か決定する関数
def Palindrome(string):
    print(string)
    if len(string) <=1:
        print("return True")
        return True
    else:
        if string[0] == string[-1]:
            return Palindrome(string[1:-1])
        else:
            return False

def isPalindrome(string):
    check = string[:]
    found = Palindrome(check)
    print(found)
    if found:
        print(string,'is Palindrome')
    else:
        print(string,'is not Palindrome')

string = 'kouiok'
"""
print(string[0],string[-1])
string = string[1:-1]
print(string)
"""
isPalindrome(string)