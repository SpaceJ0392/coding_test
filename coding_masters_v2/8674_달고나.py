cols, rows = map(int,input().split())
grid = [list(input()) for _ in range(cols)]
visited = [[False] * rows for _ in range(cols)]

def dfs(grid, ny, nx, cols, rows):

    visited[ny][nx] = True
    dir = [(-1,0), (1,0), (0,-1), (0,1)]

    for dy, dx in dir:
        if 0 <= ny + dy < cols and 0 <= nx + dx < rows \
            and visited[ny + dy][nx + dx] == False and grid[ny + dy][nx + dx] == '0':
            dfs(grid, ny + dy, nx + dx, cols, rows)


cnt = 0
for y in range(cols):
    for x in range(rows):
        if grid[y][x] == '0' and visited[y][x] == False:
            dfs(grid, y, x, cols, rows)
            cnt += 1    

print(cnt)