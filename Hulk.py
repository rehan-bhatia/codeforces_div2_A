n = int(input())
x=""
for i in range(n):
    if i%2==0:
        x = x + "I hate that "
    else:
        x= x + "I love that "
x = x[:-5]
x = x + "it"
print(x)
