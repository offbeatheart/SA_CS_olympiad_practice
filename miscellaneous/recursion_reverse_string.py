def revserse(sentence):
    if sentence == "":
        print(sentence)
        return sentence
    else:
        return revserse(sentence[1:]) + sentence[0]
    
# print(revserse("hello"))

def palindrome(sentence):
    if sentence == "" or len(sentence) == 1:
        return True
    else:
        if sentence[0] == sentence[-1]:
            return palindrome(sentence[1:-1])
    
    return False
    
    
# print(palindrome("racecar"))


def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    return decimal_to_binary(decimal //2 ) + str(decimal%2) 

# print(decimal_to_binary(1))

def sum_natural_numbers(num): # can only recursively call sum up to 998 items in the stack thus while being an o(n) function thus memory ran out before the time got too out of hand
    if num == 0:
        return num 
    return num + sum_natural_numbers(num -1)
    
print(sum_natural_numbers(998))

def iterative_sum_natural_numbers(num):
    sum = 0
    for i in range(1,num+1): sum += i
    return sum

print(iterative_sum_natural_numbers(5000000))