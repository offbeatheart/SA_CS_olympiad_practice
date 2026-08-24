moves = list(input())
# moves = ['L','U','R','D']
past = {(0,0)}


flag = False
x =0
y =0
for move in moves:

    if move == 'U':
        y += 1
    elif move == "D":
        y -= 1
    if move == 'R':
        x += 1
    elif move == "L":
        x -= 1

    if (x,y) in past:
        flag = True
        break
    else:
        past.add((x,y))

if flag:
    print(len(past))
else:
    print(-1)
