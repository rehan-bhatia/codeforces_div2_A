n,m = map(int, input().split())
out = False
for i in range(n):
    z = input().split()
    if "C" in z or "Y" in z or "M" in z:
        out = True
        break
if out:
    print("#Color")
else:
    print("#Black&White")
