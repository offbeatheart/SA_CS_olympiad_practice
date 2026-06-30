word = input()

letter_bank = []
for letter in word:
    letter_bank.append(letter)

final = ""
for letter in letter_bank:
    if letter in final:
        pass
    else:
        final += f"{letter}{letter_bank.count(letter)}"
        
print(final)