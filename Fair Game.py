n = int(input())
cards=[]
arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)
    if x not in cards:
        cards.append(x)
if len(cards)!=2:
    print("NO")
else:
    if arr.count(cards[0]) == arr.count(cards[1]):
        print("YES")
        print(cards[0], cards[1])
    else:
        print("NO")
