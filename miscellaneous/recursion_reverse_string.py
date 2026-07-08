def revserse(sentence):
    if sentence == "":
        print(sentence)
        return sentence
    else:
        return revserse(sentence[1:]) + sentence[0]
    
print(revserse("hello"))

def palindrome(sentence):
    if sentence == "" or len(sentence) == 1:
        return True
    else:
        if sentence[0] == sentence[-1]:
            return palindrome(sentence[1:-1])
    
    return False
    
    
print(palindrome("racecar"))


def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'

    return decimal_to_binary(decimal //2 ) + str(decimal%2) 

print(decimal_to_binary(1))