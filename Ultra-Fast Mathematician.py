a = input()
b = input()
out = ""
for i in range(len(a)):
    if a[i]==b[i]:
        out = out + "0"
    else:
        out = out + "1"
print(out)
