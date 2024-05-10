n = int(input())
m = int(input())
grid = [[0] * n for _ in range(n)]
min_time = float('inf')

for _ in range(m):
    start, end, time = map(int, input().split())
    grid[start - 1][end - 1] = time

def dfs(grid, start, end, time):
    global min_time
    if start == end :
        if min_time > time: min_time = time
        return

    for i in range(len(grid[start])):
        if grid[start][i] == 0: continue
        dfs(grid, i, end, time + grid[start][i])

start, end = map(int, input().split())
dfs(grid, start - 1, end - 1, 0)
print(min_time)