from collections import deque

queue = deque([(0, int(input()))])
visited = set()
lev = 0
flag = False

while queue:
    lev, data = queue.popleft()

    if data < 0:
        break

    if data == 1:
        flag = True
        break

    lev += 1
    if data % 2 == 0 and data // 2 not in visited:
        queue.append((lev, data // 2))
        visited.add(data // 2)
    if data % 3 == 0 and data // 3 * 2 not in visited:
        queue.append((lev, data // 3 * 2))
        visited.add(data // 3 * 2)
    if data % 5 == 0 and data // 5 * 4 not in visited:
        queue.append((lev, data // 5 * 4))
        visited.add(data // 5 * 4)


print(lev) if flag else print(-1)
