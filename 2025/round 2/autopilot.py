moves = list(input())
# moves = ['L','U','R','D']
past = [[0,0]]


flag = False
for move in moves:
    head = past[-1].copy()

    if move == 'U':
        head[1] += 1
    elif move == "D":
        head[1] -= 1
    if move == 'R':
        head[0] += 1
    elif move == "L":
        head[0] -= 1

    if head in past:
        flag = True
        break
    else:
        past.append(head)

if flag:
    print(len(past))
else:
    print(-1)


# flag = False
# pos= [0,0]
# for move in moves:
#     temp = []
#     if move == 'U':
#         temp = [pos[0], pos[1]+ 1]
#         pos[1] += 1
        
#     elif move == 'D':
#         temp = [pos[0], pos[1]- 1]
#         pos[1] -= 1
#     elif move == 'L':
#         temp = [pos[0]+1, pos[1]]
#         pos[0] -= 1
#     elif move == 'R':
#         temp = [pos[0]-1, pos[1]]
#         pos[0] -= 1

#     if pos in past:
#         flag = True 
#         break
#     elif move == ' ':
#         pass
#     else:
#         past.append(temp)

# if flag:
#     print(len(past)-1)
# else:
#     print(-1)