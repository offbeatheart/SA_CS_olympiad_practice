carpet = input()

carpet_length = len(carpet)

used_colour = []
for char in carpet:
    if char not in used_colour:
        used_colour.append(char)

result = carpet_length*len(used_colour)

print(result)
