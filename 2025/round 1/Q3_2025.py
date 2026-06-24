
# print(ord("a"))
# print(ord("z"))

test = input("")
count = 0
word = ''
for letter in test:
    if ord(letter) >= ord("a") and ord(letter) <= ord("z"):
        count += 1
        plain = ord(letter) -count

        while plain < ord("a"):
        # if plain < ord("a"):
            plain = plain + 26
        word += chr(plain)
        
    else:
        word += letter
        count = 0

print(word)