k = int(input())
s = list(input())
a = set(s)
output=""
out = True
for i in a:
    x = s.count(i)
    if x%k==0:
        output = output + (i * (x//k))
    else:
        out = False
        break
if out:
    print((output) * (len(s)//len(output)))
else:
    print(-1)
