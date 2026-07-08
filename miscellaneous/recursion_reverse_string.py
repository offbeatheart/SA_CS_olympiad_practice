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
    
# print(sum_natural_numbers(998))

def iterative_sum_natural_numbers(num): # can handle foar larger numbers without hitting the space limit 
    sum = 0
    for i in range(1,num+1): sum += i
    return sum

# print(iterative_sum_natural_numbers(5000000))

def binary_search(group,left, right,desired):

    if left > right:
        return -1

    mid = (left + right) //2

    if group[mid] == desired:
        return mid
    elif desired <  group[mid]:

        return binary_search(group,left,mid-1,desired)
    
    return binary_search(group,mid +1,right,desired)

to_do = [-1,0,1,2,3,4,7,9,10,20]
print(binary_search(to_do,0,len(to_do),10))
    # if group == [desired]:
    #     return 0
    
    # maradien = (len(group) //2) 

    # if group[maradien] > desired:
    #     return binary_search(group[:maradien],desired) 
    # elif group[maradien] < desired:
    #     print(maradien, group[maradien:])
    #     return binary_search(group[maradien:],desired) + len(group[:maradien])
    # else:
    #     return len(group[:maradien])
    
# to_do = [1,2,3,4,5,6,7,8,9,10]

# print(binary_search(to_do,10))
