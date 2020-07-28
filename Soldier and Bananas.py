k, n, w = map(int, input().split())
w = k*w*(w+1)//2
if w < n:
    print(0)
else:
    print(w - n)
