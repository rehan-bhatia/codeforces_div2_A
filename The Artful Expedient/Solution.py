#Actual implementation solution

N = input()
left = list(map(int, input().split()))
right = list(map(int, input().split()))
numbers = set(left + right)
 
xors = sum(l ^ r in numbers for l in left for r in right)
print("Koyomi" if xors % 2 else "Karen")


#Trick solution :p
print("Karen")
