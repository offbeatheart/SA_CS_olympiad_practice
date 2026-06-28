p,r,t =map(float,input().split())


a= p +(p * (r/100) *t)

final = round(a,2)

final = str(final)

for digit in range(0,len(final)):

    if final[digit] =='.':
        decimal_point_index = digit

if abs((decimal_point_index +1) - len(final)) < 2:
    final += '0'

print(final)

