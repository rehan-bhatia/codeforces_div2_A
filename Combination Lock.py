n = int(input())
 
a = list(input())
b = list(input())
 
count = 0
for i in range(n):
    z = abs(int(a[i]) - int(b[i]))
    z = min(z, 10-z)
    count+=z
    
print(count)
