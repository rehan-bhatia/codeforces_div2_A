n = int(input())
count=0
for _ in range(n):
    a = sum(list(map(int, input().split())))
    if a>=2:
        count+=1
print(count)
