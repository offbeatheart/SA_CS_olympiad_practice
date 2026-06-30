word = input()

time = []
for letter in word:
    time.append(letter)
    
clock = time.copy()
clock.sort()

print(clock ==  time)