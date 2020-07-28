def f(x):
    return x*(x+1)//2
 
n = int(input())
i=0
while n>=0:
    n -= f(i+1)
    i+=1
print(i-1
