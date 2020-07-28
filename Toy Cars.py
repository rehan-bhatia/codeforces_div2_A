n = int(input())
count = 0
cars = []
for i in range(n):
    a = list(map(int, input().split()))
    if 1 not in a and 3 not in a:
        count += 1
        cars.append(str(i+1))
        
        
print(count)
print(" ".join(cars))
