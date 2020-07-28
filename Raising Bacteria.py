n = int(input())
out=1
while n>1:
    if n%2==1:
        out+=1
        n-=1
    n=n//2
print(out)
