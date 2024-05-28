land = list(input())

min_cnt = 0
for i in range(1, len(land) - 1):
    left, now, right = land[i - 1], land[i], land[i + 1]
    if now == 'g'  and left != 'g' : min_cnt += 1

max_cnt = 0
for i in range(1, len(land) - 1):
    left, now, right = land[i - 1], land[i], land[i + 1]
    
    if now == 'x' and left != 'g' and right != 'g':
        land[i] = 'g'
        max_cnt += 1
    if now == 'g' and left != 'g': max_cnt += 1

print(min_cnt, max_cnt, sep='\n')