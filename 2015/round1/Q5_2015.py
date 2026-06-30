import math
n = int(input())

precalc = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def prime(num):
    global precalc
    if num in precalc:
        return True 
    if num < precalc[-1]:
        return False 
    for number in range(2,int(math.sqrt(num))+1):
        if not num%number:
            return False 
    
    precalc.append(int(num))
    return True 

def factors(num):
    factors_list = []

    for number in range(1,((num)//2)+1):
        if not num % number:
            factors_list.append(number)

            
    factors_list.append(num)
    return factors_list

total = 0
valid_factors = []
for number in range(1,n+1):
    valid_number = True 
    
    factor_list = factors(number)

    for factor in factor_list:
        if factor in valid_factors:
            pass
        elif prime(factor +(number/factor)):
            pass
        else:
            valid_number = False
    
    if valid_number:
        valid_factors.append(number)
        print(valid_factors)
        total += number

print(total)

