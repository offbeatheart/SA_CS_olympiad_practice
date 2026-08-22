R,C = map(int,input().split())

whole = []

def template_gen(R,C):
    global whole
    temp = []
    for item in range(C):
        temp.append("a")

    for item in range(R):
        whole.append(temp.copy())

seq = []


template_gen(R,C)

for value in range(1,(R * C) + 1):
    if (value %(C - 1)) == 0:
        seq.append(value)

index = 1 


def indices():
    global whole
    index = -1
    prev = (seq[0]-1)%C
    total = 0
    for item in seq:
        
        value = (item-1)%C

        if prev >= value:
            index += 1
            
        prev = value

        total += whole[index][value]

    print(total)




def right(shift):
    global index, whole
    for item in range(0,len(whole[0])):
        if whole[0 + shift][item] == 'a':
            whole[0 + shift][item] = index
            index += 1 

def down(shift):
    global index, whole
    for item in range(0,len(whole)):
        if whole[item][-1 - shift] == 'a':
            whole[item][-1 - shift] = index
            index += 1 

def left(shift):
    global index, whole
    for item in range(len(whole[0]) -1 ,-1,-1):
        if whole[-1 - shift][item] == 'a':
            whole[-1 - shift][item] = index
            index += 1 

def up(shift):
    global index, whole
    for item in range(len(whole) -1 ,-1,-1):
        if whole[item][0 + shift] == 'a':
            whole[item][0+ shift] = index
            index += 1 

shift = 0
while True:
    try:
        right(shift)
    except:
        break
    try:
        down(shift)
    except:
        break
    try:
        left(shift)
    except:
        break
    try:
        up(shift)
    except:
        break

    shift += 1

indices()
