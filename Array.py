n = int(input())
s1, s2, s3 = [], [], []
for i in list(map(int, input().split())):
    if i<0:
        s1.append(i)
    elif i>0:
        s2.append(i)
    else:
        s3.append(i)
 
if len(s2)==0:
	for i in range(2):
		s2.append(s1[-1])
		s1.pop()
 
if len(s1)%2!=1:
	s3.append(s1[-1])
	s1.pop()
 
 
 
print(int(len(s1)), end=" ")
print(" ".join([str(i) for i in s1]))
print(int(len(s2)), end=" ")
print(" ".join([str(i) for i in s2]))
print(int(len(s3)), end=" ")
print(" ".join([str(i) for i in s3]))
