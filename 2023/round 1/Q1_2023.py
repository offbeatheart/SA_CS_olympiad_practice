import math
x,y = input().split()

if math.sqrt(float(x)**2 + float(y)**2) > 1:
    print("BLUE")
else:
    print("RED") 

    