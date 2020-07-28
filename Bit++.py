n = int(input())
out = 0
for _ in range(n):
    a = input()
    if "++" in a:
        out+=1
    elif "--" in a:
        out-=1
print(out)
