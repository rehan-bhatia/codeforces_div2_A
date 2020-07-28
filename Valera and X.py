n = int(input())
out = True
letters = []
for i in range(n):
    x = input()
    a = list(set(list(x)))
    if len(a)==2:
    	if len(letters)==0:
    		letters = [a[0],a[1]]
    	if a[0] not in letters or a[1] not in letters:
    		out = False
    	else:
	    	if i==n//2:
	    		if x.count(a[0])==1:
	    			if x[i]!=a[0]:
	    				out = False
	    		elif x.count(a[1])==1:
	    			if x[i]!=a[1]:
	    				out = False
	    		else:
	    			out = False
	    	else:
		        if x.count(a[0])==2:
		            if x[i]!=a[0] or x[-1-i]!=a[0]:
		            	out = False
		        elif x.count(a[1])==2:
		            if x[i]!=a[1] or x[-1-i]!=a[1]:
		                out = False
		        else:
		            out = False
    if len(a)!=2:
    	out = False
if out:
    print("YES")
else:
    print("NO")
