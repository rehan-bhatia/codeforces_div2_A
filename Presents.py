n = int(input())
arr = list(map(int, input().split()))
out = [0] * n
for i in range(n):
    a = arr[i]
    out[a-1] = str(i+1)
print(" ".join(out))
