n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = 1

flag = False
def dfs(graph, s):
    global flag
    if s == 1:
        flag = True
        return
    
    for e in range(n + 1):
        if graph[s][e] == 1 and s != e:
            dfs(graph, e)
            if flag : return

for e in range(n + 1):
    if graph[1][e] == 1 and e != 1:
        dfs(graph, e)
        if flag: break
        
print('YES') if flag else print('NO')