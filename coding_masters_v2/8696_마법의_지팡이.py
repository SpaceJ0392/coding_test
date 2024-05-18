from collections import deque

queue = deque([(0, int(input()))])
visited = set()
lev = 0
flag = False

while queue:
    lev, data = queue.popleft()

    

    if data == 1:
        flag = True
        break

    lev += 1
    if data % 2 == 0:
        ndata = data // 2
        if ndata < 1: break
        queue.append((lev, ndata))
    if data % 3 == 0:
        ndata = data // 3 * 2
        if data < 1: break
        queue.append((lev, ndata))
    if data % 5 == 0:
        ndata = data //5 * 4
        if data < 1: break
        queue.append((lev, ndata))


print(lev) if flag else print(-1)
