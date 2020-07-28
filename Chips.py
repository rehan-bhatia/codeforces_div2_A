n,m = map(int, input().split())
 
def summation(a):
    return (a*(a+1)//2)
 
x=[]
for i in range(n):
    x.append(summation(i+1))
m = m % x[-1]
if m==0:
    print(0)
else:
    for i in range(n):
        if x[i] > m:
            m -= x[i-1]
            break      
        elif x[i] == m:
            m = 0
            break
    print(m)
