n = int(input())
nfib =[0,1]

while len(nfib) < n +1:
    nfib.append(nfib[-2] + nfib[-1])

if n == 0:
    print(0)
else:
    print(nfib[-1])


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n -1) + fib(n - 2)

print(fib(100))