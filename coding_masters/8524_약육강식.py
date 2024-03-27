n = int(input())
shark = list(map(int, input().split()))

max_cnt, cnt = 1, 1
temp = []
for i in range(n - 1):
    if shark[i] < shark[i + 1]:
        cnt += 1
    else:
        temp.append(shark[i])
        cnt = 1
    
    if max_cnt <= cnt : max_cnt = cnt

if temp[-1] < shark[-1]:
    temp.append(shark[-1])

print(max(max_cnt, len(temp)))