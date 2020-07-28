n = int(input())
def lucky(n):
    x = list(set(list(n)))
    if len(x)>2:
        return False
    elif len(x)==2:
        if x!=["4","7"] and x!=["7", "4"]:
            return False
        else:
            return True
    else:
        if "7" in x or "4" in x:
            return True
        else:
            return False
 
a = input()
if lucky(a):
    x = [int(i) for i in a[:n//2]]
    y = [int(i) for i in a[n//2:]]
    if sum(x) == sum(y):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
    
    
 
 #Other way to define lucky()
 
 def lucky(n):
  if n.count("4") + n.count("7") == len(n):
    return True
  else:
    return False
