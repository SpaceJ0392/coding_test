n, k = map(int, input().split())
hole = sorted(list(map(int, input().split())))

now, cnt = 0, 0
for h in hole:
    if now < h: 
        now = (h + k) - 1
        cnt += 1

print(cnt)


