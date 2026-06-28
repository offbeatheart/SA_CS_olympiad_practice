tower_num = int(input())
tower_height = list(map(int,input().split()))

communicable_pairs = []
faux_tower = tower_height.copy()
# print(tower_height)
for main_tower in tower_height:
    faux_tower.remove(main_tower)
    # print(main_tower,faux_tower)
    
    
    for comparison_tower in faux_tower:

        if main_tower < comparison_tower:
            pair =[main_tower,comparison_tower]
        else:
            pair = [comparison_tower,main_tower]

        

           
        if abs(main_tower - comparison_tower) <=10:
            if pair in communicable_pairs:
                pass
            # else:
                # if pair[0] == pair[1]:
                #     if (tower_height.count(pair[0]) > 1):
                #         communicable_pairs.append(pair)
                #     else:
                #         pass
                # else:
            communicable_pairs.append(pair)
        else:
            pass
        
print(len(communicable_pairs))
# print((2,1) ==(1,2))