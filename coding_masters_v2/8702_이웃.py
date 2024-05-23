from collections import deque

# 입력 받기
n, m, k = map(int, input().split())
weights = [(idx, int(input())) for idx, _ in enumerate(range(n))]
graph = [[0] * n for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1][v - 1] = 1
    graph[v - 1][u - 1] = 1

def find_max_weight(weights, start):
    return max(weights[:-start], key= lambda x : x[1])

cost = 0
queue = deque([find_max_weight(weights, )])
visited = set()
while len(visited) != n and queue and weights:
    node, weight = queue.popleft()
    visited.add(node)

    for new_node, check in enumerate(graph[node]):
        if check != 0 and new_node not in visited:
            cost += (weight - weights[new_node][1] - k)
            weights[new_node] = (new_node, weight - k)

    next = find_max_weight(weights, len(visited))
    queue.append(next)

print(cost)
