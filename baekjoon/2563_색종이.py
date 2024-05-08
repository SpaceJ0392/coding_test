n = int(input())
zone = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for y_idx in range(y, y + 10): 
        for x_idx in range(x, x + 10): zone[y_idx][x_idx] = 1
        
cnt = 0
for y in zone:
    cnt += y.count(1)

print(cnt)