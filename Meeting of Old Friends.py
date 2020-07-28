l1, r1, l2, r2, k = map(int, input().split())
l = max(l1, l2)
r = min (r1, r2)
t = r-l+1
if k>=l and k<=r:
    t-=1
if t<0:
    print(0)
else:
    print(t)
