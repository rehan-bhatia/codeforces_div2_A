n,v = map(int, input().split())
sellers=[]
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(x[0]):
        if x[j+1] < v:
            sellers.append(i)
            break
print(len(sellers))
for i in sellers:
    print(str(i+1), end=" ")
