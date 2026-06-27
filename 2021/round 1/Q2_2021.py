n = int(input())

sum = 0

for num in range(n):
    top=1 +num
    btm = 2+num
    sum += top/btm


print(round(sum,2))