n = int(input())
a = list(map(int, input().split()))
 
def gcd(a,b):
    while (b):
        a,b = b, a%b
    return a
 
x = gcd(a[0], a[1])
 
for i in range(2, n):
    x = gcd(x, a[i])
 
print(x*n)
