from collections import deque
now = int(input())
queue = deque([[now]])

cnt = 0
while True:
    now = queue.popleft()
    temp = []
    for item in now:
        if item % 5 == 0: temp.append(item // 5)
        if item % 3 == 0: temp.append(item // 3)
        if item % 2 == 0: temp.append(item // 2)
        temp.append(item - 1)

    cnt += 1
    if temp.count(1) > 0: break
    queue.append(temp)

print(cnt)