sandlength = int(input())
sandcastle = list(map(int,input().split()))

sandcastle.append(0)
sandcastle = [0] +(sandcastle)

change = True 
total = 0
# while change:
#     change = False 
while change:
    change = False
    for grain in range(len(sandcastle)):

        if (grain == 0 ) or (grain == len(sandcastle) -1) :
            pass

        
        elif (sandcastle[grain] - sandcastle[grain+1] >=2) or (sandcastle[grain] - sandcastle[grain-1] >=2):
            sandcastle[grain]-= 2
            sandcastle[grain-1] +=1
            sandcastle[grain+1] +=1
            change = True

            total += sandcastle[0] + sandcastle[-1]
            sandcastle[0],sandcastle[-1] = 0,0
             


print(total )