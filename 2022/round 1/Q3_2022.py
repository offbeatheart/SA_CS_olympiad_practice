tower_num = int(input())
tower_height = list(map(int,input().split()))

communicable = []

for main_tower in tower_height:
    for comparison_tower in tower_height:
        print(main_tower,comparison_tower)
        

           
        if abs(main_tower - comparison_tower) <=10:
            if (main_tower,comparison_tower) in communicable:
                pass
            else:
                communicable.append((main_tower,comparison_tower))
        else:
            pass
        
print(communicable)
print((2,1) ==(1,2))