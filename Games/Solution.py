n = int(input())
jerseys = []
for _ in range(n):
    jerseys.append([int(i) for i in input().split()])
count=0
for i in range(n):
    for j in range(n):
        if i!=j:
            if jerseys[i][0] == jerseys[j][1]:
                count+=1
print(count)
