l, r = map(int, input().split())
if r-l <2:
    print(-1)
elif r-l==2:
    if l%2==1:
        print(-1)
    else:
        print(l, l+1, l+2)
else:
    if l%2==0:
        print(l, l+1,l+2)
    else:
        l+=1
        print(l, l+1,l+2)
