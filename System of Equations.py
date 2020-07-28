n,m = map(int, input().split())
count=0
for a in range(int(n**0.5)+1):
    b = n - (a**2)
    if b**2 + a ==m:
        count+=1
print(count)
