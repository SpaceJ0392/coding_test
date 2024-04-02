t = int(input())
coin = [25, 10, 5, 1]

rest = [[0] * 4 for i in range(t)]
for y in range(t):
    money = int(input())    
    x = 0
    while money != 0:
        rest[y][x] = money // coin[x]
        money %= coin[x]
        x += 1

for i in range(t):    
    print(*rest[i])