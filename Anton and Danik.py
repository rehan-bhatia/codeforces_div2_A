n = int(input())
w = input()
a = w.count("A")
d = w.count("D")
if a>d:
    print("Anton")
elif a<d:
    print("Danik")
else:
    print("Friendship")
