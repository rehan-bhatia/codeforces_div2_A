n = int(input())
h,m=-1,-1
out = ""
for _ in range(n):
    a,b = map(int, input().split())
    if h==a and b==m:
        out = out + "1"
    else:
    	out = out + "0"
    h = a
    m = b
out = out.split("0")
maxm=0
for i in out:
	if len(i)>maxm:
		maxm = len(i)
print(maxm+1)
