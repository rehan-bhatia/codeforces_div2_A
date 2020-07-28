t,s,x = map(int, input().split())
if x<t:
    print("NO")
elif x==t:
    print("YES")
else:
    x -= t
    if x<s:
        print("NO")
    else:
        if x%s == 0 or x%s == 1:
            print("YES")
        else:
            print("NO")
