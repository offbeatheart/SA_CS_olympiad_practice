import math
n = int(input())

def prime(num):
    for number in range(2,int(math.sqrt(num) + 1)):
        if num%number == 0:
            return False
    return True 

precalc = [2,3,5,7,11]

num_prime = 5
prime_num = precalc[-1]
if n > num_prime:

    
    while n > num_prime:
        prime_num += 2
        if prime(prime_num):
            precalc.append(prime_num)
            num_prime += 1

    print(precalc[-1])
else:
    print(precalc[n-1])

