a,b = map(int, input().split())
x = b/a
count = 0
while x>=1:
    x=x/(3/2)
    count += 1
print(count)
