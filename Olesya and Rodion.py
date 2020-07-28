n,t = map(int, input().split())
out = "1"
for i in range(n-1):
    out += "0"
out = int(out)
x = out % t
out += t - x
if len(str(out)) != n:
    print(-1)
else:
    print(out)
