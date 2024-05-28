# from collections import deque

# # 입력 받기
# n, m, k = map(int, input().split())
# weights = [(idx, int(input())) for idx, _ in enumerate(range(n))]
# graph = [[0] * n for _ in range(n)]

# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u - 1][v - 1] = 1
#     graph[v - 1][u - 1] = 1

# def find_max_weight(weights, start):
#     if start == 0: return max(weights, key= lambda x : x[1])

#     return max(weights[:-start], key= lambda x : (x[1], x[0]))

# cost = 0
# visited = set()
# while len(visited) != m:
#     node, weight = find_max_weight(weights, len(visited))
#     visited.add(node)

#     for new_node, check in enumerate(graph[node]):
#         if check != 0 and new_node not in visited and (weight - weights[new_node][1]) > k:
#             cost += (weight - weights[new_node][1] - k)
#             weights[new_node] = (new_node, weight - k)

# print(cost)

import heapq

N, M, K = map(int, input().split())
weight_node, weights = {}, []
for node, _ in enumerate(range(N)):
    weight = int(input())
    weights.append((-weight, node))
    weight_node[node] = weight

heapq.heapify(weights)

edges = {}
for _ in range(M):
    start, end = map(int, input().split())
    edges.setdefault(start - 1, set()).add(end - 1)
    edges.setdefault(end - 1, set()).add(start - 1)

cost = 0
visited = set()
while weights:
    now_weight, now_node = heapq.heappop(weights)
    
    if now_node in visited: continue
    visited.add(now_node)
    
    for next_node in edges[now_node]:
        loss = (-now_weight - weight_node[next_node])
        
        if next_node not in visited and loss > K:
            cost += (loss - K)
            weight_node[next_node] = -now_weight - K
            heapq.heappush(weights, (-weight_node[next_node], next_node))

print(cost)
