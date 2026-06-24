def armstrong(num): 
    total = 0 

    for digit in str(num):
        total += int(digit) ** len(str(num))

    if total == num:
        return True 
    else:
        return False 
    

armstrong_list = []
for num in range(100,501):
    if armstrong(num):
        armstrong_list.append(num)

print(armstrong_list[0])
print(armstrong_list[1])
print(armstrong_list[2])
print(armstrong_list[3])

