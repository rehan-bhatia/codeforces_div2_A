n = int(input())
a = list(map(int, input().split()))
c1 = 0
c0 = 0
max0 = -1
for i in range(n):
    if a[i]==1:
        c1 +=1
        if c0 > 0:
            c0 -= 1
    else:
        c0 +=1
        if c0 > max0:
            max0 = c0
            
print(c1 + max0)
