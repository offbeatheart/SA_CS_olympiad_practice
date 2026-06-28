library = [
    ['O','N','E'],
    ['T','W','O'],
    ['T','H','R','E',"E"],
    ['F','O','U','R'],
    ['F','I','V','E'],
    ['S','I','X'],
    ['S','E','V','E','N'],
    ['E','I','G','H','T'],
    ['N','I','N','E']
]
alphabet_soup = ['O','N','E','T','W','H','R','U','F','S','V','I','G','X']
word = input()
new_word = []

for letter in word:
    if letter in alphabet_soup:
        new_word.append(letter)

temp_word = new_word.copy()

# print(temp_word)
final = ['N','O','N','E']
for book in library:
    temp_word = new_word.copy()
    match = 0
    for page in book:
        if page in temp_word:
            # print(f"{book[match]} {page}")

            match += 1
            temp_word = temp_word[temp_word.index(page):].copy()
            temp_word.remove(page)
        
        if match == len(book):
            final =book
            break

    if final != ['N','O','N','E']:
        break 
            
final_word = ""
for letter in final:
    final_word += letter

print(final_word)

# for letter in range(len(word)):
#     if word[letter] in library[letter]:
#         print("hmmm")
#     else:
#         pass
