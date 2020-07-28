a = list(map(int, input().split()))
s = input()
out = 0
for i in range(1,5):
    x = s.count(str(i))
    z=x*a[i-1]
    out += z
print(out)
