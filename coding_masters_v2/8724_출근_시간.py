import heapq

def dijkstra(start, n, graph):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def find_minimum_travel_time(N, M, K, roads):
    graph = [[] for _ in range(N + 1)]
    
    for u, v, w in roads:
        graph[u].append((v, w))
    
    dist_from_home = dijkstra(1, N, graph)
    dist_from_school = dijkstra(K, N, graph)
    
    if dist_from_home[K] == float('inf') or dist_from_school[N] == float('inf'):
        return -1
    
    return dist_from_home[K] + dist_from_school[N]

# 입력 받기
N, M, K = map(int, input().strip().split())
roads = [tuple(map(int, input().strip().split())) for _ in range(M)]

# 결과 출력
print(find_minimum_travel_time(N, M, K, roads))
