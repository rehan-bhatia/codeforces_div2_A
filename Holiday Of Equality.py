n = int(input())
a = list(map(int, input().split()))
z = max(a)
count = 0
for i in range(n):
    count += z-a[i]
print(count)
