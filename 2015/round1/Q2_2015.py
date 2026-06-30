kind_marbles = int(input())
marbles = list(map(int,input().split()))

most = 0
for num in range(len(marbles)):
    if marbles[num] > most:
        most = marbles[num]

needed = 0
for marble in marbles:
    needed += (most - marble)

print(needed)
