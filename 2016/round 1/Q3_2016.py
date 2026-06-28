plaintext = input().upper()
N = int(input())
half = plaintext[-N:]+plaintext[:-N]

# print(half)
full = ""
for letter in half:
    temp = ord(letter)  + N

    while temp > ord("Z"):
        temp -= abs(ord('Z') - ord('A')) +1

    
    full += chr(temp)


print(full)