phrase = input()

vowels = ['a','e','i','o','u']

final = ""
for letter in phrase:
    if (letter not in vowels) and (ord(letter) >= ord('a')) and (ord(letter) <= ord('z')):
        final += f"{letter}o{letter}"
    else:
        final += letter
    
print(final)
