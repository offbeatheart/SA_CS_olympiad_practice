raw_mag = input().strip()

seperators = {',','-'}
for sep in seperators:
    raw_mag = raw_mag.replace(sep,' ')

word = raw_mag.split()

vowels =  {'a','e','i','o','u'}
for spell in word:
    if len(spell) < 5:
        continue


    if spell[0] not in vowels:
        continue

    if spell[-1] in vowels:
        continue

    flag = False
    for letter in range(len(spell)-1):
        if spell[letter] == spell[letter + 1] :
            flag = True
            break

    if flag == False:
        print(spell)
