
n = int(input())

divsor_list = []
for number in range(1,n-1):

    if not n%number:
        divsor_list.append(number)
    
total = sum(divsor_list)

if total < n:
    print("Deficient")
elif total == n:
    print("Perfect")
else:
    print("Abundant")