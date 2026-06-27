sentence = list(input().split("+"))

library =list(reversed(sorted(sentence)))

final_sentence = ""

for letter in library:
    final_sentence += f"{letter}+"

print(final_sentence[0:-1])