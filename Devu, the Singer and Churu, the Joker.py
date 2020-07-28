n,t = map(int, input().split())
a = list(map(int, input().split()))
z = t - (sum(a) + (n-1)*10)
 
if z>=0:
    out = z//5 + (n-1)*2
else:
    out = -1
 
print(out)
