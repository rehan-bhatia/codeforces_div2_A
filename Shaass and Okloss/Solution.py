n = int(input())
z = list(map(int, input().split()))
m = int(input())
if m==0:
	for i in z:
		print(i)
elif n==1:
	a = input()
	print(0)
else:
	for _ in range(m):
	    wire, bird = map(int, input().split())
	    if wire==1:
	        z[wire] += z[wire-1] - bird
	        z[wire-1] = 0
	    elif wire ==n:
	        z[wire - 2] += bird - 1
	        z[wire-1] = 0 
	    else:
	        z[wire] += z[wire-1] - bird
	        z[wire-2] += bird - 1
	        z[wire - 1] = 0
	for i in z:
	    print(i)
