
def decimal_points(final):
    for digit in range(0,len(final)):

        if final[digit] =='.':
            decimal_point_index = digit

    if abs((decimal_point_index +1) - len(final)) < 2:
        final += '0'
    
    print(final)

sentence = input().lower()

post_processing = ""

for letter in sentence:
    if ((ord(letter) <= ord("z")) and (ord(letter) >= ord("a"))) or (letter == " "):
        post_processing += letter

book =  list(post_processing.split())

word_count = len(book)
word_length = 0

for word in book:
    word_length += len(word)

final = word_length/word_count

decimal_points(str(round(final,2)))