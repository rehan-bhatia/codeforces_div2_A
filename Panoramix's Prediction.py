n,m = map(int, input().split())
 
def prime(x):
    if x==2:
        return True
    elif x%2==0:
        return False
    elif x==3:
        return True
    else:
        for i in range(3, int(x**0.5)+1):
            if x%i==0:
                return False
                break
        return True
 
if prime(m):
    out = True
    for i in range(n+1, m):
        if prime(i):
            out = False
            break
    if out:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
