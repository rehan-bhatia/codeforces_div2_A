n = int(input())
arr = list(map(int, input().split()))
x,y = min(arr), max(arr)
if arr.index(x)==0 or arr.index(y)==0 or arr.index(x)==n-1 or arr.index(y)==n-1:
	print(n-1)
elif arr.index(x) < arr.index(y):
    print(max(n-1 - arr.index(x), arr.index(y)))
elif arr.index(x) > arr.index(y):
    print(max(n-1 - arr.index(y), arr.index(x)))
