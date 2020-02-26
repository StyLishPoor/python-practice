from operator import itemgetter
def CelebrityCount(time):
    arrive_celeb = []
    maxcount = 0 
    best_time = time[0][0]
    for i,c in enumerate(time):
        arrive_celeb.append(i)
        for j in arrive_celeb:
            if(c[0] >= time[j][1]):
                #帰った有名人を削除
                arrive_celeb.remove(j)
        if(len(arrive_celeb) > maxcount):
            maxcount,best_time = len(arrive_celeb),c[0]
    
    print("best time: " +str(best_time))
    print("celebrity num: " + str(maxcount))

def CelebrityCount_limit(time,ystart,yend):
    arrive_celeb = []
    maxcount = 0 
    #best_time = ystart
    #ystartの時点でいる人を求める
    for i,c in enumerate(time):
        if(c[0] <= ystart):
            if(c[1] > ystart):
                arrive_celeb.append(i)
                maxcount = len(arrive_celeb)
        else:
            if(c[0] < yend):
                arrive_celeb.append(i)
                for j in arrive_celeb:
                    if(c[0] >= time[j][1]):
                        arrive_celeb.remove(j)
                if(len(arrive_celeb) > maxcount):
                    maxcount = len(arrive_celeb)   
    print("maxnum: "+str(maxcount))
    """
    for i,c in enumerate(time):
        arrive_celeb.append(i)
        for j in arrive_celeb:
            if(c[0] >= time[j][1]):
                #帰った有名人を削除
                arrive_celeb.remove(j)
        if(len(arrive_celeb) > maxcount):
            maxcount,best_time = len(arrive_celeb),c[0]
    
    print("best time: " +str(best_time))
    print("celebrity num: " + str(maxcount))
    """
def my_sort(t_list):
    #listのkey番目の要素でsort
    #key = int(input("key: "))
    key = 0
    for i in range(len(t_list)):
        min = t_list[i][key]
        min_index = i
        for j in range(i,len(t_list)):
            if(t_list[j][key] < min):
                min = t_list[j][key]
                min_index = j
        t_list[i], t_list[min_index] = t_list[min_index],t_list[i]
    return t_list




celeb_num = int(input("Celebrity Num: "))
time_list = []
for i in range(celeb_num):
    time = tuple(map(int,input("No."+str(i)+": ").split()))
    time_list.append(time)
#sort_time_list = sorted(time_list,key=itemgetter(0))
sort_time_list = my_sort(time_list)
#print(sort_time_list)



#CelebrityCount(sort_time_list)
CelebrityCount_limit(sort_time_list,10.1,10.9)
