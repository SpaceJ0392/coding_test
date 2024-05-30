import itertools

def calculate_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_min_delivery_time(N, K, houses):
    # 식당 A의 위치
    start = (1, 1)
    
    # 모든 집들의 순열 중 K개씩 조합을 생성
    permutations = list(itertools.permutations(houses, K))
    
    min_time = float('inf')
    
    for perm in permutations:
        # 현재 순열의 경로를 따라 거리를 계산
        time = 0
        current_pos = start
        
        for house in perm:
            time += calculate_distance(current_pos[0], current_pos[1], house[0], house[1])
            current_pos = house
        
        # 마지막 집에서 다시 식당으로 돌아가는 거리 추가
        time += calculate_distance(current_pos[0], current_pos[1], start[0], start[1])
        
        # 최소 시간 갱신
        if time < min_time:
            min_time = time
    
    return min_time

# 입력 받기
N, K = map(int, input().split())
houses = []
for _ in range(N):
    x, y = map(int, input().split())
    houses.append((x, y))

# 결과 출력
print(find_min_delivery_time(N, K, houses))
