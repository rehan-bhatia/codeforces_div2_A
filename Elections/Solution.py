n,m = map(int, input().split())
a = [0]*n
for _ in range(m):
    z = list(map(int, input().split()))
    a[z.index(max(z))] += 1
print(a.index(max(a)) +1)
