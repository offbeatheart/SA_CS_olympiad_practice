number = int(input())

wheat = 0.5
total = 0
for tile in range(1,number +1):
    wheat = wheat * 2
    if tile%2:        
        total += wheat
    

print(int(total))