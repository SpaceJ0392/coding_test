n = int(input())
ground = [input().split() for _ in range(n)]

for y in range(n):
    for x in range(n):
        if ground[y][x] == '2' and ('1' not in ground[y] or '1' not in [ground[y][x] for y in range(n)]):
            ground[y][x] = '0'

cnt = 0       
for y in range(n):
    for x in range(n):
        if ground[y][x] == '2':
            cnt += 1

print(cnt)