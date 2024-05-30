N, M = map(int, input().strip().split())
K = int(input().strip())
log = list(map(int, input().split()))[::-1]

hub = [(M * i) + 1 for i in range(N)]
hub_range = [(start, start + M - 1) for start in hub]

flag = True
for i in range(K - 1):
    if log[i] == 0:
        if log[i + 1] not in hub:
            flag = False
            break
    elif log[i + 1] == 0: 
        if log[i] not in hub:
            flag = False
            break
    elif log[i] in hub:
        end = M * ((log[i] // M) + 1)
        start = end - M + 1
        
        if 0 < log[i + 1] < start or log[i + 1] > end:
            flag = False
            break
    else:
        end = M * ((log[i] // M) + 1)
        start = end - M + 1
        
        if log[i + 1] < start or log[i + 1] > end:
            flag = False
            break

print('YES') if flag else print('NO')