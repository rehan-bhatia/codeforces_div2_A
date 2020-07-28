n = int(input())
a = list(map(int, input().split()))
x = max(a)
y = min(a)
count = a.index(x)
count += a[::-1].index(y)
if n - 1 - a[::-1].index(y) < a.index(x):
    count -= 1
print(count)
