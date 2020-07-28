x1, y1, x2, y2 = map(int, input().split())
if (x1 == x2):
    side = abs(y1 - y2)
    x3 = x1 + side
    x4 = x3
    y3 = y1
    y4 = y2
    print(x3, y3, x4, y4)
elif (y1 == y2):
    side = abs(x1 - x2)
    y3 = y1 + side
    y4 = y3
    x3 = x1
    x4 = x2
    print(x3, y3, x4, y4)
else:
    if abs(y2-y1) == abs(x2-x1):
        x3 = x1
        x4 = x2
        y3 = y2
        y4 = y1
        print(x3, y3, x4, y4)
    else:
        print(-1)
