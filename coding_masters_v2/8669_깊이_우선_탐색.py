import sys
n, m = map(int, sys.stdin.readline().split())

visited = [False] * 1000
visited[1] = True

route = [1]
def dfs(graph, c):
    if graph.get(c) == None: return

    for next in graph[c]:
        if visited[next]: continue

        visited[next] = True
        route.append(next)
        dfs(graph, next)
    

graph = {}
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph.setdefault(a, []).append(b)  

graph = {key: sorted(val) for key, val in graph.items()}

dfs(graph, 1)
print(*route)