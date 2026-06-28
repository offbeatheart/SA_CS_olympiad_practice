n = int(input())

divisors_list = []
for number in range(1,n):
    if not n%number:
        divisors_list.append(number)

print(sum(divisors_list))
