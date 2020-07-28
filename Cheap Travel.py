n,m,a,b = map(int, input().split())
if a <= b/m:
    print(n*a)
else:
    x = n//m
    if n%m==0:
        print(b*x)
    else:
        if a*(n%m) < b:
            print(b*x + a*(n%m))
        else:
            print(b* (x+1))
