p, r = map(int, input().split())
i = 1
while (p*i)%10 != r and (p*i)%10 != 0:
    i+=1
print(i)
