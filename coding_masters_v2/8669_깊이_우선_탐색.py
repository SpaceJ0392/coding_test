import sys
n, m = map(int, sys.stdin.readline().split())

visited = [False] * 1000
route = []
def dfs(graph, c):
    if graph.get(c) == None: return

    visited[c] = True
    print(c, end=' ')

    for next in graph[c]:
        if visited[next]: continue
        dfs(graph, next)
    

graph = {}
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)  

graph = {key: sorted(val) for key, val in graph.items()}

dfs(graph, 1)



# or 

def DFS(adj_list, visited, node):
    visited[node] = True
    print(node, end=" ")  # 현재 노드 출력
    for neighbor in sorted(adj_list[node]):  # 인접 노드를 작은 숫자부터 탐색
        if not visited[neighbor]:
            DFS(adj_list, visited, neighbor)

N, M = map(int, input().split())  # 정점의 개수 N과 간선의 개수 M 입력
adj_list = [[] for _ in range(N+1)]  # 인접 리스트 초기화

# 간선 정보 입력 및 인접 리스트 구성
for _ in range(M):
    A, B = map(int, input().split())
    adj_list[A].append(B)
    adj_list[B].append(A)  # 양방향 그래프이므로 반대 방향도 추가

visited = [False] * (N+1)  # 방문 여부를 저장할 리스트 초기화
DFS(adj_list, visited, 1)  # 정점 1부터 DFS 수행