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
    if start == 0: return max(weights, key= lambda x : x[1])

    return max(weights[:-start], key= lambda x : (x[1], x[0]))

cost = 0
visited = set()
while len(visited) != m:
    node, weight = find_max_weight(weights, len(visited))
    visited.add(node)

    for new_node, check in enumerate(graph[node]):
        if check != 0 and new_node not in visited and (weight - weights[new_node][1]) > k:
            cost += (weight - weights[new_node][1] - k)
            weights[new_node] = (new_node, weight - k)

print(cost)
