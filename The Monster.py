def gcd(x,y):
    while(y):
        x,y = y, x%y
    return x
a,b = map(int, input().split())
c,d = map(int, input().split())
y = d-b
z = gcd(a,c)
x= abs(y)%z
if x==0:
    p,q = 0,0
    while (p*a - q*c) != y:
        if (p*a - q*c) > y:
            q +=1
        else:
            p+=1
    print((p*a)+b)
else:
    print(-1)
