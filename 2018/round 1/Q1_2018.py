d,e,w = map(int,input().split())


sum = e *70 + w*50
if d >= 100:
    d -= 100
    sum += d*80
    total =str(sum)+ 'c'
else:
    total =str(sum) + 'c'

print(total)

