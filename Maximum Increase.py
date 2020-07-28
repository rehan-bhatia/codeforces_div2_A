n = int(input())
a = list(map(int, input().split()))
out = [1]*n
i=1
while i<n:
    if a[i-1] < a[i]:
        out[i] = out[i-1] + 1
    i+=1
print(max(out))
