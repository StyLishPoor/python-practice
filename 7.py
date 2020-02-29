def findSquare_withinError(x,epsilon,increment):
    esti = 0.0
    while(x-esti**2 > epsilon):
        esti += increment
    if(abs(x-esti**2) > epsilon):
        print("Failed on square root of",x)
    else:
        print(esti," is close to root of ",x)

def bisectionSearchForSquareRoot(x,epsilon):
    min = 0
    max = x
    center = (max-min)/2.0
    while(abs(x-center**2) > epsilon):
        if(x - center**2 > 0): # centerが小さすぎる
            min = center
            center = center + (max - center)/2.0
        else: #centerが大きすぎる
            max = center
            center = min + (center - min)/2.0
    print(center,' is close to root of ',x)
    

x = int(input("input integer: "))
ep = float(input("input epsilon: "))
#inc = float(input("input increment: "))
#findSquare_withinError(x,ep,inc)

bisectionSearchForSquareRoot(x,ep)