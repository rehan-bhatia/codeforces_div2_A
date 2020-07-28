n = int(input())
a = list(map(int, input().split()))
x = sum(a)
n = n%x
if n!=0:
	i=0
	while n>0:
	    n -= a[i]
	    i+=1
	print(i)
else:
	for i in range(6,-1,-1):
		if a[i]!=0:
			print(i+1)
			break
