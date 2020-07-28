a = input()
b = input()
c = str(int(a) + int(b))
c = "".join(c.split("0"))
c = int(c)
a = "".join(a.split("0"))
b = "".join(b.split("0"))
d = int(a) + int(b)
if c==d:
    print("YES")
else:
    print("NO")
