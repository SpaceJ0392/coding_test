'''
10
1 2 3 1 2 7 1 2 10 9
'''

n = int(input())
shark = list(map(int, input().split()))

max_cnt= 1
for i in range(n - 1):
    cnt, max_shark = 1, shark[i]
    for j in range(i + 1, n):
        if max_shark < shark[j]: 
            cnt += 1
            max_shark = shark[j]
            
    if max_cnt < cnt: max_cnt = cnt

print(max_cnt)