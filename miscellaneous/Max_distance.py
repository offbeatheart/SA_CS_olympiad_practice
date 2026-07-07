n = int(input())

x_cord = [int(x) for x in input().split()]
y_cord = [int(y) for y in input().split()]

max_distance = -1
for comp_cord in range(n):
    x_compare = x_cord[comp_cord]
    y_compare = y_cord[comp_cord]

    for cord in range(comp_cord + 1,n):
        distance = ((x_compare - x_cord[cord]) **2 +(y_compare - y_cord[cord]) **2)

        max_distance = max(max_distance,distance)

print(max_distance)