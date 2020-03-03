hate = [('A','B'),('A','E'),('A','F'),('B','C'),('C','D'),('D','E'),('E','F')]
def Comnibantions(n,guestlist):
    checklist = []
    invitelist = []
    for i in range(2**n):
        num = i #numを２進数に変換
        for j in range(n):
            if num % 2 == 0:
                checklist.append(guestlist[n-1-j])
            num //= 2
        checklist.sort()
        invitelist.append(checklist)
        checklist = []
    invitelist = remove_hate(invitelist,hate)
    decide_max(invitelist)
def remove_hate(guestlist,hatelist):
    ans = []
    hate_falg = False
    for c in guestlist:
        for d in hatelist:
            if((d[0] in c) and (d[1] in c)):
                hate_falg = True
                break
        if(hate_falg == False):
            ans.append(c)
        else:
            hate_falg = False
    return ans
def decide_max(guestlist):
    people_max = 0
    max_group = []
    for c in guestlist:
        if(len(c) > people_max):
            max_group = c
            people_max = len(c)
    print('Best group: ',max_group)

def Comnibantions_good_memory(n,guestlist):
    checklist = []
    #nvitelist = []
    bestlist = []
    like = 0
    like_check = 0
    for i in range(2**n):
        num = i #numを２進数に変換
        for j in range(n):
            if num % 2 == 0:
                checklist.append(guestlist[n-1-j][0])
                like_check += int(guestlist[n-1-j][1])
            num //= 2
        checklist.sort()
        if(isGoodGroup(checklist,bestlist,hate) == True):
            if(like_check > like):
                bestlist = checklist
                like = like_check
        checklist = []
        like_check = 0
    print("Best Group: ",bestlist)

def isGoodGroup(check,best,hate):
    #嫌い会う人がいるかチェック
    for d in hate:
        if((d[0] in check) and (d[1] in check)):
                return False
    """
    if(like_tmp < like):
        return False
    elif(like_tmp > like):
        return True
    else:
        if(len(check) > len(best)):
            return True
        else:
            return False
    """
    return True
"""
def calculate_like(guest):
    like = 0
    for c in guest:
        like += int(c[1])
    return like
"""
def test_Combination(n,guestlist):
    allCombL = []
    for i in range(2**n):
        num = i
        clist = []
        for j in range(n):
            if num % 2 == 0:
                clist = [guestlist[n-1-j]]+clist #リストの連結
            num //= 2
        allCombL.append(clist)
    print("allCombL: ",allCombL)
guest = [('A',2),('B',6),('C',3),('D',10),('E',3),('F',5)]
print("all guest: ",guest)
print("hate combination: ",hate)
#Comnibantions(len(guest),guest)
Comnibantions_good_memory(len(guest),guest)
#test_Combination(len(guest),guest)