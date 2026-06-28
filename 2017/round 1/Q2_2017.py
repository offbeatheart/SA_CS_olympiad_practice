
a,b,c = map(int,input().split())
n = int(input())

tri = [a,b,c]

while len(tri) < n:
    tri.append(tri[-1] + tri[-2] + tri[-3])

print(tri[n-1])