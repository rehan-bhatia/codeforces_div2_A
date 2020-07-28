n = int(input())
u = []
l = []
for _ in range(n):
    x = input().split()
    u.append(int(x[0]))
    l.append(int(x[1]))
 
if sum(u)%2==0 and sum(l)%2==0:
    print(0)
elif sum(u)%2==1 and sum(l)%2==1:
    out = False
    for i in range(n):
        if u[i]%2 != l[i]%2:
            out = True
            break
    if out:
        print(1)
    else:
        print(-1)
else:
    print(-1)
