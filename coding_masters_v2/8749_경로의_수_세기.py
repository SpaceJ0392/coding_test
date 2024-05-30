from collections import deque, defaultdict

def find_shortest_paths_count(n, k, edges):
    MOD = 1000000007

    # 그래프를 인접 리스트로 표현
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # BFS를 위한 큐와 최단 거리 및 경로 수를 저장할 배열 초기화
    queue = deque([1])
    dist = [-1] * (n + 1)  # 최단 거리를 저장하는 배열
    path_count = [0] * (n + 1)  # 경로 수를 저장하는 배열

    dist[1] = 0
    path_count[1] = 1

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            # 아직 방문하지 않은 노드라면
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                path_count[neighbor] = path_count[current]
                queue.append(neighbor)
            # 이미 방문한 노드인데 최단 거리가 같은 경우
            elif dist[neighbor] == dist[current] + 1:
                path_count[neighbor] = (path_count[neighbor] + path_count[current]) % MOD

    return path_count[n]

# 입력 받기
n, k = map(int, input().strip().split())
edges = [tuple(map(int, input().strip().split())) for _ in range(k)]

# 결과 출력
result = find_shortest_paths_count(n, k, edges)
print(result)
