a = input()
t = ["a","e","i","o","u", "y"]
out = ""
for i in a:
    z = i.lower()
    if z not in t:
        out = out + "." + z
print(out)
