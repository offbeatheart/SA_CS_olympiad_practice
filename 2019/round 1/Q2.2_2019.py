



import math
n = int(input())

def prime(num):

    if num == 1:
        return False 
    
    for number in range(2,int(math.sqrt(num) + 1)):
        if num%number == 0:
            return False
    return True 

def right_truncatable(num):
    num = str(num)
    for number in range(len(num)):
        if prime(int(num[:number +1])):
            pass
        else:
            return False 
    return True 

precalc = [2,3,5,7]

num_prime = 4
prime_num = precalc[-1]
if n > num_prime:

    
    while n > num_prime:
        prime_num += 2
        if right_truncatable(prime_num):
            precalc.append(prime_num)
            num_prime += 1

    print(precalc[-1])
else:
    print(precalc[n-1])
