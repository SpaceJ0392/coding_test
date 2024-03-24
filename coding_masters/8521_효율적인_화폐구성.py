n, tot = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)

cnt = 0
for coin in coins:
    while tot >= coin:
        tot -= coin
        cnt += 1
 
if tot != 0:
    print(-1)
else:
    print(cnt)