angleList= list(map(int,input().split()))

if sum(angleList) != 180:
    print("IMPOSSIBLE")
else:
    if angleList.count(angleList[0]) == 3:
        print("EQUILATERAL")
    elif angleList.count(angleList[0]) == 2:
        print("ISOSCELES")
    elif angleList.count(angleList[1]) == 2:
        print("ISOSCELES")
    else:
        print("SCALENE")
