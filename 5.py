
#n:階数，d:クリスタルの個数
def howHardIsCrystal(n,d):
    #decide radix
    r = 1
    while(r**d < n):
        r += 1
    print('Radix chosen is '+str(r))
    stairs = 0
    crystal_num = 1
    drop_num = 0
    for i in range(d):
        for j in range(1,r):
            check_stair = stairs + (r**(d-1-i))
            if(check_stair > n):
                break
            else:
                print("Drop ball "+str(crystal_num)+" from Floor "+str(check_stair))
                ans = input("Did the ball break (yes/no)?: ")
                drop_num += 1
                if(ans == "no"):
                    stairs = check_stair
                    continue
                else:
                    crystal_num += 1
                    break
    print("hard: "+str(stairs)+", drop num: "+str(drop_num))

n = int(input("input height: "))
d = int(input("input ball num: "))
howHardIsCrystal(n,d)