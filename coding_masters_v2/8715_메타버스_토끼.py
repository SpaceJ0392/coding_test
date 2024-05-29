from collections import deque

n, m = map(int, input().split())
game_map = [list(input()) for _ in range(n)]
move = [(1,0), (0,1), (0,-1), (-1,0)]

queue = deque([(0, n-1, m-1)])
visited = {(n-1, m-1)}
ans = -1

while queue:
    minute, y, x = queue.popleft()
    if y == 0 and x == 0: 
        ans = minute
        break
    
    for dy, dx in move:
        for step in range(1, 3): # 2번 수행
            ny, nx = y + dy * step, x + dx * step
            if 0 <= ny < n and 0 <= nx < m and game_map[ny][nx] != '#' and (ny, nx) not in visited:    
                
                if step == 2: queue.pop()
                        
                visited.add((ny, nx))
                queue.append((minute + 1, ny, nx))
            else: break

print(ans)
