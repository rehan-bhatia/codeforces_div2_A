n = int(input()) + 1
a = sum(list(map(int, input().split())))
count=0
if (a+1)%n != 1:
    count+=1
if (a+2)%n != 1:
    count+=1
if (a+3)%n != 1:
    count+=1
if (a+4)%n != 1:
    count+=1
if (a+5)%n != 1:
    count+=1
print(count)
