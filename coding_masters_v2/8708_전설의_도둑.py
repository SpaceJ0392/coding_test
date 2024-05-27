# from collections import deque

# now, target = map(int, input().split())
# path = deque([(0, now)])
# visited = [now]

# min_lev = 0
# if now < target:
#     while True:
#         lev, now = path.popleft()

#         if now == target:
#             min_lev = lev
#             break
        
#         if now * 2 not in visited:
#             visited.append(now * 2)
#             path.append((lev + 1, now * 2))
#         if now + 3 not in visited:
#             visited.append(now + 3)
#             path.append((lev + 1, now + 3))
#         if now - 1 not in visited:
#             visited.append(now - 1)
#             path.append((lev + 1, now - 1))
# else:
#     min_lev = now - target

# print(min_lev)

import heapq

def min_warp_count(K, N):
    if K == N:
        return 0
    
    # 우선순위 큐 초기화
    pq = [(0, K)]  # (현재까지의 워프 횟수, 현재 위치)
    distances = {i: float('inf') for i in range(100001)}
    distances[K] = 0
    
    while pq:
        current_warps, current_position = heapq.heappop(pq)
        
        if current_position == N:
            return current_warps
        
        # 다음 위치들을 확인
        next_positions = [(current_position + 3, current_warps + 1), 
                          (current_position - 1, current_warps + 1), 
                          (current_position * 2, current_warps + 1)]
        
        for next_position, next_warps in next_positions:
            if 0 <= next_position <= 100000 and next_warps < distances[next_position]:
                distances[next_position] = next_warps
                heapq.heappush(pq, (next_warps, next_position))

# 입력
K, N = map(int, input().strip().split())

# 출력
print(min_warp_count(K, N))
