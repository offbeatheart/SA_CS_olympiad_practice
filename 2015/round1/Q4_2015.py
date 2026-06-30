import math
denary = int(input())

n = 1
while math.factorial(n) <= denary:
    n += 1

n -= 1

final = ""
for num in range(n,0,-1):
    if denary/math.factorial(num) >= 1:
        temp = int(denary/math.factorial(num))
        denary -= (math.factorial(num) * temp)
        final += f" {str(temp)}"
    else:
        final +=" 0"

print(final[-1:0:-1])
