fertilizer = {"a":5,"e":5,"i":5,"o":5,"u":5,'b':3, 'c':3, 'd':3, 'f':3, 'g':3}

tree = input().lower()

speed = 0
for letter in tree:
    if letter in fertilizer:
        speed += fertilizer[letter]
    else:
        speed += 2

if speed < 25:
    print("Slow")
elif speed <= 35:
    print("Medium")
else:
    print("Fast")

