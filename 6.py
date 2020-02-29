def compare(groupA,groupB):
    if(sum(groupA) > sum(groupB)):
        return 'left'
    elif(sum(groupA) < sum(groupB)):
        return 'right'
    else:
        return 'equal'

def splitCoins(coin):
    size = len(coin)
    split = size//3
    coin_1 = coin[0:split*1]
    coin_2 = coin[split*1:split*2]
    coin_3 = coin[split*2:split*3]
    return coin_1,coin_2,coin_3

def detect_Fake(group1,group2,group3):
    #fakeが重たいとわかっている場合
    """
    if(compare(group1,group2) == 'left'):
        return group1
    elif(compare(group1,group2) == 'right'):
        return group2
    else:
        return group3
    """
    #fakeが重いか軽いか分からない場合
    if(compare(group1,group2) == 'equal'):
        if(compare(group1,group3) == 'equal'):
            return "equal"
        else:
            return group3
    else:
        if(compare(group1,group3) == 'equal'):
            return group2
        else:
            return group1
def CoinComparision(coinlist):
    counter = 0
    currList = coinlist
    while(len(currList) > 1):
        coin_1,coin_2,coin_3 = splitCoins(currList)
        currList = detect_Fake(coin_1,coin_2,coin_3)
        counter += 1
        if(currList == 'equal'):
            break
    if(currList == 'equal'):
        print('No fake coin')
    else:
        fake = currList[0]
        print('The fake coin is at ',coinlist.index(fake)+1)
        print('Numbers of weightings: ',counter)

coin = list(map(float,input("coin list: ").split()))
CoinComparision(coin)
