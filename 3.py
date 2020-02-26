from operator import itemgetter
deck = ['1_C','1_D','1_H','1_S','2_C','2_D','2_H','2_S','3_C','3_D','3_H','3_S',
        '4_C','4_D','4_H','4_S','5_C','5_D','5_H','5_S','6_C','6_D','6_H','6_S',
        '7_C','7_D','7_H','7_S','8_C','8_D','8_H','9_C','9_D','9_H','9_S','9_C',
        '10_C','10_D','10_H','10_S','11_C','11_D','11_H','11_S',
        '12_C','12_D','12_H','12_S','13_C','13_D','13_H','13_S']


def AssistantOrdersCards():

    print('Cards are character strings as shown below.')
    print('Ordering is:',deck)
    selected_card = list(input("Select 5 cards: ").split()) # 5枚のカードを格納
    print('your cards:',selected_card)
    suit1,suit2 = choose_suit(selected_card)
    hiden,first,distance = decide_hiden_and_first_card(suit1,suit2)
    #hiden_suit = hiden[-1]
    #print(distance,hiden_suit)
    selected_card.remove(hiden)
    selected_card.remove(first)
    order = order_sort(selected_card)
    card_for_show(distance,order)
    print("First: "+first+", Second: "+order[0]+", Third: "+order[1]+", Fourth: "+order[2])
    print("Hiden card: "+hiden)
    to_magician = order.insert(0,hiden)
    return to_magician


def choose_suit(card):
    suit_list = ([],[],[],[])
    for i,c in enumerate(card):
        if(c[-1] == 'C'):
            suit_list[0].append(i)
        elif(c[-1] == 'D'):
            suit_list[1].append(i)
        elif(c[-1] == 'H'):
            suit_list[2].append(i)
        else:
            suit_list[3].append(i)
    for c in suit_list:
        if(len(c) >= 2):
            return card[c[0]],card[c[1]]

def card_to_num(card):
    if(len(card)==len('X_X')):
        return int(card[0])
    elif(len(card)==len('XX_X')):
        return int(card[0:2])

def decide_hiden_and_first_card(first,second):
    first_num = card_to_num(first)
    second_num = card_to_num(second)
    if(first_num > second_num):
        big,small = first,second
    else:
        big,small = second,first
    dis = max(first_num,second_num)-min(first_num,second_num)
    if(dis <= 6):
        return big,small,dis
    else:
        return small,big,13-dis

def order_sort(card):
    tmp = []
    order = []
    for c in card:
        tmp.append((c,deck.index(c)))
    tmp = sorted(tmp,key=itemgetter(1))
    print(tmp)
    for c in tmp:
        order.append(c[0])
    return order
def card_for_show(dis,card):
    if(dis == 1):
        pass
    elif(dis == 2):
        card[1],card[2] = card[2],card[1]
    elif(dis == 3):
        card[0],card[1] = card[1],card[0]
    elif(dis == 4):
        card[0],card[1],card[2] = card[1],card[2],card[0]
    elif(dis == 5):
        card[0],card[1],card[2] = card[2],card[0],card[1]
    else:
        card[0],card[1],card[2] = card[2],card[1],card[0]

def MagicianGuess(card):
    print(card)
    print('Guess hiden number')
    print("First: "+card[0]+", Second: "+card[1]+", Third: "+card[2]+", Fourth: "+card[3])
    suit = card[-1]
    hint_num = card_to_num(card[0])
    rank  = []
    for i in range(3):
        rank.append(deck.index(card[i+1]))
    dist = decide_dist(rank)
    print("Ans: Suit is "+suit+", and Number is "+str((hint_num+dist)%13))
def decide_dist(rank_list):
    if(rank_list[0] < rank_list[1] and rank_list[0] < rank_list[2]):
        if(rank_list[1] < rank_list[2]):
            return 1
        else:
            return 2
    elif(rank_list[0] > rank_list[1] and rank_list[0] < rank_list[2]):
        return 3
    elif(rank_list[0] < rank_list[1] and rank_list[0] > rank_list[2]):
        return 4
    elif(rank_list[0] > rank_list[1] and rank_list[0] > rank_list[1]):
        if(rank_list[1] < rank_list[2]):
            return 5
        else:
            return 6


magic_card = AssistantOrdersCards()   
print(magic_card)
MagicianGuess(magic_card)
