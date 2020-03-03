#Talents = ['Sing','Dance','Magic','Act','Flex','Code']
Talents = [1,2,3,4,5,6,7,8,9]
Candidates = ['A','B','C','D','E','F','G']

CandidateTalent = []
print("All talents is below")
print(Talents)
"""
for c in Candidates:
    talent = list(map(int,input("Input "+c+" talent: ").split()))
    CandidateTalent.append(talent)
#CandidateTalent = [['Flex','Code'],['Dance','Magic'],['Sing','Magic'],
#                    ['Sing','Dance'],['Dance','Act','Code'],['Act','Code']]
"""
CandidateTalent = [[4,5,7],[1,2,8],[2,4,6,9],[3,6,9],[2,3,9],[7,8,9],[1,3,7]]
def Hire4show(candlist,talentlist,candtalent):
#candlist: 人のリスト
#talentlist: タレントのリスト
#candtalent: 人とタレントの対応関係
    onlytalent = OnlyTalent(candtalent,talentlist)

    invitelist = candlist
    checklist = []
    min_num = len(invitelist)
    cand_num = len(candlist)
    for i in range(2**cand_num):
        num = i
        for j in range(cand_num):
            if(num % 2 == 0):
                checklist = [candlist[cand_num-1-j]] + checklist
            num //= 2
       # print(checklist)
       # print(id(talentlist))

       # print(checklist)
        if((ContainAllTalent(checklist,talentlist,candtalent) == True) and (len(checklist) < min_num)):
            
            invitelist = checklist
            min_num = len(checklist)
        checklist = []
    print("invite: ",invitelist)


def ContainAllTalent(check,talent,candtalent):
    remaintalent = talent[:]
    """
    リストの代入だけではidが変更されず，参照先は変更されない。
    remaintalent = talentではコピーになっていない
    スライス[:]で新しいリストを作成するか，copyモジュールを利用してコピーすること
    """
    #print(id(remaintalent))
    for c in check:
        index = Candidates.index(c)
        for d in candtalent[index]:
            if(d in remaintalent):
                remaintalent.remove(d)
    #print(remaintalent)            
    if(len(remaintalent)==0):
        return True
    return False

def OnlyTalent(candtalent,talentlist):
    talent_num = 0
    only = []
    for c in talentlist:
        print(c)
        for i,d in enumerate(candtalent):
            print(d)
            if(c in d):
                talent_num += 1
                talent_name = Candidates[i]
        print(talent_num)
        if(talent_num == 1):
            only.append(talent_name)
        talent_num = 0
    print("only",only)
    return only

Hire4show(Candidates,Talents,CandidateTalent)

