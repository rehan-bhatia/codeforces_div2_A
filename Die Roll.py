y,w = map(int, input().split())
a = max(y,w)
count=0
for i in range(6,0,-1):
    if a<=i:
        count+=1
if count==1:
    print("1/6")
elif count == 2:
    print("1/3")
elif count==3:
    print("1/2")
elif count==4:
    print("2/3")
elif count==5:
    print("5/6")
else:
    print("1/1")
