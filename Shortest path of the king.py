p = ["a", "b", "c", "d", "e", "f", "g", "h"]
 
s = input()
t = input()
 
x_dif = p.index(t[0]) - p.index(s[0])
y_dif = int(t[1]) - int(s[1])
x,y = abs(x_dif), abs(y_dif)
count = (max(x,y))
print(count)
 
if x_dif < 0:
    hmove = "L"
else:
    hmove = "R"
if y_dif < 0:
    vmove = "D"
else:
    vmove = "U"
 
z = min(x,y)
for i in range(z):
    print(str(hmove) + str(vmove))
if y== count:
    for i in range(count-z):
        print(vmove)
else:
    for i in range(count-z):
        print(hmove)
