x = input()
a = str(x.count("4") + x.count("7"))
 
z = list(set(list(a)))
if len(z)==2:
    if "4" in z and "7" in z:
        print("YES")
    else:
        print("NO")
elif len(z)==1:
    if "4" in z or "7" in z:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
