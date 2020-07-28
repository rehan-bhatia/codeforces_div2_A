n = int(input())
s = list(map(int, input().split()))
if n==1:
	if 0 in s:
		print(0)
	else:
		print(1)
else:
	i=0
	while i<len(s) and s[i]==0:
		i+=1
	s = s[i:]
	if len(s)==0:
		print(0)
	else:
		i = len(s)-1
		while i>=0 and s[i]==0:
			i-=1
		s = s[:i+1]
		x = len(s)
		if x==0:
			print(0)
		else:
			s = [str(i) for i in s]
			s = "".join(s)
			s = s.split("1")
			count=0
			for i in s:
				if len(i) > 1:
					count+= len(i)
			print(x - count)
