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

# to_do = [-1,0,1,2,3,4,7,9,10,20]
# print(binary_search(to_do,0,len(to_do),10))


def merge_sort(group):

    if len(group) == 1 :#or len(group) ==0:
        
        return group
    if len(group) == 2:
        if  group[0] > group[1]:
            return [group[1] , group[0]]
        else:
            
            return group
    else:
        meridian   = (len(group) // 2)

        return merge(merge_sort(group[:meridian]),merge_sort(group[meridian:]))

def merge(groupA,groupB):
    new_group = []
    index1 = 0
    index2 = 0

    while index1 < len(groupA) and index2 < len(groupB):
        if groupA[index1] > groupB[index2] :
            new_group.append(groupB[index2])
            index2 += 1
        else:
            new_group.append(groupA[index1])
            index1 += 1
    
    if index1 < len(groupA):
         while index1 < len(groupA):
            new_group.append(groupA[index1])
            index1 += 1
             
    else:
        while index2 < len(groupB):
            new_group.append(groupB[index2])
            index2 += 1
    return new_group
        
def subset(group,curr):
    pass

    subset()




