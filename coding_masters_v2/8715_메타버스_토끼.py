from collections import deque

n, m = map(int, input().split())
game_map = [list(input()) for _ in range(n)]
move = [(1,0), (0,1), (0,-1), (-1,0)]

queue = deque([(0, n-1, m-1)])
visited = {(n-1, m-1)}
ans = -1

while queue:
    lev, y, x = queue.popleft()
    if y == 0 and x == 0: 
        ans = lev
        break
    
    for dy, dx in move:
        for step in range(1, 3): # 2번 수행
            if 0 <= y + dy * step < n and 0 <= x + dx * step < m \
                and game_map[y + dy * step][x + dx * step] != '#' and (y + dy * step, x + dx * step) not in visited:
                    
                    if step == 2: queue.pop()
                        
                    visited.add((y + dy * step, x + dx * step))
                    queue.append((lev + 1, y + dy * step, x + dx * step))
            else: break

print(ans)
