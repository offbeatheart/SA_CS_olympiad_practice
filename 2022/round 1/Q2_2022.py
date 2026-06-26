start_letter = input()

song = ""
letter = ord(start_letter)
while letter >= ord("a"):
    song += chr(letter)
    letter -= 2

print(song)